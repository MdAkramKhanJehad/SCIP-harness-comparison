# vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py.evidence.json`. SHA-256: `27cbb0acc17263e0d8ae7c73682b4615e9dc315703ba54751a516abfae43fb83`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import time; preserve alias and import-time effects. Then Resolve source import from collections.abc import Callable, Iterable, Iterator; preserve alias and import-time effects. Then Resolve source import from dataclasses import dataclass; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:22-37
In source order: Resolve source import from typing import cast; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.errors import ModelValidationError, PluginError, SnapshotLifecycleError; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.identity import ProjectId, SnapshotId; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.models import CorrelationEdge, FrozenMap, GraphNode, GraphSnapshot, NodeRef, ProjectSnapshot, ProviderManifest, SnapshotLocator, freeze_properties; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.pipeline import AcceptedGraphReader, CorrelationContext, PluginDiagnostic; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:39-43
In source order: Resolve source import from .base import CorrelationProvider, PluginMetadata, PluginPhase; preserve alias and import-time effects. Then Resolve source import from .context import BufferedPluginReporter, CancellationToken, PluginLogRecord; preserve alias and import-time effects. Then Evaluate once 32; assign in source target order to MAX_CORRELATION_PROVIDERS. Then Evaluate once 5000; assign in source target order to MAX_ACCEPTED_TOUCHING_CORRELATIONS.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:47-65
// Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:46-46
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:47-65
interface ProviderRunLimits {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:48-52
  In source order: For max_edges_per_provider, assign 1000; source annotation int. Then For max_total_edges, assign 5000; source annotation int. Then For max_reader_queries, assign 256; source annotation int. Then For max_rows_per_query, assign 1000; source annotation int. Then For max_total_rows, assign 10000; source annotation int.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:54-65
  // Source signature: __post_init__(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __post_init__(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:55-65
    if (the source predicate min(self.max_edges_per_provider, self.max_total_edges, self.max_reader_queries, self.max_rows_per_query, self.max_total_rows) <= 0 is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:65-65
      Raise ModelValidationError('correlation limits must be positive').
    }
    If execution reaches this end, finish with the source implicit None result.
  }
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:68-137
interface CorrelationProviderRegistry {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:69-90
  // Source signature: __init__(self, providers: Iterable[object]=()) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self, providers) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:70-70
    In source order: Evaluate once tuple(providers); assign in source target order to candidates.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:71-72
    if (the source predicate len(candidates) > MAX_CORRELATION_PROVIDERS is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:72-72
      Raise ModelValidationError('correlation provider count exceeds bound').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:73-74
    In source order: For names, assign set(); source annotation set[str]. Then For registered, assign []; source annotation list[CorrelationProvider].
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:75-84
    for each provider in candidates {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:76-77
      if (the source predicate not isinstance(provider, CorrelationProvider) is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:77-77
        Raise ModelValidationError('provider must implement CorrelationProvider').
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:78-78
      In source order: Evaluate once provider.metadata; assign in source target order to metadata.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:79-80
      if (the source predicate metadata.phase != PluginPhase.CORRELATION is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:80-80
        Raise ModelValidationError('correlation provider must use correlation phase').
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:81-82
      if (the source predicate metadata.name in names is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:82-82
        Raise ModelValidationError(source_template_82_43).
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:83-84
      In source order: Evaluate names.add(metadata.name); retain side effects and discard the expression result. Then Evaluate registered.append(provider); retain side effects and discard the expression result.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:85-90
    In source order: Evaluate once tuple(sorted(registered, key=lambda provider: provider.metadata.ordering_key)); assign in source target order to self._providers. Then Evaluate once {provider.metadata.name: provider.metadata.version for provider in self._providers}; assign in source target order to self._versions.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:92-93
  // Source signature: __iter__(self) -> Iterator[CorrelationProvider]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __iter__(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:93-93
    End this invocation with iter(self._providers).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:95-96
  // Source signature: __bool__(self) -> bool
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __bool__(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:96-96
    End this invocation with bool(self._providers).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:98-106
  // Source signature: manifests(self, project_id: ProjectId, snapshot_id: SnapshotId) -> tuple[ProviderManifest, ...]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn manifests(self, project_id, snapshot_id) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:101-106
    End this invocation with tuple((ProviderManifest(project_id, snapshot_id, provider.metadata.name, provider.metadata.version) for provider in self._providers)).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:108-137
  // Source signature: preflight(self, project_id: ProjectId, manifests: tuple[ProviderManifest, ...], correlations: tuple[CorrelationEdge, ...]) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn preflight(self, project_id, manifests, correlations) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:114-120
    if (the source predicate len(manifests) > MAX_CORRELATION_PROVIDERS is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:115-120
      Raise PluginError('registry', PluginPhase.CORRELATION.value, 'accepted provider manifest count exceeds bound', context=source_template_119_24).
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:121-127
    if (the source predicate len(correlations) > MAX_ACCEPTED_TOUCHING_CORRELATIONS is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:122-127
      Raise PluginError('registry', PluginPhase.CORRELATION.value, 'accepted touching correlation count exceeds bound', context=source_template_126_24).
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:128-129
    In source order: Evaluate once {(manifest.provider_name, manifest.provider_version) for manifest in manifests}; assign in source target order to required. Then Evaluate required.update(((edge.provider_name, edge.provider_version) for edge in correlations)); retain side effects and discard the expression result.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:130-137
    for each (name, version) in sorted(required) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:131-137
      if (the source predicate self._versions.get(name) != version is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:132-137
        Raise PluginError(name, PluginPhase.CORRELATION.value, source_template_135_20, context=source_template_136_28).
      }
    }
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:140-140
In source order: Evaluate once Callable[[SnapshotLocator, str, FrozenMap, int, float], tuple[FrozenMap, ...]]; assign in source target order to AcceptedExecute.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:143-186
interface CorrelationEndpointValidator {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:144-144
  In source order: Retain source documentation literal source_literal_144_4; it is not a model call.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:146-161
  // Source signature: __init__(self, accepted: tuple[ProjectSnapshot, ...], execute: AcceptedExecute, max_checks: int, deadline_monotonic: float) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self, accepted, execute, max_checks, deadline_monotonic) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:153-160
    In source order: Evaluate once {(snapshot.project.project_id, snapshot.snapshot_id): snapshot.locator for snapshot in accepted}; assign in source target order to self._accepted. Then Evaluate once execute; assign in source target order to self._execute. Then Evaluate once max_checks; assign in source target order to self._max_checks. Then Evaluate once deadline_monotonic; assign in source target order to self._deadline_monotonic. Then Evaluate once 0; assign in source target order to self._checks.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:161-161
    In source order: For self._cache, assign {}; source annotation dict[tuple[ProjectId, SnapshotId, str, str], bool].
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:163-186
  // Source signature: exists(self, ref: NodeRef) -> bool
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn exists(self, ref) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:164-165
    In source order: Evaluate once (ref.project_id, ref.snapshot_id, ref.node_id, ref.local_id); assign in source target order to key. Then Evaluate once self._cache.get(key); assign in source target order to cached.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:166-167
    if (the source predicate cached is not None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:167-167
      End this invocation with cached.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:168-168
    In source order: Apply source augmented assignment self._checks += 1 with source evaluation/in-place semantics.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:169-170
    if (the source predicate self._checks > self._max_checks is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:170-170
      Raise ModelValidationError('endpoint validation work exceeds bound').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:171-171
    In source order: Evaluate once self._deadline_monotonic - time.monotonic(); assign in source target order to remaining.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:172-173
    if (the source predicate remaining <= 0 is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:173-173
      Raise ModelValidationError('endpoint validation deadline exceeded').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:174-174
    In source order: Evaluate once self._accepted.get((ref.project_id, ref.snapshot_id)); assign in source target order to locator.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:175-176
    if (the source predicate locator is None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:176-176
      End this invocation with False.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:177-185
    In source order: Evaluate once self._execute(locator, 'MATCH (n {id:$id}) RETURN n.localId AS localId LIMIT 2', freeze_properties({'id': ref.node_id}), 2, remaining); assign in source target order to rows. Then Evaluate once len(rows) == 1 and rows[0]['localId'] == ref.local_id; assign in source target order to exists. Then Evaluate once exists; assign in source target order to self._cache[key].
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:186-186
    End this invocation with exists.
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:189-229
interface BoundedAcceptedGraphReader {
  Describe the source Python type, preserving its base/metaclass expression order: AcceptedGraphReader.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:190-205
  // Source signature: __init__(self, accepted: tuple[ProjectSnapshot, ...], execute: AcceptedExecute, limits: ProviderRunLimits, deadline_monotonic: float) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self, accepted, execute, limits, deadline_monotonic) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:197-204
    In source order: Evaluate once {(snapshot.project.project_id, snapshot.snapshot_id): snapshot.locator for snapshot in accepted}; assign in source target order to self._accepted. Then Evaluate once execute; assign in source target order to self._execute. Then Evaluate once limits; assign in source target order to self._limits. Then Evaluate once deadline_monotonic; assign in source target order to self._deadline_monotonic. Then Evaluate once 0; assign in source target order to self._queries.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:205-205
    In source order: Evaluate once 0; assign in source target order to self._rows.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:207-229
  // Source signature: query(self, locator: SnapshotLocator, cypher: str, parameters: FrozenMap, row_limit: int) -> tuple[FrozenMap, ...]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn query(self, locator, cypher, parameters, row_limit) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:214-214
    In source order: Evaluate once self._accepted.get((locator.project_id, locator.snapshot_id)); assign in source target order to expected.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:215-216
    if (the source predicate expected != locator is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:216-216
      Raise SnapshotLifecycleError('provider requested an unaccepted snapshot locator').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:217-218
    if (the source predicate not 1 <= row_limit <= self._limits.max_rows_per_query is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:218-218
      Raise ModelValidationError('provider read row limit exceeds bound').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:219-219
    In source order: Apply source augmented assignment self._queries += 1 with source evaluation/in-place semantics.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:220-221
    if (the source predicate self._queries > self._limits.max_reader_queries is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:221-221
      Raise ModelValidationError('provider read query count exceeds bound').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:222-222
    In source order: Evaluate once self._deadline_monotonic - time.monotonic(); assign in source target order to remaining.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:223-224
    if (the source predicate remaining <= 0 is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:224-224
      Raise ModelValidationError('provider read deadline exceeded').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:225-226
    In source order: Evaluate once self._execute(locator, cypher, parameters, row_limit, remaining); assign in source target order to rows. Then Apply source augmented assignment self._rows += len(rows) with source evaluation/in-place semantics.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:227-228
    if (the source predicate self._rows > self._limits.max_total_rows is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:228-228
      Raise ModelValidationError('provider read total row count exceeds bound').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:229-229
    End this invocation with rows.
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:233-238
// Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:232-232
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:233-238
interface CorrelationRunResult {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:234-238
  In source order: For node_refs, declare without assigning a value; source annotation tuple[NodeRef, ...]. Then For correlations, declare without assigning a value; source annotation tuple[CorrelationEdge, ...]. Then For manifests, declare without assigning a value; source annotation tuple[ProviderManifest, ...]. Then For logs, declare without assigning a value; source annotation tuple[PluginLogRecord, ...]. Then For diagnostics, declare without assigning a value; source annotation tuple[PluginDiagnostic, ...].
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:241-341
interface CorrelationRunner {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:242-243
  // Source signature: __init__(self, limits: ProviderRunLimits | None=None) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self, limits) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:243-243
    In source order: Evaluate once limits or ProviderRunLimits(); assign in source target order to self._limits.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:246-247
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:245-245
  Before creating this callable, evaluate and retain decorators top-to-bottom: property.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:246-247
  // Source signature: limits(self) -> ProviderRunLimits
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn limits(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:247-247
    End this invocation with self._limits.
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:249-341
  // Source signature: run(self, candidate: GraphSnapshot, accepted: tuple[ProjectSnapshot, ...], registry: CorrelationProviderRegistry, *, graph_reader: BoundedAcceptedGraphReader, endpoint_validator: CorrelationEndpointValidator, reporter: BufferedPluginReporter, cancellation: CancellationToken, deadline_monotonic: float, configuration: FrozenMap) -> CorrelationRunResult
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn run(self, candidate, accepted, registry, graph_reader, endpoint_validator, reporter, cancellation, deadline_monotonic, configuration) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:262-270
    In source order: Evaluate once {(snapshot.project.project_id, snapshot.snapshot_id): snapshot for snapshot in accepted}; assign in source target order to accepted_by_identity. Then Evaluate once {node.id: node for node in candidate.nodes}; assign in source target order to candidate_nodes. Then For correlations, assign []; source annotation list[CorrelationEdge]. Then For seen, assign set(); source annotation set[tuple[str, str, str, str, str]]. Then Evaluate once source_template_269_12; assign in source target order to context_label.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:271-329
    for each provider in registry {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:272-282
      In source order: Evaluate once provider.metadata; assign in source target order to metadata. Then Evaluate _check_lifecycle(metadata, cancellation, deadline_monotonic, context_label); retain side effects and discard the expression result. Then Evaluate once CorrelationContext(candidate, accepted, graph_reader, reporter, configuration, cancellation, deadline_monotonic); assign in source target order to context.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:283-329
      Perform the following protected operations {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:284-284
        In source order: Evaluate once _require_correlations(provider.correlate(context)); assign in source target order to emitted.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:285-286
        if (the source predicate len(emitted) > self._limits.max_edges_per_provider is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:286-286
          Raise ModelValidationError('provider correlation fan-out exceeds bound').
        }
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:287-308
        for each edge in emitted {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:288-302
          In source order: Evaluate _validate_correlation(edge, metadata, candidate, candidate_nodes, accepted_by_identity, endpoint_validator); retain side effects and discard the expression result. Then Evaluate once (edge.source.node_id, edge.relationship_type.value, edge.target.node_id, edge.provider_name, edge.provider_version); assign in source target order to key.
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:303-304
          if (the source predicate key in seen is truthy) {
            // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:304-304
            Raise ModelValidationError('provider emitted duplicate correlation').
          }
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:305-306
          In source order: Evaluate seen.add(key); retain side effects and discard the expression result. Then Evaluate correlations.append(edge); retain side effects and discard the expression result.
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:307-308
          if (the source predicate len(correlations) > self._limits.max_total_edges is truthy) {
            // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:308-308
            Raise ModelValidationError('aggregate correlation fan-out exceeds bound').
          }
        }
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:309-309
        In source order: Evaluate _check_lifecycle(metadata, cancellation, deadline_monotonic, context_label); retain side effects and discard the expression result.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:310-322
      On the first matching source exception PluginError as exc, in handler order {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:311-316
        if (the source predicate exc.plugin_name == metadata.name and exc.phase == metadata.phase.value and (exc.context == context_label) is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:316-316
          Raise the currently handled exception.
        }
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:317-322
        Raise PluginError(metadata.name, metadata.phase.value, str(exc), context=context_label) with explicit source cause exc.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:323-329
      On the first matching source exception Exception as exc, in handler order {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:324-329
        Raise PluginError(metadata.name, metadata.phase.value, str(exc), context=context_label) with explicit source cause exc.
      }
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:330-334
    In source order: Evaluate once {(ref.project_id, ref.snapshot_id, ref.node_id): ref for edge in correlations for ref in (edge.source, edge.target)}; assign in source target order to refs.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:335-341
    End this invocation with CorrelationRunResult(tuple(sorted(refs.values(), key=_ref_key)), tuple(sorted(correlations, key=_edge_key)), registry.manifests(candidate.project.project_id, candidate.snapshot_id), reporter.logs, reporter.diagnostics).
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:344-350
// Source signature: _require_correlations(value: object) -> tuple[CorrelationEdge, ...]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _require_correlations(value) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:345-346
  if (the source predicate not isinstance(value, tuple) is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:346-346
    Raise ModelValidationError('provider must return a tuple of correlations').
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:347-347
  In source order: Evaluate once cast(tuple[object, ...], value); assign in source target order to values.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:348-349
  if (the source predicate any((not isinstance(edge, CorrelationEdge) for edge in values)) is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:349-349
    Raise ModelValidationError('provider must return a tuple of correlations').
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:350-350
  End this invocation with cast(tuple[CorrelationEdge, ...], values).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:353-381
// Source signature: _validate_correlation(edge: CorrelationEdge, metadata: PluginMetadata, candidate: GraphSnapshot, candidate_nodes: dict[str, GraphNode], accepted: dict[tuple[ProjectId, SnapshotId], ProjectSnapshot], endpoint_validator: CorrelationEndpointValidator) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _validate_correlation(edge, metadata, candidate, candidate_nodes, accepted, endpoint_validator) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:361-362
  if (the source predicate edge.provider_name != metadata.name or edge.provider_version != metadata.version is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:362-362
    Raise ModelValidationError('correlation ownership does not match provider metadata').
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:363-369
  In source order: Evaluate once (candidate.project.project_id, candidate.snapshot_id); assign in source target order to candidate_identity. Then Evaluate once (edge.source, edge.target); assign in source target order to endpoints. Then Evaluate once [endpoint for endpoint in endpoints if (endpoint.project_id, endpoint.snapshot_id) == candidate_identity]; assign in source target order to candidate_endpoints.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:370-371
  if (the source predicate len(candidate_endpoints) != 1 is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:371-371
    Raise ModelValidationError('correlation must have exactly one current candidate endpoint').
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:372-373
  In source order: Evaluate once candidate_endpoints[0]; assign in source target order to candidate_endpoint. Then Evaluate once candidate_nodes.get(candidate_endpoint.node_id); assign in source target order to candidate_node.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:374-375
  if (the source predicate candidate_node is None or candidate_node.local_id != candidate_endpoint.local_id is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:375-375
    Raise ModelValidationError('candidate correlation endpoint does not exist').
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:376-377
  In source order: Evaluate once edge.target if edge.source == candidate_endpoint else edge.source; assign in source target order to target. Then Evaluate once accepted.get((target.project_id, target.snapshot_id)); assign in source target order to target_snapshot.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:378-379
  if (the source predicate target_snapshot is None is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:379-379
    Raise ModelValidationError('correlation target is not an accepted snapshot').
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:380-381
  if (the source predicate not endpoint_validator.exists(target) is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:381-381
    Raise ModelValidationError('accepted correlation endpoint does not exist').
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:384-400
// Source signature: _check_lifecycle(metadata: PluginMetadata, cancellation: CancellationToken, deadline: float, context: str) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _check_lifecycle(metadata, cancellation, deadline, context) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:390-393
  if (the source predicate cancellation.is_cancelled is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:391-393
    Raise PluginError(metadata.name, metadata.phase.value, 'provider cancelled', context=context).
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:394-400
  if (the source predicate time.monotonic() >= deadline is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:395-400
    Raise PluginError(metadata.name, metadata.phase.value, 'provider deadline exceeded', context=context).
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:403-404
// Source signature: _ref_key(ref: NodeRef) -> tuple[str, str, str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _ref_key(ref) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:404-404
  End this invocation with (ref.project_id.value, ref.snapshot_id.value, ref.node_id).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:407-414
// Source signature: _edge_key(edge: CorrelationEdge) -> tuple[str, str, str, str, str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _edge_key(edge) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py:408-414
  End this invocation with (edge.source.node_id, edge.relationship_type.value, edge.target.node_id, edge.provider_name, edge.provider_version).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from context_graph_sdk.errors import ModelValidationError, PluginError, SnapshotLifecycleError` at source line 24: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/errors.py.sudo.md`.
- `from context_graph_sdk.identity import ProjectId, SnapshotId` at source line 25: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/identity.py.sudo.md`.
- `from context_graph_sdk.models import CorrelationEdge, FrozenMap, GraphNode, GraphSnapshot, NodeRef, ProjectSnapshot, ProviderManifest, SnapshotLocator, freeze_properties` at source line 26: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/models.py.sudo.md`.
- `from context_graph_sdk.pipeline import AcceptedGraphReader, CorrelationContext, PluginDiagnostic` at source line 37: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/pipeline/__init__.py.sudo.md`.
- `from .base import CorrelationProvider, PluginMetadata, PluginPhase` at source line 39: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/plugins/base.py.sudo.md`.
- `from .context import BufferedPluginReporter, CancellationToken, PluginLogRecord` at source line 40: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/plugins/context.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../../../prompt_representation/vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py.sudo.md). Exact strings in the evidence asset support this conversion.
