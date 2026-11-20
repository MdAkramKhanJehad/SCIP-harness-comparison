# vvaharness/models/case.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/models/case.py.evidence.json`. SHA-256: `f3dfd556d162eebbfee1371c959784307b5dec8e79fd0422b1d88322d055cc1e`.

```sudo
// Source: vvaharness/models/case.py:15-22
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import json; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from pydantic import BaseModel, ConfigDict, Field, computed_field, model_validator; preserve alias and import-time effects.
// Source: vvaharness/models/case.py:24-28
In source order: Resolve source import from vvaharness.models.derive import state_of; preserve alias and import-time effects. Then Resolve source import from vvaharness.models.remediation import Remediation; preserve alias and import-time effects. Then Resolve source import from vvaharness.models.scan import Finding; preserve alias and import-time effects. Then Resolve source import from vvaharness.models.verdict import Verdict; preserve alias and import-time effects. Then Resolve source import from vvaharness.models.vocab import CaseState; preserve alias and import-time effects.
// Source: vvaharness/models/case.py:30-33
In source order: Evaluate once ['Attempt', 'FindingCase']; assign in source target order to __all__. Then Evaluate once '2.0'; assign in source target order to SCHEMA_VERSION.
// Source: vvaharness/models/case.py:36-47
interface Attempt {
  Describe the source Python type, preserving its base/metaclass expression order: BaseModel.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/models/case.py:37-44
  In source order: Retain source documentation literal source_literal_37_4; it is not a model call. Then Evaluate once ConfigDict(frozen=True, extra='ignore'); assign in source target order to model_config. Then For ordinal, assign Field(description='1-based position in the sequence'); source annotation int. Then For remediation, assign Field(description='what was attempted'); source annotation Remediation. Then For verdict, assign Field(default=None, description='None until validated'); source annotation Verdict | None.
  // Source: vvaharness/models/case.py:45-47
  In source order: For reverted_paths, assign Field(default=(), description='paths the harness rolled back after a policy breach'); source annotation tuple[str, ...].
}
// Source: vvaharness/models/case.py:50-110
interface FindingCase {
  Describe the source Python type, preserving its base/metaclass expression order: BaseModel.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/models/case.py:51-58
  In source order: Retain source documentation literal source_literal_51_4; it is not a model call. Then Evaluate once ConfigDict(frozen=True, extra='ignore'); assign in source target order to model_config. Then For schema_version, assign Field(default=SCHEMA_VERSION, description='persisted shape version'); source annotation str. Then For case_id, assign Field(description='stable identity, assigned once per (repo, finding)'); source annotation str. Then For finding, assign Field(description='what was found'); source annotation Finding.
  // Source: vvaharness/models/case.py:59-62
  In source order: For attempts, assign Field(default=(), description='ordered, possibly multi-engine'); source annotation tuple[Attempt, ...]. Then For superseded_ids, assign Field(default=(), description='earlier ids reconciled into this case'); source annotation tuple[str, ...].
  // Source: vvaharness/models/case.py:66-68
  // Source: vvaharness/models/case.py:64-65
  Before creating this callable, evaluate and retain decorators top-to-bottom: computed_field, property.
  // Source: vvaharness/models/case.py:66-68
  // Source signature: state(self) -> CaseState
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn state(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/models/case.py:67-67
    In source order: Retain source documentation literal source_literal_67_8; it is not a model call.
    // Source: vvaharness/models/case.py:68-68
    End this invocation with state_of(self.attempts).
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vvaharness/models/case.py:72-76
  // Source: vvaharness/models/case.py:70-71
  Before creating this callable, evaluate and retain decorators top-to-bottom: model_validator(mode='before'), classmethod.
  // Source: vvaharness/models/case.py:72-76
  // Source signature: _drop_derived(cls, data: object) -> object
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _drop_derived(cls, data) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/models/case.py:73-73
    In source order: Retain source documentation literal source_literal_73_8; it is not a model call.
    // Source: vvaharness/models/case.py:74-75
    if (the source predicate isinstance(data, dict) is truthy) {
      // Source: vvaharness/models/case.py:75-75
      End this invocation with {k: v for k, v in data.items() if k != 'state'}.
    }
    // Source: vvaharness/models/case.py:76-76
    End this invocation with data.
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vvaharness/models/case.py:78-90
  // Source signature: with_attempt(self, remediation: Remediation, *, reverted_paths: tuple[str, ...]=()) -> FindingCase
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn with_attempt(self, remediation, reverted_paths) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/models/case.py:84-89
    In source order: Retain source documentation literal source_literal_84_8; it is not a model call. Then Evaluate once Attempt(ordinal=len(self.attempts) + 1, remediation=remediation, reverted_paths=reverted_paths); assign in source target order to attempt.
    // Source: vvaharness/models/case.py:90-90
    End this invocation with self.model_copy(update={'attempts': (*self.attempts, attempt)}).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/models/case.py:92-98
  // Source signature: with_verdict(self, verdict: Verdict) -> FindingCase
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn with_verdict(self, verdict) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/models/case.py:93-93
    In source order: Retain source documentation literal source_literal_93_8; it is not a model call.
    // Source: vvaharness/models/case.py:94-96
    if (the source predicate not self.attempts is truthy) {
      // Source: vvaharness/models/case.py:95-95
      In source order: Evaluate once source_template_95_18; assign in source target order to msg.
      // Source: vvaharness/models/case.py:96-96
      Raise ValueError(msg).
    }
    // Source: vvaharness/models/case.py:97-97
    In source order: Evaluate once self.attempts[-1].model_copy(update={'verdict': verdict}); assign in source target order to judged.
    // Source: vvaharness/models/case.py:98-98
    End this invocation with self.model_copy(update={'attempts': (*self.attempts[:-1], judged)}).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/models/case.py:101-103
  // Source: vvaharness/models/case.py:100-100
  Before creating this callable, evaluate and retain decorators top-to-bottom: classmethod.
  // Source: vvaharness/models/case.py:101-103
  // Source signature: read(cls, path: Path) -> FindingCase
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn read(cls, path) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/models/case.py:102-102
    In source order: Retain source documentation literal source_literal_102_8; it is not a model call.
    // Source: vvaharness/models/case.py:103-103
    End this invocation with cls.model_validate(_read_json(path)).
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vvaharness/models/case.py:105-110
  // Source signature: write(self, path: Path) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn write(self, path) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/models/case.py:106-110
    In source order: Retain source documentation literal source_literal_106_8; it is not a model call. Then Evaluate once json.dumps(self.model_dump(mode='json'), indent=2) + source_literal_107_71; assign in source target order to payload. Then Evaluate once path.with_suffix(source_template_108_31); assign in source target order to tmp. Then Evaluate tmp.write_text(payload, encoding='utf-8'); retain side effects and discard the expression result. Then Evaluate tmp.replace(path); retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vvaharness/models/case.py:113-119
// Source signature: _read_json(path: Path) -> object
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _read_json(path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/models/case.py:114-114
  In source order: Retain source documentation literal source_literal_114_4; it is not a model call.
  // Source: vvaharness/models/case.py:115-119
  Perform the following protected operations {
    // Source: vvaharness/models/case.py:116-116
    End this invocation with json.loads(path.read_text(encoding='utf-8')).
  }
  // Source: vvaharness/models/case.py:117-119
  On the first matching source exception json.JSONDecodeError as exc, in handler order {
    // Source: vvaharness/models/case.py:118-118
    In source order: Evaluate once source_template_118_14; assign in source target order to msg.
    // Source: vvaharness/models/case.py:119-119
    Raise ValueError(msg) with explicit source cause exc.
  }
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.models.derive import state_of` at source line 24: `source_detail/vvaharness/models/derive.py.sudo.md`.
- `from vvaharness.models.remediation import Remediation` at source line 25: `source_detail/vvaharness/models/remediation.py.sudo.md`.
- `from vvaharness.models.scan import Finding` at source line 26: `source_detail/vvaharness/models/scan/__init__.py.sudo.md`.
- `from vvaharness.models.verdict import Verdict` at source line 27: `source_detail/vvaharness/models/verdict.py.sudo.md`.
- `from vvaharness.models.vocab import CaseState` at source line 28: `source_detail/vvaharness/models/vocab.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../prompt_representation/vvaharness/models/case.py.sudo.md). Exact strings in the evidence asset support this conversion.
