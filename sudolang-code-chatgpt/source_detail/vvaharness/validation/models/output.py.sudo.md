# vvaharness/validation/models/output.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/validation/models/output.py.evidence.json`. SHA-256: `f5b18e3b0e62acecd8859158e8dcc9670131dc45082c78cf67138757cdeebf5e`.

```sudo
// Source: vvaharness/validation/models/output.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import json; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from typing import Final, Literal; preserve alias and import-time effects.
// Source: vvaharness/validation/models/output.py:23-43
In source order: Resolve source import from pydantic import BaseModel, ConfigDict, Field, ValidationInfo, field_validator, model_validator; preserve alias and import-time effects. Then Resolve source import from vvaharness.models import Decision, EvidenceAnchor, GateAssessment, GateStatus, Provenance, Verdict; preserve alias and import-time effects. Then Resolve source import from vvaharness.report.redact import redact; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import logs; preserve alias and import-time effects. Then Evaluate once logs.get_logger(__name__); assign in source target order to log.
// Source: vvaharness/validation/models/output.py:45-60
In source order: Evaluate once ['FIX_STATUS_LABELS', 'GateEntry', 'OutputFinding', 'SynthesizedGatesEntry', 'ValidationOutput', 'ValidationReport', 'decision_for', 'to_verdict']; assign in source target order to __all__. Then For _FIX_STATUS_FIXED, assign 'Fixed'; source annotation Final. Then For _FIX_STATUS_PARTIALLY_FIXED, assign 'Partially Fixed'; source annotation Final. Then For _FIX_STATUS_NOT_FIXED, assign 'Not Fixed'; source annotation Final. Then For _FIX_STATUS_UNVERIFIABLE, assign 'UNVERIFIABLE'; source annotation Final.
// Source: vvaharness/validation/models/output.py:63-75
In source order: For _MERGE_READINESS_NOT_READY, assign 'Not Ready'; source annotation Final. Then For _CSV_MAX_CHARS, assign 4096; source annotation Final. Then For _TRUNCATION_MARKER, assign '...[truncated]'; source annotation Final. Then For FIX_STATUS_LABELS, assign {_FIX_STATUS_FIXED: Decision.FIXED, _FIX_STATUS_PARTIALLY_FIXED: Decision.PARTIALLY_FIXED, _FIX_STATUS_NOT_FIXED: Decision.NOT_FIXED, _FIX_STATUS_UNVERIFIABLE: Decision.INCONCLUSIVE}; source annotation Final[dict[str, Decision]].
// Source: vvaharness/validation/models/output.py:78-89
interface GateEntry {
  Describe the source Python type, preserving its base/metaclass expression order: BaseModel.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/validation/models/output.py:79-86
  In source order: Retain source documentation literal source_literal_79_4; it is not a model call. Then Evaluate once ConfigDict(extra='ignore'); assign in source target order to model_config. Then For gate_name, declare without assigning a value; source annotation str. Then For status, declare without assigning a value; source annotation Literal['pass', 'partial', 'fail', 'skip']. Then For summary, assign ''; source annotation str.
  // Source: vvaharness/validation/models/output.py:88-89
  In source order: For evidence, assign Field(default_factory=list); source annotation list[EvidenceAnchor]. Then For details, assign ''; source annotation str.
}
// Source: vvaharness/validation/models/output.py:92-98
interface SynthesizedGatesEntry {
  Describe the source Python type, preserving its base/metaclass expression order: BaseModel.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/validation/models/output.py:93-98
  In source order: Retain source documentation literal source_literal_93_4; it is not a model call. Then Evaluate once ConfigDict(extra='ignore'); assign in source target order to model_config. Then For tracking_id, declare without assigning a value; source annotation str. Then For gates, declare without assigning a value; source annotation list[GateEntry].
}
// Source: vvaharness/validation/models/output.py:101-156
interface OutputFinding {
  Describe the source Python type, preserving its base/metaclass expression order: BaseModel.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/validation/models/output.py:102-108
  In source order: Retain source documentation literal source_literal_102_4; it is not a model call. Then Evaluate once ConfigDict(extra='ignore'); assign in source target order to model_config. Then For tracking_id, declare without assigning a value; source annotation str. Then For finding_title, declare without assigning a value; source annotation str. Then For finding_description, declare without assigning a value; source annotation str.
  // Source: vvaharness/validation/models/output.py:109-113
  In source order: For affected_files, declare without assigning a value; source annotation str. Then For severity, assign 'Medium'; source annotation str. Then For fix_status, assign _FIX_STATUS_UNVERIFIABLE; source annotation str. Then For raw_score, assign Field(ge=0.0, le=1.0, default=0.0); source annotation float. Then For justification, assign ''; source annotation str.
  // Source: vvaharness/validation/models/output.py:114-118
  In source order: For merge_readiness, assign _MERGE_READINESS_NOT_READY; source annotation str. Then For gate_scores, assign Field(default_factory=dict); source annotation dict[str, object]. Then For conditions_for_full_fix, assign Field(default_factory=list); source annotation list[str]. Then For recommendations, assign Field(default_factory=list); source annotation list[str]. Then For files_needing_fixes, assign ''; source annotation str.
  // Source: vvaharness/validation/models/output.py:122-138
  // Source: vvaharness/validation/models/output.py:120-121
  Before creating this callable, evaluate and retain decorators top-to-bottom: field_validator('affected_files', 'files_needing_fixes', mode='before'), classmethod.
  // Source: vvaharness/validation/models/output.py:122-138
  // Source signature: _coerce_csv(cls, v: object, info: ValidationInfo) -> object
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _coerce_csv(cls, v, info) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/validation/models/output.py:124-125
    if (the source predicate isinstance(v, (list, tuple)) is truthy) {
      // Source: vvaharness/validation/models/output.py:125-125
      In source order: Evaluate once ','.join((str(x) for x in v)); assign in source target order to v.
    }
    // Source: vvaharness/validation/models/output.py:126-127
    if (the source predicate not isinstance(v, str) is truthy) {
      // Source: vvaharness/validation/models/output.py:127-127
      End this invocation with v.
    }
    // Source: vvaharness/validation/models/output.py:130-130
    In source order: Evaluate once redact(v); assign in source target order to safe.
    // Source: vvaharness/validation/models/output.py:131-132
    if (the source predicate len(safe) <= _CSV_MAX_CHARS is truthy) {
      // Source: vvaharness/validation/models/output.py:132-132
      End this invocation with safe.
    }
    // Source: vvaharness/validation/models/output.py:133-137
    In source order: Evaluate log.warning('validation output field %s exceeded %d characters; truncating', info.field_name, _CSV_MAX_CHARS); retain side effects and discard the expression result.
    // Source: vvaharness/validation/models/output.py:138-138
    End this invocation with safe[:_CSV_MAX_CHARS - len(_TRUNCATION_MARKER)] + _TRUNCATION_MARKER.
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vvaharness/validation/models/output.py:142-156
  // Source: vvaharness/validation/models/output.py:140-141
  Before creating this callable, evaluate and retain decorators top-to-bottom: field_validator('raw_score', mode='before'), classmethod.
  // Source: vvaharness/validation/models/output.py:142-156
  // Source signature: _clamp_raw_score(cls, v: object) -> object
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _clamp_raw_score(cls, v) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/validation/models/output.py:143-143
    In source order: Retain source documentation literal source_literal_143_8; it is not a model call.
    // Source: vvaharness/validation/models/output.py:144-145
    if (the source predicate isinstance(v, bool) or not isinstance(v, (int, float)) is truthy) {
      // Source: vvaharness/validation/models/output.py:145-145
      End this invocation with v.
    }
    // Source: vvaharness/validation/models/output.py:146-147
    In source order: Evaluate once float(v); assign in source target order to score. Then Evaluate once min(1.0, max(0.0, score)); assign in source target order to clamped.
    // Source: vvaharness/validation/models/output.py:148-155
    if (the source predicate clamped != score is truthy) {
      // Source: vvaharness/validation/models/output.py:150-155
      In source order: Evaluate log.warning('validation output raw_score=%r is outside [0.0, 1.0]; clamped to %.1f', score, clamped); retain side effects and discard the expression result.
    }
    // Source: vvaharness/validation/models/output.py:156-156
    End this invocation with clamped.
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
}
// Source: vvaharness/validation/models/output.py:159-170
interface ValidationOutput {
  Describe the source Python type, preserving its base/metaclass expression order: BaseModel.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/validation/models/output.py:160-170
  In source order: Retain source documentation literal source_literal_160_4; it is not a model call. Then Evaluate once ConfigDict(extra='ignore'); assign in source target order to model_config. Then For target_jira_status, declare without assigning a value; source annotation str. Then For findings, declare without assigning a value; source annotation list[OutputFinding]. Then For synthesized_gates, declare without assigning a value; source annotation list[SynthesizedGatesEntry].
}
// Source: vvaharness/validation/models/output.py:174-180
In source order: For _NARRATIVE_TEXT, assign ('finding_description', 'affected_files', 'files_needing_fixes', 'justification'); source annotation Final. Then For _NARRATIVE_LISTS, assign ('conditions_for_full_fix', 'recommendations'); source annotation Final.
// Source: vvaharness/validation/models/output.py:183-203
interface ValidationReport {
  Describe the source Python type, preserving its base/metaclass expression order: BaseModel.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/validation/models/output.py:184-188
  In source order: Retain source documentation literal source_literal_184_4; it is not a model call. Then Evaluate once ConfigDict(extra='ignore'); assign in source target order to model_config. Then For findings, assign Field(default_factory=list); source annotation list[OutputFinding].
  // Source: vvaharness/validation/models/output.py:191-198
  // Source: vvaharness/validation/models/output.py:190-190
  Before creating this callable, evaluate and retain decorators top-to-bottom: model_validator(mode='after').
  // Source: vvaharness/validation/models/output.py:191-198
  // Source signature: _redact_narrative(self) -> ValidationReport
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _redact_narrative(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/validation/models/output.py:192-192
    In source order: Retain source documentation literal source_literal_192_8; it is not a model call.
    // Source: vvaharness/validation/models/output.py:193-197
    for each finding in self.findings {
      // Source: vvaharness/validation/models/output.py:194-195
      for each name in _NARRATIVE_TEXT {
        // Source: vvaharness/validation/models/output.py:195-195
        In source order: Evaluate setattr(finding, name, redact(getattr(finding, name))); retain side effects and discard the expression result.
      }
      // Source: vvaharness/validation/models/output.py:196-197
      for each name in _NARRATIVE_LISTS {
        // Source: vvaharness/validation/models/output.py:197-197
        In source order: Evaluate setattr(finding, name, [redact(item) for item in getattr(finding, name)]); retain side effects and discard the expression result.
      }
    }
    // Source: vvaharness/validation/models/output.py:198-198
    End this invocation with self.
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vvaharness/validation/models/output.py:201-203
  // Source: vvaharness/validation/models/output.py:200-200
  Before creating this callable, evaluate and retain decorators top-to-bottom: classmethod.
  // Source: vvaharness/validation/models/output.py:201-203
  // Source signature: from_file(cls, path: Path) -> ValidationReport
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn from_file(cls, path) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/validation/models/output.py:202-202
    In source order: Retain source documentation literal source_literal_202_8; it is not a model call.
    // Source: vvaharness/validation/models/output.py:203-203
    End this invocation with cls.model_validate(_read_json(path)).
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
}
// Source: vvaharness/validation/models/output.py:206-212
// Source signature: _read_json(path: Path) -> object
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _read_json(path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/models/output.py:207-207
  In source order: Retain source documentation literal source_literal_207_4; it is not a model call.
  // Source: vvaharness/validation/models/output.py:208-212
  Perform the following protected operations {
    // Source: vvaharness/validation/models/output.py:209-209
    End this invocation with json.loads(path.read_text(encoding='utf-8')).
  }
  // Source: vvaharness/validation/models/output.py:210-212
  On the first matching source exception json.JSONDecodeError as exc, in handler order {
    // Source: vvaharness/validation/models/output.py:211-211
    In source order: Evaluate once source_template_211_14; assign in source target order to msg.
    // Source: vvaharness/validation/models/output.py:212-212
    Raise ValueError(msg) with explicit source cause exc.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/models/output.py:215-221
// Source signature: decision_for(fix_status: str) -> Decision
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn decision_for(fix_status) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/models/output.py:216-217
  In source order: Retain source documentation literal source_literal_216_4; it is not a model call. Then Evaluate once fix_status.strip().casefold(); assign in source target order to folded.
  // Source: vvaharness/validation/models/output.py:218-221
  End this invocation with next((d for label, d in FIX_STATUS_LABELS.items() if label.casefold() == folded), Decision.INCONCLUSIVE).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/models/output.py:224-232
// Source signature: _to_gate(entry: GateEntry) -> GateAssessment
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _to_gate(entry) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/models/output.py:225-225
  In source order: Retain source documentation literal source_literal_225_4; it is not a model call.
  // Source: vvaharness/validation/models/output.py:226-232
  End this invocation with GateAssessment(name=entry.gate_name, status=GateStatus(entry.status), summary=entry.summary, details=entry.details, evidence=tuple(entry.evidence)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/models/output.py:235-252
// Source signature: to_verdict(output_finding: OutputFinding, synthesized_gates: SynthesizedGatesEntry | None, *, provenance: Provenance) -> Verdict
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn to_verdict(output_finding, synthesized_gates, provenance) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/models/output.py:241-243
  In source order: Retain source documentation literal source_literal_241_4; it is not a model call. Then Evaluate once decision_for(output_finding.fix_status); assign in source target order to decision. Then Evaluate once synthesized_gates.gates if synthesized_gates is not None else []; assign in source target order to gates.
  // Source: vvaharness/validation/models/output.py:244-252
  End this invocation with Verdict(decision=decision, rationale=output_finding.justification, score=None if decision is Decision.INCONCLUSIVE else output_finding.raw_score, gates=tuple((_to_gate(entry) for entry in gates)), conditions=tuple(output_finding.conditions_for_full_fix), recommendations=tuple(output_finding.recommendations), produced_by=provenance).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.models import Decision, EvidenceAnchor, GateAssessment, GateStatus, Provenance, Verdict` at source line 32: `source_detail/vvaharness/models/__init__.py.sudo.md`.
- `from vvaharness.report.redact import redact` at source line 40: `source_detail/vvaharness/report/redact.py.sudo.md`.
- `from vvaharness.util import logs` at source line 41: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import logs` at source line 41: `source_detail/vvaharness/util/logs.py.sudo.md`.
