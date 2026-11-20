"""Build traceability indexes for the explicitly converted batch; never run harness code.

This is bookkeeping, not an automatic semantic converter or correctness proof.
Run from any directory: python sudolang-code-chatgpt/tools/index_evidence.py
"""
from __future__ import annotations

import ast
import csv
import hashlib
import json
import re
from collections import defaultdict
from pathlib import Path

OUTPUT = Path(__file__).resolve().parents[1]
SOURCE = OUTPUT.parent / "visa-vulnerability-agentic-harness"
REP = OUTPUT / "representation"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def table(path: Path, columns: list[str], rows: list[list]) -> None:
    with path.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.writer(stream, delimiter="\t")
        writer.writerow(columns)
        writer.writerows(rows)


def cell(text: object) -> str:
    return str(text).replace("|", "&#124;").replace("\n", " ").replace("`", "&#96;")


def dotted(node: ast.AST) -> str | None:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        parent = dotted(node.value)
        return f"{parent}.{node.attr}" if parent else node.attr
    return None


def build() -> None:
    mapping = {}
    for generated in sorted(REP.rglob("*.sudo.md")):
        relative = generated.relative_to(REP).as_posix().removesuffix(".sudo.md") + ".py"
        mapping[relative] = generated

    reviewed_only = {"AGENTS.md": "operating instructions read in full; no scan performed",
                     "pyproject.toml": "dependencies, package assets and version reviewed"}
    coverage = []
    for path in sorted(SOURCE.rglob("*")):
        if not path.is_file():
            continue
        relative = path.relative_to(SOURCE).as_posix()
        status, target, notes = "pending", "", "not converted or semantically reviewed"
        if relative in mapping:
            status = "represented-local"
            target = mapping[relative].relative_to(OUTPUT).as_posix()
            notes = "read and represented at documented abstraction; imported callees not implied covered"
        elif relative in reviewed_only:
            status, notes = "reviewed-context", reviewed_only[relative]
        if relative.startswith("tests/"):
            status, notes = "not-converted-tests", "inventory only; not executed; not used as runtime behavior"
        if relative.startswith("vvaharness/config/profiles/") and path.suffix == ".yaml":
            dest = OUTPUT / "assets" / relative
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(path.read_bytes())
            status, target = "copied-unreviewed", dest.relative_to(OUTPUT).as_posix()
            notes = "exact profile evidence; effective merged behavior pending config-loader conversion"
        coverage.append([relative, len(path.read_bytes().splitlines()), sha(path), status, target, notes])
    table(OUTPUT / "coverage.tsv", ["source_path", "lines", "sha256", "status", "representation_or_asset", "notes"], coverage)

    baseline = OUTPUT / "reference" / "sudolang"
    baseline_files = [baseline / "README.md", baseline / "sudolang.sudo.md", *sorted((baseline / "examples").rglob("*"))]
    table(OUTPUT / "baseline_review.tsv", ["path", "lines", "sha256", "review_status"], [
        [p.relative_to(OUTPUT).as_posix(), len(p.read_bytes().splitlines()), sha(p), "read-full"]
        for p in baseline_files if p.is_file()
    ])

    vocabulary = [
        "# Vocabulary additions\n",
        "These are ordinary names and domain meanings within SudoLang v2.0, not grammar changes. "
        "No vocabulary-extension file was supplied; all entries are newly recorded additions to the baseline, "
        "usually retaining the source identifier. Baseline constructs (`fn`, `interface`, `if`, `else`, "
        "`while`, `for each`, assignment, Markdown, natural-language statements) are not extensions.\n",
        "The records below are namespaced by source module: the same short name in two modules "
        "is not assumed to have the same role. Dotted fields and model-visible string keys are "
        "listed alongside bindings. The use location gives a first occurrence; the named generated file "
        "can contain further uses. Source excerpts define local binding roles; they do not claim the "
        "unconverted implementation of an imported API was verified. Literal extraction is a conservative "
        "superset (it also retains referenced counter/status names). Ordinary English prose is not an identifier "
        "declaration. No language-extension proposal is needed for this batch.\n",
    ]
    core = [
        ("S0–S11", "Source stage ids for static seed, preprocessing, threat model, decomposition, deep-dive, enrichment, verification, deduplication, chaining/report, SARIF, remediation, validation; not all stages are converted.", "preserve workflow nesting/order", "tool-specific", "vvaharness/orchestrator/scan.py:569-1066", "representation/vvaharness/orchestrator/scan.sudo.md"),
        ("checkpoint", "Typed JSON value keyed by run_id and step in SQLite; failed load can cause rerun.", "describe resume gates", "general harness concept", "vvaharness/orchestrator/checkpoints.py:241-301", "representation/vvaharness/orchestrator/checkpoints.sudo.md"),
        ("provenance", "Separate step_prov checkpoint with producing model, route, raw config hash and stage token counts.", "retain cached origin", "general harness concept", "vvaharness/orchestrator/checkpoints.py:100-120", "representation/vvaharness/orchestrator/checkpoints.sudo.md"),
        ("unit", "InvestigationUnit dispatched by S4; its files, threat and risk determine prompt/scheduling context.", "retain unit/session distinction", "tool-specific", "vvaharness/pipeline/stages/s4_deepdive.py:43-82", "representation/vvaharness/pipeline/stages/s4_deepdive.sudo.md"),
        ("batch", "Several units sharing one investigation session; LARGE units remain singleton when partitioning.", "represent concurrent scheduling", "general harness concept", "vvaharness/pipeline/stages/s4/batching.py:34-48", "representation/vvaharness/pipeline/stages/s4/batching.sudo.md"),
        ("model request", "Text supplied to a model, including schema descriptions; the text alone does not enforce compliance.", "distinguish prompts from host actions", "general harness concept", "vvaharness/pipeline/stages/s4/prompts.py:423-444", "representation/vvaharness/pipeline/stages/s4/prompts.sudo.md"),
        ("evidence gate", "Middleware rejecting premature structured verdicts up to a limit, then relenting; out-of-loop behavior differs.", "represent conditional enforcement", "general harness concept", "vvaharness/backends/harness/deepagents/evidence_gate.py:128-223", "representation/vvaharness/backends/harness/deepagents/evidence_gate.sudo.md"),
        ("EV", "Exploit verification collection/preparation path; routing depends on ctx.ev_collection, not every scan.", "retain optional live verification branch", "tool-specific", "vvaharness/orchestrator/scan.py:214-262", "representation/vvaharness/orchestrator/scan.sudo.md"),
        ("pending boundary", "Conversion evidence status: call site inspected but implementation has not been converted; no inferred behavior is authorized by its name.", "expose partial coverage", "general harness concept", "coverage.tsv (conversion metadata; no corresponding harness operation)", "representation_specification.md"),
        ("represented-local", "Coverage status for a source module read and represented at the documented abstraction, without transitive dependency coverage.", "avoid treating local review as whole-program verification", "general harness concept", "coverage.tsv (conversion metadata)", "coverage.tsv"),
        ("pending", "Available source inventoried; no semantic review or conversion claim.", "identify outstanding conversion work", "general harness concept", "converter status; no original harness term", "coverage.tsv"),
        ("reviewed-context", "Source read for operating/dependency/version context without a pseudocode rendering.", "distinguish context reading from conversion", "general harness concept", "converter status; no original harness term", "coverage.tsv"),
        ("copied-unreviewed", "Source asset copied byte-for-byte; effective behavior remains unconverted.", "retain configuration evidence without overclaiming", "general harness concept", "converter status; no original harness term", "coverage.tsv"),
        ("not-converted-tests", "Test or fixture inventoried only, not executed or used to infer runtime behavior.", "bound validation claims", "general harness concept", "converter status; no original harness term", "coverage.tsv"),
        ("None", "Python source sentinel for missing/no value, retained as source semantics; distinct from an empty list or false.", "preserve checkpoint and optional-value branches", "general harness concept", "vvaharness/orchestrator/scan.py:570-571 (original spelling retained)", "representation/vvaharness/orchestrator/scan.sudo.md"),
    ]
    vocabulary += ["## Domain and evidence-status terms\n", "| Term | Definition | Why needed | Kind | Source / original wording | Used in | Reuse |",
                   "|---|---|---|---|---|---|---|"]
    for term, meaning, reason, kind, ref, used in core:
        vocabulary.append("| " + " | ".join(map(cell, [term, meaning, reason, kind, ref, used, "newly recorded; no supplied extension reused"])) + " |")

    links = []
    string_index = []
    for relative, generated in mapping.items():
        source = SOURCE / relative
        raw = source.read_text()
        lines = raw.splitlines()
        tree = ast.parse(raw)
        output_text = generated.read_text()
        output_lines = output_text.splitlines()
        symbols: dict[str, list] = defaultdict(list)

        def add(name: str, node: ast.AST, role: str, definition: str = "") -> None:
            if re.search(r"(?<![\w])" + re.escape(name) + r"(?![\w])", output_text):
                start = getattr(node, "lineno", 1)
                end = getattr(node, "end_lineno", start)
                excerpt = definition or lines[start - 1].strip()
                symbols[name].append((start, end, role, excerpt))

        strings = []
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                add(node.name, node, "callable/interface", ast.get_docstring(node) or lines[node.lineno - 1].strip())
            if isinstance(node, ast.Name):
                add(node.id, node, "binding/reference")
            if isinstance(node, ast.Attribute):
                add(node.attr, node, "member")
                name = dotted(node)
                if name:
                    add(name, node, "qualified member")
            if isinstance(node, ast.arg):
                add(node.arg, node, "parameter")
            if isinstance(node, ast.alias):
                add(node.asname or node.name, node, "imported identifier")
            if isinstance(node, ast.Constant) and isinstance(node.value, str):
                if re.fullmatch(r"(?:--)?[A-Za-z_]\w*(?:[.:-][\w-]+)*", node.value):
                    add(node.value, node, "literal key/tool/status/counter")
                strings.append({"source": relative, "line_start": node.lineno, "line_end": node.end_lineno,
                                "text": node.value,
                                "context": "f-string segment" if any(isinstance(p, ast.JoinedStr) and node in p.values for p in ast.walk(tree)) else "literal string"})
        dest = OUTPUT / "assets" / (relative + ".strings.json")
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(json.dumps({"source": relative, "source_sha256": sha(source),
                                   "notice": "Inert AST string evidence: prompts, schema descriptions, logs and docstrings. F-string segments are not complete rendered prompts; source expression preserves interpolation.",
                                   "strings": strings,
                                   "templates": [{"line_start": n.lineno, "line_end": n.end_lineno,
                                                  "source_expression": ast.get_source_segment(raw, n)}
                                                 for n in ast.walk(tree) if isinstance(n, ast.JoinedStr)]},
                                  indent=2, ensure_ascii=False) + "\n")
        string_index.append([relative, len(strings), dest.relative_to(OUTPUT).as_posix(), sha(source)])
        # One entry for every source-derived name used in this module's representation.
        vocabulary.append(f"\n## `{relative}`\n")
        vocabulary += ["| Identifier (original spelling) | Definition / local role | Why needed | Kind | Source | Used in | Reuse |",
                       "|---|---|---|---|---|---|---|"]
        for name, refs in sorted(symbols.items()):
            refs.sort(key=lambda x: (x[2] != "callable/interface", x[0]))
            start, end, role, excerpt = refs[0]
            use_line = next(i for i, line in enumerate(output_lines, 1) if re.search(r"(?<![\w])" + re.escape(name) + r"(?![\w])", line))
            meaning = f"{role}: {excerpt[:240]}"
            vocabulary.append("| " + " | ".join(map(cell, [name, meaning, f"name source {role} without renaming or inferred API expansion",
                "tool-specific identifier", f"{relative}:{start}-{end}", f"{generated.relative_to(OUTPUT)}:{use_line}",
                "newly recorded; source spelling retained; no supplied extension reused"])) + " |")

        for number, line in enumerate(output_lines, 1):
            match = re.match(r"// Source: (.+):(\d+)-(\d+)$", line)
            if match:
                path, start, end = match.groups()
                links.append([generated.relative_to(OUTPUT).as_posix(), number, path, int(start), int(end)])

    (OUTPUT / "vocabulary_extensions.md").write_text("\n".join(vocabulary) + "\n")
    table(OUTPUT / "source_links.tsv", ["representation", "representation_line", "source", "line_start", "line_end"], links)
    table(OUTPUT / "prompt_assets.tsv", ["source", "string_nodes", "asset", "source_sha256"], string_index)
    print(json.dumps({"source_files_inventoried": len(coverage), "represented_modules": len(mapping),
                      "source_links": len(links), "baseline_files_read": len(baseline_files)}, indent=2))


if __name__ == "__main__":
    build()
