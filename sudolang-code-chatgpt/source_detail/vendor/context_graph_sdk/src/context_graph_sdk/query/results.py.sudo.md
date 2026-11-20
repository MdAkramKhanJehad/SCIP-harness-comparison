# vendor/context_graph_sdk/src/context_graph_sdk/query/results.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vendor/context_graph_sdk/src/context_graph_sdk/query/results.py.evidence.json`. SHA-256: `8de2b25ce8d95d13e8eac2618568f0ce0e1da1a8c6421b9854f7ab2fb272506c`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:15-22
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from dataclasses import dataclass; preserve alias and import-time effects. Then Resolve source import from enum import StrEnum; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.errors import ModelValidationError; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:23-31
In source order: Resolve source import from context_graph_sdk.models import CorrelationEndpointRole, CorrelationType, FrozenMap, NodeRef, ProjectSnapshot; preserve alias and import-time effects. Then Evaluate once 20; assign in source target order to DEFAULT_SYMBOL_CANDIDATE_LIMIT.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:34-36
interface RelationshipDirection {
  Describe the source Python type, preserving its base/metaclass expression order: StrEnum.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:35-36
  In source order: Evaluate once 'incoming'; assign in source target order to INCOMING. Then Evaluate once 'outgoing'; assign in source target order to OUTGOING.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:39-41
interface ImpactDirection {
  Describe the source Python type, preserving its base/metaclass expression order: StrEnum.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:40-41
  In source order: Evaluate once 'upstream'; assign in source target order to UPSTREAM. Then Evaluate once 'downstream'; assign in source target order to DOWNSTREAM.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:45-54
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:44-44
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:45-54
interface SymbolSelector {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:46-48
  In source order: For value, declare without assigning a value; source annotation str. Then For file_path, assign None; source annotation str | None. Then For line, assign None; source annotation int | None.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:50-54
  // Source signature: __post_init__(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __post_init__(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:51-52
    if (the source predicate not self.value is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:52-52
      Raise ModelValidationError('symbol selector value is required').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:53-54
    if (the source predicate self.line is not None and self.line < 0 is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:54-54
      Raise ModelValidationError('symbol selector line cannot be negative').
    }
    If execution reaches this end, finish with the source implicit None result.
  }
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:58-70
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:57-57
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:58-70
interface EntityReference {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:59-63
  In source order: For id, declare without assigning a value; source annotation str. Then For local_id, declare without assigning a value; source annotation str. Then For name, declare without assigning a value; source annotation str. Then For labels, declare without assigning a value; source annotation tuple[str, ...]. Then For file_path, assign None; source annotation str | None.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:64-65
  In source order: For start_line, assign None; source annotation int | None. Then For end_line, assign None; source annotation int | None.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:67-70
  // Source signature: __post_init__(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __post_init__(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:68-69
    if (the source predicate not self.id or not self.local_id or (not self.labels) is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:69-69
      Raise ModelValidationError('entity reference requires id, local_id, and labels').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:70-70
    In source order: Evaluate object.__setattr__(self, 'labels', tuple(sorted(set(self.labels)))); retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:74-81
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:73-73
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:74-81
interface RelationshipGroup {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:75-77
  In source order: For relationship_type, declare without assigning a value; source annotation str. Then For direction, declare without assigning a value; source annotation RelationshipDirection. Then For entities, declare without assigning a value; source annotation tuple[EntityReference, ...].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:79-81
  // Source signature: __post_init__(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __post_init__(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:80-81
    if (the source predicate not self.relationship_type is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:81-81
      Raise ModelValidationError('relationship group type is required').
    }
    If execution reaches this end, finish with the source implicit None result.
  }
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:85-95
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:84-84
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:85-95
interface TraversalPath {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:86-87
  In source order: For nodes, declare without assigning a value; source annotation tuple[EntityReference, ...]. Then For relationships, declare without assigning a value; source annotation tuple[str, ...].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:89-91
  // Source signature: __post_init__(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __post_init__(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:90-91
    if (the source predicate len(self.nodes) < 2 or len(self.relationships) != len(self.nodes) - 1 is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:91-91
      Raise ModelValidationError('traversal path nodes and relationships do not align').
    }
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:94-95
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:93-93
  Before creating this callable, evaluate and retain decorators top-to-bottom: property.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:94-95
  // Source signature: depth(self) -> int
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn depth(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:95-95
    End this invocation with len(self.relationships).
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:99-113
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:98-98
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:99-113
interface ContextLimits {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:100-104
  In source order: For candidate_limit, assign DEFAULT_SYMBOL_CANDIDATE_LIMIT; source annotation int. Then For group_limit, assign 100; source annotation int. Then For call_depth, assign 3; source annotation int. Then For max_nodes, assign 500; source annotation int. Then For max_edges, assign 1000; source annotation int.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:105-105
  In source order: For max_paths, assign 500; source annotation int.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:107-113
  // Source signature: __post_init__(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __post_init__(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:108-112
    In source order: Evaluate _bounded('candidate_limit', self.candidate_limit, 1, 100); retain side effects and discard the expression result. Then Evaluate _bounded('group_limit', self.group_limit, 1, 500); retain side effects and discard the expression result. Then Evaluate _bounded('call_depth', self.call_depth, 0, 10); retain side effects and discard the expression result. Then Evaluate _bounded('max_nodes', self.max_nodes, 1, 5000); retain side effects and discard the expression result. Then Evaluate _bounded('max_edges', self.max_edges, 1, 10000); retain side effects and discard the expression result.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:113-113
    In source order: Evaluate _bounded('max_paths', self.max_paths, 1, 2000); retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:117-129
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:116-116
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:117-129
interface ImpactLimits {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:118-122
  In source order: For candidate_limit, assign DEFAULT_SYMBOL_CANDIDATE_LIMIT; source annotation int. Then For max_depth, assign 3; source annotation int. Then For max_nodes, assign 500; source annotation int. Then For max_edges, assign 1000; source annotation int. Then For max_paths, assign 500; source annotation int.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:124-129
  // Source signature: __post_init__(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __post_init__(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:125-129
    In source order: Evaluate _bounded('candidate_limit', self.candidate_limit, 1, 100); retain side effects and discard the expression result. Then Evaluate _bounded('max_depth', self.max_depth, 1, 10); retain side effects and discard the expression result. Then Evaluate _bounded('max_nodes', self.max_nodes, 1, 5000); retain side effects and discard the expression result. Then Evaluate _bounded('max_edges', self.max_edges, 1, 10000); retain side effects and discard the expression result. Then Evaluate _bounded('max_paths', self.max_paths, 1, 2000); retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:133-141
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:132-132
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:133-141
interface ContextResult {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:134-138
  In source order: For symbol, declare without assigning a value; source annotation EntityReference. Then For callers, declare without assigning a value; source annotation tuple[EntityReference, ...]. Then For callees, declare without assigning a value; source annotation tuple[EntityReference, ...]. Then For imports, declare without assigning a value; source annotation tuple[EntityReference, ...]. Then For implementors, declare without assigning a value; source annotation tuple[EntityReference, ...].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:139-141
  In source order: For processes, declare without assigning a value; source annotation tuple[EntityReference, ...]. Then For relationships, declare without assigning a value; source annotation tuple[RelationshipGroup, ...]. Then For call_paths, declare without assigning a value; source annotation tuple[TraversalPath, ...].
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:145-151
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:144-144
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:145-151
interface CorrelationLimits {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:146-147
  In source order: For candidate_limit, assign DEFAULT_SYMBOL_CANDIDATE_LIMIT; source annotation int. Then For max_results, assign 100; source annotation int.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:149-151
  // Source signature: __post_init__(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __post_init__(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:150-151
    In source order: Evaluate _bounded('candidate_limit', self.candidate_limit, 1, 100); retain side effects and discard the expression result. Then Evaluate _bounded('max_results', self.max_results, 1, 1000); retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:155-166
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:154-154
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:155-166
interface CorrelationMatch {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:156-160
  In source order: For relationship_type, declare without assigning a value; source annotation CorrelationType. Then For source, declare without assigning a value; source annotation NodeRef. Then For target, declare without assigning a value; source annotation NodeRef. Then For queried_endpoint, declare without assigning a value; source annotation CorrelationEndpointRole. Then For related_snapshot, declare without assigning a value; source annotation ProjectSnapshot.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:161-165
  In source order: For provider_name, declare without assigning a value; source annotation str. Then For provider_version, declare without assigning a value; source annotation str. Then For confidence, declare without assigning a value; source annotation float. Then For reason, declare without assigning a value; source annotation str. Then For evidence, declare without assigning a value; source annotation FrozenMap.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:166-166
  In source order: For context, assign None; source annotation ContextResult | None.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:170-172
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:169-169
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:170-172
interface CorrelationResult {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:171-172
  In source order: For source, declare without assigning a value; source annotation EntityReference. Then For matches, declare without assigning a value; source annotation tuple[CorrelationMatch, ...].
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:176-180
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:175-175
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:176-180
interface ImpactResult {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:177-180
  In source order: For symbol, declare without assigning a value; source annotation EntityReference. Then For direction, declare without assigning a value; source annotation ImpactDirection. Then For affected, declare without assigning a value; source annotation tuple[EntityReference, ...]. Then For paths, declare without assigning a value; source annotation tuple[TraversalPath, ...].
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:183-188
// Source signature: entity_sort_key(entity: EntityReference) -> tuple[str, int, str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn entity_sort_key(entity) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:184-188
  End this invocation with (entity.file_path or '', entity.start_line if entity.start_line is not None else -1, entity.id).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:191-193
// Source signature: _bounded(name: str, value: int, minimum: int, maximum: int) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _bounded(name, value, minimum, maximum) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:192-193
  if (the source predicate not minimum <= value <= maximum is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/results.py:193-193
    Raise ModelValidationError(source_template_193_35).
  }
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from context_graph_sdk.errors import ModelValidationError` at source line 22: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/errors.py.sudo.md`.
- `from context_graph_sdk.models import CorrelationEndpointRole, CorrelationType, FrozenMap, NodeRef, ProjectSnapshot` at source line 23: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/models.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../../../prompt_representation/vendor/context_graph_sdk/src/context_graph_sdk/query/results.py.sudo.md). Exact strings in the evidence asset support this conversion.
