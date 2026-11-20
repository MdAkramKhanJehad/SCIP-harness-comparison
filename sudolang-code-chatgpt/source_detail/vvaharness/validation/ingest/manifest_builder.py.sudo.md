# vvaharness/validation/ingest/manifest_builder.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/validation/ingest/manifest_builder.py.evidence.json`. SHA-256: `b064ba3774cb8b9efd0cedfc45408bb867e535b875627f33218c3b431baef030`.

```sudo
// Source: vvaharness/validation/ingest/manifest_builder.py:15-22
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from vvaharness.models import FindingCase; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.models import Manifest; preserve alias and import-time effects. Then Evaluate once ['build_manifest']; assign in source target order to __all__.
// Source: vvaharness/validation/ingest/manifest_builder.py:25-34
// Source signature: build_manifest(case: FindingCase, session_id: str) -> Manifest
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn build_manifest(case, session_id) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/ingest/manifest_builder.py:26-27
  In source order: Retain source documentation literal source_literal_26_4; it is not a model call. Then Evaluate once case.attempts[-1] if case.attempts else None; assign in source target order to latest.
  // Source: vvaharness/validation/ingest/manifest_builder.py:28-34
  End this invocation with Manifest(case_id=case.case_id, session_id=session_id, finding=case.finding, affected_files=list(latest.remediation.files_touched) if latest else [], post_results=False).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.models import FindingCase` at source line 19: `source_detail/vvaharness/models/__init__.py.sudo.md`.
- `from vvaharness.validation.models import Manifest` at source line 20: `source_detail/vvaharness/validation/models/__init__.py.sudo.md`.
