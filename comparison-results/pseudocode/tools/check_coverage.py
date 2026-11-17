"""Check that every selected source file has a corresponding pseudocode file.

Source globs are language-independent and come from harnesses.json. This is file
coverage, not proof that every source branch has been rendered correctly.
"""
import argparse
from pathlib import Path

from harnesses import HARNESSES, PSEUDO


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--harness", choices=[h["key"] for h in HARNESSES])
    args = parser.parse_args()
    failures = 0
    for h in HARNESSES:
        if args.harness and args.harness != h["key"]:
            continue
        repo = Path(h["repo"])
        selected = {p for pattern in h.get("source_globs", []) for p in repo.glob(pattern) if p.is_file()}
        if not selected:
            print(f"[{h['key']}] ERROR: no source files selected by source_globs")
            failures += 1
            continue
        missing = []
        for source in sorted(selected):
            rel = source.relative_to(repo)
            target = PSEUDO / h["folder"] / rel.with_suffix(".pseudo")
            lines = target.read_text().splitlines() if target.is_file() else []
            if not lines or not lines[0].startswith("// file: "):
                missing.append(str(rel))
            elif str(rel) not in [s.strip() for s in lines[0].removeprefix("// file: ").split(",")]:
                missing.append(f"{rel} (wrong source header)")
        print(f"[{h['key']}] selected source files {len(selected)}, represented {len(selected) - len(missing)}, missing {len(missing)}")
        for path in missing:
            print("  MISSING", path)
        failures += len(missing)
    return bool(failures)


if __name__ == "__main__":
    raise SystemExit(main())
