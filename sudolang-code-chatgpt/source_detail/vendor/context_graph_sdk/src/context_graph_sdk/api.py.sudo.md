# vendor/context_graph_sdk/src/context_graph_sdk/api.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vendor/context_graph_sdk/src/context_graph_sdk/api.py.evidence.json`. SHA-256: `a5b0758a7546c2983e1467705a13dceedb987c366033e0cf73bf22f6b4b2342d`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import json; preserve alias and import-time effects. Then Resolve source import import logging; preserve alias and import-time effects. Then Resolve source import import os; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:22-26
In source order: Resolve source import import shutil; preserve alias and import-time effects. Then Resolve source import import threading; preserve alias and import-time effects. Then Resolve source import import time; preserve alias and import-time effects. Then Resolve source import import uuid; preserve alias and import-time effects. Then Resolve source import from collections.abc import Iterable; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:27-32
In source order: Resolve source import from contextlib import suppress; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from types import TracebackType; preserve alias and import-time effects. Then Resolve source import from typing import cast; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.analysis import derive_snapshot; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:33-45
In source order: Resolve source import from context_graph_sdk.backends import GraphBackendFactory; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.code_graph import CodeGraph; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.discovery import read_documentation_text, walk_repository; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.errors import DiscoveryError, LifecycleError, ModelValidationError, SnapshotLifecycleError, StructuredQueryLimitError, WorkspaceClosedError, WorkspaceLockedError; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.extractors import analysis_components; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:46-65
In source order: Resolve source import from context_graph_sdk.graph import build_structural_snapshot; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.identity import ProjectId, SnapshotId; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.ingestion import run_builtin_ingestion; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.models import AnalysisVersion, CatalogPublication, CorrelationEdge, FrozenMap, GraphNode, GraphSnapshot, NodeRef, ProjectMetadata, ProjectSnapshot, ProviderManifest, ResolvedCorrelation, SnapshotInfo, SnapshotLocator, freeze_properties; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.normalization import graph_fingerprint; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:66-79
In source order: Resolve source import from context_graph_sdk.plugins import CorrelationProvider, GraphEnricher; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.plugins.context import BufferedPluginReporter, CancellationToken, RepositorySourceReader; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.plugins.correlation import BoundedAcceptedGraphReader, CorrelationEndpointValidator, CorrelationProviderRegistry, CorrelationRunner; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.plugins.registry import PluginRegistry; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.plugins.runner import DEFAULT_LOCAL_PLUGIN_TIMEOUT_SECONDS, LocalPluginRunner; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:80-84
In source order: Resolve source import from context_graph_sdk.progress import AnalysisPhase, AnalysisProgress, AnalysisProgressCallback; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.query import QueryLimits, QueryWorkerRequest, WorkerPoolLimits; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.query.worker import QueryWorkerManager, SpawnQueryWorkerManager; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.resolution import resolve_project; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.workspace.catalog import WorkspaceCatalog; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:85-90
In source order: Resolve source import from context_graph_sdk.workspace.contracts import SnapshotLease; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.workspace.handles import SnapshotLeaseRegistry; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.workspace.locking import WorkspaceFileLock; preserve alias and import-time effects. Then Evaluate once 75.0; assign in source target order to _CONCURRENT_CLOSE_WAIT_SECONDS. Then Evaluate once 8; assign in source target order to _ANALYSIS_STEP_COUNT.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:91-91
In source order: Evaluate once logging.getLogger(__name__); assign in source target order to _LOGGER.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:94-119
// Source signature: _emit_progress(callback: AnalysisProgressCallback | None, phase: AnalysisPhase, message: str, step: int, *, completed: int | None=None, total: int | None=None, finished: bool=False) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _emit_progress(callback, phase, message, step, completed, total, finished) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:104-105
  if (the source predicate callback is None is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:105-105
    End this invocation with None.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:106-114
  In source order: Evaluate once AnalysisProgress(phase, message, step, _ANALYSIS_STEP_COUNT, completed, total, finished); assign in source target order to event.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:116-119
  Perform the following protected operations {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:117-117
    In source order: Evaluate callback(event); retain side effects and discard the expression result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:118-119
  On the first matching source exception Exception, in handler order {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:119-119
    In source order: Evaluate _LOGGER.debug('analysis progress callback failed', exc_info=True); retain side effects and discard the expression result.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:130-132
In source order: Evaluate once frozenset({5, 32}); assign in source target order to _WINDOWS_TRANSIENT_LOCK_WINERRORS. Then Evaluate once 10.0; assign in source target order to _PUBLISH_RETRY_TIMEOUT_SECONDS. Then Evaluate once 0.5; assign in source target order to _PUBLISH_RETRY_POLL_SECONDS.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:135-149
// Source signature: _replace_with_windows_lock_retry(source: Path, destination: Path) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _replace_with_windows_lock_retry(source, destination) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:136-138
  if (the source predicate os.name != 'nt' is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:137-137
    In source order: Evaluate os.replace(source, destination); retain side effects and discard the expression result.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:138-138
    End this invocation with None.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:139-139
  In source order: Evaluate once time.monotonic() + _PUBLISH_RETRY_TIMEOUT_SECONDS; assign in source target order to deadline.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:140-149
  while (the source predicate True is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:141-149
    Perform the following protected operations {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:142-142
      In source order: Evaluate os.replace(source, destination); retain side effects and discard the expression result.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:143-143
      End this invocation with None.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:144-149
    On the first matching source exception OSError as exc, in handler order {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:145-146
      if (the source predicate getattr(exc, 'winerror', None) not in _WINDOWS_TRANSIENT_LOCK_WINERRORS is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:146-146
        Raise the currently handled exception.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:147-148
      if (the source predicate time.monotonic() >= deadline is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:148-148
        Raise the currently handled exception.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:149-149
      In source order: Evaluate time.sleep(_PUBLISH_RETRY_POLL_SECONDS); retain side effects and discard the expression result.
    }
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:152-682
interface Workspace {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:153-153
  In source order: Retain source documentation literal source_literal_153_4; it is not a model call.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:155-226
  // Source signature: __init__(self, path: str | Path, backend_factory: GraphBackendFactory, *, worker_manager: QueryWorkerManager | None=None, correlation_providers: Iterable[CorrelationProvider]=(), default_query_limits: QueryLimits | None=None) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self, path, backend_factory, worker_manager, correlation_providers, default_query_limits) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:164-170
    if (the source predicate worker_manager is None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:165-165
      In source order: Resolve source import from context_graph_sdk.backends.arcadedb import ArcadeDBBackendFactory; preserve alias and import-time effects.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:167-170
      if (the source predicate not isinstance(backend_factory, ArcadeDBBackendFactory) is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:168-170
        Raise TypeError('non-Arcade backend factories require an explicit query worker manager').
      }
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:171-173
    In source order: Evaluate once Path(path).expanduser().resolve(); assign in source target order to self.path. Then Evaluate self.path.mkdir(parents=True, exist_ok=True); retain side effects and discard the expression result. Then Evaluate once backend_factory; assign in source target order to self._factory.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:174-177
    Perform the following protected operations {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:175-175
      In source order: Evaluate once WorkspaceFileLock(self.path / '.workspace.lock'); assign in source target order to self._workspace_lock.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:176-177
    On the first matching source exception BlockingIOError as exc, in handler order {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:177-177
      Raise WorkspaceLockedError(source_template_177_39) with explicit source cause exc.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:178-179
    In source order: Evaluate once worker_manager; assign in source target order to workers. Then For catalog, assign None; source annotation WorkspaceCatalog | None.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:180-226
    Perform the following protected operations {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:181-182
      if (the source predicate workers is None is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:182-182
        In source order: Evaluate once SpawnQueryWorkerManager(WorkerPoolLimits(1)); assign in source target order to workers.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:183-187
      In source order: Evaluate once False; assign in source target order to self._closed. Then Evaluate once False; assign in source target order to self._closing. Then Evaluate once threading.Event(); assign in source target order to self._close_complete. Then For self._close_failure, assign None; source annotation LifecycleError | None. Then Evaluate once threading.RLock(); assign in source target order to self._state_lock.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:188-192
      In source order: Evaluate once 0; assign in source target order to self._request_counter. Then Evaluate once SnapshotLeaseRegistry(); assign in source target order to self._leases. Then For self._retired, assign {}; source annotation dict[str, SnapshotLocator]. Then Evaluate once CorrelationProviderRegistry(correlation_providers); assign in source target order to self._correlation_registry. Then Evaluate once CorrelationRunner(); assign in source target order to self._correlation_runner.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:193-205
      In source order: Evaluate once LocalPluginRunner(); assign in source target order to self._local_plugin_runner. Then Evaluate once default_query_limits or QueryLimits(30.0, 1024 * 1024 * 1024, 1000, 1024 * 1024); assign in source target order to self.default_query_limits. Then Evaluate once workers; assign in source target order to self._workers. Then Evaluate once self.path / 'catalog'; assign in source target order to catalog_path. Then Evaluate once self._factory.open_catalog(catalog_path) if catalog_path.exists() else self._factory.create_catalog(catalog_path); assign in source target order to catalog_backend.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:206-210
      In source order: Evaluate once WorkspaceCatalog(catalog_backend); assign in source target order to catalog. Then Evaluate once catalog; assign in source target order to self._catalog. Then Evaluate self._validate_catalog_snapshots(); retain side effects and discard the expression result. Then Evaluate self._reconcile(); retain side effects and discard the expression result. Then Evaluate self._preflight_all_providers(); retain side effects and discard the expression result.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:211-217
      for each snapshot in self._catalog.accepted_snapshots() {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:212-217
        In source order: Evaluate once _read_snapshot_integrity(snapshot.locator.database_path); assign in source target order to (fingerprint, node_count, edge_count). Then Evaluate self._workers.authorize(snapshot.locator.database_path, fingerprint, node_count, edge_count); retain side effects and discard the expression result.
      }
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:218-226
    On the first matching source exception Exception, in handler order {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:219-221
      if (the source predicate workers is not None is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:220-221
        Enter source context managers left-to-right: suppress(Exception) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:221-221
          In source order: Evaluate workers.close(); retain side effects and discard the expression result.
        }
        Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:222-224
      if (the source predicate catalog is not None is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:223-224
        Enter source context managers left-to-right: suppress(Exception) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:224-224
          In source order: Evaluate catalog.close(); retain side effects and discard the expression result.
        }
        Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:225-225
      In source order: Evaluate self._workspace_lock.release(); retain side effects and discard the expression result.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:226-226
      Raise the currently handled exception.
    }
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:228-229
  // Source signature: __enter__(self) -> Workspace
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __enter__(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:229-229
    End this invocation with self.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:231-237
  // Source signature: __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: TracebackType | None) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __exit__(self, exc_type, exc_value, traceback) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:237-237
    In source order: Evaluate self.close(); retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:239-378
  // Source signature: analyze(self, repository: str | Path, project_id: ProjectId | str, plugins: Iterable[GraphEnricher]=(), *, progress: AnalysisProgressCallback | None=None) -> CodeGraph
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn analyze(self, repository, project_id, plugins, progress) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:247-251
    In source order: Retain source documentation literal source_literal_247_8; it is not a model call. Then Evaluate self._ensure_open(); retain side effects and discard the expression result. Then Evaluate once PluginRegistry(plugins); assign in source target order to registry. Then Evaluate once project_id if isinstance(project_id, ProjectId) else ProjectId(project_id); assign in source target order to resolved. Then Evaluate self._preflight_all_providers(); retain side effects and discard the expression result.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:252-252
    In source order: Evaluate once Path(repository); assign in source target order to repository_path.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:253-254
    if (the source predicate not repository_path.is_dir() is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:254-254
      Raise DiscoveryError(source_template_254_33).
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:255-277
    In source order: Evaluate _emit_progress(progress, AnalysisPhase.DISCOVERY, 'Discovering files', 1); retain side effects and discard the expression result. Then Evaluate once walk_repository(repository_path); assign in source target order to walk. Then Evaluate _emit_progress(progress, AnalysisPhase.CONFIGURATION, 'Reading project configuration', 2); retain side effects and discard the expression result. Then Evaluate once run_builtin_ingestion(walk, on_language_start=lambda: _emit_progress(progress, AnalysisPhase.EXTRACTION, 'Extracting symbols', 3), on_file_progress=lambda completed, total: _emit_progress(progress, AnalysisPhase.EXTRACTION, 'Extracting symbols', 3, completed=completed, total=total)); assign in source target order to ingestion. Then Evaluate once ingestion.config; assign in source target order to config.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:278-292
    In source order: Evaluate once {file.relative_path: content for file in walk.files if file.is_documentation and (content := read_documentation_text(walk.root, file.relative_path))}; assign in source target order to documentation. Then Evaluate once ingestion.extraction; assign in source target order to extraction. Then Evaluate _emit_progress(progress, AnalysisPhase.RESOLUTION, 'Resolving relationships', 4); retain side effects and discard the expression result. Then Evaluate once resolve_project([(file.relative_path, file.language) for file in walk.files], list(walk.directories), extraction, config); assign in source target order to resolution. Then Evaluate _emit_progress(progress, AnalysisPhase.GRAPH_BUILD, 'Building candidate graph', 5); retain side effects and discard the expression result.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:293-324
    In source order: Evaluate once ProjectMetadata(resolved, Path(walk.root).name or resolved.value, source_path=walk.root); assign in source target order to metadata. Then Evaluate once (('analysis', '1'), ('discovery', '1'), ('extractors', '1'), *analysis_components()); assign in source target order to components. Then Evaluate once build_structural_snapshot(metadata, SnapshotId(uuid.uuid4().hex), AnalysisVersion(_sdk_version(), components), walk, config, documentation, extraction, resolution); assign in source target order to snapshot. Then Evaluate _emit_progress(progress, AnalysisPhase.DERIVATION, 'Running plugins and derived analysis', 6); retain side effects and discard the expression result. Then Evaluate once CancellationToken(); assign in source target order to cancellation.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:325-346
    In source order: Evaluate once time.monotonic() + DEFAULT_LOCAL_PLUGIN_TIMEOUT_SECONDS; assign in source target order to deadline. Then Evaluate once self._local_plugin_runner.run(snapshot, registry, source_reader=RepositorySourceReader(Path(walk.root)), cancellation=cancellation, deadline_monotonic=deadline, configuration=FrozenMap(), derive=derive_snapshot); assign in source target order to result. Then Evaluate _emit_progress(progress, AnalysisPhase.CORRELATION, 'Correlating projects', 7); retain side effects and discard the expression result. Then Evaluate once tuple((accepted_snapshot for accepted_snapshot in self._catalog.accepted_snapshots() if accepted_snapshot.project.project_id != resolved)); assign in source target order to accepted. Then Evaluate once BoundedAcceptedGraphReader(accepted, self._execute_accepted_query, self._correlation_runner.limits, deadline); assign in source target order to graph_reader.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:347-377
    In source order: Evaluate once CorrelationEndpointValidator(accepted, self._execute_accepted_query, self._correlation_runner.limits.max_total_edges, deadline); assign in source target order to endpoint_validator. Then Evaluate once self._correlation_runner.run(result.snapshot, accepted, self._correlation_registry, graph_reader=graph_reader, endpoint_validator=endpoint_validator, reporter=BufferedPluginReporter(), cancellation=cancellation, deadline_monotonic=deadline, configuration=FrozenMap()); assign in source target order to correlation_result. Then Evaluate _emit_progress(progress, AnalysisPhase.PUBLICATION, 'Publishing snapshot', 8); retain side effects and discard the expression result. Then Evaluate once self._publish_snapshot(result.snapshot, node_refs=correlation_result.node_refs, correlations=correlation_result.correlations, provider_manifests=correlation_result.manifests); assign in source target order to graph. Then Evaluate _emit_progress(progress, AnalysisPhase.PUBLICATION, 'Analysis complete', 8, finished=True); retain side effects and discard the expression result.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:378-378
    End this invocation with graph.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:380-385
  // Source signature: project(self, project_id: ProjectId | str) -> CodeGraph
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn project(self, project_id) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:381-382
    In source order: Evaluate self._ensure_open(); retain side effects and discard the expression result. Then Evaluate once project_id if isinstance(project_id, ProjectId) else ProjectId(project_id); assign in source target order to resolved.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:383-384
    if (the source predicate self._catalog.accepted_snapshot(resolved) is None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:384-384
      Raise SnapshotLifecycleError(source_template_384_41).
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:385-385
    End this invocation with CodeGraph(self, resolved).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:387-394
  // Source signature: snapshot_info(self, project_id: ProjectId | str) -> SnapshotInfo
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn snapshot_info(self, project_id) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:388-390
    In source order: Retain source documentation literal source_literal_388_8; it is not a model call. Then Evaluate once project_id if isinstance(project_id, ProjectId) else ProjectId(project_id); assign in source target order to resolved. Then Evaluate once self._resolve_with_lease(resolved); assign in source target order to (snapshot, lease).
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:391-394
    Perform the following protected operations {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:392-392
      End this invocation with SnapshotInfo(*_read_snapshot_integrity(snapshot.locator.database_path)).
    }
    On every exit from this protected/handler/normal-completion region {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:394-394
      In source order: Evaluate lease.release(); retain side effects and discard the expression result.
    }
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:396-440
  // Source signature: close(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn close(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:397-404
    Enter source context managers left-to-right: self._state_lock {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:398-399
      if (the source predicate self._closed is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:399-399
        End this invocation with None.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:400-404
      if (the source predicate self._closing is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:401-401
        In source order: Evaluate once self._close_complete; assign in source target order to close_complete.
      }
      else {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:403-404
        In source order: Evaluate once True; assign in source target order to self._closing. Then Evaluate once None; assign in source target order to close_complete.
      }
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:405-412
    if (the source predicate close_complete is not None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:406-407
      if (the source predicate not close_complete.wait(_CONCURRENT_CLOSE_WAIT_SECONDS) is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:407-407
        Raise LifecycleError('concurrent workspace close did not finish').
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:408-409
      Enter source context managers left-to-right: self._state_lock {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:409-409
        In source order: Evaluate once self._close_failure; assign in source target order to failure.
      }
      Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:410-411
      if (the source predicate failure is not None is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:411-411
        Raise failure.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:412-412
      End this invocation with None.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:413-413
    In source order: For failures, assign []; source annotation list[Exception].
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:414-440
    Perform the following protected operations {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:415-418
      Perform the following protected operations {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:416-416
        In source order: Evaluate self._workers.close(); retain side effects and discard the expression result.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:417-418
      On the first matching source exception Exception as exc, in handler order {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:418-418
        In source order: Evaluate failures.append(exc); retain side effects and discard the expression result.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:419-419
      In source order: Evaluate once self._leases.wait_for_zero(10.0); assign in source target order to leases_drained.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:420-421
      if (the source predicate not leases_drained is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:421-421
        In source order: Evaluate failures.append(LifecycleError('workspace leases did not drain before close')); retain side effects and discard the expression result.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:422-432
      if (the source predicate leases_drained is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:423-427
        for each close_resource in (self._catalog.close, self._leases.close) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:424-427
          Perform the following protected operations {
            // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:425-425
            In source order: Evaluate close_resource(); retain side effects and discard the expression result.
          }
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:426-427
          On the first matching source exception Exception as exc, in handler order {
            // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:427-427
            In source order: Evaluate failures.append(exc); retain side effects and discard the expression result.
          }
        }
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:428-432
        if (the source predicate not failures is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:429-432
          Perform the following protected operations {
            // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:430-430
            In source order: Evaluate self._workspace_lock.release(); retain side effects and discard the expression result.
          }
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:431-432
          On the first matching source exception Exception as exc, in handler order {
            // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:432-432
            In source order: Evaluate failures.append(exc); retain side effects and discard the expression result.
          }
        }
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:433-433
      In source order: Evaluate once _cleanup_failure(failures) if failures else None; assign in source target order to failure.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:434-436
      Enter source context managers left-to-right: self._state_lock {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:435-436
        In source order: Evaluate once failure; assign in source target order to self._close_failure. Then Evaluate once failure is None; assign in source target order to self._closed.
      }
      Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:437-438
      if (the source predicate failure is not None is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:438-438
        Raise failure.
      }
    }
    On every exit from this protected/handler/normal-completion region {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:440-440
      In source order: Evaluate self._close_complete.set(); retain side effects and discard the expression result.
    }
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:442-529
  // Source signature: _publish_snapshot(self, snapshot: GraphSnapshot, *, node_refs: tuple[NodeRef, ...]=(), correlations: tuple[CorrelationEdge, ...]=(), provider_manifests: tuple[ProviderManifest, ...]=(), fail_before_commit: bool=False) -> CodeGraph
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _publish_snapshot(self, snapshot, node_refs, correlations, provider_manifests, fail_before_commit) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:451-455
    In source order: Retain source documentation literal source_literal_451_8; it is not a model call. Then Evaluate self._ensure_open(); retain side effects and discard the expression result. Then Evaluate once snapshot.project.project_id; assign in source target order to project. Then Evaluate once self.path / 'projects' / project.value / snapshot.snapshot_id.value; assign in source target order to final_path. Then Evaluate once self.path / 'candidates' / source_template_455_52; assign in source target order to candidate_path.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:456-457
    if (the source predicate final_path.exists() or candidate_path.exists() is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:457-457
      Raise SnapshotLifecycleError('snapshot database path already exists').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:458-462
    In source order: Evaluate once SnapshotLocator(project, snapshot.snapshot_id, str(candidate_path)); assign in source target order to candidate_locator. Then Evaluate once None; assign in source target order to backend. Then Evaluate once graph_fingerprint(snapshot); assign in source target order to fingerprint. Then Evaluate once False; assign in source target order to moved. Then Evaluate once False; assign in source target order to authorized.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:463-527
    Perform the following protected operations {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:464-479
      In source order: Evaluate once self._factory.create_project(candidate_locator); assign in source target order to backend. Then Evaluate once tuple((GraphNode(node.project_id, node.local_id, node.labels, freeze_properties({**node.properties.to_dict(), 'snapshotId': snapshot.snapshot_id.value, 'analysisVersion': snapshot.analysis_version.sdk_version})) for node in snapshot.nodes)); assign in source target order to persisted_nodes.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:480-485
      Enter source context managers left-to-right: backend.begin_write() bound to transaction {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:481-482
        for each start in range(0, len(persisted_nodes), 10000) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:482-482
          In source order: Evaluate transaction.write_nodes(persisted_nodes[start:start + 10000]); retain side effects and discard the expression result.
        }
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:483-484
        for each start in range(0, len(snapshot.edges), 10000) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:484-484
          In source order: Evaluate transaction.write_edges(snapshot.edges[start:start + 10000]); retain side effects and discard the expression result.
        }
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:485-485
        In source order: Evaluate transaction.commit(); retain side effects and discard the expression result.
      }
      Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:486-501
      In source order: Evaluate backend.close(); retain side effects and discard the expression result. Then Evaluate once None; assign in source target order to backend. Then Evaluate (candidate_path / '.context-graph-sdk-fingerprint').write_text(json.dumps({'fingerprint': fingerprint, 'nodeCount': len(snapshot.nodes), 'edgeCount': len(snapshot.edges)}, separators=(',', ':'), sort_keys=True) + source_literal_498_18); retain side effects and discard the expression result. Then Evaluate final_path.parent.mkdir(parents=True, exist_ok=True); retain side effects and discard the expression result. Then Evaluate _replace_with_windows_lock_retry(candidate_path, final_path); retain side effects and discard the expression result.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:502-511
      In source order: Evaluate once True; assign in source target order to moved. Then Evaluate once SnapshotLocator(project, snapshot.snapshot_id, str(final_path)); assign in source target order to locator. Then Evaluate once ProjectSnapshot(snapshot.project, snapshot.snapshot_id, locator, snapshot.analysis_version, True); assign in source target order to record. Then Evaluate once CatalogPublication(record, node_refs, correlations, provider_manifests); assign in source target order to publication.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:512-520
      Enter source context managers left-to-right: self._state_lock {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:513-518
        In source order: Evaluate once self._catalog.accepted_snapshot(project); assign in source target order to previous. Then Evaluate self._workers.authorize(locator.database_path, fingerprint, len(snapshot.nodes), len(snapshot.edges)); retain side effects and discard the expression result. Then Evaluate once True; assign in source target order to authorized. Then Evaluate self._catalog.publish(publication, fail_before_commit=fail_before_commit); retain side effects and discard the expression result.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:519-520
        if (the source predicate previous is not None is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:520-520
          In source order: Evaluate once previous.locator; assign in source target order to self._retired[previous.locator.database_path].
        }
      }
      Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:521-527
    On the first matching source exception Exception, in handler order {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:522-523
      if (the source predicate backend is not None is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:523-523
        In source order: Evaluate backend.close(); retain side effects and discard the expression result.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:524-525
      if (the source predicate authorized is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:525-525
        In source order: Evaluate self._workers.revoke(str(final_path)); retain side effects and discard the expression result.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:526-526
      In source order: Evaluate shutil.rmtree(final_path if moved else candidate_path, ignore_errors=True); retain side effects and discard the expression result.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:527-527
      Raise the currently handled exception.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:528-528
    In source order: Evaluate self._collect_retired(); retain side effects and discard the expression result.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:529-529
    End this invocation with CodeGraph(self, project).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:531-565
  // Source signature: _execute_accepted_query(self, locator: SnapshotLocator, cypher: str, parameters: FrozenMap, row_limit: int, timeout_seconds: float) -> tuple[FrozenMap, ...]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _execute_accepted_query(self, locator, cypher, parameters, row_limit, timeout_seconds) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:539-543
    Enter source context managers left-to-right: self._state_lock {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:540-540
      In source order: Evaluate once self._catalog.accepted_snapshot(locator.project_id); assign in source target order to accepted.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:541-542
      if (the source predicate accepted is None or accepted.locator != locator is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:542-542
        Raise SnapshotLifecycleError('provider snapshot is no longer accepted').
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:543-543
      In source order: Evaluate once self._leases.acquire(locator).__enter__(); assign in source target order to lease.
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:544-565
    Perform the following protected operations {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:545-559
      In source order: Evaluate once self.default_query_limits; assign in source target order to limits. Then Evaluate once self._workers.execute(QueryWorkerRequest(self._next_request_id(), locator, cypher, parameters, QueryLimits(min(limits.timeout_seconds, timeout_seconds), limits.memory_bytes, row_limit, limits.byte_limit))); assign in source target order to result.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:560-561
      if (the source predicate result.truncated is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:561-561
        Raise ModelValidationError('provider read result exceeded its declared bound').
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:562-562
      End this invocation with result.rows.
    }
    On every exit from this protected/handler/normal-completion region {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:564-565
      In source order: Evaluate lease.release(); retain side effects and discard the expression result. Then Evaluate self._collect_retired(); retain side effects and discard the expression result.
    }
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:567-604
  // Source signature: _resolve_correlations_with_leases(self, node_id: str, result_limit: int) -> tuple[tuple[ResolvedCorrelation, ...], tuple[SnapshotLease, ...]]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _resolve_correlations_with_leases(self, node_id, result_limit) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:570-570
    In source order: Evaluate self._ensure_open(); retain side effects and discard the expression result.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:571-603
    for each attempt in range(2) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:572-595
      Enter source context managers left-to-right: self._state_lock {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:573-578
        Perform the following protected operations {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:574-574
          In source order: Evaluate once self._catalog.resolve_correlations(node_id, result_limit); assign in source target order to resolved.
        }
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:575-578
        On the first matching source exception ModelValidationError as exc, in handler order {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:576-577
          if (the source predicate 'limit' in str(exc) is truthy) {
            // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:577-577
            Raise StructuredQueryLimitError(str(exc)) with explicit source cause exc.
          }
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:578-578
          Raise the currently handled exception.
        }
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:579-579
        In source order: For leases_by_path, assign {}; source annotation dict[str, SnapshotLease].
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:580-590
        Perform the following protected operations {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:581-586
          for each item in resolved {
            // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:582-582
            In source order: Evaluate once item.related_snapshot.locator; assign in source target order to locator.
            // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:583-586
            if (the source predicate locator.database_path not in leases_by_path is truthy) {
              // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:584-586
              In source order: Evaluate once self._leases.acquire(locator).__enter__(); assign in source target order to leases_by_path[locator.database_path].
            }
          }
        }
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:587-590
        On the first matching source exception Exception, in handler order {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:588-589
          for each lease in leases_by_path.values() {
            // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:589-589
            In source order: Evaluate lease.release(); retain side effects and discard the expression result.
          }
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:590-590
          Raise the currently handled exception.
        }
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:591-595
        In source order: Evaluate once tuple(leases_by_path.values()); assign in source target order to leases. Then Evaluate once any((not Path(item.related_snapshot.locator.database_path).exists() for item in resolved)); assign in source target order to missing.
      }
      Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:596-597
      if (the source predicate not missing is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:597-597
        End this invocation with (resolved, leases).
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:598-599
      for each lease in leases {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:599-599
        In source order: Evaluate lease.release(); retain side effects and discard the expression result.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:600-603
      if (the source predicate attempt == 1 is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:601-603
        Raise SnapshotLifecycleError('correlation target snapshot is unavailable after re-resolution').
      }
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:604-604
    Raise AssertionError('bounded correlation resolution exhausted').
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:606-613
  // Source signature: _resolve_with_lease(self, project_id: ProjectId)
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _resolve_with_lease(self, project_id) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:607-607
    In source order: Evaluate self._ensure_open(); retain side effects and discard the expression result.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:608-613
    Enter source context managers left-to-right: self._state_lock {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:609-609
      In source order: Evaluate once self._catalog.accepted_snapshot(project_id); assign in source target order to snapshot.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:610-611
      if (the source predicate snapshot is None is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:611-611
        Raise SnapshotLifecycleError(source_template_611_45).
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:612-612
      In source order: Evaluate once self._leases.acquire(snapshot.locator).__enter__(); assign in source target order to lease.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:613-613
      End this invocation with (snapshot, lease).
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:615-624
  // Source signature: _collect_retired(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _collect_retired(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:616-624
    Enter source context managers left-to-right: self._state_lock {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:617-624
      for each (path, locator) in tuple(self._retired.items()) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:618-624
        if (the source predicate self._leases.active_count(locator) == 0 is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:619-622
          Perform the following protected operations {
            // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:620-620
            In source order: Evaluate self._factory.delete_project(locator); retain side effects and discard the expression result.
          }
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:621-622
          On the first matching source exception OSError, in handler order {
            // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:622-622
            Continue the immediately enclosing source loop at its next iteration.
          }
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:623-624
          In source order: Evaluate self._workers.revoke(path); retain side effects and discard the expression result. Then Delete source targets in order: self._retired[path].
        }
      }
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:626-629
  // Source signature: _next_request_id(self) -> str
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _next_request_id(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:627-629
    Enter source context managers left-to-right: self._state_lock {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:628-628
      In source order: Apply source augmented assignment self._request_counter += 1 with source evaluation/in-place semantics.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:629-629
      End this invocation with source_template_629_19.
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:631-650
  // Source signature: _validate_catalog_snapshots(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _validate_catalog_snapshots(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:632-632
    In source order: Evaluate once (self.path / 'projects').resolve(); assign in source target order to projects.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:633-650
    for each snapshot in self._catalog.accepted_snapshots() {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:634-635
      In source order: Evaluate once snapshot.locator; assign in source target order to locator. Then Evaluate once projects / locator.project_id.value / locator.snapshot_id.value; assign in source target order to expected.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:636-642
      Perform the following protected operations {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:637-638
        In source order: Evaluate once Path(locator.database_path).resolve(strict=True); assign in source target order to canonical. Then Evaluate once expected.resolve(strict=True); assign in source target order to expected_canonical.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:639-642
      On the first matching source exception OSError as exc, in handler order {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:640-642
        Raise SnapshotLifecycleError(source_template_641_20) with explicit source cause exc.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:643-650
      if (the source predicate canonical != expected_canonical or canonical == projects or projects not in canonical.parents is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:648-650
        Raise SnapshotLifecycleError(source_template_649_20).
      }
    }
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:652-669
  // Source signature: _reconcile(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _reconcile(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:653-657
    In source order: Evaluate once {Path(snapshot.locator.database_path).resolve() for snapshot in self._catalog.accepted_snapshots()}; assign in source target order to accepted. Then Evaluate once self.path / 'candidates'; assign in source target order to candidates.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:658-661
    if (the source predicate candidates.exists() is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:659-661
      for each path in candidates.iterdir() {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:660-661
        if (the source predicate path.is_dir() is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:661-661
          In source order: Evaluate shutil.rmtree(path); retain side effects and discard the expression result.
        }
      }
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:662-662
    In source order: Evaluate once self.path / 'projects'; assign in source target order to projects.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:663-669
    if (the source predicate projects.exists() is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:664-669
      for each project_dir in projects.iterdir() {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:665-666
        if (the source predicate not project_dir.is_dir() is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:666-666
          Continue the immediately enclosing source loop at its next iteration.
        }
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:667-669
        for each snapshot_dir in project_dir.iterdir() {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:668-669
          if (the source predicate snapshot_dir.is_dir() and snapshot_dir.resolve() not in accepted is truthy) {
            // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:669-669
            In source order: Evaluate shutil.rmtree(snapshot_dir); retain side effects and discard the expression result.
          }
        }
      }
    }
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:671-678
  // Source signature: _preflight_all_providers(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _preflight_all_providers(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:672-678
    for each snapshot in self._catalog.accepted_snapshots() {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:673-678
      In source order: Evaluate once snapshot.project.project_id; assign in source target order to project_id. Then Evaluate self._correlation_registry.preflight(project_id, self._catalog.provider_manifests(project_id), self._catalog.correlations_touching(project_id)); retain side effects and discard the expression result.
    }
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:680-682
  // Source signature: _ensure_open(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _ensure_open(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:681-682
    if (the source predicate self._closed or self._closing is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:682-682
      Raise WorkspaceClosedError('workspace is closed').
    }
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:685-689
// Source signature: _cleanup_failure(failures: list[Exception]) -> LifecycleError
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _cleanup_failure(failures) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:686-688
  In source order: Evaluate once '; '.join((source_template_686_24 for failure in failures)); assign in source target order to details. Then Evaluate once LifecycleError(source_template_687_27); assign in source target order to error. Then Evaluate once failures[0]; assign in source target order to error.__cause__.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:689-689
  End this invocation with error.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:692-698
// Source signature: _sdk_version() -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _sdk_version() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:693-693
  In source order: Resolve source import import importlib.metadata; preserve alias and import-time effects.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:695-698
  Perform the following protected operations {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:696-696
    End this invocation with importlib.metadata.version('context-graph-sdk').
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:697-698
  On the first matching source exception importlib.metadata.PackageNotFoundError, in handler order {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:698-698
    End this invocation with '0'.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:701-721
// Source signature: _read_snapshot_integrity(database_path: str) -> tuple[str, int, int]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _read_snapshot_integrity(database_path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:702-721
  Perform the following protected operations {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:703-704
    In source order: Evaluate once (Path(database_path) / '.context-graph-sdk-fingerprint').read_text(); assign in source target order to content. Then For parsed, assign json.loads(content); source annotation object.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:705-706
    if (the source predicate not isinstance(parsed, dict) is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:706-706
      Raise ValueError('integrity sidecar is not an object').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:707-710
    In source order: Evaluate once cast(dict[str, object], parsed); assign in source target order to payload. Then Evaluate once payload.get('fingerprint'); assign in source target order to fingerprint. Then Evaluate once payload.get('nodeCount'); assign in source target order to node_count. Then Evaluate once payload.get('edgeCount'); assign in source target order to edge_count.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:711-716
    if (the source predicate not isinstance(fingerprint, str) or not isinstance(node_count, int) or (not isinstance(edge_count, int)) is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:716-716
      Raise ValueError('integrity sidecar fields are invalid').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:717-717
    End this invocation with (fingerprint, node_count, edge_count).
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:718-721
  On the first matching source exception (OSError, ValueError, json.JSONDecodeError) as exc, in handler order {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/api.py:719-721
    Raise SnapshotLifecycleError(source_template_720_12) with explicit source cause exc.
  }
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from context_graph_sdk.analysis import derive_snapshot` at source line 32: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/analysis/__init__.py.sudo.md`.
- `from context_graph_sdk.backends import GraphBackendFactory` at source line 33: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/backends/__init__.py.sudo.md`.
- `from context_graph_sdk.code_graph import CodeGraph` at source line 34: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py.sudo.md`.
- `from context_graph_sdk.discovery import read_documentation_text, walk_repository` at source line 35: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/discovery/__init__.py.sudo.md`.
- `from context_graph_sdk.errors import DiscoveryError, LifecycleError, ModelValidationError, SnapshotLifecycleError, StructuredQueryLimitError, WorkspaceClosedError, WorkspaceLockedError` at source line 36: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/errors.py.sudo.md`.
- `from context_graph_sdk.extractors import analysis_components` at source line 45: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/extractors/__init__.py.sudo.md`.
- `from context_graph_sdk.graph import build_structural_snapshot` at source line 46: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/graph/__init__.py.sudo.md`.
- `from context_graph_sdk.identity import ProjectId, SnapshotId` at source line 47: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/identity.py.sudo.md`.
- `from context_graph_sdk.ingestion import run_builtin_ingestion` at source line 48: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/ingestion.py.sudo.md`.
- `from context_graph_sdk.models import AnalysisVersion, CatalogPublication, CorrelationEdge, FrozenMap, GraphNode, GraphSnapshot, NodeRef, ProjectMetadata, ProjectSnapshot, ProviderManifest, ResolvedCorrelation, SnapshotInfo, SnapshotLocator, freeze_properties` at source line 49: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/models.py.sudo.md`.
- `from context_graph_sdk.normalization import graph_fingerprint` at source line 65: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/normalization.py.sudo.md`.
- `from context_graph_sdk.plugins import CorrelationProvider, GraphEnricher` at source line 66: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/plugins/__init__.py.sudo.md`.
- `from context_graph_sdk.plugins.context import BufferedPluginReporter, CancellationToken, RepositorySourceReader` at source line 67: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/plugins/context.py.sudo.md`.
- `from context_graph_sdk.plugins.correlation import BoundedAcceptedGraphReader, CorrelationEndpointValidator, CorrelationProviderRegistry, CorrelationRunner` at source line 72: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py.sudo.md`.
- `from context_graph_sdk.plugins.registry import PluginRegistry` at source line 78: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/plugins/registry.py.sudo.md`.
- `from context_graph_sdk.plugins.runner import DEFAULT_LOCAL_PLUGIN_TIMEOUT_SECONDS, LocalPluginRunner` at source line 79: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py.sudo.md`.
- `from context_graph_sdk.progress import AnalysisPhase, AnalysisProgress, AnalysisProgressCallback` at source line 80: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/progress.py.sudo.md`.
- `from context_graph_sdk.query import QueryLimits, QueryWorkerRequest, WorkerPoolLimits` at source line 81: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/query/__init__.py.sudo.md`.
- `from context_graph_sdk.query.worker import QueryWorkerManager, SpawnQueryWorkerManager` at source line 82: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py.sudo.md`.
- `from context_graph_sdk.resolution import resolve_project` at source line 83: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/resolution/__init__.py.sudo.md`.
- `from context_graph_sdk.workspace.catalog import WorkspaceCatalog` at source line 84: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/workspace/catalog.py.sudo.md`.
- `from context_graph_sdk.workspace.contracts import SnapshotLease` at source line 85: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/workspace/contracts.py.sudo.md`.
- `from context_graph_sdk.workspace.handles import SnapshotLeaseRegistry` at source line 86: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/workspace/handles.py.sudo.md`.
- `from context_graph_sdk.workspace.locking import WorkspaceFileLock` at source line 87: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/workspace/locking.py.sudo.md`.
- `from context_graph_sdk.backends.arcadedb import ArcadeDBBackendFactory` at source line 165: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py.sudo.md`.
