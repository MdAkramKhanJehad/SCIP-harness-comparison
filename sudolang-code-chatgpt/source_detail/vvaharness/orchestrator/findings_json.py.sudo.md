# vvaharness/orchestrator/findings_json.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/orchestrator/findings_json.py.evidence.json`. SHA-256: `3cca38e021b049001d22f685a2e1097eb5275738f0ed47ddb3df741e30a2d521`.

```sudo
// Source: vvaharness/orchestrator/findings_json.py:15-22
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import json; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from pydantic import ValidationError; preserve alias and import-time effects.
// Source: vvaharness/orchestrator/findings_json.py:24-33
In source order: Resolve source import from vvaharness.models import FinalReport; preserve alias and import-time effects. Then Resolve source import from vvaharness.orchestrator.artifacts import FINDINGS_JSON_NAME, SCAN_DIR_NAME, artifact_dir; preserve alias and import-time effects. Then Resolve source import from vvaharness.report.redact import redact_tree; preserve alias and import-time effects. Then Evaluate once ['InvalidFindingsJSON', 'findings_json_path', 'read_findings_json', 'write_findings_json']; assign in source target order to __all__.
// Source: vvaharness/orchestrator/findings_json.py:36-37
interface InvalidFindingsJSON {
  Describe the source Python type, preserving its base/metaclass expression order: ValueError.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/orchestrator/findings_json.py:37-37
  In source order: Retain source documentation literal source_literal_37_4; it is not a model call.
}
// Source: vvaharness/orchestrator/findings_json.py:41-43
// Source signature: findings_json_path(repo: Path | str) -> Path
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn findings_json_path(repo) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/findings_json.py:42-42
  In source order: Retain source documentation literal source_literal_42_4; it is not a model call.
  // Source: vvaharness/orchestrator/findings_json.py:43-43
  End this invocation with Path(repo) / SCAN_DIR_NAME / FINDINGS_JSON_NAME.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/findings_json.py:46-55
// Source signature: write_findings_json(report: FinalReport, repo: Path | str) -> Path
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn write_findings_json(report, repo) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/findings_json.py:47-51
  In source order: Retain source documentation literal source_literal_47_4; it is not a model call. Then Evaluate once artifact_dir(repo, SCAN_DIR_NAME); assign in source target order to out_dir. Then Evaluate once out_dir / FINDINGS_JSON_NAME; assign in source target order to path. Then Evaluate out_dir.mkdir(parents=True, exist_ok=True); retain side effects and discard the expression result. Then Evaluate once json.dumps(redact_tree(report.model_dump(mode='json')), indent=2) + source_literal_51_82; assign in source target order to payload.
  // Source: vvaharness/orchestrator/findings_json.py:52-54
  In source order: Evaluate once path.with_suffix(source_template_52_27); assign in source target order to tmp. Then Evaluate tmp.write_text(payload, encoding='utf-8'); retain side effects and discard the expression result. Then Evaluate tmp.replace(path); retain side effects and discard the expression result.
  // Source: vvaharness/orchestrator/findings_json.py:55-55
  End this invocation with path.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/findings_json.py:58-64
// Source signature: read_findings_json(repo: Path | str) -> FinalReport | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn read_findings_json(repo) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/findings_json.py:59-61
  In source order: Retain source documentation literal source_literal_59_4; it is not a model call. Then Evaluate once findings_json_path(repo); assign in source target order to path.
  // Source: vvaharness/orchestrator/findings_json.py:62-63
  if (the source predicate not path.is_file() is truthy) {
    // Source: vvaharness/orchestrator/findings_json.py:63-63
    End this invocation with None.
  }
  // Source: vvaharness/orchestrator/findings_json.py:64-64
  End this invocation with _validated(path).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/findings_json.py:67-72
// Source signature: _validated(path: Path) -> FinalReport
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _validated(path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/findings_json.py:68-72
  Perform the following protected operations {
    // Source: vvaharness/orchestrator/findings_json.py:69-69
    End this invocation with FinalReport.model_validate_json(path.read_text(encoding='utf-8')).
  }
  // Source: vvaharness/orchestrator/findings_json.py:70-72
  On the first matching source exception (OSError, ValidationError, ValueError) as exc, in handler order {
    // Source: vvaharness/orchestrator/findings_json.py:71-72
    Raise InvalidFindingsJSON(source_template_72_12) with explicit source cause exc.
  }
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.models import FinalReport` at source line 24: `source_detail/vvaharness/models/__init__.py.sudo.md`.
- `from vvaharness.orchestrator.artifacts import FINDINGS_JSON_NAME, SCAN_DIR_NAME, artifact_dir` at source line 25: `source_detail/vvaharness/orchestrator/artifacts.py.sudo.md`.
- `from vvaharness.report.redact import redact_tree` at source line 30: `source_detail/vvaharness/report/redact.py.sudo.md`.
