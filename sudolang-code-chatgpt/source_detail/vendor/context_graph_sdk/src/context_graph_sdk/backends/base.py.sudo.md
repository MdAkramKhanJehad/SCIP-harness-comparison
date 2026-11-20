# vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py.evidence.json`. SHA-256: `3fcbe3957179fa1eb32aeca5af616fec20ca334e759c3e8efc726c21301a41e0`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from collections.abc import Iterator; preserve alias and import-time effects. Then Resolve source import from contextlib import AbstractContextManager; preserve alias and import-time effects. Then Resolve source import from dataclasses import dataclass; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py:22-36
In source order: Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from typing import Protocol, runtime_checkable; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.identity import ProjectId; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.models import CatalogPublication, CorrelationEdge, FrozenMap, GraphEdge, GraphNode, ProjectSnapshot, ProviderManifest, ResolvedCorrelation, SnapshotLocator; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py:40-44
// Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py:39-39
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True, order=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py:40-44
interface SchemaPattern {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py:41-44
  In source order: For source_label, declare without assigning a value; source annotation str. Then For relationship_type, declare without assigning a value; source annotation str. Then For target_label, declare without assigning a value; source annotation str. Then For count, declare without assigning a value; source annotation int.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py:48-71
// Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py:47-47
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py:48-71
interface GraphSchema {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py:49-53
  In source order: For labels, declare without assigning a value; source annotation tuple[str, ...]. Then For relationship_types, declare without assigning a value; source annotation tuple[str, ...]. Then For node_property_keys, declare without assigning a value; source annotation tuple[str, ...]. Then For relationship_property_keys, assign (); source annotation tuple[str, ...]. Then For patterns, assign (); source annotation tuple[SchemaPattern, ...].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py:54-55
  In source order: For node_count, assign 0; source annotation int. Then For relationship_count, assign 0; source annotation int.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py:57-66
  // Source signature: __post_init__(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __post_init__(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py:58-66
    In source order: Evaluate object.__setattr__(self, 'labels', tuple(sorted(set(self.labels)))); retain side effects and discard the expression result. Then Evaluate object.__setattr__(self, 'relationship_types', tuple(sorted(set(self.relationship_types)))); retain side effects and discard the expression result. Then Evaluate object.__setattr__(self, 'node_property_keys', tuple(sorted(set(self.node_property_keys)))); retain side effects and discard the expression result. Then Evaluate object.__setattr__(self, 'relationship_property_keys', tuple(sorted(set(self.relationship_property_keys)))); retain side effects and discard the expression result. Then Evaluate object.__setattr__(self, 'patterns', tuple(sorted(set(self.patterns)))); retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py:69-71
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py:68-68
  Before creating this callable, evaluate and retain decorators top-to-bottom: property.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py:69-71
  // Source signature: property_keys(self) -> tuple[str, ...]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn property_keys(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py:70-70
    In source order: Retain source documentation literal source_literal_70_8; it is not a model call.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py:71-71
    End this invocation with tuple(sorted(set(self.node_property_keys + self.relationship_property_keys))).
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py:75-84
// Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py:74-74
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: runtime_checkable.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py:75-84
interface GraphWriteTransaction {
  Describe the source Python type, preserving its base/metaclass expression order: Protocol.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py:76-76
  In source order: Retain source documentation literal source_literal_76_4; it is not a model call.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py:78-78
  // Source signature: write_nodes(self, nodes: tuple[GraphNode, ...]) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn write_nodes(self, nodes) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py:78-78
    In source order: Evaluate ...; retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py:80-80
  // Source signature: write_edges(self, edges: tuple[GraphEdge, ...]) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn write_edges(self, edges) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py:80-80
    In source order: Evaluate ...; retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py:82-82
  // Source signature: commit(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn commit(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py:82-82
    In source order: Evaluate ...; retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py:84-84
  // Source signature: rollback(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn rollback(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py:84-84
    In source order: Evaluate ...; retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py:88-95
// Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py:87-87
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: runtime_checkable.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py:88-95
interface CatalogWriteTransaction {
  Describe the source Python type, preserving its base/metaclass expression order: Protocol.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py:89-89
  In source order: Retain source documentation literal source_literal_89_4; it is not a model call.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py:91-91
  // Source signature: publish(self, publication: CatalogPublication) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn publish(self, publication) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py:91-91
    In source order: Evaluate ...; retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py:93-93
  // Source signature: commit(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn commit(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py:93-93
    In source order: Evaluate ...; retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py:95-95
  // Source signature: rollback(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn rollback(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py:95-95
    In source order: Evaluate ...; retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py:99-108
// Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py:98-98
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: runtime_checkable.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py:99-108
interface GraphBackend {
  Describe the source Python type, preserving its base/metaclass expression order: Protocol.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py:100-100
  In source order: Retain source documentation literal source_literal_100_4; it is not a model call.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py:102-102
  // Source signature: begin_write(self) -> AbstractContextManager[GraphWriteTransaction]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn begin_write(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py:102-102
    In source order: Evaluate ...; retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py:104-106
  // Source signature: query_readonly(self, cypher: str, parameters: FrozenMap, row_limit: int) -> Iterator[FrozenMap]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn query_readonly(self, cypher, parameters, row_limit) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py:106-106
    In source order: Evaluate ...; retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py:108-108
  // Source signature: close(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn close(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py:108-108
    In source order: Evaluate ...; retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py:112-129
// Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py:111-111
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: runtime_checkable.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py:112-129
interface CatalogBackend {
  Describe the source Python type, preserving its base/metaclass expression order: GraphBackend, Protocol.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py:113-113
  // Source signature: begin_publication(self) -> AbstractContextManager[CatalogWriteTransaction]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn begin_publication(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py:113-113
    In source order: Evaluate ...; retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py:115-115
  // Source signature: accepted_snapshot(self, project_id: ProjectId) -> ProjectSnapshot | None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn accepted_snapshot(self, project_id) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py:115-115
    In source order: Evaluate ...; retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py:117-117
  // Source signature: accepted_snapshots(self) -> tuple[ProjectSnapshot, ...]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn accepted_snapshots(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py:117-117
    In source order: Evaluate ...; retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py:119-119
  // Source signature: correlations_touching(self, project_id: ProjectId) -> tuple[CorrelationEdge, ...]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn correlations_touching(self, project_id) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py:119-119
    In source order: Evaluate ...; retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py:121-121
  // Source signature: project_snapshot_count(self, project_id: ProjectId) -> int
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn project_snapshot_count(self, project_id) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py:121-121
    In source order: Evaluate ...; retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py:123-123
  // Source signature: node_ref_count(self, project_id: ProjectId) -> int
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn node_ref_count(self, project_id) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py:123-123
    In source order: Evaluate ...; retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py:125-125
  // Source signature: provider_manifests(self, project_id: ProjectId) -> tuple[ProviderManifest, ...]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn provider_manifests(self, project_id) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py:125-125
    In source order: Evaluate ...; retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py:127-129
  // Source signature: resolve_correlations(self, node_id: str, result_limit: int) -> tuple[ResolvedCorrelation, ...]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn resolve_correlations(self, node_id, result_limit) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py:129-129
    In source order: Evaluate ...; retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py:133-144
// Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py:132-132
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: runtime_checkable.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py:133-144
interface GraphBackendFactory {
  Describe the source Python type, preserving its base/metaclass expression order: Protocol.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py:134-134
  In source order: Retain source documentation literal source_literal_134_4; it is not a model call.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py:136-136
  // Source signature: create_project(self, locator: SnapshotLocator) -> GraphBackend
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn create_project(self, locator) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py:136-136
    In source order: Evaluate ...; retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py:138-138
  // Source signature: open_project(self, locator: SnapshotLocator) -> GraphBackend
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn open_project(self, locator) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py:138-138
    In source order: Evaluate ...; retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py:140-140
  // Source signature: create_catalog(self, path: Path) -> CatalogBackend
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn create_catalog(self, path) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py:140-140
    In source order: Evaluate ...; retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py:142-142
  // Source signature: open_catalog(self, path: Path) -> CatalogBackend
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn open_catalog(self, path) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py:142-142
    In source order: Evaluate ...; retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py:144-144
  // Source signature: delete_project(self, locator: SnapshotLocator) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn delete_project(self, locator) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py:144-144
    In source order: Evaluate ...; retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
```

## Local import links

- `from context_graph_sdk.identity import ProjectId` at source line 25: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/identity.py.sudo.md`.
- `from context_graph_sdk.models import CatalogPublication, CorrelationEdge, FrozenMap, GraphEdge, GraphNode, ProjectSnapshot, ProviderManifest, ResolvedCorrelation, SnapshotLocator` at source line 26: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/models.py.sudo.md`.
