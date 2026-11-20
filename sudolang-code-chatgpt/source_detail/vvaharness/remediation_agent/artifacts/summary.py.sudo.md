# vvaharness/remediation_agent/artifacts/summary.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/remediation_agent/artifacts/summary.py.evidence.json`. SHA-256: `25a393636b5a28aec63a645d83f361243082c3eef4c923ef4371ec79f5c2aac6`.

```sudo
// Source: vvaharness/remediation_agent/artifacts/summary.py:15-18
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.models import RemediationVerdict; preserve alias and import-time effects.
// Source: vvaharness/remediation_agent/artifacts/summary.py:21-44
// Source signature: render_summary(verdict: RemediationVerdict, *, meta: dict) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn render_summary(verdict, meta) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/artifacts/summary.py:22-28
  In source order: Retain source documentation literal source_literal_22_4; it is not a model call. Then Evaluate once source_literal_23_14.join((source_template_24_8 for c in verdict.changes)) or '- (none reported)'; assign in source target order to changes. Then Evaluate once source_literal_26_11.join((source_template_26_21 for r in verdict.recommendations)) or '- (none)'; assign in source target order to recs. Then Evaluate once source_literal_27_12.join((source_template_27_22 for r in verdict.remaining_risks)) or '- (none)'; assign in source target order to risks. Then Evaluate once verdict.gates; assign in source target order to g.
  // Source: vvaharness/remediation_agent/artifacts/summary.py:29-44
  End this invocation with source_template_30_8.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.remediation_agent.models import RemediationVerdict` at source line 18: `source_detail/vvaharness/remediation_agent/models/__init__.py.sudo.md`.
