# vvaharness/backends/harness/deepagents/invalid_tool_args.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/backends/harness/deepagents/invalid_tool_args.py.evidence.json`. SHA-256: `2084025bed69d1c10118fec15a0fff39fbc17df437dbf0619e35f9dc4479c2d2`.

```sudo
// Source: vvaharness/backends/harness/deepagents/invalid_tool_args.py:15-25
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from typing import TYPE_CHECKING, Any; preserve alias and import-time effects. Then Resolve source import from langchain.agents.middleware.types import AgentMiddleware; preserve alias and import-time effects. Then Resolve source import from langchain_core.messages import AIMessage, AnyMessage, InvalidToolCall, ToolMessage; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/deepagents/invalid_tool_args.py:27-27
In source order: Resolve source import from vvaharness.util.counters import COUNTERS; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/deepagents/invalid_tool_args.py:29-32
if (the source predicate TYPE_CHECKING is truthy) {
  // Source: vvaharness/backends/harness/deepagents/invalid_tool_args.py:30-32
  In source order: Resolve source import from collections.abc import Awaitable, Callable, Sequence; preserve alias and import-time effects. Then Resolve source import from langchain.agents.middleware.types import ModelCallResult, ModelRequest; preserve alias and import-time effects.
}
// Source: vvaharness/backends/harness/deepagents/invalid_tool_args.py:35-40
// Source signature: _repair_block(block: Any, repaired_ids: frozenset[str]) -> Any
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _repair_block(block, repaired_ids) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/invalid_tool_args.py:36-36
  In source order: Retain source documentation literal source_literal_36_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/invalid_tool_args.py:37-39
  if (the source predicate isinstance(block, dict) and block.get('type') == 'function_call' and (block.get('call_id') in repaired_ids) is truthy) {
    // Source: vvaharness/backends/harness/deepagents/invalid_tool_args.py:39-39
    End this invocation with {**block, 'arguments': '{}'}.
  }
  // Source: vvaharness/backends/harness/deepagents/invalid_tool_args.py:40-40
  End this invocation with block.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/invalid_tool_args.py:43-55
// Source signature: _record_invalid_call(invalid: InvalidToolCall, call_id: str, existing_tool_message_ids: frozenset[str], counted_ids: set[str]) -> ToolMessage | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _record_invalid_call(invalid, call_id, existing_tool_message_ids, counted_ids) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/invalid_tool_args.py:47-47
  In source order: Retain source documentation literal source_literal_47_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/invalid_tool_args.py:48-50
  if (the source predicate call_id not in counted_ids is truthy) {
    // Source: vvaharness/backends/harness/deepagents/invalid_tool_args.py:49-50
    In source order: Evaluate counted_ids.add(call_id); retain side effects and discard the expression result. Then Evaluate COUNTERS.bump('deepagents_tool_args_invalid_json'); retain side effects and discard the expression result.
  }
  // Source: vvaharness/backends/harness/deepagents/invalid_tool_args.py:51-52
  if (the source predicate call_id in existing_tool_message_ids is truthy) {
    // Source: vvaharness/backends/harness/deepagents/invalid_tool_args.py:52-52
    End this invocation with None.
  }
  // Source: vvaharness/backends/harness/deepagents/invalid_tool_args.py:53-53
  In source order: Evaluate once invalid.get('error') or 'arguments were not valid JSON'; assign in source target order to error.
  // Source: vvaharness/backends/harness/deepagents/invalid_tool_args.py:54-55
  End this invocation with ToolMessage(content=source_template_54_31, tool_call_id=call_id, name=invalid.get('name')).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/invalid_tool_args.py:58-87
// Source signature: _repair_message(message: AIMessage, existing_tool_message_ids: frozenset[str], counted_ids: set[str]) -> tuple[AIMessage, list[ToolMessage]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _repair_message(message, existing_tool_message_ids, counted_ids) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/invalid_tool_args.py:61-69
  In source order: Retain source documentation literal source_literal_61_4; it is not a model call. Then For repaired_ids, assign set(); source annotation set[str]. Then Evaluate once list(message.tool_calls); assign in source target order to new_tool_calls. Then For remaining_invalid, assign []; source annotation list[InvalidToolCall]. Then For extra_tool_messages, assign []; source annotation list[ToolMessage].
  // Source: vvaharness/backends/harness/deepagents/invalid_tool_args.py:70-80
  for each invalid in message.invalid_tool_calls {
    // Source: vvaharness/backends/harness/deepagents/invalid_tool_args.py:71-71
    In source order: Evaluate once invalid.get('id'); assign in source target order to call_id.
    // Source: vvaharness/backends/harness/deepagents/invalid_tool_args.py:72-74
    if (the source predicate call_id is None is truthy) {
      // Source: vvaharness/backends/harness/deepagents/invalid_tool_args.py:73-73
      In source order: Evaluate remaining_invalid.append(invalid); retain side effects and discard the expression result.
      // Source: vvaharness/backends/harness/deepagents/invalid_tool_args.py:74-74
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/backends/harness/deepagents/invalid_tool_args.py:75-78
    In source order: Evaluate new_tool_calls.append({'name': invalid.get('name') or '', 'args': {}, 'id': call_id, 'type': 'tool_call'}); retain side effects and discard the expression result. Then Evaluate repaired_ids.add(call_id); retain side effects and discard the expression result. Then Evaluate once _record_invalid_call(invalid, call_id, existing_tool_message_ids, counted_ids); assign in source target order to extra.
    // Source: vvaharness/backends/harness/deepagents/invalid_tool_args.py:79-80
    if (the source predicate extra is not None is truthy) {
      // Source: vvaharness/backends/harness/deepagents/invalid_tool_args.py:80-80
      In source order: Evaluate extra_tool_messages.append(extra); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/backends/harness/deepagents/invalid_tool_args.py:81-81
  In source order: Evaluate once message.content; assign in source target order to content.
  // Source: vvaharness/backends/harness/deepagents/invalid_tool_args.py:82-83
  if (the source predicate isinstance(content, list) is truthy) {
    // Source: vvaharness/backends/harness/deepagents/invalid_tool_args.py:83-83
    In source order: Evaluate once [_repair_block(block, frozenset(repaired_ids)) for block in content]; assign in source target order to content.
  }
  // Source: vvaharness/backends/harness/deepagents/invalid_tool_args.py:84-86
  In source order: Evaluate once message.model_copy(update={'tool_calls': new_tool_calls, 'invalid_tool_calls': remaining_invalid, 'content': content}); assign in source target order to repaired.
  // Source: vvaharness/backends/harness/deepagents/invalid_tool_args.py:87-87
  End this invocation with (repaired, extra_tool_messages).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/invalid_tool_args.py:90-106
// Source signature: _repair(messages: Sequence[AnyMessage], counted_ids: set[str]) -> list[AnyMessage] | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _repair(messages, counted_ids) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/invalid_tool_args.py:93-97
  In source order: Retain source documentation literal source_literal_93_4; it is not a model call. Then Evaluate once frozenset((m.tool_call_id for m in messages if isinstance(m, ToolMessage))); assign in source target order to existing_tool_message_ids. Then For out, assign []; source annotation list[AnyMessage]. Then Evaluate once False; assign in source target order to changed.
  // Source: vvaharness/backends/harness/deepagents/invalid_tool_args.py:98-105
  for each message in messages {
    // Source: vvaharness/backends/harness/deepagents/invalid_tool_args.py:99-105
    if (the source predicate isinstance(message, AIMessage) and message.invalid_tool_calls is truthy) {
      // Source: vvaharness/backends/harness/deepagents/invalid_tool_args.py:100-103
      In source order: Evaluate once _repair_message(message, existing_tool_message_ids, counted_ids); assign in source target order to (repaired, extra). Then Evaluate out.append(repaired); retain side effects and discard the expression result. Then Evaluate out.extend(extra); retain side effects and discard the expression result. Then Evaluate once True; assign in source target order to changed.
    }
    else {
      // Source: vvaharness/backends/harness/deepagents/invalid_tool_args.py:105-105
      In source order: Evaluate out.append(message); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/backends/harness/deepagents/invalid_tool_args.py:106-106
  End this invocation with out if changed else None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/invalid_tool_args.py:109-133
interface RepairInvalidToolArgs {
  Describe the source Python type, preserving its base/metaclass expression order: AgentMiddleware.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/harness/deepagents/invalid_tool_args.py:110-110
  In source order: Retain source documentation literal source_literal_110_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/invalid_tool_args.py:112-115
  // Source signature: __init__(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/invalid_tool_args.py:113-115
    In source order: Retain source documentation literal source_literal_113_8; it is not a model call. Then Evaluate super().__init__(); retain side effects and discard the expression result. Then For self._counted_ids, assign set(); source annotation set[str].
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/deepagents/invalid_tool_args.py:117-119
  // Source signature: _repaired_request(self, request: ModelRequest) -> ModelRequest
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _repaired_request(self, request) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/invalid_tool_args.py:118-118
    In source order: Evaluate once _repair(request.messages, self._counted_ids); assign in source target order to repaired.
    // Source: vvaharness/backends/harness/deepagents/invalid_tool_args.py:119-119
    End this invocation with request if repaired is None else request.override(messages=repaired).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/deepagents/invalid_tool_args.py:121-125
  // Source signature: wrap_model_call(self, request: ModelRequest, handler: Callable[[ModelRequest], ModelCallResult]) -> ModelCallResult
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn wrap_model_call(self, request, handler) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/invalid_tool_args.py:124-124
    In source order: Retain source documentation literal source_literal_124_8; it is not a model call.
    // Source: vvaharness/backends/harness/deepagents/invalid_tool_args.py:125-125
    End this invocation with handler(self._repaired_request(request)).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/deepagents/invalid_tool_args.py:127-133
  // Source signature: awrap_model_call(self, request: ModelRequest, handler: Callable[[ModelRequest], Awaitable[ModelCallResult]]) -> ModelCallResult
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn awrap_model_call(self, request, handler) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    This callable produces a coroutine or async generator; await/suspension positions remain in source expressions.
    // Source: vvaharness/backends/harness/deepagents/invalid_tool_args.py:132-132
    In source order: Retain source documentation literal source_literal_132_8; it is not a model call.
    // Source: vvaharness/backends/harness/deepagents/invalid_tool_args.py:133-133
    End this invocation with await handler(self._repaired_request(request)).
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vvaharness/backends/harness/deepagents/invalid_tool_args.py:136-136
In source order: Evaluate once ['RepairInvalidToolArgs']; assign in source target order to __all__.
```

## Local import links

- `from vvaharness.util.counters import COUNTERS` at source line 27: `source_detail/vvaharness/util/counters.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../../prompt_representation/vvaharness/backends/harness/deepagents/invalid_tool_args.py.sudo.md). Exact strings in the evidence asset support this conversion.
