#!/usr/bin/env python3
"""Flatten VVAH's built-in defaults and its five profiles into one table.

Reads the harness source read-only. Output: JSON {key: {builtin, builtin_line,
default, full, sdk, semgrep, taint}} on stdout. Keys are dotted config paths.
"""
import ast, json, sys
from pathlib import Path
import yaml

ROOT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[2] / "visa-vulnerability-agentic-harness"
CFG = ROOT / "vvaharness" / "config"
MISSING = "<unset>"

def flatten(d, prefix=""):
    out = {}
    for k, v in d.items():
        key = f"{prefix}{k}"
        if isinstance(v, dict) and v:
            out.update(flatten(v, key + "."))
        else:
            out[key] = v
    return out

def builtin_defaults():
    src = (CFG / "__init__.py").read_text()
    tree = ast.parse(src)
    lines = {}
    for node in tree.body:
        tgt = None
        if isinstance(node, ast.Assign):
            tgt = node.targets[0]
        elif isinstance(node, ast.AnnAssign):
            tgt = node.target
        if isinstance(tgt, ast.Name) and tgt.id == "_STEP_DEFAULTS":
            def walk(n, prefix=""):
                out = {}
                for k, v in zip(n.keys, n.values):
                    key = prefix + ast.literal_eval(k)
                    if isinstance(v, ast.Dict) and v.keys:
                        out.update(walk(v, key + "."))
                    else:
                        try:
                            val = ast.literal_eval(v)
                        except Exception:
                            val = "<expr> " + ast.unparse(v)
                        out[key] = val
                        lines[key] = v.lineno
                return out
            return walk(node.value), lines
    raise SystemExit("_STEP_DEFAULTS not found")

def main():
    builtin, lines = builtin_defaults()
    profiles = {}
    for p in ("default", "full", "sdk", "semgrep", "taint"):
        profiles[p] = flatten(yaml.safe_load((CFG / "profiles" / f"{p}.yaml").read_text()))
    keys = list(builtin)
    for p in profiles.values():
        for k in p:
            if k not in keys:
                keys.append(k)
    table = {}
    for k in keys:
        row = {"builtin": builtin.get(k, MISSING), "builtin_line": lines.get(k)}
        for p, vals in profiles.items():
            row[p] = vals.get(k, MISSING)
        table[k] = row
    json.dump(table, sys.stdout, indent=1, default=list)

if __name__ == "__main__":
    main()
