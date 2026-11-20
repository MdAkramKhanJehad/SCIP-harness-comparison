# vvaharness/validation/io/message_logger.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/validation/io/message_logger.py.evidence.json`. SHA-256: `81d6c58914463b39d12d616cbf453d2fb59f0b0e2590aac42877a718bc403c06`.

```sudo
// Source: vvaharness/validation/io/message_logger.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import dataclasses; preserve alias and import-time effects. Then Resolve source import import json; preserve alias and import-time effects. Then Resolve source import from collections.abc import AsyncIterator, Callable, Mapping; preserve alias and import-time effects.
// Source: vvaharness/validation/io/message_logger.py:22-34
In source order: Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from typing import cast; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness import HarnessAssistantText, HarnessMessage, HarnessResult, HarnessSessionInit, HarnessToolResult, HarnessToolUse; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import console, logs; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.constants.artifacts import SESSION_LOG_FILENAME; preserve alias and import-time effects.
// Source: vvaharness/validation/io/message_logger.py:36-36
In source order: Evaluate once logs.get_logger(__name__); assign in source target order to log.
// Source: vvaharness/validation/io/message_logger.py:39-40
// Source signature: _serialize(message: HarnessMessage) -> Mapping[str, object]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _serialize(message) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/io/message_logger.py:40-40
  End this invocation with dataclasses.asdict(message).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/io/message_logger.py:43-48
// Source signature: _agent_desc(message: HarnessToolUse) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _agent_desc(message) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/io/message_logger.py:44-44
  In source order: Retain source documentation literal source_literal_44_4; it is not a model call.
  // Source: vvaharness/validation/io/message_logger.py:45-46
  if (the source predicate not isinstance(message.input, dict) is truthy) {
    // Source: vvaharness/validation/io/message_logger.py:46-46
    End this invocation with 'sub-agent'.
  }
  // Source: vvaharness/validation/io/message_logger.py:47-47
  In source order: Evaluate once message.input.get('description'); assign in source target order to raw.
  // Source: vvaharness/validation/io/message_logger.py:48-48
  End this invocation with raw if isinstance(raw, str) else 'sub-agent'.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/io/message_logger.py:51-59
// Source signature: _log_key_event(message: HarnessMessage) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _log_key_event(message) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/io/message_logger.py:52-59
  if (the source predicate isinstance(message, HarnessToolUse) is truthy) {
    // Source: vvaharness/validation/io/message_logger.py:53-53
    In source order: Evaluate log.info('Tool call: %s', message.name); retain side effects and discard the expression result.
    // Source: vvaharness/validation/io/message_logger.py:54-55
    if (the source predicate message.name == 'Agent' is truthy) {
      // Source: vvaharness/validation/io/message_logger.py:55-55
      In source order: Evaluate log.info('Agent spawned: %s', _agent_desc(message)); retain side effects and discard the expression result.
    }
  }
  else {
    // Source: vvaharness/validation/io/message_logger.py:56-59
    if (the source predicate isinstance(message, HarnessSessionInit) is truthy) {
      // Source: vvaharness/validation/io/message_logger.py:57-57
      In source order: Evaluate log.info('Session initialized'); retain side effects and discard the expression result.
    }
    else {
      // Source: vvaharness/validation/io/message_logger.py:58-59
      if (the source predicate isinstance(message, HarnessResult) is truthy) {
        // Source: vvaharness/validation/io/message_logger.py:59-59
        In source order: Evaluate log.info('Session completed: %s', message.subtype); retain side effects and discard the expression result.
      }
    }
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/io/message_logger.py:62-67
// Source signature: _format_tool_use(message: HarnessToolUse) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _format_tool_use(message) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/io/message_logger.py:63-64
  In source order: Retain source documentation literal source_literal_63_4; it is not a model call. Then Evaluate once (message.tool_id or '')[-8:]; assign in source target order to tid.
  // Source: vvaharness/validation/io/message_logger.py:65-66
  if (the source predicate message.name == 'Agent' is truthy) {
    // Source: vvaharness/validation/io/message_logger.py:66-66
    End this invocation with source_template_66_15.
  }
  // Source: vvaharness/validation/io/message_logger.py:67-67
  End this invocation with source_template_67_11.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/io/message_logger.py:70-73
// Source signature: _format_assistant_text(message: HarnessAssistantText) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _format_assistant_text(message) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/io/message_logger.py:71-72
  In source order: Retain source documentation literal source_literal_71_4; it is not a model call. Then Evaluate once message.text.strip(); assign in source target order to text.
  // Source: vvaharness/validation/io/message_logger.py:73-73
  End this invocation with [source_template_73_12] if text else [].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/io/message_logger.py:76-82
// Source signature: _format_terminal(message: HarnessMessage) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _format_terminal(message) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/io/message_logger.py:77-77
  In source order: Retain source documentation literal source_literal_77_4; it is not a model call.
  // Source: vvaharness/validation/io/message_logger.py:78-79
  if (the source predicate isinstance(message, HarnessToolResult) is truthy) {
    // Source: vvaharness/validation/io/message_logger.py:79-79
    End this invocation with [source_template_79_16].
  }
  // Source: vvaharness/validation/io/message_logger.py:80-81
  if (the source predicate isinstance(message, HarnessResult) is truthy) {
    // Source: vvaharness/validation/io/message_logger.py:81-81
    End this invocation with [source_template_81_16].
  }
  // Source: vvaharness/validation/io/message_logger.py:82-82
  End this invocation with [].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/io/message_logger.py:85-88
// Source signature: _fmt_session_init(message: HarnessMessage) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _fmt_session_init(message) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/io/message_logger.py:86-87
  In source order: Evaluate once cast(HarnessSessionInit, message); assign in source target order to m. Then Evaluate once m.session_id[:12] if m.session_id else ''; assign in source target order to sid.
  // Source: vvaharness/validation/io/message_logger.py:88-88
  End this invocation with [source_template_88_12].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/io/message_logger.py:91-92
// Source signature: _fmt_tool_use(message: HarnessMessage) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _fmt_tool_use(message) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/io/message_logger.py:92-92
  End this invocation with [_format_tool_use(cast(HarnessToolUse, message))].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/io/message_logger.py:95-96
// Source signature: _fmt_assistant_text(message: HarnessMessage) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _fmt_assistant_text(message) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/io/message_logger.py:96-96
  End this invocation with _format_assistant_text(cast(HarnessAssistantText, message)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/io/message_logger.py:99-103
In source order: For _LIVE_FORMATTERS, assign {HarnessSessionInit: _fmt_session_init, HarnessToolUse: _fmt_tool_use, HarnessAssistantText: _fmt_assistant_text}; source annotation dict[type, Callable[[HarnessMessage], list[str]]].
// Source: vvaharness/validation/io/message_logger.py:106-107
// Source signature: _format_live(message: HarnessMessage) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _format_live(message) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/io/message_logger.py:107-107
  End this invocation with _LIVE_FORMATTERS.get(type(message), _format_terminal)(message).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/io/message_logger.py:110-112
// Source signature: _print_live(message: HarnessMessage) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _print_live(message) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/io/message_logger.py:111-112
  for each line in _format_live(message) {
    // Source: vvaharness/validation/io/message_logger.py:112-112
    In source order: Evaluate console.write(line); retain side effects and discard the expression result.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/io/message_logger.py:115-129
// Source signature: _process_message(message: HarnessMessage, observed_sid: str, live: bool) -> tuple[int | None, str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _process_message(message, observed_sid, live) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/io/message_logger.py:118-119
  In source order: Retain source documentation literal source_literal_118_4; it is not a model call. Then Evaluate _log_key_event(message); retain side effects and discard the expression result.
  // Source: vvaharness/validation/io/message_logger.py:120-121
  if (the source predicate live is truthy) {
    // Source: vvaharness/validation/io/message_logger.py:121-121
    In source order: Evaluate _print_live(message); retain side effects and discard the expression result.
  }
  // Source: vvaharness/validation/io/message_logger.py:122-123
  if (the source predicate isinstance(message, HarnessSessionInit) and message.session_id is truthy) {
    // Source: vvaharness/validation/io/message_logger.py:123-123
    In source order: Evaluate once message.session_id; assign in source target order to observed_sid.
  }
  // Source: vvaharness/validation/io/message_logger.py:124-128
  if (the source predicate isinstance(message, HarnessResult) is truthy) {
    // Source: vvaharness/validation/io/message_logger.py:125-125
    In source order: Evaluate once message.session_id or observed_sid; assign in source target order to observed_sid.
    // Source: vvaharness/validation/io/message_logger.py:126-127
    if (the source predicate message.subtype == 'error_max_budget_usd' is truthy) {
      // Source: vvaharness/validation/io/message_logger.py:127-127
      In source order: Evaluate log.warning('Validation session halted: max_budget_usd exceeded'); retain side effects and discard the expression result.
    }
    // Source: vvaharness/validation/io/message_logger.py:128-128
    End this invocation with (0 if message.subtype == 'success' else 1, observed_sid).
  }
  // Source: vvaharness/validation/io/message_logger.py:129-129
  End this invocation with (None, observed_sid).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/io/message_logger.py:132-150
// Source signature: stream_and_log(messages: AsyncIterator[HarnessMessage], log_dir: Path, session_id: str, live: bool) -> tuple[int, str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn stream_and_log(messages, log_dir, session_id, live) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  This callable produces a coroutine or async generator; await/suspension positions remain in source expressions.
  // Source: vvaharness/validation/io/message_logger.py:138-142
  In source order: Retain source documentation literal source_literal_138_4; it is not a model call. Then Evaluate log_dir.mkdir(parents=True, exist_ok=True); retain side effects and discard the expression result. Then Evaluate once log_dir / SESSION_LOG_FILENAME; assign in source target order to session_log. Then Evaluate once 1; assign in source target order to exit_code. Then Evaluate once session_id; assign in source target order to observed_sid.
  // Source: vvaharness/validation/io/message_logger.py:143-149
  Enter source context managers left-to-right: session_log.open('w') bound to f {
    // Source: vvaharness/validation/io/message_logger.py:144-149
    Obtain/advance the following source async iterator by awaiting, without inventing parallel dispatch.
    for each message in messages {
      // Source: vvaharness/validation/io/message_logger.py:145-147
      In source order: Evaluate f.write(json.dumps(_serialize(message), default=str) + source_literal_145_67); retain side effects and discard the expression result. Then Evaluate f.flush(); retain side effects and discard the expression result. Then Evaluate once _process_message(message, observed_sid, live); assign in source target order to (new_code, observed_sid).
      // Source: vvaharness/validation/io/message_logger.py:148-149
      if (the source predicate new_code is not None is truthy) {
        // Source: vvaharness/validation/io/message_logger.py:149-149
        In source order: Evaluate once new_code; assign in source target order to exit_code.
      }
    }
  }
  Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
  // Source: vvaharness/validation/io/message_logger.py:150-150
  End this invocation with (exit_code, observed_sid).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.backends.harness import HarnessAssistantText, HarnessMessage, HarnessResult, HarnessSessionInit, HarnessToolResult, HarnessToolUse` at source line 25: `source_detail/vvaharness/backends/harness/__init__.py.sudo.md`.
- `from vvaharness.util import console, logs` at source line 33: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import console, logs` at source line 33: `source_detail/vvaharness/util/console.py.sudo.md`.
- `from vvaharness.util import console, logs` at source line 33: `source_detail/vvaharness/util/logs.py.sudo.md`.
- `from vvaharness.validation.constants.artifacts import SESSION_LOG_FILENAME` at source line 34: `source_detail/vvaharness/validation/constants/artifacts.py.sudo.md`.
