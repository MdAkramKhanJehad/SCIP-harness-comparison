# vvaharness/validation/scoring/_justify.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/validation/scoring/_justify.py.evidence.json`. SHA-256: `c8c1bbe350c57cf328da2d05ff1c4a272d37cc960941a6332a8e16000e44ec8f`.

```sudo
// Source: vvaharness/validation/scoring/_justify.py:15-25
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from typing import Final; preserve alias and import-time effects. Then Resolve source import from vvaharness.models import Decision, GateStatus; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.constants.scoring import CONFIDENCE_PERCENT_SCALE, MAX_EVIDENCE_ANCHORS; preserve alias and import-time effects.
// Source: vvaharness/validation/scoring/_justify.py:26-31
In source order: Resolve source import from vvaharness.validation.models.scoring import RawCriterion, RawExtra, ScoreResult; preserve alias and import-time effects. Then Evaluate once ['build_fix_justification']; assign in source target order to __all__. Then For _FAIL_STATUSES, assign frozenset({GateStatus.FAIL.value, GateStatus.PARTIAL.value}); source annotation Final. Then For _PASS_STATUSES, assign frozenset({GateStatus.PASS.value}); source annotation Final.
// Source: vvaharness/validation/scoring/_justify.py:34-36
// Source signature: _confidence(result: ScoreResult) -> int
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _confidence(result) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/scoring/_justify.py:35-35
  In source order: Retain source documentation literal source_literal_35_4; it is not a model call.
  // Source: vvaharness/validation/scoring/_justify.py:36-36
  End this invocation with round(result.raw_score * CONFIDENCE_PERCENT_SCALE).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/scoring/_justify.py:39-41
// Source signature: _summaries(gates: list[RawCriterion], statuses: frozenset[str]) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _summaries(gates, statuses) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/scoring/_justify.py:40-40
  In source order: Retain source documentation literal source_literal_40_4; it is not a model call.
  // Source: vvaharness/validation/scoring/_justify.py:41-41
  End this invocation with '; '.join((criterion.summary for criterion in gates if criterion.status in statuses)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/scoring/_justify.py:44-46
// Source signature: _anchors_str(gates: list[RawCriterion]) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _anchors_str(gates) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/scoring/_justify.py:45-45
  In source order: Retain source documentation literal source_literal_45_4; it is not a model call.
  // Source: vvaharness/validation/scoring/_justify.py:46-46
  End this invocation with '; '.join(_collect_evidence_anchors(gates)[:MAX_EVIDENCE_ANCHORS]).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/scoring/_justify.py:49-55
// Source signature: _fixed_text(result: ScoreResult, gates: list[RawCriterion]) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _fixed_text(result, gates) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/scoring/_justify.py:50-50
  In source order: Retain source documentation literal source_literal_50_4; it is not a model call.
  // Source: vvaharness/validation/scoring/_justify.py:51-55
  End this invocation with source_template_52_8.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/scoring/_justify.py:58-66
// Source signature: _partial_text(result: ScoreResult, gates: list[RawCriterion]) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _partial_text(result, gates) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/scoring/_justify.py:59-60
  In source order: Retain source documentation literal source_literal_59_4; it is not a model call. Then Evaluate once _files_needing_fixes(gates); assign in source target order to files.
  // Source: vvaharness/validation/scoring/_justify.py:61-66
  End this invocation with source_template_62_8.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/scoring/_justify.py:69-78
// Source signature: _not_fixed_text(result: ScoreResult, gates: list[RawCriterion]) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _not_fixed_text(result, gates) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/scoring/_justify.py:70-72
  In source order: Retain source documentation literal source_literal_70_4; it is not a model call. Then Evaluate once _files_needing_fixes(gates); assign in source target order to files. Then Evaluate once _recommended_actions(gates); assign in source target order to actions.
  // Source: vvaharness/validation/scoring/_justify.py:73-78
  End this invocation with source_template_74_8.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/scoring/_justify.py:81-85
In source order: For _DECISION_FORMATTERS, assign {Decision.FIXED: _fixed_text, Decision.PARTIALLY_FIXED: _partial_text, Decision.NOT_FIXED: _not_fixed_text}; source annotation Final.
// Source: vvaharness/validation/scoring/_justify.py:88-96
// Source signature: build_fix_justification(result: ScoreResult, gates: list[RawCriterion], _extra: RawExtra) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn build_fix_justification(result, gates, _extra) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/scoring/_justify.py:93-93
  In source order: Retain source documentation literal source_literal_93_4; it is not a model call.
  // Source: vvaharness/validation/scoring/_justify.py:94-95
  if (the source predicate result.decision is Decision.INCONCLUSIVE is truthy) {
    // Source: vvaharness/validation/scoring/_justify.py:95-95
    End this invocation with result.justification or ''.
  }
  // Source: vvaharness/validation/scoring/_justify.py:96-96
  End this invocation with _DECISION_FORMATTERS.get(result.decision, _not_fixed_text)(result, gates).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/scoring/_justify.py:99-105
// Source signature: _collect_evidence_anchors(criteria: list[RawCriterion]) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _collect_evidence_anchors(criteria) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/scoring/_justify.py:100-100
  In source order: Retain source documentation literal source_literal_100_4; it is not a model call.
  // Source: vvaharness/validation/scoring/_justify.py:101-105
  End this invocation with [source_template_102_8 if item.line is not None else item.file for criterion in criteria for item in criterion.evidence].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/scoring/_justify.py:108-114
// Source signature: _files_needing_fixes(criteria: list[RawCriterion]) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _files_needing_fixes(criteria) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/scoring/_justify.py:109-110
  In source order: Retain source documentation literal source_literal_109_4; it is not a model call. Then For files, assign set(); source annotation set[str].
  // Source: vvaharness/validation/scoring/_justify.py:111-113
  for each criterion in criteria {
    // Source: vvaharness/validation/scoring/_justify.py:112-113
    if (the source predicate criterion.status in _FAIL_STATUSES is truthy) {
      // Source: vvaharness/validation/scoring/_justify.py:113-113
      In source order: Evaluate files.update((item.file for item in criterion.evidence)); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/validation/scoring/_justify.py:114-114
  End this invocation with sorted((filename for filename in files if filename)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/scoring/_justify.py:117-124
// Source signature: _recommended_actions(gates: list[RawCriterion]) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _recommended_actions(gates) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/scoring/_justify.py:118-123
  In source order: Retain source documentation literal source_literal_118_4; it is not a model call. Then Evaluate once [source_template_120_8 for criterion in gates if criterion.status == GateStatus.FAIL.value]; assign in source target order to actions.
  // Source: vvaharness/validation/scoring/_justify.py:124-124
  End this invocation with actions or ['Review all failing gates and apply fixes'].
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.models import Decision, GateStatus` at source line 21: `source_detail/vvaharness/models/__init__.py.sudo.md`.
- `from vvaharness.validation.constants.scoring import CONFIDENCE_PERCENT_SCALE, MAX_EVIDENCE_ANCHORS` at source line 22: `source_detail/vvaharness/validation/constants/scoring.py.sudo.md`.
- `from vvaharness.validation.models.scoring import RawCriterion, RawExtra, ScoreResult` at source line 26: `source_detail/vvaharness/validation/models/scoring.py.sudo.md`.
