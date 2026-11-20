# vvaharness/sdk/plugins.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/sdk/plugins.py.evidence.json`. SHA-256: `bbfcd9f3832f0e7d0d8a7da6e68900ef43b466228451c9fef79396f12b814448`.

```sudo
// Source: vvaharness/sdk/plugins.py:15-20
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from collections.abc import Iterable, Mapping; preserve alias and import-time effects. Then Resolve source import from dataclasses import dataclass, field, replace; preserve alias and import-time effects. Then Resolve source import from typing import Protocol, runtime_checkable; preserve alias and import-time effects.
// Source: vvaharness/sdk/plugins.py:22-32
In source order: Resolve source import from context_graph_sdk.plugins import GraphEnricher; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness import SubagentDefinition; preserve alias and import-time effects. Then Resolve source import from vvaharness.codegraph.tools import ToolFactory, clear_plugin_graph_tools, register_graph_tools; preserve alias and import-time effects. Then Evaluate once 16; assign in source target order to MAX_PLUGINS. Then Evaluate once 8; assign in source target order to MAX_PLUGIN_GRAPH_TOOLS.
// Source: vvaharness/sdk/plugins.py:33-33
In source order: Evaluate once 64; assign in source target order to _MAX_NAME_LENGTH.
// Source: vvaharness/sdk/plugins.py:37-54
// Source: vvaharness/sdk/plugins.py:36-36
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vvaharness/sdk/plugins.py:37-54
interface PluginInfo {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/sdk/plugins.py:38-42
  In source order: Retain source documentation literal source_literal_38_4; it is not a model call. Then For name, declare without assigning a value; source annotation str. Then For version, declare without assigning a value; source annotation str. Then For priority, assign 100; source annotation int.
  // Source: vvaharness/sdk/plugins.py:44-49
  // Source signature: __post_init__(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __post_init__(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/sdk/plugins.py:45-45
    In source order: Retain source documentation literal source_literal_45_8; it is not a model call.
    // Source: vvaharness/sdk/plugins.py:46-47
    if (the source predicate not self.name or not self.version is truthy) {
      // Source: vvaharness/sdk/plugins.py:47-47
      Raise ValueError('plugin name and version are required').
    }
    // Source: vvaharness/sdk/plugins.py:48-49
    if (the source predicate len(self.name) > _MAX_NAME_LENGTH is truthy) {
      // Source: vvaharness/sdk/plugins.py:49-49
      Raise ValueError(source_template_49_29).
    }
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/sdk/plugins.py:52-54
  // Source: vvaharness/sdk/plugins.py:51-51
  Before creating this callable, evaluate and retain decorators top-to-bottom: property.
  // Source: vvaharness/sdk/plugins.py:52-54
  // Source signature: ordering_key(self) -> tuple[int, str]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn ordering_key(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/sdk/plugins.py:53-53
    In source order: Retain source documentation literal source_literal_53_8; it is not a model call.
    // Source: vvaharness/sdk/plugins.py:54-54
    End this invocation with (self.priority, self.name).
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vvaharness/sdk/plugins.py:58-75
// Source: vvaharness/sdk/plugins.py:57-57
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vvaharness/sdk/plugins.py:58-75
interface Contribution {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/sdk/plugins.py:59-63
  In source order: Retain source documentation literal source_literal_59_4; it is not a model call. Then For enrichers, assign (); source annotation tuple[GraphEnricher, ...]. Then For graph_tools, assign field(default_factory=dict); source annotation Mapping[str, ToolFactory]. Then For subagents, assign (); source annotation tuple[SubagentDefinition, ...].
  // Source: vvaharness/sdk/plugins.py:65-75
  // Source signature: merge(self, other: Contribution) -> Contribution
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn merge(self, other) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/sdk/plugins.py:66-67
    In source order: Retain source documentation literal source_literal_66_8; it is not a model call. Then Evaluate once set(self.graph_tools) & set(other.graph_tools); assign in source target order to clashes.
    // Source: vvaharness/sdk/plugins.py:68-69
    if (the source predicate clashes is truthy) {
      // Source: vvaharness/sdk/plugins.py:69-69
      Raise ValueError(source_template_69_29).
    }
    // Source: vvaharness/sdk/plugins.py:70-75
    End this invocation with replace(self, enrichers=self.enrichers + other.enrichers, graph_tools={**self.graph_tools, **other.graph_tools}, subagents=self.subagents + other.subagents).
    If execution reaches this end, finish with the source implicit None result.
  }
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vvaharness/sdk/plugins.py:79-89
// Source: vvaharness/sdk/plugins.py:78-78
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: runtime_checkable.
// Source: vvaharness/sdk/plugins.py:79-89
interface VvahPlugin {
  Describe the source Python type, preserving its base/metaclass expression order: Protocol.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/sdk/plugins.py:80-80
  In source order: Retain source documentation literal source_literal_80_4; it is not a model call.
  // Source: vvaharness/sdk/plugins.py:83-85
  // Source: vvaharness/sdk/plugins.py:82-82
  Before creating this callable, evaluate and retain decorators top-to-bottom: property.
  // Source: vvaharness/sdk/plugins.py:83-85
  // Source signature: info(self) -> PluginInfo
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn info(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/sdk/plugins.py:84-85
    In source order: Retain source documentation literal source_literal_84_8; it is not a model call. Then Evaluate ...; retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vvaharness/sdk/plugins.py:87-89
  // Source signature: contribute(self) -> Contribution
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn contribute(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/sdk/plugins.py:88-89
    In source order: Retain source documentation literal source_literal_88_8; it is not a model call. Then Evaluate ...; retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vvaharness/sdk/plugins.py:92-106
// Source signature: _validated(plugins: tuple[object, ...]) -> tuple[VvahPlugin, ...]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _validated(plugins) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/sdk/plugins.py:93-93
  In source order: Retain source documentation literal source_literal_93_4; it is not a model call.
  // Source: vvaharness/sdk/plugins.py:94-95
  if (the source predicate len(plugins) > MAX_PLUGINS is truthy) {
    // Source: vvaharness/sdk/plugins.py:95-95
    Raise ValueError(source_template_95_25).
  }
  // Source: vvaharness/sdk/plugins.py:96-97
  In source order: For seen, assign set(); source annotation set[str]. Then For checked, assign []; source annotation list[VvahPlugin].
  // Source: vvaharness/sdk/plugins.py:98-105
  for each plugin in plugins {
    // Source: vvaharness/sdk/plugins.py:99-100
    if (the source predicate not isinstance(plugin, VvahPlugin) is truthy) {
      // Source: vvaharness/sdk/plugins.py:100-100
      Raise TypeError(source_template_100_28).
    }
    // Source: vvaharness/sdk/plugins.py:101-101
    In source order: Evaluate once plugin.info.name; assign in source target order to name.
    // Source: vvaharness/sdk/plugins.py:102-103
    if (the source predicate name in seen is truthy) {
      // Source: vvaharness/sdk/plugins.py:103-103
      Raise ValueError(source_template_103_29).
    }
    // Source: vvaharness/sdk/plugins.py:104-105
    In source order: Evaluate seen.add(name); retain side effects and discard the expression result. Then Evaluate checked.append(plugin); retain side effects and discard the expression result.
  }
  // Source: vvaharness/sdk/plugins.py:106-106
  End this invocation with tuple(sorted(checked, key=lambda p: p.info.ordering_key)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/sdk/plugins.py:109-144
interface PluginSet {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/sdk/plugins.py:110-110
  In source order: Retain source documentation literal source_literal_110_4; it is not a model call.
  // Source: vvaharness/sdk/plugins.py:112-120
  // Source signature: __init__(self, plugins: Iterable[object]=()) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self, plugins) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/sdk/plugins.py:113-115
    In source order: Retain source documentation literal source_literal_113_8; it is not a model call. Then Evaluate once _validated(tuple(plugins)); assign in source target order to self._plugins. Then Evaluate once Contribution(); assign in source target order to merged.
    // Source: vvaharness/sdk/plugins.py:116-117
    for each plugin in self._plugins {
      // Source: vvaharness/sdk/plugins.py:117-117
      In source order: Evaluate once merged.merge(plugin.contribute()); assign in source target order to merged.
    }
    // Source: vvaharness/sdk/plugins.py:118-119
    if (the source predicate len(merged.graph_tools) > MAX_PLUGIN_GRAPH_TOOLS is truthy) {
      // Source: vvaharness/sdk/plugins.py:119-119
      Raise ValueError(source_template_119_29).
    }
    // Source: vvaharness/sdk/plugins.py:120-120
    In source order: Evaluate once merged; assign in source target order to self._contribution.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/sdk/plugins.py:122-124
  // Source signature: __len__(self) -> int
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __len__(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/sdk/plugins.py:123-123
    In source order: Retain source documentation literal source_literal_123_8; it is not a model call.
    // Source: vvaharness/sdk/plugins.py:124-124
    End this invocation with len(self._plugins).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/sdk/plugins.py:126-128
  // Source signature: __bool__(self) -> bool
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __bool__(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/sdk/plugins.py:127-127
    In source order: Retain source documentation literal source_literal_127_8; it is not a model call.
    // Source: vvaharness/sdk/plugins.py:128-128
    End this invocation with bool(self._plugins).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/sdk/plugins.py:131-133
  // Source: vvaharness/sdk/plugins.py:130-130
  Before creating this callable, evaluate and retain decorators top-to-bottom: property.
  // Source: vvaharness/sdk/plugins.py:131-133
  // Source signature: names(self) -> tuple[str, ...]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn names(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/sdk/plugins.py:132-132
    In source order: Retain source documentation literal source_literal_132_8; it is not a model call.
    // Source: vvaharness/sdk/plugins.py:133-133
    End this invocation with tuple((p.info.name for p in self._plugins)).
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vvaharness/sdk/plugins.py:136-138
  // Source: vvaharness/sdk/plugins.py:135-135
  Before creating this callable, evaluate and retain decorators top-to-bottom: property.
  // Source: vvaharness/sdk/plugins.py:136-138
  // Source signature: contribution(self) -> Contribution
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn contribution(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/sdk/plugins.py:137-137
    In source order: Retain source documentation literal source_literal_137_8; it is not a model call.
    // Source: vvaharness/sdk/plugins.py:138-138
    End this invocation with self._contribution.
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vvaharness/sdk/plugins.py:140-144
  // Source signature: install_graph_tools(self) -> tuple[str, ...]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn install_graph_tools(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/sdk/plugins.py:141-143
    In source order: Retain source documentation literal source_literal_141_8; it is not a model call. Then Evaluate clear_plugin_graph_tools(); retain side effects and discard the expression result. Then Evaluate register_graph_tools(self._contribution.graph_tools); retain side effects and discard the expression result.
    // Source: vvaharness/sdk/plugins.py:144-144
    End this invocation with tuple(self._contribution.graph_tools).
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vvaharness/sdk/plugins.py:147-155
In source order: Evaluate once ['MAX_PLUGINS', 'MAX_PLUGIN_GRAPH_TOOLS', 'Contribution', 'GraphEnricher', 'PluginInfo', 'PluginSet', 'VvahPlugin']; assign in source target order to __all__.
```

## Local import links

- `from context_graph_sdk.plugins import GraphEnricher` at source line 22: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/plugins/__init__.py.sudo.md`.
- `from vvaharness.backends.harness import SubagentDefinition` at source line 24: `source_detail/vvaharness/backends/harness/__init__.py.sudo.md`.
- `from vvaharness.codegraph.tools import ToolFactory, clear_plugin_graph_tools, register_graph_tools` at source line 25: `source_detail/vvaharness/codegraph/tools.py.sudo.md`.
