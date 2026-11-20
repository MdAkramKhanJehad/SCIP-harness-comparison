# vvaharness/pipeline/stages/replay.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/pipeline/stages/replay.py.evidence.json`. SHA-256: `e3c8629ed4870e52b4dff325f262365bfa3fa764335e467d77a26fae444795d4`.

```sudo
// Source: vvaharness/pipeline/stages/replay.py:15-20
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import threading; preserve alias and import-time effects. Then Resolve source import import time; preserve alias and import-time effects. Then Resolve source import from collections.abc import Callable, Iterator; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/replay.py:21-26
In source order: Resolve source import from concurrent.futures import Future; preserve alias and import-time effects. Then Resolve source import from contextlib import contextmanager; preserve alias and import-time effects. Then Resolve source import from typing import Any, TypeVar; preserve alias and import-time effects. Then Resolve source import from uuid import uuid4; preserve alias and import-time effects. Then Resolve source import from langchain.agents.middleware.types import AgentMiddleware; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/replay.py:28-38
In source order: Resolve source import from vvaharness.backends.llm import cli as _cli; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm.deepagents import release_pinned_session; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm.deepagents import resume_agentic as _resume_agentic; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm.models import TIMEOUT_STOP_GRACE_SECONDS, ClockKind, ModelRefusal, call_timeout_error, effort_scaled_seconds; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import console, logs; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/replay.py:39-61
In source order: Resolve source import from vvaharness.util.counters import COUNTERS; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.events import Event; preserve alias and import-time effects. Then Evaluate once logs.get_logger(__name__); assign in source target order to log. Then Evaluate once ['S2_REPLAY_INSTRUCTION', 'S4_REPLAY_INSTRUCTION', 'S6_REPLAY_INSTRUCTION', 'S8_REPLAY_INSTRUCTION', 'RecordTranscript', 'Transcript', 'deadline_bound', 'pinned_session', 'replay_prompt', 'resume_or_replay', 'run_with_deadline', 'session_id_for', 'settle_future', 'start_daemon']; assign in source target order to __all__. Then Evaluate once TypeVar('_T'); assign in source target order to _T.
// Source: vvaharness/pipeline/stages/replay.py:63-84
In source order: Evaluate once 4000; assign in source target order to _MAX_ENTRY_CHARS. Then Evaluate once {'human': 'USER', 'ai': 'ASSISTANT', 'tool': 'TOOL RESULT', 'system': 'SYSTEM'}; assign in source target order to _ROLE_OF. Then Evaluate once source_literal_67_4; assign in source target order to _PREAMBLE. Then Evaluate once _PREAMBLE + source_literal_75_4; assign in source target order to S2_REPLAY_INSTRUCTION. Then Evaluate once _PREAMBLE + source_literal_81_4; assign in source target order to S4_REPLAY_INSTRUCTION.
// Source: vvaharness/pipeline/stages/replay.py:86-97
In source order: Evaluate once _PREAMBLE + source_literal_87_4; assign in source target order to S6_REPLAY_INSTRUCTION. Then Evaluate once _PREAMBLE + source_literal_94_4; assign in source target order to S8_REPLAY_INSTRUCTION.
// Source: vvaharness/pipeline/stages/replay.py:100-110
// Source signature: _text_of(content: Any) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _text_of(content) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/replay.py:101-101
  In source order: Retain source documentation literal source_literal_101_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/replay.py:102-103
  if (the source predicate isinstance(content, str) is truthy) {
    // Source: vvaharness/pipeline/stages/replay.py:103-103
    End this invocation with content.
  }
  // Source: vvaharness/pipeline/stages/replay.py:104-109
  if (the source predicate isinstance(content, list) is truthy) {
    // Source: vvaharness/pipeline/stages/replay.py:105-108
    In source order: Evaluate once [str(b.get('text') or b.get('content') or '') if isinstance(b, dict) else str(b) for b in content]; assign in source target order to parts.
    // Source: vvaharness/pipeline/stages/replay.py:109-109
    End this invocation with source_literal_109_15.join((p for p in parts if p)).
  }
  // Source: vvaharness/pipeline/stages/replay.py:110-110
  End this invocation with '' if content is None else str(content).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/replay.py:113-119
// Source signature: _role_of(message: Any) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _role_of(message) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/replay.py:114-114
  In source order: Retain source documentation literal source_literal_114_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/replay.py:115-118
  if (the source predicate isinstance(message, dict) is truthy) {
    // Source: vvaharness/pipeline/stages/replay.py:116-116
    In source order: Evaluate once str(message.get('role') or message.get('type') or ''); assign in source target order to raw.
  }
  else {
    // Source: vvaharness/pipeline/stages/replay.py:118-118
    In source order: Evaluate once str(getattr(message, 'type', None) or getattr(message, 'role', '') or ''); assign in source target order to raw.
  }
  // Source: vvaharness/pipeline/stages/replay.py:119-119
  End this invocation with _ROLE_OF.get(raw.lower(), raw.upper() or 'MESSAGE').
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/replay.py:122-134
// Source signature: _tool_calls_of(message: Any) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _tool_calls_of(message) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/replay.py:123-126
  In source order: Retain source documentation literal source_literal_123_4; it is not a model call. Then Evaluate once (message.get('tool_calls') if isinstance(message, dict) else getattr(message, 'tool_calls', None)) or []; assign in source target order to calls. Then Evaluate once []; assign in source target order to lines.
  // Source: vvaharness/pipeline/stages/replay.py:127-133
  for each call in calls {
    // Source: vvaharness/pipeline/stages/replay.py:128-129
    if (the source predicate not isinstance(call, dict) is truthy) {
      // Source: vvaharness/pipeline/stages/replay.py:129-129
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/pipeline/stages/replay.py:130-133
    In source order: Evaluate once call.get('function') if isinstance(call.get('function'), dict) else {}; assign in source target order to fn. Then Evaluate once call.get('name') or fn.get('name') or '?'; assign in source target order to name. Then Evaluate once call.get('args') or fn.get('arguments') or ''; assign in source target order to args. Then Evaluate lines.append(source_template_133_21); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/replay.py:134-134
  End this invocation with source_literal_134_11.join(lines).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/replay.py:137-179
interface Transcript {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/pipeline/stages/replay.py:138-138
  In source order: Retain source documentation literal source_literal_138_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/replay.py:140-143
  // Source signature: __init__(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/pipeline/stages/replay.py:141-143
    In source order: Retain source documentation literal source_literal_141_8; it is not a model call. Then For self._messages, assign []; source annotation list[Any]. Then Evaluate once threading.Lock(); assign in source target order to self._lock.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/pipeline/stages/replay.py:145-153
  // Source signature: record(self, messages: Any) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn record(self, messages) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/pipeline/stages/replay.py:146-146
    In source order: Retain source documentation literal source_literal_146_8; it is not a model call.
    // Source: vvaharness/pipeline/stages/replay.py:147-150
    Perform the following protected operations {
      // Source: vvaharness/pipeline/stages/replay.py:148-148
      In source order: Evaluate once list(messages or []); assign in source target order to captured.
    }
    // Source: vvaharness/pipeline/stages/replay.py:149-150
    On the first matching source exception TypeError, in handler order {
      // Source: vvaharness/pipeline/stages/replay.py:150-150
      End this invocation with None.
    }
    // Source: vvaharness/pipeline/stages/replay.py:151-153
    Enter source context managers left-to-right: self._lock {
      // Source: vvaharness/pipeline/stages/replay.py:152-153
      if (the source predicate len(captured) >= len(self._messages) is truthy) {
        // Source: vvaharness/pipeline/stages/replay.py:153-153
        In source order: Evaluate once captured; assign in source target order to self._messages.
      }
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/pipeline/stages/replay.py:156-159
  // Source: vvaharness/pipeline/stages/replay.py:155-155
  Before creating this callable, evaluate and retain decorators top-to-bottom: property.
  // Source: vvaharness/pipeline/stages/replay.py:156-159
  // Source signature: captured(self) -> bool
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn captured(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/pipeline/stages/replay.py:157-157
    In source order: Retain source documentation literal source_literal_157_8; it is not a model call.
    // Source: vvaharness/pipeline/stages/replay.py:158-159
    Enter source context managers left-to-right: self._lock {
      // Source: vvaharness/pipeline/stages/replay.py:159-159
      End this invocation with bool(self._messages).
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vvaharness/pipeline/stages/replay.py:161-179
  // Source signature: render(self, *, max_chars: int=120000) -> str
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn render(self, max_chars) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/pipeline/stages/replay.py:162-162
    In source order: Retain source documentation literal source_literal_162_8; it is not a model call.
    // Source: vvaharness/pipeline/stages/replay.py:163-164
    Enter source context managers left-to-right: self._lock {
      // Source: vvaharness/pipeline/stages/replay.py:164-164
      In source order: Evaluate once list(self._messages); assign in source target order to held.
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    // Source: vvaharness/pipeline/stages/replay.py:165-165
    In source order: For blocks, assign []; source annotation list[str].
    // Source: vvaharness/pipeline/stages/replay.py:166-175
    for each message in held {
      // Source: vvaharness/pipeline/stages/replay.py:167-169
      In source order: Evaluate once message.get('content') if isinstance(message, dict) else getattr(message, 'content', ''); assign in source target order to raw. Then Evaluate once (_text_of(raw), _tool_calls_of(message)); assign in source target order to (body, calls).
      // Source: vvaharness/pipeline/stages/replay.py:170-171
      if (the source predicate not body and (not calls) is truthy) {
        // Source: vvaharness/pipeline/stages/replay.py:171-171
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/pipeline/stages/replay.py:172-174
      if (the source predicate len(body) > _MAX_ENTRY_CHARS is truthy) {
        // Source: vvaharness/pipeline/stages/replay.py:173-174
        In source order: Evaluate once body[:_MAX_ENTRY_CHARS] + source_template_174_26; assign in source target order to body.
      }
      // Source: vvaharness/pipeline/stages/replay.py:175-175
      In source order: Evaluate blocks.append(source_template_175_26 + (source_template_175_62 if calls else '')); retain side effects and discard the expression result.
    }
    // Source: vvaharness/pipeline/stages/replay.py:176-176
    In source order: Evaluate once source_literal_176_14.join(blocks); assign in source target order to out.
    // Source: vvaharness/pipeline/stages/replay.py:177-178
    if (the source predicate len(out) <= max_chars is truthy) {
      // Source: vvaharness/pipeline/stages/replay.py:178-178
      End this invocation with out.
    }
    // Source: vvaharness/pipeline/stages/replay.py:179-179
    End this invocation with source_literal_179_15 + out[-max_chars:].
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vvaharness/pipeline/stages/replay.py:182-203
interface RecordTranscript {
  Describe the source Python type, preserving its base/metaclass expression order: AgentMiddleware.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/pipeline/stages/replay.py:183-183
  In source order: Retain source documentation literal source_literal_183_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/replay.py:185-188
  // Source signature: __init__(self, sink: Transcript) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self, sink) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/pipeline/stages/replay.py:186-188
    In source order: Retain source documentation literal source_literal_186_8; it is not a model call. Then Evaluate super().__init__(); retain side effects and discard the expression result. Then Evaluate once sink; assign in source target order to self._sink.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/pipeline/stages/replay.py:191-193
  // Source: vvaharness/pipeline/stages/replay.py:190-190
  Before creating this callable, evaluate and retain decorators top-to-bottom: property.
  // Source: vvaharness/pipeline/stages/replay.py:191-193
  // Source signature: name(self) -> str
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn name(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/pipeline/stages/replay.py:192-192
    In source order: Retain source documentation literal source_literal_192_8; it is not a model call.
    // Source: vvaharness/pipeline/stages/replay.py:193-193
    End this invocation with 'RecordTranscript'.
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vvaharness/pipeline/stages/replay.py:195-198
  // Source signature: wrap_model_call(self, request: Any, handler: Callable[[Any], _T]) -> _T
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn wrap_model_call(self, request, handler) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/pipeline/stages/replay.py:196-197
    In source order: Retain source documentation literal source_literal_196_8; it is not a model call. Then Evaluate self._sink.record(getattr(request, 'messages', None)); retain side effects and discard the expression result.
    // Source: vvaharness/pipeline/stages/replay.py:198-198
    End this invocation with handler(request).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/pipeline/stages/replay.py:200-203
  // Source signature: awrap_model_call(self, request: Any, handler: Callable[[Any], Any]) -> Any
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn awrap_model_call(self, request, handler) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    This callable produces a coroutine or async generator; await/suspension positions remain in source expressions.
    // Source: vvaharness/pipeline/stages/replay.py:201-202
    In source order: Retain source documentation literal source_literal_201_8; it is not a model call. Then Evaluate self._sink.record(getattr(request, 'messages', None)); retain side effects and discard the expression result.
    // Source: vvaharness/pipeline/stages/replay.py:203-203
    End this invocation with await handler(request).
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vvaharness/pipeline/stages/replay.py:206-213
// Source signature: settle_future(fut: Future[_T], call: Callable[[], _T]) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn settle_future(fut, call) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/replay.py:207-207
  In source order: Retain source documentation literal source_literal_207_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/replay.py:208-209
  if (the source predicate not fut.set_running_or_notify_cancel() is truthy) {
    // Source: vvaharness/pipeline/stages/replay.py:209-209
    End this invocation with None.
  }
  // Source: vvaharness/pipeline/stages/replay.py:210-213
  Perform the following protected operations {
    // Source: vvaharness/pipeline/stages/replay.py:211-211
    In source order: Evaluate fut.set_result(call()); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/replay.py:212-213
  On the first matching source exception BaseException as exc, in handler order {
    // Source: vvaharness/pipeline/stages/replay.py:213-213
    In source order: Evaluate fut.set_exception(exc); retain side effects and discard the expression result.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/replay.py:216-220
// Source signature: start_daemon(call: Callable[[], _T], name: str) -> Future[_T]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn start_daemon(call, name) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/replay.py:217-219
  In source order: Retain source documentation literal source_literal_217_4; it is not a model call. Then For fut, assign Future(); source annotation Future[_T]. Then Evaluate threading.Thread(target=settle_future, args=(fut, call), name=name, daemon=True).start(); retain side effects and discard the expression result.
  // Source: vvaharness/pipeline/stages/replay.py:220-220
  End this invocation with fut.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/replay.py:223-234
// Source signature: _orphan_settled(stage: str, started: float) -> Callable[[Future], None]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _orphan_settled(stage, started) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/replay.py:224-224
  In source order: Retain source documentation literal source_literal_224_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/replay.py:226-232
  // Source signature: _on_done(fut: Future) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _on_done(fut) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/pipeline/stages/replay.py:227-228
    if (the source predicate fut.cancelled() is truthy) {
      // Source: vvaharness/pipeline/stages/replay.py:228-228
      End this invocation with None.
    }
    // Source: vvaharness/pipeline/stages/replay.py:229-232
    In source order: Evaluate once 'result' if fut.exception() is None else type(fut.exception()).__name__; assign in source target order to outcome. Then Evaluate COUNTERS.bump(source_template_230_22); retain side effects and discard the expression result. Then Evaluate log.warning(Event.STAGE_ORPHAN_SETTLED, stage=stage.split()[0], outcome=outcome, elapsed_s=round(time.monotonic() - started, 1)); retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/pipeline/stages/replay.py:234-234
  End this invocation with _on_done.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/replay.py:237-264
// Source signature: run_with_deadline(call: Callable[[], _T], *, seconds: float | None, stage: str, effort: str | None=None) -> _T
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn run_with_deadline(call, seconds, stage, effort) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/replay.py:239-239
  In source order: Retain source documentation literal source_literal_239_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/replay.py:242-243
  if (the source predicate not seconds or seconds <= 0 is truthy) {
    // Source: vvaharness/pipeline/stages/replay.py:243-243
    End this invocation with call().
  }
  // Source: vvaharness/pipeline/stages/replay.py:247-248
  In source order: Evaluate once time.monotonic(); assign in source target order to started. Then Evaluate once start_daemon(call, source_template_248_29); assign in source target order to fut.
  // Source: vvaharness/pipeline/stages/replay.py:249-264
  Perform the following protected operations {
    // Source: vvaharness/pipeline/stages/replay.py:250-250
    End this invocation with fut.result(timeout=seconds).
  }
  // Source: vvaharness/pipeline/stages/replay.py:251-264
  On the first matching source exception TimeoutError as exc, in handler order {
    // Source: vvaharness/pipeline/stages/replay.py:254-255
    if (the source predicate fut.done() is truthy) {
      // Source: vvaharness/pipeline/stages/replay.py:255-255
      End this invocation with fut.result().
    }
    // Source: vvaharness/pipeline/stages/replay.py:259-260
    In source order: Evaluate fut.add_done_callback(_orphan_settled(stage, started)); retain side effects and discard the expression result. Then Evaluate fut.cancel(); retain side effects and discard the expression result.
    // Source: vvaharness/pipeline/stages/replay.py:261-264
    Raise call_timeout_error(stage=stage, route='stage', budget_s=seconds, effort=effort, cause_text=source_template_263_23) with explicit source cause exc.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/replay.py:267-280
// Source signature: deadline_bound(existing: float | None, deadline: int, effort: str | None, *, via: str) -> float | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn deadline_bound(existing, deadline, effort, via) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/replay.py:269-269
  In source order: Retain source documentation literal source_literal_269_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/replay.py:273-274
  if (the source predicate not deadline or deadline <= TIMEOUT_STOP_GRACE_SECONDS is truthy) {
    // Source: vvaharness/pipeline/stages/replay.py:274-274
    End this invocation with existing.
  }
  // Source: vvaharness/pipeline/stages/replay.py:276-279
  In source order: Evaluate once _cli._effective_effort(effort) if via == 'cli' else effort; assign in source target order to tier. Then Evaluate once float(deadline - TIMEOUT_STOP_GRACE_SECONDS); assign in source target order to net. Then Evaluate once effort_scaled_seconds(net, tier, kind=ClockKind.SESSION) or net; assign in source target order to scaled. Then Evaluate once net * (net / scaled); assign in source target order to bound.
  // Source: vvaharness/pipeline/stages/replay.py:280-280
  End this invocation with bound if existing is None or existing > bound else existing.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/replay.py:283-291
// Source signature: replay_prompt(transcript: Transcript, original_prompt: str, *, instruction: str, stage: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn replay_prompt(transcript, original_prompt, instruction, stage) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/replay.py:285-285
  In source order: Retain source documentation literal source_literal_285_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/replay.py:286-289
  if (the source predicate not transcript.captured is truthy) {
    // Source: vvaharness/pipeline/stages/replay.py:287-287
    In source order: Evaluate COUNTERS.bump(source_template_287_22); retain side effects and discard the expression result.
    // Source: vvaharness/pipeline/stages/replay.py:288-289
    End this invocation with instruction + source_literal_288_29 + original_prompt.
  }
  // Source: vvaharness/pipeline/stages/replay.py:290-290
  In source order: Evaluate COUNTERS.bump(source_template_290_18); retain side effects and discard the expression result.
  // Source: vvaharness/pipeline/stages/replay.py:291-291
  End this invocation with instruction + source_literal_291_25 + transcript.render().
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/replay.py:294-296
// Source signature: session_id_for(stage: str, key: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn session_id_for(stage, key) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/replay.py:295-295
  In source order: Retain source documentation literal source_literal_295_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/replay.py:296-296
  End this invocation with source_template_296_11.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/replay.py:300-309
// Source: vvaharness/pipeline/stages/replay.py:299-299
Before creating this callable, evaluate and retain decorators top-to-bottom: contextmanager.
// Source: vvaharness/pipeline/stages/replay.py:300-309
// Source signature: pinned_session(stage: str, key: str) -> Iterator[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn pinned_session(stage, key) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/replay.py:301-305
  In source order: Retain source documentation literal source_literal_301_4; it is not a model call. Then Evaluate once session_id_for(stage, key); assign in source target order to session_id.
  // Source: vvaharness/pipeline/stages/replay.py:306-309
  Perform the following protected operations {
    // Source: vvaharness/pipeline/stages/replay.py:307-307
    In source order: Yield session_id; suspend this generator until resumed.
  }
  On every exit from this protected/handler/normal-completion region {
    // Source: vvaharness/pipeline/stages/replay.py:309-309
    In source order: Evaluate release_pinned_session(session_id); retain side effects and discard the expression result.
  }
  If execution reaches this end, finish with the source implicit None result.
}
At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
// Source: vvaharness/pipeline/stages/replay.py:312-336
// Source signature: resume_or_replay(session_id: str, replay: Callable[[], str], *, model: object, cfg: object, instruction: str, stage: str, tag: str, timeout: int) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn resume_or_replay(session_id, replay, model, cfg, instruction, stage, tag, timeout) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/replay.py:314-319
  In source order: Retain source documentation literal source_literal_314_4; it is not a model call. Then Evaluate COUNTERS.bump(source_template_318_18); retain side effects and discard the expression result. Then Evaluate once time.monotonic(); assign in source target order to started.
  // Source: vvaharness/pipeline/stages/replay.py:320-334
  Perform the following protected operations {
    // Source: vvaharness/pipeline/stages/replay.py:321-322
    In source order: Evaluate once _resume_agentic(session_id, instruction, model=model, cfg=cfg, tag=source_template_321_81, timeout=timeout); assign in source target order to out.
  }
  // Source: vvaharness/pipeline/stages/replay.py:325-326
  On the first matching source exception ModelRefusal, in handler order {
    // Source: vvaharness/pipeline/stages/replay.py:326-326
    Raise the currently handled exception.
  }
  // Source: vvaharness/pipeline/stages/replay.py:329-332
  On the first matching source exception Exception as exc, in handler order {
    // Source: vvaharness/pipeline/stages/replay.py:330-331
    In source order: Evaluate COUNTERS.bump(source_template_330_22); retain side effects and discard the expression result. Then Evaluate log.warning(Event.REPLAY_NO_LIVE_SESSION, stage=stage, tag=tag, detail=str(exc)); retain side effects and discard the expression result.
    // Source: vvaharness/pipeline/stages/replay.py:332-332
    End this invocation with replay().
  }
  On every exit from this protected/handler/normal-completion region {
    // Source: vvaharness/pipeline/stages/replay.py:334-334
    In source order: Evaluate release_pinned_session(session_id); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/replay.py:335-335
  In source order: Evaluate console.write(source_template_335_18); retain side effects and discard the expression result.
  // Source: vvaharness/pipeline/stages/replay.py:336-336
  End this invocation with out.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.backends.llm import cli as _cli` at source line 28: `source_detail/vvaharness/backends/llm/__init__.py.sudo.md`.
