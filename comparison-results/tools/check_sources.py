#!/usr/bin/env python3
"""Check that every knob's `source` points at a real file (and line), and print
the cited line for knobs that were collected by hand so they can be eyeballed."""
import sys
from pathlib import Path
import yaml

OUT = Path(__file__).resolve().parents[1]
ROOT = OUT.parent
bad = 0
for name in ("vvah", "vulnhunter"):
    doc = yaml.safe_load((OUT / f"{name}.knobs.yaml").read_text())
    base = ROOT / doc["source_root"]
    for cat, groups in doc["categories"].items():
        for group, knobs in groups.items():
            for k in knobs:
                for src in k["source"].split(" ; "):
                    path, _, line = src.partition(":")
                    f = base / path
                    if not f.exists():
                        bad += 1
                        print(f"MISSING {name} {k['id']}: {src}")
                        continue
                    if line and f.is_file():
                        lines = f.read_text(errors="replace").splitlines()
                        n = int(line)
                        if n > len(lines):
                            bad += 1
                            print(f"BAD LINE {name} {k['id']}: {src}")
                        elif "-v" in sys.argv and k["origin"] in ("prompt_text", "code_constant", "cli_flag"):
                            print(f"{name:10s} {k['id'][:38]:38s} {path.split('/')[-1]}:{n}: {lines[n-1].strip()[:90]}")
print("problems:", bad)
