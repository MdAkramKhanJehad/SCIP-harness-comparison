#!/usr/bin/env python3
"""Build the two knob registries (vvah.knobs.yaml, vulnhunter.knobs.yaml).

VVAH config values are read from the harness source by dump_vvah_knobs.py, so
they are never transcribed by hand. Classification, descriptions and every
knob that lives in a prompt, a code constant, a CLI flag or an env var are
curated in this file. Run:  python3 tools/build_registry.py
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from collections import OrderedDict
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
OUT = HERE.parent
ROOT = OUT.parent
UNSET = "<unset>"

# --------------------------------------------------------------------------
# Shared taxonomy: parent category -> what it means. Both files use the same
# category names so a knob in one harness can be lined up with the other.
# --------------------------------------------------------------------------
CATEGORY_GUIDE = OrderedDict([
    ("model_routing", "Which model answers each role, through which backend, and how much it reasons."),
    ("budget_and_termination", "What stops a session or a run: turn, call, token, cost and wall-clock limits, retries and stall handling."),
    ("decomposition_and_parallelism", "How the work is split into units and how many run at once."),
    ("scope_and_coverage", "Which code is in scope and what caps the amount of code or findings examined."),
    ("context_supply", "What the model is shown: evidence blocks, inlined source, skills, knowledge bases, injected files."),
    ("tool_access", "Which tools a session may call, how often, and under what sandbox or permission mode."),
    ("detection_method", "The search strategy the prompts impose: tracing direction, mandatory checks, planning."),
    ("gating_and_thresholds", "Rules a candidate must pass to survive: hard gates, confidence floors, evidence gates, severity rules."),
    ("verification_depth", "Second opinions after detection: adversarial review, exploit testing, sweeps, fix validation."),
    ("dedup_and_merge", "When two findings count as one, and when they must stay separate."),
    ("ranking_and_reporting", "Ranking, chaining, output formats and issue filing."),
    ("remediation", "The fix stage: whether it runs, its limits and its policy."),
    ("runtime_and_infra", "Plumbing that should not change what is found: credentials, TLS, caching, paths, telemetry, hardening."),
    ("evaluation", "Benchmark and scoring machinery around the scanner."),
])

SCHEMA = OrderedDict([
    ("id", "Unique knob name. VVAH: the dotted config path. VulnHunter: section.key for real config, a descriptive dotted name otherwise."),
    ("does", "One sentence on what the knob controls."),
    ("stage", "Pipeline stage that reads it."),
    ("origin", "Where the knob was collected from. Actual configuration: config_file (set in a shipped config or profile file), builtin_default (only in the code's default table, no shipped file sets it), cli_flag, env_var. Not configuration: prompt_text (a rule or number written in a prompt), code_constant (hard-coded in source), not_set (the harness sets nothing)."),
    ("kind", "explicit = a declared setting an operator can change without editing code or prompts. implicit = a value buried in prompt prose or source code. absent = the harness sets nothing here and the SDK default applies."),
    ("type", "bool | int | float | str | enum | list | map."),
    ("domain", "Values the knob can take. A list is a set of values; {min, max} is a numeric range."),
    ("domain_basis", "code = the legal set is defined by the harness. observed = only the values seen in shipped configs. suggested = my proposed exploration range, not from the source."),
    ("default", "Value that runs. VVAH: {builtin: value in _STEP_DEFAULTS, profile: value in default.yaml}; a missing side means that layer does not set it."),
    ("profiles", "VVAH only: profiles whose value differs from default.yaml."),
    ("source", "File (and line where known), relative to the harness root."),
    ("quote", "Prompt-text knobs from the exhaustive pass only: the exact text at the cited line, checked by script against the file."),
    ("requires", "Condition under which the knob has any effect."),
    ("affects", "Outcomes it is expected to move: recall | precision | cost | latency | safety | reliability | reporting."),
])


def K(id, cat, stage, default, does, source, origin="prompt_text", kind=None,
      type=None, domain=None, basis=None, requires=None, affects=None):
    """One hand-curated knob."""
    if kind is None:
        kind = {"prompt_text": "implicit", "code_constant": "implicit", "not_set": "absent"}.get(origin, "explicit")
    if type is None:
        type = _type_of(default)
    row = OrderedDict(id=id, does=does, stage=stage, origin=origin, kind=kind, type=type)
    if domain is None and type == "bool":
        domain, basis = [True, False], "code"
    if domain is not None:
        if type in ("int", "float") and isinstance(domain, list) and len(domain) == 2:
            domain = {"min": domain[0], "max": domain[1]}
        row["domain"] = domain
        row["domain_basis"] = basis or "suggested"
    row["default"] = default
    row["source"] = source
    row["requires"] = requires
    row["affects"] = affects or []
    return cat, row


def _type_of(v):
    if isinstance(v, bool):
        return "bool"
    if isinstance(v, int):
        return "int"
    if isinstance(v, float):
        return "float"
    if isinstance(v, (list, tuple)):
        return "list"
    if isinstance(v, dict):
        return "map"
    return "str"


# ==========================================================================
# VVAH
# ==========================================================================
EFFORT = ["low", "medium", "high", "xhigh", "max"]
VIA = ["cli", "sdk", "openai", "deepagents"]

STAGE_OF_PREFIX = [
    ("step0", "S0"), ("step1", "S1"), ("step2", "S2"), ("step3", "S3"), ("step4", "S4"),
    ("step5_prefilter", "S5"), ("step5_detectors", "S5"), ("step6_verify", "S6"),
    ("step6_exploit_verification", "S6-EV"), ("step7_dedup", "S7"), ("step8", "S8"),
    ("step9", "S9"), ("step_remediate", "S10"), ("step_validate", "S11"),
]
ROLE_STAGE = {
    "autoexclude": "S1-auto", "preprocess": "S1", "threatmodel": "S2", "decompose": "S3",
    "deepdive": "S4", "verify": "S6", "dedup": "S7", "chain": "S8", "remediate": "S10",
    "validate": "S11", "exploit_verification": "S6-EV",
}
NO_CALL_ROLES = {"preprocess": "S1 makes no model call", "decompose": "S3 makes no model call",
                 "dedup": "only called when step7_dedup.semantic is true"}


def stage_of(key):
    for p, s in STAGE_OF_PREFIX:
        if key == p or key.startswith(p + "."):
            return s
    if key.startswith("models."):
        return ROLE_STAGE.get(key.split(".")[1], "global")
    return "global"


# key -> (category.group, does, affects, extra)   extra: domain/basis/requires
VV = {}


def v(key, cg, does, affects, **extra):
    VV[key] = (cg, does, affects.split(), extra)


EV_REQ = "exploit verification armed (EV_API_COLLECTION set; enabled != false)"

# --- step0 / step1 --------------------------------------------------------
v("step0.callgraph_detection", "scope_and_coverage.seed_detection", "How S0 finds entry points and sinks; only pattern rules ship.", "recall")
v("step0.languages", "scope_and_coverage.exclusions", "Optional language filter applied to the static seed.", "recall cost")
v("step0.min_graph_nodes_for_gate", "gating_and_thresholds.evidence_gates", "A code graph with fewer nodes is treated as degenerate and the graph evidence gates stand down.", "precision reliability")
v("step1.max_file_kb", "scope_and_coverage.exclusions", "Files larger than this are left out of scope.", "recall cost")
v("step1.auto_exclude", "scope_and_coverage.exclusions", "Run one model call that proposes extra exclusions from a repo survey. CLI --auto-step1 / --no-auto-step1 override it.", "recall cost")
v("step1.auto_exclude_max_tokens", "budget_and_termination.output_tokens", "Token cap for the auto-exclude survey call.", "cost", requires="step1.auto_exclude")
v("step1.auto_exclude_effort", "model_routing.reasoning", "Reasoning tier for the auto-exclude survey call.", "cost recall", requires="step1.auto_exclude", domain=EFFORT, basis="code")
v("step1.auto_exclude_protect_templates", "scope_and_coverage.exclusion_vetoes", "Veto model-proposed exclusions that would drop web templates (XSS surface).", "recall", requires="step1.auto_exclude")
v("step1.auto_exclude_protect_key_material", "scope_and_coverage.exclusion_vetoes", "Veto model-proposed exclusions of files named like key or credential material.", "recall", requires="step1.auto_exclude")
v("step1.auto_exclude_protect_secrets", "scope_and_coverage.exclusion_vetoes", "Veto model-proposed exclusions of files whose head content matches a secret pattern.", "recall", requires="step1.auto_exclude")
v("step1.auto_exclude_protect_client_sinks", "scope_and_coverage.exclusion_vetoes", "Veto model-proposed exclusions of first-party JS/TS where the DOM-sink detector fires.", "recall", requires="step1.auto_exclude")
v("step1.follow_symlinks", "runtime_and_infra.hostile_repo_hardening", "Back-compat toggle; off-root symlink targets are dropped regardless.", "safety")
v("step1.allowed_tools", "tool_access.tool_allowlist", "Set in the profiles but not registered in the built-in table; S1 makes no agentic call, so treat as inert until a reader is confirmed.", "")
v("step1.exclude_dirs", "scope_and_coverage.exclusions", "Directory names removed from scope (appended to built-in excludes).", "recall cost")
v("step1.exclude_exts", "scope_and_coverage.exclusions", "File extensions removed from scope.", "recall cost")
v("step1.exclude_globs", "scope_and_coverage.exclusions", "Glob patterns removed from scope.", "recall cost")
v("step1.config_dedup.enabled", "scope_and_coverage.exclusions", "Collapse clusters of near-identical config files to representatives.", "cost recall")
v("step1.config_dedup.min_cluster_size", "scope_and_coverage.exclusions", "Smallest cluster of similar config files that gets collapsed (meaning inferred from the key name).", "cost recall", requires="step1.config_dedup.enabled")
v("step1.config_dedup.keep_per_top_dir", "scope_and_coverage.exclusions", "Keep a representative per top-level directory (meaning inferred from the key name).", "recall", requires="step1.config_dedup.enabled")
v("step1.config_dedup.promote_on_secret_hit", "scope_and_coverage.exclusions", "Keep a config file in scope when it contains a secret match (meaning inferred from the key name).", "recall", requires="step1.config_dedup.enabled")
v("step1.config_dedup.promote_on_insecure_value", "scope_and_coverage.exclusions", "Keep a config file in scope when it holds an insecure value (meaning inferred from the key name).", "recall", requires="step1.config_dedup.enabled")

# --- step2 ----------------------------------------------------------------
v("step2.max_threats", "scope_and_coverage.coverage_ceilings", "Cap on threats in the threat model. S4 only examines files named by a threat, so this bounds the whole scan.", "recall cost")
v("step2.empty_retry", "budget_and_termination.retries_and_recovery", "One re-ask when the threat model comes back empty, degenerate or schema-rejected.", "reliability")
v("step2.baseline", "detection_method.mandatory_checks", "Inject a baseline checklist for the detected repo kind (web-api, mobile, native, iac, library, web-template) that S2 must dispose of.", "recall")
for _k, _d in [
    ("max_doc_chars", "Characters of repo docs (README, SECURITY, ARCHITECTURE...) packed into the S2 prompt."),
    ("max_manifest_chars", "Characters kept per build manifest."),
    ("max_modules", "Graph modules gathered as evidence."),
    ("max_entry_points", "Entry points gathered as evidence."),
    ("max_config_reps", "Config-file representatives listed."),
    ("max_api_artefacts", "API artefacts (OpenAPI, Postman...) listed."),
    ("max_graph_files", "Graph files in the frontier view."),
    ("max_graph_sinks", "Graph sinks in the frontier view."),
    ("max_graph_edges", "Graph edges in the frontier view."),
    ("max_prompt_modules", "Modules actually printed in the prompt (truncation cap)."),
    ("max_prompt_entry_points", "Entry points actually printed in the prompt (truncation cap)."),
    ("max_inventory_files", "Files listed in the FILE INVENTORY block."),
    ("max_assets", "Cap on assets in the threat model."),
    ("max_trust_boundaries", "Cap on trust boundaries in the threat model."),
    ("max_manifest_depth", "Directory depth searched for manifests."),
    ("max_manifests", "Number of manifests included."),
    ("max_manifests_per_kind", "Manifests included per manifest kind."),
    ("max_manifest_total_chars", "Total characters across all manifests."),
    ("max_config_rep_chars", "Characters kept per config representative body."),
    ("max_config_rep_bodies", "How many config representatives are shown with (redacted) bodies; the rest are path-only."),
]:
    v("step2." + _k, "context_supply.s2_evidence_caps", _d + " 0 means emit none of this block.", "recall cost")
v("step2.bash", "tool_access.shell", "Give the S2 session a shell. Shell commands are not path-jailed.", "recall safety")
v("step2.allowed_tools", "tool_access.tool_allowlist", "Read-only tools for the S2 session; validated against {Read, Glob, Grep}.", "recall cost", domain=[["Read"], ["Read", "Grep"], ["Read", "Glob", "Grep"]], basis="code")
v("step2.graph_tools", "tool_access.graph_and_kb_tools", "Give S2 the code-graph query tools.", "recall precision")
v("step2.graph_tool_budget", "tool_access.graph_and_kb_tools", "Total graph-tool calls allowed in the S2 session.", "recall cost", requires="step2.graph_tools")
v("step2.require_graph", "gating_and_thresholds.evidence_gates", "Reject the threat model until the session has called a graph tool.", "precision", requires="step2.graph_tools and a non-degenerate graph")
v("step2.require_graph_rejections", "gating_and_thresholds.evidence_gates", "How many rejections before the graph requirement relents.", "precision cost", requires="step2.require_graph")
v("step2.planning", "detection_method.planning", "Force a write_todos plan first: one todo per directory group, request handlers last, then reconcile the inventory.", "recall cost latency")
v("step2.skills", "context_supply.injected_knowledge", "Mount the 17 skill playbooks into the S2 session.", "recall precision", requires="via == deepagents")

# --- step4 ----------------------------------------------------------------
v("step4.parallel", "decomposition_and_parallelism.concurrency", "Deep-dive sessions running at once.", "latency reliability")
v("step4.batch_size", "decomposition_and_parallelism.batching", "Investigation units per session, grouped by file overlap; LARGE units run alone.", "cost recall")
v("step4.split_retry", "budget_and_termination.retries_and_recovery", "Retry a failed batch as one session per lost unit.", "reliability cost", requires="step4.batch_size > 1")
v("step4.allowed_tools", "tool_access.tool_allowlist", "Read-only tools for the S4 session.", "recall")
v("step4.bash", "tool_access.shell", "Give the S4 session a shell (unjailed).", "recall safety")
v("step4.line_bucket", "dedup_and_merge.dedup_rules", "Line-bucket size used when keying S4 findings to a site (meaning inferred from the key name).", "precision")
v("step4.max_findings_per_run", "scope_and_coverage.coverage_ceilings", "Cap on findings one unit may emit; the overflow is counted as truncated.", "recall cost")
v("step4.cwe_tools", "tool_access.graph_and_kb_tools", "Give S4 the CweGuidance knowledge-base tool.", "precision")
v("step4.cwe_tool_budget", "tool_access.graph_and_kb_tools", "CweGuidance calls allowed per session.", "precision cost", requires="step4.cwe_tools")
v("step4.graph_tool_budget", "tool_access.graph_and_kb_tools", "Graph-tool calls allowed per session.", "recall cost")
v("step4.planning", "detection_method.planning", "Force a write_todos plan before investigating; also what makes the evidence gate enforceable.", "recall cost latency")
v("step4.inline_source", "context_supply.source_delivery", "Put the surface files in the prompt whole instead of making the model Read them.", "cost recall")
v("step4.evidence_gate", "gating_and_thresholds.evidence_gates", "Reject a verdict until every plan todo is complete and a graph tool was called.", "precision recall", requires="step4.planning and via == deepagents (otherwise telemetry only)")
v("step4.evidence_gate_refusals", "gating_and_thresholds.evidence_gates", "Rejections before the evidence gate relents.", "precision cost", requires="step4.evidence_gate")
v("step4.skills", "context_supply.injected_knowledge", "Mount the 17 skill playbooks into the S4 session.", "recall precision", requires="via == deepagents")
v("step4.require_graph", "gating_and_thresholds.evidence_gates", "Require a graph-tool call before a verdict.", "precision", requires="non-degenerate graph")
v("step4.max_extra_cwes", "scope_and_coverage.coverage_ceilings", "Extra CWEs per finding that fan out into their own findings.", "recall precision")

# --- step5 ----------------------------------------------------------------
v("step5_prefilter.sink_reanchor", "dedup_and_merge.location_normalisation", "Move a finding anchored on a function header to the nearest matching sink call (Python AST).", "precision reporting")
v("step5_prefilter.sink_reanchor_max_move_lines", "dedup_and_merge.location_normalisation", "Furthest a finding may be moved when re-anchored.", "precision", requires="step5_prefilter.sink_reanchor")
v("step5_prefilter.line_tolerance", "dedup_and_merge.dedup_rules", "Line distance within which two findings at the same site collapse before S6. Falls back to step7_dedup.line_tolerance when unset.", "precision recall")
v("step5_detectors.enabled", "detection_method.deterministic_detectors", "Run the zero-LLM pattern detectors (cookie flags, unescaped template sinks...). All or nothing.", "recall cost")
v("step5_detectors.max_rows", "detection_method.deterministic_detectors", "Detector rows one scan may add; each becomes S6 work. <= 0 removes the cap.", "recall cost", requires="step5_detectors.enabled")

# --- step6 verify ---------------------------------------------------------
v("step6_verify.parallel", "decomposition_and_parallelism.concurrency", "Verification sessions running at once.", "latency reliability")
v("step6_verify.batch_size", "decomposition_and_parallelism.batching", "Findings per verification session, sorted by file.", "cost precision")
v("step6_verify.min_confidence", "gating_and_thresholds.confidence", "A TRUE_POSITIVE below this confidence (0-10) is dropped as unconfirmed.", "precision recall", domain={"min": 0, "max": 10}, basis="code")
v("step6_verify.max_budget_usd", "budget_and_termination.cost_caps", "Dollar cap per verification session. Enforced only on the cli route; accepted and ignored on sdk.", "cost", requires="via == cli")
v("step6_verify.tool_timeout_s", "budget_and_termination.wall_clock", "Per-tool timeout; null keeps the vendor default (5s glob, 15s grep).", "reliability")
v("step6_verify.inline_source", "context_supply.source_delivery", "Hand the batch its files whole so no Read turn is needed.", "cost precision")
v("step6_verify.graph_tools", "tool_access.graph_and_kb_tools", "Give S6 the code-graph tools for reachability.", "precision")
v("step6_verify.graph_tool_budget", "tool_access.graph_and_kb_tools", "Graph-tool calls per finding in the batch (multiplied by batch size).", "precision cost", requires="step6_verify.graph_tools")
v("step6_verify.require_graph", "gating_and_thresholds.evidence_gates", "Require a graph-tool call before a verdict. Off: an earlier gate cost more true positives than it saved.", "precision recall")
v("step6_verify.evidence_gate_refusals", "gating_and_thresholds.evidence_gates", "Rejections per finding before the graph requirement relents.", "precision cost", requires="step6_verify.require_graph")
v("step6_verify.batch_wall_clock_ceiling", "budget_and_termination.wall_clock", "Hard ceiling per batch in seconds; a late batch is split or becomes VERIFY_ERROR.", "reliability latency")
v("step6_verify.trait_stamps", "ranking_and_reporting.channels", "Verifier stamps control-absence and posture traits in its reply.", "reporting")
v("step6_verify.reframe_enabled", "verification_depth.adversarial_review", "Let the verifier relabel a claim whose framing is wrong instead of returning FALSE_POSITIVE.", "recall precision")
v("step6_verify.split_retry", "budget_and_termination.retries_and_recovery", "Re-submit a truncated, rejected or timed-out batch as single-finding batches.", "reliability cost", requires="step6_verify.batch_size > 1")
v("step6_verify.progress_file", "runtime_and_infra.observability", "Append one line per verification session to a progress log. CLI --s6-progress-file turns it on.", "")
v("step6_verify.allowed_tools", "tool_access.tool_allowlist", "Read-only tools for the S6 session.", "precision")

# --- step6 exploit verification ------------------------------------------
ev = "step6_exploit_verification."
v(ev + "enabled", "verification_depth.exploit_testing", "Live HTTP exploit verification. auto = on when EV_API_COLLECTION is set.", "precision safety")
v(ev + "on_unreachable", "verification_depth.exploit_testing", "What to do when the target cannot be reached.", "reliability", requires=EV_REQ)
v(ev + "ev_overrides_static", "verification_depth.exploit_testing", "Let a live result replace the static S6 verdict. False everywhere: EV only adds confirmation.", "precision recall", requires=EV_REQ)
v(ev + "parallel", "decomposition_and_parallelism.concurrency", "Findings exploit-tested at once.", "latency", requires=EV_REQ)
v(ev + "store_probes", "runtime_and_infra.observability", "Persist the probes that were sent.", "", requires=EV_REQ)
v(ev + "timeout_s", "budget_and_termination.wall_clock", "Per-request HTTP timeout.", "reliability", requires=EV_REQ)
v(ev + "safe_mode", "tool_access.live_traffic_safety", "Restrict payloads to non-destructive ones.", "safety", requires=EV_REQ)
v(ev + "allow_state_changing_methods", "tool_access.live_traffic_safety", "Allow POST/PUT/DELETE-style requests against the target.", "safety recall", requires=EV_REQ)
v(ev + "rate_limit_rps", "tool_access.live_traffic_safety", "Requests per second against the target; 0 = unlimited.", "safety latency", requires=EV_REQ)
v(ev + "max_concurrency_target", "tool_access.live_traffic_safety", "Concurrent requests against the whole target; 0 = no cap.", "safety latency", requires=EV_REQ)
v(ev + "max_concurrency_endpoint", "tool_access.live_traffic_safety", "Concurrent requests against one endpoint.", "safety latency", requires=EV_REQ)
v(ev + "max_requests_per_finding", "budget_and_termination.request_caps", "Request budget per finding, shared by the fixed payload set and the attacker loop.", "cost precision", requires=EV_REQ)
v(ev + "max_payloads_per_finding", "budget_and_termination.request_caps", "Size of the deterministic payload set tried before the attacker agent.", "cost precision", requires=EV_REQ)
v(ev + "oob", "verification_depth.exploit_testing", "Out-of-band callback listener for blind findings.", "precision", requires=EV_REQ)
v(ev + "on_auth_failure", "runtime_and_infra.target_auth", "Behaviour when target authentication fails.", "reliability", requires=EV_REQ)
v(ev + "auth_expiry_skew_s", "runtime_and_infra.target_auth", "Seconds before expiry at which the target token is refreshed.", "reliability", requires=EV_REQ)
v(ev + "max_reauth", "runtime_and_infra.target_auth", "Re-authentication attempts.", "reliability", requires=EV_REQ)
v(ev + "ev_replay_variants", "verification_depth.fix_validation", "ev-replay re-sends payload variants after a fix.", "precision", requires="vvaharness ev-replay")
v(ev + "classify.batch", "decomposition_and_parallelism.batching", "Findings per classify call (attack vs skip).", "cost", requires=EV_REQ)
v(ev + "classify.parallel", "decomposition_and_parallelism.concurrency", "Classify calls in flight.", "latency", requires=EV_REQ)
v(ev + "mapper.parallel", "decomposition_and_parallelism.concurrency", "Mapping sessions in flight.", "latency", requires=EV_REQ)
v(ev + "mapper.endpoint_index.chunk", "decomposition_and_parallelism.batching", "Endpoints per endpoint-index session.", "cost", requires=EV_REQ)
v(ev + "mapper.finding_map.chunk", "decomposition_and_parallelism.batching", "Findings per finding-map session.", "cost", requires=EV_REQ)
v(ev + "mapper.finding_map.max_endpoints", "scope_and_coverage.coverage_ceilings", "Ranked endpoints kept per finding.", "recall cost", requires=EV_REQ)
v(ev + "attacker.enabled", "verification_depth.exploit_testing", "Run the adaptive attacker agent after the fixed payload set fails.", "precision cost", requires=EV_REQ)
v(ev + "attacker.max_tool_result_chars", "context_supply.source_delivery", "Characters of each HTTP response shown to the attacker.", "cost precision", requires=EV_REQ)
v(ev + "judge.max_records", "context_supply.source_delivery", "Probe records shown to the judge.", "cost precision", requires=EV_REQ)

# --- step7 / step8 / step9 ------------------------------------------------
v("step7_dedup.line_tolerance", "dedup_and_merge.dedup_rules", "Line distance within which same-file, same-class findings collapse.", "precision recall")
v("step7_dedup.semantic", "dedup_and_merge.dedup_rules", "Add one model call that judges duplicates ('one fix closes both'). False in all five profiles.", "precision cost")
v("step7_dedup.per_sink_keep", "dedup_and_merge.merge_rules", "When the semantic pass says a group has independent sink sites, keep each sink line as a location.", "recall", requires="step7_dedup.semantic")
v("step8.prompt_token_budget", "context_supply.source_delivery", "Input-token guard for the finding table handed to the chain call.", "cost")
v("step8.hop_text", "context_supply.source_delivery", "Add each finding's scenario and preconditions to the chain prompt.", "precision cost")
v("step8.severity_lift_gate", "ranking_and_reporting.chains", "Cap a chain's severity at its strongest member unless every link is cited.", "precision reporting")
v("step8.chain_quality_checks", "ranking_and_reporting.chains", "Emit per-chain annotations and the unpromoted-link disclosure.", "reporting")
v("step8.chain_dedup", "ranking_and_reporting.chains", "Collapse identical chains and annotate near-duplicates.", "reporting")
v("step8.prompt_fact_blocks", "context_supply.source_delivery", "Feed the chain call deterministic entry-point and deployment facts.", "precision")
v("step9.duplicate_result_guard", "ranking_and_reporting.output_files", "Skip SARIF results identical on the dedup key.", "reporting")

# --- remediate / validate -------------------------------------------------
v("step_remediate.enabled", "remediation.enablement", "Run the fix stage (S10) after detection. CLI --remediate also turns it on.", "safety cost")
v("step_remediate.enforce_policy", "remediation.policy", "Apply the remediation policy gates (pre-gate by CWE, post-gate reverting forbidden paths).", "safety")
v("step_remediate.top_n_findings", "remediation.limits", "How many findings, by CVSS, get a fix session. CLI --top overrides.", "cost")
v("step_remediate.max_budget_usd", "budget_and_termination.cost_caps", "Dollar cap per fix session (cli / Agent SDK routes only).", "cost")
v("step_remediate.policy_file", "remediation.policy", "Override path for the remediation policy.", "safety")
v("step_remediate.playbook_file", "remediation.policy", "Override path for the fix-strategy playbook.", "safety")
v("step_remediate.allowed_tools", "tool_access.tool_allowlist", "Tools for the fix session, including Edit and Write.", "safety")
v("step_validate.enabled", "verification_depth.fix_validation", "Run the 3-persona validation panel (S11) on each fix.", "precision cost")
v("step_validate.max_budget_usd", "budget_and_termination.cost_caps", "Dollar cap per validation session.", "cost", requires="step_validate.enabled")
v("step_validate.max_findings", "verification_depth.fix_validation", "Fix cases validated per run.", "cost", requires="step_validate.enabled")
v("step_validate.orchestrator_max_model_calls", "budget_and_termination.turn_and_call_caps", "Model calls for the validation orchestrator before a forced report; 0 = none.", "cost", requires="step_validate.enabled")
v("step_validate.allowed_tools", "tool_access.tool_allowlist", "Read-only tools for validation sessions.", "safety")

# --- output / global ------------------------------------------------------
v("output.emit_unreachable_appendix", "ranking_and_reporting.output_files", "Add an appendix of findings judged unreachable.", "reporting")
v("output.posture_channel", "ranking_and_reporting.channels", "Render posture findings in their own report subsection.", "reporting")
v("output.preserve_on_cleanup", "ranking_and_reporting.output_files", "Directories kept when a batch clone is cleaned up.", "reporting")
v("output.ingest_url", "ranking_and_reporting.output_files", "Endpoint results are uploaded to.", "reporting")
v("output.ingest_token", "runtime_and_infra.credentials_and_tls", "Token for the ingest endpoint.", "")
v("output.ingest_verify", "runtime_and_infra.credentials_and_tls", "Verify TLS on the ingest upload.", "safety")
v("cli.mcp_tools", "tool_access.graph_and_kb_tools", "On the cli route, publish stage tools (graph, CweGuidance) through an in-process MCP server.", "recall precision", requires="via == cli")
v("cli.restricted", "tool_access.sandbox_and_permissions", "Pass --restricted on the cli route: the only read jail that route has.", "safety", requires="via == cli")
v("cli.effort", "model_routing.reasoning", "Global reasoning tier for every cli-route call.", "recall precision cost", requires="via == cli", domain=EFFORT, basis="code")
v("cli.verify_ssl", "runtime_and_infra.credentials_and_tls", "Verify TLS for the Claude CLI gateway.", "safety")
v("cli.ca_cert", "runtime_and_infra.credentials_and_tls", "CA bundle for the Claude CLI gateway.", "")
v("cache_min_block_tokens", "runtime_and_infra.caching", "Override of the per-model minimum cacheable block size.", "cost")
v("cache_markers", "runtime_and_infra.caching", "Place prompt-cache markers on the cli, sdk and openai routes.", "cost", domain=["on", "off"], basis="code")
v("cache_route", "runtime_and_infra.caching", "Which cache-marker regime the endpoint honours.", "cost", domain=["auto", "anthropic", "vertex", "bedrock", "none"], basis="code")
v("think_in_prompt", "model_routing.reasoning", "Replace native thinking with a written-reasoning instruction appended to the system prompt.", "cost latency recall precision", requires="via == deepagents and model accepts it")
v("refusal_retries", "budget_and_termination.retries_and_recovery", "Identical resends of a refused call (Anthropic routes only). 0 also disables the S6 refused-batch split.", "reliability", domain=[0, 1], basis="code")
v("pricing.file", "runtime_and_infra.observability", "Price table used to cost the run manifest; none bundled.", "")
v("sdk.api_key", "runtime_and_infra.credentials_and_tls", "API key for the Anthropic SDK / deepagents route.", "")
v("sdk.base_url", "runtime_and_infra.credentials_and_tls", "Base URL for the Anthropic SDK / deepagents route.", "")
v("sdk.verify_ssl", "runtime_and_infra.credentials_and_tls", "Verify TLS on the Anthropic route.", "safety")
v("sdk.ca_cert", "runtime_and_infra.credentials_and_tls", "CA bundle for the Anthropic route.", "")
v("sdk.client_cert", "runtime_and_infra.credentials_and_tls", "Client certificate for the Anthropic route.", "")
v("sdk.cache_markers", "runtime_and_infra.caching", "The only cache-marker switch that reaches the deepagents route.", "cost", domain=["on", "off"], basis="code")
v("sdk.plugins", "tool_access.graph_and_kb_tools", "Graph plugins. The semgrep plugin adds 4 read-only tools to S2, S4 and S6.", "recall precision cost")
v("openai.api_key", "runtime_and_infra.credentials_and_tls", "API key for the OpenAI-compatible route.", "")
v("openai.base_url", "runtime_and_infra.credentials_and_tls", "Base URL for the OpenAI-compatible route.", "")
v("openai.verify_ssl", "runtime_and_infra.credentials_and_tls", "Verify TLS on the OpenAI-compatible route.", "safety")
v("openai.ca_cert", "runtime_and_infra.credentials_and_tls", "CA bundle for the OpenAI-compatible route.", "")
v("inject.cve_file", "context_supply.injected_knowledge", "Known-CVE list injected into S1/S2.", "recall")
v("inject.controls_file", "context_supply.injected_knowledge", "Design controls injected into S1/S2; S6 must show a bypass to keep a finding they cover.", "precision")
v("inject.cmdb_file", "context_supply.injected_knowledge", "Application profile (externally facing, PCI, PII) used for environmental severity.", "reporting")
v("batch.git_token", "runtime_and_infra.credentials_and_tls", "Token used to clone repos in batch mode.", "")
v("batch.git_base_url", "runtime_and_infra.state_and_paths", "Git host used in batch mode.", "")
v("batch.skip_repo_patterns", "scope_and_coverage.exclusions", "Repo-name patterns skipped in batch mode (test automation, e2e...).", "cost")
v("scan_progress.enabled", "runtime_and_infra.observability", "Show scan progress.", "")
v("scan_progress.style", "runtime_and_infra.observability", "Progress display style.", "")

# Pattern rules for the repeated per-stage keys. First match wins.
RULES = [
    (r"\.effort$", "model_routing.reasoning", "Reasoning tier this stage's calls send.", "recall precision cost latency", dict(domain=EFFORT, basis="code")),
    (r"\.max_turns$", "budget_and_termination.turn_and_call_caps", "Turn limit for the session. On the deepagents route this is a recursion floor (max_turns + 900), not a cap; a hard cap on sdk and cli.", "recall cost", {}),
    (r"\.max_model_calls$", "budget_and_termination.turn_and_call_caps", "Model calls per session; on the last one every tool but the outcome tool is withdrawn. 0 = unmetered.", "recall cost", {}),
    (r"\.max_tokens$", "budget_and_termination.output_tokens", "Output-token cap per call (harness ceiling 64000).", "cost reliability", {}),
    (r"\.replay_max_tokens$", "budget_and_termination.output_tokens", "Output cap for the tool-free replay after a deadline.", "cost reliability", {}),
    (r"\.(deadline|batch_deadline)$", "budget_and_termination.wall_clock", "Stage-owned wall clock per session in seconds; on expiry the session is resumed or replayed. 0 = no clock.", "latency recall", {}),
    (r"\.replay_timeout$", "budget_and_termination.wall_clock", "Seconds allowed for the tool-free transcript replay after a deadline.", "latency reliability", {}),
    (r"\.resume_timeout$", "budget_and_termination.wall_clock", "Seconds allowed to resume the live session after a deadline.", "latency reliability", {}),
    (r"\.timeout$", "budget_and_termination.wall_clock", "Backend wall clock in seconds; dropped on some routes (sdk/openai).", "latency reliability", {}),
]


def model_rule(key):
    parts = key.split(".")
    role = ".".join(parts[1:-1])
    leaf = parts[-1]
    note = NO_CALL_ROLES.get(parts[1])
    tail = f" Note: {note}." if note else ""
    if leaf == "id":
        return ("model_routing.model_choice", f"Model for the {role} role.{tail}", ["recall", "precision", "cost"], {})
    if leaf == "via":
        return ("model_routing.backend_route", f"Backend for the {role} role. Changes what max_turns, budgets and tools mean.{tail}", ["recall", "cost", "reliability"], dict(domain=VIA, basis="code"))
    if leaf == "provider":
        return ("model_routing.backend_route", f"Provider behind deepagents for the {role} role.{tail}", ["cost", "reliability"], dict(domain=["anthropic", "openai"], basis="observed", requires="via == deepagents"))
    if leaf == "temperature":
        return ("model_routing.reasoning", f"Sampling temperature for the {role} role. Dropped on the cli route.", ["recall", "precision"], {})
    return None


def classify_vvah(key):
    if key in VV:
        cg, does, aff, extra = VV[key]
        return cg, does, aff, dict(extra)
    if key.startswith("models."):
        r = model_rule(key)
        if r:
            return r
    for rx, cg, does, aff, extra in RULES:
        if re.search(rx, key):
            return cg, does, aff.split(), dict(extra)
    return None


def vvah_rows():
    table = json.loads(subprocess.check_output([sys.executable, str(HERE / "dump_vvah_knobs.py")]))
    rows, unclassified = [], []
    for key, r in table.items():
        if key == "step3":
            continue  # empty dict: step3 has no live keys
        c = classify_vvah(key)
        if c is None:
            unclassified.append(key)
            continue
        cg, does, aff, extra = c
        builtin, prof = r["builtin"], r["default"]
        default = OrderedDict()
        if builtin != UNSET:
            default["builtin"] = builtin
        if prof != UNSET:
            default["profile"] = prof
        others = OrderedDict()
        for p in ("full", "sdk", "semgrep", "taint"):
            if r[p] != prof:
                others[p] = "unset" if r[p] == UNSET else r[p]
        seen = [x for x in [builtin, prof] + [r[p] for p in ("full", "sdk", "semgrep", "taint")] if x != UNSET and x is not None]
        sample = seen[0] if seen else None
        typ = _type_of(sample) if sample is not None else "str"
        if "domain" in extra and typ == "str":
            typ = "enum"
        origin = "config_file" if prof != UNSET else "builtin_default"
        src = "vvaharness/config/profiles/default.yaml" if builtin == UNSET else f"vvaharness/config/__init__.py:{r['builtin_line']}"
        if builtin != UNSET and prof != UNSET:
            src += " ; vvaharness/config/profiles/default.yaml"
        row = OrderedDict(id=key, does=does, stage=stage_of(key), origin=origin, kind="explicit", type=typ)
        if "domain" in extra:
            row["domain"], row["domain_basis"] = extra["domain"], extra.get("basis", "code")
        elif typ == "bool":
            row["domain"], row["domain_basis"] = [True, False], "code"
        elif typ in ("int", "float", "str"):
            uniq = []
            for x in seen:
                if x not in uniq:
                    uniq.append(x)
            if not any(isinstance(x, str) and x.startswith("${") for x in uniq) and uniq:
                row["domain"], row["domain_basis"] = uniq, "observed"
        row["default"] = dict(default)
        if others:
            row["profiles"] = dict(others)
        row["source"] = src
        row["requires"] = extra.get("requires")
        row["affects"] = aff
        rows.append((cg, row))
    if unclassified:
        raise SystemExit("unclassified VVAH keys: " + ", ".join(unclassified))
    return rows, len(table) - 1


P = "vvaharness/pipeline/stages/"
VVAH_EXTRA = [
    # ---- code constants --------------------------------------------------
    K("code.s3.small_unit_loc_max", "decomposition_and_parallelism.work_units", "S3", 2000, "Units under this many lines are SMALL.", P + "s3_decompose.py:32", "code_constant", affects=["cost"]),
    K("code.s3.medium_unit_loc_max", "decomposition_and_parallelism.work_units", "S3", 8000, "Units under this many lines are MEDIUM; larger are LARGE and run alone in S4.", P + "s3_decompose.py:33", "code_constant", affects=["cost", "recall"]),
    K("code.s3.unit_rule", "decomposition_and_parallelism.work_units", "S3", "one unit per threat, ranked impact x likelihood", "How threats become investigation units. Deterministic; no catch-all unit for unnamed files.", P + "s3_decompose.py:35", "code_constant", affects=["recall"]),
    K("code.deepagents.recursion_headroom", "budget_and_termination.turn_and_call_caps", "global", 900, "Added to max_turns to form the LangGraph recursion limit; this is why max_turns is a floor on deepagents.", "vvaharness/backends/harness/deepagents/limits.py:30", "code_constant", affects=["cost"]),
    K("code.deepagents.model_timeout_seconds", "budget_and_termination.wall_clock", "global", 1800.0, "Per-model-call timeout on the deepagents route.", "vvaharness/backends/harness/deepagents/limits.py:33", "code_constant", affects=["reliability"]),
    K("code.deepagents.model_max_output_tokens", "budget_and_termination.output_tokens", "global", 64000, "Ceiling a truncated call is retried up to (one resend at double budget).", "vvaharness/backends/harness/deepagents/limits.py:36", "code_constant", affects=["reliability", "cost"]),
    K("code.deepagents.model_max_retries", "budget_and_termination.retries_and_recovery", "global", 2, "Client-level retries per model call.", "vvaharness/backends/harness/deepagents/limits.py:39", "code_constant", affects=["reliability"]),
    K("code.deepagents.transient_attempts", "budget_and_termination.retries_and_recovery", "global", 3, "Attempts on a transient error, 60 s apart.", "vvaharness/backends/llm/deepagents.py:344", "code_constant", affects=["reliability"]),
    K("code.repeat_call_limit", "budget_and_termination.stall_and_compaction", "S10/S11", 20, "Identical consecutive tool calls before the session is aborted (VVAH-E009).", "vvaharness/backends/harness/repeat_guard.py:31", "code_constant", affects=["reliability", "cost"]),
    K("code.default_llm_via", "model_routing.backend_route", "global", "cli", "Backend used when a model is given as a bare string id.", "vvaharness/backends/llm/registry.py:137", "code_constant", type="enum", domain=VIA, basis="code", affects=["reliability"]),
    K("code.s5.detector_rules", "detection_method.deterministic_detectors", "S5", "11 rules, 9 enabled", "Per-rule enable flags are packaged data, not config: form-no-csrf-post and form-get-password ship disabled.", "vvaharness/detect/patterns.py:326", "code_constant", affects=["recall", "precision"]),
    K("code.s5.test_path_gate", "scope_and_coverage.exclusions", "S5", "regex on test/mock/example paths", "Findings in test, mock or example paths are dropped before S6.", P + "s5/rules.py", "code_constant", affects=["precision", "recall"]),
    K("code.s6.verdict_routing", "gating_and_thresholds.confidence", "S6", "FP dropped; INCONCLUSIVE kept; TP below floor dropped; missing verdict = VERIFY_ERROR", "How S6 verdicts become report rows.", P + "s6/outcomes.py:262", "code_constant", affects=["precision", "recall"]),
    K("code.s6.reverify_discoveries", "verification_depth.adversarial_review", "S6", True, "Findings the verifier discovers are re-verified in a fresh second-wave session.", P + "s6_verify.py:250", "code_constant", affects=["precision"]),
    K("code.ev.live_classes", "verification_depth.exploit_testing", "S6-EV", "fixed set", "Which classify verdicts are tested live. Deliberately a code constant.", "vvaharness/exploit_verification/verify/router.py:319", "code_constant", affects=["precision"]),
    K("code.ev.oracle_time_threshold_s", "gating_and_thresholds.confidence", "S6-EV", 4.5, "Response time that counts as a time-based injection tell (payloads sleep 5 s; must also exceed baseline by 3 s).", "vvaharness/exploit_verification/verify/oracle.py:41", "code_constant", affects=["precision"]),
    K("code.s11.gate_weights", "verification_depth.fix_validation", "S11", {"root_cause": 0.43, "instance_coverage": 0.2467, "no_new_vulnerabilities": 0.1867, "security_best_practices": 0.1366}, "Weights of the four validation gates in the host-computed score.", "vvaharness/validation/claude_config/rules/scoring-matrix.md:22", "prompt_text", affects=["precision"]),
    K("code.s11.score_thresholds", "verification_depth.fix_validation", "S11", {"fixed": 0.80, "partially_fixed": 0.50, "coverage_floor": 0.50}, "Score cut-offs for Fixed / Partially Fixed / Not Fixed, and the coverage floor below which the verdict is UNVERIFIABLE.", "vvaharness/validation/claude_config/rules/scoring-matrix.md:48", "prompt_text", affects=["precision"]),
    K("code.s11.consensus_rule", "verification_depth.fix_validation", "S11", "2 of 3 personas; contradiction takes the most conservative status", "How three persona reports become one gate status. Computed by the host, not the model.", "vvaharness/validation/synthesis/_consensus.py", "code_constant", affects=["precision"]),
    K("playbook.policy.max_diff_lines", "remediation.limits", "S10", 40, "Largest patch the playbook allows.", "inputs/remediation_playbook.yaml:40", "config_file", affects=["safety"]),
    K("playbook.policy.max_files_touched", "remediation.limits", "S10", 2, "Files one fix may touch.", "inputs/remediation_playbook.yaml:41", "config_file", affects=["safety"]),
    K("playbook.policy.allow_new_dependencies", "remediation.policy", "S10", False, "Whether a fix may add a dependency.", "inputs/remediation_playbook.yaml:42", "config_file", affects=["safety"]),
    K("playbook.policy.never_autofix_cwes", "remediation.policy", "S10", [284, 285, 287, 840, 841, 327], "CWEs always routed to a human.", "inputs/remediation_playbook.yaml:51", "config_file", affects=["safety"]),
    K("policy.default_action", "remediation.policy", "S10", "allow", "What happens to a CWE that matches no policy rule.", "inputs/remediation_policy.yaml:36", "config_file", type="enum", domain=["allow", "deny"], basis="code", affects=["safety"]),
    # ---- CLI flags -------------------------------------------------------
    K("cli_flag.config", "runtime_and_infra.state_and_paths", "global", None, "Profile to load; else ./config.yaml, else the packaged default.", "vvaharness/orchestrator/entry.py:153", "cli_flag", type="str", affects=["recall", "precision", "cost"]),
    K("cli_flag.stop_after", "budget_and_termination.wall_clock", "global", None, "Stop the pipeline after a named stage.", "vvaharness/orchestrator/entry.py:174", "cli_flag", type="enum", domain=["clone", "ev", "s0", "s1", "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9", "s10", "s11"], basis="code", affects=["cost"]),
    K("cli_flag.resume", "budget_and_termination.retries_and_recovery", "global", False, "Resume from checkpoints; a re-run stage invalidates every later checkpoint.", "vvaharness/orchestrator/entry.py:172", "cli_flag", affects=["cost", "reliability"]),
    K("cli_flag.remediate", "remediation.enablement", "S10", False, "Run fix mode.", "vvaharness/orchestrator/entry.py:185", "cli_flag", affects=["safety", "cost"]),
    K("cli_flag.top", "remediation.limits", "S10", None, "Number of findings to fix (N or all).", "vvaharness/orchestrator/entry.py:191", "cli_flag", type="str", affects=["cost"]),
    K("cli_flag.skip_preflight", "runtime_and_infra.state_and_paths", "global", False, "Skip the backend probes (including the tool round-trip check).", "vvaharness/orchestrator/entry.py:201", "cli_flag", affects=["reliability"]),
    K("cli_flag.step1_config", "scope_and_coverage.exclusions", "S1", None, "Extra exclusion overlay file; lists append.", "vvaharness/orchestrator/entry.py:204", "cli_flag", type="str", affects=["recall", "cost"]),
    K("cli_flag.group_by_app", "decomposition_and_parallelism.work_units", "global", False, "Batch mode: one scan per application directory instead of per repo.", "vvaharness/orchestrator/entry.py:167", "cli_flag", affects=["recall", "cost"]),
    # ---- env vars --------------------------------------------------------
    K("env.EV_API_COLLECTION", "verification_depth.exploit_testing", "S6-EV", None, "Postman/OpenAPI collection; setting it arms exploit verification.", ".env.exploit.example", "env_var", type="str", affects=["precision", "safety"]),
    K("env.EV_TARGET_URL", "verification_depth.exploit_testing", "S6-EV", None, "Running target for live verification; localhost only.", ".env.exploit.example", "env_var", type="str", affects=["safety"]),
    K("env.EV_AUTH_STRATEGY", "runtime_and_infra.target_auth", "S6-EV", None, "How the verifier authenticates to the target.", ".env.exploit.example", "env_var", type="enum", domain=["bearer", "basic", "api_key_header", "session_cookie", "oauth2_client_credentials", "none"], basis="code", affects=["recall"]),
    K("env.VVAHARNESS_REMEDIATE_DISABLE", "remediation.enablement", "S10", None, "Kill switch for the fix stage.", "inputs/remediation_policy.yaml", "env_var", type="str", affects=["safety"]),
    K("env.VVAHARNESS_NO_LOCAL_CONFIG", "runtime_and_infra.state_and_paths", "global", None, "Ignore the config.local.yaml overlay next to the config.", "vvaharness/config/__init__.py:868", "env_var", type="str", affects=[]),
    K("env.VVAHARNESS_STATE_DIR", "runtime_and_infra.state_and_paths", "global", None, "Where checkpoints and run state live (must be outside the scanned repo).", "vvaharness/orchestrator/scan.py:411", "env_var", type="str", affects=[]),
    # ---- prompt text -----------------------------------------------------
    K("prompt.s2.method", "detection_method.search_strategy", "S2", "STRIDE threat model from a structural snapshot", "S2 models threats from deterministic evidence (docs, manifests, inventory, entry points) plus tools; it does not read all source.", P + "s2/prompts.py:35", affects=["recall"]),
    K("prompt.s2.hollow_retry", "budget_and_termination.retries_and_recovery", "S2", "one tool-less re-ask, then hard fail", "What happens when the threat model has zero threats or no valid surface files.", P + "s2/session.py:86", affects=["reliability"]),
    K("prompt.s4.role", "detection_method.search_strategy", "S4", "confirm or refute ONE specific threat claim", "S4 is hypothesis-driven: it tests a threat, it does not trace every input.", P + "s4/prompts.py:348", affects=["recall", "precision"]),
    K("prompt.s4.verdicts", "gating_and_thresholds.verdict_scheme", "S4", ["confirmed", "refuted", "inconclusive"], "Verdicts S4 may return per unit; an omitted unit is recorded as uninvestigated.", P + "s4/prompts.py:92", type="list", affects=["precision", "recall"]),
    K("prompt.s4.sweep_variant", "detection_method.search_strategy", "S4", "breadth sweep, or budgeted sweep when max_model_calls > 0", "The sweep text changes with the call budget and with whether source is inlined and a graph exists.", P + "s4/prompts.py:304", affects=["recall", "cost"], requires="step4.max_model_calls, step4.inline_source, graph present"),
    K("prompt.s4.breadth_and_siblings", "detection_method.mandatory_checks", "S4", True, "Look for other weakness classes at the same site and sibling instances elsewhere (breadth clause, CWE pairs).", P + "s4/prompts.py:31", affects=["recall"]),
    K("prompt.s4.absence_method", "detection_method.mandatory_checks", "S4", True, "Method for proving a control is missing rather than assuming it.", P + "s4/prompts.py:136", affects=["precision"]),
    K("prompt.s4.fp_discipline", "gating_and_thresholds.hard_gates", "S4", True, "False-positive discipline clause in the deep-dive system prompt.", P + "s4/prompts.py:115", affects=["precision"]),
    K("prompt.s4.read_completely", "detection_method.mandatory_checks", "S4", True, "Read each named file to the end before a verdict.", P + "s4/prompts.py:122", affects=["recall", "cost"]),
    K("prompt.s6.stance", "verification_depth.adversarial_review", "S6", "assume each finding is wrong", "The verifier's starting position.", P + "s6/prompts.py:23", affects=["precision"]),
    K("prompt.s6.exclusion_rules", "gating_and_thresholds.hard_gates", "S6", "rules A-F", "Out-of-scope rules that turn a finding into FALSE_POSITIVE.", P + "s6/prompts.py:29", affects=["precision", "recall"]),
    K("prompt.s6.verdicts", "gating_and_thresholds.verdict_scheme", "S6", ["TRUE_POSITIVE", "FALSE_POSITIVE", "INCONCLUSIVE"], "Verdicts S6 may return; INCONCLUSIVE is kept as undetermined.", P + "s6/prompts.py:84", type="list", affects=["precision", "recall"]),
    K("prompt.s6.correction_duty", "verification_depth.adversarial_review", "S6", True, "Correct a wrong CWE or line instead of rejecting the finding.", P + "s6/prompts.py:135", affects=["recall"]),
    K("prompt.s6.cvss_duty", "gating_and_thresholds.severity_rules", "S6", "CVSS 3.1 vector", "Severity is re-scored by the verifier from a CVSS vector; S4 severity is not trusted.", P + "s6/prompts.py:192", affects=["reporting"]),
    K("prompt.s7.collapse_test", "dedup_and_merge.merge_rules", "S7", "one fix closes both", "Semantic dedup test; never collapse across CWEs except sibling sets.", P + "s7/prompts.py:23", affects=["precision", "recall"], requires="step7_dedup.semantic"),
    K("prompt.s8.evidence_rule", "ranking_and_reporting.chains", "S8", "each chain link needs file:line evidence", "Chains without evidenced links are dropped or annotated by code.", P + "s8/prompts.py:26", affects=["reporting"]),
    K("prompt.skills.set", "context_supply.injected_knowledge", "S2/S4", 17, "Skill playbooks copied into <repo>/.vvaharness/skills/, one per weakness family, each with a HARD GATE and FP checks. 8 ship a probe.sh grep script.", "vvaharness/skills/", type="int", affects=["recall", "precision"], requires="via == deepagents"),
    K("prompt.cwe_kb", "context_supply.injected_knowledge", "S4", "27 CWE entries", "Sanitizers, non-sanitizers and FP checks returned by the CweGuidance tool.", "vvaharness/rules/generic.kb.yaml", affects=["precision"]),
    K("prompt.reason_in_prompt", "model_routing.reasoning", "global", "name each candidate, the control that would refute it, discard what does not hold", "Text appended to system prompts when think_in_prompt is on.", "vvaharness/backends/harness/deepagents/options/model_building.py:364", affects=["precision", "cost"], requires="think_in_prompt"),
    K("prompt.investigation_floor", "detection_method.mandatory_checks", "global", "openai provider only", "Suffix that forbids describing unopened code and asks for enumeration rather than summaries. Applied only to OpenAI-provider models.", "vvaharness/backends/harness/deepagents/profiles.py:70", affects=["precision", "recall"], requires="provider == openai"),
    K("prompt.evidence_gate_nudge", "gating_and_thresholds.evidence_gates", "S4", "HOLD ... verdict is rejected", "Message sent when a verdict arrives with unfinished todos.", "vvaharness/backends/harness/deepagents/evidence_gate.py:66", affects=["precision"], requires="step4.evidence_gate"),
    K("prompt.replay_instructions", "budget_and_termination.retries_and_recovery", "S2/S4/S6/S8", "report from the transcript alone; unreached items are inconclusive", "What a session is told after it hits its deadline.", P + "replay.py:66", affects=["recall", "reliability"]),
    K("prompt.output_schema_text", "gating_and_thresholds.verdict_scheme", "S4/S6", "Pydantic Field descriptions", "Much instruction is carried in the structured-output schema (e.g. 'Do NOT use confirmed as a default').", P + "s4/outcomes.py:34", affects=["precision", "recall"]),
    K("prompt.s11.personas", "verification_depth.fix_validation", "S11", ["security-architect", "penetration-tester", "cross-repo-analyzer"], "The three isolated validation personas.", "vvaharness/validation/subagents/", type="list", affects=["precision"], requires="step_validate.enabled"),
    K("prompt.s10.playbook_rule", "remediation.policy", "S10", "select a playbook strategy, do not invent one", "The fixer must follow the playbook strategy for the CWE.", "vvaharness/remediation_agent/prompts.py:44", affects=["safety"]),
]

VVAH_PIPELINE = """\
# θ.<id> refers to a knob id in `categories` below.
# DET = deterministic code, LLM_ONESHOT = one model call, LLM_AGENT = tool-using session.
scan(repo, θ):                                           # orchestrator/scan.py
  preflight(θ.models.*)                                  # probe each (model, via, provider)
  if θ.step1.auto_exclude:
    overlay = LLM_ONESHOT(models.autoexclude, survey(repo))
    overlay = DET veto(overlay, θ.step1.auto_exclude_protect_*)
  seed    = DET S0(repo, θ.step0.*, θ.step1.exclude_*)    # entry points and sinks by pattern
  graph   = DET codegraph(repo)                          # tree-sitter + communities
  ctx     = DET S1(seed, graph, θ.inject.*)
  tm      = LLM_AGENT S2(ctx,
              evidence capped by θ.step2.max_*,
              tools = θ.step2.allowed_tools + graph tools (θ.step2.graph_tool_budget),
              bounds = θ.step2.{max_turns, max_model_calls, deadline},
              gate   = θ.step2.require_graph,
              plan   = θ.step2.planning)
  threats = tm.threats[: θ.step2.max_threats], dropping any whose surface_files do not resolve
  units   = DET S3(threats)                              # one unit per threat, ranked
  batches = group(units, θ.step4.batch_size)             # by file overlap
  cands   = PARALLEL(θ.step4.parallel) for b in batches:
              LLM_AGENT S4(b,
                tools = Read/Glob/Grep + CweGuidance + graph tools,
                skills = θ.step4.skills, plan = θ.step4.planning,
                gate  = θ.step4.evidence_gate,
                bounds = θ.step4.{max_turns, max_model_calls, deadline})
              -> per unit: confirmed | refuted | inconclusive, with findings
  cands   = DET S5(cands)                                # path gate, re-anchor, same-site collapse
  cands  += DET detectors() if θ.step5_detectors.enabled
  if exploit verification armed:
    EV(cands)                                            # classify -> map -> payloads -> attacker -> oracle -> judge
  verdicts = PARALLEL(θ.step6_verify.parallel) for b in batches(cands, θ.step6_verify.batch_size):
               LLM_AGENT S6(b) -> TRUE_POSITIVE | FALSE_POSITIVE | INCONCLUSIVE, confidence 0-10, CVSS
  kept    = [f for f in verdicts if TRUE_POSITIVE and confidence >= θ.step6_verify.min_confidence]
            + INCONCLUSIVE kept as undetermined
  kept    = DET S7(kept, θ.step7_dedup.line_tolerance)
  if θ.step7_dedup.semantic: kept = LLM_ONESHOT S7(kept)
  report  = LLM_ONESHOT S8(kept), then DET validate; on failure a severity-sorted report
  DET S9(report) -> findings.json, Markdown, SARIF
  if θ.step_remediate.enabled or --remediate:
    for f in top θ.step_remediate.top_n_findings by CVSS: LLM_AGENT S10(f) between policy gates
  if θ.step_validate.enabled:
    for case in fixes: orchestrator + 3 personas -> DET consensus and score
