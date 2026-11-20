# vvaharness/models/scan/_sections_pipeline.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/models/scan/_sections_pipeline.py.evidence.json`. SHA-256: `b1ce43de7718c4ed93675707c391a6f7b052b405fef8a934778f3a48fc1444a0`.

```sudo
// Source: vvaharness/models/scan/_sections_pipeline.py:14-21
In source order: Retain source documentation literal source_literal_14_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import logging; preserve alias and import-time effects. Then Resolve source import from vvaharness.models.scan._render import _md_cell; preserve alias and import-time effects. Then Evaluate once logging.getLogger(__name__); assign in source target order to log.
// Source: vvaharness/models/scan/_sections_pipeline.py:25-28
In source order: Evaluate once [('risk', 'risk'), ('catchall', 'catch-all'), ('specialist', 'specialist'), ('taint', 'taint'), ('threat', 'threat'), ('other', 'other')]; assign in source target order to _CHUNK_KIND_LABELS.
// Source: vvaharness/models/scan/_sections_pipeline.py:30-42
// Source signature: _render_chunk_kind_line(report) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _render_chunk_kind_line(report) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/models/scan/_sections_pipeline.py:31-31
  In source order: Evaluate once report.metrics; assign in source target order to m.
  // Source: vvaharness/models/scan/_sections_pipeline.py:32-41
  if (the source predicate m.chunks_by_kind is truthy) {
    // Source: vvaharness/models/scan/_sections_pipeline.py:33-37
    In source order: Evaluate once dict(_CHUNK_KIND_LABELS); assign in source target order to known. Then Evaluate once [source_template_34_17 for key, label in _CHUNK_KIND_LABELS if key in m.chunks_by_kind]; assign in source target order to parts. Then Apply source augmented assignment parts += [source_template_36_18 for key, v in m.chunks_by_kind.items() if key not in known] with source evaluation/in-place semantics.
  }
  else {
    // Source: vvaharness/models/scan/_sections_pipeline.py:40-41
    In source order: Evaluate once [source_template_40_17, source_template_40_42, source_template_41_17]; assign in source target order to parts.
  }
  // Source: vvaharness/models/scan/_sections_pipeline.py:42-42
  End this invocation with source_template_42_11.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/models/scan/_sections_pipeline.py:46-47
In source order: Evaluate once ('s2', 's4', 's6', 's7', 's8'); assign in source target order to _STRUCTURED_RETRY_STAGES. Then Evaluate once ('s1', 's2', 's4', 's6', 's7', 's8', 'ev_classify'); assign in source target order to _TRUNCATED_RETRY_STAGES.
// Source: vvaharness/models/scan/_sections_pipeline.py:50-323
// Source signature: _render_pipeline_diagnostics(report, *, unreachable_appendix: bool=True) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _render_pipeline_diagnostics(report, unreachable_appendix) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/models/scan/_sections_pipeline.py:52-55
  In source order: Retain source documentation literal source_literal_52_4; it is not a model call. Then Evaluate once report.metrics; assign in source target order to m. Then For lines, assign []; source annotation list[str].
  // Source: vvaharness/models/scan/_sections_pipeline.py:57-62
  if (the source predicate m.s2_degraded is truthy) {
    // Source: vvaharness/models/scan/_sections_pipeline.py:58-62
    In source order: Evaluate lines.append(source_literal_59_12); retain side effects and discard the expression result.
  }
  // Source: vvaharness/models/scan/_sections_pipeline.py:63-64
  if (the source predicate m.s2_threats_raw is truthy) {
    // Source: vvaharness/models/scan/_sections_pipeline.py:64-64
    In source order: Evaluate lines.append(source_template_64_21); retain side effects and discard the expression result.
  }
  // Source: vvaharness/models/scan/_sections_pipeline.py:65-66
  if (the source predicate m.s2_threats_truncated is truthy) {
    // Source: vvaharness/models/scan/_sections_pipeline.py:66-66
    In source order: Evaluate lines.append(source_template_66_21); retain side effects and discard the expression result.
  }
  // Source: vvaharness/models/scan/_sections_pipeline.py:67-71
  if (the source predicate m.s2_threats_promoted is truthy) {
    // Source: vvaharness/models/scan/_sections_pipeline.py:68-71
    In source order: Evaluate lines.append(source_template_69_12); retain side effects and discard the expression result.
  }
  // Source: vvaharness/models/scan/_sections_pipeline.py:72-76
  In source order: Evaluate once [(label, n) for label, n in (('files', m.s2_frontier_files_excluded), ('entry points', m.s2_frontier_entry_points_excluded), ('sinks', m.s2_frontier_sinks_excluded), ('modules', m.s2_frontier_modules_excluded)) if n]; assign in source target order to frontier_cuts.
  // Source: vvaharness/models/scan/_sections_pipeline.py:77-81
  if (the source predicate frontier_cuts is truthy) {
    // Source: vvaharness/models/scan/_sections_pipeline.py:78-81
    In source order: Evaluate lines.append('- **Threat-model evidence excluded by step2 caps:** ' + ', '.join((source_template_80_24 for label, n in frontier_cuts))); retain side effects and discard the expression result.
  }
  // Source: vvaharness/models/scan/_sections_pipeline.py:82-85
  In source order: Evaluate once [(label, n) for label, n in (('inventory files', m.s2_inventory_files_truncated), ('entry points', m.s2_prompt_entry_points_truncated), ('modules', m.s2_prompt_modules_truncated)) if n]; assign in source target order to prompt_cuts.
  // Source: vvaharness/models/scan/_sections_pipeline.py:86-90
  if (the source predicate prompt_cuts is truthy) {
    // Source: vvaharness/models/scan/_sections_pipeline.py:87-90
    In source order: Evaluate lines.append('- **Threat-model prompt truncated by step2 caps:** ' + ', '.join((source_template_89_24 for label, n in prompt_cuts))); retain side effects and discard the expression result.
  }
  // Source: vvaharness/models/scan/_sections_pipeline.py:91-92
  if (the source predicate m.s2_assets_truncated is truthy) {
    // Source: vvaharness/models/scan/_sections_pipeline.py:92-92
    In source order: Evaluate lines.append(source_template_92_21); retain side effects and discard the expression result.
  }
  // Source: vvaharness/models/scan/_sections_pipeline.py:93-95
  if (the source predicate m.s2_trust_boundaries_truncated is truthy) {
    // Source: vvaharness/models/scan/_sections_pipeline.py:94-95
    In source order: Evaluate lines.append(source_template_94_21); retain side effects and discard the expression result.
  }
  // Source: vvaharness/models/scan/_sections_pipeline.py:96-100
  if (the source predicate m.s2_baseline_undisposed is truthy) {
    // Source: vvaharness/models/scan/_sections_pipeline.py:97-100
    In source order: Evaluate lines.append(source_template_98_12); retain side effects and discard the expression result.
  }
  // Source: vvaharness/models/scan/_sections_pipeline.py:101-102
  if (the source predicate m.s2_repo_kinds is truthy) {
    // Source: vvaharness/models/scan/_sections_pipeline.py:102-102
    In source order: Evaluate lines.append(source_template_102_21); retain side effects and discard the expression result.
  }
  // Source: vvaharness/models/scan/_sections_pipeline.py:103-107
  if (the source predicate m.s2_surface_files_dropped is truthy) {
    // Source: vvaharness/models/scan/_sections_pipeline.py:104-107
    In source order: Evaluate lines.append(source_template_105_12); retain side effects and discard the expression result.
  }
  // Source: vvaharness/models/scan/_sections_pipeline.py:109-113
  if (the source predicate m.s3_unknown_file_ids is truthy) {
    // Source: vvaharness/models/scan/_sections_pipeline.py:110-113
    In source order: Evaluate lines.append(source_template_111_12); retain side effects and discard the expression result.
  }
  // Source: vvaharness/models/scan/_sections_pipeline.py:114-115
  if (the source predicate m.s3_dropped_paths is truthy) {
    // Source: vvaharness/models/scan/_sections_pipeline.py:115-115
    In source order: Evaluate lines.append(source_template_115_21); retain side effects and discard the expression result.
  }
  // Source: vvaharness/models/scan/_sections_pipeline.py:116-122
  if (the source predicate m.s3_relocated_paths is truthy) {
    // Source: vvaharness/models/scan/_sections_pipeline.py:117-122
    In source order: Evaluate lines.append(source_template_118_12); retain side effects and discard the expression result.
  }
  // Source: vvaharness/models/scan/_sections_pipeline.py:123-133
  if (the source predicate m.s3_unreachable_files is truthy) {
    // Source: vvaharness/models/scan/_sections_pipeline.py:125-133
    In source order: Evaluate once 'they are listed in the appendix below' if unreachable_appendix and report.unreachable_files else 'set output.emit_unreachable_appendix: true to list them in the report'; assign in source target order to where. Then Evaluate lines.append(source_template_130_12); retain side effects and discard the expression result.
  }
  // Source: vvaharness/models/scan/_sections_pipeline.py:134-143
  if (the source predicate m.s3_threats_without_unit is truthy) {
    // Source: vvaharness/models/scan/_sections_pipeline.py:138-143
    In source order: Evaluate once report.threats_without_unit or []; assign in source target order to ids. Then Evaluate once source_template_139_17 if ids else ''; assign in source target order to listed. Then Evaluate lines.append(source_template_141_12); retain side effects and discard the expression result.
  }
  // Source: vvaharness/models/scan/_sections_pipeline.py:145-151
  if (the source predicate m.s4_findings_truncated is truthy) {
    // Source: vvaharness/models/scan/_sections_pipeline.py:146-151
    In source order: Evaluate lines.append(source_template_147_12); retain side effects and discard the expression result.
  }
  // Source: vvaharness/models/scan/_sections_pipeline.py:153-160
  if (the source predicate m.deepagents_oversize_prompts is truthy) {
    // Source: vvaharness/models/scan/_sections_pipeline.py:154-160
    In source order: Evaluate lines.append(source_template_155_12); retain side effects and discard the expression result.
  }
  // Source: vvaharness/models/scan/_sections_pipeline.py:162-176
  if (the source predicate m.llm_truncated_replies is truthy) {
    // Source: vvaharness/models/scan/_sections_pipeline.py:164-176
    In source order: Evaluate lines.append(source_template_165_12); retain side effects and discard the expression result.
  }
  // Source: vvaharness/models/scan/_sections_pipeline.py:178-188
  if (the source predicate m.llm_truncated_retry_attempted is truthy) {
    // Source: vvaharness/models/scan/_sections_pipeline.py:180-188
    In source order: Evaluate lines.append(source_template_181_12); retain side effects and discard the expression result.
  }
  // Source: vvaharness/models/scan/_sections_pipeline.py:190-197
  if (the source predicate m.deepagents_tool_state_not_roundtripped is truthy) {
    // Source: vvaharness/models/scan/_sections_pipeline.py:191-197
    In source order: Evaluate lines.append(source_template_192_12); retain side effects and discard the expression result.
  }
  // Source: vvaharness/models/scan/_sections_pipeline.py:200-213
  if (the source predicate m.llm_adapter_evidence_gate_unenforced is truthy) {
    // Source: vvaharness/models/scan/_sections_pipeline.py:201-213
    In source order: Evaluate lines.append(source_template_202_12); retain side effects and discard the expression result.
  }
  // Source: vvaharness/models/scan/_sections_pipeline.py:214-225
  if (the source predicate m.cli_mcp_evidence_gate_unenforced is truthy) {
    // Source: vvaharness/models/scan/_sections_pipeline.py:215-225
    In source order: Evaluate lines.append(source_template_216_12); retain side effects and discard the expression result.
  }
  // Source: vvaharness/models/scan/_sections_pipeline.py:227-239
  if (the source predicate m.s6_confirmed_without_vector is truthy) {
    // Source: vvaharness/models/scan/_sections_pipeline.py:228-239
    In source order: Evaluate lines.append(source_template_229_12); retain side effects and discard the expression result.
  }
  // Source: vvaharness/models/scan/_sections_pipeline.py:240-249
  if (the source predicate m.s6_cvss_zero_impact_on_tp is truthy) {
    // Source: vvaharness/models/scan/_sections_pipeline.py:241-249
    In source order: Evaluate lines.append(source_template_242_12); retain side effects and discard the expression result.
  }
  // Source: vvaharness/models/scan/_sections_pipeline.py:250-260
  if (the source predicate m.s6_confidence_clamped is truthy) {
    // Source: vvaharness/models/scan/_sections_pipeline.py:251-260
    In source order: Evaluate lines.append(source_template_252_12); retain side effects and discard the expression result.
  }
  // Source: vvaharness/models/scan/_sections_pipeline.py:261-270
  if (the source predicate m.s6_confidence_uniform is truthy) {
    // Source: vvaharness/models/scan/_sections_pipeline.py:262-270
    In source order: Evaluate lines.append(source_template_263_12); retain side effects and discard the expression result.
  }
  // Source: vvaharness/models/scan/_sections_pipeline.py:273-277
  In source order: Evaluate once sum((getattr(m, source_template_273_30) for s in _STRUCTURED_RETRY_STAGES)); assign in source target order to rejected. Then Evaluate once sum((getattr(m, source_template_274_33) for s in _STRUCTURED_RETRY_STAGES)); assign in source target order to rejected_ok. Then Evaluate once sum((getattr(m, source_template_276_29) for s in _TRUNCATED_RETRY_STAGES)); assign in source target order to clipped. Then Evaluate once sum((getattr(m, source_template_277_32) for s in _TRUNCATED_RETRY_STAGES)); assign in source target order to clipped_ok.
  // Source: vvaharness/models/scan/_sections_pipeline.py:278-303
  if (the source predicate rejected or clipped or m.s2_empty_retry_attempted is truthy) {
    // Source: vvaharness/models/scan/_sections_pipeline.py:281-303
    In source order: Evaluate once m.sdk_tool_choice_dropped_for_thinking + m.deepagents_tool_choice_dropped; assign in source target order to dropped. Then Evaluate lines.append(source_template_283_12 + (source_template_291_15 if m.llm_structured_retry_truncated else '') + (source_template_295_15 if m.s2_empty_retry_attempted else '') + (source_template_298_15 if dropped else '')); retain side effects and discard the expression result.
  }
  // Source: vvaharness/models/scan/_sections_pipeline.py:304-307
  In source order: Evaluate once m.s2_parse_repair_attempted + m.s4_outcome_repaired_attempt + m.s4_batch_repaired_attempt + m.s6_outcome_repaired_attempt; assign in source target order to repaired. Then Evaluate once m.s2_parse_repair_recovered + m.s4_outcome_repaired_ok + m.s4_batch_repaired_ok + m.s6_outcome_repaired_ok; assign in source target order to repaired_ok.
  // Source: vvaharness/models/scan/_sections_pipeline.py:308-319
  if (the source predicate repaired or m.llm_structured_prose_reask or m.llm_structured_submit_rejected is truthy) {
    // Source: vvaharness/models/scan/_sections_pipeline.py:309-319
    In source order: Evaluate lines.append(source_template_310_12); retain side effects and discard the expression result.
  }
  // Source: vvaharness/models/scan/_sections_pipeline.py:321-322
  if (the source predicate not lines is truthy) {
    // Source: vvaharness/models/scan/_sections_pipeline.py:322-322
    End this invocation with [].
  }
  // Source: vvaharness/models/scan/_sections_pipeline.py:323-323
  End this invocation with ['### Pipeline Diagnostics', '', *lines, ''].
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.models.scan._render import _md_cell` at source line 19: `source_detail/vvaharness/models/scan/_render.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../prompt_representation/vvaharness/models/scan/_sections_pipeline.py.sudo.md). Exact strings in the evidence asset support this conversion.
