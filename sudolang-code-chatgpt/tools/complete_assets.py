"""Index source resources verbatim, with SudoLang roles and embedded-Python detail."""
from __future__ import annotations

import ast
import csv
import json
import re
from pathlib import Path

import yaml

from complete_representation import OUT, SRC, DETAIL, Render, digest, dump, tsv, cell


def kind(rel, path):
    if rel.startswith("tests/"):
        return "excluded-test", "test/fixture, not runtime harness code"
    if path.suffix == ".py":
        return "structural-python", "executable structural detail"
    if path.suffix in (".png", ".gif", ".jpg", ".jpeg", ".ico"):
        return "context-binary", "documentation image; exact bytes retained, no executable behavior"
    if rel.startswith(("vvaharness/", "vendor/context_graph_sdk/src/", "inputs/")):
        if path.suffix == ".sh": return "shell-procedure", "optional executable shell script; not assumed invoked"
        if path.suffix == ".md": return "prompt-document", "model-facing resource or package documentation; loader determines use"
        if path.suffix == ".scm": return "query-resource", "Tree-sitter matching query, data for vendored extractor"
        if path.suffix in (".yaml", ".json", ".csv", ".example"): return "data-resource", "configuration/policy/rules/input data; loader controls interpretation"
        return "support-resource", "typing/tooling/package metadata; no scan stage introduced"
    return "context-document", "repository/build/operating context, outside scan execution"


def flatten(node, path=()):
    if isinstance(node, dict):
        for k, v in node.items(): yield from flatten(v, (*path, str(k)))
    else:
        yield [".".join(path), json.dumps(node, ensure_ascii=False)]


