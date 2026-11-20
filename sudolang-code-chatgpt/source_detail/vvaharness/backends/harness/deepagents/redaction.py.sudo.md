# vvaharness/backends/harness/deepagents/redaction.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/backends/harness/deepagents/redaction.py.evidence.json`. SHA-256: `c99c885bd299c597c7d8a9ece0cc1b6397471d1a8734a98b6c6559edb3b549bf`.

```sudo
// Source: vvaharness/backends/harness/deepagents/redaction.py:15-25
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from typing import TYPE_CHECKING, Any; preserve alias and import-time effects. Then Resolve source import from langchain.agents.middleware.types import AgentMiddleware; preserve alias and import-time effects. Then Resolve source import from langchain_core.messages import ToolMessage; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/deepagents/redaction.py:27-31
In source order: Resolve source import from vvaharness.backends.harness.deepagents.exclude_tools import ExcludeTools; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.deepagents.models import DELETE_TOOL_NAME; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.models import NATIVE_CONTENT_TOOLS, NATIVE_WRITE_TOOLS; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm.tools import sanitize_packed_text; preserve alias and import-time effects. Then Resolve source import from vvaharness.report.redact import redact_counts; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/deepagents/redaction.py:33-37
if (the source predicate TYPE_CHECKING is truthy) {
  // Source: vvaharness/backends/harness/deepagents/redaction.py:34-37
  In source order: Resolve source import from collections.abc import Awaitable, Callable; preserve alias and import-time effects. Then Resolve source import from langchain.agents.middleware.types import ToolCallRequest; preserve alias and import-time effects. Then Resolve source import from langgraph.types import Command; preserve alias and import-time effects.
}
// Source: vvaharness/backends/harness/deepagents/redaction.py:40-49
// Source signature: _redact_block(block: Any, rel: str) -> Any
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _redact_block(block, rel) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/redaction.py:41-42
  In source order: Retain source documentation literal source_literal_41_4; it is not a model call. Then Evaluate once isinstance(block, dict) and block.get('type') == 'text'; assign in source target order to is_text_dict.
  // Source: vvaharness/backends/harness/deepagents/redaction.py:43-46
  if (the source predicate isinstance(block, str) or is_text_dict is truthy) {
    // Source: vvaharness/backends/harness/deepagents/redaction.py:44-45
    In source order: Evaluate once block if isinstance(block, str) else block.get('text', ''); assign in source target order to text. Then Evaluate once redact_counts(sanitize_packed_text(text, rel))[0]; assign in source target order to masked.
    // Source: vvaharness/backends/harness/deepagents/redaction.py:46-46
    End this invocation with masked if isinstance(block, str) else {**block, 'text': masked}.
  }
  // Source: vvaharness/backends/harness/deepagents/redaction.py:47-48
  if (the source predicate not isinstance(block, dict) is truthy) {
    // Source: vvaharness/backends/harness/deepagents/redaction.py:48-48
    End this invocation with block.
  }
  // Source: vvaharness/backends/harness/deepagents/redaction.py:49-49
  End this invocation with {'type': 'text', 'text': source_template_49_36}.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/redaction.py:52-62
// Source signature: _redact_message(message: ToolMessage | Command[Any]) -> ToolMessage | Command[Any]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _redact_message(message) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/redaction.py:53-53
  In source order: Retain source documentation literal source_literal_53_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/redaction.py:54-55
  if (the source predicate not isinstance(message, ToolMessage) is truthy) {
    // Source: vvaharness/backends/harness/deepagents/redaction.py:55-55
    End this invocation with message.
  }
  // Source: vvaharness/backends/harness/deepagents/redaction.py:56-57
  In source order: Evaluate once message.additional_kwargs.get('read_file_path', ''); assign in source target order to rel. Then Evaluate once message.content; assign in source target order to content.
  // Source: vvaharness/backends/harness/deepagents/redaction.py:58-61
  if (the source predicate isinstance(content, str) and content is truthy) {
    // Source: vvaharness/backends/harness/deepagents/redaction.py:59-59
    In source order: Evaluate once redact_counts(sanitize_packed_text(content, rel))[0]; assign in source target order to message.content.
  }
  else {
    // Source: vvaharness/backends/harness/deepagents/redaction.py:60-61
    if (the source predicate isinstance(content, list) is truthy) {
      // Source: vvaharness/backends/harness/deepagents/redaction.py:61-61
      In source order: Evaluate once [_redact_block(block, rel) for block in content]; assign in source target order to message.content.
    }
  }
  // Source: vvaharness/backends/harness/deepagents/redaction.py:62-62
  End this invocation with message.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/redaction.py:65-71
// Source signature: _redact_if_content_tool(request: ToolCallRequest, result: ToolMessage | Command[Any]) -> ToolMessage | Command[Any]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _redact_if_content_tool(request, result) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/redaction.py:68-68
  In source order: Retain source documentation literal source_literal_68_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/redaction.py:69-70
  if (the source predicate request.tool_call.get('name') in NATIVE_CONTENT_TOOLS is truthy) {
    // Source: vvaharness/backends/harness/deepagents/redaction.py:70-70
    End this invocation with _redact_message(result).
  }
  // Source: vvaharness/backends/harness/deepagents/redaction.py:71-71
  End this invocation with result.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/redaction.py:74-91
interface RedactToolResults {
  Describe the source Python type, preserving its base/metaclass expression order: AgentMiddleware.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/harness/deepagents/redaction.py:75-75
  In source order: Retain source documentation literal source_literal_75_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/redaction.py:77-83
  // Source signature: wrap_tool_call(self, request: ToolCallRequest, handler: Callable[[ToolCallRequest], ToolMessage | Command[Any]]) -> ToolMessage | Command[Any]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn wrap_tool_call(self, request, handler) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/redaction.py:82-82
    In source order: Retain source documentation literal source_literal_82_8; it is not a model call.
    // Source: vvaharness/backends/harness/deepagents/redaction.py:83-83
    End this invocation with _redact_if_content_tool(request, handler(request)).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/deepagents/redaction.py:85-91
  // Source signature: awrap_tool_call(self, request: ToolCallRequest, handler: Callable[[ToolCallRequest], Awaitable[ToolMessage | Command[Any]]]) -> ToolMessage | Command[Any]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn awrap_tool_call(self, request, handler) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    This callable produces a coroutine or async generator; await/suspension positions remain in source expressions.
    // Source: vvaharness/backends/harness/deepagents/redaction.py:90-90
    In source order: Retain source documentation literal source_literal_90_8; it is not a model call.
    // Source: vvaharness/backends/harness/deepagents/redaction.py:91-91
    End this invocation with _redact_if_content_tool(request, await handler(request)).
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vvaharness/backends/harness/deepagents/redaction.py:94-100
// Source signature: read_only_middleware(extra_excluded: frozenset[str]=frozenset()) -> list[AgentMiddleware]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn read_only_middleware(extra_excluded) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/redaction.py:97-99
  In source order: Retain source documentation literal source_literal_97_4; it is not a model call. Then Evaluate once NATIVE_WRITE_TOOLS | frozenset({DELETE_TOOL_NAME}) | extra_excluded; assign in source target order to excluded.
  // Source: vvaharness/backends/harness/deepagents/redaction.py:100-100
  End this invocation with [RedactToolResults(), ExcludeTools(excluded)].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/redaction.py:103-106
In source order: Evaluate once ['RedactToolResults', 'read_only_middleware']; assign in source target order to __all__.
```

## Local import links

- `from vvaharness.backends.harness.deepagents.exclude_tools import ExcludeTools` at source line 27: `source_detail/vvaharness/backends/harness/deepagents/exclude_tools.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.models import DELETE_TOOL_NAME` at source line 28: `source_detail/vvaharness/backends/harness/deepagents/models.py.sudo.md`.
- `from vvaharness.backends.harness.models import NATIVE_CONTENT_TOOLS, NATIVE_WRITE_TOOLS` at source line 29: `source_detail/vvaharness/backends/harness/models.py.sudo.md`.
- `from vvaharness.backends.llm.tools import sanitize_packed_text` at source line 30: `source_detail/vvaharness/backends/llm/tools.py.sudo.md`.
- `from vvaharness.report.redact import redact_counts` at source line 31: `source_detail/vvaharness/report/redact.py.sudo.md`.