"""

# ==========================================================================
# VulnHunter
# ==========================================================================
SK = "vulnhunt/SKILL.md"
PH = "vulnhunt/phases/"
AG = "vulnhunter-agent/agent/"
HA = "harness/local_harness/"
FX = "vulnhunter-fix/"

VH = [
    # ---------------- model_routing --------------------------------------
    K("anthropic.model", "model_routing.model_choice", "all", "(required; example claude-opus-4-8)", "The one model that runs the whole scan: orchestrator and every subagent. CLI --model overrides.", AG + "config.py:448", "config_file", type="str", affects=["recall", "precision", "cost"]),
    K("skill.min_model", "model_routing.model_choice", "step0", "Opus 4.7", "Interactive runs stop unless the model is Opus 4.7 or newer; skipped when the agent drives the scan.", SK + ":18", affects=["recall", "precision"]),
    K("issues.haiku_model", "model_routing.model_choice", "issues", "claude-haiku-4-5", "First model tried for report-to-JSON extraction and issue dedup.", AG + "config.py:226", "config_file", affects=["cost", "reporting"]),
    K("issues.sonnet_model", "model_routing.model_choice", "issues", "claude-sonnet-5", "Fallback model for extraction and dedup.", AG + "config.py:227", "config_file", affects=["cost", "reporting"]),
    K("code.issues.fallback_chain", "model_routing.fallback_chain", "issues", ["haiku", "sonnet", "scan model"], "Order of models tried for extraction; dedup stops at sonnet.", AG + "issues_extract.py:209", "code_constant", type="list", affects=["reliability"]),
    K("harness.MODEL", "model_routing.model_choice", "benchmark", "claude-opus-4-8", "Model for the harness scan, judge and miss diagnosis.", HA + "config.py:21", "code_constant", affects=["recall", "precision", "cost"]),
    K("fix.models.default", "model_routing.model_choice", "fix", "sonnet", "Default fixer model in config.json.", FX + "config.json", "config_file", affects=["cost"]),
    K("fix.models.routing", "model_routing.model_choice", "fix", "opus / sonnet / haiku by severity and CWE", "Model routing table. No prompt or script reads it; the skill insists on Opus. Treat as inert.", FX + "config.json", "config_file", type="map", affects=[]),
    K("fix.subagent_models", "model_routing.model_choice", "fix", {"severity_annotation": "haiku", "readme_extraction": "sonnet"}, "Cheaper models named in the fix prompts for mechanical sub-steps.", FX + "prompts/parse_issues.md", affects=["cost"]),
    K("anthropic.auth_mode", "model_routing.backend_route", "all", "api_key", "How the agent reaches the model: direct API key, Bedrock with OAuth, or Bedrock with SigV4.", AG + "config.py:57", "config_file", type="enum", domain=["api_key", "bedrock_oauth", "bedrock_sigv4"], basis="code", affects=["reliability"]),
    K("sdk.effort_or_thinking", "model_routing.reasoning", "all", None, "No reasoning tier, thinking budget or temperature is set for the scan session.", AG + "runner.py:680", "not_set", type="str", affects=["recall", "precision", "cost"]),
    K("sdk.system_prompt", "model_routing.reasoning", "all", None, "No system prompt is set; all method text comes from the installed skill files.", AG + "runner.py:680", "not_set", type="str", affects=["recall", "precision"]),
    K("fix.reviewer_sampling", "model_routing.reasoning", "fix", {"temperature": 0, "max_tokens": 800}, "Sampling stated in the test-reviewer and tier-judgment prompts.", FX + "prompts/reviewer_test.md", affects=["precision"]),
    # ---------------- budget_and_termination -----------------------------
    K("sdk.max_turns", "budget_and_termination.turn_and_call_caps", "all", None, "No turn limit on the scan session.", AG + "runner.py:680", "not_set", type="int", affects=["cost", "recall"]),
    K("sdk.max_budget_usd", "budget_and_termination.cost_caps", "all", None, "No cost cap. Cost is recorded in the manifest but never enforced.", AG + "runner.py:680", "not_set", type="float", affects=["cost"]),
    K("sdk.wall_clock", "budget_and_termination.wall_clock", "all", None, "No overall wall clock in the agent; only the harness has one.", AG + "runner.py:680", "not_set", type="int", affects=["cost", "latency"]),
    K("scan.async_agent_stall_timeout_ms", "budget_and_termination.stall_and_compaction", "all", 1200000, "A subagent with no activity for this long is treated as stalled (20 minutes).", AG + "config.py:595", "config_file", affects=["reliability", "latency"]),
    K("scan.autocompact_pct_override", "budget_and_termination.stall_and_compaction", "all", None, "Context-fill percentage that triggers compaction. Unset: 85, or 90 on 1M-context models.", AG + "build_settings.py:35", "config_file", type="int", domain=[50, 95], basis="suggested", affects=["recall", "cost"]),
    K("code.max_stalled_continuations", "budget_and_termination.stall_and_compaction", "all", 60, "Consecutive 'continue' re-prompts with no subagent activity before the run aborts.", AG + "runner.py:459", "code_constant", affects=["reliability", "cost"]),
    K("code.continuation_prompt", "budget_and_termination.retries_and_recovery", "all", "Continue the /vulnhunt workflow ... do not stop until the report is written", "Re-sent whenever the orchestrator stops while subagents are still pending.", AG + "runner.py:460", "code_constant", affects=["reliability", "recall"]),
    K("code.max_consecutive_rate_limits", "budget_and_termination.retries_and_recovery", "all", 3, "Rate-limit messages before the first reply that count as a cold-start failure.", AG + "runner.py:441", "code_constant", affects=["reliability"]),
    K("code.scan_retry_backoffs", "budget_and_termination.retries_and_recovery", "all", [60.0, 120.0, 300.0], "Waits between cold-start retries (4 attempts in total).", AG + "runner.py:446", "code_constant", affects=["reliability", "latency"]),
    K("code.max_consecutive_auth_failures", "budget_and_termination.retries_and_recovery", "all", 3, "Consecutive auth failures before abort.", AG + "runner.py:434", "code_constant", affects=["reliability"]),
    K("code.llm_transient_backoffs", "budget_and_termination.retries_and_recovery", "issues", [60.0], "One same-model retry for the small JSON calls, then the fallback model.", AG + "_llm.py:107", "code_constant", affects=["reliability"]),
    K("scan.clone_timeout_seconds", "budget_and_termination.wall_clock", "clone", 300, "Clone timeout.", AG + "config.py:102", "config_file", affects=["reliability"]),
    K("issues.request_timeout_seconds", "budget_and_termination.wall_clock", "issues", 60, "Timeout for GitHub and small LLM requests in the issues stage.", AG + "config.py:229", "config_file", affects=["reliability"]),
    K("harness.SCAN_TIMEOUT", "budget_and_termination.wall_clock", "benchmark", 21600, "Kill timer per scan in the harness (6 hours). The only hard run limit anywhere.", HA + "config.py:18", "code_constant", affects=["cost", "recall"]),
    K("harness.JUDGE_TIMEOUT", "budget_and_termination.wall_clock", "benchmark", 600, "Timeout for the batched judge call.", HA + "config.py:19", "code_constant", affects=["reliability"]),
    K("harness.SCAN_MAX_RETRIES", "budget_and_termination.retries_and_recovery", "benchmark", 3, "Scan retries on 429, backing off 60 s x2 up to 300 s.", HA + "config.py:24", "code_constant", affects=["reliability"]),
    K("harness.JUDGE_MAX_RETRIES", "budget_and_termination.retries_and_recovery", "benchmark", 3, "Judge retries, backing off 30 s x2 up to 180 s.", HA + "config.py:29", "code_constant", affects=["reliability"]),
    K("prompt.subagent_return_words", "budget_and_termination.output_tokens", "all phases", 20, "Maximum words a subagent may return to the orchestrator; results go to files instead.", SK + ":338", type="int", domain=[10, 200], affects=["cost", "reliability"]),
    K("prompt.recon.callgraph_call_budget", "budget_and_termination.turn_and_call_caps", "phase1", "2-4 Grep/Read calls per entry point", "Tool-call budget for building the call graph in recon.", PH + "phase1_recon.md:249", affects=["cost", "recall"]),
    K("prompt.gate_cost", "budget_and_termination.turn_and_call_caps", "phase2", "1-2 tool calls per gate", "Stated cost of each hard gate; a failed gate stops work on the candidate.", PH + "phase2_shared.md:113", affects=["cost"]),
    K("prompt.redispatch_on_failure", "budget_and_termination.retries_and_recovery", "phase2", "re-launch, do not diagnose", "A subagent that fails or leaves no results file is re-dispatched; a failed agent is unknown coverage, not 'no findings'.", PH + "phase2_hunt.md:77", affects=["recall", "reliability"]),
    # ---------------- decomposition_and_parallelism ----------------------
    K("prompt.phase_topology", "decomposition_and_parallelism.work_units", "all phases", ["recon", "hunt (many agents)", "verify", "reproduce+test+fix", "sweep", "report (orchestrator)"], "One subagent per phase; the orchestrator only dispatches and checks that output files exist.", SK + ":228", type="list", affects=["recall", "cost"]),
    K("prompt.hunt.class_groups", "decomposition_and_parallelism.work_units", "phase2", ["INJ", "NAV", "LOG"], "Vulnerability class groups; each partition gets one trace agent per group.", PH + "phase2_hunt.md:46", type="list", domain=[["INJ", "NAV", "LOG"], ["INJ", "NAV"], ["INJ"]], affects=["recall", "cost"]),
    K("prompt.hunt.sink_driven_agents", "decomposition_and_parallelism.work_units", "phase2", 1, "Extra agent that works backward from dangerous sinks (6 audits), run as its own final wave.", PH + "phase2_hunt.md:25", type="int", domain=[0, 1], affects=["recall", "cost"]),
    K("prompt.hunt.min_agent_count", "decomposition_and_parallelism.work_units", "phase2", "(3 x production partitions) + 1", "Minimum agents the orchestrator must spawn; fewer is a procedure violation.", PH + "phase2_hunt.md:30", affects=["recall", "cost"]),
    K("prompt.hunt.wave_size", "decomposition_and_parallelism.concurrency", "phase2", 6, "Agents dispatched per wave. The prompt says 12 concurrent agents caused 429 failures.", PH + "phase2_hunt.md:54", type="int", domain=[1, 12], affects=["latency", "reliability"]),
    K("prompt.recon.partition_rule", "decomposition_and_parallelism.work_units", "phase1", "union-find on shared application functions", "Two entry points share a partition if they call a common app-specific function.", PH + "phase1_recon.md:289", affects=["recall", "cost"]),
    K("prompt.recon.callgraph_depth", "decomposition_and_parallelism.work_units", "phase1", 2, "Call levels followed from each handler when building the partition map.", PH + "phase1_recon.md:229", type="int", domain=[1, 4], affects=["recall", "cost"]),
    K("prompt.recon.shared_infra_import_share", "decomposition_and_parallelism.work_units", "phase1", 0.5, "A module imported by more than this share of entry points is shared infrastructure and does not join partitions.", PH + "phase1_recon.md:259", type="float", domain=[0.2, 0.8], affects=["recall", "cost"]),
    K("prompt.recon.oversize_inputs", "decomposition_and_parallelism.work_units", "phase1", 20, "A partition with more inputs is sub-partitioned; if it cannot be split it becomes SEQUENTIAL-FALLBACK.", PH + "phase1_recon.md:312", type="int", domain=[10, 40], affects=["recall", "cost"]),
    K("prompt.recon.oversize_files", "decomposition_and_parallelism.work_units", "phase1", 15, "A partition with more app-specific files is sub-partitioned.", PH + "phase1_recon.md:312", type="int", domain=[8, 30], affects=["recall", "cost"]),
    K("prompt.recon.undersize_rule", "decomposition_and_parallelism.work_units", "phase1", "<= 2 inputs and 1 file", "Partitions this small are merged into the closest one.", PH + "phase1_recon.md:321", affects=["cost"]),
    K("prompt.hunt.sequential_fallback", "decomposition_and_parallelism.work_units", "phase2", "orchestrator processes entry point x class group, checkpointing to files", "How a partition too large to parallelise is handled.", PH + "phase2_hunt.md:246", affects=["recall", "cost"]),
    K("harness.MAX_SCAN_WORKERS", "decomposition_and_parallelism.concurrency", "benchmark", 5, "Repos scanned at once by the harness. CLI --max-workers overrides.", HA + "config.py:17", "code_constant", affects=["latency"]),
    # ---------------- scope_and_coverage ---------------------------------
    K("prompt.scope.exclusions", "scope_and_coverage.exclusions", "all phases", ["test code", "build/config scripts", "vendored/third-party", "generated code", "documentation"], "Paths never audited or traced through.", SK + ":84", type="list", affects=["precision", "recall", "cost"]),
    K("prompt.scope.infra_config_exception", "scope_and_coverage.exclusions", "all phases", True, "Security-relevant infrastructure config (nginx, proxy, TLS, CORS) is audited despite the build/config exclusion.", SK + ":91", affects=["recall"]),
    K("prompt.scope.dev_only_skip", "scope_and_coverage.exclusions", "phase1", True, "Partitions gated to non-production environments are not dispatched; inputs are marked SAFE.", PH + "phase1_recon.md:324", affects=["precision", "recall", "cost"]),
    K("prompt.scope.input_inventory", "scope_and_coverage.coverage_ceilings", "phase1", "every user-controllable input", "The inventory is the unit of coverage: every row must end with a disposition.", PH + "phase1_recon.md:51", affects=["recall"]),
    K("prompt.scope.sink_prepass", "scope_and_coverage.seed_detection", "phase1", True, "Enumerate dangerous sinks per app before the input inventory; an app with zero sinks gets a second look.", PH + "phase1_recon.md:24", affects=["recall"]),
    K("prompt.scope.indirect_dispatch", "scope_and_coverage.seed_detection", "phase1", True, "Detect routers, registries and reflection that hide entry points.", PH + "phase1_recon.md:172", affects=["recall"]),
    K("prompt.scope.build_time_swapping", "scope_and_coverage.seed_detection", "phase1", True, "Detect builds that swap production and mock sources, and audit the production variant.", PH + "phase1_recon.md:467", affects=["precision"]),
    K("prompt.scope.partition_coverage_check", "scope_and_coverage.coverage_ceilings", "phase1", True, "Every production app must appear in at least one partition.", PH + "phase1_recon.md:338", affects=["recall"]),
    K("prompt.scope.phase3_severity_floor", "scope_and_coverage.coverage_ceilings", "phase3", ["High", "Medium"], "Severities that get a PoC and exploit test.", PH + "phase3_reproduce_test.md:22", type="list", affects=["cost", "recall"]),
    K("prompt.scope.dependency_cves", "scope_and_coverage.exclusions", "phase4", "report only if provable from the first-party call site", "Dependency internals are not analysed.", PH + "phase4_report.md:178", affects=["precision", "cost"]),
    K("code.prior_results_guard", "scope_and_coverage.exclusions", "pre-stage", True, "The scan refuses to start if an old results directory exists, so the model cannot read prior output.", AG + "runner.py:411", "code_constant", affects=["precision"]),
    K("code.clone_depth", "scope_and_coverage.exclusions", "clone", 1, "Shallow clone depth; no history is available to the scan.", AG + "clone.py:119", "code_constant", affects=["cost"]),
    # ---------------- context_supply --------------------------------------
    K("prompt.orchestrator_context_rule", "context_supply.orchestrator_context", "all phases", "do not read results, recon analysis or source", "The orchestrator reads only the partition and inventory tables; everything else stays in files.", SK + ":334", affects=["reliability", "cost"]),
    K("prompt.trace_agent_reading_list", "context_supply.source_delivery", "phase2", ["phase2_shared.md", "phase2_class_<class>.md", "partitions/sg-N_data.md"], "Files each trace agent reads, in order. The orchestrator does not interpolate their content.", PH + "phase2_hunt.md:97", type="list", affects=["recall", "precision"]),
    K("prompt.partition_data_file", "context_supply.source_delivery", "phase2", ["inputs", "file scope", "shared infrastructure catalog", "threat model"], "What the orchestrator extracts into each partition file.", SK + ":241", type="list", affects=["recall", "precision"]),
    K("prompt.threat_model_fields", "context_supply.injected_knowledge", "phase1", ["app-layer auth enforcement", "caller identity binding", "per-resource authorization"], "Each needs a file:line in audited code or NONE; this becomes the Gate 3 baseline.", PH + "phase1_recon.md:380", type="list", affects=["precision", "recall"]),
    K("prompt.inadmissible_evidence", "context_supply.injected_knowledge", "phase1", ["route naming", "comments", "skip-auth config", "optional client-cert", "deployment inference", "gateway claims", "shape validators"], "Evidence that may not justify an auth field.", PH + "phase1_recon.md:433", type="list", affects=["recall"]),
    K("prompt.recon_stance", "context_supply.injected_knowledge", "phase1", "intentionally pessimistic", "Recon records what the code does at face value; downgrades wait for Phase 2b.", PH + "phase1_recon.md:387", affects=["recall", "precision"]),
    K("code.kickoff_metadata", "context_supply.source_delivery", "pre-stage", ["results dir", "branch and sha", "repo URL", "model tag", "Bash availability"], "Values computed in Python and passed in the kickoff prompt, so the model never shells out for them.", AG + "runner.py:132", "code_constant", type="list", affects=["reliability"]),
    K("code.setting_sources", "context_supply.injected_knowledge", "all", ["user"], "Skills and settings load from the user's install only; the scanned repo's .claude/ is never loaded.", AG + "runner.py:680", "code_constant", type="list", affects=["safety"]),
    K("prompt.class_files", "context_supply.injected_knowledge", "phase2", ["phase2_class_inj.md", "phase2_class_nav.md", "phase2_class_log.md"], "Per-class sink references, vulnerability classes and class-specific gate rules.", PH, type="list", affects=["recall", "precision"]),
    # ---------------- tool_access ----------------------------------------
    K("scan.allowed_tools", "tool_access.tool_allowlist", "all", ["Agent", "Glob", "Read", "Write"], "Tools visible to and auto-approved for the scan session. Grep is not in the default list although the skill text relies on it; the example config says to add it if tracing comes back thin.", AG + "config.py:572", "config_file", affects=["recall", "cost"]),
    K("cli.read_only", "tool_access.shell", "all", True, "--read-only (default) vs --no-read-only. Read-only scans write exploit tests but do not run them.", AG + "__main__.py:221", "cli_flag", affects=["precision", "safety"]),
    K("cli.enable_bash", "tool_access.shell", "all", False, "Adds Bash. Must be paired with --no-read-only; Bash in the config list is silently stripped.", AG + "__main__.py:238", "cli_flag", requires="cli.read_only == false", affects=["precision", "safety", "cost"]),
    K("prompt.dependency_install", "tool_access.shell", "step2", "npm / pip / go mod / mvn / sbt", "In Bash mode the skill installs dependencies before Phase 1 so exploit tests can run.", SK + ":52", requires="Bash available", affects=["precision", "safety"]),
    K("scan.permission_mode", "tool_access.sandbox_and_permissions", "all", "acceptEdits", "Permission mode for the scan and verify sessions.", AG + "config.py:576", "config_file", affects=["safety", "reliability"]),
    K("sandbox.enabled", "tool_access.sandbox_and_permissions", "all", True, "OS sandbox: reads limited to the clone, network limited to the inference host.", AG + "config.py:84", "config_file", affects=["safety"]),
    K("sandbox.fail_if_unavailable", "tool_access.sandbox_and_permissions", "all", True, "Refuse to run when the sandbox cannot start.", AG + "config.py:85", "config_file", affects=["safety"]),
    K("sandbox.allow_unsandboxed_commands", "tool_access.sandbox_and_permissions", "all", False, "Allow commands outside the sandbox.", AG + "config.py:86", "config_file", affects=["safety"]),
    K("harness.scan_tools", "tool_access.tool_allowlist", "benchmark", ["Read", "Write", "Edit", "Grep", "Glob", "Agent"], "Tools for harness scans (includes Grep, unlike the agent default). --execute adds Bash.", HA + "scan.py:424", "code_constant", type="list", affects=["recall"]),
    K("code.verify_tools", "tool_access.tool_allowlist", "verify", ["Read", "Write", "Edit", "Glob", "Grep", "Agent"], "Fixed tool set for the fix-verify session; not configurable.", AG + "verify_runner.py:73", "code_constant", type="list", affects=["safety"]),
    # ---------------- detection_method -----------------------------------
    K("prompt.persona", "detection_method.search_strategy", "all phases", "VulnHunter, a security auditor", "Role line for the orchestrator.", SK + ":68", affects=[]),
    K("prompt.tracing_direction", "detection_method.search_strategy", "phase2", "input-forward", "Every inventoried input is traced forward to a sink; switching to entry-point- or sink-driven hunting is forbidden for trace agents.", PH + "phase2_shared.md:107", type="enum", domain=["input-forward", "sink-backward", "both"], affects=["recall", "cost"]),
    K("prompt.sink_audits", "detection_method.search_strategy", "phase2", ["action-scope", "credential-issuing", "cryptographic", "sensitive storage", "concurrency", "rate-limit"], "The six backward audits run by the sink-driven agent.", PH + "phase2_hunt.md:146", type="list", affects=["recall"]),
    K("prompt.investigation_discipline", "detection_method.mandatory_checks", "phase2", ["1 read entry point", "2 trace forward", "2b audit all outbound params", "3 exhaust all paths", "4 follow stores", "4b response taint", "4c response-to-caller", "5 read sink", "6 transitive callers"], "Ordered tracing steps every input goes through.", SK + ":119", type="list", affects=["recall", "cost"]),
    K("prompt.absent_input_analysis", "detection_method.mandatory_checks", "phase2", True, "After tracing, ask what happens when each security-gating input is omitted (Conditional Validation Bypass).", PH + "phase2_shared.md:62", affects=["recall"]),
    K("prompt.request_body_gate", "detection_method.mandatory_checks", "phase2 NAV", True, "Mandatory mass-assignment check (CWE-915) for every request body.", PH + "phase2_class_nav.md:5", affects=["recall"]),
    K("prompt.resource_id_gate", "detection_method.mandatory_checks", "phase2 NAV", True, "Mandatory ownership check (CWE-639) for every ID input.", PH + "phase2_class_nav.md:40", affects=["recall"]),
    K("prompt.auth_branch_enumeration", "detection_method.mandatory_checks", "phase2", True, "Each authentication branch of a multi-auth endpoint is traced as its own path.", PH + "phase2_shared.md:93", affects=["recall"]),
    K("prompt.continue_past_first_finding", "detection_method.mandatory_checks", "phase2", True, "Keep tracing an input after its first sink; each further sink is a separate candidate.", PH + "phase2_shared.md:38", affects=["recall"]),
    K("prompt.auth_helper_coverage_audit", "detection_method.mandatory_checks", "phase2 NAV", True, "Post-trace audit that every handler calls the authorization helper.", PH + "phase2_class_nav.md:212", affects=["recall"]),
    K("prompt.enforcement_style", "detection_method.search_strategy", "all phases", "MANDATORY / STOP / count checks", "Rules are enforced by prose and row-count checks, not by code.", SK + ":289", affects=["recall", "reliability"]),
    # ---------------- gating_and_thresholds -------------------------------
    K("prompt.hard_gates", "gating_and_thresholds.hard_gates", "phase2", ["0 design intent", "1 reachable", "2a attacker-controlled", "2b sanitization", "3 new capability"], "Gates every candidate passes in order; the first failure eliminates it.", PH + "phase2_shared.md:111", type="list", affects=["precision", "recall"]),
    K("prompt.gate2b_empirical", "gating_and_thresholds.hard_gates", "phase2", True, "A sanitizer must be verified by reading or testing it, never assumed from the library name; it must match the sink context.", PH + "phase2_class_inj.md:116", affects=["recall", "precision"]),
    K("prompt.gate_exemptions", "gating_and_thresholds.exemptions", "phase2", ["CVB immune to Gate 0", "CWE-306/639 immune to Gate 3", "weak crypto exempt from Gate 2a", "class-specific Do-NOT-eliminate lists"], "Finding types a gate may not eliminate.", PH + "phase2_shared.md:83", type="list", affects=["recall", "precision"]),
    K("prompt.gate_principle", "gating_and_thresholds.hard_gates", "all phases", "report what the gates confirm", "A finding that passes the gates is reported; 'low impact' reasoning may not override them.", SK + ":74", affects=["recall", "precision"]),
    K("prompt.severity_tiers", "gating_and_thresholds.severity_rules", "phase2", ["High+", "High", "Medium", "Low", "Informational"], "Severity scale, defined by attacker position and impact (no CVSS).", PH + "phase2_shared.md:307", type="list", affects=["reporting"]),
    K("prompt.severity_floors", "gating_and_thresholds.severity_rules", "phase2", "class-specific minimums (INJ, NAV)", "Severities a class may not be rated below.", PH + "phase2_class_nav.md:84", affects=["reporting", "recall"]),
    K("prompt.severity_context_check", "gating_and_thresholds.severity_rules", "phase2", True, "Classify under the most dangerous context the sink accepts.", PH + "phase2_shared.md:47", affects=["reporting"]),
    K("prompt.stopping_rules", "gating_and_thresholds.hard_gates", "all phases", "zero findings is valid; do not soften criteria", "The run may end with no findings; weak candidates become code smells.", SK + ":308", affects=["precision"]),
    K("prompt.dispositions", "gating_and_thresholds.verdict_scheme", "phase2", ["CANDIDATE", "SAFE", "NO-MATCH", "CROSS-CLASS", "DESIGN-INTENT"], "Outcome a trace agent records per input.", PH + "phase2_hunt.md:102", type="list", affects=["recall", "precision"]),
    # ---------------- verification_depth ----------------------------------
    K("prompt.phase2b.enabled", "verification_depth.adversarial_review", "phase2b", True, "Mandatory disprove pass by a separate subagent over every candidate.", PH + "phase2b_verify.md:12", affects=["precision", "cost"]),
    K("prompt.phase2b.fp_prior", "verification_depth.adversarial_review", "phase2b", "~50% of candidates are false positives", "Prior stated to the verifier.", PH + "phase2b_verify.md:18", type="str", affects=["precision", "recall"]),
    K("prompt.phase2b.candidate_manifest", "verification_depth.adversarial_review", "phase2b", True, "Count candidates first; the verdict table must have exactly that many rows.", PH + "phase2b_verify.md:22", affects=["recall"]),
    K("prompt.phase2b.consensus_skip", "verification_depth.adversarial_review", "phase2b", True, "Skip re-reading source when all agents cite the same Gate 1 evidence at the same file:line.", PH + "phase2b_verify.md:31", affects=["cost", "precision"]),
    K("prompt.phase2b.checks", "verification_depth.adversarial_review", "phase2b", ["1 gates answered", "2 reachability", "3 defenses", "4 severity", "5 downgrade discipline", "6 CVB", "7 comment skepticism", "8 authorization delegation", "9 universal auth gap"], "The nine checks applied to each candidate.", PH + "phase2b_verify.md:46", type="list", affects=["precision", "recall"]),
    K("prompt.phase2b.fp_needs_citation", "verification_depth.adversarial_review", "phase2b", True, "A FALSE POSITIVE verdict must cite the file:line that eliminates the finding, otherwise it stands.", PH + "phase2b_verify.md:261", affects=["recall"]),
    K("prompt.phase2b.downgrade_discipline", "verification_depth.adversarial_review", "phase2b", "all call sites verified", "A finding is only downgraded when every call site of the sink is shown non-exploitable.", PH + "phase2b_verify.md:111", affects=["recall", "cost"]),
    K("prompt.phase2b.full_codebase_search", "verification_depth.adversarial_review", "phase2b", True, "Verification searches the whole repo, not the originating partition.", PH + "phase2b_verify.md:48", affects=["precision"]),
    K("prompt.phase2b.verdicts", "gating_and_thresholds.verdict_scheme", "phase2b", ["CONFIRMED", "FALSE POSITIVE"], "Verdicts of the disprove pass; there is no numeric confidence.", PH + "phase2b_verify.md:249", type="list", affects=["precision", "recall"]),
    K("prompt.exploit_test.enabled", "verification_depth.exploit_testing", "phase3b", True, "Every confirmed finding needs an exploit test that proves the attacker's goal, not just that the code runs.", PH + "phase3_reproduce_test.md:109", affects=["precision", "cost"]),
    K("prompt.exploit_test.execution", "verification_depth.exploit_testing", "phase3b", "mentally executed unless Bash is enabled", "Whether tests are run or reasoned through.", PH + "phase3_reproduce_test.md:194", type="enum", domain=["static", "executed"], basis="code", requires="cli.enable_bash for executed", affects=["precision"]),
    K("prompt.exploit_test.outcomes", "verification_depth.exploit_testing", "phase3b", ["PASS -> confirmed", "mitigated -> Code Smell", "framework prevents -> Code Smell", "type system prevents -> eliminate", "can't construct -> Potential", "exception before sink -> eliminate"], "What each test result does to the finding. Only PASS proceeds.", PH + "phase3_reproduce_test.md:192", type="list", affects=["precision", "recall"]),
    K("prompt.exploit_test.poc_before_code_smell", "verification_depth.exploit_testing", "phase3b", True, "A PoC and test must be written before any downgrade to Code Smell.", PH + "phase3_reproduce_test.md:211", affects=["recall"]),
    K("prompt.exploit_test.config_provable", "verification_depth.exploit_testing", "phase3b", "static verification test", "Missing-control findings are proven by asserting the config, with no network proof required.", PH + "phase3_reproduce_test.md:231", affects=["recall"]),
    K("prompt.poc_format", "verification_depth.exploit_testing", "phase3a", ["runnable PoC", "static data flow trace"], "PoC form, chosen by whether a test environment exists.", PH + "phase3_reproduce_test.md:44", type="list", affects=["precision"]),
    K("prompt.sweep.enabled", "verification_depth.sweep", "phase3d", True, "After confirmation, grep the whole repo for each root cause (source and sink patterns, transitive callers).", PH + "phase3d_sweep.md:6", affects=["recall", "cost"]),
    K("prompt.sweep.reentry", "verification_depth.sweep", "phase3d", "new instances go through the full pipeline", "Sweep hits are candidates, not findings.", PH + "phase3d_sweep.md:48", affects=["recall", "precision"]),
    K("prompt.fix_verify.gates", "verification_depth.fix_validation", "verify", ["sink_mitigated", "reachability", "class_eliminated", "sweep_complete"], "Gates the separate fix-verify skill applies to a claimed fix.", "vulnhunt-fix-verify/phases/phase2_verify.md", type="list", affects=["precision"]),
    K("prompt.fix_verify.comment_rules", "verification_depth.fix_validation", "verify", "R0-R7", "How developer comments are treated: only cited, confirmed claims count, and only as hints; injection attempts are flagged.", "vulnhunt-fix-verify/comment_rules.md", affects=["precision", "safety"]),
    # ---------------- dedup_and_merge -------------------------------------
    K("prompt.aggregate.any_candidate_wins", "dedup_and_merge.merge_rules", "phase2", True, "An input is a CANDIDATE if any class agent says so; SAFE only if all do.", PH + "phase2_hunt.md:213", affects=["recall"]),
    K("prompt.aggregate.same_sink_dedup", "dedup_and_merge.dedup_rules", "phase2", "same file:line", "Candidates at the same sink file:line merge, keeping the worst severity and all data flows.", PH + "phase2_hunt.md:227", affects=["precision"]),
    K("prompt.anti_merge_rule", "dedup_and_merge.merge_rules", "phase2b", ["attacker auth level", "entry point", "gateway context", "exploited parameter"], "Findings differing in any of these must stay separate; silent omission counts as merging.", PH + "phase2b_verify.md:267", type="list", affects=["recall"]),
    K("prompt.one_vuln_per_sink", "dedup_and_merge.merge_rules", "phase4", True, "One VULN-NNN per sink location; the summary has one row per exploit-test PASS.", SK + ":289", affects=["recall", "reporting"]),
    K("prompt.universal_auth_rollup", "dedup_and_merge.merge_rules", "phase2b", "VULN-PLATFORM-AUTHN / AUTHZ", "The one allowed merge: a platform-wide auth gap subsumes per-endpoint findings and gets one PoC.", PH + "phase2b_verify.md:219", affects=["reporting", "cost"]),
    K("issues.semantic_dedup", "dedup_and_merge.dedup_rules", "issues", True, "Model pass that compares new findings to open issues (same location, root cause and impact).", AG + "config.py:228", "config_file", affects=["reporting", "cost"]),
    K("code.vulnfix_key", "dedup_and_merge.dedup_rules", "issues", "sha256(location|cwe|root_cause)[:16]", "Deterministic key used for exact issue dedup.", AG + "issues_extract.py", "code_constant", affects=["reporting"]),
    K("issues.token_budget_fraction", "dedup_and_merge.dedup_rules", "issues", 0.7, "Share of the model context a dedup request may fill before issues are chunked.", AG + "config.py:234", "config_file", affects=["cost"]),
    K("issues.model_context_tokens", "dedup_and_merge.dedup_rules", "issues", 200000, "Context size assumed when chunking dedup requests.", AG + "config.py:236", "config_file", affects=["cost"]),
    K("issues.max_open_issues", "dedup_and_merge.dedup_rules", "issues", 1000, "Open issues fetched as the dedup pool.", AG + "config.py:230", "config_file", affects=["cost"]),
    K("code.issue_body_truncation_chars", "dedup_and_merge.dedup_rules", "issues", 4000, "Issue body characters shown to the dedup model.", AG + "issues_dedup.py:54", "code_constant", affects=["cost"]),
    # ---------------- ranking_and_reporting -------------------------------
    K("prompt.report_format", "ranking_and_reporting.output_files", "phase4", "README.md with summary table, per-finding detail, inventory, sweep table, code smells", "Final report layout.", PH + "phase4_report.md:1", affects=["reporting"]),
    K("prompt.code_smell_section", "ranking_and_reporting.channels", "phase4", True, "Non-exploitable risky patterns go to a separate section without VULN ids.", PH + "phase3_reproduce_test.md:206", affects=["reporting", "precision"]),
    K("prompt.cost_report", "ranking_and_reporting.output_files", "all phases", True, "Run /cost after each phase and report it.", SK + ":229", affects=["reporting"]),
    K("cli.stage_toggles", "ranking_and_reporting.output_files", "agent", {"scan": True, "publish": "config", "issues": "config"}, "--scan/--no-scan, --publish/--no-publish, --issues/--no-issues.", AG + "__main__.py:149", "cli_flag", type="map", affects=["reporting"]),
    K("publish.enabled", "ranking_and_reporting.output_files", "publish", False, "Push the results directory to a reports repo.", AG + "config.py:155", "config_file", affects=["reporting"]),
    K("issues.enabled", "ranking_and_reporting.issue_filing", "issues", True, "File one GitHub issue per confirmed finding.", AG + "config.py:222", "config_file", affects=["reporting"]),
    K("issues.labels", "ranking_and_reporting.issue_filing", "issues", ["security", "vulnhunter"], "Labels on posted issues.", AG + "config.py:224", "config_file", affects=["reporting"]),
    K("issues.notify_clean_scan", "ranking_and_reporting.issue_filing", "issues", True, "Post a closed receipt issue when a scan finds nothing.", AG + "config.py:241", "config_file", affects=["reporting"]),
    K("prompt.issue_extract_scope", "ranking_and_reporting.issue_filing", "issues", "Confirmed rows only", "Code smells, observations and informational items are not filed.", AG + "issues_extract.py:72", affects=["precision", "reporting"]),
    # ---------------- remediation -----------------------------------------
    K("prompt.fix_strategies_only", "remediation.enablement", "phase3c", "describe, do not edit", "The scan proposes fix strategies but never edits source.", PH + "phase3c_fixes.md:8", affects=["safety"]),
    K("fix.modes.default", "remediation.enablement", "fix", "auto", "Fix skill mode: in-place (one PR per cluster of issues) or fork (one PR per finding).", FX + "config.json", "config_file", affects=["reporting"]),
    K("fix.verification.max_repair_attempts", "remediation.limits", "fix", 3, "Repair attempts per finding in fork mode; in-place mode is uncapped.", FX + "config.json", "config_file", affects=["cost"]),
    K("fix.verification.max_retries", "remediation.limits", "fix", 2, "Verification retries.", FX + "config.json", "config_file", affects=["cost"]),
    K("fix.verification.test_timeout_seconds", "remediation.limits", "fix", 120, "Timeout per test run.", FX + "config.json", "config_file", affects=["reliability"]),
    K("fix.behavior.confirm_before_push", "remediation.policy", "fix", False, "Ask before pushing. SKILL.md documents the default as true; config.json says false.", FX + "config.json", "config_file", affects=["safety"]),
    K("fix.github.pr_draft", "remediation.policy", "fix", True, "Open PRs as drafts.", FX + "config.json", "config_file", affects=["safety"]),
    K("prompt.fix.tdd_gate", "remediation.policy", "fix", "RED evidence on disk before any source edit", "The failing security test must exist before the fix is written.", FX + "prompts/implement.md", affects=["precision"]),
    K("prompt.fix.completeness_tiers", "remediation.policy", "fix", ["FULL", "MITIGATION", "WORKAROUND"], "Tier each fix is classified into; the fallback judgment never returns FULL.", FX + "prompts/tier_judgment.md", type="list", affects=["precision", "reporting"]),
    K("code.fix.delivery_gates", "remediation.policy", "fix", 7, "Mechanical gates run before delivery (severity mask, body completeness, scope, idempotency, anti-merge at 0.6, verification table, test naming).", FX + "scripts/run-gates.py:162", "code_constant", affects=["precision", "safety"]),
    K("prompt.fix.operator_gate", "remediation.policy", "fix", "approve at every phase boundary", "A human approves each phase; there is no fast path.", FX + "SKILL.md:299", affects=["safety"]),
    # ---------------- runtime_and_infra ----------------------------------
    K("anthropic.api_key", "runtime_and_infra.credentials_and_tls", "all", "", "API key; falls back to ANTHROPIC_API_KEY.", AG + "config.py:58", "config_file", affects=[]),
    K("anthropic.bedrock_base_url", "runtime_and_infra.credentials_and_tls", "all", "", "Bedrock gateway URL.", AG + "config.py:59", "config_file", affects=[]),
    K("anthropic.aws_region", "runtime_and_infra.credentials_and_tls", "all", "us-east-1", "AWS region for Bedrock.", AG + "config.py:60", "config_file", affects=[]),
    K("oauth.*", "runtime_and_infra.credentials_and_tls", "all", {"expiry_safety_factor": 0.9, "default_lifetime_seconds": 3600, "http_timeout_seconds": 30}, "OAuth token endpoint, client id/secret and refresh timing for bedrock_oauth.", AG + "config.py:69", "config_file", type="map", requires="anthropic.auth_mode == bedrock_oauth", affects=["reliability"]),
    K("tls.ssl_cert_path", "runtime_and_infra.credentials_and_tls", "all", "", "CA bundle path.", AG + "config.py:79", "config_file", affects=[]),
    K("scan.no_proxy", "runtime_and_infra.credentials_and_tls", "all", "localhost,127.0.0.1,169.254.169.254,10.0.0.0/8,172.16.0.0/12,192.168.0.0/16", "NO_PROXY passed to the session; proxy variables are blanked.", AG + "config.py:119", "config_file", affects=["safety"]),
    K("github.*", "runtime_and_infra.vcs_integration", "all", {"host": "github.com"}, "GitHub host and two tokens: one to clone and file issues, one to publish reports.", AG + "config.py:145", "config_file", type="map", affects=[]),
    K("publish.*", "runtime_and_infra.vcs_integration", "publish", {"branch": "main", "commit_author_name": "VulnHunter Agent"}, "Destination repo, branch and commit author for published reports.", AG + "config.py:156", "config_file", type="map", requires="publish.enabled", affects=[]),
    K("scan.clone_base_dir", "runtime_and_infra.state_and_paths", "clone", "./clones", "Where targets are cloned.", AG + "config.py:101", "config_file", affects=[]),
    K("verify.*", "runtime_and_infra.hostile_repo_hardening", "verify", {"max_comment_pages": 20, "max_timeline_bytes": 5000000, "max_event_pages": 20, "max_edit_diff_bytes": 200000, "max_edit_total_bytes": 5000000, "clone_timeout_seconds": 300}, "Verify-mode bounds and allowlists (clone hosts, token path prefixes, repo aliases).", AG + "config.py:262", "config_file", type="map", affects=["safety"]),
    K("telemetry.enabled", "runtime_and_infra.observability", "all", False, "OpenTelemetry export, including user prompts and tool content.", AG + "config.py:91", "config_file", affects=[]),
    K("audit.enabled", "runtime_and_infra.observability", "all", True, "JSONL audit and findings event streams.", AG + "config.py:185", "config_file", affects=[]),
    K("logging.per_turn_usage", "runtime_and_infra.observability", "all", False, "Log token usage per turn.", AG + "config.py:205", "config_file", affects=[]),
    K("code.bedrock_cache_ttl", "runtime_and_infra.caching", "all", "1h on Bedrock", "ENABLE_PROMPT_CACHING_1H_BEDROCK is set for Bedrock runs; no other caching control exists.", AG + "build_settings.py:151", "code_constant", affects=["cost"]),
    K("code.strict_mcp_config", "runtime_and_infra.hostile_repo_hardening", "benchmark", True, "Harness passes --strict-mcp-config and --setting-sources user so the scanned repo cannot add MCP servers or settings.", HA + "scan.py:456", "code_constant", affects=["safety"]),
    # ---------------- evaluation ------------------------------------------
    K("harness.judge_match_rule", "evaluation.benchmark", "benchmark", "same class (or earlier finding in the same flow) + same location + same root cause", "What the LLM judge counts as 'detected'. Line numbers, severity and wording need not match.", HA + "benchmark/judge.py:18", "prompt_text", affects=["reporting"]),
    K("harness.metric", "evaluation.benchmark", "benchmark", "detection rate (recall) overall and per type", "The only score the benchmark computes; there is no precision or false-positive metric.", HA + "benchmark/tally.py:25", "code_constant", affects=["reporting"]),
    K("harness.stable_threshold", "evaluation.benchmark", "benchmark", 3, "--skip-stable skips ground-truth findings detected in this many consecutive runs.", HA + "benchmark/finding_history.py:64", "code_constant", affects=["cost"]),
    K("harness.miss_diagnostic", "evaluation.benchmark", "benchmark", "one agentic diagnosis per miss, 1200 s timeout", "Suggests a minimal prompt edit for each missed finding and rates its false-positive risk.", HA + "benchmark/analyze_misses.py:43", "prompt_text", affects=["reporting"]),
]

VH_PIPELINE = """\
# θ.<id> refers to a knob id in `categories` below.
# The control flow below is written in prompts (SKILL.md and phases/*.md); only
# agent_scan is Python.
agent_scan(repo_url, θ):                                  # vulnhunter-agent/agent/runner.py
  clone(repo_url, depth = θ.code.clone_depth)
  refuse if an old results directory exists               # θ.code.prior_results_guard
  tools   = θ.scan.allowed_tools - {Bash}                 # + Bash only with --no-read-only --enable-bash
  session = SDK(model = θ.anthropic.model, tools, permission = θ.scan.permission_mode,
                no system prompt, no max_turns, no budget cap)
  send("/vulnhunt <clone>" + θ.code.kickoff_metadata)
  while subagents pending: send(θ.code.continuation_prompt)
    abort after θ.code.max_stalled_continuations idle re-prompts
  publish results if θ.publish.enabled
  if θ.issues.enabled: extract Confirmed findings -> dedup -> post issues

