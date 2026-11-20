# vvaharness/backends/harness/deepagents/force_verdict_only.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/backends/harness/deepagents/force_verdict_only.py.evidence.json`. SHA-256: `a9a6c219f76c34ae2e8a986c5113c5e85261ca7617e473213e3f6bad50275628`.

```sudo
// Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import threading; preserve alias and import-time effects. Then Resolve source import from collections.abc import Awaitable, Callable; preserve alias and import-time effects. Then Resolve source import from typing import TYPE_CHECKING, cast; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:23-38
In source order: Resolve source import from langchain.agents.middleware.types import AgentMiddleware, ExtendedModelResponse, ModelCallResult, ModelRequest, ModelResponse; preserve alias and import-time effects. Then Resolve source import from langchain.agents.structured_output import ToolStrategy; preserve alias and import-time effects. Then Resolve source import from langchain_core.messages import AIMessage, HumanMessage; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.deepagents.tool_choice_rejection import UNSUPPORTED_MODELS, is_tool_choice_unsupported_rejection, learn_tool_choice_unsupported; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.counters import COUNTERS; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:40-42
if (the source predicate TYPE_CHECKING is truthy) {
  // Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:42-42
  In source order: Resolve source import from vvaharness.backends.harness.deepagents.options.forcing import ForcingChatAnthropic; preserve alias and import-time effects.
}
// Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:45-45
In source order: Evaluate once 'deepagents_verdict_forced_after_auto'; assign in source target order to FORCED_VERDICT_COUNTER.
// Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:48-54
// Source signature: _report_now(tool_names: list[str]) -> HumanMessage
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _report_now(tool_names) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:49-50
  In source order: Retain source documentation literal source_literal_49_4; it is not a model call. Then Evaluate once ' or '.join((source_template_50_24 for n in tool_names)) or 'the outcome tool'; assign in source target order to names.
  // Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:51-54
  End this invocation with HumanMessage(content=source_template_52_8).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:57-59
// Source signature: _forcing(request: ModelRequest) -> ForcingChatAnthropic
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _forcing(request) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:58-58
  In source order: Retain source documentation literal source_literal_58_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:59-59
  End this invocation with cast('ForcingChatAnthropic', request.model).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:62-68
// Source signature: _reply(result: ModelCallResult) -> AIMessage | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _reply(result) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:63-63
  In source order: Retain source documentation literal source_literal_63_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:64-65
  if (the source predicate isinstance(result, ExtendedModelResponse) is truthy) {
    // Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:65-65
    In source order: Evaluate once result.model_response; assign in source target order to result.
  }
  // Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:66-67
  In source order: Evaluate once result.result if isinstance(result, ModelResponse) else [result]; assign in source target order to messages. Then Evaluate once messages[-1] if messages else None; assign in source target order to last.
  // Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:68-68
  End this invocation with last if isinstance(last, AIMessage) else None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:71-180
interface ForceVerdictOnly {
  Describe the source Python type, preserving its base/metaclass expression order: AgentMiddleware.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:72-77
  In source order: Retain source documentation literal source_literal_72_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:80-84
  // Source signature: __init__(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:81-84
    In source order: Retain source documentation literal source_literal_81_8; it is not a model call. Then Evaluate super().__init__(); retain side effects and discard the expression result. Then For self._auto, assign {}; source annotation dict[int, ForcingChatAnthropic]. Then Evaluate once threading.Lock(); assign in source target order to self._lock.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:86-92
  // Source signature: _auto_model(self, model: ForcingChatAnthropic) -> ForcingChatAnthropic
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _auto_model(self, model) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:87-87
    In source order: Retain source documentation literal source_literal_87_8; it is not a model call.
    // Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:88-92
    Enter source context managers left-to-right: self._lock {
      // Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:89-89
      In source order: Evaluate once self._auto.get(id(model)); assign in source target order to copy.
      // Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:90-91
      if (the source predicate copy is None is truthy) {
        // Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:91-91
        In source order: Evaluate once model.model_copy(update={'force_tool_choice': False}); assign in source target order to copy, self._auto[id(model)].
      }
      // Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:92-92
      End this invocation with copy.
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:95-99
  // Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:94-94
  Before creating this callable, evaluate and retain decorators top-to-bottom: staticmethod.
  // Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:95-99
  // Source signature: _applies(request: ModelRequest) -> bool
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _applies(request) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:96-96
    In source order: Retain source documentation literal source_literal_96_8; it is not a model call.
    // Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:98-99
    End this invocation with isinstance(request.response_format, ToolStrategy) and getattr(request.model, 'force_tool_choice', None) is True.
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:101-103
  // Source signature: _unforced(self, request: ModelRequest) -> ModelRequest
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _unforced(self, request) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:102-102
    In source order: Retain source documentation literal source_literal_102_8; it is not a model call.
    // Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:103-103
    End this invocation with request.override(model=self._auto_model(_forcing(request))).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:105-110
  // Source signature: _learn_rejection(self, request: ModelRequest, exc: Exception) -> bool
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _learn_rejection(self, request, exc) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:106-106
    In source order: Retain source documentation literal source_literal_106_8; it is not a model call.
    // Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:107-108
    if (the source predicate not is_tool_choice_unsupported_rejection(exc) is truthy) {
      // Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:108-108
      End this invocation with False.
    }
    // Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:109-109
    In source order: Evaluate learn_tool_choice_unsupported(_forcing(request).model); retain side effects and discard the expression result.
    // Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:110-110
    End this invocation with True.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:113-120
  // Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:112-112
  Before creating this callable, evaluate and retain decorators top-to-bottom: staticmethod.
  // Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:113-120
  // Source signature: _forced(request: ModelRequest, reply: AIMessage) -> ModelRequest
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _forced(request, reply) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:114-118
    In source order: Retain source documentation literal source_literal_114_8; it is not a model call. Then Evaluate once request.response_format; assign in source target order to strategy. Then Evaluate once [spec.name for spec in strategy.schema_specs] if isinstance(strategy, ToolStrategy) else []; assign in source target order to names. Then Evaluate COUNTERS.bump(FORCED_VERDICT_COUNTER); retain side effects and discard the expression result.
    // Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:119-120
    End this invocation with request.override(tools=[], messages=[*request.messages, reply, _report_now(names)]).
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:122-133
  // Source signature: _force(self, request: ModelRequest, handler: Callable[[ModelRequest], ModelCallResult]) -> ModelCallResult
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _force(self, request, handler) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:125-125
    In source order: Retain source documentation literal source_literal_125_8; it is not a model call.
    // Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:126-127
    if (the source predicate _forcing(request).model in UNSUPPORTED_MODELS is truthy) {
      // Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:127-127
      End this invocation with handler(self._unforced(request)).
    }
    // Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:128-132
    Perform the following protected operations {
      // Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:129-129
      End this invocation with handler(request).
    }
    // Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:130-132
    On the first matching source exception Exception as exc, in handler order {
      // Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:131-132
      if (the source predicate not self._learn_rejection(request, exc) is truthy) {
        // Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:132-132
        Raise the currently handled exception.
      }
    }
    // Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:133-133
    End this invocation with handler(self._unforced(request)).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:135-147
  // Source signature: _aforce(self, request: ModelRequest, handler: Callable[[ModelRequest], Awaitable[ModelCallResult]]) -> ModelCallResult
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _aforce(self, request, handler) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    This callable produces a coroutine or async generator; await/suspension positions remain in source expressions.
    // Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:139-139
    In source order: Retain source documentation literal source_literal_139_8; it is not a model call.
    // Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:140-141
    if (the source predicate _forcing(request).model in UNSUPPORTED_MODELS is truthy) {
      // Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:141-141
      End this invocation with await handler(self._unforced(request)).
    }
    // Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:142-146
    Perform the following protected operations {
      // Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:143-143
      End this invocation with await handler(request).
    }
    // Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:144-146
    On the first matching source exception Exception as exc, in handler order {
      // Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:145-146
      if (the source predicate not self._learn_rejection(request, exc) is truthy) {
        // Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:146-146
        Raise the currently handled exception.
      }
    }
    // Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:147-147
    End this invocation with await handler(self._unforced(request)).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:149-164
  // Source signature: wrap_model_call(self, request: ModelRequest, handler: Callable[[ModelRequest], ModelCallResult]) -> ModelCallResult
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn wrap_model_call(self, request, handler) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:154-154
    In source order: Retain source documentation literal source_literal_154_8; it is not a model call.
    // Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:155-156
    if (the source predicate not self._applies(request) is truthy) {
      // Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:156-156
      End this invocation with handler(request).
    }
    // Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:158-163
    if (the source predicate request.tools is truthy) {
      // Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:159-160
      In source order: Evaluate once handler(self._unforced(request)); assign in source target order to result. Then Evaluate once _reply(result); assign in source target order to reply.
      // Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:161-162
      if (the source predicate reply is None or reply.tool_calls is truthy) {
        // Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:162-162
        End this invocation with result.
      }
      // Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:163-163
      In source order: Evaluate once self._forced(request, reply); assign in source target order to request.
    }
    // Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:164-164
    End this invocation with self._force(request, handler).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:166-180
  // Source signature: awrap_model_call(self, request: ModelRequest, handler: Callable[[ModelRequest], Awaitable[ModelCallResult]]) -> ModelCallResult
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn awrap_model_call(self, request, handler) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    This callable produces a coroutine or async generator; await/suspension positions remain in source expressions.
    // Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:171-171
    In source order: Retain source documentation literal source_literal_171_8; it is not a model call.
    // Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:172-173
    if (the source predicate not self._applies(request) is truthy) {
      // Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:173-173
      End this invocation with await handler(request).
    }
    // Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:174-179
    if (the source predicate request.tools is truthy) {
      // Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:175-176
      In source order: Evaluate once await handler(self._unforced(request)); assign in source target order to result. Then Evaluate once _reply(result); assign in source target order to reply.
      // Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:177-178
      if (the source predicate reply is None or reply.tool_calls is truthy) {
        // Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:178-178
        End this invocation with result.
      }
      // Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:179-179
      In source order: Evaluate once self._forced(request, reply); assign in source target order to request.
    }
    // Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:180-180
    End this invocation with await self._aforce(request, handler).
    If execution reaches this end, finish with the source implicit None result.
  }
}
```

## Local import links

- `from vvaharness.backends.harness.deepagents.tool_choice_rejection import UNSUPPORTED_MODELS, is_tool_choice_unsupported_rejection, learn_tool_choice_unsupported` at source line 33: `source_detail/vvaharness/backends/harness/deepagents/tool_choice_rejection.py.sudo.md`.
- `from vvaharness.util.counters import COUNTERS` at source line 38: `source_detail/vvaharness/util/counters.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.options.forcing import ForcingChatAnthropic` at source line 42: `source_detail/vvaharness/backends/harness/deepagents/options/forcing.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../../prompt_representation/vvaharness/backends/harness/deepagents/force_verdict_only.py.sudo.md). Exact strings in the evidence asset support this conversion.
