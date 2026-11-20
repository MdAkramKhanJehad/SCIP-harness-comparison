# vvaharness/util/metrics.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/util/metrics.py.evidence.json`. SHA-256: `fbaeadaf0e8fb234cab3cea8326d0ff88c0d9e96c2683e680b645d7e6750e84b`.

```sudo
// Source: vvaharness/util/metrics.py:15-20
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from collections import defaultdict; preserve alias and import-time effects. Then Resolve source import from collections.abc import Mapping; preserve alias and import-time effects. Then Resolve source import from datetime import UTC, datetime; preserve alias and import-time effects.
// Source: vvaharness/util/metrics.py:21-32
In source order: Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from vvaharness.lang.detect import EXT_TO_LANG; preserve alias and import-time effects. Then Resolve source import from vvaharness.models import ContextPackage, InvestigationUnit, ScanMetrics, ScopeEntry, TaskManifest; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import errlog, stage_telemetry; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.counters import COUNTERS; preserve alias and import-time effects.
// Source: vvaharness/util/metrics.py:33-34
In source order: Resolve source import from vvaharness.util.pricing import PricingTable; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.tokens import TOKENS; preserve alias and import-time effects.
// Source: vvaharness/util/metrics.py:37-44
// Source signature: _priced_cost_usd(tok: dict, role_models: Mapping[str, str] | None, pricing: PricingTable | None) -> float | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _priced_cost_usd(tok, role_models, pricing) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/metrics.py:39-39
  In source order: Retain source documentation literal source_literal_39_4; it is not a model call.
  // Source: vvaharness/util/metrics.py:41-42
  if (the source predicate not pricing or not role_models is truthy) {
    // Source: vvaharness/util/metrics.py:42-42
    End this invocation with None.
  }
  // Source: vvaharness/util/metrics.py:43-43
  In source order: Evaluate once stage_telemetry.compose_stage_section({}, tok, role_models, pricing); assign in source target order to section.
  // Source: vvaharness/util/metrics.py:44-44
  End this invocation with section['totals']['cost_usd'].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/metrics.py:48-149
In source order: Evaluate once (('taint-', 'taint'), ('catchall-', 'catchall'), ('spec-', 'specialist'), ('threat-', 'threat'), ('chunk-', 'risk')); assign in source target order to _KIND_PREFIXES. Then Evaluate once ('s2_threats_raw', 's2_threats_truncated', 's2_threats_promoted', 's2_frontier_files_excluded', 's2_frontier_entry_points_excluded', 's2_frontier_sinks_excluded', 's2_frontier_modules_excluded', 's2_assets_truncated', 's2_trust_boundaries_truncated', 's2_prompt_modules_truncated', 's2_prompt_entry_points_truncated', 's2_inventory_files_truncated', 's2_baseline_undisposed_recovered', 's2_surface_files_dropped', 's2_evidence_gate_rejected', 's2_evidence_gate_rejected_relented', 's3_unknown_file_ids', 's3_dropped_paths', 's3_relocated_paths', 's4_findings_truncated', 's4_finding_extra_cwe_collapsed', 's4_unit_key_deduped', 's4_unit_no_outcome', 's4_batch_member_uninvestigated', 's4_batch_member_failed', 's4_batch_member_resubmitted', 's4_batch_member_recovered', 's4_evidence_gate_rejected', 's4_evidence_gate_rejected_relented', 'deepagents_oversize_prompts', 'deepagents_tool_state_not_roundtripped', 'deepagents_path_jail_refused', 'llm_truncated_replies', 'llm_truncated_below_budget', 'llm_adapter_evidence_gate_unenforced', 'cli_mcp_evidence_gate_unenforced', 'evidence_gate_stood_down_degenerate_graph', 's6_evidence_gate_rejected', 's6_evidence_gate_rejected_relented', 'llm_turn_cap_exhausted', 's6_confirmed_without_vector', 's6_cvss_zero_impact_on_tp', 's6_confidence_clamped', 's6_confidence_uniform', 's6_finding_line_correction_reverted_reanchor', 's6_batch_structured_split', 's6_batch_guardrail_split', 's6_batch_generic_split', 's6_structured_retry_attempted', 's6_structured_retry_recovered', 's6_truncated_retry_attempted', 's6_truncated_retry_recovered', 'llm_structured_submit_rejected', 'llm_structured_prose_reask', 's1_autoexclude_language_veto', 'sdk_tool_choice_dropped_for_thinking', 'deepagents_tool_choice_dropped', 's1_truncated_retry_attempted', 's1_truncated_retry_recovered', 's2_structured_retry_attempted', 's2_structured_retry_recovered', 's2_truncated_retry_attempted', 's2_truncated_retry_recovered', 's4_structured_retry_attempted', 's4_structured_retry_recovered', 's4_truncated_retry_attempted', 's4_truncated_retry_recovered', 's7_structured_retry_attempted', 's7_structured_retry_recovered', 's7_truncated_retry_attempted', 's7_truncated_retry_recovered', 's8_structured_retry_attempted', 's8_structured_retry_recovered', 's8_truncated_retry_attempted', 's8_truncated_retry_recovered', 'ev_classify_truncated_retry_attempted', 'ev_classify_truncated_retry_recovered', 'llm_structured_retry_truncated', 's2_empty_retry_attempted', 's2_empty_retry_recovered', 's2_parse_repair_attempted', 's2_parse_repair_recovered', 's4_outcome_repaired_attempt', 's4_outcome_repaired_ok', 's4_batch_repaired_attempt', 's4_batch_repaired_ok', 's6_outcome_repaired_attempt', 's6_outcome_repaired_ok', 'llm_call_timeouts', 'llm_call_budget_near', 'llm_model_refusals', 'llm_refusal_retry_attempted', 'llm_refusal_retry_recovered', 'llm_truncated_retry_attempted', 'llm_truncated_retry_recovered', 's6_replayed_fp_held', 's6_replayed_tp_shipped', 's6_fp_premise_contradicted', 's6_outcome_members_resubmitted', 's6_outcome_members_recovered', 's2_orphan_settled', 's4_orphan_settled', 's6_orphan_settled', 's8_orphan_settled'); assign in source target order to _INT_COUNTER_NAMES.
// Source: vvaharness/util/metrics.py:152-158
// Source signature: _classify_unit_kind(u: InvestigationUnit) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _classify_unit_kind(u) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/metrics.py:153-154
  In source order: Retain source documentation literal source_literal_153_4; it is not a model call. Then Evaluate once u.id; assign in source target order to uid.
  // Source: vvaharness/util/metrics.py:155-157
  for each (prefix, kind) in _KIND_PREFIXES {
    // Source: vvaharness/util/metrics.py:156-157
    if (the source predicate uid.startswith(prefix) is truthy) {
      // Source: vvaharness/util/metrics.py:157-157
      End this invocation with kind.
    }
  }
  // Source: vvaharness/util/metrics.py:158-158
  End this invocation with 'other'.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/metrics.py:161-162
// Source signature: now_iso() -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn now_iso() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/metrics.py:162-162
  End this invocation with datetime.now(UTC).strftime('%Y-%m-%dT%H:%M:%SZ').
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/metrics.py:165-171
// Source signature: _elapsed_sec(start_ts: str, end_ts: str) -> float
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _elapsed_sec(start_ts, end_ts) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/metrics.py:166-171
  Perform the following protected operations {
    // Source: vvaharness/util/metrics.py:167-168
    In source order: Evaluate once datetime.fromisoformat(start_ts.replace('Z', '+00:00')); assign in source target order to s. Then Evaluate once datetime.fromisoformat(end_ts.replace('Z', '+00:00')); assign in source target order to e.
    // Source: vvaharness/util/metrics.py:169-169
    End this invocation with (e - s).total_seconds().
  }
  // Source: vvaharness/util/metrics.py:170-171
  On the first matching source exception Exception, in handler order {
    // Source: vvaharness/util/metrics.py:171-171
    End this invocation with 0.0.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/metrics.py:174-203
// Source signature: refresh_tokens(metrics: ScanMetrics | None, *, end_ts: str | None=None, role_models: Mapping[str, str] | None=None, pricing: PricingTable | None=None) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn refresh_tokens(metrics, end_ts, role_models, pricing) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/metrics.py:178-178
  In source order: Retain source documentation literal source_literal_178_4; it is not a model call.
  // Source: vvaharness/util/metrics.py:180-181
  if (the source predicate metrics is None is truthy) {
    // Source: vvaharness/util/metrics.py:181-181
    End this invocation with None.
  }
  // Source: vvaharness/util/metrics.py:182-184
  if (the source predicate end_ts is truthy) {
    // Source: vvaharness/util/metrics.py:183-184
    In source order: Evaluate once end_ts; assign in source target order to metrics.end_ts. Then Evaluate once _elapsed_sec(metrics.start_ts, end_ts); assign in source target order to metrics.duration_sec.
  }
  // Source: vvaharness/util/metrics.py:186-189
  In source order: Evaluate once errlog.counts_by_stage(); assign in source target order to metrics.errors_by_stage. Then Evaluate once str(errlog.current_path()) if errlog.current_path().exists() else ''; assign in source target order to metrics.errors_log_path. Then Evaluate once COUNTERS.snapshot(); assign in source target order to counters.
  // Source: vvaharness/util/metrics.py:190-194
  for each name in _INT_COUNTER_NAMES {
    // Source: vvaharness/util/metrics.py:193-194
    if (the source predicate name in counters and name != 'llm_turn_cap_exhausted' is truthy) {
      // Source: vvaharness/util/metrics.py:194-194
      In source order: Evaluate setattr(metrics, name, counters[name]); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/util/metrics.py:195-195
  In source order: Evaluate once TOKENS.snapshot(); assign in source target order to tok.
  // Source: vvaharness/util/metrics.py:196-197
  if (the source predicate tok['calls_with_usage'] <= 0 is truthy) {
    // Source: vvaharness/util/metrics.py:197-197
    End this invocation with None.
  }
  // Source: vvaharness/util/metrics.py:198-202
  In source order: Evaluate once tok['prompt']; assign in source target order to metrics.prompt_tokens. Then Evaluate once tok['completion']; assign in source target order to metrics.completion_tokens. Then Evaluate once tok['total']; assign in source target order to metrics.total_tokens. Then Evaluate once tok.get('by_phase'); assign in source target order to metrics.tokens_by_phase. Then Evaluate once tok.get('usd'); assign in source target order to metrics.reported_cost_usd.
  // Source: vvaharness/util/metrics.py:203-203
  In source order: Evaluate once _priced_cost_usd(tok, role_models, pricing); assign in source target order to metrics.priced_cost_usd.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/metrics.py:206-324
// Source signature: build(ctx: ContextPackage, manifest: TaskManifest, *, repo_name: str, start_ts: str, end_ts: str, raw_findings: int, true_pos: int, false_pos: int, duplicates: int, discovered_tp: int=0, clone_tp: int=0, ev_rescued: int=0, unit_outcomes: dict[str, str] | None=None, external_input: bool=False, role_models: Mapping[str, str] | None=None, pricing: PricingTable | None=None) -> ScanMetrics
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn build(ctx, manifest, repo_name, start_ts, end_ts, raw_findings, true_pos, false_pos, duplicates, discovered_tp, clone_tp, ev_rescued, unit_outcomes, external_input, role_models, pricing) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/metrics.py:215-222
  In source order: Evaluate once Path(ctx.repo_root); assign in source target order to repo_root. Then Evaluate once unit_outcomes or {}; assign in source target order to outcomes. Then Evaluate once external_input and all((outcome in ('injected', 'confirmed') for outcome in outcomes.values())); assign in source target order to external_only. Then For analyzed, assign set(); source annotation set[str]. Then For scope, assign []; source annotation list[ScopeEntry].
  // Source: vvaharness/util/metrics.py:223-223
  In source order: For kind_counts, assign defaultdict(int); source annotation dict[str, int].
  // Source: vvaharness/util/metrics.py:224-230
  for each u in manifest.units {
    // Source: vvaharness/util/metrics.py:225-227
    if (the source predicate not external_only and outcomes.get(u.id, 'uninvestigated' if external_input else 'completed') == 'completed' is truthy) {
      // Source: vvaharness/util/metrics.py:227-227
      In source order: Evaluate analyzed.update(u.files); retain side effects and discard the expression result.
    }
    // Source: vvaharness/util/metrics.py:228-230
    In source order: Evaluate once _classify_unit_kind(u); assign in source target order to kind. Then Apply source augmented assignment kind_counts[kind] += 1 with source evaluation/in-place semantics. Then Evaluate scope.append(ScopeEntry(name=u.id, kind=kind, files=sorted(u.files))); retain side effects and discard the expression result.
  }
  // Source: vvaharness/util/metrics.py:232-239
  In source order: Evaluate once kind_counts.get('specialist', 0); assign in source target order to n_spec. Then Evaluate once kind_counts.get('catchall', 0); assign in source target order to n_catch. Then Evaluate once kind_counts.get('risk', 0); assign in source target order to n_risk. Then Evaluate once sorted({str(Path(f).parent).replace('\\', '/') for f in analyzed if '/' in f or '\\' in f} | {'.'}); assign in source target order to folders. Then For loc_scope, assign defaultdict(int); source annotation dict[str, int].
  // Source: vvaharness/util/metrics.py:240-240
  In source order: For loc_scan, assign defaultdict(int); source annotation dict[str, int].
  // Source: vvaharness/util/metrics.py:241-246
  for each f in ctx.all_files {
    // Source: vvaharness/util/metrics.py:242-244
    In source order: Evaluate once EXT_TO_LANG.get(Path(f).suffix.lower(), 'other'); assign in source target order to lang. Then Evaluate once _loc(repo_root / f); assign in source target order to loc. Then Apply source augmented assignment loc_scope[lang] += loc with source evaluation/in-place semantics.
    // Source: vvaharness/util/metrics.py:245-246
    if (the source predicate f in analyzed is truthy) {
      // Source: vvaharness/util/metrics.py:246-246
      In source order: Apply source augmented assignment loc_scan[lang] += loc with source evaluation/in-place semantics.
    }
  }
  // Source: vvaharness/util/metrics.py:248-257
  In source order: Evaluate once _elapsed_sec(start_ts, end_ts); assign in source target order to dur. Then Evaluate once TOKENS.snapshot(); assign in source target order to tok. Then Evaluate once tok['calls_with_usage'] > 0; assign in source target order to tok_avail. Then Evaluate once 0 if external_only else len(manifest.units); assign in source target order to chunks_attempted. Then Evaluate once ('completed', 'skipped', 'injected', 'confirmed') if external_input else ('completed', 'skipped'); assign in source target order to non_failures.
  // Source: vvaharness/util/metrics.py:258-262
  In source order: Evaluate once sum((1 for outcome in outcomes.values() if outcome not in non_failures)); assign in source target order to chunks_failed. Then Evaluate once COUNTERS.snapshot(); assign in source target order to counters. Then For counter_fields, assign {}; source annotation dict[str, object].
  // Source: vvaharness/util/metrics.py:264-266
  for each name in _INT_COUNTER_NAMES {
    // Source: vvaharness/util/metrics.py:265-266
    if (the source predicate name in counters is truthy) {
      // Source: vvaharness/util/metrics.py:266-266
      In source order: Evaluate once counters[name]; assign in source target order to counter_fields[name].
    }
  }
  // Source: vvaharness/util/metrics.py:269-270
  if (the source predicate 's2_degraded' in counters is truthy) {
    // Source: vvaharness/util/metrics.py:270-270
    In source order: Evaluate once bool(counters['s2_degraded']); assign in source target order to counter_fields['s2_degraded'].
  }
  // Source: vvaharness/util/metrics.py:273-276
  for each name in ('s2_baseline_undisposed', 's2_repo_kinds') {
    // Source: vvaharness/util/metrics.py:274-276
    if (the source predicate name in counters is truthy) {
      // Source: vvaharness/util/metrics.py:275-276
      In source order: Evaluate once counters[name]; assign in source target order to raw. Then Evaluate once raw.split(',') if raw else []; assign in source target order to counter_fields[name].
    }
  }
  // Source: vvaharness/util/metrics.py:278-324
  End this invocation with ScanMetrics(scan_id=source_template_279_16, module_name=repo_name, start_ts=start_ts, end_ts=end_ts, duration_sec=dur, total_files_in_scope=len(ctx.all_files), analyzed_files_unique=len(analyzed & set(ctx.all_files)), s3_unreachable_files=len(manifest.unreachable_files), s3_threats_without_unit=len(manifest.threats_without_unit_for(ctx.threat_model)), chunks_total=len(manifest.units), chunks_risk=n_risk, chunks_catchall=n_catch, chunks_specialist=n_spec, chunks_attempted=chunks_attempted, chunks_failed=chunks_failed, deepdive_skipped=external_only, errors_by_stage=errlog.counts_by_stage(), errors_log_path=str(errlog.current_path()) if errlog.current_path().exists() else '', loc_in_scope_by_language=dict(loc_scope), loc_scanned_by_language=dict(loc_scan), raw_findings_count=raw_findings, true_positive_count=true_pos, false_positive_count=false_pos, duplicate_count=duplicates, discovered_true_positive_count=discovered_tp, repeat_clone_true_positive_count=clone_tp, ev_rescued_count=ev_rescued, prompt_tokens=tok['prompt'] if tok_avail else None, completion_tokens=tok['completion'] if tok_avail else None, total_tokens=tok['total'] if tok_avail else None, tokens_by_phase=tok.get('by_phase') if tok_avail else None, reported_cost_usd=tok.get('usd'), priced_cost_usd=_priced_cost_usd(tok, role_models, pricing) if tok_avail else None, folders_scanned=folders, scope=scope, excluded=ctx.excluded or {}, chunks_by_kind=dict(kind_counts), **counter_fields).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/metrics.py:327-332
// Source signature: _loc(p: Path) -> int
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _loc(p) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/metrics.py:328-332
  Perform the following protected operations {
    // Source: vvaharness/util/metrics.py:329-330
    End this invocation with sum((1 for ln in p.open('r', encoding='utf-8', errors='replace') if ln.strip())).
  }
  // Source: vvaharness/util/metrics.py:331-332
  On the first matching source exception OSError, in handler order {
    // Source: vvaharness/util/metrics.py:332-332
    End this invocation with 0.
  }
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.lang.detect import EXT_TO_LANG` at source line 23: `source_detail/vvaharness/lang/detect.py.sudo.md`.
- `from vvaharness.models import ContextPackage, InvestigationUnit, ScanMetrics, ScopeEntry, TaskManifest` at source line 24: `source_detail/vvaharness/models/__init__.py.sudo.md`.
- `from vvaharness.util import errlog, stage_telemetry` at source line 31: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import errlog, stage_telemetry` at source line 31: `source_detail/vvaharness/util/errlog.py.sudo.md`.
- `from vvaharness.util import errlog, stage_telemetry` at source line 31: `source_detail/vvaharness/util/stage_telemetry.py.sudo.md`.
- `from vvaharness.util.counters import COUNTERS` at source line 32: `source_detail/vvaharness/util/counters.py.sudo.md`.
- `from vvaharness.util.pricing import PricingTable` at source line 33: `source_detail/vvaharness/util/pricing.py.sudo.md`.
- `from vvaharness.util.tokens import TOKENS` at source line 34: `source_detail/vvaharness/util/tokens.py.sudo.md`.
