# vvaharness/remediation_agent/artifacts/report.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/remediation_agent/artifacts/report.py.evidence.json`. SHA-256: `e1962b0f5471307c4cdbd35cef03090fb6b58e823ba6e1726d7a20476a7a4e1b`.

```sudo
// Source: vvaharness/remediation_agent/artifacts/report.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from vvaharness.models import FindingCase, Remediation; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.target import RemediationTarget; preserve alias and import-time effects. Then Evaluate once ['build_report']; assign in source target order to __all__.
// Source: vvaharness/remediation_agent/artifacts/report.py:24-32
// Source signature: build_report(target: RemediationTarget, remediation: Remediation, *, reverted_paths: tuple[str, ...]=()) -> FindingCase
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn build_report(target, remediation, reverted_paths) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/artifacts/report.py:26-31
  In source order: Retain source documentation literal source_literal_26_4; it is not a model call. Then Evaluate once target.case_id; assign in source target order to case_id. Then Evaluate once target.finding if target.finding.case_id else target.finding.model_copy(update={'case_id': case_id}); assign in source target order to finding. Then Evaluate once FindingCase(case_id=case_id, finding=finding); assign in source target order to case.
  // Source: vvaharness/remediation_agent/artifacts/report.py:32-32
  End this invocation with case.with_attempt(remediation, reverted_paths=reverted_paths).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.models import FindingCase, Remediation` at source line 18: `source_detail/vvaharness/models/__init__.py.sudo.md`.
- `from vvaharness.remediation_agent.target import RemediationTarget` at source line 19: `source_detail/vvaharness/remediation_agent/target.py.sudo.md`.
