# vvaharness/backends/harness/deepagents/tool_budget.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/backends/harness/deepagents/tool_budget.py.evidence.json`. SHA-256: `7c07cf7099b04582e07c3414f60a24451ccf9e694e6fe9ffe989a44584383b16`.

```sudo
// Source: vvaharness/backends/harness/deepagents/tool_budget.py:15-23
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import threading; preserve alias and import-time effects. Then Resolve source import from collections.abc import Awaitable, Callable; preserve alias and import-time effects. Then Resolve source import from typing import Any; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/deepagents/tool_budget.py:25-35
In source order: Resolve source import from langchain.agents.middleware.types import AgentMiddleware, ModelRequest, ModelResponse, ToolCallRequest; preserve alias and import-time effects. Then Resolve source import from langchain_core.messages import HumanMessage, ToolCall, ToolMessage; preserve alias and import-time effects. Then Resolve source import from langgraph.types import Command; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.counters import COUNTERS; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.warn_once import stage_label, warn_once; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/deepagents/tool_budget.py:37-54
In source order: Evaluate once source_literal_38_4; assign in source target order to _BUDGET_MESSAGE. Then Evaluate once 'tool_call_budget_exhausted'; assign in source target order to _DEFAULT_COUNTER. Then For _KNOB_NAMES, assign {'s2_graph_tool_budget_exhausted': 'step2.graph_tool_budget', 's4_graph_tool_budget_exhausted': 'step4.graph_tool_budget', 's4_cwe_tool_budget_exhausted': 'step4.cwe_tool_budget', 's6_graph_tool_budget_exhausted': 'step6_verify.graph_tool_budget'}; source annotation dict[str, str]. Then For _WARNED_EXHAUSTED, assign set(); source annotation set[str].
// Source: vvaharness/backends/harness/deepagents/tool_budget.py:57-61
// Source signature: _calls_counter_name(counter: str, tool: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _calls_counter_name(counter, tool) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/tool_budget.py:58-58
  In source order: Retain source documentation literal source_literal_58_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/tool_budget.py:59-60
  if (the source predicate counter == _DEFAULT_COUNTER is truthy) {
    // Source: vvaharness/backends/harness/deepagents/tool_budget.py:60-60
    End this invocation with source_template_60_15.
  }
  // Source: vvaharness/backends/harness/deepagents/tool_budget.py:61-61
  End this invocation with source_template_61_11.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/tool_budget.py:64-74
// Source signature: _exhaustion_warning(counter: str, limit: int, tool_names: frozenset[str]) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _exhaustion_warning(counter, limit, tool_names) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/tool_budget.py:65-67
  In source order: Retain source documentation literal source_literal_65_4; it is not a model call. Then Evaluate once _KNOB_NAMES.get(counter, 'its scan-config budget knob'); assign in source target order to knob. Then Evaluate once ', '.join(sorted(tool_names)); assign in source target order to names.
  // Source: vvaharness/backends/harness/deepagents/tool_budget.py:68-74
  End this invocation with source_template_69_8.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/tool_budget.py:77-80
// Source signature: _refuse(tool_call: ToolCall, content: str) -> ToolMessage
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _refuse(tool_call, content) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/tool_budget.py:78-78
  In source order: Retain source documentation literal source_literal_78_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/tool_budget.py:79-80
  End this invocation with ToolMessage(content=content, name=tool_call['name'], tool_call_id=tool_call['id'], status='error').
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/tool_budget.py:83-89
// Source signature: _withdrawn_notice(tool_names: frozenset[str]) -> HumanMessage
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _withdrawn_notice(tool_names) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/tool_budget.py:84-84
  In source order: Retain source documentation literal source_literal_84_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/tool_budget.py:85-89
  End this invocation with HumanMessage(content=source_template_86_8).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/tool_budget.py:92-189
interface ToolCallBudget {
  Describe the source Python type, preserving its base/metaclass expression order: AgentMiddleware.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/harness/deepagents/tool_budget.py:93-93
  In source order: Retain source documentation literal source_literal_93_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/tool_budget.py:96-105
  // Source signature: __init__(self, tool_names: frozenset[str], *, limit: int, counter: str='tool_call_budget_exhausted') -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self, tool_names, limit, counter) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/tool_budget.py:98-102
    In source order: Retain source documentation literal source_literal_98_8; it is not a model call. Then Evaluate super().__init__(); retain side effects and discard the expression result. Then Evaluate once tool_names; assign in source target order to self._tool_names. Then Evaluate once limit; assign in source target order to self._limit. Then Evaluate once counter; assign in source target order to self._counter.
    // Source: vvaharness/backends/harness/deepagents/tool_budget.py:103-105
    In source order: Evaluate once 0; assign in source target order to self._spent. Then Evaluate once threading.Lock(); assign in source target order to self._lock. Then Evaluate once False; assign in source target order to self._withdrawal_announced.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/deepagents/tool_budget.py:108-111
  // Source: vvaharness/backends/harness/deepagents/tool_budget.py:107-107
  Before creating this callable, evaluate and retain decorators top-to-bottom: property.
  // Source: vvaharness/backends/harness/deepagents/tool_budget.py:108-111
  // Source signature: name(self) -> str
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn name(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/tool_budget.py:109-109
    In source order: Retain source documentation literal source_literal_109_8; it is not a model call.
    // Source: vvaharness/backends/harness/deepagents/tool_budget.py:111-111
    End this invocation with source_template_111_15.
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vvaharness/backends/harness/deepagents/tool_budget.py:113-119
  // Source signature: _claim(self) -> bool
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _claim(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/tool_budget.py:114-114
    In source order: Retain source documentation literal source_literal_114_8; it is not a model call.
    // Source: vvaharness/backends/harness/deepagents/tool_budget.py:115-119
    Enter source context managers left-to-right: self._lock {
      // Source: vvaharness/backends/harness/deepagents/tool_budget.py:116-117
      if (the source predicate self._spent >= self._limit is truthy) {
        // Source: vvaharness/backends/harness/deepagents/tool_budget.py:117-117
        End this invocation with False.
      }
      // Source: vvaharness/backends/harness/deepagents/tool_budget.py:118-118
      In source order: Apply source augmented assignment self._spent += 1 with source evaluation/in-place semantics.
      // Source: vvaharness/backends/harness/deepagents/tool_budget.py:119-119
      End this invocation with True.
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/deepagents/tool_budget.py:121-131
  // Source signature: _gate(self, tool_call: ToolCall) -> ToolMessage | None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _gate(self, tool_call) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/tool_budget.py:122-122
    In source order: Retain source documentation literal source_literal_122_8; it is not a model call.
    // Source: vvaharness/backends/harness/deepagents/tool_budget.py:123-124
    if (the source predicate tool_call['name'] not in self._tool_names is truthy) {
      // Source: vvaharness/backends/harness/deepagents/tool_budget.py:124-124
      End this invocation with None.
    }
    // Source: vvaharness/backends/harness/deepagents/tool_budget.py:125-127
    if (the source predicate self._claim() is truthy) {
      // Source: vvaharness/backends/harness/deepagents/tool_budget.py:126-126
      In source order: Evaluate COUNTERS.bump(_calls_counter_name(self._counter, tool_call['name'])); retain side effects and discard the expression result.
      // Source: vvaharness/backends/harness/deepagents/tool_budget.py:127-127
      End this invocation with None.
    }
    // Source: vvaharness/backends/harness/deepagents/tool_budget.py:128-130
    In source order: Evaluate COUNTERS.bump(self._counter); retain side effects and discard the expression result. Then Evaluate warn_once(_WARNED_EXHAUSTED, self._counter, _exhaustion_warning(self._counter, self._limit, self._tool_names)); retain side effects and discard the expression result.
    // Source: vvaharness/backends/harness/deepagents/tool_budget.py:131-131
    End this invocation with _refuse(tool_call, _BUDGET_MESSAGE).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/deepagents/tool_budget.py:133-136
  // Source signature: exhausted_tools(self) -> frozenset[str]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn exhausted_tools(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/tool_budget.py:134-134
    In source order: Retain source documentation literal source_literal_134_8; it is not a model call.
    // Source: vvaharness/backends/harness/deepagents/tool_budget.py:135-136
    Enter source context managers left-to-right: self._lock {
      // Source: vvaharness/backends/harness/deepagents/tool_budget.py:136-136
      End this invocation with self._tool_names if self._spent >= self._limit else frozenset().
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/deepagents/tool_budget.py:138-142
  // Source signature: refusal_for(self, tool_name: str) -> str | None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn refusal_for(self, tool_name) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/tool_budget.py:139-141
    In source order: Retain source documentation literal source_literal_139_8; it is not a model call. Then Evaluate once self._gate({'name': tool_name, 'id': 'out-of-loop', 'args': {}}); assign in source target order to refusal.
    // Source: vvaharness/backends/harness/deepagents/tool_budget.py:142-142
    End this invocation with None if refusal is None else str(refusal.content).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/deepagents/tool_budget.py:144-150
  // Source signature: wrap_tool_call(self, request: ToolCallRequest, handler: Callable[[ToolCallRequest], ToolMessage | Command[Any]]) -> ToolMessage | Command[Any]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn wrap_tool_call(self, request, handler) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/tool_budget.py:149-149
    In source order: Retain source documentation literal source_literal_149_8; it is not a model call.
    // Source: vvaharness/backends/harness/deepagents/tool_budget.py:150-150
    End this invocation with self._gate(request.tool_call) or handler(request).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/deepagents/tool_budget.py:152-159
  // Source signature: awrap_tool_call(self, request: ToolCallRequest, handler: Callable[[ToolCallRequest], Awaitable[ToolMessage | Command[Any]]]) -> ToolMessage | Command[Any]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn awrap_tool_call(self, request, handler) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    This callable produces a coroutine or async generator; await/suspension positions remain in source expressions.
    // Source: vvaharness/backends/harness/deepagents/tool_budget.py:157-158
    In source order: Retain source documentation literal source_literal_157_8; it is not a model call. Then Evaluate once self._gate(request.tool_call); assign in source target order to refusal.
    // Source: vvaharness/backends/harness/deepagents/tool_budget.py:159-159
    End this invocation with refusal if refusal is not None else await handler(request).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/deepagents/tool_budget.py:161-169
  // Source signature: _withdraw(self, request: ModelRequest) -> ModelRequest
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _withdraw(self, request) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/tool_budget.py:162-165
    In source order: Retain source documentation literal source_literal_162_8; it is not a model call. Then Evaluate once [t for t in request.tools or [] if getattr(t, 'name', None) not in self._tool_names]; assign in source target order to kept. Then Evaluate once request.messages; assign in source target order to messages.
    // Source: vvaharness/backends/harness/deepagents/tool_budget.py:166-168
    if (the source predicate not self._withdrawal_announced is truthy) {
      // Source: vvaharness/backends/harness/deepagents/tool_budget.py:167-168
      In source order: Evaluate once True; assign in source target order to self._withdrawal_announced. Then Evaluate once [*messages, _withdrawn_notice(self._tool_names)]; assign in source target order to messages.
    }
    // Source: vvaharness/backends/harness/deepagents/tool_budget.py:169-169
    End this invocation with request.override(tools=kept, messages=messages).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/deepagents/tool_budget.py:171-179
  // Source signature: wrap_model_call(self, request: ModelRequest, handler: Callable[[ModelRequest], ModelResponse]) -> ModelResponse
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn wrap_model_call(self, request, handler) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/tool_budget.py:176-176
    In source order: Retain source documentation literal source_literal_176_8; it is not a model call.
    // Source: vvaharness/backends/harness/deepagents/tool_budget.py:177-178
    if (the source predicate self.exhausted_tools() is truthy) {
      // Source: vvaharness/backends/harness/deepagents/tool_budget.py:178-178
      In source order: Evaluate once self._withdraw(request); assign in source target order to request.
    }
    // Source: vvaharness/backends/harness/deepagents/tool_budget.py:179-179
    End this invocation with handler(request).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/deepagents/tool_budget.py:181-189
  // Source signature: awrap_model_call(self, request: ModelRequest, handler: Callable[[ModelRequest], Awaitable[ModelResponse]]) -> ModelResponse
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn awrap_model_call(self, request, handler) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    This callable produces a coroutine or async generator; await/suspension positions remain in source expressions.
    // Source: vvaharness/backends/harness/deepagents/tool_budget.py:186-186
    In source order: Retain source documentation literal source_literal_186_8; it is not a model call.
    // Source: vvaharness/backends/harness/deepagents/tool_budget.py:187-188
    if (the source predicate self.exhausted_tools() is truthy) {
      // Source: vvaharness/backends/harness/deepagents/tool_budget.py:188-188
      In source order: Evaluate once self._withdraw(request); assign in source target order to request.
    }
    // Source: vvaharness/backends/harness/deepagents/tool_budget.py:189-189
    End this invocation with await handler(request).
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vvaharness/backends/harness/deepagents/tool_budget.py:192-192
In source order: Evaluate once ['ToolCallBudget']; assign in source target order to __all__.
```

## Local import links

- `from vvaharness.util.counters import COUNTERS` at source line 34: `source_detail/vvaharness/util/counters.py.sudo.md`.
- `from vvaharness.util.warn_once import stage_label, warn_once` at source line 35: `source_detail/vvaharness/util/warn_once.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../../prompt_representation/vvaharness/backends/harness/deepagents/tool_budget.py.sudo.md). Exact strings in the evidence asset support this conversion.
