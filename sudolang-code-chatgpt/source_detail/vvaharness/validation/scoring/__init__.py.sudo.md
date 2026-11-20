# vvaharness/validation/scoring/__init__.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/validation/scoring/__init__.py.evidence.json`. SHA-256: `e07937e877038b7e17bcd8aecfb2d7ab70c4f98e48ca438083101d8f289ec095`.

```sudo
// Source: vvaharness/validation/scoring/__init__.py:15-26
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from collections.abc import Mapping; preserve alias and import-time effects. Then Resolve source import from vvaharness.models import GateAssessment, GateStatus, ScoringPolicy; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.constants.scoring import CRITERION_NAME_FIELD, FIX_POLICY, STATUS_MULTIPLIER; preserve alias and import-time effects.
// Source: vvaharness/validation/scoring/__init__.py:27-36
In source order: Resolve source import from vvaharness.validation.models.scoring import RawCriterion, ScoringConfig, ValidationScore; preserve alias and import-time effects. Then Resolve source import from ._configs import FIX_CONFIG; preserve alias and import-time effects. Then Resolve source import from ._engine import _CRITICAL_NOT_CLEAN, parse_raw_criterion; preserve alias and import-time effects. Then Resolve source import from ._engine import score as _score; preserve alias and import-time effects. Then Resolve source import from ._justify import build_fix_justification; preserve alias and import-time effects.
// Source: vvaharness/validation/scoring/__init__.py:38-38
In source order: Evaluate once ['FIX_CONFIG', 'FIX_POLICY', 'ValidationScore', 'score_fix']; assign in source target order to __all__.
// Source: vvaharness/validation/scoring/__init__.py:41-51
// Source signature: _config_for(policy: ScoringPolicy | None) -> ScoringConfig
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _config_for(policy) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/scoring/__init__.py:42-42
  In source order: Retain source documentation literal source_literal_42_4; it is not a model call.
  // Source: vvaharness/validation/scoring/__init__.py:43-44
  if (the source predicate policy is None or policy == FIX_POLICY is truthy) {
    // Source: vvaharness/validation/scoring/__init__.py:44-44
    End this invocation with FIX_CONFIG.
  }
  // Source: vvaharness/validation/scoring/__init__.py:45-51
  End this invocation with ScoringConfig.from_policy(policy, name='fix', criterion_name_field=CRITERION_NAME_FIELD, status_multiplier=STATUS_MULTIPLIER, justify=build_fix_justification).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/scoring/__init__.py:54-59
// Source signature: _has_critical_failure(config: ScoringConfig, parsed: list[RawCriterion]) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _has_critical_failure(config, parsed) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/scoring/__init__.py:55-55
  In source order: Retain source documentation literal source_literal_55_4; it is not a model call.
  // Source: vvaharness/validation/scoring/__init__.py:56-59
  End this invocation with any((criterion.name in config.critical_criteria and criterion.status in _CRITICAL_NOT_CLEAN for criterion in parsed)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/scoring/__init__.py:62-70
// Source signature: _to_gate(criterion: RawCriterion) -> GateAssessment
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _to_gate(criterion) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/scoring/__init__.py:63-63
  In source order: Retain source documentation literal source_literal_63_4; it is not a model call.
  // Source: vvaharness/validation/scoring/__init__.py:64-70
  End this invocation with GateAssessment(name=criterion.name, status=GateStatus(criterion.status), summary=criterion.summary, details=criterion.details, evidence=criterion.evidence).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/scoring/__init__.py:73-86
// Source signature: score_fix(gates: list[Mapping[str, object]], *, policy: ScoringPolicy | None=None) -> ValidationScore
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn score_fix(gates, policy) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/scoring/__init__.py:76-79
  In source order: Retain source documentation literal source_literal_76_4; it is not a model call. Then Evaluate once _config_for(policy); assign in source target order to config. Then Evaluate once [parse_raw_criterion(gate, config.criterion_name_field) for gate in gates]; assign in source target order to parsed. Then Evaluate once _score(config, parsed); assign in source target order to result.
  // Source: vvaharness/validation/scoring/__init__.py:80-86
  End this invocation with ValidationScore(raw_score=result.raw_score, decision=result.decision, justification=result.justification, gates=tuple((_to_gate(criterion) for criterion in parsed)), has_critical_failure=_has_critical_failure(config, parsed)).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.models import GateAssessment, GateStatus, ScoringPolicy` at source line 21: `source_detail/vvaharness/models/__init__.py.sudo.md`.
- `from vvaharness.validation.constants.scoring import CRITERION_NAME_FIELD, FIX_POLICY, STATUS_MULTIPLIER` at source line 22: `source_detail/vvaharness/validation/constants/scoring.py.sudo.md`.
- `from vvaharness.validation.models.scoring import RawCriterion, ScoringConfig, ValidationScore` at source line 27: `source_detail/vvaharness/validation/models/scoring.py.sudo.md`.
- `from ._configs import FIX_CONFIG` at source line 33: `source_detail/vvaharness/validation/scoring/_configs.py.sudo.md`.
- `from ._engine import _CRITICAL_NOT_CLEAN, parse_raw_criterion` at source line 34: `source_detail/vvaharness/validation/scoring/_engine.py.sudo.md`.
- `from ._engine import score as _score` at source line 35: `source_detail/vvaharness/validation/scoring/_engine.py.sudo.md`.
- `from ._justify import build_fix_justification` at source line 36: `source_detail/vvaharness/validation/scoring/_justify.py.sudo.md`.
