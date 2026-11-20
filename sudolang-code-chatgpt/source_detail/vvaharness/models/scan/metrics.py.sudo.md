# vvaharness/models/scan/metrics.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/models/scan/metrics.py.evidence.json`. SHA-256: `461dcbb57694773adbcad21c9db5eb9445f862d35182fa1a23de28e89a5d7f7d`.

```sudo
// Source: vvaharness/models/scan/metrics.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import logging; preserve alias and import-time effects. Then Resolve source import from typing import Literal; preserve alias and import-time effects. Then Resolve source import from pydantic import BaseModel; preserve alias and import-time effects.
// Source: vvaharness/models/scan/metrics.py:23-23
In source order: Evaluate once logging.getLogger(__name__); assign in source target order to log.
// Source: vvaharness/models/scan/metrics.py:25-29
interface ScopeEntry {
  Describe the source Python type, preserving its base/metaclass expression order: BaseModel.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/models/scan/metrics.py:26-29
  In source order: Retain source documentation literal source_literal_26_4; it is not a model call. Then For name, declare without assigning a value; source annotation str. Then For kind, declare without assigning a value; source annotation Literal['risk', 'catchall', 'specialist', 'taint', 'threat', 'other']. Then For files, declare without assigning a value; source annotation list[str].
}
// Source: vvaharness/models/scan/metrics.py:32-247
interface ScanMetrics {
  Describe the source Python type, preserving its base/metaclass expression order: BaseModel.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/models/scan/metrics.py:33-37
  In source order: Retain source documentation literal source_literal_33_4; it is not a model call. Then For scan_id, assign ''; source annotation str. Then For module_name, assign ''; source annotation str. Then For start_ts, assign ''; source annotation str. Then For end_ts, assign ''; source annotation str.
  // Source: vvaharness/models/scan/metrics.py:38-42
  In source order: For duration_sec, assign 0.0; source annotation float. Then For total_files_in_scope, assign 0; source annotation int. Then For analyzed_files_unique, assign 0; source annotation int. Then For chunks_total, assign 0; source annotation int. Then For chunks_risk, assign 0; source annotation int.
  // Source: vvaharness/models/scan/metrics.py:43-48
  In source order: For chunks_catchall, assign 0; source annotation int. Then For chunks_specialist, assign 0; source annotation int. Then For chunks_attempted, assign 0; source annotation int. Then For chunks_failed, assign 0; source annotation int. Then For deepdive_skipped, assign False; source annotation bool.
  // Source: vvaharness/models/scan/metrics.py:49-53
  In source order: For errors_by_stage, assign {}; source annotation dict[str, int]. Then For errors_log_path, assign ''; source annotation str. Then For loc_in_scope_by_language, assign {}; source annotation dict[str, int]. Then For loc_scanned_by_language, assign {}; source annotation dict[str, int]. Then For raw_findings_count, assign 0; source annotation int.
  // Source: vvaharness/models/scan/metrics.py:54-60
  In source order: For true_positive_count, assign 0; source annotation int. Then For false_positive_count, assign 0; source annotation int. Then For duplicate_count, assign 0; source annotation int. Then For discovered_true_positive_count, assign 0; source annotation int. Then For repeat_clone_true_positive_count, assign 0; source annotation int.
  // Source: vvaharness/models/scan/metrics.py:61-66
  In source order: For ev_rescued_count, assign 0; source annotation int. Then For prompt_tokens, assign None; source annotation int | None. Then For completion_tokens, assign None; source annotation int | None. Then For total_tokens, assign None; source annotation int | None. Then For tokens_by_phase, assign None; source annotation dict[str, dict] | None.
  // Source: vvaharness/models/scan/metrics.py:68-72
  In source order: For reported_cost_usd, assign None; source annotation float | None. Then For priced_cost_usd, assign None; source annotation float | None. Then For folders_scanned, assign []; source annotation list[str]. Then For scope, assign []; source annotation list[ScopeEntry]. Then For excluded, assign {}; source annotation dict.
  // Source: vvaharness/models/scan/metrics.py:75-80
  In source order: For s2_degraded, assign False; source annotation bool. Then For s2_threats_raw, assign 0; source annotation int. Then For s2_threats_truncated, assign 0; source annotation int. Then For s2_threats_promoted, assign 0; source annotation int. Then For s2_frontier_files_excluded, assign 0; source annotation int.
  // Source: vvaharness/models/scan/metrics.py:81-85
  In source order: For s2_frontier_entry_points_excluded, assign 0; source annotation int. Then For s2_frontier_sinks_excluded, assign 0; source annotation int. Then For s2_frontier_modules_excluded, assign 0; source annotation int. Then For s2_assets_truncated, assign 0; source annotation int. Then For s2_trust_boundaries_truncated, assign 0; source annotation int.
  // Source: vvaharness/models/scan/metrics.py:87-92
  In source order: For s2_prompt_modules_truncated, assign 0; source annotation int. Then For s2_prompt_entry_points_truncated, assign 0; source annotation int. Then For s2_inventory_files_truncated, assign 0; source annotation int. Then For s2_baseline_undisposed, assign []; source annotation list[str]. Then For s2_baseline_undisposed_recovered, assign 0; source annotation int.
  // Source: vvaharness/models/scan/metrics.py:93-99
  In source order: For s2_repo_kinds, assign []; source annotation list[str]. Then For s2_surface_files_dropped, assign 0; source annotation int. Then For s2_evidence_gate_rejected, assign 0; source annotation int. Then For s2_evidence_gate_rejected_relented, assign 0; source annotation int. Then For s3_unknown_file_ids, assign 0; source annotation int.
  // Source: vvaharness/models/scan/metrics.py:100-106
  In source order: For s3_dropped_paths, assign 0; source annotation int. Then For s3_relocated_paths, assign 0; source annotation int. Then For s3_unreachable_files, assign 0; source annotation int. Then For s3_threats_without_unit, assign 0; source annotation int. Then For s4_findings_truncated, assign 0; source annotation int.
  // Source: vvaharness/models/scan/metrics.py:108-115
  In source order: For s4_finding_extra_cwe_collapsed, assign 0; source annotation int. Then For s4_unit_key_deduped, assign 0; source annotation int. Then For s4_unit_no_outcome, assign 0; source annotation int. Then For s4_batch_member_uninvestigated, assign 0; source annotation int. Then For s4_batch_member_failed, assign 0; source annotation int.
  // Source: vvaharness/models/scan/metrics.py:117-123
  In source order: For s4_batch_member_resubmitted, assign 0; source annotation int. Then For s4_batch_member_recovered, assign 0; source annotation int. Then For s4_evidence_gate_rejected, assign 0; source annotation int. Then For s4_evidence_gate_rejected_relented, assign 0; source annotation int. Then For deepagents_oversize_prompts, assign 0; source annotation int.
  // Source: vvaharness/models/scan/metrics.py:125-133
  In source order: For deepagents_tool_state_not_roundtripped, assign 0; source annotation int. Then For deepagents_path_jail_refused, assign 0; source annotation int. Then For llm_truncated_replies, assign 0; source annotation int. Then For llm_truncated_below_budget, assign 0; source annotation int. Then For llm_adapter_evidence_gate_unenforced, assign 0; source annotation int.
  // Source: vvaharness/models/scan/metrics.py:134-141
  In source order: For cli_mcp_evidence_gate_unenforced, assign 0; source annotation int. Then For evidence_gate_stood_down_degenerate_graph, assign 0; source annotation int. Then For s6_evidence_gate_rejected, assign 0; source annotation int. Then For s6_evidence_gate_rejected_relented, assign 0; source annotation int. Then For llm_turn_cap_exhausted, assign 0; source annotation int.
  // Source: vvaharness/models/scan/metrics.py:143-149
  In source order: For llm_model_refusals, assign 0; source annotation int. Then For llm_refusal_retry_attempted, assign 0; source annotation int. Then For llm_refusal_retry_recovered, assign 0; source annotation int. Then For llm_truncated_retry_attempted, assign 0; source annotation int. Then For llm_truncated_retry_recovered, assign 0; source annotation int.
  // Source: vvaharness/models/scan/metrics.py:151-159
  In source order: For s6_confirmed_without_vector, assign 0; source annotation int. Then For s6_cvss_zero_impact_on_tp, assign 0; source annotation int. Then For s6_confidence_clamped, assign 0; source annotation int. Then For s6_confidence_uniform, assign 0; source annotation int. Then For s6_finding_line_correction_reverted_reanchor, assign 0; source annotation int.
  // Source: vvaharness/models/scan/metrics.py:161-167
  In source order: For s6_batch_structured_split, assign 0; source annotation int. Then For s6_batch_guardrail_split, assign 0; source annotation int. Then For s6_batch_generic_split, assign 0; source annotation int. Then For s6_structured_retry_attempted, assign 0; source annotation int. Then For s6_structured_retry_recovered, assign 0; source annotation int.
  // Source: vvaharness/models/scan/metrics.py:170-177
  In source order: For s6_truncated_retry_attempted, assign 0; source annotation int. Then For s6_truncated_retry_recovered, assign 0; source annotation int. Then For s6_replayed_fp_held, assign 0; source annotation int. Then For s6_fp_premise_contradicted, assign 0; source annotation int. Then For s6_replayed_tp_shipped, assign 0; source annotation int.
  // Source: vvaharness/models/scan/metrics.py:179-184
  In source order: For s6_outcome_members_resubmitted, assign 0; source annotation int. Then For s6_outcome_members_recovered, assign 0; source annotation int. Then For s2_orphan_settled, assign 0; source annotation int. Then For s4_orphan_settled, assign 0; source annotation int. Then For s6_orphan_settled, assign 0; source annotation int.
  // Source: vvaharness/models/scan/metrics.py:185-194
  In source order: For s8_orphan_settled, assign 0; source annotation int. Then For llm_structured_submit_rejected, assign 0; source annotation int. Then For llm_structured_prose_reask, assign 0; source annotation int. Then For s1_autoexclude_language_veto, assign 0; source annotation int. Then For sdk_tool_choice_dropped_for_thinking, assign 0; source annotation int.
  // Source: vvaharness/models/scan/metrics.py:197-203
  In source order: For deepagents_tool_choice_dropped, assign 0; source annotation int. Then For s1_truncated_retry_attempted, assign 0; source annotation int. Then For s1_truncated_retry_recovered, assign 0; source annotation int. Then For s2_structured_retry_attempted, assign 0; source annotation int. Then For s2_structured_retry_recovered, assign 0; source annotation int.
  // Source: vvaharness/models/scan/metrics.py:204-208
  In source order: For s2_truncated_retry_attempted, assign 0; source annotation int. Then For s2_truncated_retry_recovered, assign 0; source annotation int. Then For s4_structured_retry_attempted, assign 0; source annotation int. Then For s4_structured_retry_recovered, assign 0; source annotation int. Then For s4_truncated_retry_attempted, assign 0; source annotation int.
  // Source: vvaharness/models/scan/metrics.py:209-213
  In source order: For s4_truncated_retry_recovered, assign 0; source annotation int. Then For s7_structured_retry_attempted, assign 0; source annotation int. Then For s7_structured_retry_recovered, assign 0; source annotation int. Then For s7_truncated_retry_attempted, assign 0; source annotation int. Then For s7_truncated_retry_recovered, assign 0; source annotation int.
  // Source: vvaharness/models/scan/metrics.py:214-218
  In source order: For s8_structured_retry_attempted, assign 0; source annotation int. Then For s8_structured_retry_recovered, assign 0; source annotation int. Then For s8_truncated_retry_attempted, assign 0; source annotation int. Then For s8_truncated_retry_recovered, assign 0; source annotation int. Then For ev_classify_truncated_retry_attempted, assign 0; source annotation int.
  // Source: vvaharness/models/scan/metrics.py:219-226
  In source order: For ev_classify_truncated_retry_recovered, assign 0; source annotation int. Then For llm_structured_retry_truncated, assign 0; source annotation int. Then For s2_empty_retry_attempted, assign 0; source annotation int. Then For s2_empty_retry_recovered, assign 0; source annotation int. Then For s2_parse_repair_attempted, assign 0; source annotation int.
  // Source: vvaharness/models/scan/metrics.py:227-231
  In source order: For s2_parse_repair_recovered, assign 0; source annotation int. Then For s4_outcome_repaired_attempt, assign 0; source annotation int. Then For s4_outcome_repaired_ok, assign 0; source annotation int. Then For s4_batch_repaired_attempt, assign 0; source annotation int. Then For s4_batch_repaired_ok, assign 0; source annotation int.
  // Source: vvaharness/models/scan/metrics.py:232-240
  In source order: For s6_outcome_repaired_attempt, assign 0; source annotation int. Then For s6_outcome_repaired_ok, assign 0; source annotation int. Then For llm_call_timeouts, assign 0; source annotation int. Then For llm_call_budget_near, assign 0; source annotation int. Then For chunks_by_kind, assign {}; source annotation dict[str, int].
  // Source: vvaharness/models/scan/metrics.py:243-247
  // Source: vvaharness/models/scan/metrics.py:242-242
  Before creating this callable, evaluate and retain decorators top-to-bottom: property.
  // Source: vvaharness/models/scan/metrics.py:243-247
  // Source signature: coverage_pct(self) -> float
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn coverage_pct(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/models/scan/metrics.py:244-244
    In source order: Retain source documentation literal source_literal_244_8; it is not a model call.
    // Source: vvaharness/models/scan/metrics.py:245-246
    if (the source predicate not self.total_files_in_scope is truthy) {
      // Source: vvaharness/models/scan/metrics.py:246-246
      End this invocation with 0.0.
    }
    // Source: vvaharness/models/scan/metrics.py:247-247
    End this invocation with self.analyzed_files_unique / self.total_files_in_scope * 100.
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
}
```

## Local import links

No statically resolved in-checkout import; external calls remain explicit dependency boundaries.
