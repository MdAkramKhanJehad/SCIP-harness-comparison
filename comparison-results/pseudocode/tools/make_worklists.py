"""Split every knob of both registries into work lists, one per pseudocode writer.

Each knob gets a target .pseudo file (where it should be read as θ["id"]):
  - config / CLI / env knobs: the stage or module where the value acts (prefix rules below)
  - everything else: the .pseudo file that mirrors its real source file
Writes tools/worklists/<group>.json and prints counts.
Run from pseudocode/:  python3 tools/make_worklists.py
"""
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
PSEUDO = HERE.parent
RESULTS = PSEUDO.parent
OUT = HERE / "worklists"
OUT.mkdir(exist_ok=True)

V = "vvaharness/"
ST = V + "pipeline/stages/"
VVAH_PREFIX = [
    (r"^step0\.", ST + "s0_seed.pseudo"),
    (r"^step1\.auto_exclude", ST + "s1_autoexclude.pseudo"),
    (r"^step1\.", ST + "s1_preprocess.pseudo"),
    (r"^inject\.", ST + "s1_preprocess.pseudo"),
    (r"^step2\.", ST + "s2/session.pseudo"),
    (r"^step4\.batch", ST + "s4/batching.pseudo"),
    (r"^step4\.", ST + "s4_deepdive.pseudo"),
    (r"^step5_detectors\.", ST + "s5/detectors.pseudo"),
    (r"^step5_prefilter\.", ST + "s5/gates.pseudo"),
    (r"^step6_verify\.", ST + "s6_verify.pseudo"),
    (r"^step6_exploit_verification\.", V + "exploit_verification/stub.pseudo"),
    (r"^step7_dedup\.", ST + "s7_dedup.pseudo"),
    (r"^step8\.", ST + "s8_chain.pseudo"),
    (r"^step9\.", ST + "s9_sarif.pseudo"),
    (r"^step_remediate\.", V + "remediation_agent/remediate.pseudo"),
    (r"^step_validate\.", ST + "s11_validate.pseudo"),
    (r"^playbook\.", V + "remediation_agent/playbook.pseudo"),
    (r"^policy\.", V + "remediation_agent/policy_gate.pseudo"),
    (r"^(models|sdk|openai|cache_markers|cache_min_block_tokens|cache_route|think_in_prompt|refusal_retries|pricing)\b",
     V + "backends/llm/registry.pseudo"),
    (r"^batch\.", V + "orchestrator/batch.pseudo"),
    (r"^(output|scan_progress)\.", V + "orchestrator/scan.pseudo"),
    (r"^(cli|cli_flag|env)\.", V + "orchestrator/entry.pseudo"),
]
VH_PREFIX = [
    (r"^(anthropic|scan|tls|telemetry|logging|oauth|audit|github|publish|sdk)\.", "vulnhunter-agent/agent/runner.pseudo"),
    (r"^sandbox\.", "vulnhunter-agent/agent/build_settings.pseudo"),
    (r"^issues\.", "vulnhunter-agent/agent/issues_extract.pseudo"),
    (r"^verify\.", "vulnhunter-agent/agent/verify_runner.pseudo"),
    (r"^cli\.", "vulnhunter-agent/agent/__main__.pseudo"),
    (r"^skill\.", "vulnhunt/SKILL.pseudo"),
]