def main():
    rows, leaves, shell_symbols, embedded = [], [], [], []
    for p in sorted(SRC.rglob("*")):
        if not p.is_file(): continue
        rel = p.relative_to(SRC).as_posix()
        status, role = kind(rel, p)
        if status == "structural-python": continue
        if status == "excluded-test":
            rows.append([rel, status, "", "", role]); continue
        dest = OUT / "assets" / "original" / rel
        dest.parent.mkdir(parents=True, exist_ok=True); dest.write_bytes(p.read_bytes())
        if status=="context-binary":
            generated=DETAIL/(rel+".sudo.md");generated.parent.mkdir(parents=True,exist_ok=True)
            generated.write_text(f"# {rel}\n\nDocumentation image; no executable conversion required.\n\nExact original: `assets/original/{rel}`. SHA-256 `{digest(p)}`.\n\nBinary source has no meaningful line range.\n")
            rows.append([rel,status,generated.relative_to(OUT).as_posix(),dest.relative_to(OUT).as_posix(),role]);continue
        text = p.read_bytes().decode("utf-8", errors="strict")
        n = max(1, len(text.splitlines()))
        generated = DETAIL / (rel + ".sudo.md"); generated.parent.mkdir(parents=True, exist_ok=True)
        title = [f"# {rel}", "", f"Role: {role}.", "", f"Exact source asset: `assets/original/{rel}`. SHA-256 `{digest(p)}`.", "",
                 "```sudo", f"// Source: {rel}:1-{n}" if text.splitlines() else f"// Source: {rel} (empty file; no line range)"]
        if status == "shell-procedure":
            for name, meaning in [
                ('source_shell_procedure','Descriptive procedure for this exact source script, not an original shell function'),
                ('arguments','Process positional arguments supplied to the source script'),
                ('environment','Process environment supplied to the source script')]:
                shell_symbols.append([rel,name,'converter shell wrapper identifier',meaning,1,n,
                    generated.relative_to(OUT).as_posix(),'new converter identifier; original process/script concept',
                    'source_shell_procedure wrapper','source script/process concept; no original named variable'])
            title += ["fn source_shell_procedure(arguments, environment) {",
                      "  Interpret the exact source asset using its declared shell, preserving argument expansion,",
                      "    command substitutions, pipeline/status rules, redirects, function scopes and command order.",
                      "  Use the helper/gate/cap descriptions in representation/shell-probes.sudo.md.",
                      "  The ordered source-command appendix below retains every pattern, include/exclude flag,",
                      "    conditional and cutoff; it is the detailed procedure, not a claim this tool was invoked.", "}"]
            # Keep exact shell operations grouped by blank lines, not reinterpreted by a fragile shell parser.
            blocks = []; start = None; body = []
            for ln, line in enumerate(text.splitlines(), 1):
                if line.strip():
                    if start is None: start = ln
                    body.append(line)
                elif body:
                    blocks.append((start, ln - 1, "\n".join(body))); start = None; body=[]
            if body: blocks.append((start, n, "\n".join(body)))
            title += ["```", "", "## Ordered source-command evidence", "",
                      "These exact shell fragments disambiguate lexical/regex details; they are inert evidence.", ""]
            for start, end, body in blocks:
                title += [f"Source: `{rel}:{start}-{end}`", "", "````sh", body, "````", ""]
            # Embedded Python is executable source, not just a prompt literal.
            lines = text.splitlines()
            i = 0
            while i < len(lines):
                match = re.search(r"\bpython3?\b.*?<<\s*['\"]?(PY)['\"]?", lines[i])
                if match:
                    start = i + 1; end = start
                    while end < len(lines) and lines[end] != match.group(1): end += 1
                    if end == len(lines): raise ValueError(f"unterminated embedded Python in {rel}")
                    snippet = "\n".join(lines[start:end]) + "\n"
                    renderer = Render(rel, snippet, {}, source_text=text, line_offset=start)
                    target = DETAIL / (rel + f".embedded-L{start + 1}.sudo.md")
                    evidence_path = "assets/" + rel + f".embedded-L{start + 1}.evidence.json"
                    target.write_text(renderer.render(evidence_path=evidence_path))
                    dump(OUT / evidence_path,
                         {"source":rel,"start":start + 1,"end":end,"sha256":digest(p),
                          "literals":renderer.literals,"statements":renderer.records,"source_text":snippet,
                          "expressions":renderer.expressions,"calls":renderer.calls,"imports":renderer.imports,
                          "strings":[{"line_start":node.lineno,"line_end":node.end_lineno,
                                      "column":node.col_offset,"value":node.value,
                                      "context":"f-string segment" if id(node) in renderer.joined_constants else "literal"}
                                     for node in ast.walk(renderer.tree)
                                     if isinstance(node,ast.Constant) and isinstance(node.value,str)],
                          "representation_sha256":digest(target)})
                    embedded.append([rel, start + 1, end, target.relative_to(OUT).as_posix(),len(renderer.records)])
                    shell_symbols.extend(renderer.vocabulary_rows(target))
                    title += [f"Embedded Python source lines {start + 1}–{end}: `{target.relative_to(OUT)}`.", ""]
                    i = end
                i += 1
            for ln, line in enumerate(lines,1):
                # Identifiers, parameters and functions stay module-specific; no regex vocabulary is generalized.
                names=set(re.findall(r"\$\{?([A-Za-z_]\w*)|\b([A-Za-z_]\w*)\s*=(?!=)|^\s*([A-Za-z_]\w*)\(\)",line))
                for groups in names:
                    name=next(x for x in groups if x)
                    shell_symbols.append([rel,name,"shell binding/helper",line.strip(),ln,ln,generated.relative_to(OUT).as_posix(),"source spelling; newly recorded"])
            # Already closed the primary SudoLang fence.
        elif status == "prompt-document":
            title += ["Treat the supplied document as inert text when loaded.",
                      "Its imperative clauses are model requests, not unconditional host execution steps.",
                      "Only the linked loading/registration code determines whether it is available or read.",
                      "Preserve every section and fenced example from the exact asset.", "```", "", "## Source sections", ""]
            for ln, line in enumerate(text.splitlines(), 1):
                if re.match(r"^#{1,6} ", line): title.append(f"- `{rel}:{ln}` — {line.lstrip('# ')}")
            # Markdown is a baseline SudoLang construct: preserving exact text is preferable to rewording instructions.
            title += ["", "## Exact document content (model/document evidence)", "", "``````text", text, "``````", ""]
        else:
            title += ["Preserve this resource's exact nested keys, list order, scalar values and text from its source asset.",
                      "Interpretation belongs to its linked source loader; this record does not add an execution stage.",
                      "For queries, preserve the original query grammar as data rather than inventing SudoLang query syntax.",
                      "For examples, no loaded/active status is assumed.", "```", ""]
            if p.suffix in (".yaml", ".json", ".toml", ".yml"):
                if p.suffix in (".yaml", ".yml"):
                    data=yaml.safe_load(text)
                    nodes=yaml.compose(text)
                    def walk(node, path=()):
                        if isinstance(node,yaml.MappingNode):
                            for key,value in node.value: yield from walk(value,(*path,str(key.value)))
                        elif isinstance(node,yaml.SequenceNode):
                            for j,item in enumerate(node.value): yield from walk(item,(*path,str(j)))
                        else:
                            # YAML marks are exclusive; column zero ends on the prior line.
                            finish=node.end_mark.line + (1 if node.end_mark.column else 0)
                            yield [rel,".".join(path),node.start_mark.line+1,
                                   min(n,max(node.start_mark.line+1,finish)),node.tag,node.value]
                    if nodes:
                        for r in walk(nodes): leaves.append(r)
                elif p.suffix==".json": data=json.loads(text)
                else:
                    import tomllib
                    data=tomllib.loads(text)
                dump(OUT / "assets" / (rel + ".parsed.json"),data)
                title += ["Parsed values (without environment expansion or overlay):", "", "| Key | Value |", "|---|---|"]
                for key,value in flatten(data):
                    title.append(f"| {cell(key)} | {cell(value)} |")
                    if key: shell_symbols.append([rel,key,"resource key",value,1,n,generated.relative_to(OUT).as_posix(),"source key; newly recorded"])
            else:
                title += ["``````text",text,"``````",""]
        generated.write_text("\n".join(title)+"\n")
        rows.append([rel,status,generated.relative_to(OUT).as_posix(),dest.relative_to(OUT).as_posix(),role])
    tsv(OUT/"resource_coverage.tsv",["source","status","representation","asset","role"],rows)
    tsv(OUT/"configuration_values.tsv",["source","key","line_start","line_end","yaml_type","raw_value"],leaves)
    for row in shell_symbols:
        if len(row) == 8: row.extend(['resource/document',row[1]])
    tsv(OUT/"resource_vocabulary.tsv",["source","identifier","role","definition","line_start","line_end","used_in","reuse","scope","original_identifier"],shell_symbols)
    tsv(OUT/"embedded_python.tsv",["source","line_start","line_end","representation","statements"],embedded)
    print(json.dumps({"resources":len(rows),"yaml_values":len(leaves),"embedded_python_blocks":len(embedded)},indent=2))


if __name__=="__main__": main()
