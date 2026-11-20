# vvaharness/validation/models/results.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/validation/models/results.py.evidence.json`. SHA-256: `e669960ec812c6d746fab768badef40161efef831373d608d46026eea98b5c62`.

```sudo
// Source: vvaharness/validation/models/results.py:15-22
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from dataclasses import dataclass; preserve alias and import-time effects. Then Resolve source import from typing import TYPE_CHECKING; preserve alias and import-time effects. Then Resolve source import from pydantic import BaseModel, ConfigDict, Field; preserve alias and import-time effects.
// Source: vvaharness/validation/models/results.py:24-25
In source order: Resolve source import from vvaharness.models import Decision, MergeReadiness, Severity, merge_readiness_for; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.constants.scoring import SCORE_PRECISION; preserve alias and import-time effects.
// Source: vvaharness/validation/models/results.py:27-30
if (the source predicate TYPE_CHECKING is truthy) {
  // Source: vvaharness/validation/models/results.py:28-30
  In source order: Resolve source import from vvaharness.models import ScoringPolicy, Verdict; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.models.output import OutputFinding; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.models.scoring import ScoringConfig; preserve alias and import-time effects.
}
// Source: vvaharness/validation/models/results.py:32-44
In source order: Evaluate once ['RunMetadata', 'SarifLocation', 'ValidationResult', 'gate_score_rows', 'render_row', 'unverifiable_row']; assign in source target order to __all__. Then Evaluate once 'Yes'; assign in source target order to _YES. Then Evaluate once 'No'; assign in source target order to _NO. Then Evaluate once '?'; assign in source target order to _UNKNOWN.
// Source: vvaharness/validation/models/results.py:47-55
interface RunMetadata {
  Describe the source Python type, preserving its base/metaclass expression order: BaseModel.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/validation/models/results.py:48-54
  In source order: Retain source documentation literal source_literal_48_4; it is not a model call. Then Evaluate once ConfigDict(extra='forbid'); assign in source target order to model_config. Then For total_findings, assign 0; source annotation int. Then For findings_processed, assign 0; source annotation int. Then For findings_failed, assign 0; source annotation int.
  // Source: vvaharness/validation/models/results.py:55-55
  In source order: For errors, assign Field(default_factory=list); source annotation list[str].
}
// Source: vvaharness/validation/models/results.py:58-78
interface ValidationResult {
  Describe the source Python type, preserving its base/metaclass expression order: BaseModel.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/validation/models/results.py:59-65
  In source order: Retain source documentation literal source_literal_59_4; it is not a model call. Then Evaluate once ConfigDict(extra='forbid'); assign in source target order to model_config. Then For finding_number, declare without assigning a value; source annotation int. Then For tracking_id, declare without assigning a value; source annotation str. Then For finding_title, declare without assigning a value; source annotation str.
  // Source: vvaharness/validation/models/results.py:66-70
  In source order: For finding_description, declare without assigning a value; source annotation str. Then For affected_files, declare without assigning a value; source annotation str. Then For fixed, declare without assigning a value; source annotation str. Then For partially_fixed, declare without assigning a value; source annotation str. Then For not_fixed, declare without assigning a value; source annotation str.
  // Source: vvaharness/validation/models/results.py:71-75
  In source order: For files_needing_fixes, declare without assigning a value; source annotation str. Then For reason_for_decision, declare without assigning a value; source annotation str. Then For severity, declare without assigning a value; source annotation str. Then For pr_merge_readiness, declare without assigning a value; source annotation str. Then For recommendations, declare without assigning a value; source annotation str.
  // Source: vvaharness/validation/models/results.py:76-78
  In source order: For fix_confidence, assign 0.0; source annotation float. Then For gate_results_json, assign ''; source annotation str. Then For justification, assign ''; source annotation str.
}
// Source: vvaharness/validation/models/results.py:82-86
// Source: vvaharness/validation/models/results.py:81-81
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vvaharness/validation/models/results.py:82-86
interface SarifLocation {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/validation/models/results.py:83-86
  In source order: Retain source documentation literal source_literal_83_4; it is not a model call. Then For uri, declare without assigning a value; source annotation str. Then For start_line, declare without assigning a value; source annotation int.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vvaharness/validation/models/results.py:89-100
// Source signature: gate_score_rows(verdict: Verdict, config: ScoringConfig) -> dict[str, dict[str, object]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn gate_score_rows(verdict, config) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/models/results.py:90-91
  In source order: Retain source documentation literal source_literal_90_4; it is not a model call. Then For rows, assign {}; source annotation dict[str, dict[str, object]].
  // Source: vvaharness/validation/models/results.py:92-99
  for each gate in verdict.gates {
    // Source: vvaharness/validation/models/results.py:93-99
    In source order: Evaluate once config.weights.get(gate.name, 0.0); assign in source target order to weight. Then Evaluate once config.status_multiplier.get(gate.status.value, 0.0); assign in source target order to multiplier. Then Evaluate once {'status': gate.status.value, 'weight': weight, 'weighted_score': round(weight * multiplier, SCORE_PRECISION)}; assign in source target order to rows[gate.name].
  }
  // Source: vvaharness/validation/models/results.py:100-100
  End this invocation with rows.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/models/results.py:104-109
In source order: For _ANSWER_COLUMNS, assign {Decision.FIXED: (_YES, _NO, _NO), Decision.PARTIALLY_FIXED: (_NO, _YES, _NO), Decision.NOT_FIXED: (_NO, _NO, _YES), Decision.INCONCLUSIVE: (_UNKNOWN, _UNKNOWN, _UNKNOWN)}; source annotation dict[Decision, tuple[str, str, str]].
// Source: vvaharness/validation/models/results.py:112-140
// Source signature: render_row(verdict: Verdict, output_finding: OutputFinding, *, finding_number: int, gate_scores_json: str='', policy: ScoringPolicy | None=None) -> ValidationResult
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn render_row(verdict, output_finding, finding_number, gate_scores_json, policy) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/models/results.py:120-122
  In source order: Retain source documentation literal source_literal_120_4; it is not a model call. Then Evaluate once _ANSWER_COLUMNS[verdict.decision]; assign in source target order to (fixed, partially, not_fixed). Then Evaluate once verdict.score if verdict.score is not None else 0.0; assign in source target order to score.
  // Source: vvaharness/validation/models/results.py:123-140
  End this invocation with ValidationResult(finding_number=finding_number, tracking_id=output_finding.tracking_id, finding_title=output_finding.finding_title, finding_description=output_finding.finding_description, affected_files=output_finding.affected_files, fixed=fixed, partially_fixed=partially, not_fixed=not_fixed, files_needing_fixes=_files_needing_fixes(output_finding), reason_for_decision=source_template_133_28, severity=output_finding.severity, pr_merge_readiness=merge_readiness_for(verdict, policy).value, recommendations='; '.join(verdict.recommendations), fix_confidence=score, gate_results_json=gate_scores_json, justification=verdict.rationale).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/models/results.py:143-147
// Source signature: _files_needing_fixes(output_finding: OutputFinding) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _files_needing_fixes(output_finding) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/models/results.py:144-144
  In source order: Retain source documentation literal source_literal_144_4; it is not a model call.
  // Source: vvaharness/validation/models/results.py:145-146
  if (the source predicate output_finding.conditions_for_full_fix is truthy) {
    // Source: vvaharness/validation/models/results.py:146-146
    End this invocation with '; '.join(output_finding.conditions_for_full_fix).
  }
  // Source: vvaharness/validation/models/results.py:147-147
  End this invocation with output_finding.files_needing_fixes.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/models/results.py:150-169
// Source signature: unverifiable_row(tracking_id: str, title: str, reason: str, finding_number: int=0) -> ValidationResult
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn unverifiable_row(tracking_id, title, reason, finding_number) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/models/results.py:153-153
  In source order: Retain source documentation literal source_literal_153_4; it is not a model call.
  // Source: vvaharness/validation/models/results.py:154-169
  End this invocation with ValidationResult(finding_number=finding_number, tracking_id=tracking_id, finding_title=title, finding_description='', affected_files='', fixed=_UNKNOWN, partially_fixed=_UNKNOWN, not_fixed=_UNKNOWN, files_needing_fixes='', reason_for_decision=source_template_164_28, severity=Severity.MEDIUM.value, pr_merge_readiness=MergeReadiness.NOT_READY.value, recommendations=source_template_168_24).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.models import Decision, MergeReadiness, Severity, merge_readiness_for` at source line 24: `source_detail/vvaharness/models/__init__.py.sudo.md`.
- `from vvaharness.validation.constants.scoring import SCORE_PRECISION` at source line 25: `source_detail/vvaharness/validation/constants/scoring.py.sudo.md`.
- `from vvaharness.models import ScoringPolicy, Verdict` at source line 28: `source_detail/vvaharness/models/__init__.py.sudo.md`.
- `from vvaharness.validation.models.output import OutputFinding` at source line 29: `source_detail/vvaharness/validation/models/output.py.sudo.md`.
- `from vvaharness.validation.models.scoring import ScoringConfig` at source line 30: `source_detail/vvaharness/validation/models/scoring.py.sudo.md`.
