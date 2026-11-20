# vvaharness/util/warn_once.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/util/warn_once.py.evidence.json`. SHA-256: `b51b3037a4c819a51d455e34603d2d85e7a078c0ed72be1286f2f054a5a24fca`.

```sudo
// Source: vvaharness/util/warn_once.py:15-23
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import sys; preserve alias and import-time effects. Then Resolve source import import threading; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import console; preserve alias and import-time effects.
// Source: vvaharness/util/warn_once.py:25-29
In source order: Evaluate once ['reset_warn_once_registries', 'stage_label', 'warn_once']; assign in source target order to __all__. Then Evaluate once threading.Lock(); assign in source target order to _LOCK.
// Source: vvaharness/util/warn_once.py:32-39
// Source signature: warn_once(seen: set[str], key: str, message: str) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn warn_once(seen, key, message) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/warn_once.py:33-33
  In source order: Retain source documentation literal source_literal_33_4; it is not a model call.
  // Source: vvaharness/util/warn_once.py:35-38
  Enter source context managers left-to-right: _LOCK {
    // Source: vvaharness/util/warn_once.py:36-37
    if (the source predicate key in seen is truthy) {
      // Source: vvaharness/util/warn_once.py:37-37
      End this invocation with None.
    }
    // Source: vvaharness/util/warn_once.py:38-38
    In source order: Evaluate seen.add(key); retain side effects and discard the expression result.
  }
  Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
  // Source: vvaharness/util/warn_once.py:39-39
  In source order: Evaluate console.write(message); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/warn_once.py:42-47
// Source signature: stage_label(counter: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn stage_label(counter) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/warn_once.py:43-46
  In source order: Retain source documentation literal source_literal_43_4; it is not a model call. Then Evaluate once counter.split('_', 1)[0]; assign in source target order to prefix.
  // Source: vvaharness/util/warn_once.py:47-47
  End this invocation with source_template_47_11 if prefix[:1] == 's' and prefix[1:].isdigit() else '[stage]'.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/warn_once.py:51-83
In source order: For _REGISTRY_SITES, assign (('vvaharness.backends.llm.deepagents', '_NO_USAGE_WARNED_TAGS'), ('vvaharness.backends.llm.deepagents', '_WARNED_LEGACY_KW'), ('vvaharness.backends.llm.sdk', '_CACHE_ROUTE_NOTED'), ('vvaharness.backends.harness.deepagents.tools', '_WARNED_UNKNOWN_TOOLS'), ('vvaharness.backends.harness.deepagents.usage', '_EXCLUSIVE_USAGE_WARNED'), ('vvaharness.backends.harness.deepagents.client', '_EFFORT_UNSUPPORTED_WARNED'), ('vvaharness.backends.harness.deepagents.client', '_TRANSPORT_FALLBACK_WARNED'), ('vvaharness.orchestrator.store', '_PERM_WARNED'), ('vvaharness.backends.llm.openai', '_WARNED_DROPS'), ('vvaharness.backends.llm.sdk', '_WARNED_DROPS'), ('vvaharness.backends.llm.tool_adapter', '_WARNED'), ('vvaharness.backends.llm.cli_mcp', '_WARNED'), ('vvaharness.backends.llm.deepagents', '_WARNED_DROPPED_KNOBS'), ('vvaharness.backends.llm.registry', '_WARNED_CLI_DROPPED'), ('vvaharness.backends.llm.cli', '_WARNED_CAPS'), ('vvaharness.pipeline.stages.s2.session', '_WARNED_NO_GRAPH_TOOLS'), ('vvaharness.pipeline.stages.s2.session', '_WARNED_DEGENERATE_GRAPH'), ('vvaharness.pipeline.stages.s4.session', '_WARNED_DEGENERATE_GRAPH'), ('vvaharness.pipeline.stages.s6.session', '_WARNED_NO_GRAPH'), ('vvaharness.pipeline.stages.s6.session', '_WARNED_DEGENERATE_GRAPH'), ('vvaharness.backends.harness.deepagents.options.model_building', '_INFERRED_VENDOR_WARNED'), ('vvaharness.remediation_agent.plugin_runner', '_WARNED_CLI_REDACTION'), ('vvaharness.pipeline.stages.s4_deepdive', '_WARNED_REDACTED_SOURCE'), ('vvaharness.pipeline.stages.s6_verify', '_WARNED_REPLAYED_DISCOVERIES'), ('vvaharness.validation.config.validate_role', '_WARNED_VIA_REWRITE'), ('vvaharness.backends.harness.deepagents.tool_budget', '_WARNED_EXHAUSTED'), ('vvaharness.backends.harness.deepagents.evidence_gate', '_WARNED_RELENTED'), ('vvaharness.backends.harness.deepagents.options.response_format', '_WARNED_DROPS')); source annotation tuple[tuple[str, str], ...].
// Source: vvaharness/util/warn_once.py:86-94
// Source signature: reset_warn_once_registries() -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn reset_warn_once_registries() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/warn_once.py:87-87
  In source order: Retain source documentation literal source_literal_87_4; it is not a model call.
  // Source: vvaharness/util/warn_once.py:88-94
  for each (mod_name, attr) in _REGISTRY_SITES {
    // Source: vvaharness/util/warn_once.py:89-89
    In source order: Evaluate once sys.modules.get(mod_name); assign in source target order to mod.
    // Source: vvaharness/util/warn_once.py:90-91
    if (the source predicate mod is None is truthy) {
      // Source: vvaharness/util/warn_once.py:91-91
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/util/warn_once.py:92-92
    In source order: Evaluate once getattr(mod, attr, None); assign in source target order to reg.
    // Source: vvaharness/util/warn_once.py:93-94
    if (the source predicate isinstance(reg, set) is truthy) {
      // Source: vvaharness/util/warn_once.py:94-94
      In source order: Evaluate reg.clear(); retain side effects and discard the expression result.
    }
  }
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.util import console` at source line 23: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import console` at source line 23: `source_detail/vvaharness/util/console.py.sudo.md`.
