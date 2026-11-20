# vvaharness/backends/harness/deepagents/translate.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/backends/harness/deepagents/translate.py.evidence.json`. SHA-256: `030740386dbc60778d5a10267492603afc456cb3af26c85fc6f3853d0947c820`.

```sudo
// Source: vvaharness/backends/harness/deepagents/translate.py:15-26
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from collections.abc import AsyncIterator, Mapping, Sequence; preserve alias and import-time effects. Then Resolve source import from langchain_core.messages import AIMessage, BaseMessage, ToolMessage; preserve alias and import-time effects. Then Resolve source import from langchain_core.messages.tool import ToolCall; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/deepagents/translate.py:27-44
In source order: Resolve source import from pydantic import BaseModel; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.deepagents.models import DeepAgentsGraphState, StreamEvent; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.deepagents.usage import SessionUsage, aggregate_usage_metadata; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.models import HarnessAssistantText, HarnessMessage, HarnessResult, HarnessToolResult, HarnessToolUse, OneShotResult; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm.models import ai_message_refused, finish_truncated, reply_finish; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/deepagents/translate.py:45-45
In source order: Resolve source import from vvaharness.util.tokens import TOKENS; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/deepagents/translate.py:48-56
// Source signature: _extract_text(message: AIMessage) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _extract_text(message) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/translate.py:49-50
  if (the source predicate isinstance(message.content, str) is truthy) {
    // Source: vvaharness/backends/harness/deepagents/translate.py:50-50
    End this invocation with message.content.
  }
  // Source: vvaharness/backends/harness/deepagents/translate.py:51-55
  In source order: Evaluate once [str(block.get('text', '')) for block in message.content if isinstance(block, dict) and block.get('type') == 'text']; assign in source target order to parts.
  // Source: vvaharness/backends/harness/deepagents/translate.py:56-56
  End this invocation with ''.join(parts).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/translate.py:59-60
// Source signature: _tool_calls(message: AIMessage) -> list[ToolCall]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _tool_calls(message) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/translate.py:60-60
  End this invocation with list(message.tool_calls).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/translate.py:63-70
// Source signature: _last_ai_text(messages: Sequence[BaseMessage]) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _last_ai_text(messages) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/translate.py:64-64
  In source order: Retain source documentation literal source_literal_64_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/translate.py:65-69
  for each message in reversed(messages) {
    // Source: vvaharness/backends/harness/deepagents/translate.py:66-69
    if (the source predicate isinstance(message, AIMessage) is truthy) {
      // Source: vvaharness/backends/harness/deepagents/translate.py:67-67
      In source order: Evaluate once _extract_text(message).strip(); assign in source target order to text.
      // Source: vvaharness/backends/harness/deepagents/translate.py:68-69
      if (the source predicate text is truthy) {
        // Source: vvaharness/backends/harness/deepagents/translate.py:69-69
        End this invocation with text.
      }
    }
  }
  // Source: vvaharness/backends/harness/deepagents/translate.py:70-70
  End this invocation with None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/translate.py:73-78
// Source signature: _last_ai_message(messages: Sequence[BaseMessage]) -> AIMessage | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _last_ai_message(messages) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/translate.py:74-74
  In source order: Retain source documentation literal source_literal_74_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/translate.py:75-77
  for each message in reversed(messages) {
    // Source: vvaharness/backends/harness/deepagents/translate.py:76-77
    if (the source predicate isinstance(message, AIMessage) is truthy) {
      // Source: vvaharness/backends/harness/deepagents/translate.py:77-77
      End this invocation with message.
    }
  }
  // Source: vvaharness/backends/harness/deepagents/translate.py:78-78
  End this invocation with None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/translate.py:81-84
// Source signature: reply_truncated(messages: Sequence[BaseMessage]) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn reply_truncated(messages) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/translate.py:82-83
  In source order: Retain source documentation literal source_literal_82_4; it is not a model call. Then Evaluate once _last_ai_message(messages); assign in source target order to message.
  // Source: vvaharness/backends/harness/deepagents/translate.py:84-84
  End this invocation with message is not None and finish_truncated(reply_finish(message.response_metadata or {})).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/translate.py:87-96
// Source signature: reply_refusal(messages: Sequence[BaseMessage]) -> tuple[bool, str | None]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn reply_refusal(messages) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/translate.py:88-88
  In source order: Retain source documentation literal source_literal_88_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/translate.py:91-95
  for each message in messages {
    // Source: vvaharness/backends/harness/deepagents/translate.py:92-95
    if (the source predicate isinstance(message, AIMessage) is truthy) {
      // Source: vvaharness/backends/harness/deepagents/translate.py:93-93
      In source order: Evaluate once ai_message_refused(message); assign in source target order to (refused, category).
      // Source: vvaharness/backends/harness/deepagents/translate.py:94-95
      if (the source predicate refused is truthy) {
        // Source: vvaharness/backends/harness/deepagents/translate.py:95-95
        End this invocation with (True, category).
      }
    }
  }
  // Source: vvaharness/backends/harness/deepagents/translate.py:96-96
  End this invocation with (False, None).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/translate.py:99-120
// Source signature: translate_final_state(state: DeepAgentsGraphState, *, oneshot: bool=False) -> OneShotResult
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn translate_final_state(state, oneshot) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/translate.py:100-103
  In source order: Retain source documentation literal source_literal_100_4; it is not a model call. Then Evaluate once state.get('messages', []); assign in source target order to messages. Then Evaluate once aggregate_usage_metadata(messages); assign in source target order to usage.
  // Source: vvaharness/backends/harness/deepagents/translate.py:104-105
  if (the source predicate usage is not None is truthy) {
    // Source: vvaharness/backends/harness/deepagents/translate.py:105-105
    In source order: Evaluate TOKENS.add(usage, turns=usage.get('turns')); retain side effects and discard the expression result.
  }
  // Source: vvaharness/backends/harness/deepagents/translate.py:106-107
  In source order: Evaluate once reply_truncated(messages); assign in source target order to truncated. Then Evaluate once state.get('structured_response'); assign in source target order to structured.
  // Source: vvaharness/backends/harness/deepagents/translate.py:108-115
  if (the source predicate isinstance(structured, BaseModel) is truthy) {
    // Source: vvaharness/backends/harness/deepagents/translate.py:110-115
    End this invocation with OneShotResult(result_text=structured.model_dump_json(), structured=structured, usage=usage, truncated=truncated).
  }
  // Source: vvaharness/backends/harness/deepagents/translate.py:116-116
  In source order: Evaluate once reply_refusal(messages); assign in source target order to (refused, category).
  // Source: vvaharness/backends/harness/deepagents/translate.py:117-120
  End this invocation with OneShotResult(result_text=_last_ai_text(messages), usage=usage, truncated=truncated, refused=refused, refusal_category=category).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/translate.py:123-132
// Source signature: _messages_from_event(payload: Mapping[str, DeepAgentsGraphState]) -> list[BaseMessage]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _messages_from_event(payload) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/translate.py:124-125
  In source order: Retain source documentation literal source_literal_124_4; it is not a model call. Then For messages, assign []; source annotation list[BaseMessage].
  // Source: vvaharness/backends/harness/deepagents/translate.py:126-131
  for each update in payload.values() {
    // Source: vvaharness/backends/harness/deepagents/translate.py:127-128
    if (the source predicate not isinstance(update, dict) is truthy) {
      // Source: vvaharness/backends/harness/deepagents/translate.py:128-128
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/backends/harness/deepagents/translate.py:129-129
    In source order: Evaluate once update.get('messages'); assign in source target order to node_messages.
    // Source: vvaharness/backends/harness/deepagents/translate.py:130-131
    if (the source predicate isinstance(node_messages, Sequence) is truthy) {
      // Source: vvaharness/backends/harness/deepagents/translate.py:131-131
      In source order: Evaluate messages.extend(node_messages); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/backends/harness/deepagents/translate.py:132-132
  End this invocation with messages.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/translate.py:135-174
// Source signature: translate_stream_events(event: StreamEvent | Mapping[str, DeepAgentsGraphState], seen_tool_call_ids: set[str], ns_to_agent: dict[tuple[str, ...], str] | None=None) -> AsyncIterator[HarnessMessage]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn translate_stream_events(event, seen_tool_call_ids, ns_to_agent) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  This callable produces a coroutine or async generator; await/suspension positions remain in source expressions.
  // Source: vvaharness/backends/harness/deepagents/translate.py:140-140
  In source order: Retain source documentation literal source_literal_140_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/translate.py:141-142
  if (the source predicate ns_to_agent is None is truthy) {
    // Source: vvaharness/backends/harness/deepagents/translate.py:142-142
    In source order: Evaluate once {}; assign in source target order to ns_to_agent.
  }
  // Source: vvaharness/backends/harness/deepagents/translate.py:143-144
  In source order: Evaluate once event if isinstance(event, tuple) else ((), event); assign in source target order to (namespace, payload). Then Evaluate once tuple(namespace) if namespace else None; assign in source target order to namespace_tag.
  // Source: vvaharness/backends/harness/deepagents/translate.py:145-174
  for each message in _messages_from_event(payload) {
    // Source: vvaharness/backends/harness/deepagents/translate.py:146-174
    if (the source predicate isinstance(message, AIMessage) is truthy) {
      // Source: vvaharness/backends/harness/deepagents/translate.py:147-147
      In source order: Evaluate once getattr(message, 'name', None); assign in source target order to name.
      // Source: vvaharness/backends/harness/deepagents/translate.py:148-149
      if (the source predicate name is truthy) {
        // Source: vvaharness/backends/harness/deepagents/translate.py:149-149
        In source order: Evaluate once name; assign in source target order to ns_to_agent[namespace].
      }
      // Source: vvaharness/backends/harness/deepagents/translate.py:150-151
      In source order: Evaluate once name or ns_to_agent.get(namespace); assign in source target order to agent. Then Evaluate once _extract_text(message); assign in source target order to text.
      // Source: vvaharness/backends/harness/deepagents/translate.py:152-153
      if (the source predicate text.strip() is truthy) {
        // Source: vvaharness/backends/harness/deepagents/translate.py:153-153
        In source order: Yield HarnessAssistantText(text=text, agent=agent, namespace=namespace_tag); suspend this generator until resumed.
      }
      // Source: vvaharness/backends/harness/deepagents/translate.py:154-167
      for each call in _tool_calls(message) {
        // Source: vvaharness/backends/harness/deepagents/translate.py:155-155
        In source order: Evaluate once call.get('id', ''); assign in source target order to tool_call_id.
        // Source: vvaharness/backends/harness/deepagents/translate.py:156-157
        if (the source predicate not tool_call_id is truthy) {
          // Source: vvaharness/backends/harness/deepagents/translate.py:157-157
          Continue the immediately enclosing source loop at its next iteration.
        }
        // Source: vvaharness/backends/harness/deepagents/translate.py:158-159
        if (the source predicate tool_call_id in seen_tool_call_ids is truthy) {
          // Source: vvaharness/backends/harness/deepagents/translate.py:159-159
          Continue the immediately enclosing source loop at its next iteration.
        }
        // Source: vvaharness/backends/harness/deepagents/translate.py:160-167
        In source order: Evaluate seen_tool_call_ids.add(tool_call_id); retain side effects and discard the expression result. Then Yield HarnessToolUse(tool_id=tool_call_id, name=call.get('name', ''), input=call.get('args', {}), agent=agent, namespace=namespace_tag); suspend this generator until resumed.
      }
    }
    else {
      // Source: vvaharness/backends/harness/deepagents/translate.py:168-174
      if (the source predicate isinstance(message, ToolMessage) is truthy) {
        // Source: vvaharness/backends/harness/deepagents/translate.py:169-174
        In source order: Yield HarnessToolResult(content=message.content, is_error=getattr(message, 'status', 'success') == 'error', agent=ns_to_agent.get(namespace), namespace=namespace_tag); suspend this generator until resumed.
      }
    }
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/translate.py:177-212
// Source signature: make_terminal_result(state: DeepAgentsGraphState, session_id: str | None=None, stream_usage: SessionUsage | None=None) -> HarnessResult
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn make_terminal_result(state, session_id, stream_usage) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/translate.py:182-187
  In source order: Retain source documentation literal source_literal_182_4; it is not a model call. Then Evaluate once state.get('messages', []); assign in source target order to messages. Then Evaluate once _last_ai_text(messages); assign in source target order to final_text. Then Evaluate once state.get('structured_response'); assign in source target order to structured. Then Evaluate once (False, None); assign in source target order to (refused, category).
  // Source: vvaharness/backends/harness/deepagents/translate.py:188-192
  if (the source predicate isinstance(structured, BaseModel) is truthy) {
    // Source: vvaharness/backends/harness/deepagents/translate.py:189-189
    In source order: Evaluate once structured.model_dump_json(); assign in source target order to final_text.
  }
  else {
    // Source: vvaharness/backends/harness/deepagents/translate.py:191-192
    In source order: Evaluate once None; assign in source target order to structured. Then Evaluate once reply_refusal(messages); assign in source target order to (refused, category).
  }
  // Source: vvaharness/backends/harness/deepagents/translate.py:194-195
  In source order: Evaluate once state.get('usage'); assign in source target order to raw_usage. Then Evaluate once raw_usage if isinstance(raw_usage, dict) else None; assign in source target order to usage.
  // Source: vvaharness/backends/harness/deepagents/translate.py:196-197
  if (the source predicate usage is None is truthy) {
    // Source: vvaharness/backends/harness/deepagents/translate.py:197-197
    In source order: Evaluate once stream_usage if stream_usage is not None else aggregate_usage_metadata(messages); assign in source target order to usage.
  }
  // Source: vvaharness/backends/harness/deepagents/translate.py:198-199
  if (the source predicate usage is not None is truthy) {
    // Source: vvaharness/backends/harness/deepagents/translate.py:199-199
    In source order: Evaluate TOKENS.add(usage, turns=usage.get('turns')); retain side effects and discard the expression result.
  }
  // Source: vvaharness/backends/harness/deepagents/translate.py:201-212
  End this invocation with HarnessResult(subtype='success', session_id=session_id, result_text=final_text, structured=structured, usage=usage, total_cost_usd=None, state=state, truncated=reply_truncated(messages), refused=refused, refusal_category=category).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/translate.py:215-221
In source order: Evaluate once ['make_terminal_result', 'reply_refusal', 'reply_truncated', 'translate_final_state', 'translate_stream_events']; assign in source target order to __all__.
```

## Local import links

- `from vvaharness.backends.harness.deepagents.models import DeepAgentsGraphState, StreamEvent` at source line 29: `source_detail/vvaharness/backends/harness/deepagents/models.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.usage import SessionUsage, aggregate_usage_metadata` at source line 30: `source_detail/vvaharness/backends/harness/deepagents/usage.py.sudo.md`.
- `from vvaharness.backends.harness.models import HarnessAssistantText, HarnessMessage, HarnessResult, HarnessToolResult, HarnessToolUse, OneShotResult` at source line 34: `source_detail/vvaharness/backends/harness/models.py.sudo.md`.
- `from vvaharness.backends.llm.models import ai_message_refused, finish_truncated, reply_finish` at source line 44: `source_detail/vvaharness/backends/llm/models.py.sudo.md`.
- `from vvaharness.util.tokens import TOKENS` at source line 45: `source_detail/vvaharness/util/tokens.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../../prompt_representation/vvaharness/backends/harness/deepagents/translate.py.sudo.md). Exact strings in the evidence asset support this conversion.
