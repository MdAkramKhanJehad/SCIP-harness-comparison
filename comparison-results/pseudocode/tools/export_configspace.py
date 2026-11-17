"""Export a <harness>.knobs.json to a ConfigSpace configuration space (ConfigSpace JSON format).

  python3 tools/export_configspace.py vvah/vvah.knobs.json            -> vvah/vvah.configspace.json
  python3 tools/export_configspace.py vulnhunter/vulnhunter.knobs.json --origin real

Needs the ConfigSpace package (pip install ConfigSpace).

Mapping (same for every harness):
  int / float with a {min, max} domain     -> UniformInteger / UniformFloat
  any knob with a list domain              -> Categorical over that list
  bool                                      -> Categorical [true, false]
  prompt_text knob with no domain           -> Categorical ["on", "off"]   (keep or remove the rule)
  anything else with no domain, or a domain with one value -> Constant (current value; meta.searchable = false).
    Most numeric config knobs only have the values seen in shipped profiles (domain_basis "observed"),
    so they export as Constant or as a Categorical over the observed values. Add a {min, max} domain in
    the knob file to make one a numeric range.
Each hyperparameter's `meta` keeps category, group, stage, origin, component, source and domain_basis,
so a search can filter by any of them. `conditions` naming another knob id of a bool knob become
EqualsCondition(child, parent, True); other conditions stay in meta.
--origin real   keeps only config_file / builtin_default / cli_flag / env_var knobs.
--origin prompt keeps only prompt_text knobs.
"""
import argparse
import json
from pathlib import Path

from ConfigSpace import (Categorical, CategoricalHyperparameter, ConfigurationSpace, Constant, EqualsCondition,
                         Float, Integer)
import io

REAL = {"config_file", "builtin_default", "cli_flag", "env_var"}


def scalar(v):
    if isinstance(v, dict):
        v = v.get("profile", v.get("builtin", json.dumps(v, sort_keys=True)))
    if isinstance(v, (list, dict)):
        return json.dumps(v, sort_keys=True, default=str)
    if v is None:
        return "null"
    return v


def to_hp(k):
    name, dom, t = k["id"], k.get("domain"), k["type"]
    meta = {f: k.get(f) for f in ("category", "group", "stage", "origin", "component", "source", "domain_basis", "does")}
    meta["searchable"] = True
    d = scalar(k.get("default"))
    if isinstance(dom, dict) and "min" in dom and "max" in dom and t in ("int", "float"):
        lo, hi = dom["min"], dom["max"]
        try:
            dv = min(max(float(d), lo), hi)
        except (TypeError, ValueError):
            dv = lo
        if t == "int":
            return Integer(name, (int(lo), int(hi)), default=int(dv), meta=meta)
        return Float(name, (float(lo), float(hi)), default=float(dv), meta=meta)
    if isinstance(dom, list) and len(dom) >= 2:
        choices = [scalar(x) for x in dom]
        choices = list(dict.fromkeys(str(c) if not isinstance(c, (int, float, bool)) else c for c in choices))
        dflt = d if d in choices else (str(d) if str(d) in choices else choices[0])
        return Categorical(name, choices, default=dflt, meta=meta)
    if t == "bool":
        return Categorical(name, [True, False], default=bool(d) if isinstance(d, bool) else True, meta=meta)
    if k["origin"] == "prompt_text":
        meta["value_when_on"] = d if isinstance(d, (int, float, bool, str)) else str(d)
        return Categorical(name, ["on", "off"], default="on", meta=meta)
    meta["searchable"] = False
    return Constant(name, d if isinstance(d, (int, float, str)) else str(d), meta=meta)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("knobs_json")
    ap.add_argument("--origin", choices=["all", "real", "prompt"], default="all")
    ap.add_argument("-o", "--out")
    a = ap.parse_args()
    src = Path(a.knobs_json)
    doc = json.loads(src.read_text())
    knobs = doc["knobs"]
    if a.origin == "real":
        knobs = [k for k in knobs if k["origin"] in REAL]
    elif a.origin == "prompt":
        knobs = [k for k in knobs if k["origin"] == "prompt_text"]
    cs = ConfigurationSpace(name=f"{doc['harness']['name']}-{a.origin}",
                            meta={"harness": doc["harness"], "schema_version": doc["schema_version"]})
    hps = {}
    for k in knobs:
        hp = to_hp(k)
        hps[k["id"]] = hp
    cs.add(list(hps.values()))
    conds = []
    for k in knobs:
        for c in k.get("conditions", []) or []:
            parent = hps.get(c.strip())
            if parent is not None and isinstance(parent, CategoricalHyperparameter) and set(parent.choices) == {True, False} \
                    and parent.name != k["id"] and not isinstance(hps[k["id"]], Constant):
                conds.append(EqualsCondition(hps[k["id"]], parent, True))
    added = 0
    for c in conds:
        try:
            cs.add(c)
            added += 1
        except Exception:
            pass
    stem = src.name.replace(".knobs.json", "")
    out = Path(a.out) if a.out else src.with_name(f"{stem}.configspace{'' if a.origin == 'all' else '.' + a.origin}.json")
    buf = io.StringIO()
    cs.to_json(buf, indent=1)
    out.write_text(buf.getvalue())
    kinds = {}
    for hp in hps.values():
        kinds[type(hp).__name__] = kinds.get(type(hp).__name__, 0) + 1
    print(f"wrote {out}: {len(hps)} hyperparameters {kinds}, {added} conditions")


if __name__ == "__main__":
    main()
