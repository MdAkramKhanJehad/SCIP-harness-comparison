# vvaharness/backends/harness/deepagents/options/forcing.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/backends/harness/deepagents/options/forcing.py.evidence.json`. SHA-256: `b3f8753762ac6984e98c160a970b8de3c4ccda65311d7459b0faa3ede71faa6a`.

```sudo
// Source: vvaharness/backends/harness/deepagents/options/forcing.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import warnings; preserve alias and import-time effects. Then Resolve source import from typing import Any; preserve alias and import-time effects. Then Resolve source import from langchain_anthropic import ChatAnthropic; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/deepagents/options/forcing.py:22-29
In source order: Resolve source import from langchain_core.runnables import Runnable; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.counters import COUNTERS; preserve alias and import-time effects. Then Evaluate once ['ForcingChatAnthropic']; assign in source target order to __all__. Then Evaluate once 'tool_choice is forced but thinking is enabled'; assign in source target order to _DROP_MESSAGE. Then Evaluate once ('any', 'tool'); assign in source target order to _FORCED_TYPES.
// Source: vvaharness/backends/harness/deepagents/options/forcing.py:32-40
// Source signature: _forced_choice(tool_choice: Any) -> dict[str, Any] | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _forced_choice(tool_choice) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/options/forcing.py:33-33
  In source order: Retain source documentation literal source_literal_33_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/options/forcing.py:34-35
  if (the source predicate isinstance(tool_choice, dict) is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/forcing.py:35-35
    End this invocation with dict(tool_choice) if tool_choice.get('type') in _FORCED_TYPES else None.
  }
  // Source: vvaharness/backends/harness/deepagents/options/forcing.py:36-37
  if (the source predicate tool_choice in _FORCED_TYPES is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/forcing.py:37-37
    End this invocation with {'type': tool_choice}.
  }
  // Source: vvaharness/backends/harness/deepagents/options/forcing.py:38-39
  if (the source predicate isinstance(tool_choice, str) is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/forcing.py:39-39
    End this invocation with {'type': 'tool', 'name': tool_choice}.
  }
  // Source: vvaharness/backends/harness/deepagents/options/forcing.py:40-40
  End this invocation with None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/options/forcing.py:43-66
interface ForcingChatAnthropic {
  Describe the source Python type, preserving its base/metaclass expression order: ChatAnthropic.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/harness/deepagents/options/forcing.py:44-47
  In source order: Retain source documentation literal source_literal_44_4; it is not a model call. Then For force_tool_choice, assign True; source annotation bool.
  // Source: vvaharness/backends/harness/deepagents/options/forcing.py:49-66
  // Source signature: bind_tools(self, tools: Any, *, tool_choice: Any=None, **kwargs: Any) -> Runnable[Any, Any]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn bind_tools(self, tools, tool_choice, kwargs) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/options/forcing.py:51-51
    In source order: Retain source documentation literal source_literal_51_8; it is not a model call.
    // Source: vvaharness/backends/harness/deepagents/options/forcing.py:52-53
    if (the source predicate not self.force_tool_choice is truthy) {
      // Source: vvaharness/backends/harness/deepagents/options/forcing.py:53-53
      End this invocation with super().bind_tools(tools, tool_choice=None, **kwargs).
    }
    // Source: vvaharness/backends/harness/deepagents/options/forcing.py:59-60
    In source order: Evaluate once _forced_choice(tool_choice); assign in source target order to forced. Then Evaluate once (self.thinking or {}).get('type') == 'adaptive'; assign in source target order to adaptive.
    // Source: vvaharness/backends/harness/deepagents/options/forcing.py:61-62
    if (the source predicate forced is None or not adaptive is truthy) {
      // Source: vvaharness/backends/harness/deepagents/options/forcing.py:62-62
      End this invocation with super().bind_tools(tools, tool_choice=tool_choice, **kwargs).
    }
    // Source: vvaharness/backends/harness/deepagents/options/forcing.py:63-65
    Enter source context managers left-to-right: warnings.catch_warnings() {
      // Source: vvaharness/backends/harness/deepagents/options/forcing.py:64-65
      In source order: Evaluate warnings.filterwarnings('ignore', message=_DROP_MESSAGE, category=UserWarning); retain side effects and discard the expression result. Then Evaluate once super().bind_tools(tools, tool_choice=tool_choice, **kwargs); assign in source target order to bound.
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    // Source: vvaharness/backends/harness/deepagents/options/forcing.py:66-66
    End this invocation with _reforce(bound, forced).
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vvaharness/backends/harness/deepagents/options/forcing.py:69-80
// Source signature: _reforce(bound: Runnable[Any, Any], forced: dict[str, Any]) -> Runnable[Any, Any]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _reforce(bound, forced) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/options/forcing.py:70-71
  In source order: Retain source documentation literal source_literal_70_4; it is not a model call. Then Evaluate once getattr(bound, 'kwargs', None); assign in source target order to held.
  // Source: vvaharness/backends/harness/deepagents/options/forcing.py:72-73
  if (the source predicate not isinstance(held, dict) is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/forcing.py:73-73
    End this invocation with bound.
  }
  // Source: vvaharness/backends/harness/deepagents/options/forcing.py:74-75
  if (the source predicate held.get('tool_choice', {}).get('type') in _FORCED_TYPES is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/forcing.py:75-75
    End this invocation with bound.
  }
  // Source: vvaharness/backends/harness/deepagents/options/forcing.py:76-76
  In source order: Evaluate once held.get('tool_choice') or {}; assign in source target order to existing.
  // Source: vvaharness/backends/harness/deepagents/options/forcing.py:77-78
  if (the source predicate 'disable_parallel_tool_use' in existing is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/forcing.py:78-78
    In source order: Evaluate once existing['disable_parallel_tool_use']; assign in source target order to forced['disable_parallel_tool_use'].
  }
  // Source: vvaharness/backends/harness/deepagents/options/forcing.py:79-79
  In source order: Evaluate COUNTERS.bump('deepagents_tool_choice_reforced_under_adaptive_thinking'); retain side effects and discard the expression result.
  // Source: vvaharness/backends/harness/deepagents/options/forcing.py:80-80
  End this invocation with bound.bind(tool_choice=forced).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.util.counters import COUNTERS` at source line 24: `source_detail/vvaharness/util/counters.py.sudo.md`.
