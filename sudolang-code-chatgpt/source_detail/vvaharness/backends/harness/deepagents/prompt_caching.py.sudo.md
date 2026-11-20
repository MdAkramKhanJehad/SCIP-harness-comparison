# vvaharness/backends/harness/deepagents/prompt_caching.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/backends/harness/deepagents/prompt_caching.py.evidence.json`. SHA-256: `4aa2b8f42eb877beac9e6bc6dd6bedfef8146d15d11ec6c16909dcf4e87a804d`.

```sudo
// Source: vvaharness/backends/harness/deepagents/prompt_caching.py:15-27
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from typing import TYPE_CHECKING, Final; preserve alias and import-time effects. Then Resolve source import from langchain_anthropic.middleware.prompt_caching import AnthropicPromptCachingMiddleware, _tag_system_message, _tag_tools; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/deepagents/prompt_caching.py:29-31
if (the source predicate TYPE_CHECKING is truthy) {
  // Source: vvaharness/backends/harness/deepagents/prompt_caching.py:30-31
  In source order: Resolve source import from langchain.agents.middleware.types import ModelRequest; preserve alias and import-time effects. Then Resolve source import from langchain_core.messages import AnyMessage; preserve alias and import-time effects.
}
// Source: vvaharness/backends/harness/deepagents/prompt_caching.py:34-42
In source order: For _TTL, assign '5m'; source annotation Final. Then For _UNSUPPORTED_MODEL_BEHAVIOR, assign 'ignore'; source annotation Final. Then For _INELIGIBLE_TAIL_BLOCK_TYPES, assign frozenset({'thinking', 'redacted_thinking'}); source annotation Final[frozenset[str]].
// Source: vvaharness/backends/harness/deepagents/prompt_caching.py:45-58
// Source signature: _tagged_block(block: str | dict[str, object], cache_control: dict[str, str]) -> dict[str, object] | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _tagged_block(block, cache_control) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/prompt_caching.py:48-48
  In source order: Retain source documentation literal source_literal_48_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/prompt_caching.py:49-55
  if (the source predicate isinstance(block, str) is truthy) {
    // Source: vvaharness/backends/harness/deepagents/prompt_caching.py:50-54
    In source order: For promoted, assign {'type': 'text', 'text': block, 'cache_control': cache_control}; source annotation dict[str, object].
    // Source: vvaharness/backends/harness/deepagents/prompt_caching.py:55-55
    End this invocation with promoted if block else None.
  }
  // Source: vvaharness/backends/harness/deepagents/prompt_caching.py:56-57
  if (the source predicate isinstance(block, dict) and block.get('type') not in _INELIGIBLE_TAIL_BLOCK_TYPES is truthy) {
    // Source: vvaharness/backends/harness/deepagents/prompt_caching.py:57-57
    End this invocation with {**block, 'cache_control': cache_control}.
  }
  // Source: vvaharness/backends/harness/deepagents/prompt_caching.py:58-58
  End this invocation with None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/prompt_caching.py:61-69
// Source signature: _tag_blocks(content: list[str | dict[str, object]], cache_control: dict[str, str]) -> list[str | dict[str, object]] | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _tag_blocks(content, cache_control) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/prompt_caching.py:64-64
  In source order: Retain source documentation literal source_literal_64_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/prompt_caching.py:65-68
  for each index in range(len(content) - 1, -1, -1) {
    // Source: vvaharness/backends/harness/deepagents/prompt_caching.py:66-66
    In source order: Evaluate once _tagged_block(content[index], cache_control); assign in source target order to tagged.
    // Source: vvaharness/backends/harness/deepagents/prompt_caching.py:67-68
    if (the source predicate tagged is not None is truthy) {
      // Source: vvaharness/backends/harness/deepagents/prompt_caching.py:68-68
      End this invocation with [*content[:index], tagged, *content[index + 1:]].
    }
  }
  // Source: vvaharness/backends/harness/deepagents/prompt_caching.py:69-69
  End this invocation with None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/prompt_caching.py:72-79
// Source signature: _tag_content(content: str | list[str | dict[str, object]], cache_control: dict[str, str]) -> list[str | dict[str, object]] | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _tag_content(content, cache_control) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/prompt_caching.py:75-75
  In source order: Retain source documentation literal source_literal_75_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/prompt_caching.py:76-78
  if (the source predicate isinstance(content, str) is truthy) {
    // Source: vvaharness/backends/harness/deepagents/prompt_caching.py:77-77
    In source order: Evaluate once _tagged_block(content, cache_control); assign in source target order to block.
    // Source: vvaharness/backends/harness/deepagents/prompt_caching.py:78-78
    End this invocation with None if block is None else [block].
  }
  // Source: vvaharness/backends/harness/deepagents/prompt_caching.py:79-79
  End this invocation with _tag_blocks(content, cache_control).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/prompt_caching.py:82-92
// Source signature: _tag_tail(messages: list[AnyMessage], cache_control: dict[str, str]) -> list[AnyMessage] | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _tag_tail(messages, cache_control) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/prompt_caching.py:85-85
  In source order: Retain source documentation literal source_literal_85_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/prompt_caching.py:86-87
  if (the source predicate not messages is truthy) {
    // Source: vvaharness/backends/harness/deepagents/prompt_caching.py:87-87
    End this invocation with None.
  }
  // Source: vvaharness/backends/harness/deepagents/prompt_caching.py:88-89
  In source order: Evaluate once messages[-1]; assign in source target order to last. Then Evaluate once _tag_content(last.content, cache_control); assign in source target order to new_content.
  // Source: vvaharness/backends/harness/deepagents/prompt_caching.py:90-91
  if (the source predicate new_content is None is truthy) {
    // Source: vvaharness/backends/harness/deepagents/prompt_caching.py:91-91
    End this invocation with None.
  }
  // Source: vvaharness/backends/harness/deepagents/prompt_caching.py:92-92
  End this invocation with [*messages[:-1], last.model_copy(update={'content': new_content})].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/prompt_caching.py:95-124
interface BlockMarkerPromptCaching {
  Describe the source Python type, preserving its base/metaclass expression order: AnthropicPromptCachingMiddleware.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/harness/deepagents/prompt_caching.py:96-96
  In source order: Retain source documentation literal source_literal_96_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/prompt_caching.py:98-102
  // Source signature: __init__(self, *, enabled: bool=True, mark_tail: bool=True) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self, enabled, mark_tail) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/prompt_caching.py:99-102
    In source order: Retain source documentation literal source_literal_99_8; it is not a model call. Then Evaluate super().__init__(ttl=_TTL, unsupported_model_behavior=_UNSUPPORTED_MODEL_BEHAVIOR); retain side effects and discard the expression result. Then Evaluate once enabled; assign in source target order to self._enabled. Then Evaluate once mark_tail; assign in source target order to self._mark_tail.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/deepagents/prompt_caching.py:105-107
  // Source: vvaharness/backends/harness/deepagents/prompt_caching.py:104-104
  Before creating this callable, evaluate and retain decorators top-to-bottom: property.
  // Source: vvaharness/backends/harness/deepagents/prompt_caching.py:105-107
  // Source signature: name(self) -> str
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn name(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/prompt_caching.py:106-106
    In source order: Retain source documentation literal source_literal_106_8; it is not a model call.
    // Source: vvaharness/backends/harness/deepagents/prompt_caching.py:107-107
    End this invocation with AnthropicPromptCachingMiddleware.__name__.
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vvaharness/backends/harness/deepagents/prompt_caching.py:109-111
  // Source signature: _should_apply_caching(self, request: ModelRequest) -> bool
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _should_apply_caching(self, request) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/prompt_caching.py:110-110
    In source order: Retain source documentation literal source_literal_110_8; it is not a model call.
    // Source: vvaharness/backends/harness/deepagents/prompt_caching.py:111-111
    End this invocation with self._enabled and super()._should_apply_caching(request).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/deepagents/prompt_caching.py:113-124
  // Source signature: _apply_caching(self, request: ModelRequest) -> ModelRequest
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _apply_caching(self, request) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/prompt_caching.py:114-119
    In source order: Retain source documentation literal source_literal_114_8; it is not a model call. Then Evaluate once self._cache_control; assign in source target order to cache_control. Then Evaluate once _tag_system_message(request.system_message, cache_control); assign in source target order to system_message. Then Evaluate once _tag_tools(request.tools, cache_control); assign in source target order to tools. Then Evaluate once _tag_tail(request.messages, cache_control) if self._mark_tail else None; assign in source target order to tail.
    // Source: vvaharness/backends/harness/deepagents/prompt_caching.py:120-124
    End this invocation with request.override(system_message=system_message, tools=request.tools if tools is None else tools, messages=request.messages if tail is None else tail).
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vvaharness/backends/harness/deepagents/prompt_caching.py:127-127
In source order: Evaluate once ['BlockMarkerPromptCaching']; assign in source target order to __all__.
```

## Local import links

No statically resolved in-checkout import; external calls remain explicit dependency boundaries.
