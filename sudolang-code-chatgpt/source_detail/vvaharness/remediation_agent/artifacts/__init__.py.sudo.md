# vvaharness/remediation_agent/artifacts/__init__.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/remediation_agent/artifacts/__init__.py.evidence.json`. SHA-256: `d2743a134b56b856bcb998ab019b1156579371f9445041128cd5a602864d834a`.

```sudo
// Source: vvaharness/remediation_agent/artifacts/__init__.py:15-34
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.artifacts.diff import _safe_repo_path, capture_git_diff, changed_files_whole_tree, changed_since_snapshot, derive_diff, snapshot_files, synth_unified_diff; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.artifacts.layout import DIFF_PATCH, EVIDENCE_DIR, FINDING_CASE_JSON, SUMMARY_MD, TRIAGE_JSON; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.artifacts.report import build_report; preserve alias and import-time effects.
// Source: vvaharness/remediation_agent/artifacts/__init__.py:35-54
In source order: Resolve source import from vvaharness.remediation_agent.artifacts.summary import render_summary; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.artifacts.writer import write_case; preserve alias and import-time effects. Then Evaluate once ['DIFF_PATCH', 'EVIDENCE_DIR', 'FINDING_CASE_JSON', 'SUMMARY_MD', 'TRIAGE_JSON', '_safe_repo_path', 'build_report', 'capture_git_diff', 'changed_files_whole_tree', 'changed_since_snapshot', 'derive_diff', 'render_summary', 'snapshot_files', 'synth_unified_diff', 'write_case']; assign in source target order to __all__.
```

## Local import links

- `from vvaharness.remediation_agent.artifacts.diff import _safe_repo_path, capture_git_diff, changed_files_whole_tree, changed_since_snapshot, derive_diff, snapshot_files, synth_unified_diff` at source line 18: `source_detail/vvaharness/remediation_agent/artifacts/diff/__init__.py.sudo.md`.
- `from vvaharness.remediation_agent.artifacts.layout import DIFF_PATCH, EVIDENCE_DIR, FINDING_CASE_JSON, SUMMARY_MD, TRIAGE_JSON` at source line 27: `source_detail/vvaharness/remediation_agent/artifacts/layout.py.sudo.md`.
- `from vvaharness.remediation_agent.artifacts.report import build_report` at source line 34: `source_detail/vvaharness/remediation_agent/artifacts/report.py.sudo.md`.
- `from vvaharness.remediation_agent.artifacts.summary import render_summary` at source line 35: `source_detail/vvaharness/remediation_agent/artifacts/summary.py.sudo.md`.
- `from vvaharness.remediation_agent.artifacts.writer import write_case` at source line 36: `source_detail/vvaharness/remediation_agent/artifacts/writer.py.sudo.md`.
