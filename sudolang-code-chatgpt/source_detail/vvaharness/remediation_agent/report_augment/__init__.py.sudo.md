# vvaharness/remediation_agent/report_augment/__init__.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/remediation_agent/report_augment/__init__.py.evidence.json`. SHA-256: `a9ff7cba57113144047c00fae4c522fb45cbcf12772b47628b4c8e46c53a435c`.

```sudo
// Source: vvaharness/remediation_agent/report_augment/__init__.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from vvaharness.orchestrator.artifacts import artifact_dir; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.report_augment.dto import _load_cases; preserve alias and import-time effects.
// Source: vvaharness/remediation_agent/report_augment/__init__.py:22-32
In source order: Resolve source import from vvaharness.remediation_agent.report_augment.locate import _ensure_combined, _locate_scan_report; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.report_augment.markdown import _augment_md; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.report_augment.sarif import _augment_sarif; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.report_parser import REMEDIATION_DIR_NAME, SCAN_DIR_NAME; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import logs; preserve alias and import-time effects.
// Source: vvaharness/remediation_agent/report_augment/__init__.py:34-36
In source order: Evaluate once logs.get_logger(__name__); assign in source target order to log. Then Evaluate once ['augment_reports']; assign in source target order to __all__.
// Source: vvaharness/remediation_agent/report_augment/__init__.py:39-45
// Source signature: augment_reports(repo: Path, report_md: Path | str | None=None) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn augment_reports(repo, report_md) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/report_augment/__init__.py:40-40
  In source order: Retain source documentation literal source_literal_40_4; it is not a model call.
  // Source: vvaharness/remediation_agent/report_augment/__init__.py:41-45
  Perform the following protected operations {
    // Source: vvaharness/remediation_agent/report_augment/__init__.py:42-42
    In source order: Evaluate _augment(Path(repo), Path(report_md) if report_md else None); retain side effects and discard the expression result.
  }
  // Source: vvaharness/remediation_agent/report_augment/__init__.py:43-45
  On the first matching source exception Exception, in handler order {
    // Source: vvaharness/remediation_agent/report_augment/__init__.py:44-45
    In source order: Evaluate log.exception('remediation report augmentation failed; results not written to combined report'); retain side effects and discard the expression result.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/report_augment/__init__.py:48-66
// Source signature: _augment(repo: Path, report_md: Path | None=None) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _augment(repo, report_md) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/report_augment/__init__.py:49-53
  In source order: Retain source documentation literal source_literal_49_4; it is not a model call. Then Evaluate once artifact_dir(repo, REMEDIATION_DIR_NAME); assign in source target order to rem_dir. Then Evaluate once _load_cases(rem_dir) if rem_dir.is_dir() else []; assign in source target order to records.
  // Source: vvaharness/remediation_agent/report_augment/__init__.py:54-56
  if (the source predicate not records is truthy) {
    // Source: vvaharness/remediation_agent/report_augment/__init__.py:55-55
    In source order: Evaluate log.info('no remediation cases under %s — skipping report augmentation', rem_dir); retain side effects and discard the expression result.
    // Source: vvaharness/remediation_agent/report_augment/__init__.py:56-56
    End this invocation with None.
  }
  // Source: vvaharness/remediation_agent/report_augment/__init__.py:58-58
  In source order: Evaluate once _locate_scan_report(repo, report_md); assign in source target order to located.
  // Source: vvaharness/remediation_agent/report_augment/__init__.py:59-62
  if (the source predicate located is None is truthy) {
    // Source: vvaharness/remediation_agent/report_augment/__init__.py:60-61
    In source order: Evaluate log.warning('no scan report under %s/%s — skipping report augmentation', repo, SCAN_DIR_NAME); retain side effects and discard the expression result.
    // Source: vvaharness/remediation_agent/report_augment/__init__.py:62-62
    End this invocation with None.
  }
  // Source: vvaharness/remediation_agent/report_augment/__init__.py:63-66
  In source order: Evaluate once _ensure_combined(repo, *located); assign in source target order to (sarif_dst, md_dst). Then Evaluate once _augment_sarif(sarif_dst, records); assign in source target order to ordinal_matches. Then Evaluate _augment_md(md_dst, records, ordinal_matches=ordinal_matches); retain side effects and discard the expression result. Then Evaluate log.info('remediation results written to combined report under %s', sarif_dst.parent); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.orchestrator.artifacts import artifact_dir` at source line 20: `source_detail/vvaharness/orchestrator/artifacts.py.sudo.md`.
- `from vvaharness.remediation_agent.report_augment.dto import _load_cases` at source line 21: `source_detail/vvaharness/remediation_agent/report_augment/dto.py.sudo.md`.
- `from vvaharness.remediation_agent.report_augment.locate import _ensure_combined, _locate_scan_report` at source line 22: `source_detail/vvaharness/remediation_agent/report_augment/locate.py.sudo.md`.
- `from vvaharness.remediation_agent.report_augment.markdown import _augment_md` at source line 26: `source_detail/vvaharness/remediation_agent/report_augment/markdown.py.sudo.md`.
- `from vvaharness.remediation_agent.report_augment.sarif import _augment_sarif` at source line 27: `source_detail/vvaharness/remediation_agent/report_augment/sarif.py.sudo.md`.
- `from vvaharness.remediation_agent.report_parser import REMEDIATION_DIR_NAME, SCAN_DIR_NAME` at source line 28: `source_detail/vvaharness/remediation_agent/report_parser/__init__.py.sudo.md`.
- `from vvaharness.util import logs` at source line 32: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import logs` at source line 32: `source_detail/vvaharness/util/logs.py.sudo.md`.
