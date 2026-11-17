"""Build <harness>.knobs.json (schema/knobspace.schema.json) from the registries and the pseudocode.

For each harness:
  components  <- parsed from the .pseudo files (modules, classes, methods, calls, knob reads)
  knobs       <- the YAML registry rows, plus where each knob is read in the pseudocode:
                   used_in   = every component that reads θ["id"]
                   component = first reader in the knob's target file (else first reader anywhere)
Validates against the schema and writes vvah/vvah.knobs.json and vulnhunter/vulnhunter.knobs.json.
Run from pseudocode/:  python3 tools/build_knobspace.py
"""
import json
import sys
from collections import defaultdict
from pathlib import Path

import jsonschema
import yaml

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from pseudo_parse import parse_tree  # noqa: E402
from harnesses import HARNESSES, harness_of  # noqa: E402

PSEUDO = HERE.parent
RESULTS = PSEUDO.parent
SCHEMA = json.loads((PSEUDO / "schema" / "knobspace.schema.json").read_text())

COMPONENT_KEYS = {"id", "kind", "parent", "executed_by", "role", "stage", "real_source", "line", "calls", "knobs", "doc"}


def worklist_targets(key):
    t = {}
    for p in (HERE / "worklists").glob("*.json"):
        if harness_of(p.stem) != key:
            continue
        for r in json.loads(p.read_text()):
            t[r["id"]] = r["target"]
    return t


def clean_component(c):
    out = {k: v for k, v in c.items() if k in COMPONENT_KEYS}
    if out.get("role") is None:
        out.pop("role", None)
    if not out.get("doc"):
        out.pop("doc", None)
    return out


def build(h):
    reg = yaml.safe_load(open(RESULTS / h["registry"]))
    root = PSEUDO / h["folder"]
    comps, refs, probs = parse_tree(root)
    comp_ids = {c["id"] for c in comps}
    targets = worklist_targets(h["key"])
    readers = defaultdict(list)
    for kid, comp, f, line in refs:
        if comp not in readers[kid]:
            readers[kid].append(comp)
    knobs, unplaced = [], []
    rows = [(cat, grp, k) for cat, groups in reg["categories"].items() for grp, ks in groups.items() for k in ks]
    for p in sorted((HERE / "new_knobs").glob("*.json")):
        if harness_of(p.stem) != h["key"]:
            continue
        for r in json.loads(p.read_text()):
            targets[r["id"]] = r["target"]
            k = dict(r)
            k.setdefault("kind", "implicit")
            rows.append((r["category"], r["group"], k))
    for cat, grp, k in rows:
        used = readers.get(k["id"], [])
        tgt = targets.get(k["id"])
        primary = next((c for c in used if tgt and c.split("#")[0] == tgt), used[0] if used else None)
        if primary is None:
            unplaced.append(k["id"])
            primary = tgt if tgt and tgt in comp_ids else (tgt or "UNPLACED.pseudo")
            used = [primary]
        row = dict(id=k["id"], component=primary, used_in=used, category=cat, group=grp,
                   stage=k.get("stage"), origin=k["origin"], kind=k["kind"], type=k["type"],
                   default=k.get("default"), source=str(k.get("source", "")), does=k.get("does", ""),
                   affects=k.get("affects") or [])
        if "domain" in k:
            row["domain"] = k["domain"]
            row["domain_basis"] = k.get("domain_basis")
        if k.get("profiles"):
            row["profiles"] = k["profiles"]
        if k.get("requires"):
            row["conditions"] = [str(k["requires"])]
        if k.get("quote"):
            row["quote"] = k["quote"]
        knobs.append(row)
    harness = dict(name=h["name"], repo_path=h["repo"], commit=reg["commit"], description=reg["about"])
    if h["version"]:
        harness["version"] = h["version"]
    if h["profiles"]:
        harness["profiles"] = h["profiles"]
    doc = dict(schema_version="1.0", harness=harness, pseudocode_root=".",
               components=[clean_component(c) for c in comps], knobs=knobs)
    errors = sorted(jsonschema.Draft202012Validator(SCHEMA).iter_errors(doc), key=lambda e: list(e.path))
    invalid_links = [k["id"] for k in knobs if k["component"] not in comp_ids or any(c not in comp_ids for c in k["used_in"])]
    duplicate_ids = len(knobs) - len({k["id"] for k in knobs})
    out = root / h["out"]
    bad = len(errors) + len(unplaced) + len(probs) + len(invalid_links) + duplicate_ids
    if not bad:
        out.write_text(json.dumps(doc, indent=1, ensure_ascii=False, default=str))
    ex = defaultdict(int)
    for c in comps:
        if c["kind"] == "method":
            ex[c["executed_by"]] += 1
    print(f"[{h['name']}] {'rejected' if bad else 'wrote'} {out.relative_to(PSEUDO)}: {len(comps)} components "
          f"({sum(c['kind'] == 'module' for c in comps)} files), {len(knobs)} knobs, "
          f"{len(unplaced)} not read in pseudocode, schema errors {len(errors)}, convention problems {len(probs)}; "
          f"methods by executor {dict(ex)}")
    for e in errors[:10]:
        print("   schema:", list(e.path)[:4], e.message[:160])
    for u in unplaced[:10]:
        print("   not read:", u)
    for kid in invalid_links[:10]:
        print("   unknown component reference:", kid)
    if duplicate_ids:
        print("   duplicate knob ids:", duplicate_ids)
    return bad


def main():
    bad = sum(build(h) for h in HARNESSES)
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