/vulnhunt (orchestrator prompt):                          # vulnhunt/SKILL.md
  if interactive and model < θ.skill.min_model: STOP
  mode = STATIC | EXECUTE                                 # EXECUTE needs Bash and installs dependencies
  A recon = SUBAGENT(phase1_recon):
      inventory of inputs; sinks; call graph (depth θ.prompt.recon.callgraph_depth)
      shared infra = modules imported by > θ.prompt.recon.shared_infra_import_share of entry points
      partitions SG-1..n = union-find on shared app functions
        split if > θ.prompt.recon.oversize_inputs inputs or > θ.prompt.recon.oversize_files files
      tag each partition PRODUCTION | DEV-ONLY; threat model (3 auth fields, file:line or NONE)
  B hunt:
      jobs = [trace(p, c) for p in PRODUCTION partitions for c in θ.prompt.hunt.class_groups]
           + [sink_audit] * θ.prompt.hunt.sink_driven_agents
      run jobs in waves of θ.prompt.hunt.wave_size; sink audit runs last
      trace(p, c): for each input in p:
          follow it forward (θ.prompt.investigation_discipline)
          -> CANDIDATE | SAFE | NO-MATCH | CROSS-CLASS | DESIGN-INTENT
          each CANDIDATE must pass θ.prompt.hard_gates in order
      aggregate: CANDIDATE if any agent says so; merge same sink file:line;
                 count dispositions == inventory size; absent-input checkpoint
  C verified = SUBAGENT(phase2b):                         # θ.prompt.phase2b.*
      count candidates; consensus-skip; nine checks per candidate
      -> CONFIRMED | FALSE POSITIVE (needs file:line)
  D SUBAGENT(phase3 + phase3c): for f in CONFIRMED with severity in θ.prompt.scope.phase3_severity_floor:
      write PoC; write exploit test; run it if EXECUTE else reason through it
      PASS -> fix strategy (not applied); otherwise Code Smell | Potential | eliminated
  E SUBAGENT(phase3d): grep each root cause across the full repo; new hits re-enter the pipeline
  report (orchestrator, phase4): one VULN-NNN per sink location, after count checks
