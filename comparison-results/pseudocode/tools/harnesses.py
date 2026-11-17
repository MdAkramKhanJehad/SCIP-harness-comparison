"""Shared harness catalog; paths resolve from the catalog, independent of cwd."""
import json
from pathlib import Path

PSEUDO = Path(__file__).resolve().parent.parent
HARNESSES = json.loads((PSEUDO / "harnesses.json").read_text())
if len({h["key"] for h in HARNESSES}) != len(HARNESSES):
    raise ValueError("duplicate harness key in harnesses.json")
for harness in HARNESSES:
    harness["repo"] = str((PSEUDO / harness["repo"]).resolve())
DIRS = {h["key"]: PSEUDO / h["folder"] for h in HARNESSES}


def harness_of(group):
    tokens = set(group.split("_"))
    matches = [h["key"] for h in HARNESSES if tokens.intersection(h["worklist_tokens"])]
    if len(matches) != 1:
        raise ValueError(f"worklist {group!r} must identify exactly one harness from harnesses.json")
    return matches[0]
