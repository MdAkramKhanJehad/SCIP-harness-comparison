# vvaharness/backends/harness/deepagents/evidence_gate.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/backends/harness/deepagents/evidence_gate.py.evidence.json`. SHA-256: `4a8fd9b1c518f83d7f39dc6d583497464c4ee5a3c2824f9e55966374ecd9dd56`.

```sudo
// Source: vvaharness/backends/harness/deepagents/evidence_gate.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import threading; preserve alias and import-time effects. Then Resolve source import from collections.abc import Awaitable, Callable; preserve alias and import-time effects. Then Resolve source import from typing import Any; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/deepagents/evidence_gate.py:23-33
In source order: Resolve source import from langchain.agents.middleware.types import AgentMiddleware, ModelRequest, ModelResponse, ToolCallRequest; preserve alias and import-time effects. Then Resolve source import from langchain_core.messages import HumanMessage, ToolMessage; preserve alias and import-time effects. Then Resolve source import from langgraph.types import Command; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.counters import COUNTERS; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.warn_once import stage_label, warn_once; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/deepagents/evidence_gate.py:35-37
In source order: Evaluate once frozenset({'completed'}); assign in source target order to _DONE. Then For _WARNED_RELENTED, assign set(); source annotation set[str].
// Source: vvaharness/backends/harness/deepagents/evidence_gate.py:40-48
// Source signature: _relent_warning(counter: str, max_rejections: int, required: frozenset[str]) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _relent_warning(counter, max_rejections, required) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:41-42
  In source order: Retain source documentation literal source_literal_41_4; it is not a model call. Then Evaluate once source_template_42_13 if required else 'an unfinished plan'; assign in source target order to reason.
  // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:43-48
  End this invocation with source_template_44_8.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/evidence_gate.py:51-57
// Source signature: _todos(state: object) -> list[dict[str, Any]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _todos(state) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:52-52
  In source order: Retain source documentation literal source_literal_52_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:53-56
  Perform the following protected operations {
    // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:54-54
    In source order: Evaluate once state.get('todos') if hasattr(state, 'get') else getattr(state, 'todos', None); assign in source target order to raw.
  }
  // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:55-56
  On the first matching source exception (AttributeError, TypeError), in handler order {
    // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:56-56
    End this invocation with [].
  }
  // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:57-57
  End this invocation with [t for t in raw or [] if isinstance(t, dict)].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/evidence_gate.py:60-62
// Source signature: _outstanding(todos: list[dict[str, Any]]) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _outstanding(todos) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:61-61
  In source order: Retain source documentation literal source_literal_61_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:62-62
  End this invocation with [str(t.get('content', '?')) for t in todos if t.get('status') not in _DONE].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/evidence_gate.py:65-77
// Source signature: _nudge(outstanding: list[str]) -> HumanMessage
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _nudge(outstanding) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:66-67
  In source order: Retain source documentation literal source_literal_66_4; it is not a model call. Then Evaluate once source_literal_67_13.join((source_template_67_23 for c in outstanding)); assign in source target order to listed.
  // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:68-77
  End this invocation with HumanMessage(content=source_template_69_8).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/evidence_gate.py:80-223
interface EvidenceGate {
  Describe the source Python type, preserving its base/metaclass expression order: AgentMiddleware.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:81-81
  In source order: Retain source documentation literal source_literal_81_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:83-97
  // Source signature: __init__(self, *, max_rejections: int=3, counter: str='evidence_gate_rejected', required_tools: frozenset[str]=frozenset(), require_tool_call: bool=False, ignored_tools: frozenset[str]=frozenset()) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self, max_rejections, counter, required_tools, require_tool_call, ignored_tools) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:88-92
    In source order: Retain source documentation literal source_literal_88_8; it is not a model call. Then Evaluate super().__init__(); retain side effects and discard the expression result. Then Evaluate once max_rejections; assign in source target order to self._max. Then Evaluate once counter; assign in source target order to self._counter. Then Evaluate once required_tools; assign in source target order to self._required.
    // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:93-97
    In source order: Evaluate once require_tool_call; assign in source target order to self._require_tool_call. Then Evaluate once ignored_tools; assign in source target order to self._ignored. Then For self._called, assign set(); source annotation set[str]. Then Evaluate once 0; assign in source target order to self._rejected. Then Evaluate once threading.Lock(); assign in source target order to self._lock.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:99-106
  // Source signature: wrap_tool_call(self, request: ToolCallRequest, handler: Callable[[ToolCallRequest], ToolMessage | Command[Any]]) -> ToolMessage | Command[Any]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn wrap_tool_call(self, request, handler) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:104-105
    In source order: Retain source documentation literal source_literal_104_8; it is not a model call. Then Evaluate self._called.add(request.tool_call['name']); retain side effects and discard the expression result.
    // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:106-106
    End this invocation with handler(request).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:108-115
  // Source signature: awrap_tool_call(self, request: ToolCallRequest, handler: Callable[[ToolCallRequest], Awaitable[ToolMessage | Command[Any]]]) -> ToolMessage | Command[Any]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn awrap_tool_call(self, request, handler) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    This callable produces a coroutine or async generator; await/suspension positions remain in source expressions.
    // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:113-114
    In source order: Retain source documentation literal source_literal_113_8; it is not a model call. Then Evaluate self._called.add(request.tool_call['name']); retain side effects and discard the expression result.
    // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:115-115
    End this invocation with await handler(request).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:118-120
  // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:117-117
  Before creating this callable, evaluate and retain decorators top-to-bottom: property.
  // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:118-120
  // Source signature: name(self) -> str
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn name(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:119-119
    In source order: Retain source documentation literal source_literal_119_8; it is not a model call.
    // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:120-120
    End this invocation with source_template_120_15.
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:123-126
  // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:122-122
  Before creating this callable, evaluate and retain decorators top-to-bottom: property.
  // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:123-126
  // Source signature: required_tools(self) -> frozenset[str]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn required_tools(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:124-124
    In source order: Retain source documentation literal source_literal_124_8; it is not a model call.
    // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:126-126
    End this invocation with self._required.
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:128-134
  // Source signature: _claim(self) -> bool
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _claim(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:129-129
    In source order: Retain source documentation literal source_literal_129_8; it is not a model call.
    // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:130-134
    Enter source context managers left-to-right: self._lock {
      // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:131-132
      if (the source predicate self._rejected >= self._max is truthy) {
        // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:132-132
        End this invocation with False.
      }
      // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:133-133
      In source order: Apply source augmented assignment self._rejected += 1 with source evaluation/in-place semantics.
      // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:134-134
      End this invocation with True.
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:136-140
  // Source signature: note_call(self, name: str) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn note_call(self, name) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:137-137
    In source order: Retain source documentation literal source_literal_137_8; it is not a model call.
    // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:139-140
    Enter source context managers left-to-right: self._lock {
      // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:140-140
      In source order: Evaluate self._called.add(name); retain side effects and discard the expression result.
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:142-162
  // Source signature: hold_for_verdict(self) -> str | None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn hold_for_verdict(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:143-143
    In source order: Retain source documentation literal source_literal_143_8; it is not a model call.
    // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:144-145
    if (the source predicate not self._required or self._required & self._called is truthy) {
      // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:145-145
      End this invocation with None.
    }
    // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:146-150
    if (the source predicate not self._claim() is truthy) {
      // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:147-149
      In source order: Evaluate COUNTERS.bump(source_template_147_26); retain side effects and discard the expression result. Then Evaluate warn_once(_WARNED_RELENTED, self._counter, _relent_warning(self._counter, self._max, self._required)); retain side effects and discard the expression result.
      // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:150-150
      End this invocation with None.
    }
    // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:151-151
    In source order: Evaluate COUNTERS.bump(self._counter); retain side effects and discard the expression result.
    // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:152-162
    End this invocation with 'Rejected: you have not called any of ' + ', '.join(sorted(self._required)) + source_literal_155_14.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:164-168
  // Source signature: _tool_call_items(self) -> list[str]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _tool_call_items(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:165-165
    In source order: Retain source documentation literal source_literal_165_8; it is not a model call.
    // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:166-167
    if (the source predicate self._require_tool_call and (not self._called - self._ignored) is truthy) {
      // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:167-167
      End this invocation with ['read the code with a tool before you report'].
    }
    // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:168-168
    End this invocation with [].
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:170-194
  // Source signature: _premature(self, request: ModelRequest, response: ModelResponse) -> list[str]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _premature(self, request, response) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:171-171
    In source order: Retain source documentation literal source_literal_171_8; it is not a model call.
    // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:172-173
    if (the source predicate getattr(response, 'structured_response', None) is None is truthy) {
      // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:173-173
      End this invocation with [].
    }
    // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:174-174
    In source order: Evaluate once _outstanding(_todos(request.state)); assign in source target order to outstanding.
    // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:175-184
    if (the source predicate self._required and (not self._required & self._called) is truthy) {
      // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:176-184
      In source order: Evaluate once [*outstanding, 'establish reachability from the call graph — you have not called any of ' + ', '.join(sorted(self._required)) + source_literal_179_18]; assign in source target order to outstanding.
    }
    // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:185-185
    In source order: Evaluate once [*outstanding, *self._tool_call_items()]; assign in source target order to outstanding.
    // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:186-187
    if (the source predicate not outstanding is truthy) {
      // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:187-187
      End this invocation with [].
    }
    // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:188-192
    if (the source predicate not self._claim() is truthy) {
      // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:189-191
      In source order: Evaluate COUNTERS.bump(source_template_189_26); retain side effects and discard the expression result. Then Evaluate warn_once(_WARNED_RELENTED, self._counter, _relent_warning(self._counter, self._max, self._required)); retain side effects and discard the expression result.
      // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:192-192
      End this invocation with [].
    }
    // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:193-193
    In source order: Evaluate COUNTERS.bump(self._counter); retain side effects and discard the expression result.
    // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:194-194
    End this invocation with outstanding.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:196-199
  // Source signature: _retry_request(self, request: ModelRequest, outstanding: list[str]) -> ModelRequest
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _retry_request(self, request, outstanding) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:197-197
    In source order: Retain source documentation literal source_literal_197_8; it is not a model call.
    // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:199-199
    End this invocation with request.override(messages=[*request.messages, _nudge(outstanding)]).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:201-211
  // Source signature: wrap_model_call(self, request: ModelRequest, handler: Callable[[ModelRequest], ModelResponse]) -> ModelResponse
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn wrap_model_call(self, request, handler) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:206-207
    In source order: Retain source documentation literal source_literal_206_8; it is not a model call. Then Evaluate once handler(request); assign in source target order to response.
    // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:208-210
    while (the source predicate (outstanding := self._premature(request, response)) is truthy) {
      // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:209-210
      In source order: Evaluate once self._retry_request(request, outstanding); assign in source target order to request. Then Evaluate once handler(request); assign in source target order to response.
    }
    // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:211-211
    End this invocation with response.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:213-223
  // Source signature: awrap_model_call(self, request: ModelRequest, handler: Callable[[ModelRequest], Awaitable[ModelResponse]]) -> ModelResponse
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn awrap_model_call(self, request, handler) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    This callable produces a coroutine or async generator; await/suspension positions remain in source expressions.
    // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:218-219
    In source order: Retain source documentation literal source_literal_218_8; it is not a model call. Then Evaluate once await handler(request); assign in source target order to response.
    // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:220-222
    while (the source predicate (outstanding := self._premature(request, response)) is truthy) {
      // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:221-222
      In source order: Evaluate once self._retry_request(request, outstanding); assign in source target order to request. Then Evaluate once await handler(request); assign in source target order to response.
    }
    // Source: vvaharness/backends/harness/deepagents/evidence_gate.py:223-223
    End this invocation with response.
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vvaharness/backends/harness/deepagents/evidence_gate.py:226-226
In source order: Evaluate once ['EvidenceGate']; assign in source target order to __all__.
```

## Local import links

- `from vvaharness.util.counters import COUNTERS` at source line 32: `source_detail/vvaharness/util/counters.py.sudo.md`.
- `from vvaharness.util.warn_once import stage_label, warn_once` at source line 33: `source_detail/vvaharness/util/warn_once.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../../prompt_representation/vvaharness/backends/harness/deepagents/evidence_gate.py.sudo.md). Exact strings in the evidence asset support this conversion.
