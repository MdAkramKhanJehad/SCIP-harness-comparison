"""Check artifact consistency without importing/running the harness or an LLM."""
from __future__ import annotations

import ast
import csv
import hashlib
import json
import re
from collections import Counter
from pathlib import Path

OUTPUT = Path(__file__).resolve().parents[1]
SOURCE = OUTPUT.parent / "visa-vulnerability-agentic-harness"


def rows(name: str) -> list[dict]:
    with (OUTPUT / name).open() as file:
        return list(csv.DictReader(file, delimiter="\t"))


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    errors = []
    ledger = rows("coverage.tsv")
    actual = {p.relative_to(SOURCE).as_posix() for p in SOURCE.rglob("*") if p.is_file()}
    if {r["source_path"] for r in ledger} != actual:
        errors.append("coverage ledger does not exactly match source files")
    for row in ledger:
        path = SOURCE / row["source_path"]
        if digest(path) != row["sha256"] or len(path.read_bytes().splitlines()) != int(row["lines"]):
            errors.append(f"source changed: {row['source_path']}")
        if row["representation_or_asset"] and not (OUTPUT / row["representation_or_asset"]).is_file():
            errors.append(f"missing artifact: {row['representation_or_asset']}")
        if row["status"] == "copied-unreviewed":
            if (OUTPUT / row["representation_or_asset"]).read_bytes() != path.read_bytes():
                errors.append(f"profile copy differs: {path}")
    citations = rows("source_links.tsv")
    for row in citations:
        path = SOURCE / row["source"]
        count = len(path.read_text().splitlines())
        if not 1 <= int(row["line_start"]) <= int(row["line_end"]) <= count:
            errors.append(f"invalid citation range: {row}")
        text = (OUTPUT / row["representation"]).read_text().splitlines()
        expected = f"// Source: {row['source']}:{row['line_start']}-{row['line_end']}"
        if text[int(row["representation_line"]) - 1] != expected:
            errors.append(f"stale source link: {row}")
    for path in (OUTPUT / "representation").rglob("*.sudo.md"):
        text = path.read_text()
        if text.count("```") % 2:
            errors.append(f"unbalanced code fence: {path}")
        if not re.search(r"// Source: .+:\d+-\d+", text):
            errors.append(f"uncited representation: {path}")
    for row in rows("prompt_assets.tsv"):
        path = SOURCE / row["source"]
        payload = json.loads((OUTPUT / row["asset"]).read_text())
        if digest(path) != payload["source_sha256"]:
            errors.append(f"stale string asset: {row['asset']}")
        raw = path.read_text()
        tree = ast.parse(raw)
        originals = {(n.lineno, n.end_lineno, n.value) for n in ast.walk(tree)
                     if isinstance(n, ast.Constant) and isinstance(n.value, str)}
        extracts = {(n["line_start"], n["line_end"], n["text"]) for n in payload["strings"]}
        if originals != extracts:
            errors.append(f"literal extraction differs: {row['asset']}")
        for template in payload["templates"]:
            if not template["source_expression"]:
                errors.append(f"missing f-string expression: {row['asset']}")
    baseline_rows = rows("baseline_review.tsv")
    for row in baseline_rows:
        if digest(OUTPUT / row["path"]) != row["sha256"]:
            errors.append(f"baseline snapshot changed: {row['path']}")
    examples = {p.relative_to(OUTPUT).as_posix() for p in (OUTPUT / "reference/sudolang/examples").rglob("*") if p.is_file()}
    if not examples <= {r["path"] for r in baseline_rows}:
        errors.append("baseline reading index omits examples")
    result = {"scope": "artifact consistency only; no semantic equivalence, model compliance or runtime test claim",
              "coverage_counts": dict(Counter(r["status"] for r in ledger)),
              "source_files": len(ledger), "source_citations": len(citations),
              "baseline_files": len(baseline_rows), "example_files": len(examples),
              "prompt_source_modules": len(rows("prompt_assets.tsv")),
              "errors": errors, "passed": not errors}
    (OUTPUT / "verification.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    raise SystemExit(bool(errors))


if __name__ == "__main__":
    main()
