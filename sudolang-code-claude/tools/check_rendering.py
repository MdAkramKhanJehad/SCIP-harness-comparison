#!/usr/bin/env python3
"""Mechanical checks for the VVAH SudoLang rendering.

Checks:
  1. Every `// src:` and `// prompt-src:` pointer names an existing harness file
     and a line range inside it. Short forms such as `scan.py:401-410` are
     resolved against the output file's own `Source:` header.
  2. Every output file has a `Source:` header that names an existing file.
  3. Every source file in scope has exactly one coverage row (merged from
     `_work/*/coverage.tsv`), and every `full`/`partial` row names an output
     file that exists.
  4. Counts of markers (unresolved, preserved, external, abstracted).

It does not check meaning. Passing proves pointers and coverage are well formed,
not that the pseudocode is faithful.

Usage: python3 tools/check_rendering.py [--write-coverage]
"""
from __future__ import annotations

import csv
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HARNESS = ROOT.parent / "visa-vulnerability-agentic-harness"
OUT = ROOT / "vvah"

SCOPE_DIRS = ["vvaharness"]
SCOPE_INPUTS = ["inputs"]
EXCLUDED_PREFIXES: list[str] = []
IGNORED_SUFFIXES = {".pyc"}

SRC_RE = re.compile(r"//\s*(?:prompt-)?src:\s*([^\s—;,()]+?):(\d+)(?:-(\d+))?\b")
HEADER_RE = re.compile(r"^Source:\s*`([^`]+)`", re.M)
MARKERS = ["unresolved:", "preserved:", "external:", "abstracted:"]


def line_count(p: Path) -> int:
    try:
        return len(p.read_text(encoding="utf-8", errors="replace").splitlines())
    except OSError:
        return -1


def resolve(ref: str, header: str | None) -> Path | None:
    cand = HARNESS / ref
    if cand.is_file():
        return cand
    if header:
        h = HARNESS / header
        if h.name == Path(ref).name or ref == h.name:
            return h
        sib = h.parent / ref
        if sib.is_file():
            return sib
    return None


def scope_files() -> list[str]:
    files = []
    for d in SCOPE_DIRS + SCOPE_INPUTS:
        for p in sorted((HARNESS / d).rglob("*")):
            if not p.is_file() or p.suffix in IGNORED_SUFFIXES or "__pycache__" in p.parts:
                continue
            rel = p.relative_to(HARNESS).as_posix()
            if any(rel.startswith(x) for x in EXCLUDED_PREFIXES):
                continue
            files.append(rel)
    return files


def main() -> int:
    problems: list[str] = []
    markers = Counter()
    outputs = sorted(p for p in OUT.rglob("*") if p.is_file() and (p.suffix == ".sudo" or p.name.endswith(".sudo.md")))
    pointer_count = 0
    for out in outputs:
        text = out.read_text(encoding="utf-8")
        rel_out = out.relative_to(ROOT).as_posix()
        m = HEADER_RE.search(text)
        header = m.group(1) if m else None
        if out.name == "INDEX.sudo.md":
            header = None
        elif not header:
            problems.append(f"{rel_out}: no Source: header")
        elif not (HARNESS / header).is_file():
            problems.append(f"{rel_out}: Source header names missing file {header}")
        for mk in MARKERS:
            markers[mk] += text.count("// " + mk)
        for i, line in enumerate(text.splitlines(), 1):
            for sm in SRC_RE.finditer(line):
                pointer_count += 1
                ref, a, b = sm.group(1), int(sm.group(2)), int(sm.group(3) or sm.group(2))
                target = resolve(ref, header)
                if target is None:
                    problems.append(f"{rel_out}:{i}: pointer to unknown file {ref}")
                    continue
                n = line_count(target)
                if a < 1 or b < a or b > n:
                    problems.append(f"{rel_out}:{i}: range {a}-{b} outside {ref} ({n} lines)")

    rows: dict[str, dict] = {}
    dupes = []
    for tsv in sorted((ROOT / "_work").glob("*/coverage.tsv")):
        with tsv.open(encoding="utf-8") as fh:
            for r in csv.DictReader(fh, delimiter="\t"):
                sp = (r.get("source_path") or "").strip()
                if not sp:
                    continue
                if sp in rows:
                    dupes.append(f"{sp} ({rows[sp]['_batch']} and {tsv.parent.name})")
                r["_batch"] = tsv.parent.name
                rows[sp] = r
    for sp in sorted(set(dupes)):
        problems.append(f"coverage: duplicate row {sp}")
    # The spine was written outside the batches.
    rows.setdefault("vvaharness/orchestrator/scan.py", {
        "source_path": "vvaharness/orchestrator/scan.py", "source_lines": str(line_count(HARNESS / "vvaharness/orchestrator/scan.py")),
        "output_path": "vvah/vvaharness/orchestrator/scan.sudo", "status": "full", "notes": "spine, written first", "_batch": "spine"})

    in_scope = scope_files()
    missing = [f for f in in_scope if f not in rows]
    for f in missing:
        problems.append(f"coverage: no row for {f}")
    status = Counter()
    for sp, r in rows.items():
        st = (r.get("status") or "").strip()
        status[st] += 1
        op = (r.get("output_path") or "").strip()
        if st in ("full", "partial"):
            if not op or not (ROOT / op).is_file():
                problems.append(f"coverage: {sp} marked {st} but output {op!r} missing")
        if not (HARNESS / sp).is_file():
            problems.append(f"coverage: row for nonexistent source {sp}")

    if "--write-coverage" in sys.argv:
        with (ROOT / "coverage.tsv").open("w", encoding="utf-8", newline="") as fh:
            w = csv.writer(fh, delimiter="\t")
            w.writerow(["source_path", "source_lines", "output_path", "status", "batch", "notes"])
            for sp in in_scope:
                r = rows.get(sp)
                if r is None:
                    w.writerow([sp, line_count(HARNESS / sp), "", "not covered", "", "no batch row"])
                else:
                    w.writerow([sp, r.get("source_lines", ""), r.get("output_path", ""), r.get("status", ""), r["_batch"], r.get("notes", "")])

    print(f"output files: {len(outputs)}   pointers checked: {pointer_count}")
    print(f"source files in scope: {len(in_scope)}   coverage rows: {len(rows)}   status: {dict(status)}")
    print("markers: " + ", ".join(f"{k[:-1]}={v}" for k, v in markers.items()))
    print(f"problems: {len(problems)}")
    for p in problems[:200]:
        print("  " + p)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
