# vendor/context_graph_sdk/src/context_graph_sdk/plugins/registry.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vendor/context_graph_sdk/src/context_graph_sdk/plugins/registry.py.evidence.json`. SHA-256: `a044c1cc0ac5492458180152474a7b87641e32aa0fbd5122fa552a1883e4a4e0`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/registry.py:15-23
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from collections.abc import Iterable, Iterator; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.errors import ModelValidationError; preserve alias and import-time effects. Then Resolve source import from .base import GraphEnricher, PluginMetadata, PluginPhase; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/registry.py:25-29
In source order: Evaluate once 64; assign in source target order to MAX_LOCAL_PLUGINS. Then Evaluate once 128; assign in source target order to _MAX_NAME_LENGTH. Then Evaluate once 64; assign in source target order to _MAX_VERSION_LENGTH. Then Evaluate once 10000; assign in source target order to _MAX_PRIORITY. Then Evaluate once frozenset({PluginPhase.PRE_DERIVATION, PluginPhase.POST_DERIVATION}); assign in source target order to _LOCAL_PHASES.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/registry.py:32-62
interface PluginRegistry {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/registry.py:33-48
  // Source signature: __init__(self, plugins: Iterable[object]=()) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self, plugins) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/registry.py:34-34
    In source order: Evaluate once tuple(plugins); assign in source target order to candidates.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/registry.py:35-36
    if (the source predicate len(candidates) > MAX_LOCAL_PLUGINS is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/registry.py:36-36
      Raise ModelValidationError(source_template_36_39).
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/registry.py:37-38
    In source order: For registered, assign []; source annotation list[GraphEnricher]. Then For names, assign set(); source annotation set[str].
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/registry.py:39-47
    for each plugin in candidates {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/registry.py:40-41
      if (the source predicate not isinstance(plugin, GraphEnricher) is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/registry.py:41-41
        Raise ModelValidationError('local plugin must implement GraphEnricher').
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/registry.py:42-43
      In source order: Evaluate once plugin.metadata; assign in source target order to metadata. Then Evaluate _validate_metadata(metadata); retain side effects and discard the expression result.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/registry.py:44-45
      if (the source predicate metadata.name in names is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/registry.py:45-45
        Raise ModelValidationError(source_template_45_43).
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/registry.py:46-47
      In source order: Evaluate names.add(metadata.name); retain side effects and discard the expression result. Then Evaluate registered.append(plugin); retain side effects and discard the expression result.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/registry.py:48-48
    In source order: Evaluate once tuple(sorted(registered, key=lambda plugin: plugin.metadata.ordering_key)); assign in source target order to self._plugins.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/registry.py:50-51
  // Source signature: __bool__(self) -> bool
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __bool__(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/registry.py:51-51
    End this invocation with bool(self._plugins).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/registry.py:53-54
  // Source signature: __len__(self) -> int
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __len__(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/registry.py:54-54
    End this invocation with len(self._plugins).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/registry.py:56-57
  // Source signature: __iter__(self) -> Iterator[GraphEnricher]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __iter__(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/registry.py:57-57
    End this invocation with iter(self._plugins).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/registry.py:59-62
  // Source signature: for_phase(self, phase: PluginPhase) -> tuple[GraphEnricher, ...]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn for_phase(self, phase) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/registry.py:60-61
    if (the source predicate phase not in _LOCAL_PHASES is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/registry.py:61-61
      Raise ModelValidationError(source_template_61_39).
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/registry.py:62-62
    End this invocation with tuple((plugin for plugin in self._plugins if plugin.metadata.phase == phase)).
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/registry.py:65-75
// Source signature: _validate_metadata(metadata: PluginMetadata) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _validate_metadata(metadata) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/registry.py:66-69
  if (the source predicate metadata.phase not in _LOCAL_PHASES is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/registry.py:67-69
    Raise ModelValidationError(source_template_68_12).
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/registry.py:70-71
  if (the source predicate len(metadata.name) > _MAX_NAME_LENGTH is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/registry.py:71-71
    Raise ModelValidationError('plugin name exceeds bound').
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/registry.py:72-73
  if (the source predicate len(metadata.version) > _MAX_VERSION_LENGTH is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/registry.py:73-73
    Raise ModelValidationError('plugin version exceeds bound').
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/registry.py:74-75
  if (the source predicate not -_MAX_PRIORITY <= metadata.priority <= _MAX_PRIORITY is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/registry.py:75-75
    Raise ModelValidationError('plugin priority exceeds bound').
  }
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from context_graph_sdk.errors import ModelValidationError` at source line 21: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/errors.py.sudo.md`.
- `from .base import GraphEnricher, PluginMetadata, PluginPhase` at source line 23: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/plugins/base.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../../../prompt_representation/vendor/context_graph_sdk/src/context_graph_sdk/plugins/registry.py.sudo.md). Exact strings in the evidence asset support this conversion.
