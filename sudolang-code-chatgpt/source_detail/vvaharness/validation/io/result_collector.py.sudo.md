# vvaharness/validation/io/result_collector.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/validation/io/result_collector.py.evidence.json`. SHA-256: `0a3b26b10ebeb7c8a704b4ca5c6a584b834b07b7d42a7cc6804761c694406f44`.

```sudo
// Source: vvaharness/validation/io/result_collector.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import json; preserve alias and import-time effects. Then Resolve source import from collections.abc import Mapping; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects.
// Source: vvaharness/validation/io/result_collector.py:22-30
In source order: Resolve source import from typing import NamedTuple; preserve alias and import-time effects. Then Resolve source import from vvaharness.models import Provenance, ScoringPolicy, Severity, Verdict; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import logs; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.constants.artifacts import MANIFEST_FILENAME, VALIDATION_REPORT_FILENAME; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.io._host_score import load_synthesized_gates, verdict_for; preserve alias and import-time effects.
// Source: vvaharness/validation/io/result_collector.py:31-46
In source order: Resolve source import from vvaharness.validation.models import Manifest, OutputFinding, ValidationReport, ValidationResult, gate_score_rows, render_row; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.scoring import FIX_CONFIG; preserve alias and import-time effects. Then Evaluate once logs.get_logger(__name__); assign in source target order to log. Then Evaluate once ['CollectedFinding', 'collect_and_enrich']; assign in source target order to __all__. Then Evaluate once 3; assign in source target order to _MIN_AFFECTED_FILE_LEN.
// Source: vvaharness/validation/io/result_collector.py:49-53
interface CollectedFinding {
  Describe the source Python type, preserving its base/metaclass expression order: NamedTuple.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/validation/io/result_collector.py:50-53
  In source order: Retain source documentation literal source_literal_50_4; it is not a model call. Then For verdict, declare without assigning a value; source annotation Verdict. Then For row, declare without assigning a value; source annotation ValidationResult.
}
// Source: vvaharness/validation/io/result_collector.py:56-75
// Source signature: _collect(workspace_dir: Path, finding_number_start: int, *, provenance: Provenance, policy: ScoringPolicy | None) -> list[CollectedFinding]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _collect(workspace_dir, finding_number_start, provenance, policy) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/io/result_collector.py:63-64
  In source order: Retain source documentation literal source_literal_63_4; it is not a model call. Then Evaluate once workspace_dir / VALIDATION_REPORT_FILENAME; assign in source target order to report_path.
  // Source: vvaharness/validation/io/result_collector.py:65-69
  Perform the following protected operations {
    // Source: vvaharness/validation/io/result_collector.py:66-66
    In source order: Evaluate once ValidationReport.from_file(report_path); assign in source target order to report.
  }
  // Source: vvaharness/validation/io/result_collector.py:67-69
  On the first matching source exception (OSError, ValueError), in handler order {
    // Source: vvaharness/validation/io/result_collector.py:68-68
    In source order: Evaluate log.warning('Could not read validation report at %s', report_path); retain side effects and discard the expression result.
    // Source: vvaharness/validation/io/result_collector.py:69-69
    End this invocation with [].
  }
  // Source: vvaharness/validation/io/result_collector.py:70-70
  In source order: Evaluate once load_synthesized_gates(workspace_dir); assign in source target order to gates_by_id.
  // Source: vvaharness/validation/io/result_collector.py:71-75
  End this invocation with [_one(finding, gates_by_id.get(finding.tracking_id), finding_number_start + index, provenance=provenance, policy=policy) for index, finding in enumerate(report.findings)].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/io/result_collector.py:78-98
// Source signature: _one(finding: OutputFinding, gates: list[Mapping[str, object]] | None, finding_number: int, *, provenance: Provenance, policy: ScoringPolicy | None) -> CollectedFinding
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _one(finding, gates, finding_number, provenance, policy) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/io/result_collector.py:86-88
  In source order: Retain source documentation literal source_literal_86_4; it is not a model call. Then Evaluate once verdict_for(finding, gates, provenance=provenance, policy=policy); assign in source target order to verdict. Then Evaluate once gate_score_rows(verdict, FIX_CONFIG); assign in source target order to rows.
  // Source: vvaharness/validation/io/result_collector.py:89-98
  End this invocation with CollectedFinding(verdict=verdict, row=render_row(verdict, finding, finding_number=finding_number, gate_scores_json=json.dumps(rows) if rows else '', policy=policy)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/io/result_collector.py:101-107
// Source signature: _filter_affected_files(affected: list[str]) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _filter_affected_files(affected) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/io/result_collector.py:102-106
  In source order: Retain source documentation literal source_literal_102_4; it is not a model call. Then Evaluate once [name for name in affected if not name.startswith('//') and len(name) > _MIN_AFFECTED_FILE_LEN]; assign in source target order to kept.
  // Source: vvaharness/validation/io/result_collector.py:107-107
  End this invocation with ', '.join(kept).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/io/result_collector.py:110-115
// Source signature: _load_manifest(workspace_dir: Path) -> Manifest | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _load_manifest(workspace_dir) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/io/result_collector.py:111-111
  In source order: Retain source documentation literal source_literal_111_4; it is not a model call.
  // Source: vvaharness/validation/io/result_collector.py:112-115
  Perform the following protected operations {
    // Source: vvaharness/validation/io/result_collector.py:113-113
    End this invocation with Manifest.from_file(workspace_dir / MANIFEST_FILENAME).
  }
  // Source: vvaharness/validation/io/result_collector.py:114-115
  On the first matching source exception (OSError, ValueError), in handler order {
    // Source: vvaharness/validation/io/result_collector.py:115-115
    End this invocation with None.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/io/result_collector.py:118-138
// Source signature: collect_and_enrich(workspace_dir: Path, finding_number_start: int=0, *, provenance: Provenance | None=None, policy: ScoringPolicy | None=None) -> list[CollectedFinding]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn collect_and_enrich(workspace_dir, finding_number_start, provenance, policy) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/io/result_collector.py:125-132
  In source order: Retain source documentation literal source_literal_125_4; it is not a model call. Then Evaluate once _collect(workspace_dir, finding_number_start, provenance=provenance or Provenance(), policy=policy); assign in source target order to collected. Then Evaluate once _load_manifest(workspace_dir); assign in source target order to manifest.
  // Source: vvaharness/validation/io/result_collector.py:133-134
  if (the source predicate not collected or manifest is None or manifest.finding is None is truthy) {
    // Source: vvaharness/validation/io/result_collector.py:134-134
    End this invocation with collected.
  }
  // Source: vvaharness/validation/io/result_collector.py:135-138
  End this invocation with [CollectedFinding(item.verdict, _enrich(item.row, manifest)) for item in collected].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/io/result_collector.py:141-172
// Source signature: _enrich(row: ValidationResult, manifest: Manifest) -> ValidationResult
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _enrich(row, manifest) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/io/result_collector.py:142-143
  In source order: Retain source documentation literal source_literal_142_4; it is not a model call. Then Evaluate once manifest.finding; assign in source target order to finding.
  // Source: vvaharness/validation/io/result_collector.py:144-145
  if (the source predicate finding is None is truthy) {
    // Source: vvaharness/validation/io/result_collector.py:145-145
    End this invocation with row.
  }
  // Source: vvaharness/validation/io/result_collector.py:147-171
  In source order: For fills, assign (('finding_title', finding.title, not row.finding_title), ('finding_description', finding.description.replace('\\n', ' ').strip(), not row.finding_description), ('affected_files', _filter_affected_files(manifest.affected_files), not row.affected_files), ('tracking_id', finding.case_id or manifest.case_id, not row.tracking_id or row.tracking_id == manifest.case_id), ('severity', finding.severity.value, row.severity.casefold() == Severity.MEDIUM.value)); source annotation tuple[tuple[str, str, bool], ...]. Then Evaluate once {name: value for name, value, absent in fills if absent and value}; assign in source target order to updates.
  // Source: vvaharness/validation/io/result_collector.py:172-172
  End this invocation with row.model_copy(update=updates) if updates else row.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.models import Provenance, ScoringPolicy, Severity, Verdict` at source line 24: `source_detail/vvaharness/models/__init__.py.sudo.md`.
- `from vvaharness.util import logs` at source line 25: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import logs` at source line 25: `source_detail/vvaharness/util/logs.py.sudo.md`.
- `from vvaharness.validation.constants.artifacts import MANIFEST_FILENAME, VALIDATION_REPORT_FILENAME` at source line 26: `source_detail/vvaharness/validation/constants/artifacts.py.sudo.md`.
- `from vvaharness.validation.io._host_score import load_synthesized_gates, verdict_for` at source line 30: `source_detail/vvaharness/validation/io/_host_score.py.sudo.md`.
- `from vvaharness.validation.models import Manifest, OutputFinding, ValidationReport, ValidationResult, gate_score_rows, render_row` at source line 31: `source_detail/vvaharness/validation/models/__init__.py.sudo.md`.
- `from vvaharness.validation.scoring import FIX_CONFIG` at source line 39: `source_detail/vvaharness/validation/scoring/__init__.py.sudo.md`.
