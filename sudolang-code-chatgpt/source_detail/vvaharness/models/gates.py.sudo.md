# vvaharness/models/gates.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/models/gates.py.evidence.json`. SHA-256: `11b0bf8fb0436bca6bbeffd102293c82d5e15883132b8cb52f481108c7af2279`.

```sudo
// Source: vvaharness/models/gates.py:15-23
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from pydantic import BaseModel, ConfigDict, Field, field_validator; preserve alias and import-time effects. Then Resolve source import from vvaharness.models.vocab import GateStatus, normalise_gate_name; preserve alias and import-time effects. Then Evaluate once ['EvidenceAnchor', 'GateAssessment']; assign in source target order to __all__.
// Source: vvaharness/models/gates.py:26-40
interface EvidenceAnchor {
  Describe the source Python type, preserving its base/metaclass expression order: BaseModel.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/models/gates.py:27-34
  In source order: Retain source documentation literal source_literal_27_4; it is not a model call. Then Evaluate once ConfigDict(frozen=True, extra='ignore'); assign in source target order to model_config. Then For file, assign Field(default='', description='repo-relative path'); source annotation str. Then For line, assign Field(default=None, description='1-indexed line, when anchored'); source annotation int | None. Then For snippet, assign Field(default='', description='the cited source text'); source annotation str.
  // Source: vvaharness/models/gates.py:38-40
  // Source: vvaharness/models/gates.py:36-37
  Before creating this callable, evaluate and retain decorators top-to-bottom: field_validator('file', 'snippet', mode='before'), classmethod.
  // Source: vvaharness/models/gates.py:38-40
  // Source signature: _none_to_empty(cls, value: object) -> object
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _none_to_empty(cls, value) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/models/gates.py:39-39
    In source order: Retain source documentation literal source_literal_39_8; it is not a model call.
    // Source: vvaharness/models/gates.py:40-40
    End this invocation with '' if value is None else value.
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
}
// Source: vvaharness/models/gates.py:43-59
interface GateAssessment {
  Describe the source Python type, preserving its base/metaclass expression order: BaseModel.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/models/gates.py:44-51
  In source order: Retain source documentation literal source_literal_44_4; it is not a model call. Then Evaluate once ConfigDict(frozen=True, extra='ignore'); assign in source target order to model_config. Then For name, assign Field(description='gate identifier; an OPEN vocabulary, so any name is legal'); source annotation str. Then For status, assign Field(default=GateStatus.INVALID, description='the outcome'); source annotation GateStatus. Then For summary, assign Field(default='', description='one-line result'); source annotation str.
  // Source: vvaharness/models/gates.py:52-53
  In source order: For details, assign Field(default='', description='longer reasoning, when supplied'); source annotation str. Then For evidence, assign Field(default=(), description='cited source'); source annotation tuple[EvidenceAnchor, ...].
  // Source: vvaharness/models/gates.py:57-59
  // Source: vvaharness/models/gates.py:55-56
  Before creating this callable, evaluate and retain decorators top-to-bottom: field_validator('name', mode='before'), classmethod.
  // Source: vvaharness/models/gates.py:57-59
  // Source signature: _canonical_name(cls, value: object) -> object
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _canonical_name(cls, value) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/models/gates.py:58-58
    In source order: Retain source documentation literal source_literal_58_8; it is not a model call.
    // Source: vvaharness/models/gates.py:59-59
    End this invocation with normalise_gate_name(value) if isinstance(value, str) else value.
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
}
```

## Local import links

- `from vvaharness.models.vocab import GateStatus, normalise_gate_name` at source line 21: `source_detail/vvaharness/models/vocab.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../prompt_representation/vvaharness/models/gates.py.sudo.md). Exact strings in the evidence asset support this conversion.
