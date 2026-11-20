# vvaharness/backends/harness/deepagents/model_call_budget.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/backends/harness/deepagents/model_call_budget.py.evidence.json`. SHA-256: `70d58b29724adc927b701c0b1153cbabc09b4be88960e51bf3d8866dd70f922e`.

```sudo
// Source: vvaharness/backends/harness/deepagents/model_call_budget.py:15-22
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import threading; preserve alias and import-time effects. Then Resolve source import from collections.abc import Awaitable, Callable; preserve alias and import-time effects. Then Resolve source import from langchain.agents.middleware.types import AgentMiddleware, ModelRequest, ModelResponse; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/deepagents/model_call_budget.py:23-26
In source order: Resolve source import from langchain_core.messages import HumanMessage; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.models import ModelCallBudgetExhaustedError; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.counters import COUNTERS; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/deepagents/model_call_budget.py:29-39
// Source signature: _final_turn_notice(limit: int) -> HumanMessage
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _final_turn_notice(limit) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/model_call_budget.py:30-30
  In source order: Retain source documentation literal source_literal_30_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/model_call_budget.py:31-39
  End this invocation with HumanMessage(content=source_template_32_8).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/model_call_budget.py:42-117
interface ModelCallBudget {
  Describe the source Python type, preserving its base/metaclass expression order: AgentMiddleware.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/harness/deepagents/model_call_budget.py:43-43
  In source order: Retain source documentation literal source_literal_43_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/model_call_budget.py:46-58
  // Source signature: __init__(self, *, limit: int, outcome_tools: frozenset[str], counter: str='model_call_budget_final_turn', raise_when_exhausted: bool=False, stage: str='') -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self, limit, outcome_tools, counter, raise_when_exhausted, stage) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/model_call_budget.py:49-53
    In source order: Retain source documentation literal source_literal_49_8; it is not a model call. Then Evaluate super().__init__(); retain side effects and discard the expression result. Then Evaluate once max(1, int(limit)); assign in source target order to self._limit. Then Evaluate once outcome_tools; assign in source target order to self._outcome. Then Evaluate once counter; assign in source target order to self._counter.
    // Source: vvaharness/backends/harness/deepagents/model_call_budget.py:54-58
    In source order: Evaluate once 0; assign in source target order to self._calls. Then Evaluate once threading.Lock(); assign in source target order to self._lock. Then Evaluate once raise_when_exhausted; assign in source target order to self._raise_when_exhausted. Then Evaluate once stage; assign in source target order to self._stage. Then Evaluate once False; assign in source target order to self._final_turn_issued.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/deepagents/model_call_budget.py:61-63
  // Source: vvaharness/backends/harness/deepagents/model_call_budget.py:60-60
  Before creating this callable, evaluate and retain decorators top-to-bottom: property.
  // Source: vvaharness/backends/harness/deepagents/model_call_budget.py:61-63
  // Source signature: name(self) -> str
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn name(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/model_call_budget.py:62-62
    In source order: Retain source documentation literal source_literal_62_8; it is not a model call.
    // Source: vvaharness/backends/harness/deepagents/model_call_budget.py:63-63
    End this invocation with source_template_63_15.
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vvaharness/backends/harness/deepagents/model_call_budget.py:65-69
  // Source signature: _claim(self) -> bool
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _claim(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/model_call_budget.py:66-66
    In source order: Retain source documentation literal source_literal_66_8; it is not a model call.
    // Source: vvaharness/backends/harness/deepagents/model_call_budget.py:67-69
    Enter source context managers left-to-right: self._lock {
      // Source: vvaharness/backends/harness/deepagents/model_call_budget.py:68-68
      In source order: Apply source augmented assignment self._calls += 1 with source evaluation/in-place semantics.
      // Source: vvaharness/backends/harness/deepagents/model_call_budget.py:69-69
      End this invocation with self._calls >= self._limit.
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/deepagents/model_call_budget.py:71-77
  // Source signature: grant_resume_turn(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn grant_resume_turn(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/model_call_budget.py:72-72
    In source order: Retain source documentation literal source_literal_72_8; it is not a model call.
    // Source: vvaharness/backends/harness/deepagents/model_call_budget.py:73-77
    Enter source context managers left-to-right: self._lock {
      // Source: vvaharness/backends/harness/deepagents/model_call_budget.py:74-75
      if (the source predicate not self._final_turn_issued is truthy) {
        // Source: vvaharness/backends/harness/deepagents/model_call_budget.py:75-75
        End this invocation with None.
      }
      // Source: vvaharness/backends/harness/deepagents/model_call_budget.py:76-77
      In source order: Evaluate once False; assign in source target order to self._final_turn_issued. Then Evaluate once self._limit - 1; assign in source target order to self._calls.
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/deepagents/model_call_budget.py:79-84
  // Source signature: _final(self, request: ModelRequest) -> ModelRequest
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _final(self, request) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/model_call_budget.py:80-82
    In source order: Retain source documentation literal source_literal_80_8; it is not a model call. Then Evaluate once [t for t in request.tools or [] if getattr(t, 'name', None) in self._outcome]; assign in source target order to kept. Then Evaluate COUNTERS.bump(self._counter); retain side effects and discard the expression result.
    // Source: vvaharness/backends/harness/deepagents/model_call_budget.py:83-84
    End this invocation with request.override(tools=kept, messages=[*request.messages, _final_turn_notice(self._limit)]).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/deepagents/model_call_budget.py:86-93
  // Source signature: _check_exhausted(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _check_exhausted(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/model_call_budget.py:87-87
    In source order: Retain source documentation literal source_literal_87_8; it is not a model call.
    // Source: vvaharness/backends/harness/deepagents/model_call_budget.py:89-93
    if (the source predicate self._raise_when_exhausted and self._final_turn_issued is truthy) {
      // Source: vvaharness/backends/harness/deepagents/model_call_budget.py:90-93
      Raise ModelCallBudgetExhaustedError('the forced final turn (every tool but the outcome withdrawn) still did not end the session on the outcome tool', stage=self._stage, limit=self._limit).
    }
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/deepagents/model_call_budget.py:95-105
  // Source signature: wrap_model_call(self, request: ModelRequest, handler: Callable[[ModelRequest], ModelResponse]) -> ModelResponse
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn wrap_model_call(self, request, handler) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/model_call_budget.py:100-101
    In source order: Retain source documentation literal source_literal_100_8; it is not a model call. Then Evaluate self._check_exhausted(); retain side effects and discard the expression result.
    // Source: vvaharness/backends/harness/deepagents/model_call_budget.py:102-104
    if (the source predicate self._claim() is truthy) {
      // Source: vvaharness/backends/harness/deepagents/model_call_budget.py:103-104
      In source order: Evaluate once True; assign in source target order to self._final_turn_issued. Then Evaluate once self._final(request); assign in source target order to request.
    }
    // Source: vvaharness/backends/harness/deepagents/model_call_budget.py:105-105
    End this invocation with handler(request).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/deepagents/model_call_budget.py:107-117
  // Source signature: awrap_model_call(self, request: ModelRequest, handler: Callable[[ModelRequest], Awaitable[ModelResponse]]) -> ModelResponse
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn awrap_model_call(self, request, handler) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    This callable produces a coroutine or async generator; await/suspension positions remain in source expressions.
    // Source: vvaharness/backends/harness/deepagents/model_call_budget.py:112-113
    In source order: Retain source documentation literal source_literal_112_8; it is not a model call. Then Evaluate self._check_exhausted(); retain side effects and discard the expression result.
    // Source: vvaharness/backends/harness/deepagents/model_call_budget.py:114-116
    if (the source predicate self._claim() is truthy) {
      // Source: vvaharness/backends/harness/deepagents/model_call_budget.py:115-116
      In source order: Evaluate once True; assign in source target order to self._final_turn_issued. Then Evaluate once self._final(request); assign in source target order to request.
    }
    // Source: vvaharness/backends/harness/deepagents/model_call_budget.py:117-117
    End this invocation with await handler(request).
    If execution reaches this end, finish with the source implicit None result.
  }
}
```

## Local import links

- `from vvaharness.backends.harness.models import ModelCallBudgetExhaustedError` at source line 25: `source_detail/vvaharness/backends/harness/models.py.sudo.md`.
- `from vvaharness.util.counters import COUNTERS` at source line 26: `source_detail/vvaharness/util/counters.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../../prompt_representation/vvaharness/backends/harness/deepagents/model_call_budget.py.sudo.md). Exact strings in the evidence asset support this conversion.
