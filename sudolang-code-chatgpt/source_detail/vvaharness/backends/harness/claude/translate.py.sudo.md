# vvaharness/backends/harness/claude/translate.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/backends/harness/claude/translate.py.evidence.json`. SHA-256: `c0bbeff0b7b6beb1e24ba1809d407166045d988aa6d0cb2a80ffe162b2b95a61`.

```sudo
// Source: vvaharness/backends/harness/claude/translate.py:15-29
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from collections.abc import Callable, Mapping; preserve alias and import-time effects. Then Resolve source import from typing import cast; preserve alias and import-time effects. Then Resolve source import from claude_agent_sdk import AssistantMessage, ResultMessage, SystemMessage, TextBlock, ToolUseBlock, UserMessage; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/claude/translate.py:30-40
In source order: Resolve source import from pydantic import BaseModel; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.models import HarnessAssistantText, HarnessMessage, HarnessResult, HarnessSessionInit, HarnessToolResult, HarnessToolUse; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.tokens import TOKENS, TokenUsage; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/claude/translate.py:43-51
// Source signature: validate_structured(raw: object, response_model: type | None) -> BaseModel | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn validate_structured(raw, response_model) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/claude/translate.py:46-46
  In source order: Retain source documentation literal source_literal_46_4; it is not a model call.
  // Source: vvaharness/backends/harness/claude/translate.py:47-48
  if (the source predicate response_model is None is truthy) {
    // Source: vvaharness/backends/harness/claude/translate.py:48-48
    End this invocation with None.
  }
  // Source: vvaharness/backends/harness/claude/translate.py:49-50
  if (the source predicate isinstance(raw, Mapping) is truthy) {
    // Source: vvaharness/backends/harness/claude/translate.py:50-50
    End this invocation with cast(BaseModel, response_model.model_validate(raw)).
  }
  // Source: vvaharness/backends/harness/claude/translate.py:51-51
  End this invocation with cast(BaseModel, raw) if isinstance(raw, response_model) else None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/claude/translate.py:54-61
// Source signature: translate_init(message: SystemMessage) -> list[HarnessMessage]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn translate_init(message) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/claude/translate.py:55-57
  In source order: Retain source documentation literal source_literal_55_4; it is not a model call. Then For data, assign message.data if isinstance(message.data, Mapping) else {}; source annotation Mapping[str, object]. Then Evaluate once data.get('session_id'); assign in source target order to sid_raw.
  // Source: vvaharness/backends/harness/claude/translate.py:58-61
  End this invocation with [HarnessSessionInit(session_id=sid_raw if isinstance(sid_raw, str) else '', raw=dict(data))].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/claude/translate.py:64-73
// Source signature: translate_assistant(message: AssistantMessage) -> list[HarnessMessage]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn translate_assistant(message) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/claude/translate.py:65-66
  In source order: Retain source documentation literal source_literal_65_4; it is not a model call. Then For out, assign []; source annotation list[HarnessMessage].
  // Source: vvaharness/backends/harness/claude/translate.py:67-72
  for each block in message.content {
    // Source: vvaharness/backends/harness/claude/translate.py:68-72
    if (the source predicate isinstance(block, ToolUseBlock) is truthy) {
      // Source: vvaharness/backends/harness/claude/translate.py:69-70
      In source order: For inp, assign block.input if isinstance(block.input, Mapping) else {}; source annotation Mapping[str, object]. Then Evaluate out.append(HarnessToolUse(tool_id=block.id or '', name=block.name, input=dict(inp))); retain side effects and discard the expression result.
    }
    else {
      // Source: vvaharness/backends/harness/claude/translate.py:71-72
      if (the source predicate isinstance(block, TextBlock) is truthy) {
        // Source: vvaharness/backends/harness/claude/translate.py:72-72
        In source order: Evaluate out.append(HarnessAssistantText(text=block.text)); retain side effects and discard the expression result.
      }
    }
  }
  // Source: vvaharness/backends/harness/claude/translate.py:73-73
  End this invocation with out.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/claude/translate.py:76-87
// Source signature: translate_tool_result(message: UserMessage) -> list[HarnessMessage]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn translate_tool_result(message) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/claude/translate.py:77-80
  In source order: Retain source documentation literal source_literal_77_4; it is not a model call. Then Evaluate once message.tool_use_result; assign in source target order to tru. Then For items, assign list(tru) if isinstance(tru, list) else [tru]; source annotation list[object]. Then For out, assign []; source annotation list[HarnessMessage].
  // Source: vvaharness/backends/harness/claude/translate.py:81-86
  for each item in items {
    // Source: vvaharness/backends/harness/claude/translate.py:82-86
    if (the source predicate isinstance(item, Mapping) is truthy) {
      // Source: vvaharness/backends/harness/claude/translate.py:83-84
      In source order: Evaluate out.append(HarnessToolResult(is_error=bool(item.get('is_error', False)), content=dict(item))); retain side effects and discard the expression result.
    }
    else {
      // Source: vvaharness/backends/harness/claude/translate.py:86-86
      In source order: Evaluate out.append(HarnessToolResult(is_error=False, content=item)); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/backends/harness/claude/translate.py:87-87
  End this invocation with out.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/claude/translate.py:90-105
// Source signature: translate_result(message: ResultMessage, response_model: type | None=None) -> list[HarnessMessage]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn translate_result(message, response_model) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/claude/translate.py:93-95
  In source order: Retain source documentation literal source_literal_93_4; it is not a model call. Then Evaluate TOKENS.add(cast('TokenUsage | None', message.usage), usd=message.total_cost_usd); retain side effects and discard the expression result.
  // Source: vvaharness/backends/harness/claude/translate.py:96-105
  End this invocation with [HarnessResult(subtype=message.subtype, is_error=bool(message.is_error), session_id=message.session_id, result_text=message.result, structured=validate_structured(message.structured_output, response_model), errors=message.errors, usage=cast('TokenUsage | None', message.usage), total_cost_usd=message.total_cost_usd)].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/claude/translate.py:108-110
// Source signature: _translate_system(message: object) -> list[HarnessMessage]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _translate_system(message) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/claude/translate.py:109-109
  In source order: Evaluate once cast(SystemMessage, message); assign in source target order to m.
  // Source: vvaharness/backends/harness/claude/translate.py:110-110
  End this invocation with translate_init(m) if m.subtype == 'init' else [].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/claude/translate.py:113-115
// Source signature: _translate_user(message: object) -> list[HarnessMessage]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _translate_user(message) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/claude/translate.py:114-114
  In source order: Evaluate once cast(UserMessage, message); assign in source target order to m.
  // Source: vvaharness/backends/harness/claude/translate.py:115-115
  End this invocation with translate_tool_result(m) if m.tool_use_result is not None else [].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/claude/translate.py:118-122
In source order: For _TRANSLATORS, assign {SystemMessage: _translate_system, AssistantMessage: lambda m: translate_assistant(cast(AssistantMessage, m)), UserMessage: _translate_user}; source annotation dict[type, Callable[[object], list[HarnessMessage]]].
// Source: vvaharness/backends/harness/claude/translate.py:125-132
// Source signature: translate(message: object, response_model: type | None=None) -> list[HarnessMessage]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn translate(message, response_model) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/claude/translate.py:128-128
  In source order: Retain source documentation literal source_literal_128_4; it is not a model call.
  // Source: vvaharness/backends/harness/claude/translate.py:129-130
  if (the source predicate isinstance(message, ResultMessage) is truthy) {
    // Source: vvaharness/backends/harness/claude/translate.py:130-130
    End this invocation with translate_result(message, response_model).
  }
  // Source: vvaharness/backends/harness/claude/translate.py:131-131
  In source order: Evaluate once _TRANSLATORS.get(type(message)); assign in source target order to handler.
  // Source: vvaharness/backends/harness/claude/translate.py:132-132
  End this invocation with handler(message) if handler is not None else [].
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.backends.harness.models import HarnessAssistantText, HarnessMessage, HarnessResult, HarnessSessionInit, HarnessToolResult, HarnessToolUse` at source line 32: `source_detail/vvaharness/backends/harness/models.py.sudo.md`.
- `from vvaharness.util.tokens import TOKENS, TokenUsage` at source line 40: `source_detail/vvaharness/util/tokens.py.sudo.md`.
