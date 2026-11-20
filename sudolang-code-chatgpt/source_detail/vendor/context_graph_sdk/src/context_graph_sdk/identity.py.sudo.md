# vendor/context_graph_sdk/src/context_graph_sdk/identity.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vendor/context_graph_sdk/src/context_graph_sdk/identity.py.evidence.json`. SHA-256: `e66dd4586d5fa79b4e15db76b531fa148f2670f8dd91542cd7c9fb7d872f97ef`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/identity.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import hashlib; preserve alias and import-time effects. Then Resolve source import import re; preserve alias and import-time effects. Then Resolve source import from dataclasses import dataclass; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/identity.py:23-25
In source order: Resolve source import from .errors import ModelValidationError; preserve alias and import-time effects. Then Evaluate once re.compile('^[A-Za-z0-9][A-Za-z0-9._-]*$'); assign in source target order to _ID_PATTERN.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/identity.py:28-33
// Source signature: _validate_named_id(value: str, kind: str, maximum: int=128) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _validate_named_id(value, kind, maximum) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/identity.py:29-30
  if (the source predicate not value or len(value) > maximum is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/identity.py:30-30
    Raise ModelValidationError(source_template_30_35).
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/identity.py:31-32
  if (the source predicate not _ID_PATTERN.fullmatch(value) is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/identity.py:32-32
    Raise ModelValidationError(source_template_32_35).
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/identity.py:33-33
  End this invocation with value.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/identity.py:37-44
// Source: vendor/context_graph_sdk/src/context_graph_sdk/identity.py:36-36
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True, order=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/identity.py:37-44
interface ProjectId {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/identity.py:38-38
  In source order: For value, declare without assigning a value; source annotation str.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/identity.py:40-41
  // Source signature: __post_init__(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __post_init__(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/identity.py:41-41
    In source order: Evaluate _validate_named_id(self.value, 'project_id'); retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/identity.py:43-44
  // Source signature: __str__(self) -> str
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __str__(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/identity.py:44-44
    End this invocation with self.value.
    If execution reaches this end, finish with the source implicit None result.
  }
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/identity.py:48-55
// Source: vendor/context_graph_sdk/src/context_graph_sdk/identity.py:47-47
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True, order=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/identity.py:48-55
interface SnapshotId {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/identity.py:49-49
  In source order: For value, declare without assigning a value; source annotation str.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/identity.py:51-52
  // Source signature: __post_init__(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __post_init__(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/identity.py:52-52
    In source order: Evaluate _validate_named_id(self.value, 'snapshot_id'); retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/identity.py:54-55
  // Source signature: __str__(self) -> str
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __str__(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/identity.py:55-55
    End this invocation with self.value.
    If execution reaches this end, finish with the source implicit None result.
  }
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/identity.py:58-61
// Source signature: validate_local_id(local_id: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn validate_local_id(local_id) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/identity.py:59-60
  if (the source predicate not local_id or len(local_id) > 512 is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/identity.py:60-60
    Raise ModelValidationError('local_id must contain 1..512 characters').
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/identity.py:61-61
  End this invocation with local_id.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/identity.py:64-71
// Source signature: _sha256(namespace: str, *components: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _sha256(namespace, components) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/identity.py:65-66
  In source order: Evaluate once hashlib.sha256(); assign in source target order to digest. Then Evaluate digest.update(namespace.encode()); retain side effects and discard the expression result.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/identity.py:67-70
  for each component in components {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/identity.py:68-70
    In source order: Evaluate once component.encode(); assign in source target order to encoded. Then Evaluate digest.update(len(encoded).to_bytes(8, 'big')); retain side effects and discard the expression result. Then Evaluate digest.update(encoded); retain side effects and discard the expression result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/identity.py:71-71
  End this invocation with digest.hexdigest().
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/identity.py:74-78
// Source signature: make_local_id(kind: str, *components: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn make_local_id(kind, components) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/identity.py:75-75
  In source order: Evaluate _validate_named_id(kind, 'identity kind', 64); retain side effects and discard the expression result.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/identity.py:76-77
  if (the source predicate not components is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/identity.py:77-77
    Raise ModelValidationError('local identity requires string components').
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/identity.py:78-78
  End this invocation with _sha256(source_template_78_19, *components).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/identity.py:81-82
// Source signature: make_global_id(project_id: ProjectId, local_id: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn make_global_id(project_id, local_id) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/identity.py:82-82
  End this invocation with _sha256('global-node', project_id.value, validate_local_id(local_id)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/identity.py:85-96
// Source signature: make_edge_id(project_id: ProjectId, source_id: str, relationship_type: str, target_id: str, discriminator: str='') -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn make_edge_id(project_id, source_id, relationship_type, target_id, discriminator) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/identity.py:92-93
  if (the source predicate not all((value for value in (source_id, relationship_type, target_id))) is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/identity.py:93-93
    Raise ModelValidationError('edge identity requires non-empty endpoint and type values').
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/identity.py:94-96
  End this invocation with _sha256('local-edge', project_id.value, source_id, relationship_type, target_id, discriminator).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from .errors import ModelValidationError` at source line 23: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/errors.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../../prompt_representation/vendor/context_graph_sdk/src/context_graph_sdk/identity.py.sudo.md). Exact strings in the evidence asset support this conversion.
