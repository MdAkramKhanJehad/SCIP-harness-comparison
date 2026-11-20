# vvaharness/pipeline/stages/s9/health.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/pipeline/stages/s9/health.py.evidence.json`. SHA-256: `aef0e43411badabed26a382028e76c19ae57cfdf634542400535b1ee08a47f22`.

```sudo
// Source: vvaharness/pipeline/stages/s9/health.py:16-19
In source order: Retain source documentation literal source_literal_16_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from vvaharness.models import FinalReport; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s9/health.py:22-51
// Source signature: scan_health(report: FinalReport) -> dict
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn scan_health(report) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s9/health.py:23-26
  In source order: Retain source documentation literal source_literal_23_4; it is not a model call. Then Evaluate once report.metrics; assign in source target order to m. Then Evaluate once bool(m is not None and (not m.total_files_in_scope)); assign in source target order to empty_scope. Then Evaluate once report.coverage_degraded(); assign in source target order to coverage_degraded_reasons.
  // Source: vvaharness/pipeline/stages/s9/health.py:27-51
  End this invocation with {'executionSuccessful': not empty_scope, 'hollow': report.is_hollow(), 'degraded': report.degraded, 'degraded_reason': report.degraded_reason, 'enrichment_unavailable': report.enrichment_unavailable, 'coverage_degraded': bool(coverage_degraded_reasons), 'coverage_degraded_reasons': list(coverage_degraded_reasons), 'chunks_failed': m.chunks_failed if m else 0, 'deepdive_skipped': m.deepdive_skipped if m else False, 'errors_by_stage': m.errors_by_stage if m else {}, 'threats_total': len(report.threat_model.threats) if report.threat_model else 0, 'threats_without_unit': None if report.threats_without_unit is None else list(report.threats_without_unit), 'threats_before_cap': m.s2_threats_raw if m else 0, 'threats_truncated': m.s2_threats_truncated if m else 0, 'threats_promoted': m.s2_threats_promoted if m else 0}.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.models import FinalReport` at source line 19: `source_detail/vvaharness/models/__init__.py.sudo.md`.