- `from vvaharness.backends.llm import cli as _cli` at source line 28: `source_detail/vvaharness/backends/llm/cli/__init__.py.sudo.md`.
- `from vvaharness.backends.llm.deepagents import release_pinned_session` at source line 29: `source_detail/vvaharness/backends/llm/deepagents.py.sudo.md`.
- `from vvaharness.backends.llm.deepagents import resume_agentic as _resume_agentic` at source line 30: `source_detail/vvaharness/backends/llm/deepagents.py.sudo.md`.
- `from vvaharness.backends.llm.models import TIMEOUT_STOP_GRACE_SECONDS, ClockKind, ModelRefusal, call_timeout_error, effort_scaled_seconds` at source line 31: `source_detail/vvaharness/backends/llm/models.py.sudo.md`.
- `from vvaharness.util import console, logs` at source line 38: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import console, logs` at source line 38: `source_detail/vvaharness/util/console.py.sudo.md`.
- `from vvaharness.util import console, logs` at source line 38: `source_detail/vvaharness/util/logs.py.sudo.md`.
- `from vvaharness.util.counters import COUNTERS` at source line 39: `source_detail/vvaharness/util/counters.py.sudo.md`.
- `from vvaharness.util.events import Event` at source line 40: `source_detail/vvaharness/util/events.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../prompt_representation/vvaharness/pipeline/stages/replay.py.sudo.md). Exact strings in the evidence asset support this conversion.
