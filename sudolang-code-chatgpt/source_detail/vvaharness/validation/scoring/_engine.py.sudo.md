# vvaharness/validation/scoring/_engine.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/validation/scoring/_engine.py.evidence.json`. SHA-256: `167ee7696b9608943a8f85c74f4e4dee6feb79c081e7ac454449e2efd7bff528`.

```sudo
// Source: vvaharness/validation/scoring/_engine.py:15-22
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from collections.abc import Mapping; preserve alias and import-time effects. Then Resolve source import from typing import Final; preserve alias and import-time effects. Then Resolve source import from vvaharness.models import Decision, EvidenceAnchor, GateStatus; preserve alias and import-time effects.
// Source: vvaharness/validation/scoring/_engine.py:23-35
In source order: Resolve source import from vvaharness.validation.constants.scoring import SCORE_FLOOR, SCORE_PRECISION; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.enums.synthesis import SynthesisConfidence; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.models.scoring import RawCriterion, RawExtra, ScoreResult, ScoringConfig; preserve alias and import-time effects. Then Evaluate once ['parse_raw_criterion', 'score']; assign in source target order to __all__. Then For INCONCLUSIVE_PREFIX, assign 'INCONCLUSIVE'; source annotation Final.
// Source: vvaharness/validation/scoring/_engine.py:38-41
// Source signature: _str_from(entry: Mapping[str, object], field_key: str, default: str='') -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _str_from(entry, field_key, default) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/scoring/_engine.py:39-40
  In source order: Retain source documentation literal source_literal_39_4; it is not a model call. Then Evaluate once entry.get(field_key, default); assign in source target order to value.
  // Source: vvaharness/validation/scoring/_engine.py:41-41
  End this invocation with value if isinstance(value, str) else default.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/scoring/_engine.py:44-48
// Source signature: _int_or_none(value: object) -> int | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _int_or_none(value) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/scoring/_engine.py:45-45
  In source order: Retain source documentation literal source_literal_45_4; it is not a model call.
  // Source: vvaharness/validation/scoring/_engine.py:46-47
  if (the source predicate isinstance(value, bool) is truthy) {
    // Source: vvaharness/validation/scoring/_engine.py:47-47
    End this invocation with None.
  }
  // Source: vvaharness/validation/scoring/_engine.py:48-48
  End this invocation with value if isinstance(value, int) else None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/scoring/_engine.py:51-57
// Source signature: _parse_evidence(entry: Mapping[str, object]) -> EvidenceAnchor
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _parse_evidence(entry) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/scoring/_engine.py:52-52
  In source order: Retain source documentation literal source_literal_52_4; it is not a model call.
  // Source: vvaharness/validation/scoring/_engine.py:53-57
  End this invocation with EvidenceAnchor(file=_str_from(entry, 'file'), line=_int_or_none(entry.get('line')), snippet=_str_from(entry, 'snippet')).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/scoring/_engine.py:60-78
// Source signature: parse_raw_criterion(entry: Mapping[str, object], name_field: str) -> RawCriterion
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn parse_raw_criterion(entry, name_field) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/scoring/_engine.py:61-63
  In source order: Retain source documentation literal source_literal_61_4; it is not a model call. Then Evaluate once entry.get('evidence', []); assign in source target order to evidence_raw. Then For evidence, assign (); source annotation tuple[EvidenceAnchor, ...].
  // Source: vvaharness/validation/scoring/_engine.py:64-69
  if (the source predicate isinstance(evidence_raw, list) is truthy) {
    // Source: vvaharness/validation/scoring/_engine.py:65-69
    In source order: Evaluate once tuple((_parse_evidence(evidence_entry) for evidence_entry in evidence_raw if isinstance(evidence_entry, Mapping))); assign in source target order to evidence.
  }
  // Source: vvaharness/validation/scoring/_engine.py:70-78
  End this invocation with RawCriterion(name=_str_from(entry, name_field), status=GateStatus(_str_from(entry, 'status')).value, confidence=_str_from(entry, 'confidence'), summary=_str_from(entry, 'summary'), details=_str_from(entry, 'details'), evidence=evidence).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/scoring/_engine.py:81-87
// Source signature: _inconclusive(reason: str) -> ScoreResult
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _inconclusive(reason) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/scoring/_engine.py:82-82
  In source order: Retain source documentation literal source_literal_82_4; it is not a model call.
  // Source: vvaharness/validation/scoring/_engine.py:83-87
  End this invocation with ScoreResult(raw_score=0.0, decision=Decision.INCONCLUSIVE, justification=source_template_86_22).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/scoring/_engine.py:90-100
// Source signature: _shape_error(config: ScoringConfig, criteria: list[RawCriterion]) -> ScoreResult | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _shape_error(config, criteria) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/scoring/_engine.py:91-93
  In source order: Retain source documentation literal source_literal_91_4; it is not a model call. Then For names, assign [criterion.name for criterion in criteria]; source annotation list[str]. Then For provided, assign set(names); source annotation set[str].
  // Source: vvaharness/validation/scoring/_engine.py:94-96
  if (the source predicate provided != config.expected_criteria is truthy) {
    // Source: vvaharness/validation/scoring/_engine.py:95-95
    In source order: Evaluate once sorted(config.expected_criteria - provided); assign in source target order to missing.
    // Source: vvaharness/validation/scoring/_engine.py:96-96
    End this invocation with _inconclusive(source_template_96_29).
  }
  // Source: vvaharness/validation/scoring/_engine.py:97-99
  if (the source predicate len(names) != len(provided) is truthy) {
    // Source: vvaharness/validation/scoring/_engine.py:98-98
    In source order: For duplicates, assign sorted({name for name in names if names.count(name) > 1}); source annotation list[str].
    // Source: vvaharness/validation/scoring/_engine.py:99-99
    End this invocation with _inconclusive(source_template_99_29).
  }
  // Source: vvaharness/validation/scoring/_engine.py:100-100
  End this invocation with None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/scoring/_engine.py:103-119
// Source signature: _renormalized_score(config: ScoringConfig, criteria: list[RawCriterion]) -> ScoreResult | float
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _renormalized_score(config, criteria) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/scoring/_engine.py:106-108
  In source order: Retain source documentation literal source_literal_106_4; it is not a model call. Then Evaluate once 0.0; assign in source target order to earned. Then Evaluate once 0.0; assign in source target order to active_weight.
  // Source: vvaharness/validation/scoring/_engine.py:109-115
  for each criterion in criteria {
    // Source: vvaharness/validation/scoring/_engine.py:110-111
    if (the source predicate criterion.status == GateStatus.SKIP.value is truthy) {
      // Source: vvaharness/validation/scoring/_engine.py:111-111
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/validation/scoring/_engine.py:112-115
    In source order: Apply source augmented assignment active_weight += config.weights[criterion.name] with source evaluation/in-place semantics. Then Apply source augmented assignment earned += config.weights[criterion.name] * config.status_multiplier.get(criterion.status, SCORE_FLOOR) with source evaluation/in-place semantics.
  }
  // Source: vvaharness/validation/scoring/_engine.py:116-117
  if (the source predicate active_weight <= 0.0 is truthy) {
    // Source: vvaharness/validation/scoring/_engine.py:117-117
    End this invocation with _inconclusive('no gates were evaluated.').
  }
  // Source: vvaharness/validation/scoring/_engine.py:119-119
  End this invocation with round(min(earned / active_weight, 1.0), SCORE_PRECISION).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/scoring/_engine.py:122-124
In source order: For _UNEVALUATED, assign frozenset({GateStatus.SKIP.value, GateStatus.INVALID.value}); source annotation Final. Then For _CRITICAL_NOT_CLEAN, assign frozenset({GateStatus.PARTIAL.value, GateStatus.FAIL.value}); source annotation Final.
// Source: vvaharness/validation/scoring/_engine.py:127-137
// Source signature: _critical_gate_error(config: ScoringConfig, criteria: list[RawCriterion]) -> ScoreResult | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _critical_gate_error(config, criteria) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/scoring/_engine.py:130-130
  In source order: Retain source documentation literal source_literal_130_4; it is not a model call.
  // Source: vvaharness/validation/scoring/_engine.py:131-136
  for each criterion in criteria {
    // Source: vvaharness/validation/scoring/_engine.py:132-136
    if (the source predicate criterion.name in config.critical_criteria and criterion.status in _UNEVALUATED is truthy) {
      // Source: vvaharness/validation/scoring/_engine.py:133-136
      End this invocation with _inconclusive(source_template_134_16).
    }
  }
  // Source: vvaharness/validation/scoring/_engine.py:137-137
  End this invocation with None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/scoring/_engine.py:140-151
// Source signature: _consensus_error(criteria: list[RawCriterion]) -> ScoreResult | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _consensus_error(criteria) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/scoring/_engine.py:141-146
  In source order: Retain source documentation literal source_literal_141_4; it is not a model call. Then Evaluate once sorted((criterion.name for criterion in criteria if criterion.confidence == SynthesisConfidence.FLAGGED.value)); assign in source target order to flagged.
  // Source: vvaharness/validation/scoring/_engine.py:147-148
  if (the source predicate not flagged is truthy) {
    // Source: vvaharness/validation/scoring/_engine.py:148-148
    End this invocation with None.
  }
  // Source: vvaharness/validation/scoring/_engine.py:149-151
  End this invocation with _inconclusive(source_template_150_8).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/scoring/_engine.py:154-164
// Source signature: _cap_critical_fail(config: ScoringConfig, criteria: list[RawCriterion], decision: Decision) -> Decision
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _cap_critical_fail(config, criteria, decision) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/scoring/_engine.py:157-157
  In source order: Retain source documentation literal source_literal_157_4; it is not a model call.
  // Source: vvaharness/validation/scoring/_engine.py:158-159
  if (the source predicate not config.verdicts or decision is not config.verdicts[0].decision is truthy) {
    // Source: vvaharness/validation/scoring/_engine.py:159-159
    End this invocation with decision.
  }
  // Source: vvaharness/validation/scoring/_engine.py:160-163
  In source order: Evaluate once any((criterion.name in config.critical_criteria and criterion.status in _CRITICAL_NOT_CLEAN for criterion in criteria)); assign in source target order to not_clean.
  // Source: vvaharness/validation/scoring/_engine.py:164-164
  End this invocation with config.verdicts[1].decision if not_clean and len(config.verdicts) > 1 else decision.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/scoring/_engine.py:167-173
// Source signature: _precheck(config: ScoringConfig, criteria: list[RawCriterion]) -> ScoreResult | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _precheck(config, criteria) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/scoring/_engine.py:168-168
  In source order: Retain source documentation literal source_literal_168_4; it is not a model call.
  // Source: vvaharness/validation/scoring/_engine.py:169-173
  End this invocation with _shape_error(config, criteria) or _consensus_error(criteria) or _critical_gate_error(config, criteria).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/scoring/_engine.py:176-181
// Source signature: _apply_verdicts(config: ScoringConfig, raw_score: float) -> Decision
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _apply_verdicts(config, raw_score) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/scoring/_engine.py:177-177
  In source order: Retain source documentation literal source_literal_177_4; it is not a model call.
  // Source: vvaharness/validation/scoring/_engine.py:178-180
  for each rule in config.verdicts {
    // Source: vvaharness/validation/scoring/_engine.py:179-180
    if (the source predicate raw_score >= rule.min_score is truthy) {
      // Source: vvaharness/validation/scoring/_engine.py:180-180
      End this invocation with rule.decision.
    }
  }
  // Source: vvaharness/validation/scoring/_engine.py:181-181
  End this invocation with Decision.INCONCLUSIVE.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/scoring/_engine.py:184-202
// Source signature: score(config: ScoringConfig, criteria: list[RawCriterion], extra: RawExtra | None=None) -> ScoreResult
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn score(config, criteria, extra) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/scoring/_engine.py:189-190
  In source order: Retain source documentation literal source_literal_189_4; it is not a model call. Then For precheck_error, assign _precheck(config, criteria); source annotation ScoreResult | None.
  // Source: vvaharness/validation/scoring/_engine.py:191-192
  if (the source predicate precheck_error is not None is truthy) {
    // Source: vvaharness/validation/scoring/_engine.py:192-192
    End this invocation with precheck_error.
  }
  // Source: vvaharness/validation/scoring/_engine.py:193-193
  In source order: For scored, assign _renormalized_score(config, criteria); source annotation ScoreResult | float.
  // Source: vvaharness/validation/scoring/_engine.py:194-195
  if (the source predicate isinstance(scored, ScoreResult) is truthy) {
    // Source: vvaharness/validation/scoring/_engine.py:195-195
    End this invocation with scored.
  }
  // Source: vvaharness/validation/scoring/_engine.py:196-197
  In source order: Evaluate once _cap_critical_fail(config, criteria, _apply_verdicts(config, scored)); assign in source target order to decision. Then Evaluate once ScoreResult(raw_score=scored, decision=decision, justification=''); assign in source target order to partial.
  // Source: vvaharness/validation/scoring/_engine.py:198-202
  End this invocation with ScoreResult(raw_score=scored, decision=decision, justification=config.justify(partial, criteria, extra or {})).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.models import Decision, EvidenceAnchor, GateStatus` at source line 22: `source_detail/vvaharness/models/__init__.py.sudo.md`.
- `from vvaharness.validation.constants.scoring import SCORE_FLOOR, SCORE_PRECISION` at source line 23: `source_detail/vvaharness/validation/constants/scoring.py.sudo.md`.
- `from vvaharness.validation.enums.synthesis import SynthesisConfidence` at source line 24: `source_detail/vvaharness/validation/enums/synthesis.py.sudo.md`.
- `from vvaharness.validation.models.scoring import RawCriterion, RawExtra, ScoreResult, ScoringConfig` at source line 25: `source_detail/vvaharness/validation/models/scoring.py.sudo.md`.
