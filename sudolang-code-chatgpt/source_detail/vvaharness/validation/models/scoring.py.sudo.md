# vvaharness/validation/models/scoring.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/validation/models/scoring.py.evidence.json`. SHA-256: `c2472f6349af141981c52cb1779903dfd9999006a5f6b0c5f483a429f8c4e377`.

```sudo
// Source: vvaharness/validation/models/scoring.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from collections.abc import Callable, Mapping; preserve alias and import-time effects. Then Resolve source import from dataclasses import dataclass, field; preserve alias and import-time effects. Then Resolve source import from typing import TYPE_CHECKING; preserve alias and import-time effects.
// Source: vvaharness/validation/models/scoring.py:23-23
In source order: Resolve source import from vvaharness.models import Decision, GateAssessment, ScoringPolicy; preserve alias and import-time effects.
// Source: vvaharness/validation/models/scoring.py:25-26
if (the source predicate TYPE_CHECKING is truthy) {
  // Source: vvaharness/validation/models/scoring.py:26-26
  In source order: Resolve source import from vvaharness.models import EvidenceAnchor; preserve alias and import-time effects.
}
// Source: vvaharness/validation/models/scoring.py:28-38
In source order: Evaluate once ['RawCriterion', 'RawExtra', 'ScoreResult', 'ScoringConfig', 'ValidationScore', 'VerdictRule']; assign in source target order to __all__. Then Evaluate once Mapping[str, object]; assign in source target order to RawExtra.
// Source: vvaharness/validation/models/scoring.py:42-50
// Source: vvaharness/validation/models/scoring.py:41-41
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vvaharness/validation/models/scoring.py:42-50
interface RawCriterion {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/validation/models/scoring.py:43-48
  In source order: Retain source documentation literal source_literal_43_4; it is not a model call. Then For name, declare without assigning a value; source annotation str. Then For status, declare without assigning a value; source annotation str. Then For summary, assign ''; source annotation str. Then For details, assign ''; source annotation str.
  // Source: vvaharness/validation/models/scoring.py:49-50
  In source order: For evidence, assign field(default_factory=tuple); source annotation tuple[EvidenceAnchor, ...]. Then For confidence, assign ''; source annotation str.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vvaharness/validation/models/scoring.py:54-58
// Source: vvaharness/validation/models/scoring.py:53-53
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vvaharness/validation/models/scoring.py:54-58
interface VerdictRule {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/validation/models/scoring.py:55-58
  In source order: Retain source documentation literal source_literal_55_4; it is not a model call. Then For min_score, declare without assigning a value; source annotation float. Then For decision, declare without assigning a value; source annotation Decision.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vvaharness/validation/models/scoring.py:62-67
// Source: vvaharness/validation/models/scoring.py:61-61
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vvaharness/validation/models/scoring.py:62-67
interface ScoreResult {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/validation/models/scoring.py:63-67
  In source order: Retain source documentation literal source_literal_63_4; it is not a model call. Then For raw_score, declare without assigning a value; source annotation float. Then For decision, declare without assigning a value; source annotation Decision. Then For justification, declare without assigning a value; source annotation str.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vvaharness/validation/models/scoring.py:71-119
// Source: vvaharness/validation/models/scoring.py:70-70
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vvaharness/validation/models/scoring.py:71-119
interface ScoringConfig {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/validation/models/scoring.py:72-77
  In source order: Retain source documentation literal source_literal_72_4; it is not a model call. Then For name, declare without assigning a value; source annotation str. Then For criterion_name_field, declare without assigning a value; source annotation str. Then For weights, declare without assigning a value; source annotation Mapping[str, float]. Then For status_multiplier, declare without assigning a value; source annotation Mapping[str, float].
  // Source: vvaharness/validation/models/scoring.py:78-83
  In source order: For verdicts, declare without assigning a value; source annotation tuple[VerdictRule, ...]. Then For justify, declare without assigning a value; source annotation Callable[[ScoreResult, list[RawCriterion], RawExtra], str]. Then For expected_criteria, declare without assigning a value; source annotation frozenset[str]. Then For critical_criteria, assign frozenset(); source annotation frozenset[str].
  // Source: vvaharness/validation/models/scoring.py:86-109
  // Source: vvaharness/validation/models/scoring.py:85-85
  Before creating this callable, evaluate and retain decorators top-to-bottom: classmethod.
  // Source: vvaharness/validation/models/scoring.py:86-109
  // Source signature: from_policy(cls, policy: ScoringPolicy, *, name: str, criterion_name_field: str, status_multiplier: Mapping[str, float], justify: Callable[[ScoreResult, list[RawCriterion], RawExtra], str]) -> ScoringConfig
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn from_policy(cls, policy, name, criterion_name_field, status_multiplier, justify) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/validation/models/scoring.py:95-95
    In source order: Retain source documentation literal source_literal_95_8; it is not a model call.
    // Source: vvaharness/validation/models/scoring.py:96-109
    End this invocation with cls(name=name, criterion_name_field=criterion_name_field, weights=dict(policy.weights), expected_criteria=frozenset(policy.required_gates), status_multiplier=dict(status_multiplier), verdicts=(VerdictRule(min_score=policy.ready_at, decision=Decision.FIXED), VerdictRule(min_score=policy.conditional_at, decision=Decision.PARTIALLY_FIXED), VerdictRule(min_score=0.0, decision=Decision.NOT_FIXED)), justify=justify, critical_criteria=frozenset(policy.critical)).
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vvaharness/validation/models/scoring.py:111-119
  // Source signature: to_policy(self) -> ScoringPolicy
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn to_policy(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/validation/models/scoring.py:112-112
    In source order: Retain source documentation literal source_literal_112_8; it is not a model call.
    // Source: vvaharness/validation/models/scoring.py:113-119
    End this invocation with ScoringPolicy(required_gates=tuple(sorted(self.expected_criteria)), weights=dict(self.weights), critical=self.critical_criteria, ready_at=self.verdicts[0].min_score if self.verdicts else 0.0, conditional_at=self.verdicts[1].min_score if len(self.verdicts) > 1 else 0.0).
    If execution reaches this end, finish with the source implicit None result.
  }
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vvaharness/validation/models/scoring.py:123-130
// Source: vvaharness/validation/models/scoring.py:122-122
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vvaharness/validation/models/scoring.py:123-130
interface ValidationScore {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/validation/models/scoring.py:124-129
  In source order: Retain source documentation literal source_literal_124_4; it is not a model call. Then For raw_score, declare without assigning a value; source annotation float. Then For decision, declare without assigning a value; source annotation Decision. Then For justification, declare without assigning a value; source annotation str. Then For gates, declare without assigning a value; source annotation tuple[GateAssessment, ...].
  // Source: vvaharness/validation/models/scoring.py:130-130
  In source order: For has_critical_failure, declare without assigning a value; source annotation bool.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
```

## Local import links

- `from vvaharness.models import Decision, GateAssessment, ScoringPolicy` at source line 23: `source_detail/vvaharness/models/__init__.py.sudo.md`.
- `from vvaharness.models import EvidenceAnchor` at source line 26: `source_detail/vvaharness/models/__init__.py.sudo.md`.
