"""Primary class name for a .pseudo file, so files written by different people call each other consistently.

  python3 tools/class_name.py vvaharness/pipeline/stages/s4/prompts.pseudo   -> S4Prompts
  python3 tools/class_name.py vulnhunt/phases/phase2b_verify.pseudo          -> Phase2bVerify

Names listed in tools/class_names.json win (unique within a harness; a new file whose rule name would
collide gets its parent folder(s) as a prefix). Otherwise the rule applies:
CamelCase of the file stem (split on _ - .); if the stem is generic, prefix the parent folder's CamelCase.
__init__ becomes the parent folder alone.
"""
import re
import sys

GENERIC = {"__init__", "_index", "SKILL", "probe", "prompts", "outcomes", "session", "batching", "models",
           "tools", "options", "registry", "config", "settings", "cli", "facts", "validate", "window",
           "collapse", "enrich", "reanchor", "gates", "rules", "detectors", "health", "baseline", "limits",
           "profiles", "stub", "entry", "scan", "batch", "preflight", "sdk", "openai", "remediate", "playbook",
           "policy_gate", "system", "launch_prompt", "verify", "deliver", "implement", "plan", "parse", "sweep",
           "judge", "tally", "threat", "findings", "patterns", "oracle", "router", "_consensus"}


def camel(s):
    parts = [p for p in re.split(r"[_\-.]+", s) if p]
    return "".join(p[:1].upper() + p[1:] if not p.isupper() else p[:1] + p[1:].lower() for p in parts)


def class_name(path):
    path = path.strip("/")
    segs = path.split("/")
    stem = re.sub(r"\.pseudo$", "", segs[-1])
    parent = segs[-2] if len(segs) > 1 else ""
    if stem == "__init__":
        return camel(parent)
    if stem in GENERIC:
        return camel(parent) + camel(stem)
    return camel(stem)


def lookup(path, harness=None):
    """Name from tools/class_names.json (unique per harness) if listed, else the rule."""
    import json
    from pathlib import Path
    table = Path(__file__).with_name("class_names.json")
    if table.exists():
        tables = json.loads(table.read_text())
        if harness is not None:
            if harness not in tables:
                raise ValueError(f"unknown class-name table: {harness}")
            return tables[harness].get(path.strip("/"), class_name(path))
        matches = {names[path.strip("/")] for names in tables.values() if path.strip("/") in names}
        if len(matches) > 1:
            raise ValueError(f"ambiguous class name for {path}; pass --harness <folder>")
        if matches:
            return next(iter(matches))
    return class_name(path)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--harness", help="class_names.json table key (harness folder)")
    parser.add_argument("paths", nargs="+")
    args = parser.parse_args()
    for path in args.paths:
        print(lookup(path, args.harness))
