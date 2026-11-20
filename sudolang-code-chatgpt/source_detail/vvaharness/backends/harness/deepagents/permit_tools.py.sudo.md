# vvaharness/backends/harness/deepagents/permit_tools.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/backends/harness/deepagents/permit_tools.py.evidence.json`. SHA-256: `9eafa28981bd4c88042ff52d443dedb027c98b76add1889e8b81492f5cb08c21`.

```sudo
// Source: vvaharness/backends/harness/deepagents/permit_tools.py:15-24
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from typing import TYPE_CHECKING, Any; preserve alias and import-time effects. Then Resolve source import from langchain.agents.middleware.types import AgentMiddleware; preserve alias and import-time effects. Then Resolve source import from langchain_core.messages import ToolMessage; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/deepagents/permit_tools.py:26-29
In source order: Resolve source import from vvaharness.util import logs; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.events import Event; preserve alias and import-time effects. Then Evaluate once logs.get_logger(__name__); assign in source target order to log.
// Source: vvaharness/backends/harness/deepagents/permit_tools.py:31-35
if (the source predicate TYPE_CHECKING is truthy) {
  // Source: vvaharness/backends/harness/deepagents/permit_tools.py:32-35
  In source order: Resolve source import from collections.abc import Awaitable, Callable; preserve alias and import-time effects. Then Resolve source import from langchain.agents.middleware.types import ToolCallRequest; preserve alias and import-time effects. Then Resolve source import from langgraph.types import Command; preserve alias and import-time effects.
}
// Source: vvaharness/backends/harness/deepagents/permit_tools.py:38-77
interface PermitTools {
  Describe the source Python type, preserving its base/metaclass expression order: AgentMiddleware.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/harness/deepagents/permit_tools.py:39-39
  In source order: Retain source documentation literal source_literal_39_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/permit_tools.py:41-44
  // Source signature: __init__(self, permitted: frozenset[str]) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self, permitted) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/permit_tools.py:42-44
    In source order: Retain source documentation literal source_literal_42_8; it is not a model call. Then Evaluate super().__init__(); retain side effects and discard the expression result. Then Evaluate once permitted; assign in source target order to self._permitted.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/deepagents/permit_tools.py:46-61
  // Source signature: _refusal(self, request: ToolCallRequest) -> ToolMessage | None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _refusal(self, request) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/permit_tools.py:47-49
    In source order: Retain source documentation literal source_literal_47_8; it is not a model call. Then Evaluate once request.tool_call; assign in source target order to tool_call. Then Evaluate once tool_call.get('name') or ''; assign in source target order to name.
    // Source: vvaharness/backends/harness/deepagents/permit_tools.py:50-51
    if (the source predicate name in self._permitted is truthy) {
      // Source: vvaharness/backends/harness/deepagents/permit_tools.py:51-51
      End this invocation with None.
    }
    // Source: vvaharness/backends/harness/deepagents/permit_tools.py:52-52
    In source order: Evaluate log.warning(Event.TOOL_CALL_REFUSED, tool=name); retain side effects and discard the expression result.
    // Source: vvaharness/backends/harness/deepagents/permit_tools.py:53-61
    End this invocation with ToolMessage(content=source_template_55_16, name=name, tool_call_id=tool_call.get('id') or '', status='error').
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/deepagents/permit_tools.py:63-69
  // Source signature: wrap_tool_call(self, request: ToolCallRequest, handler: Callable[[ToolCallRequest], ToolMessage | Command[Any]]) -> ToolMessage | Command[Any]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn wrap_tool_call(self, request, handler) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/permit_tools.py:68-68
    In source order: Retain source documentation literal source_literal_68_8; it is not a model call.
    // Source: vvaharness/backends/harness/deepagents/permit_tools.py:69-69
    End this invocation with self._refusal(request) or handler(request).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/deepagents/permit_tools.py:71-77
  // Source signature: awrap_tool_call(self, request: ToolCallRequest, handler: Callable[[ToolCallRequest], Awaitable[ToolMessage | Command[Any]]]) -> ToolMessage | Command[Any]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn awrap_tool_call(self, request, handler) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    This callable produces a coroutine or async generator; await/suspension positions remain in source expressions.
    // Source: vvaharness/backends/harness/deepagents/permit_tools.py:76-76
    In source order: Retain source documentation literal source_literal_76_8; it is not a model call.
    // Source: vvaharness/backends/harness/deepagents/permit_tools.py:77-77
    End this invocation with self._refusal(request) or await handler(request).
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vvaharness/backends/harness/deepagents/permit_tools.py:80-80
In source order: Evaluate once ['PermitTools']; assign in source target order to __all__.
```

## Local import links

- `from vvaharness.util import logs` at source line 26: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import logs` at source line 26: `source_detail/vvaharness/util/logs.py.sudo.md`.
- `from vvaharness.util.events import Event` at source line 27: `source_detail/vvaharness/util/events.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../../prompt_representation/vvaharness/backends/harness/deepagents/permit_tools.py.sudo.md). Exact strings in the evidence asset support this conversion.
