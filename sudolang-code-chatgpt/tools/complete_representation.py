"""Structural SudoLang rendering of the supplied runtime, with exact expression evidence.

No harness imports, scans, model calls, or shell probes are executed. Every Python
statement kind must be handled explicitly; unsupported syntax stops generation.
This tool supplies the detailed layer, not a claim of human semantic proof.
"""
from __future__ import annotations

import ast
import csv
import hashlib
import io
import json
import re
import tokenize
from collections import Counter, defaultdict
from pathlib import Path

OUT = Path(__file__).resolve().parents[1]
SRC = OUT.parent / "visa-vulnerability-agentic-harness"
DETAIL = OUT / "source_detail"


def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def dump(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def tsv(path, fields, rows):
    with path.open("w", newline="") as f:
        w = csv.writer(f, delimiter="\t")
        w.writerow(fields)
        w.writerows(rows)


def cell(x):
    return str(x).replace("|", "&#124;").replace("\n", " ").replace("`", "&#96;")


def module_name(rel):
    if rel.startswith("vvaharness/"):
        name = rel[:-3].replace("/", ".")
    elif rel.startswith("vendor/context_graph_sdk/src/"):
        name = rel[len("vendor/context_graph_sdk/src/"):-3].replace("/", ".")
    else:
        return None
    return name.removesuffix(".__init__")


class Render:
    simple = (ast.Assign, ast.AnnAssign, ast.AugAssign, ast.Expr, ast.Import,
              ast.ImportFrom, ast.Global, ast.Nonlocal, ast.Delete, ast.Pass)

    def __init__(self, rel, text, modules, *, source_text=None, line_offset=0):
        self.rel, self.text, self.modules = rel, source_text if source_text is not None else text, modules
        self.tree = ast.parse(text)
        if line_offset:
            ast.increment_lineno(self.tree, line_offset)
        self.lines, self.records, self.calls, self.symbols = [], [], [], {}
        self.literals, self.imports, self.links = {}, [], []
        self.expressions = []
        self.parents = {}
        for parent in ast.walk(self.tree):
            for child in ast.iter_child_nodes(parent):
                self.parents[child] = parent
        self.joined_constants = {id(c) for n in ast.walk(self.tree) if isinstance(n, ast.JoinedStr)
                                 for c in n.values if isinstance(c, ast.Constant)}
        self.identifiers = defaultdict(list)
        for n in ast.walk(self.tree):
            if isinstance(n, ast.Name): self.identifiers[n.id].append(n)
            if isinstance(n, ast.Attribute): self.identifiers[n.attr].append(n)
            if isinstance(n, ast.arg): self.identifiers[n.arg].append(n)
            if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                self.identifiers[n.name].append(n)
            if isinstance(n, ast.keyword) and n.arg: self.identifiers[n.arg].append(n)
            if isinstance(n, ast.alias):
                name = n.asname or n.name.split('.')[0]
                if name != '*': self.identifiers[name].append(n)
            if isinstance(n, ast.ExceptHandler) and n.name:
                self.identifiers[n.name].append(n)
            if isinstance(n, (ast.Global, ast.Nonlocal)):
                for name in n.names: self.identifiers[name].append(n)
            if isinstance(n, ast.Constant) and isinstance(n.value, str) and re.fullmatch(r"(?:--)?[A-Za-z_]\w*(?:[.:-][\w-]+)*", n.value):
                self.identifiers[n.value].append(n)
        for n in ast.walk(self.tree):
            if isinstance(n, (ast.Import, ast.ImportFrom)):
                self.imports.append(self.import_record(n))
            if isinstance(n, ast.Call):
                self.calls.append({"line": n.lineno, "end_line": n.end_lineno,
                                   "callee": ast.unparse(n.func), "enclosing": self.owner(n),
                                   "expression": ast.get_source_segment(self.text, n)})

    def owner(self, node):
        names = []
        while node in self.parents:
            node = self.parents[node]
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                names.append(node.name)
        return ".".join(reversed(names)) or "module initialization"

    def import_record(self, node):
        if isinstance(node, ast.Import):
            targets = [x.name for x in node.names]
        else:
            base = node.module or ""
            if node.level:
                mod = module_name(self.rel) or ""
                package = mod if self.rel.endswith("__init__.py") else mod.rpartition(".")[0]
                parts = package.split(".")
                base = ".".join(parts[:len(parts) - node.level + 1] + ([base] if base else []))
            targets = [base] + [base + "." + x.name for x in node.names if x.name != "*"]
        local = sorted({self.modules[t] for t in targets if t in self.modules})
        return {"line": node.lineno, "source_expression": ast.unparse(node), "targets": targets,
                "local_source_paths": local,
                "boundary": "local definition linked" if local else "external/standard-library import; see dependency_boundaries.md"}

    def emit(self, level, text):
        self.lines.append("  " * level + text)

    def cite(self, node, level, end=None):
        start, finish = node.lineno, end or node.end_lineno
        self.emit(level, f"// Source: {self.rel}:{start}-{finish}")
        self.links.append([self.rel, start, finish, len(self.lines)])

    def literal(self, n):
        # The name is converter vocabulary, not a harness variable or language keyword.
        key = f"source_literal_{n.lineno}_{n.col_offset}"
        if key not in self.literals:
            self.literals[key] = {"source": self.rel, "line_start": n.lineno,
                                  "line_end": n.end_lineno, "value": n.value,
                                  "meaning": "exact source string constant; inert unless passed to an executable API"}
        return key

    def expr(self, node):
        renderer = self
        class Literals(ast.NodeTransformer):
            def visit_Constant(self, n):
                if isinstance(n.value, str) and (len(n.value) > 120 or "\n" in n.value):
                    return ast.copy_location(ast.Name(id=renderer.literal(n), ctx=ast.Load()), n)
                return n
            def visit_JoinedStr(self, n):
                # Preserve complete format syntax and evaluation order as source evidence.
                key = f"source_template_{n.lineno}_{n.col_offset}"
                renderer.literals[key] = {"source": renderer.rel, "line_start": n.lineno,
                    "line_end": n.end_lineno, "source_expression": ast.get_source_segment(renderer.text, n),
                    "meaning": "evaluate this source f-string at its original call site; not a frozen output"}
                return ast.copy_location(ast.Name(id=key, ctx=ast.Load()), n)
        # Reparse an isolated AST copy to keep original nodes/locations unmodified.
        import copy
        transformed = Literals().visit(copy.deepcopy(node))
        rendered = ast.unparse(ast.fix_missing_locations(transformed))
        self.expressions.append({"line_start": node.lineno, "line_end": node.end_lineno,
                                 "column": node.col_offset, "kind": type(node).__name__,
                                 "original_ast": ast.dump(node, include_attributes=False),
                                 "rendered": rendered})
        return rendered

    def simple_text(self, n):
        if isinstance(n, ast.Assign):
            return "Evaluate once " + self.expr(n.value) + "; assign in source target order to " + ", ".join(ast.unparse(t) for t in n.targets) + "."
        if isinstance(n, ast.AnnAssign):
            value = "declare without assigning a value" if n.value is None else "assign " + self.expr(n.value)
            return f"For {ast.unparse(n.target)}, {value}; source annotation {ast.unparse(n.annotation)}."
        if isinstance(n, ast.AugAssign):
            return "Apply source augmented assignment " + self.expr(n) + " with source evaluation/in-place semantics."
        if isinstance(n, ast.Expr):
            if isinstance(n.value, ast.Constant) and isinstance(n.value.value, str):
                return "Retain source documentation literal " + self.literal(n.value) + "; it is not a model call."
            if isinstance(n.value, ast.Yield):
                return "Yield " + (self.expr(n.value.value) if n.value.value else "None") + "; suspend this generator until resumed."
            if isinstance(n.value, ast.YieldFrom):
                return "Delegate generator iteration, sends and exceptions to " + self.expr(n.value.value) + "."
            return "Evaluate " + self.expr(n.value) + "; retain side effects and discard the expression result."
        if isinstance(n, (ast.Import, ast.ImportFrom)):
            return "Resolve source import " + ast.unparse(n) + "; preserve alias and import-time effects."
        if isinstance(n, ast.Global): return "Bind names in module scope: " + ", ".join(n.names) + "."
        if isinstance(n, ast.Nonlocal): return "Bind names in enclosing nonlocal scope: " + ", ".join(n.names) + "."
        if isinstance(n, ast.Delete): return "Delete source targets in order: " + ", ".join(ast.unparse(t) for t in n.targets) + "."
        if isinstance(n, ast.Pass): return "Perform no operation at this source statement."
        raise TypeError(type(n).__name__)

    def block(self, body, level):
        i = 0
        while i < len(body):
            n = body[i]
            if isinstance(n, self.simple):
                group = []
                while i < len(body) and isinstance(body[i], self.simple) and len(group) < 5:
                    group.append(body[i]); i += 1
                self.cite(group[0], level, group[-1].end_lineno)
                rendered = []
                for item in group:
                    self.records.append(self.record(item))
                    rendered.append(self.simple_text(item))
                self.emit(level, "In source order: " + " Then ".join(rendered))
                continue
            self.stmt(n, level)
            i += 1

    def record(self, n):
        return {"kind": type(n).__name__, "line_start": n.lineno, "line_end": n.end_lineno,
                "column": n.col_offset, "owner": self.owner(n), "representation_line": len(self.lines) + 1}

    def stmt(self, n, level):
        self.records.append(self.record(n)); self.cite(n, level)
        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)):
            if n.decorator_list:
                self.cite(n.decorator_list[0], level, n.decorator_list[-1].end_lineno)
                self.emit(level, "Before creating this callable, evaluate and retain decorators top-to-bottom: " + ", ".join(self.expr(x) for x in n.decorator_list) + ".")
                self.cite(n, level)
            signature = ast.unparse(n.args)
            self.emit(level, "// Source signature: " + n.name + "(" + signature + ")" + (" -> " + ast.unparse(n.returns) if n.returns else ""))
            self.emit(level, "Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.")
            args = [a.arg for a in [*n.args.posonlyargs, *n.args.args, *n.args.kwonlyargs]]
            if n.args.vararg: args.append(n.args.vararg.arg)
            if n.args.kwarg: args.append(n.args.kwarg.arg)
            self.emit(level, f"fn {n.name}({', '.join(args)}) {{")
            self.emit(level + 1, "Bind arguments/defaults/annotations exactly as the source signature specifies.")
            if isinstance(n, ast.AsyncFunctionDef): self.emit(level + 1, "This callable produces a coroutine or async generator; await/suspension positions remain in source expressions.")
            self.block(n.body, level + 1)
            self.emit(level + 1, "If execution reaches this end, finish with the source implicit None result.")
            self.emit(level, "}")
            if n.decorator_list:
                self.emit(level, "At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.")
        elif isinstance(n, ast.ClassDef):
            if n.decorator_list:
                self.cite(n.decorator_list[0], level, n.decorator_list[-1].end_lineno)
                self.emit(level, "Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: " + ", ".join(self.expr(x) for x in n.decorator_list) + ".")
                self.cite(n, level)
            self.emit(level, f"interface {n.name} {{")
            bases = [self.expr(x) for x in n.bases] + [self.expr(x) for x in n.keywords]
            self.emit(level + 1, "Describe the source Python type, preserving its base/metaclass expression order: " + (", ".join(bases) or "implicit object") + ".")
            self.emit(level + 1, "Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.")
            self.block(n.body, level + 1); self.emit(level, "}")
            if n.decorator_list: self.emit(level, "Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.")
        elif isinstance(n, ast.If):
            self.emit(level, "if (the source predicate " + self.expr(n.test) + " is truthy) {")
            self.block(n.body, level + 1); self.emit(level, "}")
            if n.orelse:
                self.emit(level, "else {"); self.block(n.orelse, level + 1); self.emit(level, "}")
        elif isinstance(n, (ast.For, ast.AsyncFor)):
            if isinstance(n, ast.AsyncFor): self.emit(level, "Obtain/advance the following source async iterator by awaiting, without inventing parallel dispatch.")
            self.emit(level, "for each " + ast.unparse(n.target) + " in " + self.expr(n.iter) + " {")
            self.block(n.body, level + 1); self.emit(level, "}")
            if n.orelse:
                self.emit(level, "Only on normal iterator exhaustion, with no break from this loop {")
                self.block(n.orelse, level + 1); self.emit(level, "}")
        elif isinstance(n, ast.While):
            self.emit(level, "while (the source predicate " + self.expr(n.test) + " is truthy) {")
            self.block(n.body, level + 1); self.emit(level, "}")
            if n.orelse:
                self.emit(level, "Only when the condition becomes false, with no break from this loop {")
                self.block(n.orelse, level + 1); self.emit(level, "}")
        elif isinstance(n, ast.Try):
            self.emit(level, "Perform the following protected operations {")
            self.block(n.body, level + 1); self.emit(level, "}")
            for handler in n.handlers:
                self.cite(handler, level)
                condition = self.expr(handler.type) if handler.type else "any raised exception"
                binding = " as " + handler.name if handler.name else ""
                self.emit(level, "On the first matching source exception " + condition + binding + ", in handler order {")
                self.block(handler.body, level + 1); self.emit(level, "}")
            if n.orelse:
                self.emit(level, "Only when the protected body falls through normally, without exception, return, break or continue {")
                self.block(n.orelse, level + 1); self.emit(level, "}")
            if n.finalbody:
                self.emit(level, "On every exit from this protected/handler/normal-completion region {")
                self.block(n.finalbody, level + 1); self.emit(level, "}")
        elif isinstance(n, (ast.With, ast.AsyncWith)):
            items = [self.expr(x.context_expr) + (" bound to " + ast.unparse(x.optional_vars) if x.optional_vars else "") for x in n.items]
            self.emit(level, ("Await and enter" if isinstance(n, ast.AsyncWith) else "Enter") + " source context managers left-to-right: " + "; ".join(items) + " {")
            self.block(n.body, level + 1); self.emit(level, "}")
            self.emit(level, "Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics" + (" and await async exits." if isinstance(n, ast.AsyncWith) else "."))
        elif isinstance(n, ast.Return):
            self.emit(level, "End this invocation with " + (self.expr(n.value) if n.value else "None") + ".")
        elif isinstance(n, ast.Raise):
            self.emit(level, "Raise " + (self.expr(n.exc) if n.exc else "the currently handled exception") + (" with explicit source cause " + self.expr(n.cause) if n.cause else "") + ".")
        elif isinstance(n, ast.Continue): self.emit(level, "Continue the immediately enclosing source loop at its next iteration.")
        elif isinstance(n, ast.Break): self.emit(level, "Leave the immediately enclosing source loop, skipping its normal-exhaustion body.")
        elif isinstance(n, ast.Assert): self.emit(level, "Enforce source assert " + self.expr(n.test) + (" with message " + self.expr(n.msg) if n.msg else "") + "; retain Python optimization-dependent assert behavior.")
        else: raise TypeError(f"Unsupported statement {type(n).__name__} in {self.rel}:{n.lineno}")

    def render(self, evidence_path=None):
        self.block(self.tree.body, 0)
        header = [f"# {self.rel}", "", "Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.",
                  "Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.",
                  "Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.",
                  "Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.", "",
                  f"Evidence: `{evidence_path or ('assets/' + self.rel + '.evidence.json')}`. SHA-256: `{hashlib.sha256(self.text.encode()).hexdigest()}`.", "",
                  "```sudo", *self.lines, "```", "", "## Local import links", ""]
        for imp in self.imports:
            for local in imp["local_source_paths"]:
                header.append(f"- `{imp['source_expression']}` at source line {imp['line']}: `source_detail/{local}.sudo.md`.")
        if not any(i["local_source_paths"] for i in self.imports): header.append("No statically resolved in-checkout import; external calls remain explicit dependency boundaries.")
        return "\n".join(header) + "\n"

    def vocabulary_rows(self, destination):
        """Keep distinct lexical scopes and symbol roles separate, with actual use sites."""
        groups = defaultdict(list)
        def scope_of(node):
            scopes = []
            parent = self.parents.get(node)
            while parent is not None:
                if isinstance(parent, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                    scopes.append(f"{parent.name}@{parent.lineno}")
                elif isinstance(parent,(ast.Lambda,ast.ListComp,ast.SetComp,ast.DictComp,ast.GeneratorExp)):
                    scopes.append(f"{type(parent).__name__}@{parent.lineno}:{parent.col_offset}")
                parent = self.parents.get(parent)
            return '.'.join(reversed(scopes)) or 'module'
        def role_of(node):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)): return 'callable'
            if isinstance(node, ast.ClassDef): return 'source type'
            if isinstance(node, ast.arg): return 'parameter'
            if isinstance(node, ast.alias): return 'import binding'
            if isinstance(node, ast.Attribute): return 'source member reference'
            if isinstance(node, ast.keyword): return 'call keyword'
            if isinstance(node, ast.Constant): return 'source string key/name/status'
            if isinstance(node, ast.ExceptHandler): return 'exception binding'
            return 'source binding/reference'
        for name, nodes in self.identifiers.items():
            for node in nodes:
                # Distinguish receiver.member from unrelated objects' same-spelled fields.
                identifier = ast.unparse(node) if isinstance(node, ast.Attribute) else name
                groups[(scope_of(node), identifier, role_of(node))].append(node)
        record_lines = {(r['kind'], r['line_start'], r['column']): r['representation_line'] for r in self.records}
        # The fixed preamble precedes the first fenced source line; do not execute source.
        fence_offset = destination.read_text().splitlines().index('```sudo') + 1
        result = []
        for (scope, identifier, role), nodes in sorted(groups.items()):
            node = min(nodes, key=lambda n: (not isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef, ast.arg)), n.lineno))
            definition = ast.get_docstring(node) if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)) else None
            statement = node
            while not isinstance(statement, ast.stmt) and statement in self.parents:
                statement = self.parents[statement]
            anchor = ast.get_source_segment(self.text, statement) or self.text.splitlines()[node.lineno-1].strip()
            if isinstance(node, ast.arg):
                context_doc = ast.get_docstring(statement) if isinstance(statement,(ast.FunctionDef,ast.AsyncFunctionDef,ast.ClassDef)) else None
                definition = f"Formal parameter {identifier} of {scope}; source argument/default/annotation binding is retained. Declaration: {ast.unparse(node)}. Callable context: {context_doc or anchor[:400]}"
            elif not definition:
                definition = f"{role} {identifier} in {scope}; its value/role follows this source operation, not a universal meaning shared with other scopes: {anchor}"
            sites = set()
            for used in nodes:
                parent = used
                while not isinstance(parent, ast.stmt) and parent in self.parents:
                    parent = self.parents[parent]
                line = record_lines.get((type(parent).__name__, getattr(parent,'lineno',0), getattr(parent,'col_offset',0)))
                if line is not None: sites.add(line + fence_offset)
            used_in = '; '.join(f"{destination.relative_to(OUT).as_posix()}:{line}" for line in sorted(sites))
            original = ast.get_source_segment(self.text, node) if isinstance(node, ast.Attribute) else identifier
            result.append([self.rel, identifier, role, definition[:700], node.lineno, node.end_lineno,
                           used_in or destination.relative_to(OUT).as_posix(),
                           'source spelling retained; newly recorded relative to SudoLang; no supplied vocabulary reused',
                           scope, original])
        for name, record in sorted(self.literals.items()):
            result.append([self.rel,name,'converter evidence identifier',record['meaning'],record['line_start'],record['line_end'],
                           destination.relative_to(OUT).as_posix(),'new converter identifier; original literal/template has no variable name',
                           f"source coordinate {record['line_start']}",'unnamed original literal/template at cited source coordinate'])
        return result


