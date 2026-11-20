# vvaharness/sdk/loading.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/sdk/loading.py.evidence.json`. SHA-256: `1f0d39fe492a3b87d5ba86e9fe3ae6b504a0d99bac8b7f6e0b18b2d5fbb36a9d`.

```sudo
// Source: vvaharness/sdk/loading.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from collections.abc import Callable; preserve alias and import-time effects. Then Resolve source import from importlib import import_module; preserve alias and import-time effects. Then Resolve source import from vvaharness.sdk.plugins import PluginSet, VvahPlugin; preserve alias and import-time effects.
// Source: vvaharness/sdk/loading.py:22-32
In source order: Resolve source import from vvaharness.util import logs; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.config import knob; preserve alias and import-time effects. Then Evaluate once logs.get_logger(__name__); assign in source target order to log. Then For BUILTIN_PLUGINS, assign {'semgrep': 'vvaharness.plugins.semgrep:SemgrepPlugin'}; source annotation dict[str, str].
// Source: vvaharness/sdk/loading.py:35-45
// Source signature: _plugin_specs(cfg: object) -> tuple[dict, ...]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _plugin_specs(cfg) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/sdk/loading.py:36-37
  In source order: Retain source documentation literal source_literal_36_4; it is not a model call. Then Evaluate once knob(cfg, 'sdk.plugins', []) or []; assign in source target order to raw.
  // Source: vvaharness/sdk/loading.py:38-39
  if (the source predicate not isinstance(raw, (list, tuple)) is truthy) {
    // Source: vvaharness/sdk/loading.py:39-39
    Raise TypeError('sdk.plugins must be a list of mappings').
  }
  // Source: vvaharness/sdk/loading.py:40-40
  In source order: Evaluate once []; assign in source target order to specs.
  // Source: vvaharness/sdk/loading.py:41-44
  for each entry in raw {
    // Source: vvaharness/sdk/loading.py:42-43
    if (the source predicate not isinstance(entry, dict) or not entry.get('name') is truthy) {
      // Source: vvaharness/sdk/loading.py:43-43
      Raise TypeError(source_template_43_28).
    }
    // Source: vvaharness/sdk/loading.py:44-44
    In source order: Evaluate specs.append(dict(entry)); retain side effects and discard the expression result.
  }
  // Source: vvaharness/sdk/loading.py:45-45
  End this invocation with tuple(specs).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/sdk/loading.py:48-59
// Source signature: _built(spec: dict) -> VvahPlugin
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _built(spec) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/sdk/loading.py:49-52
  In source order: Retain source documentation literal source_literal_49_4; it is not a model call. Then Evaluate once dict(spec); assign in source target order to options. Then Evaluate once options.pop('name'); assign in source target order to name. Then Evaluate once BUILTIN_PLUGINS.get(name); assign in source target order to target.
  // Source: vvaharness/sdk/loading.py:53-54
  if (the source predicate target is None is truthy) {
    // Source: vvaharness/sdk/loading.py:54-54
    Raise ValueError(source_template_54_25).
  }
  // Source: vvaharness/sdk/loading.py:55-55
  In source order: Evaluate once _resolve(target); assign in source target order to factory.
  // Source: vvaharness/sdk/loading.py:56-58
  for each key in ('configs', 'rulesets') {
    // Source: vvaharness/sdk/loading.py:57-58
    if (the source predicate key in options is truthy) {
      // Source: vvaharness/sdk/loading.py:58-58
      In source order: Evaluate once tuple(options[key] or ()); assign in source target order to options[key].
    }
  }
  // Source: vvaharness/sdk/loading.py:59-59
  End this invocation with factory(**options).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/sdk/loading.py:62-65
// Source signature: _resolve(target: str) -> Callable[..., VvahPlugin]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _resolve(target) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/sdk/loading.py:63-64
  In source order: Retain source documentation literal source_literal_63_4; it is not a model call. Then Evaluate once target.partition(':'); assign in source target order to (module_name, _, attr).
  // Source: vvaharness/sdk/loading.py:65-65
  End this invocation with getattr(import_module(module_name), attr).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/sdk/loading.py:68-75
// Source signature: load_plugin_set(cfg: object) -> PluginSet
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn load_plugin_set(cfg) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/sdk/loading.py:69-70
  In source order: Retain source documentation literal source_literal_69_4; it is not a model call. Then Evaluate once _plugin_specs(cfg); assign in source target order to specs.
  // Source: vvaharness/sdk/loading.py:71-72
  if (the source predicate not specs is truthy) {
    // Source: vvaharness/sdk/loading.py:72-72
    End this invocation with PluginSet().
  }
  // Source: vvaharness/sdk/loading.py:73-74
  In source order: Evaluate once PluginSet([_built(spec) for spec in specs]); assign in source target order to plugins. Then Evaluate log.info('sdk plugins loaded: %s', ', '.join(plugins.names)); retain side effects and discard the expression result.
  // Source: vvaharness/sdk/loading.py:75-75
  End this invocation with plugins.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/sdk/loading.py:78-78
In source order: Evaluate once ['BUILTIN_PLUGINS', 'load_plugin_set']; assign in source target order to __all__.
```

## Local import links

- `from vvaharness.sdk.plugins import PluginSet, VvahPlugin` at source line 21: `source_detail/vvaharness/sdk/plugins.py.sudo.md`.
- `from vvaharness.util import logs` at source line 22: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import logs` at source line 22: `source_detail/vvaharness/util/logs.py.sudo.md`.
- `from vvaharness.util.config import knob` at source line 23: `source_detail/vvaharness/util/config.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../prompt_representation/vvaharness/sdk/loading.py.sudo.md). Exact strings in the evidence asset support this conversion.
