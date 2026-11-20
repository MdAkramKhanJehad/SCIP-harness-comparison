# vvaharness/models/scan/_sections_metrics.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/models/scan/_sections_metrics.py.evidence.json`. SHA-256: `621a68650076fcc621022f4cace5cc30d3528525a5e5d33773e8b49138aee99f`.

```sudo
// Source: vvaharness/models/scan/_sections_metrics.py:14-19
In source order: Retain source documentation literal source_literal_14_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import logging; preserve alias and import-time effects. Then Resolve source import from collections import Counter; preserve alias and import-time effects. Then Resolve source import from typing import TYPE_CHECKING; preserve alias and import-time effects.
// Source: vvaharness/models/scan/_sections_metrics.py:21-28
In source order: Resolve source import from vvaharness.models.scan._finding_section import _EV_POSITIVE_ONLY_NOTE; preserve alias and import-time effects. Then Resolve source import from vvaharness.models.scan._render import _md_cell; preserve alias and import-time effects. Then Resolve source import from vvaharness.models.scan._sections_pipeline import _render_chunk_kind_line, _render_pipeline_diagnostics; preserve alias and import-time effects.
// Source: vvaharness/models/scan/_sections_metrics.py:30-32
if (the source predicate TYPE_CHECKING is truthy) {
  // Source: vvaharness/models/scan/_sections_metrics.py:31-32
  In source order: Resolve source import from vvaharness.models.scan.metrics import ScanMetrics; preserve alias and import-time effects. Then Resolve source import from vvaharness.models.scan.report import FinalReport; preserve alias and import-time effects.
}
// Source: vvaharness/models/scan/_sections_metrics.py:34-34
In source order: Evaluate once logging.getLogger(__name__); assign in source target order to log.
// Source: vvaharness/models/scan/_sections_metrics.py:37-95
// Source signature: _render_metrics(report, *, unreachable_appendix: bool=True) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _render_metrics(report, unreachable_appendix) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/models/scan/_sections_metrics.py:38-55
  In source order: Evaluate once report.metrics; assign in source target order to m. Then Evaluate once ['## Scan Metrics', '', source_template_42_8, source_template_43_8, source_template_44_8, source_template_45_8, source_template_46_8, source_template_47_8, source_template_48_8, source_template_49_8, _render_chunk_kind_line(report), source_template_51_8, source_template_52_8, source_template_53_8, '']; assign in source target order to lines.
  // Source: vvaharness/models/scan/_sections_metrics.py:56-57
  if (the source predicate m.folders_scanned is truthy) {
    // Source: vvaharness/models/scan/_sections_metrics.py:57-57
    In source order: Evaluate lines.append(source_template_57_21); retain side effects and discard the expression result.
  }
  // Source: vvaharness/models/scan/_sections_metrics.py:58-59
  In source order: Evaluate lines.extend(_render_pipeline_diagnostics(report, unreachable_appendix=unreachable_appendix)); retain side effects and discard the expression result.
  // Source: vvaharness/models/scan/_sections_metrics.py:60-82
  if (the source predicate m.tokens_by_phase is truthy) {
    // Source: vvaharness/models/scan/_sections_metrics.py:61-71
    In source order: Evaluate lines.extend(['### Tokens by Phase', '', '_Prompt = fresh + cache-write (billable). Cache-read shown separately, NOT included in totals._', '', '| Phase | Calls | Prompt | Completion | Total | % | Cache-read (excl.) |', '|---|---:|---:|---:|---:|---:|---:|']); retain side effects and discard the expression result. Then Evaluate once sum((b['prompt'] + b['completion'] for b in m.tokens_by_phase.values())) or 1; assign in source target order to grand.
    // Source: vvaharness/models/scan/_sections_metrics.py:72-81
    for each (ph, b) in sorted(m.tokens_by_phase.items(), key=lambda kv: -(kv[1]['prompt'] + kv[1]['completion'])) {
      // Source: vvaharness/models/scan/_sections_metrics.py:74-81
      In source order: Evaluate once 'unscoped (outside stage wrapper)' if ph in {'unlabeled', 'unscoped'} else ph; assign in source target order to phase_label. Then Evaluate once b['prompt'] + b['completion']; assign in source target order to tot. Then Evaluate lines.append(source_template_79_16); retain side effects and discard the expression result.
    }
    // Source: vvaharness/models/scan/_sections_metrics.py:82-82
    In source order: Evaluate lines.append(''); retain side effects and discard the expression result.
  }
  // Source: vvaharness/models/scan/_sections_metrics.py:83-94
  if (the source predicate m.loc_in_scope_by_language is truthy) {
    // Source: vvaharness/models/scan/_sections_metrics.py:84-89
    In source order: Evaluate lines.extend(['### Language LOC Coverage', '', '| Language | LOC in scope | LOC scanned | Coverage % |', '|---|---:|---:|---:|']); retain side effects and discard the expression result.
    // Source: vvaharness/models/scan/_sections_metrics.py:90-93
    for each (lang, loc_in) in sorted(m.loc_in_scope_by_language.items()) {
      // Source: vvaharness/models/scan/_sections_metrics.py:91-93
      In source order: Evaluate once m.loc_scanned_by_language.get(lang, 0); assign in source target order to loc_sc. Then Evaluate once loc_sc / loc_in * 100 if loc_in else 0.0; assign in source target order to pct. Then Evaluate lines.append(source_template_93_25); retain side effects and discard the expression result.
    }
    // Source: vvaharness/models/scan/_sections_metrics.py:94-94
    In source order: Evaluate lines.append(''); retain side effects and discard the expression result.
  }
  // Source: vvaharness/models/scan/_sections_metrics.py:95-95
  End this invocation with lines.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/models/scan/_sections_metrics.py:97-153
// Source signature: _render_verification(report: FinalReport, *, posture_channel: bool=True) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _render_verification(report, posture_channel) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/models/scan/_sections_metrics.py:98-104
  In source order: Retain source documentation literal source_literal_98_4; it is not a model call. Then Evaluate once report.dropped; assign in source target order to drops. Then Evaluate once Counter((d.reason for d in drops)); assign in source target order to by_reason. Then Evaluate once (by_reason['FALSE_POSITIVE'], by_reason['UNCONFIRMED'], by_reason['DUPLICATE']); assign in source target order to (fp, unc, dup). Then Evaluate once report._undetermined_drop_count(); assign in source target order to verr.
  // Source: vvaharness/models/scan/_sections_metrics.py:108-117
  In source order: Evaluate once sum((1 for d in drops if d.reason != 'DUPLICATE' and d.chunk_id.endswith('+s6'))); assign in source target order to reverify_dropped. Then Evaluate once sum((1 for d in drops if d.reason == 'DUPLICATE' and d.canonical_idx is None)); assign in source target order to dup_pre. Then Evaluate once report._verified_tp_fp(); assign in source target order to (verified_tp, verified_fp). Then Evaluate once verified_tp + verified_fp; assign in source target order to _tp_plus_fp. Then Evaluate once source_template_116_12 if _tp_plus_fp else 'n/a (no TRUE_POSITIVE/FALSE_POSITIVE verdicts)'; assign in source target order to rate.
  // Source: vvaharness/models/scan/_sections_metrics.py:118-125
  In source order: Evaluate once report.metrics; assign in source target order to m. Then Evaluate once m.discovered_true_positive_count if m else 0; assign in source target order to discovered. Then Evaluate once m.repeat_clone_true_positive_count if m else 0; assign in source target order to clones. Then Evaluate once sum((1 for rf in report.findings if rf.finding.channel == 'posture')) if posture_channel else 0; assign in source target order to n_posture. Then Evaluate once source_template_124_13 if n_posture else ''; assign in source target order to split.
  // Source: vvaharness/models/scan/_sections_metrics.py:126-131
  In source order: Evaluate once ['## Verification', source_template_128_8, source_template_129_9]; assign in source target order to out.
  // Source: vvaharness/models/scan/_sections_metrics.py:132-135
  if (the source predicate discovered + clones is truthy) {
    // Source: vvaharness/models/scan/_sections_metrics.py:134-135
    In source order: Evaluate out.append(source_template_134_19); retain side effects and discard the expression result.
  }
  // Source: vvaharness/models/scan/_sections_metrics.py:136-140
  In source order: Evaluate out.extend([source_template_137_8, source_template_138_8, source_template_139_8]); retain side effects and discard the expression result.
  // Source: vvaharness/models/scan/_sections_metrics.py:141-143
  if (the source predicate reverify_dropped is truthy) {
    // Source: vvaharness/models/scan/_sections_metrics.py:142-143
    In source order: Evaluate out.append(source_template_142_19); retain side effects and discard the expression result.
  }
  // Source: vvaharness/models/scan/_sections_metrics.py:144-152
  In source order: Evaluate out.extend([source_template_145_9, source_template_147_8, source_literal_148_9]); retain side effects and discard the expression result. Then Evaluate out.extend(_ev_lines(report)); retain side effects and discard the expression result.
  // Source: vvaharness/models/scan/_sections_metrics.py:153-153
  End this invocation with out.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/models/scan/_sections_metrics.py:156-180
// Source signature: _ev_lines(report: FinalReport) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _ev_lines(report) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/models/scan/_sections_metrics.py:157-162
  In source order: Retain source documentation literal source_literal_157_4; it is not a model call. Then Evaluate once [rf.finding.ev_status for rf in report.findings]; assign in source target order to _ev. Then Evaluate once _ev.count('CONFIRMED'); assign in source target order to ev_confirmed. Then Evaluate once _ev.count('NOT_CONFIRMED'); assign in source target order to ev_not. Then Evaluate once _ev.count('INCONCLUSIVE'); assign in source target order to ev_inconc.
  // Source: vvaharness/models/scan/_sections_metrics.py:163-164
  In source order: Evaluate once ev_confirmed + ev_not + ev_inconc; assign in source target order to ev_tested. Then For out, assign []; source annotation list[str].
  // Source: vvaharness/models/scan/_sections_metrics.py:165-171
  if (the source predicate ev_tested is truthy) {
    // Source: vvaharness/models/scan/_sections_metrics.py:166-171
    In source order: Evaluate once [source_template_167_13, source_template_170_12]; assign in source target order to out.
  }
  // Source: vvaharness/models/scan/_sections_metrics.py:175-176
  In source order: Evaluate once report.metrics; assign in source target order to m. Then Evaluate once m.ev_rescued_count if m else 0; assign in source target order to rescued.
  // Source: vvaharness/models/scan/_sections_metrics.py:177-179
  if (the source predicate rescued is truthy) {
    // Source: vvaharness/models/scan/_sections_metrics.py:178-179
    In source order: Evaluate out.append(source_template_178_19); retain side effects and discard the expression result.
  }
  // Source: vvaharness/models/scan/_sections_metrics.py:180-180
  End this invocation with out.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/models/scan/_sections_metrics.py:184-188
In source order: For _RELENT_STAGES, assign (('s2', 'S2 threat model'), ('s4', 'S4 deep-dive'), ('s6', 'S6 verification')); source annotation tuple[tuple[str, str], ...].
// Source: vvaharness/models/scan/_sections_metrics.py:191-206
// Source signature: _relent_lines(m: ScanMetrics | None) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _relent_lines(m) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/models/scan/_sections_metrics.py:192-192
  In source order: Retain source documentation literal source_literal_192_4; it is not a model call.
  // Source: vvaharness/models/scan/_sections_metrics.py:193-194
  if (the source predicate m is None is truthy) {
    // Source: vvaharness/models/scan/_sections_metrics.py:194-194
    End this invocation with [].
  }
  // Source: vvaharness/models/scan/_sections_metrics.py:195-195
  In source order: For out, assign []; source annotation list[str].
  // Source: vvaharness/models/scan/_sections_metrics.py:196-205
  for each (prefix, label) in _RELENT_STAGES {
    // Source: vvaharness/models/scan/_sections_metrics.py:197-197
    In source order: Evaluate once getattr(m, source_template_197_30, 0); assign in source target order to relented.
    // Source: vvaharness/models/scan/_sections_metrics.py:198-199
    if (the source predicate not relented is truthy) {
      // Source: vvaharness/models/scan/_sections_metrics.py:199-199
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/models/scan/_sections_metrics.py:200-205
    In source order: Evaluate once getattr(m, source_template_200_30, 0); assign in source target order to rejected. Then Evaluate out.append(source_template_202_12); retain side effects and discard the expression result.
  }
  // Source: vvaharness/models/scan/_sections_metrics.py:206-206
  End this invocation with out.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/models/scan/_sections_metrics.py:209-220
// Source signature: _unranked_lines(report: FinalReport) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _unranked_lines(report) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/models/scan/_sections_metrics.py:210-212
  In source order: Retain source documentation literal source_literal_210_4; it is not a model call. Then Evaluate once report.unranked_split(); assign in source target order to (ranked, by_design, feeder_missed). Then Evaluate once ranked + by_design + feeder_missed; assign in source target order to total.
  // Source: vvaharness/models/scan/_sections_metrics.py:213-214
  if (the source predicate not (by_design or feeder_missed) is truthy) {
    // Source: vvaharness/models/scan/_sections_metrics.py:214-214
    End this invocation with [].
  }
  // Source: vvaharness/models/scan/_sections_metrics.py:215-215
  In source order: Evaluate once source_template_215_11; assign in source target order to line.
  // Source: vvaharness/models/scan/_sections_metrics.py:216-217
  if (the source predicate by_design is truthy) {
    // Source: vvaharness/models/scan/_sections_metrics.py:217-217
    In source order: Apply source augmented assignment line += source_template_217_16 with source evaluation/in-place semantics.
  }
  // Source: vvaharness/models/scan/_sections_metrics.py:218-219
  if (the source predicate feeder_missed is truthy) {
    // Source: vvaharness/models/scan/_sections_metrics.py:219-219
    In source order: Apply source augmented assignment line += source_template_219_16 with source evaluation/in-place semantics.
  }
  // Source: vvaharness/models/scan/_sections_metrics.py:220-220
  End this invocation with [line + '.'].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/models/scan/_sections_metrics.py:223-268
// Source signature: _render_scan_health(report) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _render_scan_health(report) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/models/scan/_sections_metrics.py:224-228
  In source order: Retain source documentation literal source_literal_224_4; it is not a model call. Then Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Evaluate once report.metrics; assign in source target order to m. Then For lines, assign []; source annotation list[str]. Then Evaluate once getattr(report, 'degraded', False); assign in source target order to degraded.
  // Source: vvaharness/models/scan/_sections_metrics.py:229-233
  In source order: Evaluate once m.chunks_failed if m else 0; assign in source target order to failed. Then Evaluate once (m.errors_by_stage if m else {}) or {}; assign in source target order to errs. Then Evaluate once report.is_hollow(); assign in source target order to hollow. Then Evaluate once report.coverage_degraded(); assign in source target order to coverage. Then Evaluate once _relent_lines(m); assign in source target order to relents.
  // Source: vvaharness/models/scan/_sections_metrics.py:234-234
  In source order: Evaluate once _unranked_lines(report); assign in source target order to unranked.
  // Source: vvaharness/models/scan/_sections_metrics.py:235-237
  if (the source predicate not (degraded or failed or errs or hollow or coverage or relents or unranked or (m and m.deepdive_skipped)) is truthy) {
    // Source: vvaharness/models/scan/_sections_metrics.py:237-237
    End this invocation with lines.
  }
  // Source: vvaharness/models/scan/_sections_metrics.py:238-238
  In source order: Evaluate lines.extend(['## Scan Health', '']); retain side effects and discard the expression result.
  // Source: vvaharness/models/scan/_sections_metrics.py:239-241
  if (the source predicate m and m.deepdive_skipped is truthy) {
    // Source: vvaharness/models/scan/_sections_metrics.py:240-241
    In source order: Evaluate lines.append(source_literal_240_21); retain side effects and discard the expression result.
  }
  // Source: vvaharness/models/scan/_sections_metrics.py:242-247
  if (the source predicate hollow is truthy) {
    // Source: vvaharness/models/scan/_sections_metrics.py:243-247
    In source order: Evaluate lines.append(source_literal_244_12); retain side effects and discard the expression result.
  }
  // Source: vvaharness/models/scan/_sections_metrics.py:248-248
  In source order: Evaluate lines.extend(_coverage_degraded_lines(report, coverage)); retain side effects and discard the expression result.
  // Source: vvaharness/models/scan/_sections_metrics.py:249-252
  if (the source predicate degraded is truthy) {
    // Source: vvaharness/models/scan/_sections_metrics.py:251-252
    In source order: Evaluate once getattr(report, 'degraded_reason', '') or '(no reason recorded)'; assign in source target order to reason. Then Evaluate lines.append(source_template_252_21); retain side effects and discard the expression result.
  }
  // Source: vvaharness/models/scan/_sections_metrics.py:253-258
  if (the source predicate failed is truthy) {
    // Source: vvaharness/models/scan/_sections_metrics.py:254-258
    In source order: Evaluate once m.chunks_attempted or m.chunks_total if m else 0; assign in source target order to attempted. Then Evaluate lines.append(source_template_255_21); retain side effects and discard the expression result.
  }
  // Source: vvaharness/models/scan/_sections_metrics.py:259-262
  if (the source predicate errs is truthy) {
    // Source: vvaharness/models/scan/_sections_metrics.py:260-262
    In source order: Evaluate once ', '.join((source_template_260_24 for s, n in sorted(errs.items()))); assign in source target order to brk. Then Evaluate lines.append(source_template_262_21); retain side effects and discard the expression result.
  }
  // Source: vvaharness/models/scan/_sections_metrics.py:263-264
  In source order: Evaluate lines.extend(relents); retain side effects and discard the expression result. Then Evaluate lines.extend(unranked); retain side effects and discard the expression result.
  // Source: vvaharness/models/scan/_sections_metrics.py:265-266
  if (the source predicate m and m.errors_log_path is truthy) {
    // Source: vvaharness/models/scan/_sections_metrics.py:266-266
    In source order: Evaluate lines.append(source_template_266_21); retain side effects and discard the expression result.
  }
  // Source: vvaharness/models/scan/_sections_metrics.py:267-267
  In source order: Evaluate lines.append(''); retain side effects and discard the expression result.
  // Source: vvaharness/models/scan/_sections_metrics.py:268-268
  End this invocation with lines.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/models/scan/_sections_metrics.py:270-306
// Source signature: _coverage_degraded_lines(report, reasons: tuple[str, ...]) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _coverage_degraded_lines(report, reasons) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/models/scan/_sections_metrics.py:271-273
  In source order: Retain source documentation literal source_literal_271_4; it is not a model call. Then Evaluate once report.metrics; assign in source target order to m. Then For out, assign []; source annotation list[str].
  // Source: vvaharness/models/scan/_sections_metrics.py:274-282
  if (the source predicate 's6_undetermined' in reasons is truthy) {
    // Source: vvaharness/models/scan/_sections_metrics.py:276-282
    In source order: Evaluate once report._undetermined_drop_count(); assign in source target order to n. Then Evaluate once report._verified_tp_fp(); assign in source target order to (tp, fp). Then Evaluate once n + tp + fp; assign in source target order to total. Then Evaluate out.append(source_template_280_12); retain side effects and discard the expression result.
  }
  // Source: vvaharness/models/scan/_sections_metrics.py:283-297
  if (the source predicate 'zero_analysis' in reasons is truthy) {
    // Source: vvaharness/models/scan/_sections_metrics.py:285-290
    In source order: Evaluate once all((rf.finding.origin == 'detector' for rf in report.findings)); assign in source target order to _all_detector. Then Evaluate once 'from a deterministic detector, not a reviewed analysis' if _all_detector else "from detectors and the verifier's re-verify wave, not a reviewed analysis"; assign in source target order to _source.
    // Source: vvaharness/models/scan/_sections_metrics.py:291-292
    if (the source predicate m.deepdive_skipped is truthy) {
      // Source: vvaharness/models/scan/_sections_metrics.py:292-292
      In source order: Evaluate once 'from external input and downstream processing, not S4 deep-dive analysis'; assign in source target order to _source.
    }
    // Source: vvaharness/models/scan/_sections_metrics.py:293-297
    In source order: Evaluate out.append(source_template_294_12); retain side effects and discard the expression result.
  }
  // Source: vvaharness/models/scan/_sections_metrics.py:298-305
  if (the source predicate 'llm_turn_cap_exhausted' in reasons is truthy) {
    // Source: vvaharness/models/scan/_sections_metrics.py:299-305
    In source order: Evaluate out.append(source_template_300_12); retain side effects and discard the expression result.
  }
  // Source: vvaharness/models/scan/_sections_metrics.py:306-306
  End this invocation with out.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/models/scan/_sections_metrics.py:308-404
// Source signature: _render_scope_appendix(report) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _render_scope_appendix(report) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/models/scan/_sections_metrics.py:309-310
  In source order: Evaluate once report.metrics; assign in source target order to m. Then Evaluate once ['', '---', '', '## Appendix: Scan Scope', '']; assign in source target order to out.
  // Source: vvaharness/models/scan/_sections_metrics.py:312-318
  if (the source predicate m.folders_scanned is truthy) {
    // Source: vvaharness/models/scan/_sections_metrics.py:313-314
    In source order: Evaluate out.append(source_template_313_19); retain side effects and discard the expression result. Then Evaluate out.append(''); retain side effects and discard the expression result.
    // Source: vvaharness/models/scan/_sections_metrics.py:316-317
    for each d in m.folders_scanned {
      // Source: vvaharness/models/scan/_sections_metrics.py:317-317
      In source order: Evaluate out.append(source_template_317_23); retain side effects and discard the expression result.
    }
    // Source: vvaharness/models/scan/_sections_metrics.py:318-318
    In source order: Evaluate out.append(''); retain side effects and discard the expression result.
  }
  // Source: vvaharness/models/scan/_sections_metrics.py:320-321
  In source order: Evaluate once m.excluded or {}; assign in source target order to ex. Then Evaluate once (ex.get('config_dedup') or {}).get('dropped') or 0; assign in source target order to dd_dropped.
  // Source: vvaharness/models/scan/_sections_metrics.py:322-402
  if (the source predicate dd_dropped or any((ex.get(k) for k in ('dirs', 'exts', 'globs', 'oversize', 'symlinks', 'symlink_targets'))) is truthy) {
    // Source: vvaharness/models/scan/_sections_metrics.py:325-333
    In source order: Evaluate once sum((ex.get('dirs') or {}).values()) + sum((ex.get('exts') or {}).values()) + sum((ex.get('globs') or {}).values()) + (ex.get('oversize') or 0) + sum((ex.get('symlinks') or {}).values()) + sum((ex.get('symlink_targets') or {}).values()) + dd_dropped; assign in source target order to n_total. Then Evaluate out.append(source_template_332_19); retain side effects and discard the expression result. Then Evaluate out.append(''); retain side effects and discard the expression result.
    // Source: vvaharness/models/scan/_sections_metrics.py:334-340
    if (the source predicate ex.get('dirs') is truthy) {
      // Source: vvaharness/models/scan/_sections_metrics.py:335-336
      In source order: Evaluate out.append('**Folders** (matched `exclude_dirs`):'); retain side effects and discard the expression result. Then Evaluate out.append(''); retain side effects and discard the expression result.
      // Source: vvaharness/models/scan/_sections_metrics.py:337-339
      for each (d, n) in sorted(ex['dirs'].items(), key=lambda kv: -kv[1]) {
        // Source: vvaharness/models/scan/_sections_metrics.py:338-339
        In source order: Evaluate out.append(source_template_338_27); retain side effects and discard the expression result.
      }
      // Source: vvaharness/models/scan/_sections_metrics.py:340-340
      In source order: Evaluate out.append(''); retain side effects and discard the expression result.
    }
    // Source: vvaharness/models/scan/_sections_metrics.py:341-347
    if (the source predicate ex.get('exts') is truthy) {
      // Source: vvaharness/models/scan/_sections_metrics.py:342-343
      In source order: Evaluate out.append('**File types** (matched `exclude_exts`):'); retain side effects and discard the expression result. Then Evaluate out.append(''); retain side effects and discard the expression result.
      // Source: vvaharness/models/scan/_sections_metrics.py:344-346
      for each (e, n) in sorted(ex['exts'].items(), key=lambda kv: -kv[1]) {
        // Source: vvaharness/models/scan/_sections_metrics.py:345-346
        In source order: Evaluate out.append(source_template_345_27); retain side effects and discard the expression result.
      }
      // Source: vvaharness/models/scan/_sections_metrics.py:347-347
      In source order: Evaluate out.append(''); retain side effects and discard the expression result.
    }
    // Source: vvaharness/models/scan/_sections_metrics.py:348-354
    if (the source predicate ex.get('globs') is truthy) {
      // Source: vvaharness/models/scan/_sections_metrics.py:349-350
      In source order: Evaluate out.append('**Patterns** (matched `exclude_globs`):'); retain side effects and discard the expression result. Then Evaluate out.append(''); retain side effects and discard the expression result.
      // Source: vvaharness/models/scan/_sections_metrics.py:351-353
      for each (g, n) in sorted(ex['globs'].items(), key=lambda kv: -kv[1]) {
        // Source: vvaharness/models/scan/_sections_metrics.py:352-353
        In source order: Evaluate out.append(source_template_352_27); retain side effects and discard the expression result.
      }
      // Source: vvaharness/models/scan/_sections_metrics.py:354-354
      In source order: Evaluate out.append(''); retain side effects and discard the expression result.
    }
    // Source: vvaharness/models/scan/_sections_metrics.py:355-362
    if (the source predicate ex.get('oversize') is truthy) {
      // Source: vvaharness/models/scan/_sections_metrics.py:356-357
      In source order: Evaluate out.append(source_template_356_23); retain side effects and discard the expression result. Then Evaluate out.append(''); retain side effects and discard the expression result.
      // Source: vvaharness/models/scan/_sections_metrics.py:358-360
      for each (path, sz) in ex.get('oversize_files') or [] {
        // Source: vvaharness/models/scan/_sections_metrics.py:359-360
        In source order: Evaluate out.append(source_template_359_27); retain side effects and discard the expression result.
      }
      // Source: vvaharness/models/scan/_sections_metrics.py:361-362
      if (the source predicate ex.get('oversize_files') is truthy) {
        // Source: vvaharness/models/scan/_sections_metrics.py:362-362
        In source order: Evaluate out.append(''); retain side effects and discard the expression result.
      }
    }
    // Source: vvaharness/models/scan/_sections_metrics.py:363-371
    if (the source predicate ex.get('symlinks') is truthy) {
      // Source: vvaharness/models/scan/_sections_metrics.py:364-366
      In source order: Evaluate out.append('**Symlinks** (target resolves outside the repo — not followed):'); retain side effects and discard the expression result. Then Evaluate out.append(''); retain side effects and discard the expression result.
      // Source: vvaharness/models/scan/_sections_metrics.py:367-370
      for each (path, n) in sorted(ex['symlinks'].items(), key=lambda kv: -kv[1]) {
        // Source: vvaharness/models/scan/_sections_metrics.py:369-370
        In source order: Evaluate out.append(source_template_369_27 + (source_template_370_30 if n != 1 else '')); retain side effects and discard the expression result.
      }
      // Source: vvaharness/models/scan/_sections_metrics.py:371-371
      In source order: Evaluate out.append(''); retain side effects and discard the expression result.
    }
    // Source: vvaharness/models/scan/_sections_metrics.py:372-377
    if (the source predicate ex.get('symlink_targets') is truthy) {
      // Source: vvaharness/models/scan/_sections_metrics.py:373-377
      In source order: Evaluate out.append('**Symlinks** (target is excluded from scope):'); retain side effects and discard the expression result. Then Evaluate out.append(''); retain side effects and discard the expression result. Then Evaluate out.extend((source_template_375_23 for path in sorted(ex['symlink_targets']))); retain side effects and discard the expression result. Then Evaluate out.append(''); retain side effects and discard the expression result.
    }
    // Source: vvaharness/models/scan/_sections_metrics.py:378-378
    In source order: Evaluate once ex.get('config_dedup') or {}; assign in source target order to dd.
    // Source: vvaharness/models/scan/_sections_metrics.py:379-402
    if (the source predicate dd.get('dropped') is truthy) {
      // Source: vvaharness/models/scan/_sections_metrics.py:380-386
      In source order: Evaluate out.append(source_template_381_16); retain side effects and discard the expression result. Then Evaluate out.append(''); retain side effects and discard the expression result.
      // Source: vvaharness/models/scan/_sections_metrics.py:387-391
      for each c in dd.get('top_clusters') or [] {
        // Source: vvaharness/models/scan/_sections_metrics.py:388-391
        In source order: Evaluate out.append(source_template_389_20); retain side effects and discard the expression result.
      }
      // Source: vvaharness/models/scan/_sections_metrics.py:392-401
      if (the source predicate dd.get('promoted_files') is truthy) {
        // Source: vvaharness/models/scan/_sections_metrics.py:393-396
        In source order: Evaluate out.append(''); retain side effects and discard the expression result. Then Evaluate out.append('Promoted (suspicious value not present in cluster representative):'); retain side effects and discard the expression result. Then Evaluate out.append(''); retain side effects and discard the expression result.
        // Source: vvaharness/models/scan/_sections_metrics.py:398-401
        for each (p, why) in dd['promoted_files'] {
          // Source: vvaharness/models/scan/_sections_metrics.py:399-401
          In source order: Evaluate out.append(source_template_400_24); retain side effects and discard the expression result.
        }
      }
      // Source: vvaharness/models/scan/_sections_metrics.py:402-402
      In source order: Evaluate out.append(''); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/models/scan/_sections_metrics.py:404-404
  End this invocation with out.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.models.scan._finding_section import _EV_POSITIVE_ONLY_NOTE` at source line 21: `source_detail/vvaharness/models/scan/_finding_section.py.sudo.md`.
- `from vvaharness.models.scan._render import _md_cell` at source line 22: `source_detail/vvaharness/models/scan/_render.py.sudo.md`.
- `from vvaharness.models.scan._sections_pipeline import _render_chunk_kind_line, _render_pipeline_diagnostics` at source line 25: `source_detail/vvaharness/models/scan/_sections_pipeline.py.sudo.md`.
- `from vvaharness.models.scan.metrics import ScanMetrics` at source line 31: `source_detail/vvaharness/models/scan/metrics.py.sudo.md`.
- `from vvaharness.models.scan.report import FinalReport` at source line 32: `source_detail/vvaharness/models/scan/report.py.sudo.md`.
