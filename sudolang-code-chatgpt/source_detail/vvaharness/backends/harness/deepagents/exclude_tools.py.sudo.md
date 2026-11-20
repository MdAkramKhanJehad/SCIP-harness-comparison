# vvaharness/backends/harness/deepagents/exclude_tools.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/backends/harness/deepagents/exclude_tools.py.evidence.json`. SHA-256: `2103704a86f7ff2d993158575192910f74164a3280135123b4b9ea8477ea20c4`.

```sudo
// Source: vvaharness/backends/harness/deepagents/exclude_tools.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from typing import TYPE_CHECKING, Any; preserve alias and import-time effects. Then Resolve source import from langchain.agents.middleware.types import AgentMiddleware; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/deepagents/exclude_tools.py:23-27
if (the source predicate TYPE_CHECKING is truthy) {
  // Source: vvaharness/backends/harness/deepagents/exclude_tools.py:24-27
  In source order: Resolve source import from collections.abc import Awaitable, Callable; preserve alias and import-time effects. Then Resolve source import from langchain.agents.middleware.types import ModelCallResult, ModelRequest; preserve alias and import-time effects. Then Resolve source import from langchain_core.tools import BaseTool; preserve alias and import-time effects.
}
// Source: vvaharness/backends/harness/deepagents/exclude_tools.py:30-33
// Source signature: _tool_name(tool: BaseTool | dict[str, Any]) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _tool_name(tool) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/exclude_tools.py:31-32
  In source order: Retain source documentation literal source_literal_31_4; it is not a model call. Then Evaluate once tool.get('name') if isinstance(tool, dict) else getattr(tool, 'name', None); assign in source target order to name.
  // Source: vvaharness/backends/harness/deepagents/exclude_tools.py:33-33
  End this invocation with name if isinstance(name, str) else None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/exclude_tools.py:36-60
interface ExcludeTools {
  Describe the source Python type, preserving its base/metaclass expression order: AgentMiddleware.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/harness/deepagents/exclude_tools.py:37-37
  In source order: Retain source documentation literal source_literal_37_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/exclude_tools.py:39-42
  // Source signature: __init__(self, excluded: frozenset[str]) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self, excluded) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/exclude_tools.py:40-42
    In source order: Retain source documentation literal source_literal_40_8; it is not a model call. Then Evaluate super().__init__(); retain side effects and discard the expression result. Then Evaluate once excluded; assign in source target order to self._excluded.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/deepagents/exclude_tools.py:44-46
  // Source signature: _filter(self, request: ModelRequest) -> ModelRequest
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _filter(self, request) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/exclude_tools.py:45-45
    In source order: Evaluate once [tool for tool in request.tools if _tool_name(tool) not in self._excluded]; assign in source target order to kept.
    // Source: vvaharness/backends/harness/deepagents/exclude_tools.py:46-46
    End this invocation with request.override(tools=kept) if len(kept) != len(request.tools) else request.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/deepagents/exclude_tools.py:48-52
  // Source signature: wrap_model_call(self, request: ModelRequest, handler: Callable[[ModelRequest], ModelCallResult]) -> ModelCallResult
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn wrap_model_call(self, request, handler) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/exclude_tools.py:51-51
    In source order: Retain source documentation literal source_literal_51_8; it is not a model call.
    // Source: vvaharness/backends/harness/deepagents/exclude_tools.py:52-52
    End this invocation with handler(self._filter(request)).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/deepagents/exclude_tools.py:54-60
  // Source signature: awrap_model_call(self, request: ModelRequest, handler: Callable[[ModelRequest], Awaitable[ModelCallResult]]) -> ModelCallResult
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn awrap_model_call(self, request, handler) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    This callable produces a coroutine or async generator; await/suspension positions remain in source expressions.
    // Source: vvaharness/backends/harness/deepagents/exclude_tools.py:59-59
    In source order: Retain source documentation literal source_literal_59_8; it is not a model call.
    // Source: vvaharness/backends/harness/deepagents/exclude_tools.py:60-60
    End this invocation with await handler(self._filter(request)).
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vvaharness/backends/harness/deepagents/exclude_tools.py:63-63
In source order: Evaluate once ['ExcludeTools']; assign in source target order to __all__.
```

## Local import links

No statically resolved in-checkout import; external calls remain explicit dependency boundaries.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../../prompt_representation/vvaharness/backends/harness/deepagents/exclude_tools.py.sudo.md). Exact strings in the evidence asset support this conversion.
