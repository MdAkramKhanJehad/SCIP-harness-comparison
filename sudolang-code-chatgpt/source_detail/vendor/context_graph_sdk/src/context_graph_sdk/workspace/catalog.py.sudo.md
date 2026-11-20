# vendor/context_graph_sdk/src/context_graph_sdk/workspace/catalog.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vendor/context_graph_sdk/src/context_graph_sdk/workspace/catalog.py.evidence.json`. SHA-256: `be65a911af80287b2d0a04ae323b07e892cfb8f26ce9069b2c42eff856e2ae32`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/catalog.py:15-27
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.backends import CatalogBackend; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.identity import ProjectId; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.models import CatalogPublication, CorrelationEdge, ProjectSnapshot, ProviderManifest, ResolvedCorrelation; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/catalog.py:30-65
interface WorkspaceCatalog {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/catalog.py:31-32
  // Source signature: __init__(self, backend: CatalogBackend) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self, backend) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/catalog.py:32-32
    In source order: Evaluate once backend; assign in source target order to self._backend.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/catalog.py:34-39
  // Source signature: publish(self, publication: CatalogPublication, *, fail_before_commit: bool=False) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn publish(self, publication, fail_before_commit) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/catalog.py:35-39
    Enter source context managers left-to-right: self._backend.begin_publication() bound to transaction {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/catalog.py:36-36
      In source order: Evaluate transaction.publish(publication); retain side effects and discard the expression result.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/catalog.py:37-38
      if (the source predicate fail_before_commit is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/catalog.py:38-38
        Raise RuntimeError('injected failure before catalog commit').
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/catalog.py:39-39
      In source order: Evaluate transaction.commit(); retain side effects and discard the expression result.
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/catalog.py:41-42
  // Source signature: accepted_snapshot(self, project_id: ProjectId) -> ProjectSnapshot | None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn accepted_snapshot(self, project_id) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/catalog.py:42-42
    End this invocation with self._backend.accepted_snapshot(project_id).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/catalog.py:44-45
  // Source signature: accepted_snapshots(self) -> tuple[ProjectSnapshot, ...]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn accepted_snapshots(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/catalog.py:45-45
    End this invocation with self._backend.accepted_snapshots().
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/catalog.py:47-48
  // Source signature: correlations_touching(self, project_id: ProjectId) -> tuple[CorrelationEdge, ...]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn correlations_touching(self, project_id) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/catalog.py:48-48
    End this invocation with self._backend.correlations_touching(project_id).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/catalog.py:50-51
  // Source signature: project_snapshot_count(self, project_id: ProjectId) -> int
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn project_snapshot_count(self, project_id) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/catalog.py:51-51
    End this invocation with self._backend.project_snapshot_count(project_id).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/catalog.py:53-54
  // Source signature: node_ref_count(self, project_id: ProjectId) -> int
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn node_ref_count(self, project_id) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/catalog.py:54-54
    End this invocation with self._backend.node_ref_count(project_id).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/catalog.py:56-57
  // Source signature: provider_manifests(self, project_id: ProjectId) -> tuple[ProviderManifest, ...]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn provider_manifests(self, project_id) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/catalog.py:57-57
    End this invocation with self._backend.provider_manifests(project_id).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/catalog.py:59-62
  // Source signature: resolve_correlations(self, node_id: str, result_limit: int) -> tuple[ResolvedCorrelation, ...]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn resolve_correlations(self, node_id, result_limit) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/catalog.py:62-62
    End this invocation with self._backend.resolve_correlations(node_id, result_limit).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/catalog.py:64-65
  // Source signature: close(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn close(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/catalog.py:65-65
    In source order: Evaluate self._backend.close(); retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
}
```

## Local import links

- `from context_graph_sdk.backends import CatalogBackend` at source line 19: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/backends/__init__.py.sudo.md`.
- `from context_graph_sdk.identity import ProjectId` at source line 20: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/identity.py.sudo.md`.
- `from context_graph_sdk.models import CatalogPublication, CorrelationEdge, ProjectSnapshot, ProviderManifest, ResolvedCorrelation` at source line 21: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/models.py.sudo.md`.