# writer groups: (name, harness, regex on target path)
GROUPS = [
    ("vvah_s0_s3", "vvah", r"^vvaharness/(pipeline/stages/(s0_|s1_|s2|s3_)|rules/|codegraph/|detect/|models/scan/threat)"),
    ("vvah_s4", "vvah", r"^vvaharness/(pipeline/stages/s4|backends/harness/)"),
    ("vvah_skills_a", "vvah", r"^vvaharness/skills/(code-exploration|client-side|templates|missing-controls|hardcoded-creds|csrf|ssrf|iac)/"),
    ("vvah_s5_s9", "vvah", r"^vvaharness/(pipeline/stages/(s5|s6|s7|s8|s9)|exploit_verification/|models/scan/findings)|^\.env"),
    ("vvah_remediation_validation", "vvah", r"^(vvaharness/(remediation_agent|validation)/|vvaharness/pipeline/stages/s11|inputs/)"),
    ("vvah_core_and_skills_b", "vvah", r"."),   # orchestrator, config, backends/llm, replay, remaining skills
    ("vh_runner_recon", "vh", r"^(vulnhunter-agent/agent/(runner|config|__main__|build_settings|_llm|clone|auth)|vulnhunt/SKILL|vulnhunt/phases/(phase1_recon|phase3d_sweep)|vulnhunt/phases/_index)"),
    ("vh_hunt_shared", "vh", r"^vulnhunt/phases/phase2_(shared|hunt)"),
    ("vh_hunt_classes", "vh", r"^vulnhunt/phases/phase2_class_"),
    ("vh_verify_report", "vh", r"^(vulnhunt/phases/(phase2b|phase3_|phase3c|phase4)|vulnhunter-agent/agent/(issues_|verify_))"),
    ("vh_fix_core_a", "vh", r"^vulnhunter-fix/(SKILL|prompts/(implement|parse_issues))"),
    ("vh_fix_core_b", "vh", r"^vulnhunter-fix/prompts/(verify|deliver)"),
    ("vh_fix_workers", "vh", r"^vulnhunter-fix/(prompts/|config|scripts/)"),
    ("vh_fix_references", "vh", r"^vulnhunter-fix/references/"),
    ("vh_fixverify_bench", "vh", r"."),
]


def mirror(source):
    path = source.split(";")[0].strip().split(":")[0].strip()
    if path.endswith("/"):
        return path + "_index.pseudo"
    if path.startswith(".env") or path.startswith("vvaharness/exploit_verification/"):
        return "vvaharness/exploit_verification/stub.pseudo"
    if path == "vvaharness/config/__init__.py" or path.startswith("vvaharness/config/profiles/"):
        return None
    return re.sub(r"\.[A-Za-z0-9]+$", "", path) + ".pseudo"


def target(harness, k):
    rules = VVAH_PREFIX if harness == "vvah" else VH_PREFIX
    if k["origin"] in ("config_file", "builtin_default", "cli_flag", "env_var", "not_set") or not k["id"].startswith(("p.", "prompt.", "code.", "harness.")):
        for rx, t in rules:
            if re.search(rx, k["id"]):
                return t
    t = mirror(str(k.get("source", "")))
    if t is None:
        for rx, tt in rules:
            if re.search(rx, k["id"]):
                return tt
        return "vvaharness/config/__init__.pseudo"
    if harness == "vh" and t == "vulnhunter-agent/agent/config.pseudo":
        return "vulnhunter-agent/agent/runner.pseudo"
    return t


def load(fname):
    d = yaml.safe_load(open(RESULTS / fname))
    for cat, groups in d["categories"].items():
        for g, ks in groups.items():
            for k in ks:
                yield cat, g, k


def main():
    summary = {}
    for harness, fname in (("vvah", "vvah.knobs.yaml"), ("vh", "vulnhunter.knobs.yaml")):
        lists = defaultdict(list)
        for cat, g, k in load(fname):
            t = target(harness, k)
            grp = next(n for n, h, rx in GROUPS if h == harness and re.search(rx, t))
            row = dict(id=k["id"], target=t, category=cat, group=g, stage=k.get("stage"), origin=k["origin"],
                       type=k["type"], default=k.get("default"), requires=k.get("requires"),
                       does=k.get("does"), source=k.get("source"))
            if k.get("quote"):
                row["quote"] = k["quote"]
            lists[grp].append(row)
        for grp, rows in lists.items():
            rows.sort(key=lambda r: (r["target"], str(r["source"])))
            (OUT / f"{grp}.json").write_text(json.dumps(rows, indent=1, ensure_ascii=False, default=str))
            files = Counter(r["target"] for r in rows)
            summary[grp] = (len(rows), len(files))
            print(f"{grp:30s} {len(rows):5d} knobs  {len(files):3d} files")
    return summary


if __name__ == "__main__":
    main()
