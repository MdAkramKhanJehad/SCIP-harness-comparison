# vvaharness/remediation_agent/artifacts/diff/__init__.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/remediation_agent/artifacts/diff/__init__.py.evidence.json`. SHA-256: `205377f2519da01df1101bf3b8afe4e0aed47ac9dfdd3971657e8518a5ee3617`.

```sudo
// Source: vvaharness/remediation_agent/artifacts/diff/__init__.py:15-26
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.artifacts.diff.derive import derive_diff; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.artifacts.diff.gitcapture import capture_git_diff, changed_files_whole_tree; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.artifacts.diff.paths import _norm_path, _safe_repo_path; preserve alias and import-time effects.
// Source: vvaharness/remediation_agent/artifacts/diff/__init__.py:27-46
In source order: Resolve source import from vvaharness.remediation_agent.artifacts.diff.snapshot import changed_since_snapshot, snapshot_files; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.artifacts.diff.synth import SYNTH_HEADER, synth_unified_diff; preserve alias and import-time effects. Then Evaluate once ['SYNTH_HEADER', '_norm_path', '_safe_repo_path', 'capture_git_diff', 'changed_files_whole_tree', 'changed_since_snapshot', 'derive_diff', 'snapshot_files', 'synth_unified_diff']; assign in source target order to __all__.
```

## Local import links

- `from vvaharness.remediation_agent.artifacts.diff.derive import derive_diff` at source line 18: `source_detail/vvaharness/remediation_agent/artifacts/diff/derive.py.sudo.md`.
- `from vvaharness.remediation_agent.artifacts.diff.gitcapture import capture_git_diff, changed_files_whole_tree` at source line 19: `source_detail/vvaharness/remediation_agent/artifacts/diff/gitcapture.py.sudo.md`.
- `from vvaharness.remediation_agent.artifacts.diff.paths import _norm_path, _safe_repo_path` at source line 23: `source_detail/vvaharness/remediation_agent/artifacts/diff/paths.py.sudo.md`.
- `from vvaharness.remediation_agent.artifacts.diff.snapshot import changed_since_snapshot, snapshot_files` at source line 27: `source_detail/vvaharness/remediation_agent/artifacts/diff/snapshot.py.sudo.md`.
- `from vvaharness.remediation_agent.artifacts.diff.synth import SYNTH_HEADER, synth_unified_diff` at source line 31: `source_detail/vvaharness/remediation_agent/artifacts/diff/synth.py.sudo.md`.
