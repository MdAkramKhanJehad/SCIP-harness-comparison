"""Check every `// src: path:line` in the pseudocode points at an existing file and line in the real repo.
Run from pseudocode/:  python3 tools/check_src.py
"""
import re
from collections import Counter
from pathlib import Path
from harnesses import HARNESSES, PSEUDO

ROOTS = {h["folder"]: Path(h["repo"]) for h in HARNESSES}
SRC = re.compile(r'(?:@src\("|//\s*src:\s*)([^\s,;"()]+?):(\d+)')
failures = 0
for name, repo in ROOTS.items():
    total, bad, nlines = 0, Counter(), {}
    for p in (PSEUDO / name).rglob("*.pseudo"):
        for no, line in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
            for path, ln in SRC.findall(line):
                total += 1
                f = repo / path
                if path not in nlines:
                    nlines[path] = len(f.read_text(errors="replace").splitlines()) if f.is_file() else -1
                if nlines[path] < 0:
                    bad[f"missing file {path}"] += 1
                elif int(ln) > nlines[path] or int(ln) < 1:
                    bad[f"line out of range {path}"] += 1
    print(f"[{name}] src pointers {total}, bad {sum(bad.values())}")
    if total == 0:
        print("   ERROR: no source pointers found")
        failures += 1
    failures += sum(bad.values())
    for k, n in bad.most_common(15):
        print(f"   {n:4d} {k}")
raise SystemExit(1 if failures else 0)
