# vvaharness/remediation_agent/report_augment/summary.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/remediation_agent/report_augment/summary.py.evidence.json`. SHA-256: `94644768eb1d7f354d37b7264d94a692832ad84774da7725509bd7ebfe672b2c`.

```sudo
// Source: vvaharness/remediation_agent/report_augment/summary.py:15-18
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.report_augment.dto import REMEDIATED, CaseRecord; preserve alias and import-time effects.
// Source: vvaharness/remediation_agent/report_augment/summary.py:21-30
// Source signature: _summary_counts(records: list[CaseRecord]) -> dict[str, int]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _summary_counts(records) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/report_augment/summary.py:22-25
  In source order: Retain source documentation literal source_literal_22_4; it is not a model call. Then Evaluate once len(records); assign in source target order to total. Then Evaluate once sum((1 for r in records if r.false_positive)); assign in source target order to false_positive. Then Evaluate once sum((1 for r in records if r.bucket == REMEDIATED)); assign in source target order to remediated.
  // Source: vvaharness/remediation_agent/report_augment/summary.py:26-30
  End this invocation with {'true_positive': total - false_positive, 'in_scope': total, 'remediated': remediated}.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/report_augment/summary.py:33-48
// Source signature: _md_summary_section(records: list[CaseRecord]) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _md_summary_section(records) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/report_augment/summary.py:34-38
  In source order: Retain source documentation literal source_literal_34_4; it is not a model call. Then Evaluate once _summary_counts(records); assign in source target order to c. Then Evaluate once c['true_positive']; assign in source target order to true_positive. Then Evaluate once c['in_scope']; assign in source target order to in_scope. Then Evaluate once c['remediated']; assign in source target order to remediated.
  // Source: vvaharness/remediation_agent/report_augment/summary.py:41-41
  In source order: Evaluate once source_template_41_11 if true_positive > 0 else 'n/a'; assign in source target order to rate.
  // Source: vvaharness/remediation_agent/report_augment/summary.py:42-48
  End this invocation with source_template_43_8.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.remediation_agent.report_augment.dto import REMEDIATED, CaseRecord` at source line 18: `source_detail/vvaharness/remediation_agent/report_augment/dto.py.sudo.md`.