def main():
    files = sorted(p for p in SRC.rglob("*.py") if "tests" not in p.relative_to(SRC).parts)
    modules = {module_name(p.relative_to(SRC).as_posix()): p.relative_to(SRC).as_posix() for p in files if module_name(p.relative_to(SRC).as_posix())}
    manifest, statements, calls, imports = [], [], [], []
    symbols = []
    for p in files:
        rel = p.relative_to(SRC).as_posix(); text = p.read_text()
        renderer = Render(rel, text, modules)
        dest = DETAIL / (rel + ".sudo.md"); dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(renderer.render())
        comments = [{"line": t.start[0], "text": t.string} for t in tokenize.generate_tokens(io.StringIO(text).readline) if t.type == tokenize.COMMENT]
        all_strings = [{"line_start": n.lineno, "line_end": n.end_lineno, "column": n.col_offset,
                        "value": n.value, "context": "f-string segment" if id(n) in renderer.joined_constants else "literal"}
                       for n in ast.walk(renderer.tree) if isinstance(n, ast.Constant) and isinstance(n.value, str)]
        evidence = {"source": rel, "sha256": digest(p), "source_text": text,
                    "literals": renderer.literals, "strings": all_strings, "comments": comments,
                    "statements": renderer.records, "expressions": renderer.expressions,
                    "calls": renderer.calls, "imports": renderer.imports}
        dump(OUT / "assets" / (rel + ".evidence.json"), evidence)
        for record in renderer.records: statements.append([rel, record["kind"], record["line_start"], record["line_end"], record["column"], record["owner"]])
        for call in renderer.calls: calls.append([rel, call["line"], call["end_line"], call["enclosing"], call["callee"]])
        for imp in renderer.imports: imports.append([rel, imp["line"], imp["source_expression"], ";".join(imp["local_source_paths"]), imp["boundary"]])
        symbols.extend(renderer.vocabulary_rows(dest))
        expected = sum(isinstance(n, ast.stmt) for n in ast.walk(renderer.tree))
        if len(renderer.records) != expected: raise AssertionError((rel, len(renderer.records), expected))
        manifest.append({"source": rel, "source_sha256": digest(p), "representation": dest.relative_to(OUT).as_posix(),
                         "evidence": "assets/" + rel + ".evidence.json", "statement_count": expected,
                         "representation_sha256": digest(dest), "conversion": "structural AST rendering, manually reviewed conventions"})
    dump(OUT / "structural_manifest.json", manifest)
    tsv(OUT / "statement_coverage.tsv", ["source", "kind", "line_start", "line_end", "column", "owner"], statements)
    tsv(OUT / "call_sites.tsv", ["source", "line_start", "line_end", "owner", "callee"], calls)
    tsv(OUT / "import_links.tsv", ["source", "line", "import", "local_targets", "boundary"], imports)
    tsv(OUT / "vocabulary_symbols.tsv", ["source", "identifier", "role", "definition", "line_start", "line_end", "used_in", "reuse", "scope", "original_identifier"], symbols)
    print(json.dumps({"modules": len(manifest), "source_statements": len(statements), "call_sites": len(calls), "vocabulary_symbols": len(symbols)}, indent=2))


if __name__ == "__main__":
    main()
