# vvaharness/models/vocab.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/models/vocab.py.evidence.json`. SHA-256: `db1aeb2a47cff972709b46e511505e141f9b395b4968c4945ff5013fd3846a33`.

```sudo
// Source: vvaharness/models/vocab.py:15-37
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from enum import Enum, StrEnum; preserve alias and import-time effects. Then Resolve source import from typing import Final; preserve alias and import-time effects. Then Evaluate once ['CANONICAL_GATE_NAMES', 'EVIDENCE_GATES', 'FIX_VALIDATION_GATES', 'OFFENSIVE_LABELS', 'CaseState', 'Decision', 'Disposition', 'GateStatus', 'MergeReadiness', 'RemediationKind', 'RemediationOutcome', 'Severity', 'VulnClass', 'normalise_gate_name']; assign in source target order to __all__.
// Source: vvaharness/models/vocab.py:40-44
// Source signature: _fold(value: object) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _fold(value) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/models/vocab.py:41-41
  In source order: Retain source documentation literal source_literal_41_4; it is not a model call.
  // Source: vvaharness/models/vocab.py:42-43
  if (the source predicate not isinstance(value, str) is truthy) {
    // Source: vvaharness/models/vocab.py:43-43
    End this invocation with None.
  }
  // Source: vvaharness/models/vocab.py:44-44
  End this invocation with value.strip().casefold().replace('-', '_').replace(' ', '_').
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/models/vocab.py:47-60
interface Severity {
  Describe the source Python type, preserving its base/metaclass expression order: str, Enum.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/models/vocab.py:48-53
  In source order: Retain source documentation literal source_literal_48_4; it is not a model call. Then Evaluate once 'critical'; assign in source target order to CRITICAL. Then Evaluate once 'high'; assign in source target order to HIGH. Then Evaluate once 'medium'; assign in source target order to MEDIUM. Then Evaluate once 'low'; assign in source target order to LOW.
  // Source: vvaharness/models/vocab.py:54-54
  In source order: Evaluate once 'info'; assign in source target order to INFO.
  // Source: vvaharness/models/vocab.py:57-60
  // Source: vvaharness/models/vocab.py:56-56
  Before creating this callable, evaluate and retain decorators top-to-bottom: classmethod.
  // Source: vvaharness/models/vocab.py:57-60
  // Source signature: _missing_(cls, value: object) -> Severity | None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _missing_(cls, value) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/models/vocab.py:58-59
    In source order: Retain source documentation literal source_literal_58_8; it is not a model call. Then Evaluate once _fold(value); assign in source target order to folded.
    // Source: vvaharness/models/vocab.py:60-60
    End this invocation with next((m for m in cls if m.value == folded), None).
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
}
// Source: vvaharness/models/vocab.py:64-73
In source order: For SEV_RANK, assign {s: i for i, s in enumerate(Severity)}; source annotation Final[dict[Severity, int]]. Then For OFFENSIVE_LABELS, assign {'P1': 'Externally Exploitable, No Auth', 'P2': 'Externally Exploitable, Obtainable Auth', 'P3': 'Internal Network / Privileged Position', 'P4': 'Code-Knowledge / Insider Dependent'}; source annotation Final[dict[str, str]].
// Source: vvaharness/models/vocab.py:76-101
interface VulnClass {
  Describe the source Python type, preserving its base/metaclass expression order: str, Enum.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/models/vocab.py:77-82
  In source order: Retain source documentation literal source_literal_77_4; it is not a model call. Then Evaluate once 'use-after-free'; assign in source target order to UAF. Then Evaluate once 'heap-overflow'; assign in source target order to HEAP_OVERFLOW. Then Evaluate once 'stack-overflow'; assign in source target order to STACK_OVERFLOW. Then Evaluate once 'format-string'; assign in source target order to FMT_STRING.
  // Source: vvaharness/models/vocab.py:83-87
  In source order: Evaluate once 'integer-overflow'; assign in source target order to INT_OVERFLOW. Then Evaluate once 'type-confusion'; assign in source target order to TYPE_CONFUSION. Then Evaluate once 'race-condition'; assign in source target order to RACE. Then Evaluate once 'injection'; assign in source target order to INJECTION. Then Evaluate once 'unsafe-deserialization'; assign in source target order to DESERIALIZATION.
  // Source: vvaharness/models/vocab.py:88-90
  In source order: Evaluate once 'logic-flaw'; assign in source target order to LOGIC. Then Evaluate once 'info-leak'; assign in source target order to INFO_LEAK. Then Evaluate once 'other'; assign in source target order to OTHER.
  // Source: vvaharness/models/vocab.py:93-101
  // Source: vvaharness/models/vocab.py:92-92
  Before creating this callable, evaluate and retain decorators top-to-bottom: classmethod.
  // Source: vvaharness/models/vocab.py:93-101
  // Source signature: _missing_(cls, value: object) -> VulnClass
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _missing_(cls, value) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/models/vocab.py:94-95
    In source order: Retain source documentation literal source_literal_94_8; it is not a model call. Then Evaluate once _fold(value); assign in source target order to folded.
    // Source: vvaharness/models/vocab.py:96-97
    if (the source predicate folded is None is truthy) {
      // Source: vvaharness/models/vocab.py:97-97
      End this invocation with cls.OTHER.
    }
    // Source: vvaharness/models/vocab.py:98-100
    for each member in cls {
      // Source: vvaharness/models/vocab.py:99-100
      if (the source predicate member.value.replace('-', '_') == folded is truthy) {
        // Source: vvaharness/models/vocab.py:100-100
        End this invocation with member.
      }
    }
    // Source: vvaharness/models/vocab.py:101-101
    End this invocation with cls.OTHER.
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
}
// Source: vvaharness/models/vocab.py:104-111
interface RemediationKind {
  Describe the source Python type, preserving its base/metaclass expression order: StrEnum.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/models/vocab.py:105-110
  In source order: Retain source documentation literal source_literal_105_4; it is not a model call. Then Evaluate once 'edits_applied'; assign in source target order to EDITS_APPLIED. Then Evaluate once 'diff_proposed'; assign in source target order to DIFF_PROPOSED. Then Evaluate once 'pull_request'; assign in source target order to PULL_REQUEST. Then Evaluate once 'no_action'; assign in source target order to NO_ACTION.
  // Source: vvaharness/models/vocab.py:111-111
  In source order: Evaluate once 'already_resolved'; assign in source target order to ALREADY_RESOLVED.
}
// Source: vvaharness/models/vocab.py:114-122
interface RemediationOutcome {
  Describe the source Python type, preserving its base/metaclass expression order: StrEnum.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/models/vocab.py:115-120
  In source order: Retain source documentation literal source_literal_115_4; it is not a model call. Then Evaluate once 'fixed'; assign in source target order to FIXED. Then Evaluate once 'partially_fixed'; assign in source target order to PARTIALLY_FIXED. Then Evaluate once 'not_fixed'; assign in source target order to NOT_FIXED. Then Evaluate once 'false_positive'; assign in source target order to FALSE_POSITIVE.
  // Source: vvaharness/models/vocab.py:121-122
  In source order: Evaluate once 'needs_review'; assign in source target order to NEEDS_REVIEW. Then Evaluate once 'denied'; assign in source target order to DENIED.
}
// Source: vvaharness/models/vocab.py:125-131
interface Disposition {
  Describe the source Python type, preserving its base/metaclass expression order: StrEnum.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/models/vocab.py:126-131
  In source order: Retain source documentation literal source_literal_126_4; it is not a model call. Then Evaluate once 'false_positive'; assign in source target order to FALSE_POSITIVE. Then Evaluate once 'policy_denied'; assign in source target order to POLICY_DENIED. Then Evaluate once 'accepted_risk'; assign in source target order to ACCEPTED_RISK. Then Evaluate once 'not_applicable'; assign in source target order to NOT_APPLICABLE.
}
// Source: vvaharness/models/vocab.py:134-148
interface Decision {
  Describe the source Python type, preserving its base/metaclass expression order: StrEnum.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/models/vocab.py:135-140
  In source order: Retain source documentation literal source_literal_135_4; it is not a model call. Then Evaluate once 'fixed'; assign in source target order to FIXED. Then Evaluate once 'partially_fixed'; assign in source target order to PARTIALLY_FIXED. Then Evaluate once 'not_fixed'; assign in source target order to NOT_FIXED. Then Evaluate once 'inconclusive'; assign in source target order to INCONCLUSIVE.
  // Source: vvaharness/models/vocab.py:143-148
  // Source: vvaharness/models/vocab.py:142-142
  Before creating this callable, evaluate and retain decorators top-to-bottom: classmethod.
  // Source: vvaharness/models/vocab.py:143-148
  // Source signature: _missing_(cls, value: object) -> Decision
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _missing_(cls, value) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/models/vocab.py:144-145
    In source order: Retain source documentation literal source_literal_144_8; it is not a model call. Then Evaluate once _fold(value); assign in source target order to folded.
    // Source: vvaharness/models/vocab.py:146-147
    if (the source predicate folded is None is truthy) {
      // Source: vvaharness/models/vocab.py:147-147
      End this invocation with cls.INCONCLUSIVE.
    }
    // Source: vvaharness/models/vocab.py:148-148
    End this invocation with next((m for m in cls if m.value == folded), cls.INCONCLUSIVE).
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
}
// Source: vvaharness/models/vocab.py:151-166
interface GateStatus {
  Describe the source Python type, preserving its base/metaclass expression order: StrEnum.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/models/vocab.py:152-157
  In source order: Retain source documentation literal source_literal_152_4; it is not a model call. Then Evaluate once 'pass'; assign in source target order to PASS. Then Evaluate once 'partial'; assign in source target order to PARTIAL. Then Evaluate once 'fail'; assign in source target order to FAIL. Then Evaluate once 'skip'; assign in source target order to SKIP.
  // Source: vvaharness/models/vocab.py:158-158
  In source order: Evaluate once 'invalid'; assign in source target order to INVALID.
  // Source: vvaharness/models/vocab.py:161-166
  // Source: vvaharness/models/vocab.py:160-160
  Before creating this callable, evaluate and retain decorators top-to-bottom: classmethod.
  // Source: vvaharness/models/vocab.py:161-166
  // Source signature: _missing_(cls, value: object) -> GateStatus
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _missing_(cls, value) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/models/vocab.py:162-163
    In source order: Retain source documentation literal source_literal_162_8; it is not a model call. Then Evaluate once _fold(value); assign in source target order to folded.
    // Source: vvaharness/models/vocab.py:164-165
    if (the source predicate folded is None is truthy) {
      // Source: vvaharness/models/vocab.py:165-165
      End this invocation with cls.INVALID.
    }
    // Source: vvaharness/models/vocab.py:166-166
    End this invocation with next((m for m in cls if m.value == folded), cls.INVALID).
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
}
// Source: vvaharness/models/vocab.py:169-177
interface CaseState {
  Describe the source Python type, preserving its base/metaclass expression order: StrEnum.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/models/vocab.py:170-175
  In source order: Retain source documentation literal source_literal_170_4; it is not a model call. Then Evaluate once 'open'; assign in source target order to OPEN. Then Evaluate once 'remediated'; assign in source target order to REMEDIATED. Then Evaluate once 'validated'; assign in source target order to VALIDATED. Then Evaluate once 'failed'; assign in source target order to FAILED.
  // Source: vvaharness/models/vocab.py:176-177
  In source order: Evaluate once 'declined'; assign in source target order to DECLINED. Then Evaluate once 'pending'; assign in source target order to PENDING.
}
// Source: vvaharness/models/vocab.py:180-185
interface MergeReadiness {
  Describe the source Python type, preserving its base/metaclass expression order: StrEnum.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/models/vocab.py:181-185
  In source order: Retain source documentation literal source_literal_181_4; it is not a model call. Then Evaluate once 'ready'; assign in source target order to READY. Then Evaluate once 'ready_with_conditions'; assign in source target order to READY_WITH_CONDITIONS. Then Evaluate once 'not_ready'; assign in source target order to NOT_READY.
}
// Source: vvaharness/models/vocab.py:189-200
In source order: For EVIDENCE_GATES, assign ('source', 'sink', 'missing_control'); source annotation Final[tuple[str, ...]]. Then For FIX_VALIDATION_GATES, assign ('root_cause', 'instance_coverage', 'no_new_vulnerabilities', 'security_best_practices'); source annotation Final[tuple[str, ...]]. Then For CANONICAL_GATE_NAMES, assign EVIDENCE_GATES + FIX_VALIDATION_GATES; source annotation Final[tuple[str, ...]].
// Source: vvaharness/models/vocab.py:203-205
// Source signature: normalise_gate_name(value: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn normalise_gate_name(value) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/models/vocab.py:204-204
  In source order: Retain source documentation literal source_literal_204_4; it is not a model call.
  // Source: vvaharness/models/vocab.py:205-205
  End this invocation with _fold(value) or ''.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

No statically resolved in-checkout import; external calls remain explicit dependency boundaries.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../prompt_representation/vvaharness/models/vocab.py.sudo.md). Exact strings in the evidence asset support this conversion.