"""


# ==========================================================================
# Exhaustive prompt pass: rows written by readers into tools/prompt_knobs/*.json
# ==========================================================================
AFFECTS = {"recall", "precision", "cost", "latency", "safety", "reliability", "reporting"}
HARNESS_ROOT = {"vh": ROOT / "VulnHunter", "vvah": ROOT / "visa-vulnerability-agentic-harness"}


def _norm(t):
    return re.sub(r"\s+", " ", t).strip()


def prompt_rows(prefix, taken):
    """Load, validate and convert reader output. A row is kept only if its quote
    is found in the cited file at (or within 3 lines of) the cited line."""
    base = HARNESS_ROOT[prefix]
    rows, rejects, cache = [], [], {}
    for jf in sorted((HERE / "prompt_knobs").glob(prefix + "_*.json")):
        try:
            data = json.loads(jf.read_text())
        except Exception as e:  # noqa: BLE001
            rejects.append((jf.name, "-", f"file does not parse: {e}"))
            continue
        for r in data:
            rid = str(r.get("id", "")).strip()
            src = str(r.get("source", ""))
            path, _, line = src.rpartition(":")
            for pre in ("VulnHunter/", "visa-vulnerability-agentic-harness/"):
                if path.startswith(pre):
                    path = path[len(pre):]
            f = base / path
            if not rid or not line.isdigit() or not f.is_file():
                rejects.append((jf.name, rid, f"bad source {src!r}"))
                continue
            if r.get("category") not in CATEGORY_GUIDE:
                rejects.append((jf.name, rid, f"unknown category {r.get('category')!r}"))
                continue
            group = re.sub(r"[^a-z0-9_]", "_", str(r.get("group") or "misc").lower())
            lines = cache.setdefault(f, f.read_text(errors="replace").splitlines())
            n, q = int(line), _norm(str(r.get("quote", "")))
            hit = None
            if len(q) >= 12:
                for d in (0, 1, -1, 2, -2, 3, -3):
                    i = n + d
                    if 1 <= i <= len(lines) and q in _norm(lines[i - 1]):
                        hit = i
                        break
                if hit is None:  # quote may straddle a wrapped line
                    for d in (0, -1, 1):
                        i = n + d
                        if 1 <= i < len(lines) and q in _norm(lines[i - 1] + " " + lines[i]):
                            hit = i
                            break
            if hit is None:
                rejects.append((jf.name, rid, f"quote not found near {src}"))
                continue
            while rid in taken:
                rid += "_2"
            taken.add(rid)
            default = r.get("default", True)
            typ = r.get("type") or _type_of(default)
            row = OrderedDict(id=rid, does=str(r.get("does", "")).strip(), stage=str(r.get("stage", "")),
                              origin="prompt_text", kind="implicit", type=typ)
            if r.get("domain"):
                row["domain"], row["domain_basis"] = r["domain"], "code"
            elif typ == "bool":
                row["domain"], row["domain_basis"] = [True, False], "code"
            row["default"] = default
            row["source"] = f"{path}:{hit}"
            row["quote"] = str(r.get("quote", "")).strip()
            row["requires"] = r.get("requires")
            row["affects"] = [a for a in (r.get("affects") or []) if a in AFFECTS]
            rows.append((f"{r['category']}.{group}", row))
    return rows, rejects


# ==========================================================================
# Emit
# ==========================================================================
def nest(rows):
    cats = OrderedDict((c, OrderedDict()) for c in CATEGORY_GUIDE)
    for cg, row in rows:
        cat, group = cg.split(".")
        if cat not in cats:
            raise SystemExit(f"unknown category {cat} for {row['id']}")
        cats[cat].setdefault(group, []).append(plain(row))
    return OrderedDict((c, dict(g)) for c, g in cats.items() if g)


def plain(x):
    if isinstance(x, dict):
        return {k: plain(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [plain(v) for v in x]
    return x


class Dumper(yaml.SafeDumper):
    pass


Dumper.add_representer(OrderedDict, lambda d, data: d.represent_dict(data.items()))
Dumper.add_representer(str, lambda d, s: d.represent_scalar("tag:yaml.org,2002:str", s, style="|" if "\n" in s else None))


def emit(path, harness, about, source_root, commit, pipeline, rows, notes):
    ids = [r["id"] for _, r in rows]
    dupes = {i for i in ids if ids.count(i) > 1}
    if dupes:
        raise SystemExit(f"duplicate ids in {harness}: {sorted(dupes)}")
    cats = nest(rows)
    counts = OrderedDict((c, sum(len(v) for v in g.values())) for c, g in cats.items())
    origin_counts = OrderedDict()
    for _, r in rows:
        origin_counts[r["origin"]] = origin_counts.get(r["origin"], 0) + 1
    doc = OrderedDict([
        ("harness", harness),
        ("about", about),
        ("source_root", source_root),
        ("commit", commit),
        ("generated_by", "comparison-results/tools/build_registry.py"),
        ("knob_count", len(rows)),
        ("knobs_by_origin", dict(origin_counts)),
        ("knobs_by_category", dict(counts)),
        ("schema", dict(SCHEMA)),
        ("category_guide", dict((c, CATEGORY_GUIDE[c]) for c in cats)),
        ("notes", notes),
        ("pipeline", pipeline),
        ("categories", cats),
    ])
    cats_only = OrderedDict([("categories", doc.pop("categories"))])
    head = yaml.dump(doc, Dumper=Dumper, sort_keys=False, default_flow_style=False, width=10000, allow_unicode=True)
    body = yaml.dump(cats_only, Dumper=Dumper, sort_keys=False, default_flow_style=None, width=10000, allow_unicode=True)
    text = head + body
    # blank line before each top-level key, category and group, for readability
    text = re.sub(r"\n(?=[a-z_]+:)", "\n\n", text)
    text = re.sub(r"\n(  [a-z_]+:\n)", r"\n\n\1", text)
    text = re.sub(r"\n(    [a-z0-9_]+:\n    - )", r"\n\n\1", text)
    path.write_text(text)
    yaml.safe_load(path.read_text())  # must parse
    return len(rows), counts, origin_counts


def write_categories(by_harness):
    """knob_categories.yaml: only the hierarchy (category -> sub-group) with counts."""
    tree = OrderedDict()
    for cat, about in CATEGORY_GUIDE.items():
        groups, totals = OrderedDict(), OrderedDict()
        for h, rows in by_harness.items():
            totals[h] = 0
            for cg, _ in rows:
                c, g = cg.split(".")
                if c == cat:
                    groups.setdefault(g, OrderedDict((x, 0) for x in by_harness))[h] += 1
                    totals[h] += 1
        tree[cat] = OrderedDict(about=about, knobs=dict(totals),
                                sub_groups=OrderedDict((g, dict(v)) for g, v in sorted(groups.items())))
    doc = OrderedDict([
        ("about", "The knob hierarchy only: parent categories and their sub-groups, with the number of knobs each harness has in them. The knobs themselves are in vulnhunter.knobs.yaml and vvah.knobs.yaml."),
        ("generated_by", "comparison-results/tools/build_registry.py"),
        ("levels", ["category", "sub_group", "knob (in the per-harness files)"]),
        ("totals", {h: len(r) for h, r in by_harness.items()}),
        ("categories", tree),
    ])
    text = yaml.dump(doc, Dumper=Dumper, sort_keys=False, default_flow_style=None, width=10000, allow_unicode=True)
    text = re.sub(r"\n(  [a-z_]+:\n    about)", r"\n\n\1", text)
    (OUT / "knob_categories.yaml").write_text(text)


def main():
    vv_rows, n_cfg = vvah_rows()
    vv_rows += VVAH_EXTRA
    vh_rows = list(VH)
    all_rejects = []
    for prefix, rows in (("vvah", vv_rows), ("vh", vh_rows)):
        extra, rej = prompt_rows(prefix, {r["id"] for _, r in rows})
        rows += extra
        all_rejects += rej
        print(f"{prefix}: {len(extra)} prompt knobs merged from the exhaustive pass, {len(rej)} rejected")
    (HERE / "prompt_knobs" / "REJECTED.tsv").write_text(
        "file\tid\treason\n" + "".join(f"{a}\t{b}\t{c}\n" for a, b, c in all_rejects))
    out = {}
    out["vvah"] = emit(
        OUT / "vvah.knobs.yaml", "vvah",
        "Visa Vulnerability Agentic Harness (vvaharness 1.5.1). A Python pipeline: stages S0-S11, typed config, model calls wrapped by deterministic code.",
        "visa-vulnerability-agentic-harness", "0e6f00d", VVAH_PIPELINE, vv_rows,
        [
            "Every config key in _STEP_DEFAULTS and in the five shipped profiles is listed (values read from source by tools/dump_vvah_knobs.py).",
            "Prompt-text knobs with ids starting p. come from an exhaustive line-by-line pass over the stage prompts, skill playbooks, output schemas, tool descriptions, injected text, remediation and validation prompts; each carries a quote that was checked against the source. The exploit-verification prompts (classifier, mapper, attacker, judge) were NOT covered by that pass.",
            "Knobs with ids starting prompt. are the earlier hand-picked summary rows; some overlap with finer-grained p. rows. Knobs with origin code_constant, cli_flag or env_var are a selection, not an exhaustive list.",
            "Two default layers exist. `builtin` is what a hand-written config gets; `profile` is what default.yaml ships and what normally runs. They often differ.",
            "max_turns means different things per backend: a hard cap on sdk and cli, a recursion floor (max_turns + 900) on deepagents, which is the default route.",
            "step4.evidence_gate only enforces when step4.planning is on and the route is deepagents, so it is inactive in the default and semgrep profiles.",
            "S2 sets the coverage ceiling: S4 only examines files named in a threat's surface_files.",
            "Keys present in the profiles for stages that make no model call (models.preprocess, models.decompose) are still required and probed.",
            "The config loader is not schema-validated: unknown keys are silently ignored.",
        ])
    out["vulnhunter"] = emit(
        OUT / "vulnhunter.knobs.yaml", "vulnhunter",
        "Capital One VulnHunter. Prompt-only Claude Code skills (/vulnhunt, /vulnhunter-fix, /vulnhunt-fix-verify) plus a Python agent that launches them headlessly and a benchmark harness.",
        "VulnHunter", "6d25b5c", VH_PIPELINE, vh_rows,
        [
            "Most knobs that shape detection are prompt_text: numbers and rules written into SKILL.md and phases/*.md. Changing one means editing a prompt file; there is no config key for it.",
            "Real config (origin config_file) is almost all plumbing: model, auth, tools, timeouts, GitHub.",
            "Knobs with kind absent are limits the harness does not set at all (turns, cost, reasoning tier).",
            "Prompt-text knobs with ids starting p. come from an exhaustive line-by-line pass over every prompt file (scan skill, fixer skill and its rubrics, fix-verify skill, and the prompts written inline in Python); each carries a quote that was checked against the source.",
            "Knobs with ids starting prompt. are the earlier hand-picked summary rows; some overlap with finer-grained p. rows.",
            "A few config sections are folded into one row each (oauth.*, github.*, publish.*, verify.*) because they are plumbing.",
            "The agent's default tool list has no Grep, while the skill text tells the model to use Grep throughout.",
            "This registry describes the harness-comparison/VulnHunter checkout at 6d25b5c, not the edited copy in update-cap-one-harness.",
        ])
    write_categories(OrderedDict([("vulnhunter", vh_rows), ("vvah", vv_rows)]))
    for h, (n, counts, origins) in out.items():
        print(h, n, dict(origins))
        for c, k in counts.items():
            print(f"   {c:32s} {k}")
    print("vvah config keys read from source:", n_cfg)


if __name__ == "__main__":
    main()
