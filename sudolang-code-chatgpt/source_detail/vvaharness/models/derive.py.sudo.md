# vvaharness/models/derive.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/models/derive.py.evidence.json`. SHA-256: `48683a7acda864432480eba4b74e2f8878ede2dc8856ce524bde4cd66158937a`.

```sudo
// Source: vvaharness/models/derive.py:15-22
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from collections.abc import Sequence; preserve alias and import-time effects. Then Resolve source import from typing import TYPE_CHECKING, Final; preserve alias and import-time effects. Then Resolve source import from vvaharness.models.context import ScoringPolicy; preserve alias and import-time effects.
// Source: vvaharness/models/derive.py:23-29
In source order: Resolve source import from vvaharness.models.vocab import CaseState, Decision, Disposition, MergeReadiness, RemediationKind; preserve alias and import-time effects.
// Source: vvaharness/models/derive.py:31-33
if (the source predicate TYPE_CHECKING is truthy) {
  // Source: vvaharness/models/derive.py:32-33
  In source order: Resolve source import from vvaharness.models.case import Attempt; preserve alias and import-time effects. Then Resolve source import from vvaharness.models.verdict import Verdict; preserve alias and import-time effects.
}
// Source: vvaharness/models/derive.py:35-57
In source order: Evaluate once ['merge_readiness_for', 'state_of', 'verdict_state']; assign in source target order to __all__. Then For _KIND_STATE, assign {RemediationKind.EDITS_APPLIED: CaseState.REMEDIATED, RemediationKind.DIFF_PROPOSED: CaseState.REMEDIATED, RemediationKind.PULL_REQUEST: CaseState.REMEDIATED, RemediationKind.ALREADY_RESOLVED: CaseState.REMEDIATED, RemediationKind.NO_ACTION: CaseState.DECLINED}; source annotation Final[dict[RemediationKind, CaseState]]. Then For _DECISION_STATE, assign {Decision.FIXED: CaseState.VALIDATED, Decision.PARTIALLY_FIXED: CaseState.FAILED, Decision.NOT_FIXED: CaseState.FAILED, Decision.INCONCLUSIVE: CaseState.OPEN}; source annotation Final[dict[Decision, CaseState]]. Then For _CLOSING, assign frozenset({Disposition.FALSE_POSITIVE, Disposition.ACCEPTED_RISK, Disposition.NOT_APPLICABLE}); source annotation Final[frozenset[Disposition]].
// Source: vvaharness/models/derive.py:60-66
// Source signature: verdict_state(verdict: Verdict) -> CaseState
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn verdict_state(verdict) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/models/derive.py:61-61
  In source order: Retain source documentation literal source_literal_61_4; it is not a model call.
  // Source: vvaharness/models/derive.py:62-63
  if (the source predicate verdict.ticket is not None is truthy) {
    // Source: vvaharness/models/derive.py:63-63
    End this invocation with CaseState.PENDING.
  }
  // Source: vvaharness/models/derive.py:64-65
  if (the source predicate verdict.disposition in _CLOSING is truthy) {
    // Source: vvaharness/models/derive.py:65-65
    End this invocation with CaseState.DECLINED.
  }
  // Source: vvaharness/models/derive.py:66-66
  End this invocation with _DECISION_STATE[verdict.decision].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/models/derive.py:69-73
// Source signature: _attempt_state(attempt: Attempt) -> CaseState
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _attempt_state(attempt) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/models/derive.py:70-70
  In source order: Retain source documentation literal source_literal_70_4; it is not a model call.
  // Source: vvaharness/models/derive.py:71-72
  if (the source predicate attempt.verdict is None is truthy) {
    // Source: vvaharness/models/derive.py:72-72
    End this invocation with _KIND_STATE[attempt.remediation.kind].
  }
  // Source: vvaharness/models/derive.py:73-73
  End this invocation with verdict_state(attempt.verdict).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/models/derive.py:76-80
// Source signature: state_of(attempts: Sequence[Attempt]) -> CaseState
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn state_of(attempts) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/models/derive.py:77-77
  In source order: Retain source documentation literal source_literal_77_4; it is not a model call.
  // Source: vvaharness/models/derive.py:78-79
  if (the source predicate not attempts is truthy) {
    // Source: vvaharness/models/derive.py:79-79
    End this invocation with CaseState.OPEN.
  }
  // Source: vvaharness/models/derive.py:80-80
  End this invocation with _attempt_state(attempts[-1]).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/models/derive.py:83-89
// Source signature: _readiness_for_score(score: float, policy: ScoringPolicy) -> MergeReadiness
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _readiness_for_score(score, policy) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/models/derive.py:84-84
  In source order: Retain source documentation literal source_literal_84_4; it is not a model call.
  // Source: vvaharness/models/derive.py:85-86
  if (the source predicate score >= policy.ready_at is truthy) {
    // Source: vvaharness/models/derive.py:86-86
    End this invocation with MergeReadiness.READY.
  }
  // Source: vvaharness/models/derive.py:87-88
  if (the source predicate score >= policy.conditional_at is truthy) {
    // Source: vvaharness/models/derive.py:88-88
    End this invocation with MergeReadiness.READY_WITH_CONDITIONS.
  }
  // Source: vvaharness/models/derive.py:89-89
  End this invocation with MergeReadiness.NOT_READY.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/models/derive.py:93-105
In source order: For _DECISION_READINESS, assign {Decision.FIXED: MergeReadiness.READY, Decision.PARTIALLY_FIXED: MergeReadiness.READY_WITH_CONDITIONS, Decision.NOT_FIXED: MergeReadiness.NOT_READY, Decision.INCONCLUSIVE: MergeReadiness.NOT_READY}; source annotation Final[dict[Decision, MergeReadiness]]. Then For _RANK, assign {MergeReadiness.NOT_READY: 0, MergeReadiness.READY_WITH_CONDITIONS: 1, MergeReadiness.READY: 2}; source annotation Final[dict[MergeReadiness, int]].
// Source: vvaharness/models/derive.py:108-110
// Source signature: _lowest(*readiness: MergeReadiness) -> MergeReadiness
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _lowest(readiness) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/models/derive.py:109-109
  In source order: Retain source documentation literal source_literal_109_4; it is not a model call.
  // Source: vvaharness/models/derive.py:110-110
  End this invocation with min(readiness, key=_RANK.__getitem__).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/models/derive.py:113-122
// Source signature: merge_readiness_for(verdict: Verdict, policy: ScoringPolicy | None=None) -> MergeReadiness
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn merge_readiness_for(verdict, policy) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/models/derive.py:116-117
  In source order: Retain source documentation literal source_literal_116_4; it is not a model call. Then Evaluate once _DECISION_READINESS[verdict.decision]; assign in source target order to ceiling.
  // Source: vvaharness/models/derive.py:118-119
  if (the source predicate verdict.conditions is truthy) {
    // Source: vvaharness/models/derive.py:119-119
    In source order: Evaluate once _lowest(ceiling, MergeReadiness.READY_WITH_CONDITIONS); assign in source target order to ceiling.
  }
  // Source: vvaharness/models/derive.py:120-121
  if (the source predicate verdict.score is None is truthy) {
    // Source: vvaharness/models/derive.py:121-121
    End this invocation with ceiling.
  }
  // Source: vvaharness/models/derive.py:122-122
  End this invocation with _lowest(ceiling, _readiness_for_score(verdict.score, policy or ScoringPolicy())).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.models.context import ScoringPolicy` at source line 22: `source_detail/vvaharness/models/context.py.sudo.md`.
- `from vvaharness.models.vocab import CaseState, Decision, Disposition, MergeReadiness, RemediationKind` at source line 23: `source_detail/vvaharness/models/vocab.py.sudo.md`.
- `from vvaharness.models.case import Attempt` at source line 32: `source_detail/vvaharness/models/case.py.sudo.md`.
- `from vvaharness.models.verdict import Verdict` at source line 33: `source_detail/vvaharness/models/verdict.py.sudo.md`.
