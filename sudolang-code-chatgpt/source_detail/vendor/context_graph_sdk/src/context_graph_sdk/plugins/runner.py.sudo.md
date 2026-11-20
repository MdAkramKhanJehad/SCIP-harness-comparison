# vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py.evidence.json`. SHA-256: `b6859d2c4b9594babbafe3da4f1a767a2cc978cca49cd6cb8fdf54e030dc9d19`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import time; preserve alias and import-time effects. Then Resolve source import from collections.abc import Callable; preserve alias and import-time effects. Then Resolve source import from dataclasses import dataclass; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:23-28
In source order: Resolve source import from context_graph_sdk.errors import ModelValidationError, PluginError; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.models import FrozenMap, GraphEdge, GraphMutation, GraphNode, GraphSnapshot; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.pipeline import PluginContext, PluginDiagnostic, SourceReader; preserve alias and import-time effects. Then Resolve source import from .base import PluginMetadata, PluginPhase; preserve alias and import-time effects. Then Resolve source import from .context import BufferedPluginReporter, CancellationToken, PluginLogRecord; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:29-31
In source order: Resolve source import from .registry import PluginRegistry; preserve alias and import-time effects. Then Evaluate once 300.0; assign in source target order to DEFAULT_LOCAL_PLUGIN_TIMEOUT_SECONDS.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:35-51
// Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:34-34
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:35-51
interface LocalPluginLimits {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:36-39
  In source order: For max_nodes_per_plugin, assign 10000; source annotation int. Then For max_edges_per_plugin, assign 20000; source annotation int. Then For max_removals_per_plugin, assign 20000; source annotation int. Then For max_total_work, assign 50000; source annotation int.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:41-51
  // Source signature: __post_init__(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __post_init__(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:42-51
    if (the source predicate min(self.max_nodes_per_plugin, self.max_edges_per_plugin, self.max_removals_per_plugin, self.max_total_work) <= 0 is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:51-51
      Raise ModelValidationError('local plugin limits must be positive').
    }
    If execution reaches this end, finish with the source implicit None result.
  }
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:55-59
// Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:54-54
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:55-59
interface LocalPluginResult {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:56-59
  In source order: For snapshot, declare without assigning a value; source annotation GraphSnapshot. Then For executed, declare without assigning a value; source annotation tuple[PluginMetadata, ...]. Then For logs, declare without assigning a value; source annotation tuple[PluginLogRecord, ...]. Then For diagnostics, declare without assigning a value; source annotation tuple[PluginDiagnostic, ...].
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:62-171
interface LocalPluginRunner {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:63-64
  // Source signature: __init__(self, limits: LocalPluginLimits | None=None) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self, limits) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:64-64
    In source order: Evaluate once limits or LocalPluginLimits(); assign in source target order to self._limits.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:66-139
  // Source signature: run(self, snapshot: GraphSnapshot, registry: PluginRegistry, *, source_reader: SourceReader, cancellation: CancellationToken, deadline_monotonic: float, configuration: FrozenMap, derive: Callable[[GraphSnapshot], GraphSnapshot] | None=None) -> LocalPluginResult
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn run(self, snapshot, registry, source_reader, cancellation, deadline_monotonic, configuration, derive) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:77-83
    In source order: Evaluate once snapshot; assign in source target order to current. Then Evaluate once BufferedPluginReporter(); assign in source target order to reporter. Then For executed, assign []; source annotation list[PluginMetadata]. Then Evaluate once 0; assign in source target order to total_work. Then Evaluate once source_template_82_12; assign in source target order to context_label.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:84-138
    for each phase in (PluginPhase.PRE_DERIVATION, PluginPhase.POST_DERIVATION) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:85-128
      for each plugin in registry.for_phase(phase) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:86-96
        In source order: Evaluate once plugin.metadata; assign in source target order to metadata. Then Evaluate self._check_lifecycle(metadata, cancellation, deadline_monotonic, context_label); retain side effects and discard the expression result. Then Evaluate once PluginContext(snapshot.project, current, source_reader, reporter, cancellation, configuration, deadline_monotonic); assign in source target order to context.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:97-125
        Perform the following protected operations {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:98-99
          In source order: Evaluate once _require_mutation(plugin.enrich(context)); assign in source target order to mutation. Then Evaluate once self._validate_bounds(mutation); assign in source target order to work.
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:100-101
          if (the source predicate total_work + work > self._limits.max_total_work is truthy) {
            // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:101-101
            Raise ModelValidationError('aggregate local plugin work exceeds bound').
          }
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:102-103
          In source order: Evaluate once _apply_mutation(current, mutation); assign in source target order to candidate. Then Evaluate self._check_lifecycle(metadata, cancellation, deadline_monotonic, context_label); retain side effects and discard the expression result.
        }
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:104-118
        On the first matching source exception PluginError as exc, in handler order {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:107-112
          if (the source predicate exc.plugin_name == metadata.name and exc.phase == metadata.phase.value and (exc.context == context_label) is truthy) {
            // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:112-112
            Raise the currently handled exception.
          }
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:113-118
          Raise PluginError(metadata.name, metadata.phase.value, str(exc), context=context_label) with explicit source cause exc.
        }
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:119-125
        On the first matching source exception Exception as exc, in handler order {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:120-125
          Raise PluginError(metadata.name, metadata.phase.value, str(exc), context=context_label) with explicit source cause exc.
        }
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:126-128
        In source order: Evaluate once candidate; assign in source target order to current. Then Apply source augmented assignment total_work += work with source evaluation/in-place semantics. Then Evaluate executed.append(metadata); retain side effects and discard the expression result.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:129-138
      if (the source predicate phase == PluginPhase.PRE_DERIVATION and derive is not None is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:130-130
        In source order: Evaluate once derive(current); assign in source target order to derived.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:131-137
        if (the source predicate derived.project != snapshot.project or derived.snapshot_id != snapshot.snapshot_id is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:135-137
          Raise ModelValidationError('derived graph changed the candidate project or snapshot identity').
        }
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:138-138
        In source order: Evaluate once derived; assign in source target order to current.
      }
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:139-139
    End this invocation with LocalPluginResult(current, tuple(executed), reporter.logs, reporter.diagnostics).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:141-149
  // Source signature: _validate_bounds(self, mutation: GraphMutation) -> int
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _validate_bounds(self, mutation) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:142-142
    In source order: Evaluate once len(mutation.removed_node_ids) + len(mutation.removed_edge_ids); assign in source target order to removals.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:143-144
    if (the source predicate len(mutation.nodes) > self._limits.max_nodes_per_plugin is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:144-144
      Raise ModelValidationError('plugin node emission exceeds bound').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:145-146
    if (the source predicate len(mutation.edges) > self._limits.max_edges_per_plugin is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:146-146
      Raise ModelValidationError('plugin edge emission exceeds bound').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:147-148
    if (the source predicate removals > self._limits.max_removals_per_plugin is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:148-148
      Raise ModelValidationError('plugin removal emission exceeds bound').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:149-149
    End this invocation with len(mutation.nodes) + len(mutation.edges) + removals.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:152-171
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:151-151
  Before creating this callable, evaluate and retain decorators top-to-bottom: staticmethod.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:152-171
  // Source signature: _check_lifecycle(metadata: PluginMetadata, cancellation: CancellationToken, deadline_monotonic: float, context: str) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _check_lifecycle(metadata, cancellation, deadline_monotonic, context) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:158-164
    if (the source predicate cancellation.is_cancelled is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:159-164
      Raise PluginError(metadata.name, metadata.phase.value, 'plugin execution cancelled', context=context).
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:165-171
    if (the source predicate time.monotonic() >= deadline_monotonic is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:166-171
      Raise PluginError(metadata.name, metadata.phase.value, 'plugin execution deadline exceeded', context=context).
    }
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:174-177
// Source signature: _require_mutation(value: object) -> GraphMutation
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _require_mutation(value) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:175-176
  if (the source predicate not isinstance(value, GraphMutation) is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:176-176
    Raise ModelValidationError('plugin must return GraphMutation').
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:177-177
  End this invocation with value.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:180-222
// Source signature: _apply_mutation(snapshot: GraphSnapshot, mutation: GraphMutation) -> GraphSnapshot
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _apply_mutation(snapshot, mutation) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:181-182
  if (the source predicate mutation.project_id != snapshot.project.project_id is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:182-182
    Raise ModelValidationError('plugin mutation targets another project').
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:183-187
  In source order: For nodes, assign {node.id: node for node in snapshot.nodes}; source annotation dict[str, GraphNode]. Then For edges, assign {edge.id: edge for edge in snapshot.edges}; source annotation dict[str, GraphEdge]. Then Evaluate once set(mutation.removed_node_ids).difference(nodes); assign in source target order to missing_nodes. Then Evaluate once set(mutation.removed_edge_ids); assign in source target order to removed_edge_ids. Then Evaluate once removed_edge_ids.difference(edges); assign in source target order to missing_edges.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:188-189
  if (the source predicate missing_nodes or missing_edges is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:189-189
    Raise ModelValidationError('plugin mutation removes unknown graph identities').
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:190-197
  In source order: Evaluate once {edge_id: edge for edge_id, edge in edges.items() if edge_id not in removed_edge_ids}; assign in source target order to remaining_edges. Then Evaluate once {endpoint for edge in remaining_edges.values() for endpoint in (edge.source_id, edge.target_id)}; assign in source target order to remaining_endpoints.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:198-203
  for each node_id in mutation.removed_node_ids {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:199-202
    if (the source predicate node_id in remaining_endpoints is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:200-202
      Raise ModelValidationError('plugin must explicitly remove edges incident to removed nodes').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:203-203
    In source order: Delete source targets in order: nodes[node_id].
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:204-205
  for each edge_id in mutation.removed_edge_ids {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:205-205
    In source order: Evaluate edges.pop(edge_id); retain side effects and discard the expression result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:206-209
  for each node in mutation.nodes {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:207-208
    if (the source predicate node.id in nodes is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:208-208
      Raise ModelValidationError('plugin adds an existing node identity').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:209-209
    In source order: Evaluate once node; assign in source target order to nodes[node.id].
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:210-215
  for each edge in mutation.edges {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:211-212
    if (the source predicate edge.id in edges is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:212-212
      Raise ModelValidationError('plugin adds an existing edge identity').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:213-214
    if (the source predicate edge.source_id not in nodes or edge.target_id not in nodes is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:214-214
      Raise ModelValidationError('plugin edge endpoints must exist in the candidate graph').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:215-215
    In source order: Evaluate once edge; assign in source target order to edges[edge.id].
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py:216-222
  End this invocation with GraphSnapshot(snapshot.project, snapshot.snapshot_id, snapshot.analysis_version, tuple(nodes.values()), tuple(edges.values())).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from context_graph_sdk.errors import ModelValidationError, PluginError` at source line 23: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/errors.py.sudo.md`.
- `from context_graph_sdk.models import FrozenMap, GraphEdge, GraphMutation, GraphNode, GraphSnapshot` at source line 24: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/models.py.sudo.md`.
- `from context_graph_sdk.pipeline import PluginContext, PluginDiagnostic, SourceReader` at source line 25: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/pipeline/__init__.py.sudo.md`.
- `from .base import PluginMetadata, PluginPhase` at source line 27: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/plugins/base.py.sudo.md`.
- `from .context import BufferedPluginReporter, CancellationToken, PluginLogRecord` at source line 28: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/plugins/context.py.sudo.md`.
- `from .registry import PluginRegistry` at source line 29: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/plugins/registry.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../../../prompt_representation/vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py.sudo.md). Exact strings in the evidence asset support this conversion.
