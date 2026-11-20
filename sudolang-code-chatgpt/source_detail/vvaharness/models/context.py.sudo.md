# vvaharness/models/context.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/models/context.py.evidence.json`. SHA-256: `fb22f9409eecc3f908aede8d42faf210d352f9c1418e50a1b7cdf475a6c8bc7d`.

```sudo
// Source: vvaharness/models/context.py:15-23
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from collections.abc import Iterable; preserve alias and import-time effects. Then Resolve source import from pydantic import BaseModel, ConfigDict, Field, model_validator; preserve alias and import-time effects. Then Evaluate once ['ScoringPolicy']; assign in source target order to __all__.
// Source: vvaharness/models/context.py:26-59
interface ScoringPolicy {
  Describe the source Python type, preserving its base/metaclass expression order: BaseModel.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/models/context.py:27-35
  In source order: Retain source documentation literal source_literal_27_4; it is not a model call. Then Evaluate once ConfigDict(frozen=True, extra='forbid'); assign in source target order to model_config. Then For required_gates, assign Field(default=(), description='gates a validator must answer'); source annotation tuple[str, ...]. Then For weights, assign Field(default_factory=dict, description='per-gate weight'); source annotation dict[str, float]. Then For critical, assign Field(default=frozenset(), description='gates whose failure caps the verdict'); source annotation frozenset[str].
  // Source: vvaharness/models/context.py:36-39
  In source order: For ready_at, assign Field(default=0.85, description='score at or above which a fix is ready'); source annotation float. Then For conditional_at, assign Field(default=0.6, description='score at or above which a fix is ready with conditions'); source annotation float.
  // Source: vvaharness/models/context.py:42-51
  // Source: vvaharness/models/context.py:41-41
  Before creating this callable, evaluate and retain decorators top-to-bottom: model_validator(mode='after').
  // Source: vvaharness/models/context.py:42-51
  // Source signature: _gates_and_weights_agree(self) -> ScoringPolicy
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _gates_and_weights_agree(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/models/context.py:43-43
    In source order: Retain source documentation literal source_literal_43_8; it is not a model call.
    // Source: vvaharness/models/context.py:44-50
    if (the source predicate set(self.required_gates) != set(self.weights) is truthy) {
      // Source: vvaharness/models/context.py:45-49
      In source order: Evaluate once sorted(set(self.required_gates) - set(self.weights)); assign in source target order to only_required. Then Evaluate once sorted(set(self.weights) - set(self.required_gates)); assign in source target order to only_weighted. Then Evaluate once source_template_47_19; assign in source target order to msg.
      // Source: vvaharness/models/context.py:50-50
      Raise ValueError(msg).
    }
    // Source: vvaharness/models/context.py:51-51
    End this invocation with self.
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vvaharness/models/context.py:53-59
  // Source signature: missing_from(self, gate_names: Iterable[str]) -> tuple[str, ...]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn missing_from(self, gate_names) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/models/context.py:54-57
    In source order: Retain source documentation literal source_literal_54_8; it is not a model call. Then Resolve source import from vvaharness.models.vocab import normalise_gate_name; preserve alias and import-time effects. Then Evaluate once {normalise_gate_name(n) for n in gate_names}; assign in source target order to answered.
    // Source: vvaharness/models/context.py:58-59
    End this invocation with tuple((g for g in self.required_gates if normalise_gate_name(g) not in answered)).
    If execution reaches this end, finish with the source implicit None result.
  }
}
```

## Local import links

- `from vvaharness.models.vocab import normalise_gate_name` at source line 55: `source_detail/vvaharness/models/vocab.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../prompt_representation/vvaharness/models/context.py.sudo.md). Exact strings in the evidence asset support this conversion.
