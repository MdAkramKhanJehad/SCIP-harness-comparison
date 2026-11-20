# vvaharness/remediation_agent/artifacts/diff/derive.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/remediation_agent/artifacts/diff/derive.py.evidence.json`. SHA-256: `cdb1e299bc1e0eb4268d49ad7f65c5feaab56fd913907d7971e5f62b596593cb`.

```sudo
// Source: vvaharness/remediation_agent/artifacts/diff/derive.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from collections.abc import Sequence; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.artifacts.diff.gitcapture import capture_git_diff; preserve alias and import-time effects.
// Source: vvaharness/remediation_agent/artifacts/diff/derive.py:22-24
In source order: Resolve source import from vvaharness.remediation_agent.artifacts.diff.synth import synth_unified_diff; preserve alias and import-time effects. Then Evaluate once ['derive_diff']; assign in source target order to __all__.
// Source: vvaharness/remediation_agent/artifacts/diff/derive.py:27-34
// Source signature: derive_diff(repo: Path, snapshot: dict[str, str | None] | None, changed: Sequence[str]) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn derive_diff(repo, snapshot, changed) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/artifacts/diff/derive.py:29-31
  In source order: Retain source documentation literal source_literal_29_4; it is not a model call. Then Evaluate once capture_git_diff(Path(repo), list(changed), baseline=snapshot); assign in source target order to diff.
  // Source: vvaharness/remediation_agent/artifacts/diff/derive.py:32-33
  if (the source predicate not diff and snapshot is not None is truthy) {
    // Source: vvaharness/remediation_agent/artifacts/diff/derive.py:33-33
    In source order: Evaluate once synth_unified_diff(Path(repo), snapshot, extra_files=list(changed)); assign in source target order to diff.
  }
  // Source: vvaharness/remediation_agent/artifacts/diff/derive.py:34-34
  End this invocation with diff or ''.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.remediation_agent.artifacts.diff.gitcapture import capture_git_diff` at source line 21: `source_detail/vvaharness/remediation_agent/artifacts/diff/gitcapture.py.sudo.md`.
- `from vvaharness.remediation_agent.artifacts.diff.synth import synth_unified_diff` at source line 22: `source_detail/vvaharness/remediation_agent/artifacts/diff/synth.py.sudo.md`.
