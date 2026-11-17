"""Check pseudocode against conventions and knob coverage.

  python3 tools/check_pseudocode.py                 # both harnesses, summary
  python3 tools/check_pseudocode.py --group vh_hunt # one work list, detailed
  python3 tools/check_pseudocode.py --harness vvah -v

Reports: convention problems, knobs in the work lists never read as θ["id"],
knobs read only outside their target file, and θ ids that are not knobs.
Exit code 1 if any knob is missing or any id is unknown.
"""
import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from pseudo_parse import parse_tree  # noqa: E402
from harnesses import DIRS, harness_of  # noqa: E402

PSEUDO = HERE.parent


CATEGORIES = {"model_routing", "budget_and_termination", "decomposition_and_parallelism", "scope_and_coverage",
              "context_supply", "tool_access", "detection_method", "gating_and_thresholds", "verification_depth",
              "dedup_and_merge", "ranking_and_reporting", "remediation", "runtime_and_infra", "evaluation"}
NEW_KNOB_FIELDS = {"id", "target", "category", "group", "stage", "origin", "type", "default", "does", "source", "affects"}


def worklists(harness=None, group=None):
    """Knob rows: registry work lists + new knobs found while writing (tools/new_knobs/<group>.json)."""
    rows = []
    for folder in ("worklists", "new_knobs"):
        for p in sorted((HERE / folder).glob("*.json")):
            g = p.stem
            h = harness_of(g)
            if harness and h != harness:
                continue
            if group and g != group:
                continue
            for r in json.loads(p.read_text()):
                r["_group"], r["_harness"], r["_new"] = g, h, folder == "new_knobs"
                rows.append(r)
    return rows


def all_ids(harness):
    return {r["id"] for r in worklists(harness)}


def phase2_targets(group):
    p = HERE / "phase2" / f"{group}.json"
    return [r["target"] for r in json.loads(p.read_text())] if p.exists() else []


def check_new_knobs(harness):
    """New-knob rows: required fields, valid category/origin, ids unique across registry + new knobs."""
    probs, seen = [], {}
    for r in worklists(harness):
        if r["id"] in seen:
            probs.append(f"duplicate knob id {r['id']} ({seen[r['id']]} and {r['_group']})")
        seen[r["id"]] = r["_group"]
        if not r["_new"]:
            continue
        miss = NEW_KNOB_FIELDS - set(r)
        if miss:
            probs.append(f"new knob {r['id']} missing fields {sorted(miss)}")
        if r.get("category") not in CATEGORIES:
            probs.append(f"new knob {r['id']} bad category {r.get('category')}")
        if r.get("origin") not in ("code_constant", "prompt_text", "config_file", "builtin_default", "cli_flag", "env_var"):
            probs.append(f"new knob {r['id']} bad origin {r.get('origin')}")
    return probs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--harness", choices=list(DIRS))
    ap.add_argument("--group")
    ap.add_argument("-v", action="store_true")
    ap.add_argument("--calls", action="store_true", help="list unresolved cross-file method calls")
    ap.add_argument("--strict", action="store_true", help="also fail on conventions, absent targets and unresolved calls")
    a = ap.parse_args()
    harnesses = [a.harness] if a.harness else ([harness_of(a.group)] if a.group else list(DIRS))
    bad = 0
    for h in harnesses:
        root = DIRS[h]
        if not root.exists():
            print(f"[{h}] no pseudocode folder yet")
            continue
        comps, refs, probs = parse_tree(root)
        rows = worklists(h, a.group)
        targets = {r["target"] for r in rows} | set(phase2_targets(a.group) if a.group else [])
        known = all_ids(h)
        probs = probs + check_new_knobs(h)
        owners = defaultdict(set)
        for c in comps:
            if c["kind"] == "class":
                owners[c["id"].split("#")[1]].add(c["id"].split("#")[0])
        for name, files in owners.items():
            if len(files) > 1:
                probs.append(f"{sorted(files)[0]}: class name {name} also defined in {sorted(files)[1:]}")
        where = defaultdict(set)
        for kid, comp, f, line in refs:
            where[kid].add(f)
        if a.group:
            probs = [p for p in probs if p.split(":")[0] in targets or p.startswith(("duplicate", "new knob"))]
        missing = [r for r in rows if r["id"] not in where]
        elsewhere = [r for r in rows if r["id"] in where and r["target"] not in where[r["id"]]]
        unknown = sorted({(kid, f, line) for kid, comp, f, line in refs if kid not in known})
        if a.group:
            unknown = [u for u in unknown if u[1] in targets]
        files = sorted({c["id"] for c in comps if c["kind"] == "module"})
        n_new = sum(1 for r in rows if r["_new"])
        print(f"[{h}] files {len(files)}  components {len(comps)}  knob refs {len(refs)}  new knobs {n_new}  "
              f"knobs covered {len(rows) - len(missing)}/{len(rows)}  missing {len(missing)}  "
              f"outside target {len(elsewhere)}  unknown ids {len(unknown)}  convention problems {len(probs)}")
        absent_targets = sorted(t for t in targets if not (root / t).exists())
        if absent_targets:
            print(f"  target files not written yet: {len(absent_targets)}")
            for t in absent_targets[: 50 if a.v or a.group else 10]:
                print("    ", t)
        for p in probs[: 200 if a.v or a.group else 20]:
            print("  PROBLEM", p)
        if missing:
            by = defaultdict(list)
            for r in missing:
                by[r["target"]].append(r["id"])
            for t, ids in sorted(by.items()):
                print(f"  MISSING in {t}: {len(ids)}")
                if a.v or a.group:
                    for i in ids:
                        print("     ", i)
        for kid, f, line in unknown[: 200 if a.v or a.group else 20]:
            print(f"  UNKNOWN θ[\"{kid}\"] at {f}:{line}")
        if (a.v or a.group) and elsewhere:
            for r in elsewhere:
                print(f"  OUTSIDE TARGET {r['id']} (target {r['target']}, found in {sorted(where[r['id']])})")
        # cross-file calls: Class.method(...) where Class is defined somewhere in this harness (or schema/)
        common, _, _ = parse_tree(PSEUDO / "schema")
        classes = defaultdict(set)
        for c in comps + common:
            if c["kind"] == "class":
                classes[c["id"].split("#")[1]]
        for c in comps + common:
            if c["kind"] == "method":
                cls, m = c["id"].split("#")[1].split(".", 1)
                classes[cls].add(m)
        unresolved = []
        for c in comps:
            if c["kind"] != "method":
                continue
            if a.group and c["id"].split("#")[0] not in targets:
                continue
            for call in c["calls"]:
                cls, m = call.split(".", 1)
                if cls in classes and m not in classes[cls]:
                    unresolved.append((c["id"], call))
        print(f"  cross-file calls to a known class but unknown method: {len(unresolved)}")
        if a.calls:
            for owner, call in unresolved:
                print(f"    {call}  <- {owner}")
        bad += len(missing) + len(unknown)
        if a.strict:
            bad += len(probs) + len(absent_targets) + len(unresolved)
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
