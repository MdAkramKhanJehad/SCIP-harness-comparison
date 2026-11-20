# vvaharness/backends/llm/deepagents.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/backends/llm/deepagents.py.evidence.json`. SHA-256: `39e32863caf168672ef92be040275dafb66ca31bcf429c51a2c6c0154809c97c`.

```sudo
// Source: vvaharness/backends/llm/deepagents.py:15-34
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import asyncio; preserve alias and import-time effects. Then Resolve source import import atexit; preserve alias and import-time effects. Then Resolve source import import os; preserve alias and import-time effects.
// Source: vvaharness/backends/llm/deepagents.py:35-39
In source order: Resolve source import import re; preserve alias and import-time effects. Then Resolve source import import threading; preserve alias and import-time effects. Then Resolve source import import time; preserve alias and import-time effects. Then Resolve source import from collections.abc import Callable, Coroutine, Sequence; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects.
// Source: vvaharness/backends/llm/deepagents.py:40-42
In source order: Resolve source import from typing import TYPE_CHECKING, Final, TypeVar; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import logs; preserve alias and import-time effects.
// Source: vvaharness/backends/llm/deepagents.py:44-45
if (the source predicate TYPE_CHECKING is truthy) {
  // Source: vvaharness/backends/llm/deepagents.py:45-45
  In source order: Resolve source import from langchain.agents.middleware.types import AgentMiddleware; preserve alias and import-time effects.
}
// Source: vvaharness/backends/llm/deepagents.py:47-75
In source order: Resolve source import from vvaharness.backends.harness import READ_TOOLS, HarnessProcessError, HarnessResult, OneShotOptions, OneShotResult, StreamingOptions, ToolPolicy, get_harness; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.deepagents.limits import MODEL_MAX_OUTPUT_TOKENS; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.models import DEFAULT_GRAPH_NAME, LOGICAL_TO_NATIVE, NATIVE_IMPLIED_READS, NATIVE_SHELL_TOOL, AuthenticationError, OversizePromptError, ProxyError, SessionNotResumableError, ToolBuilder, ToolStateNotRoundTrippedError, TruncatedResponseError; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.provider_routing import credential_env_overrides, routes_to_anthropic; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.transcript import Transcript, open_transcript; preserve alias and import-time effects.
// Source: vvaharness/backends/llm/deepagents.py:76-101
In source order: Resolve source import from vvaharness.backends.llm import cli as _cli; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm import registry; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm.cache import markers_enabled; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm.cli import _truncation_error; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm.models import AGENTIC_MAX_TOKENS, DEEPAGENTS_MAX_PROMPT_TOKENS, RATE_LIMIT_TRANSIENT_RX, RETRYABLE_STATUS, SERVER_ERROR_TRANSIENT_RX, TRUNCATED_REPLIES_COUNTER, ClockKind, ModelRefusal, call_timeout_error, effort_scaled_seconds, jittered_delay, model_refusal, model_refusal_from, note_budget_use, proxy_detail, truncation_retry_max, turn_timeout, wait_overrun; preserve alias and import-time effects.
// Source: vvaharness/backends/llm/deepagents.py:102-113
In source order: Resolve source import from vvaharness.backends.llm.registry import _flatten_blocks, clamp_output_tokens, output_cap_of, resolve; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm.sdk import _AUTH_STATUS_RX; preserve alias and import-time effects. Then Resolve source import from vvaharness.report.redact import redact; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import console; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.config import knob; preserve alias and import-time effects.
// Source: vvaharness/backends/llm/deepagents.py:114-121
In source order: Resolve source import from vvaharness.util.counters import COUNTERS; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.events import Event; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.exceptions import exception_chain; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.response_quality import check_response_quality, output_tokens_for_gate; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.scan_progress import get_active_tracker; preserve alias and import-time effects.
// Source: vvaharness/backends/llm/deepagents.py:122-144
In source order: Resolve source import from vvaharness.util.tokens import TOKENS, TokenUsage, estimate_tokens; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.warn_once import warn_once; preserve alias and import-time effects. Then Evaluate once logs.get_logger(__name__); assign in source target order to log. Then Evaluate once ['agentic', 'build_harness_env', 'dispatch_agentic', 'dispatch_prompt', 'drain_classified', 'drain_streaming', 'droppable_effort', 'map_allowed_tools', 'prompt', 'raise_if_refused', 'route_carries_tools', 'run_oneshot', 'terminal_text', 'think_in_prompt_enabled']; assign in source target order to __all__. Then Evaluate once TypeVar('_T'); assign in source target order to _T.
// Source: vvaharness/backends/llm/deepagents.py:147-154
// Source signature: _permitted_natives(granted: Sequence[str], allow_shell: bool=False) -> frozenset[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _permitted_natives(granted, allow_shell) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/deepagents.py:148-149
  In source order: Retain source documentation literal source_literal_148_4; it is not a model call. Then Evaluate once {LOGICAL_TO_NATIVE[t] for t in granted if t in LOGICAL_TO_NATIVE}; assign in source target order to natives.
  // Source: vvaharness/backends/llm/deepagents.py:150-151
  if (the source predicate natives & {LOGICAL_TO_NATIVE[r] for r in READ_TOOLS} is truthy) {
    // Source: vvaharness/backends/llm/deepagents.py:151-151
    In source order: Apply source augmented assignment natives |= NATIVE_IMPLIED_READS with source evaluation/in-place semantics.
  }
  // Source: vvaharness/backends/llm/deepagents.py:152-153
  if (the source predicate allow_shell is truthy) {
    // Source: vvaharness/backends/llm/deepagents.py:153-153
    In source order: Evaluate natives.add(NATIVE_SHELL_TOOL); retain side effects and discard the expression result.
  }
  // Source: vvaharness/backends/llm/deepagents.py:154-154
  End this invocation with frozenset(natives).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/deepagents.py:157-178
In source order: For _DEFAULT_TOOLS, assign ('Read', 'Glob', 'Grep'); source annotation tuple[str, ...]. Then For _ACCEPTED_UNUSED_KW, assign frozenset({'betas', 'json_schema', 'max_budget_usd', 'output_format', 'permission_mode', 'stream_cb', 'temperature', 'thinking_budget'}); source annotation frozenset[str]. Then For _WARNED_LEGACY_KW, assign set(); source annotation set[str]. Then Evaluate once threading.Lock(); assign in source target order to _LOOP_LOCK. Then For _loop, assign None; source annotation asyncio.AbstractEventLoop | None.
// Source: vvaharness/backends/llm/deepagents.py:179-179
In source order: For _loop_thread, assign None; source annotation threading.Thread | None.
// Source: vvaharness/backends/llm/deepagents.py:182-189
// Source signature: _shutdown_loop() -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _shutdown_loop() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/deepagents.py:183-183
  In source order: Retain source documentation literal source_literal_183_4; it is not a model call.
  // Source: vvaharness/backends/llm/deepagents.py:184-185
  Enter source context managers left-to-right: _LOOP_LOCK {
    // Source: vvaharness/backends/llm/deepagents.py:185-185
    In source order: Evaluate once (_loop, _loop_thread); assign in source target order to (loop, thread).
  }
  Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
  // Source: vvaharness/backends/llm/deepagents.py:186-187
  if (the source predicate loop is None or thread is None is truthy) {
    // Source: vvaharness/backends/llm/deepagents.py:187-187
    End this invocation with None.
  }
  // Source: vvaharness/backends/llm/deepagents.py:188-189
  In source order: Evaluate loop.call_soon_threadsafe(loop.stop); retain side effects and discard the expression result. Then Evaluate thread.join(timeout=5.0); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/deepagents.py:192-205
// Source signature: _harness_loop() -> asyncio.AbstractEventLoop
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _harness_loop() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/deepagents.py:193-194
  In source order: Retain source documentation literal source_literal_193_4; it is not a model call. Then Bind names in module scope: _loop, _loop_thread.
  // Source: vvaharness/backends/llm/deepagents.py:195-205
  Enter source context managers left-to-right: _LOOP_LOCK {
    // Source: vvaharness/backends/llm/deepagents.py:196-197
    if (the source predicate _loop is not None is truthy) {
      // Source: vvaharness/backends/llm/deepagents.py:197-197
      End this invocation with _loop.
    }
    // Source: vvaharness/backends/llm/deepagents.py:198-204
    In source order: Evaluate once asyncio.new_event_loop(); assign in source target order to loop. Then Evaluate once threading.Thread(target=loop.run_forever, name='vvaharness-llm-deepagents', daemon=True); assign in source target order to thread. Then Evaluate thread.start(); retain side effects and discard the expression result. Then Evaluate atexit.register(_shutdown_loop); retain side effects and discard the expression result. Then Evaluate once (loop, thread); assign in source target order to (_loop, _loop_thread).
    // Source: vvaharness/backends/llm/deepagents.py:205-205
    End this invocation with loop.
  }
  Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/deepagents.py:208-239
// Source signature: _run_sync(awaitable: Coroutine[None, None, _T], *, timeout: float | None=None, tag: str | None=None, effort: str | None=None) -> _T
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _run_sync(awaitable, timeout, tag, effort) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/deepagents.py:212-214
  In source order: Retain source documentation literal source_literal_212_4; it is not a model call. Then Evaluate once _harness_loop(); assign in source target order to loop.
  // Source: vvaharness/backends/llm/deepagents.py:215-219
  if (the source predicate threading.current_thread() is _loop_thread is truthy) {
    // Source: vvaharness/backends/llm/deepagents.py:216-216
    In source order: Evaluate awaitable.close(); retain side effects and discard the expression result.
    // Source: vvaharness/backends/llm/deepagents.py:217-219
    Raise RuntimeError('_run_sync called from the harness loop thread — this would deadlock').
  }
  // Source: vvaharness/backends/llm/deepagents.py:220-221
  In source order: Evaluate once asyncio.run_coroutine_threadsafe(awaitable, loop); assign in source target order to future. Then Evaluate once time.monotonic(); assign in source target order to _start.
  // Source: vvaharness/backends/llm/deepagents.py:222-237
  Perform the following protected operations {
    // Source: vvaharness/backends/llm/deepagents.py:223-223
    In source order: Evaluate once future.result(timeout=timeout); assign in source target order to result.
  }
  // Source: vvaharness/backends/llm/deepagents.py:224-237
  On the first matching source exception BaseException as exc, in handler order {
    // Source: vvaharness/backends/llm/deepagents.py:226-226
    In source order: Evaluate once future.cancel(); assign in source target order to cancelled.
    // Source: vvaharness/backends/llm/deepagents.py:232-236
    if (the source predicate isinstance(exc, TimeoutError) and cancelled is truthy) {
      // Source: vvaharness/backends/llm/deepagents.py:233-236
      Raise call_timeout_error(stage=tag or '', route='deepagents', budget_s=timeout, effort=effort, cause_text=source_template_235_27) with explicit source cause exc.
    }
    // Source: vvaharness/backends/llm/deepagents.py:237-237
    Raise the currently handled exception.
  }
  // Source: vvaharness/backends/llm/deepagents.py:238-238
  In source order: Evaluate note_budget_use(time.monotonic() - _start, timeout, effort); retain side effects and discard the expression result.
  // Source: vvaharness/backends/llm/deepagents.py:239-239
  End this invocation with result.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/deepagents.py:242-250
In source order: Evaluate once registry.provider_of; assign in source target order to _provider_of. Then Evaluate once registry.use_responses_api_of; assign in source target order to _use_responses_api_of. Then For _HTTP_UNAUTHORIZED, assign 401; source annotation int. Then For _HTTP_PROXY_AUTH, assign 407; source annotation int. Then Evaluate once re.compile('\\b407\\b'); assign in source target order to _PROXY_407_RX.
// Source: vvaharness/backends/llm/deepagents.py:253-259
In source order: For _NO_USAGE_WARNED_TAGS, assign set(); source annotation set[str]. Then Evaluate once 'deepagents_oversize_prompts'; assign in source target order to _OVERSIZE_PROMPT_COUNTER. Then Evaluate once 'deepagents_tool_state_not_roundtripped'; assign in source target order to _TOOL_STATE_NOT_ROUNDTRIPPED_COUNTER.
// Source: vvaharness/backends/llm/deepagents.py:262-274
// Source signature: _check_prompt_ceiling(text: str, *, tag: str | None) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _check_prompt_ceiling(text, tag) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/deepagents.py:263-264
  In source order: Retain source documentation literal source_literal_263_4; it is not a model call. Then Evaluate once estimate_tokens(text); assign in source target order to estimated.
  // Source: vvaharness/backends/llm/deepagents.py:265-266
  if (the source predicate estimated <= DEEPAGENTS_MAX_PROMPT_TOKENS is truthy) {
    // Source: vvaharness/backends/llm/deepagents.py:266-266
    End this invocation with None.
  }
  // Source: vvaharness/backends/llm/deepagents.py:267-267
  In source order: Evaluate COUNTERS.bump(_OVERSIZE_PROMPT_COUNTER); retain side effects and discard the expression result.
  // Source: vvaharness/backends/llm/deepagents.py:268-274
  Raise OversizePromptError('refused before dispatch; reduce what this call packs (chunk sizing / per-call caps) and re-run', stage=tag or '', estimated_tokens=estimated, limit=DEEPAGENTS_MAX_PROMPT_TOKENS).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/deepagents.py:280-290
// Source signature: _auth_failure(exc: BaseException) -> tuple[int, str] | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _auth_failure(exc) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/deepagents.py:281-281
  In source order: Retain source documentation literal source_literal_281_4; it is not a model call.
  // Source: vvaharness/backends/llm/deepagents.py:283-289
  for each err in exception_chain(exc) {
    // Source: vvaharness/backends/llm/deepagents.py:284-284
    In source order: Evaluate once getattr(err, 'status_code', None); assign in source target order to status.
    // Source: vvaharness/backends/llm/deepagents.py:285-286
    if (the source predicate not isinstance(status, int) is truthy) {
      // Source: vvaharness/backends/llm/deepagents.py:286-286
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/backends/llm/deepagents.py:287-287
    In source order: Evaluate once str(getattr(err, 'message', err)); assign in source target order to body.
    // Source: vvaharness/backends/llm/deepagents.py:288-289
    if (the source predicate status == _HTTP_UNAUTHORIZED or _AUTH_STATUS_RX.search(body) is truthy) {
      // Source: vvaharness/backends/llm/deepagents.py:289-289
      End this invocation with (status, body).
    }
  }
  // Source: vvaharness/backends/llm/deepagents.py:290-290
  End this invocation with None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/deepagents.py:293-298
// Source signature: _proxy_failure(exc: BaseException) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _proxy_failure(exc) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/deepagents.py:294-294
  In source order: Retain source documentation literal source_literal_294_4; it is not a model call.
  // Source: vvaharness/backends/llm/deepagents.py:295-297
  for each err in exception_chain(exc) {
    // Source: vvaharness/backends/llm/deepagents.py:296-297
    if (the source predicate type(err).__name__ == 'APIConnectionError' and (detail := proxy_detail(err)) is truthy) {
      // Source: vvaharness/backends/llm/deepagents.py:297-297
      End this invocation with detail.
    }
  }
  // Source: vvaharness/backends/llm/deepagents.py:298-298
  End this invocation with None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/deepagents.py:301-337
// Source signature: _classify_failure(exc: BaseException, *, model_id: str, tag: str | None) -> AuthenticationError | ProxyError | ToolStateNotRoundTrippedError | ModelRefusal | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _classify_failure(exc, model_id, tag) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/deepagents.py:304-308
  In source order: Retain source documentation literal source_literal_304_4; it is not a model call. Then Evaluate once model_refusal_from(exc, route='deepagents', stage=tag or ''); assign in source target order to refusal.
  // Source: vvaharness/backends/llm/deepagents.py:309-310
  if (the source predicate refusal is not None is truthy) {
    // Source: vvaharness/backends/llm/deepagents.py:310-310
    End this invocation with refusal.
  }
  // Source: vvaharness/backends/llm/deepagents.py:311-312
  In source order: Evaluate once source_template_311_14 + (source_template_311_37 if tag else ''); assign in source target order to context. Then Evaluate once _auth_failure(exc); assign in source target order to auth.
  // Source: vvaharness/backends/llm/deepagents.py:313-319
  if (the source predicate auth is not None is truthy) {
    // Source: vvaharness/backends/llm/deepagents.py:314-314
    In source order: Evaluate once auth; assign in source target order to (status, body).
    // Source: vvaharness/backends/llm/deepagents.py:315-319
    End this invocation with AuthenticationError(source_template_316_12, status_code=status, backend='deepagents').
  }
  // Source: vvaharness/backends/llm/deepagents.py:320-320
  In source order: Evaluate once _proxy_failure(exc); assign in source target order to detail.
  // Source: vvaharness/backends/llm/deepagents.py:321-326
  if (the source predicate detail is not None is truthy) {
    // Source: vvaharness/backends/llm/deepagents.py:322-326
    End this invocation with ProxyError(source_template_323_12, status_code=_HTTP_PROXY_AUTH if _PROXY_407_RX.search(detail) else None, backend='deepagents').
  }
  // Source: vvaharness/backends/llm/deepagents.py:327-329
  In source order: Resolve source import from vvaharness.backends.harness.deepagents.client import _is_missing_thought_signature; preserve alias and import-time effects.
  // Source: vvaharness/backends/llm/deepagents.py:330-336
  if (the source predicate _is_missing_thought_signature(exc) is truthy) {
    // Source: vvaharness/backends/llm/deepagents.py:331-331
    In source order: Evaluate COUNTERS.bump(_TOOL_STATE_NOT_ROUNDTRIPPED_COUNTER); retain side effects and discard the expression result.
    // Source: vvaharness/backends/llm/deepagents.py:332-336
    End this invocation with ToolStateNotRoundTrippedError(source_template_333_12, stage=tag or '', model_id=model_id).
  }
  // Source: vvaharness/backends/llm/deepagents.py:337-337
  End this invocation with None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/deepagents.py:341-348
In source order: For _UNHEALABLE_STATUS, assign frozenset({_HTTP_UNAUTHORIZED, 403}); source annotation Final[frozenset[int]]. Then For _TRANSIENT_ATTEMPTS, assign 3; source annotation Final. Then For _TRANSIENT_WAIT_SECONDS, assign 60; source annotation Final. Then For _RETRY_AFTER_MAX_SECONDS, assign 300.0; source annotation Final.
// Source: vvaharness/backends/llm/deepagents.py:351-365
// Source signature: _transient_failure(exc: BaseException) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _transient_failure(exc) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/deepagents.py:352-354
  In source order: Retain source documentation literal source_literal_352_4; it is not a model call. Then Evaluate once False; assign in source target order to transient.
  // Source: vvaharness/backends/llm/deepagents.py:355-364
  for each err in exception_chain(exc) {
    // Source: vvaharness/backends/llm/deepagents.py:356-356
    In source order: Evaluate once getattr(err, 'status_code', None); assign in source target order to status.
    // Source: vvaharness/backends/llm/deepagents.py:357-358
    if (the source predicate isinstance(status, int) and status in _UNHEALABLE_STATUS is truthy) {
      // Source: vvaharness/backends/llm/deepagents.py:358-358
      End this invocation with False.
    }
    // Source: vvaharness/backends/llm/deepagents.py:359-364
    In source order: Evaluate once str(getattr(err, 'message', None) or err); assign in source target order to body. Then Evaluate once transient or bool(isinstance(status, int) and status in RETRYABLE_STATUS or RATE_LIMIT_TRANSIENT_RX.search(body) or SERVER_ERROR_TRANSIENT_RX.search(body)); assign in source target order to transient.
  }
  // Source: vvaharness/backends/llm/deepagents.py:365-365
  End this invocation with transient.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/deepagents.py:368-381
// Source signature: _retry_after_seconds(exc: BaseException) -> float | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _retry_after_seconds(exc) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/deepagents.py:369-369
  In source order: Retain source documentation literal source_literal_369_4; it is not a model call.
  // Source: vvaharness/backends/llm/deepagents.py:370-380
  for each err in exception_chain(exc) {
    // Source: vvaharness/backends/llm/deepagents.py:371-372
    In source order: Evaluate once getattr(getattr(err, 'response', None), 'headers', None); assign in source target order to headers. Then Evaluate once headers.get('retry-after') if hasattr(headers, 'get') else None; assign in source target order to raw.
    // Source: vvaharness/backends/llm/deepagents.py:373-374
    if (the source predicate raw is None is truthy) {
      // Source: vvaharness/backends/llm/deepagents.py:374-374
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/backends/llm/deepagents.py:375-378
    Perform the following protected operations {
      // Source: vvaharness/backends/llm/deepagents.py:376-376
      In source order: Evaluate once float(raw); assign in source target order to seconds.
    }
    // Source: vvaharness/backends/llm/deepagents.py:377-378
    On the first matching source exception (TypeError, ValueError), in handler order {
      // Source: vvaharness/backends/llm/deepagents.py:378-378
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/backends/llm/deepagents.py:379-380
    if (the source predicate seconds > 0 is truthy) {
      // Source: vvaharness/backends/llm/deepagents.py:380-380
      End this invocation with min(seconds, _RETRY_AFTER_MAX_SECONDS).
    }
  }
  // Source: vvaharness/backends/llm/deepagents.py:381-381
  End this invocation with None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/deepagents.py:384-388
// Source signature: _refusal_or_raise(mapped: Exception, exc: BaseException) -> ModelRefusal
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _refusal_or_raise(mapped, exc) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/deepagents.py:385-385
  In source order: Retain source documentation literal source_literal_385_4; it is not a model call.
  // Source: vvaharness/backends/llm/deepagents.py:386-387
  if (the source predicate not isinstance(mapped, ModelRefusal) is truthy) {
    // Source: vvaharness/backends/llm/deepagents.py:387-387
    Raise mapped with explicit source cause exc.
  }
  // Source: vvaharness/backends/llm/deepagents.py:388-388
  End this invocation with mapped.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/deepagents.py:391-400
// Source signature: _transient_wait(exc: Exception, *, session_t0: float, budget: float | None, tag: str | None) -> float
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _transient_wait(exc, session_t0, budget, tag) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/deepagents.py:393-396
  In source order: Retain source documentation literal source_literal_393_4; it is not a model call. Then Evaluate once _retry_after_seconds(exc); assign in source target order to retry_after. Then Evaluate once retry_after if retry_after is not None else jittered_delay(_TRANSIENT_WAIT_SECONDS); assign in source target order to wait.
  // Source: vvaharness/backends/llm/deepagents.py:397-399
  if (the source predicate (overrun := wait_overrun(wait, session_t0, budget, stage=tag or '', route='deepagents', effort=None)) is truthy) {
    // Source: vvaharness/backends/llm/deepagents.py:399-399
    Raise overrun with explicit source cause exc.
  }
  // Source: vvaharness/backends/llm/deepagents.py:400-400
  End this invocation with wait.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/deepagents.py:403-431
// Source signature: _call_classified(call: Callable[[float | None], _T], *, model_id: str, tag: str | None, budget: float | None=None) -> _T
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _call_classified(call, model_id, tag, budget) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/deepagents.py:405-409
  In source order: Retain source documentation literal source_literal_405_4; it is not a model call. Then Evaluate once 0; assign in source target order to attempt. Then Evaluate once time.monotonic(); assign in source target order to session_t0. Then Evaluate once budget; assign in source target order to remaining.
  // Source: vvaharness/backends/llm/deepagents.py:410-428
  while (the source predicate True is truthy) {
    // Source: vvaharness/backends/llm/deepagents.py:411-411
    In source order: Apply source augmented assignment attempt += 1 with source evaluation/in-place semantics.
    // Source: vvaharness/backends/llm/deepagents.py:412-428
    Perform the following protected operations {
      // Source: vvaharness/backends/llm/deepagents.py:413-413
      End this invocation with call(remaining).
    }
    // Source: vvaharness/backends/llm/deepagents.py:414-428
    On the first matching source exception Exception as exc, in handler order {
      // Source: vvaharness/backends/llm/deepagents.py:415-415
      In source order: Evaluate once _classify_failure(exc, model_id=model_id, tag=tag); assign in source target order to mapped.
      // Source: vvaharness/backends/llm/deepagents.py:416-418
      if (the source predicate mapped is not None is truthy) {
        // Source: vvaharness/backends/llm/deepagents.py:417-417
        In source order: Evaluate once _refusal_or_raise(mapped, exc); assign in source target order to refusal.
        // Source: vvaharness/backends/llm/deepagents.py:418-418
        Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
      }
      // Source: vvaharness/backends/llm/deepagents.py:419-420
      if (the source predicate attempt >= _TRANSIENT_ATTEMPTS or not _transient_failure(exc) is truthy) {
        // Source: vvaharness/backends/llm/deepagents.py:420-420
        Raise the currently handled exception.
      }
      // Source: vvaharness/backends/llm/deepagents.py:421-428
      In source order: Evaluate once _transient_wait(exc, session_t0=session_t0, budget=budget, tag=tag); assign in source target order to wait. Then Evaluate console.write(source_template_423_16); retain side effects and discard the expression result. Then Evaluate time.sleep(wait); retain side effects and discard the expression result. Then Evaluate once None if budget is None else turn_timeout(session_t0, budget, budget); assign in source target order to remaining.
    }
  }
  // Source: vvaharness/backends/llm/deepagents.py:431-431
  Raise refusal.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/deepagents.py:434-446
// Source signature: _warn_no_usage(usage: object, *, model_id: str, tag: str | None) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _warn_no_usage(usage, model_id, tag) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/deepagents.py:435-435
  In source order: Retain source documentation literal source_literal_435_4; it is not a model call.
  // Source: vvaharness/backends/llm/deepagents.py:436-437
  if (the source predicate usage is not None is truthy) {
    // Source: vvaharness/backends/llm/deepagents.py:437-437
    End this invocation with None.
  }
  // Source: vvaharness/backends/llm/deepagents.py:438-446
  In source order: Evaluate once tag or ''; assign in source target order to tag_text. Then Evaluate once tag_text.split(maxsplit=1)[0] if tag_text.strip() else ''; assign in source target order to stage_key. Then Evaluate warn_once(_NO_USAGE_WARNED_TAGS, stage_key, source_template_443_8); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/deepagents.py:450-450
In source order: For _WARNED_DROPPED_KNOBS, assign set(); source annotation set[str].
// Source: vvaharness/backends/llm/deepagents.py:453-464
// Source signature: _warn_dropped_model_knobs(model_id: str, extras: object) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _warn_dropped_model_knobs(model_id, extras) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/deepagents.py:454-454
  In source order: Retain source documentation literal source_literal_454_4; it is not a model call.
  // Source: vvaharness/backends/llm/deepagents.py:455-456
  if (the source predicate not isinstance(extras, dict) is truthy) {
    // Source: vvaharness/backends/llm/deepagents.py:456-456
    End this invocation with None.
  }
  // Source: vvaharness/backends/llm/deepagents.py:457-464
  for each name in sorted(extras) {
    // Source: vvaharness/backends/llm/deepagents.py:458-464
    In source order: Evaluate warn_once(_WARNED_DROPPED_KNOBS, source_template_460_12, source_template_461_12); retain side effects and discard the expression result.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/deepagents.py:467-478
// Source signature: _warn_max_budget_unenforced(max_budget_usd: float | None) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _warn_max_budget_unenforced(max_budget_usd) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/deepagents.py:468-468
  In source order: Retain source documentation literal source_literal_468_4; it is not a model call.
  // Source: vvaharness/backends/llm/deepagents.py:470-471
  if (the source predicate max_budget_usd is None is truthy) {
    // Source: vvaharness/backends/llm/deepagents.py:471-471
    End this invocation with None.
  }
  // Source: vvaharness/backends/llm/deepagents.py:472-478
  In source order: Evaluate warn_once(_WARNED_DROPPED_KNOBS, 'deepagents:max_budget_usd', source_template_475_8); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/deepagents.py:481-483
// Source signature: _output_tokens(usage: TokenUsage | None) -> int | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _output_tokens(usage) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/deepagents.py:482-482
  In source order: Retain source documentation literal source_literal_482_4; it is not a model call.
  // Source: vvaharness/backends/llm/deepagents.py:483-483
  End this invocation with output_tokens_for_gate(usage).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/deepagents.py:486-489
// Source signature: _usage_of(result: object) -> TokenUsage | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _usage_of(result) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/deepagents.py:487-488
  In source order: Retain source documentation literal source_literal_487_4; it is not a model call. Then Evaluate once getattr(result, 'usage', None); assign in source target order to usage.
  // Source: vvaharness/backends/llm/deepagents.py:489-489
  End this invocation with usage if isinstance(usage, dict) else None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/deepagents.py:492-514
// Source signature: build_harness_env(model_id: str, provider: str | None, *, sdk_cfg: object, openai_cfg: object, cfg_dir: str | Path | None=None) -> dict[str, str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn build_harness_env(model_id, provider, sdk_cfg, openai_cfg, cfg_dir) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/deepagents.py:500-504
  In source order: Retain source documentation literal source_literal_500_4; it is not a model call. Then Resolve source import from vvaharness.backends.harness.deepagents.options.model_building import tls_carriers_for; preserve alias and import-time effects.
  // Source: vvaharness/backends/llm/deepagents.py:506-514
  End this invocation with {**os.environ, **credential_env_overrides(model_id, provider, sdk_cfg=sdk_cfg, openai_cfg=openai_cfg), **tls_carriers_for(model_id, provider, sdk_cfg=sdk_cfg, openai_cfg=openai_cfg, cfg_dir=cfg_dir)}.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/deepagents.py:517-527
// Source signature: map_allowed_tools(allowed_tools: Sequence[str] | None) -> tuple[tuple[str, ...], tuple[str, ...]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn map_allowed_tools(allowed_tools) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/deepagents.py:520-520
  In source order: Retain source documentation literal source_literal_520_4; it is not a model call.
  // Source: vvaharness/backends/llm/deepagents.py:522-523
  if (the source predicate allowed_tools is None is truthy) {
    // Source: vvaharness/backends/llm/deepagents.py:523-523
    End this invocation with (_DEFAULT_TOOLS, ()).
  }
  // Source: vvaharness/backends/llm/deepagents.py:524-526
  In source order: Evaluate once tuple(dict.fromkeys(allowed_tools)); assign in source target order to names. Then Evaluate once tuple((n for n in names if n in READ_TOOLS)); assign in source target order to granted. Then Evaluate once tuple((n for n in names if n not in READ_TOOLS)); assign in source target order to stripped.
  // Source: vvaharness/backends/llm/deepagents.py:527-527
  End this invocation with (granted, stripped).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/deepagents.py:530-540
// Source signature: _consume(user_prompt: str, options: StreamingOptions, transcript: Transcript | None, seen: list[HarnessResult]) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _consume(user_prompt, options, transcript, seen) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  This callable produces a coroutine or async generator; await/suspension positions remain in source expressions.
  // Source: vvaharness/backends/llm/deepagents.py:534-534
  In source order: Retain source documentation literal source_literal_534_4; it is not a model call.
  // Source: vvaharness/backends/llm/deepagents.py:536-540
  Obtain/advance the following source async iterator by awaiting, without inventing parallel dispatch.
  for each message in get_harness('deepagents').run_streaming(user_prompt, options) {
    // Source: vvaharness/backends/llm/deepagents.py:537-538
    if (the source predicate transcript is not None is truthy) {
      // Source: vvaharness/backends/llm/deepagents.py:538-538
      In source order: Evaluate transcript.add(message); retain side effects and discard the expression result.
    }
    // Source: vvaharness/backends/llm/deepagents.py:539-540
    if (the source predicate isinstance(message, HarnessResult) is truthy) {
      // Source: vvaharness/backends/llm/deepagents.py:540-540
      In source order: Evaluate seen.append(message); retain side effects and discard the expression result.
    }
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/deepagents.py:544-545
In source order: For _PINNED, assign {}; source annotation dict[str, StreamingOptions]. Then Evaluate once threading.Lock(); assign in source target order to _PINNED_LOCK.
// Source: vvaharness/backends/llm/deepagents.py:548-552
// Source signature: _pin_session(options: StreamingOptions) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _pin_session(options) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/deepagents.py:549-549
  In source order: Retain source documentation literal source_literal_549_4; it is not a model call.
  // Source: vvaharness/backends/llm/deepagents.py:550-552
  if (the source predicate options.session_id is truthy) {
    // Source: vvaharness/backends/llm/deepagents.py:551-552
    Enter source context managers left-to-right: _PINNED_LOCK {
      // Source: vvaharness/backends/llm/deepagents.py:552-552
      In source order: Evaluate once options; assign in source target order to _PINNED[options.session_id].
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/deepagents.py:555-558
// Source signature: _streaming_options_of(session_id: str) -> StreamingOptions | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _streaming_options_of(session_id) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/deepagents.py:556-556
  In source order: Retain source documentation literal source_literal_556_4; it is not a model call.
  // Source: vvaharness/backends/llm/deepagents.py:557-558
  Enter source context managers left-to-right: _PINNED_LOCK {
    // Source: vvaharness/backends/llm/deepagents.py:558-558
    End this invocation with _PINNED.get(session_id).
  }
  Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/deepagents.py:561-569
// Source signature: release_pinned_session(session_id: str) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn release_pinned_session(session_id) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/deepagents.py:562-564
  In source order: Retain source documentation literal source_literal_562_4; it is not a model call. Then Resolve source import from vvaharness.backends.harness.deepagents.options import release_session; preserve alias and import-time effects.
  // Source: vvaharness/backends/llm/deepagents.py:566-567
  Enter source context managers left-to-right: _PINNED_LOCK {
    // Source: vvaharness/backends/llm/deepagents.py:567-567
    In source order: Evaluate _PINNED.pop(session_id, None); retain side effects and discard the expression result.
  }
  Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
  // Source: vvaharness/backends/llm/deepagents.py:568-569
  In source order: Evaluate release_session(session_id); retain side effects and discard the expression result. Then Evaluate _cli.session.release_pinned_session(session_id); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/deepagents.py:572-581
// Source signature: _consume_resume(instruction: str, options: StreamingOptions, transcript: Transcript | None, seen: list[HarnessResult]) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _consume_resume(instruction, options, transcript, seen) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  This callable produces a coroutine or async generator; await/suspension positions remain in source expressions.
  // Source: vvaharness/backends/llm/deepagents.py:576-576
  In source order: Retain source documentation literal source_literal_576_4; it is not a model call.
  // Source: vvaharness/backends/llm/deepagents.py:577-581
  Obtain/advance the following source async iterator by awaiting, without inventing parallel dispatch.
  for each message in get_harness('deepagents').resume_streaming(instruction, options) {
    // Source: vvaharness/backends/llm/deepagents.py:578-579
    if (the source predicate transcript is not None is truthy) {
      // Source: vvaharness/backends/llm/deepagents.py:579-579
      In source order: Evaluate transcript.add(message); retain side effects and discard the expression result.
    }
    // Source: vvaharness/backends/llm/deepagents.py:580-581
    if (the source predicate isinstance(message, HarnessResult) is truthy) {
      // Source: vvaharness/backends/llm/deepagents.py:581-581
      In source order: Evaluate seen.append(message); retain side effects and discard the expression result.
    }
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/deepagents.py:584-596
// Source signature: _drain_resume(instruction: str, options: StreamingOptions, *, tag: str | None=None) -> HarnessResult | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _drain_resume(instruction, options, tag) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  This callable produces a coroutine or async generator; await/suspension positions remain in source expressions.
  // Source: vvaharness/backends/llm/deepagents.py:587-590
  In source order: Retain source documentation literal source_literal_587_4; it is not a model call. Then For seen, assign []; source annotation list[HarnessResult]. Then Evaluate once open_transcript(tag=tag, model=options.model, graph_name=options.graph_name); assign in source target order to transcript.
  // Source: vvaharness/backends/llm/deepagents.py:591-595
  Perform the following protected operations {
    // Source: vvaharness/backends/llm/deepagents.py:592-592
    In source order: Evaluate await _consume_resume(instruction, options, transcript, seen); retain side effects and discard the expression result.
  }
  On every exit from this protected/handler/normal-completion region {
    // Source: vvaharness/backends/llm/deepagents.py:594-595
    if (the source predicate transcript is not None is truthy) {
      // Source: vvaharness/backends/llm/deepagents.py:595-595
      In source order: Evaluate transcript.close(); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/backends/llm/deepagents.py:596-596
  End this invocation with seen[-1] if seen else None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/deepagents.py:599-606
// Source signature: drain_resume(instruction: str, options: StreamingOptions, *, tag: str | None=None, timeout: float | None=None) -> HarnessResult
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn drain_resume(instruction, options, tag, timeout) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/deepagents.py:601-603
  In source order: Retain source documentation literal source_literal_601_4; it is not a model call. Then Evaluate once _run_sync(_drain_resume(instruction, options, tag=tag), timeout=timeout, tag=tag, effort=options.effort); assign in source target order to terminal.
  // Source: vvaharness/backends/llm/deepagents.py:604-605
  if (the source predicate terminal is None is truthy) {
    // Source: vvaharness/backends/llm/deepagents.py:605-605
    Raise RuntimeError('DeepAgents resume ended without a terminal result').
  }
  // Source: vvaharness/backends/llm/deepagents.py:606-606
  End this invocation with terminal.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/deepagents.py:609-629
// Source signature: _drain(user_prompt: str, options: StreamingOptions, *, tag: str | None=None) -> tuple[HarnessResult | None, HarnessProcessError | None]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _drain(user_prompt, options, tag) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  This callable produces a coroutine or async generator; await/suspension positions remain in source expressions.
  // Source: vvaharness/backends/llm/deepagents.py:612-616
  In source order: Retain source documentation literal source_literal_612_4; it is not a model call. Then For seen, assign []; source annotation list[HarnessResult]. Then Evaluate once open_transcript(tag=tag, model=options.model, graph_name=options.graph_name); assign in source target order to transcript.
  // Source: vvaharness/backends/llm/deepagents.py:617-628
  Perform the following protected operations {
    // Source: vvaharness/backends/llm/deepagents.py:618-618
    In source order: Evaluate await _consume(user_prompt, options, transcript, seen); retain side effects and discard the expression result.
  }
  // Source: vvaharness/backends/llm/deepagents.py:619-624
  On the first matching source exception HarnessProcessError as exc, in handler order {
    // Source: vvaharness/backends/llm/deepagents.py:621-623
    if (the source predicate not (getattr(exc, 'recursion_limited', False) or 'GraphRecursionError' in str(exc)) or not seen is truthy) {
      // Source: vvaharness/backends/llm/deepagents.py:623-623
      Raise the currently handled exception.
    }
    // Source: vvaharness/backends/llm/deepagents.py:624-624
    End this invocation with (seen[-1], exc).
  }
  On every exit from this protected/handler/normal-completion region {
    // Source: vvaharness/backends/llm/deepagents.py:627-628
    if (the source predicate transcript is not None is truthy) {
      // Source: vvaharness/backends/llm/deepagents.py:628-628
      In source order: Evaluate transcript.close(); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/backends/llm/deepagents.py:629-629
  End this invocation with (seen[-1] if seen else None, None).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/deepagents.py:632-650
// Source signature: drain_streaming(user_prompt: str, options: StreamingOptions, *, tag: str | None=None, timeout: float | None=None) -> HarnessResult
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn drain_streaming(user_prompt, options, tag, timeout) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/deepagents.py:635-639
  In source order: Retain source documentation literal source_literal_635_4; it is not a model call. Then Evaluate once _run_sync(_drain(user_prompt, options, tag=tag), timeout=timeout, tag=tag, effort=options.effort); assign in source target order to (terminal, recursion_error).
  // Source: vvaharness/backends/llm/deepagents.py:640-641
  if (the source predicate terminal is None is truthy) {
    // Source: vvaharness/backends/llm/deepagents.py:641-641
    Raise RuntimeError('DeepAgents session ended without a terminal result').
  }
  // Source: vvaharness/backends/llm/deepagents.py:642-645
  if (the source predicate terminal.is_error and recursion_error is None is truthy) {
    // Source: vvaharness/backends/llm/deepagents.py:643-645
    Raise RuntimeError(source_template_644_12).
  }
  // Source: vvaharness/backends/llm/deepagents.py:646-649
  if (the source predicate recursion_error is not None is truthy) {
    // Source: vvaharness/backends/llm/deepagents.py:648-649
    In source order: Evaluate log.warning(Event.AGENTIC_TURN_LIMIT, model=options.model, tag=tag); retain side effects and discard the expression result. Then Evaluate COUNTERS.bump('llm_turn_cap_exhausted'); retain side effects and discard the expression result.
  }
  // Source: vvaharness/backends/llm/deepagents.py:650-650
  End this invocation with terminal.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/deepagents.py:653-661
// Source signature: run_oneshot(user_prompt: str, options: OneShotOptions, *, tag: str | None=None, timeout: float | None=None) -> OneShotResult
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn run_oneshot(user_prompt, options, tag, timeout) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/deepagents.py:657-657
  In source order: Retain source documentation literal source_literal_657_4; it is not a model call.
  // Source: vvaharness/backends/llm/deepagents.py:658-661
  End this invocation with _run_sync(get_harness('deepagents').run_oneshot(user_prompt, options), timeout=timeout, tag=tag, effort=options.effort).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/deepagents.py:664-684
// Source signature: _run_oneshot_with_truncation_retry(user_prompt: str, options: OneShotOptions, *, model_id: str, tag: str | None, timeout: float | None=None) -> OneShotResult
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _run_oneshot_with_truncation_retry(user_prompt, options, model_id, tag, timeout) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/deepagents.py:668-675
  In source order: Retain source documentation literal source_literal_668_4; it is not a model call. Then Evaluate once options.max_output_tokens or MODEL_MAX_OUTPUT_TOKENS; assign in source target order to requested. Then Evaluate once options.output_cap if options.output_cap is not None else MODEL_MAX_OUTPUT_TOKENS; assign in source target order to cap_ceiling. Then Evaluate once truncation_retry_max(requested, cap=cap_ceiling); assign in source target order to retry_at. Then Evaluate once _call_classified(lambda remaining: run_oneshot(user_prompt, options, tag=tag, timeout=remaining), model_id=model_id, tag=tag, budget=timeout); assign in source target order to result.
  // Source: vvaharness/backends/llm/deepagents.py:676-676
  In source order: Evaluate raise_if_refused(result, tag=tag); retain side effects and discard the expression result.
  // Source: vvaharness/backends/llm/deepagents.py:678-679
  if (the source predicate not getattr(result, 'truncated', False) is truthy) {
    // Source: vvaharness/backends/llm/deepagents.py:679-679
    End this invocation with result.
  }
  // Source: vvaharness/backends/llm/deepagents.py:681-684
  Raise _truncation_error(requested=requested, retried=retry_at or 0, tag=tag, retry_at=retry_at, produced=_output_tokens(result.usage)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/deepagents.py:687-692
// Source signature: raise_if_refused(result: object, *, tag: str | None) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn raise_if_refused(result, tag) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/deepagents.py:688-688
  In source order: Retain source documentation literal source_literal_688_4; it is not a model call.
  // Source: vvaharness/backends/llm/deepagents.py:690-692
  if (the source predicate getattr(result, 'refused', False) is truthy) {
    // Source: vvaharness/backends/llm/deepagents.py:691-692
    Raise model_refusal(route='deepagents', stage=tag or '', category=getattr(result, 'refusal_category', None)).
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/deepagents.py:695-703
// Source signature: drain_classified(user_prompt: str, options: StreamingOptions, *, model_id: str, tag: str | None, timeout: float | None=None) -> HarnessResult
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn drain_classified(user_prompt, options, model_id, tag, timeout) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/deepagents.py:697-702
  In source order: Retain source documentation literal source_literal_697_4; it is not a model call. Then Evaluate once _call_classified(lambda remaining: drain_streaming(user_prompt, options, tag=tag, timeout=remaining), model_id=model_id, tag=tag, budget=timeout); assign in source target order to terminal. Then Evaluate raise_if_refused(terminal, tag=tag); retain side effects and discard the expression result.
  // Source: vvaharness/backends/llm/deepagents.py:703-703
  End this invocation with terminal.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/deepagents.py:706-708
// Source signature: terminal_text(result: HarnessResult) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn terminal_text(result) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/deepagents.py:707-707
  In source order: Retain source documentation literal source_literal_707_4; it is not a model call.
  // Source: vvaharness/backends/llm/deepagents.py:708-708
  End this invocation with result.result_text or ''.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/deepagents.py:711-821
// Source signature: agentic(user_prompt: str, *, model: object, system_prompt: str | None=None, allowed_tools: Sequence[str] | None=None, cwd: str, max_budget_usd: float | None=None, permission_mode: str='auto', max_turns: int | None=None, tag: str | None=None, graph_name: str=DEFAULT_GRAPH_NAME, sdk_cfg: object=None, openai_cfg: object=None, cfg_dir: str | None=None, tool_builder: ToolBuilder | None=None, fact_tools: Sequence[str]=(), response_model: type | None=None, parent_middleware: tuple[AgentMiddleware, ...]=(), skill_root: Path | None=None, cache_prefix: str | None=None, max_output_tokens: int | None=None, effort: str | None=None, agents: dict[str, object] | None=None, allow_shell: bool=False, timeout: float | None=None, session_id: str='', think_in_prompt: bool=False) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn agentic(user_prompt, model, system_prompt, allowed_tools, cwd, max_budget_usd, permission_mode, max_turns, tag, graph_name, sdk_cfg, openai_cfg, cfg_dir, tool_builder, fact_tools, response_model, parent_middleware, skill_root, cache_prefix, max_output_tokens, effort, agents, allow_shell, timeout, session_id, think_in_prompt) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/deepagents.py:740-745
  In source order: Retain source documentation literal source_literal_740_4; it is not a model call. Then Evaluate once resolve(model); assign in source target order to (model_id, _via, extras). Then Evaluate _warn_dropped_model_knobs(model_id, extras); retain side effects and discard the expression result. Then Evaluate _warn_max_budget_unenforced(max_budget_usd); retain side effects and discard the expression result. Then Evaluate once _provider_of(model); assign in source target order to provider.
  // Source: vvaharness/backends/llm/deepagents.py:746-747
  In source order: Evaluate once output_cap_of(model); assign in source target order to output_cap. Then Evaluate once max_output_tokens or AGENTIC_MAX_TOKENS; assign in source target order to effective_max_output_tokens.
  // Source: vvaharness/backends/llm/deepagents.py:748-750
  if (the source predicate output_cap is not None is truthy) {
    // Source: vvaharness/backends/llm/deepagents.py:749-750
    In source order: Evaluate once clamp_output_tokens(effective_max_output_tokens, model, tag=tag); assign in source target order to effective_max_output_tokens.
  }
  // Source: vvaharness/backends/llm/deepagents.py:751-751
  In source order: Evaluate once cache_prefix or ''; assign in source target order to prefix.
  // Source: vvaharness/backends/llm/deepagents.py:752-755
  if (the source predicate prefix and (not (routes_to_anthropic(model_id, provider) and markers_on(sdk_cfg))) is truthy) {
    // Source: vvaharness/backends/llm/deepagents.py:754-755
    In source order: Evaluate once prefix + user_prompt; assign in source target order to user_prompt. Then Evaluate once ''; assign in source target order to prefix.
  }
  // Source: vvaharness/backends/llm/deepagents.py:756-757
  In source order: Evaluate _check_prompt_ceiling(prefix + user_prompt, tag=tag); retain side effects and discard the expression result. Then Evaluate once map_allowed_tools(allowed_tools); assign in source target order to (granted, stripped).
  // Source: vvaharness/backends/llm/deepagents.py:758-759
  if (the source predicate stripped is truthy) {
    // Source: vvaharness/backends/llm/deepagents.py:759-759
    In source order: Evaluate log.warning(Event.TOOLS_UNSUPPORTED_ON_ROUTE, stripped=sorted(stripped)); retain side effects and discard the expression result.
  }
  // Source: vvaharness/backends/llm/deepagents.py:761-802
  In source order: Evaluate once StreamingOptions(model=model_id, model_provider=provider, use_responses_api=_use_responses_api_of(model), cwd=Path(cwd), env=build_harness_env(model_id, provider, sdk_cfg=sdk_cfg, openai_cfg=openai_cfg, cfg_dir=cfg_dir), max_turns=max_turns, max_budget_usd=max_budget_usd, system_prompt=system_prompt, tool_policy=ToolPolicy(allowed_tools=granted, disallowed_tools=stripped), graph_name=graph_name, skill_root=skill_root, effort=effort, agents=agents or {}, permitted_tool_calls=_permitted_natives(granted, allow_shell), allow_shell=allow_shell, max_output_tokens=effective_max_output_tokens, output_cap=output_cap, cache_markers=markers_on(sdk_cfg), cache_prefix=prefix or None, tool_builder=tool_builder, fact_tools=tuple(fact_tools), response_model=response_model, parent_middleware=parent_middleware, session_id=session_id, think_in_prompt=think_in_prompt); assign in source target order to options. Then Evaluate _pin_session(options); retain side effects and discard the expression result. Then Evaluate once effort_scaled_seconds(timeout, effort, kind=ClockKind.SESSION); assign in source target order to session_timeout. Then Evaluate once drain_classified(user_prompt, options, model_id=model_id, tag=tag, timeout=session_timeout); assign in source target order to terminal. Then Evaluate once _usage_of(terminal); assign in source target order to usage.
  // Source: vvaharness/backends/llm/deepagents.py:803-815
  if (the source predicate getattr(terminal, 'truncated', False) is truthy) {
    // Source: vvaharness/backends/llm/deepagents.py:805-807
    In source order: Evaluate COUNTERS.bump(TRUNCATED_REPLIES_COUNTER); retain side effects and discard the expression result. Then Evaluate once output_cap if output_cap is not None else MODEL_MAX_OUTPUT_TOKENS; assign in source target order to cap_ceiling.
    // Source: vvaharness/backends/llm/deepagents.py:808-815
    Raise TruncatedResponseError(source_literal_809_12, stage=tag or '', requested=effective_max_output_tokens, retried=truncation_retry_max(effective_max_output_tokens, cap=cap_ceiling) or 0).
  }
  // Source: vvaharness/backends/llm/deepagents.py:816-820
  In source order: Evaluate _warn_no_usage(usage, model_id=model_id, tag=tag); retain side effects and discard the expression result. Then Evaluate once terminal_text(terminal); assign in source target order to text. Then Evaluate check_response_quality(text.strip(), stage=tag or '', output_tokens=_output_tokens(usage)); retain side effects and discard the expression result.
  // Source: vvaharness/backends/llm/deepagents.py:821-821
  End this invocation with text.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/deepagents.py:824-827
// Source signature: markers_on(sdk_cfg: object) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn markers_on(sdk_cfg) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/deepagents.py:825-826
  In source order: Retain source documentation literal source_literal_825_4; it is not a model call. Then Evaluate once getattr(sdk_cfg, 'cache_markers', None); assign in source target order to value.
  // Source: vvaharness/backends/llm/deepagents.py:827-827
  End this invocation with markers_enabled({} if value is None else {'cache_markers': value}).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/deepagents.py:831-831
In source order: Evaluate once markers_on; assign in source target order to _markers_on.
// Source: vvaharness/backends/llm/deepagents.py:834-917
// Source signature: prompt(user_prompt: str | list[dict[str, object]], *, model: object, system_prompt: str | None=None, max_tokens: int | None=None, cwd: str, tag: str | None=None, graph_name: str=DEFAULT_GRAPH_NAME, sdk_cfg: object=None, openai_cfg: object=None, cfg_dir: str | None=None, cache_prefix: str | None=None, response_model: type | None=None, tool_builder: ToolBuilder | None=None, fact_tools: Sequence[str]=(), parent_middleware: tuple[AgentMiddleware, ...]=(), max_turns: int | None=None, effort: str | None=None, timeout: float | None=None, think_in_prompt: bool=False) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn prompt(user_prompt, model, system_prompt, max_tokens, cwd, tag, graph_name, sdk_cfg, openai_cfg, cfg_dir, cache_prefix, response_model, tool_builder, fact_tools, parent_middleware, max_turns, effort, timeout, think_in_prompt) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/deepagents.py:856-859
  In source order: Retain source documentation literal source_literal_856_4; it is not a model call. Then Evaluate once resolve(model); assign in source target order to (model_id, _via, extras). Then Evaluate _warn_dropped_model_knobs(model_id, extras); retain side effects and discard the expression result.
  // Source: vvaharness/backends/llm/deepagents.py:860-861
  if (the source predicate max_tokens is not None is truthy) {
    // Source: vvaharness/backends/llm/deepagents.py:861-861
    In source order: Evaluate once clamp_output_tokens(int(max_tokens), model, tag=tag); assign in source target order to max_tokens.
  }
  // Source: vvaharness/backends/llm/deepagents.py:862-864
  In source order: Evaluate once _provider_of(model); assign in source target order to provider. Then Evaluate once _flatten_blocks(user_prompt); assign in source target order to flat. Then Evaluate once cache_prefix or ''; assign in source target order to prefix.
  // Source: vvaharness/backends/llm/deepagents.py:865-869
  if (the source predicate prefix and (not (routes_to_anthropic(model_id, provider) and _markers_on(sdk_cfg))) is truthy) {
    // Source: vvaharness/backends/llm/deepagents.py:868-869
    In source order: Evaluate once prefix + flat; assign in source target order to flat. Then Evaluate once ''; assign in source target order to prefix.
  }
  // Source: vvaharness/backends/llm/deepagents.py:871-872
  In source order: Evaluate _check_prompt_ceiling(prefix + flat, tag=tag); retain side effects and discard the expression result. Then Evaluate once get_active_tracker(); assign in source target order to tracker.
  // Source: vvaharness/backends/llm/deepagents.py:873-881
  if (the source predicate tracker is not None is truthy) {
    // Source: vvaharness/backends/llm/deepagents.py:874-881
    In source order: Evaluate tracker.llm_payload(phase=TOKENS.current_phase(), backend='deepagents', model_id=model_id, tag=tag or '', user_prompt=prefix + flat, system_prompt=system_prompt or ''); retain side effects and discard the expression result.
  }
  // Source: vvaharness/backends/llm/deepagents.py:883-912
  In source order: Evaluate once OneShotOptions(model=model_id, model_provider=provider, use_responses_api=_use_responses_api_of(model), cwd=Path(cwd), env=build_harness_env(model_id, provider, sdk_cfg=sdk_cfg, openai_cfg=openai_cfg, cfg_dir=cfg_dir), system_prompt=system_prompt, tool_policy=ToolPolicy(), graph_name=graph_name, max_output_tokens=max_tokens, output_cap=output_cap_of(model), cache_prefix=prefix or None, cache_markers=markers_on(sdk_cfg), response_model=response_model, tool_builder=tool_builder, fact_tools=tuple(fact_tools), parent_middleware=parent_middleware, max_turns=15 if max_turns is None else max_turns, effort=effort, think_in_prompt=think_in_prompt); assign in source target order to options. Then Evaluate once effort_scaled_seconds(timeout, effort, kind=ClockKind.REQUEST); assign in source target order to request_timeout. Then Evaluate once _run_oneshot_with_truncation_retry(flat, options, model_id=model_id, tag=tag, timeout=request_timeout); assign in source target order to result. Then Evaluate once _usage_of(result); assign in source target order to usage. Then Evaluate _warn_no_usage(usage, model_id=model_id, tag=tag); retain side effects and discard the expression result.
  // Source: vvaharness/backends/llm/deepagents.py:913-916
  In source order: Evaluate once result.result_text or ''; assign in source target order to text. Then Evaluate check_response_quality(text.strip(), stage=tag or '', output_tokens=_output_tokens(usage)); retain side effects and discard the expression result.
  // Source: vvaharness/backends/llm/deepagents.py:917-917
  End this invocation with text.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/deepagents.py:923-940
// Source signature: _screen_legacy_kwargs(legacy_kw: dict[str, object], *, route: str='deepagents') -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _screen_legacy_kwargs(legacy_kw, route) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/deepagents.py:924-926
  In source order: Retain source documentation literal source_literal_924_4; it is not a model call. Then Evaluate once legacy_kw.pop('cache_prefix', None); assign in source target order to prefix.
  // Source: vvaharness/backends/llm/deepagents.py:927-934
  for each name in legacy_kw {
    // Source: vvaharness/backends/llm/deepagents.py:928-934
    if (the source predicate name not in _ACCEPTED_UNUSED_KW is truthy) {
      // Source: vvaharness/backends/llm/deepagents.py:929-934
      In source order: Evaluate warn_once(_WARNED_LEGACY_KW, name, source_template_932_16); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/backends/llm/deepagents.py:935-936
  if (the source predicate not prefix is truthy) {
    // Source: vvaharness/backends/llm/deepagents.py:936-936
    End this invocation with ''.
  }
  // Source: vvaharness/backends/llm/deepagents.py:938-939
  if (the source predicate isinstance(prefix, (list, tuple)) is truthy) {
    // Source: vvaharness/backends/llm/deepagents.py:939-939
    End this invocation with source_literal_939_15.join((str(p) for p in prefix if p)).
  }
  // Source: vvaharness/backends/llm/deepagents.py:940-940
  End this invocation with str(prefix).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/deepagents.py:943-947
// Source signature: _cfg_blocks(cfg: object) -> tuple[object, object, str | None]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _cfg_blocks(cfg) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/deepagents.py:944-946
  In source order: Retain source documentation literal source_literal_944_4; it is not a model call. Then Evaluate once getattr(cfg, '_data', None); assign in source target order to data. Then Evaluate once data.get('_config_dir') if isinstance(data, dict) else None; assign in source target order to cfg_dir.
  // Source: vvaharness/backends/llm/deepagents.py:947-947
  End this invocation with (getattr(cfg, 'sdk', None), getattr(cfg, 'openai', None), cfg_dir).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/deepagents.py:950-952
// Source signature: think_in_prompt_enabled(cfg: object) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn think_in_prompt_enabled(cfg) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/deepagents.py:951-951
  In source order: Retain source documentation literal source_literal_951_4; it is not a model call.
  // Source: vvaharness/backends/llm/deepagents.py:952-952
  End this invocation with bool(knob(cfg, 'think_in_prompt', True)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/deepagents.py:955-961
// Source signature: _json_schema_of(response_model: type) -> dict[str, object]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _json_schema_of(response_model) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/deepagents.py:956-960
  In source order: Retain source documentation literal source_literal_956_4; it is not a model call. Then Evaluate once dict(response_model.model_json_schema()); assign in source target order to schema. Then Evaluate schema.pop('title', None); retain side effects and discard the expression result. Then Evaluate schema.pop('$schema', None); retain side effects and discard the expression result.
  // Source: vvaharness/backends/llm/deepagents.py:961-961
  End this invocation with schema.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/deepagents.py:964-1025
// Source signature: dispatch_prompt(user_prompt: str | list[dict[str, object]], *, model: object, cfg: object, cwd: str, system_prompt: str | None=None, max_tokens: int | None=None, tag: str | None=None, graph_name: str=DEFAULT_GRAPH_NAME, response_model: type | None=None, tool_builder: ToolBuilder | None=None, fact_tools: Sequence[str]=(), parent_middleware: tuple[AgentMiddleware, ...]=(), max_turns: int | None=None, effort: str | None=None, **legacy_kw: object) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn dispatch_prompt(user_prompt, model, cfg, cwd, system_prompt, max_tokens, tag, graph_name, response_model, tool_builder, fact_tools, parent_middleware, max_turns, effort, legacy_kw) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/deepagents.py:982-984
  In source order: Retain source documentation literal source_literal_982_4; it is not a model call. Then Evaluate once resolve(model).via; assign in source target order to via.
  // Source: vvaharness/backends/llm/deepagents.py:985-1007
  if (the source predicate via != 'deepagents' is truthy) {
    // Source: vvaharness/backends/llm/deepagents.py:986-990
    if (the source predicate tool_builder is not None or fact_tools or parent_middleware is truthy) {
      // Source: vvaharness/backends/llm/deepagents.py:987-990
      In source order: Evaluate warn_once(_WARNED_LEGACY_KW, source_template_988_35, source_template_989_16); retain side effects and discard the expression result.
    }
    // Source: vvaharness/backends/llm/deepagents.py:991-992
    if (the source predicate effort is not None is truthy) {
      // Source: vvaharness/backends/llm/deepagents.py:992-992
      In source order: Evaluate once effort; assign in source target order to legacy_kw['effort'].
    }
    // Source: vvaharness/backends/llm/deepagents.py:993-1003
    if (the source predicate response_model is not None is truthy) {
      // Source: vvaharness/backends/llm/deepagents.py:994-1003
      if (the source predicate via in ('cli', 'openai') is truthy) {
        // Source: vvaharness/backends/llm/deepagents.py:996-996
        In source order: Evaluate once _json_schema_of(response_model); assign in source target order to legacy_kw['json_schema'].
      }
      else {
        // Source: vvaharness/backends/llm/deepagents.py:997-1003
        if (the source predicate via == 'sdk' is truthy) {
          // Source: vvaharness/backends/llm/deepagents.py:998-998
          In source order: Evaluate once response_model; assign in source target order to legacy_kw['response_model'].
        }
        else {
          // Source: vvaharness/backends/llm/deepagents.py:1000-1003
          Raise ValueError(source_template_1001_20).
        }
      }
    }
    // Source: vvaharness/backends/llm/deepagents.py:1004-1007
    End this invocation with registry.prompt(user_prompt, model=model, system_prompt=system_prompt, max_tokens=max_tokens, tag=tag, **legacy_kw).
  }
  // Source: vvaharness/backends/llm/deepagents.py:1010-1013
  In source order: Evaluate once legacy_kw.pop('timeout', None); assign in source target order to timeout. Then Evaluate once timeout if timeout is not None and timeout > 0 else None; assign in source target order to timeout. Then Evaluate once _screen_legacy_kwargs(legacy_kw); assign in source target order to prefix. Then Evaluate once _cfg_blocks(cfg); assign in source target order to (sdk_cfg, openai_cfg, cfg_dir).
  // Source: vvaharness/backends/llm/deepagents.py:1014-1025
  End this invocation with prompt(user_prompt, model=model, system_prompt=system_prompt, max_tokens=max_tokens, cwd=cwd, tag=tag, graph_name=graph_name, sdk_cfg=sdk_cfg, openai_cfg=openai_cfg, cfg_dir=cfg_dir, cache_prefix=prefix or None, response_model=response_model, tool_builder=tool_builder, fact_tools=fact_tools, parent_middleware=parent_middleware, max_turns=max_turns, effort=effort, timeout=timeout, think_in_prompt=think_in_prompt_enabled(cfg)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/deepagents.py:1028-1047
// Source signature: route_carries_tools(cfg: object, via: str, *, agentic: bool=True) -> tuple[bool, str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn route_carries_tools(cfg, via, agentic) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/deepagents.py:1030-1030
  In source order: Retain source documentation literal source_literal_1030_4; it is not a model call.
  // Source: vvaharness/backends/llm/deepagents.py:1032-1034
  if (the source predicate not agentic and via != 'deepagents' is truthy) {
    // Source: vvaharness/backends/llm/deepagents.py:1034-1034
    End this invocation with (False, 'dispatch_prompt has no tool seam on this route').
  }
  // Source: vvaharness/backends/llm/deepagents.py:1035-1036
  if (the source predicate via == 'deepagents' is truthy) {
    // Source: vvaharness/backends/llm/deepagents.py:1036-1036
    End this invocation with (True, '').
  }
  // Source: vvaharness/backends/llm/deepagents.py:1037-1038
  if (the source predicate via in ('sdk', 'openai') is truthy) {
    // Source: vvaharness/backends/llm/deepagents.py:1038-1038
    End this invocation with (True, '').
  }
  // Source: vvaharness/backends/llm/deepagents.py:1039-1046
  if (the source predicate via == 'cli' is truthy) {
    // Source: vvaharness/backends/llm/deepagents.py:1040-1041
    if (the source predicate not knob(cfg, 'cli.mcp_tools', True) is truthy) {
      // Source: vvaharness/backends/llm/deepagents.py:1041-1041
      End this invocation with (False, 'cli.mcp_tools is off').
    }
    // Source: vvaharness/backends/llm/deepagents.py:1042-1042
    In source order: Resolve source import from vvaharness.backends.llm import cli_mcp; preserve alias and import-time effects.
    // Source: vvaharness/backends/llm/deepagents.py:1043-1045
    if (the source predicate not cli_mcp.available() is truthy) {
      // Source: vvaharness/backends/llm/deepagents.py:1044-1045
      End this invocation with (False, 'the Claude Agent SDK the via: cli tool bridge needs is not importable').
    }
    // Source: vvaharness/backends/llm/deepagents.py:1046-1046
    End this invocation with (True, '').
  }
  // Source: vvaharness/backends/llm/deepagents.py:1047-1047
  End this invocation with (False, source_template_1047_18).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/deepagents.py:1050-1063
// Source signature: droppable_effort(model: object, effort: str | None, *, agentic: bool) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn droppable_effort(model, effort, agentic) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/deepagents.py:1051-1051
  In source order: Retain source documentation literal source_literal_1051_4; it is not a model call.
  // Source: vvaharness/backends/llm/deepagents.py:1054-1055
  if (the source predicate effort is None is truthy) {
    // Source: vvaharness/backends/llm/deepagents.py:1055-1055
    End this invocation with None.
  }
  // Source: vvaharness/backends/llm/deepagents.py:1056-1056
  In source order: Evaluate once resolve(model); assign in source target order to (_model_id, via, extras).
  // Source: vvaharness/backends/llm/deepagents.py:1061-1062
  if (the source predicate via == 'cli' or (via == 'sdk' and (not agentic) and ('thinking_budget' in extras)) is truthy) {
    // Source: vvaharness/backends/llm/deepagents.py:1062-1062
    End this invocation with None.
  }
  // Source: vvaharness/backends/llm/deepagents.py:1063-1063
  End this invocation with effort.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/deepagents.py:1067-1074
In source order: For _MODEL_CALL_BUDGET_CLAUSE, assign '`max_model_calls` does not bound this session on this route — `max_turns` does'; source annotation Final. Then For _EVIDENCE_GATE_NO_STACK_CLAUSE, assign "the evidence gate's tool-call requirement cannot apply with no tool stack"; source annotation Final. Then For _DROP_CLAUSES, assign {'ModelCallBudget': _MODEL_CALL_BUDGET_CLAUSE, 'EvidenceGate': _EVIDENCE_GATE_NO_STACK_CLAUSE}; source annotation Final.
// Source: vvaharness/backends/llm/deepagents.py:1077-1079
// Source signature: _stage_of(tag: str | None) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _stage_of(tag) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/deepagents.py:1078-1078
  In source order: Retain source documentation literal source_literal_1078_4; it is not a model call.
  // Source: vvaharness/backends/llm/deepagents.py:1079-1079
  End this invocation with (tag or '').split()[0] if tag else ''.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/deepagents.py:1082-1103
// Source signature: _warn_dropped_middleware(parent_middleware: tuple[AgentMiddleware, ...], *, via: str, tag: str | None) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _warn_dropped_middleware(parent_middleware, via, tag) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/deepagents.py:1084-1084
  In source order: Retain source documentation literal source_literal_1084_4; it is not a model call.
  // Source: vvaharness/backends/llm/deepagents.py:1085-1086
  if (the source predicate not parent_middleware is truthy) {
    // Source: vvaharness/backends/llm/deepagents.py:1086-1086
    End this invocation with None.
  }
  // Source: vvaharness/backends/llm/deepagents.py:1087-1094
  In source order: Resolve source import from vvaharness.backends.harness.deepagents.evidence_gate import EvidenceGate; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.deepagents.model_call_budget import ModelCallBudget; preserve alias and import-time effects. Then Evaluate once [mw for mw in parent_middleware if isinstance(mw, (ModelCallBudget, EvidenceGate))]; assign in source target order to gated.
  // Source: vvaharness/backends/llm/deepagents.py:1095-1096
  if (the source predicate not gated is truthy) {
    // Source: vvaharness/backends/llm/deepagents.py:1096-1096
    End this invocation with None.
  }
  // Source: vvaharness/backends/llm/deepagents.py:1097-1103
  In source order: Evaluate once sorted({type(mw).__name__ for mw in gated}); assign in source target order to classes. Then Evaluate once ', '.join(classes); assign in source target order to names. Then Evaluate once '; '.join((_DROP_CLAUSES[c] for c in classes)); assign in source target order to tail. Then Evaluate warn_once(_WARNED_LEGACY_KW, source_template_1101_27, source_template_1102_8); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/deepagents.py:1106-1118
// Source signature: _warn_model_call_budget_not_metered(parent_middleware: tuple[AgentMiddleware, ...], *, via: str, tag: str | None) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _warn_model_call_budget_not_metered(parent_middleware, via, tag) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/deepagents.py:1108-1111
  In source order: Retain source documentation literal source_literal_1108_4; it is not a model call. Then Resolve source import from vvaharness.backends.harness.deepagents.model_call_budget import ModelCallBudget; preserve alias and import-time effects.
  // Source: vvaharness/backends/llm/deepagents.py:1113-1114
  if (the source predicate not any((isinstance(mw, ModelCallBudget) for mw in parent_middleware)) is truthy) {
    // Source: vvaharness/backends/llm/deepagents.py:1114-1114
    End this invocation with None.
  }
  // Source: vvaharness/backends/llm/deepagents.py:1115-1118
  In source order: Evaluate warn_once(_WARNED_LEGACY_KW, source_template_1116_27, source_template_1117_8); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/deepagents.py:1121-1158
// Source signature: _adapt_tools(tool_builder: ToolBuilder | None, *, model_id: str, cwd: str, fact_tools: Sequence[str], parent_middleware: tuple[AgentMiddleware, ...], legacy_kw: dict[str, object], tag: str | None, via: str)
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _adapt_tools(tool_builder, model_id, cwd, fact_tools, parent_middleware, legacy_kw, tag, via) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/deepagents.py:1125-1125
  In source order: Retain source documentation literal source_literal_1125_4; it is not a model call.
  // Source: vvaharness/backends/llm/deepagents.py:1127-1129
  if (the source predicate tool_builder is None or not fact_tools is truthy) {
    // Source: vvaharness/backends/llm/deepagents.py:1128-1128
    In source order: Evaluate _warn_dropped_middleware(parent_middleware, via=via, tag=tag); retain side effects and discard the expression result.
    // Source: vvaharness/backends/llm/deepagents.py:1129-1129
    End this invocation with None.
  }
  // Source: vvaharness/backends/llm/deepagents.py:1130-1134
  In source order: Resolve source import from vvaharness.backends.llm import tool_adapter; preserve alias and import-time effects. Then Evaluate once tool_adapter.build(tool_builder, model=model_id, cwd=cwd, fact_tools=fact_tools, parent_middleware=parent_middleware); assign in source target order to stack.
  // Source: vvaharness/backends/llm/deepagents.py:1135-1141
  if (the source predicate stack is None is truthy) {
    // Source: vvaharness/backends/llm/deepagents.py:1136-1140
    In source order: Evaluate warn_once(_WARNED_LEGACY_KW, source_template_1137_31, source_template_1138_12); retain side effects and discard the expression result.
    // Source: vvaharness/backends/llm/deepagents.py:1141-1141
    End this invocation with None.
  }
  // Source: vvaharness/backends/llm/deepagents.py:1142-1145
  In source order: Evaluate _warn_model_call_budget_not_metered(parent_middleware, via=via, tag=tag); retain side effects and discard the expression result. Then Evaluate once list(legacy_kw.get('extra_tools') or []); assign in source target order to caller_tools. Then Evaluate once legacy_kw.get('extra_dispatch'); assign in source target order to caller_dispatch. Then Evaluate once [*stack.schemas, *caller_tools]; assign in source target order to legacy_kw['extra_tools'].
  // Source: vvaharness/backends/llm/deepagents.py:1147-1151
  // Source signature: _dispatch(name: str, args: dict)
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _dispatch(name, args) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/llm/deepagents.py:1148-1148
    In source order: Evaluate once stack.dispatch(name, args, tag=tag); assign in source target order to out.
    // Source: vvaharness/backends/llm/deepagents.py:1149-1150
    if (the source predicate out is not None is truthy) {
      // Source: vvaharness/backends/llm/deepagents.py:1150-1150
      End this invocation with out.
    }
    // Source: vvaharness/backends/llm/deepagents.py:1151-1151
    End this invocation with caller_dispatch(name, args) if caller_dispatch is not None else None.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/llm/deepagents.py:1153-1157
  In source order: Evaluate once _dispatch; assign in source target order to legacy_kw['extra_dispatch']. Then Evaluate once stack.submit_guard; assign in source target order to legacy_kw['submit_guard']. Then Evaluate once stack.exhausted_tools; assign in source target order to legacy_kw['exhausted_tools'].
  // Source: vvaharness/backends/llm/deepagents.py:1158-1158
  End this invocation with stack.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/deepagents.py:1161-1183
// Source signature: _resume_agentic_deepagents(session_id: str, instruction: str, *, model: object, tag: str | None, timeout: float | None) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _resume_agentic_deepagents(session_id, instruction, model, tag, timeout) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/deepagents.py:1163-1167
  In source order: Retain source documentation literal source_literal_1163_4; it is not a model call. Then Evaluate once _streaming_options_of(session_id); assign in source target order to held.
  // Source: vvaharness/backends/llm/deepagents.py:1168-1170
  if (the source predicate held is None is truthy) {
    // Source: vvaharness/backends/llm/deepagents.py:1169-1170
    Raise SessionNotResumableError(source_template_1170_12).
  }
  // Source: vvaharness/backends/llm/deepagents.py:1172-1173
  In source order: Evaluate once timeout if timeout is not None and timeout > 0 else None; assign in source target order to timeout. Then Evaluate once effort_scaled_seconds(timeout, held.effort, kind=ClockKind.SESSION); assign in source target order to session_timeout.
  // Source: vvaharness/backends/llm/deepagents.py:1175-1178
  for each mw in held.parent_middleware {
    // Source: vvaharness/backends/llm/deepagents.py:1176-1176
    In source order: Evaluate once getattr(mw, 'grant_resume_turn', None); assign in source target order to grant.
    // Source: vvaharness/backends/llm/deepagents.py:1177-1178
    if (the source predicate grant is not None is truthy) {
      // Source: vvaharness/backends/llm/deepagents.py:1178-1178
      In source order: Evaluate grant(); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/backends/llm/deepagents.py:1179-1182
  In source order: Evaluate once _call_classified(lambda remaining: drain_resume(instruction, held, tag=tag, timeout=remaining), model_id=resolve(model).model_id, tag=tag, budget=session_timeout); assign in source target order to terminal. Then Evaluate raise_if_refused(terminal, tag=tag); retain side effects and discard the expression result.
  // Source: vvaharness/backends/llm/deepagents.py:1183-1183
  End this invocation with terminal_text(terminal).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/deepagents.py:1186-1200
// Source signature: resume_agentic(session_id: str, instruction: str, *, model: object, cfg: object, tag: str | None=None, timeout: float | None=None) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn resume_agentic(session_id, instruction, model, cfg, tag, timeout) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/deepagents.py:1188-1194
  In source order: Retain source documentation literal source_literal_1188_4; it is not a model call. Then Evaluate once resolve(model).via; assign in source target order to via.
  // Source: vvaharness/backends/llm/deepagents.py:1195-1196
  if (the source predicate via == 'cli' is truthy) {
    // Source: vvaharness/backends/llm/deepagents.py:1196-1196
    End this invocation with _cli.session.resume_agentic(session_id, instruction, timeout=timeout, tag=tag).
  }
  // Source: vvaharness/backends/llm/deepagents.py:1197-1199
  if (the source predicate via == 'deepagents' is truthy) {
    // Source: vvaharness/backends/llm/deepagents.py:1198-1199
    End this invocation with _resume_agentic_deepagents(session_id, instruction, model=model, tag=tag, timeout=timeout).
  }
  // Source: vvaharness/backends/llm/deepagents.py:1200-1200
  Raise SessionNotResumableError(source_template_1200_35).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/deepagents.py:1203-1335
// Source signature: dispatch_agentic(user_prompt: str, *, model: object, cfg: object, cwd: str, system_prompt: str | None=None, allowed_tools: Sequence[str] | None=None, max_turns: int | None=None, max_budget_usd: float | None=None, tag: str | None=None, graph_name: str=DEFAULT_GRAPH_NAME, tool_builder: ToolBuilder | None=None, fact_tools: Sequence[str]=(), response_model: type | None=None, parent_middleware: tuple[AgentMiddleware, ...]=(), max_output_tokens: int | None=None, skill_root: Path | None=None, effort: str | None=None, agents: dict[str, object] | None=None, allow_shell: bool=False, session_id: str='', **legacy_kw: object) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn dispatch_agentic(user_prompt, model, cfg, cwd, system_prompt, allowed_tools, max_turns, max_budget_usd, tag, graph_name, tool_builder, fact_tools, response_model, parent_middleware, max_output_tokens, skill_root, effort, agents, allow_shell, session_id, legacy_kw) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/deepagents.py:1227-1229
  In source order: Retain source documentation literal source_literal_1227_4; it is not a model call. Then Evaluate once resolve(model).via; assign in source target order to via.
  // Source: vvaharness/backends/llm/deepagents.py:1230-1309
  if (the source predicate via != 'deepagents' is truthy) {
    // Source: vvaharness/backends/llm/deepagents.py:1231-1233
    In source order: Evaluate once via == 'cli' and tool_builder is not None and fact_tools and knob(cfg, 'cli.mcp_tools', True); assign in source target order to mcp_bridged. Then Evaluate once int(max_output_tokens) if max_output_tokens else None; assign in source target order to tokens.
    // Source: vvaharness/backends/llm/deepagents.py:1234-1235
    if (the source predicate tokens is truthy) {
      // Source: vvaharness/backends/llm/deepagents.py:1235-1235
      In source order: Evaluate once clamp_output_tokens(tokens, model, tag=tag); assign in source target order to tokens.
    }
    // Source: vvaharness/backends/llm/deepagents.py:1236-1246
    if (the source predicate response_model is not None is truthy) {
      // Source: vvaharness/backends/llm/deepagents.py:1237-1246
      if (the source predicate via == 'cli' is truthy) {
        // Source: vvaharness/backends/llm/deepagents.py:1238-1238
        In source order: Evaluate once _json_schema_of(response_model); assign in source target order to legacy_kw['json_schema'].
      }
      else {
        // Source: vvaharness/backends/llm/deepagents.py:1239-1246
        if (the source predicate via in ('sdk', 'openai') is truthy) {
          // Source: vvaharness/backends/llm/deepagents.py:1241-1241
          In source order: Evaluate once response_model; assign in source target order to legacy_kw['response_model'].
        }
        else {
          // Source: vvaharness/backends/llm/deepagents.py:1243-1246
          Raise ValueError(source_template_1244_20).
        }
      }
    }
    // Source: vvaharness/backends/llm/deepagents.py:1247-1274
    if (the source predicate mcp_bridged is truthy) {
      // Source: vvaharness/backends/llm/deepagents.py:1248-1256
      In source order: Resolve source import from vvaharness.backends.llm import cli_mcp; preserve alias and import-time effects. Then Evaluate once legacy_kw.pop('timeout', None); assign in source target order to timeout. Then Evaluate once _screen_legacy_kwargs(legacy_kw, route='cli'); assign in source target order to bridge_prefix.
      // Source: vvaharness/backends/llm/deepagents.py:1257-1259
      if (the source predicate bridge_prefix is truthy) {
        // Source: vvaharness/backends/llm/deepagents.py:1259-1259
        In source order: Evaluate once bridge_prefix + user_prompt; assign in source target order to user_prompt.
      }
      // Source: vvaharness/backends/llm/deepagents.py:1261-1264
      In source order: Evaluate legacy_kw.pop('stream_cb', None); retain side effects and discard the expression result. Then Evaluate legacy_kw.pop('permission_mode', None); retain side effects and discard the expression result. Then Evaluate legacy_kw.pop('json_schema', None); retain side effects and discard the expression result.
      // Source: vvaharness/backends/llm/deepagents.py:1265-1274
      End this invocation with cli_mcp.agentic_with_tools(user_prompt, model=resolve(model).model_id, system_prompt=system_prompt, allowed_tools=allowed_tools, cwd=cwd, tool_builder=tool_builder, fact_tools=fact_tools, parent_middleware=parent_middleware, max_turns=max_turns, max_budget_usd=max_budget_usd, max_tokens=tokens, effort=effort, allow_shell=allow_shell, response_model=response_model, tag=tag, timeout=timeout).
    }
    // Source: vvaharness/backends/llm/deepagents.py:1275-1280
    if (the source predicate via == 'cli' and (skill_root is not None or allow_shell) is truthy) {
      // Source: vvaharness/backends/llm/deepagents.py:1277-1280
      In source order: Evaluate warn_once(_WARNED_LEGACY_KW, 'cli_skill_root_allow_shell', source_template_1279_16); retain side effects and discard the expression result.
    }
    // Source: vvaharness/backends/llm/deepagents.py:1281-1283
    if (the source predicate via == 'cli' and effort is not None is truthy) {
      // Source: vvaharness/backends/llm/deepagents.py:1283-1283
      In source order: Evaluate once effort; assign in source target order to legacy_kw['effort'].
    }
    // Source: vvaharness/backends/llm/deepagents.py:1284-1285
    if (the source predicate via == 'cli' and tokens is truthy) {
      // Source: vvaharness/backends/llm/deepagents.py:1285-1285
      In source order: Evaluate once tokens; assign in source target order to legacy_kw['max_tokens'].
    }
    // Source: vvaharness/backends/llm/deepagents.py:1286-1288
    if (the source predicate via == 'cli' and session_id is truthy) {
      // Source: vvaharness/backends/llm/deepagents.py:1288-1288
      In source order: Evaluate once session_id; assign in source target order to legacy_kw['session_id'].
    }
    // Source: vvaharness/backends/llm/deepagents.py:1289-1291
    if (the source predicate via == 'cli' is truthy) {
      // Source: vvaharness/backends/llm/deepagents.py:1291-1291
      In source order: Evaluate _warn_dropped_middleware(parent_middleware, via=via, tag=tag); retain side effects and discard the expression result.
    }
    // Source: vvaharness/backends/llm/deepagents.py:1292-1292
    In source order: Evaluate once None; assign in source target order to stack.
    // Source: vvaharness/backends/llm/deepagents.py:1293-1301
    if (the source predicate via in ('sdk', 'openai') is truthy) {
      // Source: vvaharness/backends/llm/deepagents.py:1294-1295
      if (the source predicate tokens is truthy) {
        // Source: vvaharness/backends/llm/deepagents.py:1295-1295
        In source order: Evaluate once tokens; assign in source target order to legacy_kw['max_output_tokens'].
      }
      // Source: vvaharness/backends/llm/deepagents.py:1297-1301
      In source order: Evaluate once effort; assign in source target order to legacy_kw['effort']. Then Evaluate once _adapt_tools(tool_builder, model_id=resolve(model).model_id, cwd=cwd, fact_tools=fact_tools, parent_middleware=parent_middleware, legacy_kw=legacy_kw, tag=tag, via=via); assign in source target order to stack.
    }
    // Source: vvaharness/backends/llm/deepagents.py:1302-1306
    In source order: Evaluate once registry.agentic(user_prompt, model=model, system_prompt=system_prompt, allowed_tools=allowed_tools, cwd=cwd, max_budget_usd=max_budget_usd, max_turns=max_turns, tag=tag, **legacy_kw); assign in source target order to text.
    // Source: vvaharness/backends/llm/deepagents.py:1307-1308
    if (the source predicate stack is not None is truthy) {
      // Source: vvaharness/backends/llm/deepagents.py:1308-1308
      In source order: Evaluate stack.report_evidence_degradation(tag=tag or '', label=via); retain side effects and discard the expression result.
    }
    // Source: vvaharness/backends/llm/deepagents.py:1309-1309
    End this invocation with text.
  }
  // Source: vvaharness/backends/llm/deepagents.py:1313-1316
  In source order: Evaluate once legacy_kw.pop('timeout', None); assign in source target order to timeout. Then Evaluate once timeout if timeout is not None and timeout > 0 else None; assign in source target order to timeout. Then Evaluate once _screen_legacy_kwargs(legacy_kw); assign in source target order to prefix. Then Evaluate once _cfg_blocks(cfg); assign in source target order to (sdk_cfg, openai_cfg, cfg_dir).
  // Source: vvaharness/backends/llm/deepagents.py:1317-1335
  End this invocation with agentic(user_prompt, model=model, system_prompt=system_prompt, allowed_tools=allowed_tools, cwd=cwd, max_budget_usd=max_budget_usd, max_turns=max_turns, tag=tag, graph_name=graph_name, sdk_cfg=sdk_cfg, openai_cfg=openai_cfg, cfg_dir=cfg_dir, tool_builder=tool_builder, fact_tools=fact_tools, response_model=response_model, parent_middleware=parent_middleware, cache_prefix=prefix or None, max_output_tokens=max_output_tokens, skill_root=skill_root, effort=effort, agents=agents, allow_shell=allow_shell, timeout=timeout, session_id=session_id, think_in_prompt=think_in_prompt_enabled(cfg)).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.util import logs` at source line 42: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import logs` at source line 42: `source_detail/vvaharness/util/logs.py.sudo.md`.
- `from vvaharness.backends.harness import READ_TOOLS, HarnessProcessError, HarnessResult, OneShotOptions, OneShotResult, StreamingOptions, ToolPolicy, get_harness` at source line 47: `source_detail/vvaharness/backends/harness/__init__.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.limits import MODEL_MAX_OUTPUT_TOKENS` at source line 57: `source_detail/vvaharness/backends/harness/deepagents/limits.py.sudo.md`.
- `from vvaharness.backends.harness.models import DEFAULT_GRAPH_NAME, LOGICAL_TO_NATIVE, NATIVE_IMPLIED_READS, NATIVE_SHELL_TOOL, AuthenticationError, OversizePromptError, ProxyError, SessionNotResumableError, ToolBuilder, ToolStateNotRoundTrippedError, TruncatedResponseError` at source line 58: `source_detail/vvaharness/backends/harness/models.py.sudo.md`.
- `from vvaharness.backends.harness.provider_routing import credential_env_overrides, routes_to_anthropic` at source line 71: `source_detail/vvaharness/backends/harness/provider_routing.py.sudo.md`.
- `from vvaharness.backends.harness.transcript import Transcript, open_transcript` at source line 75: `source_detail/vvaharness/backends/harness/transcript.py.sudo.md`.
- `from vvaharness.backends.llm import cli as _cli` at source line 76: `source_detail/vvaharness/backends/llm/__init__.py.sudo.md`.
- `from vvaharness.backends.llm import cli as _cli` at source line 76: `source_detail/vvaharness/backends/llm/cli/__init__.py.sudo.md`.
- `from vvaharness.backends.llm import registry` at source line 77: `source_detail/vvaharness/backends/llm/__init__.py.sudo.md`.
- `from vvaharness.backends.llm import registry` at source line 77: `source_detail/vvaharness/backends/llm/registry.py.sudo.md`.
- `from vvaharness.backends.llm.cache import markers_enabled` at source line 78: `source_detail/vvaharness/backends/llm/cache.py.sudo.md`.
- `from vvaharness.backends.llm.cli import _truncation_error` at source line 81: `source_detail/vvaharness/backends/llm/cli/__init__.py.sudo.md`.
- `from vvaharness.backends.llm.models import AGENTIC_MAX_TOKENS, DEEPAGENTS_MAX_PROMPT_TOKENS, RATE_LIMIT_TRANSIENT_RX, RETRYABLE_STATUS, SERVER_ERROR_TRANSIENT_RX, TRUNCATED_REPLIES_COUNTER, ClockKind, ModelRefusal, call_timeout_error, effort_scaled_seconds, jittered_delay, model_refusal, model_refusal_from, note_budget_use, proxy_detail, truncation_retry_max, turn_timeout, wait_overrun` at source line 82: `source_detail/vvaharness/backends/llm/models.py.sudo.md`.
- `from vvaharness.backends.llm.registry import _flatten_blocks, clamp_output_tokens, output_cap_of, resolve` at source line 102: `source_detail/vvaharness/backends/llm/registry.py.sudo.md`.
- `from vvaharness.backends.llm.sdk import _AUTH_STATUS_RX` at source line 110: `source_detail/vvaharness/backends/llm/sdk.py.sudo.md`.
- `from vvaharness.report.redact import redact` at source line 111: `source_detail/vvaharness/report/redact.py.sudo.md`.
- `from vvaharness.util import console` at source line 112: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import console` at source line 112: `source_detail/vvaharness/util/console.py.sudo.md`.
- `from vvaharness.util.config import knob` at source line 113: `source_detail/vvaharness/util/config.py.sudo.md`.
- `from vvaharness.util.counters import COUNTERS` at source line 114: `source_detail/vvaharness/util/counters.py.sudo.md`.
- `from vvaharness.util.events import Event` at source line 115: `source_detail/vvaharness/util/events.py.sudo.md`.
- `from vvaharness.util.exceptions import exception_chain` at source line 116: `source_detail/vvaharness/util/exceptions.py.sudo.md`.
- `from vvaharness.util.response_quality import check_response_quality, output_tokens_for_gate` at source line 117: `source_detail/vvaharness/util/response_quality.py.sudo.md`.
- `from vvaharness.util.scan_progress import get_active_tracker` at source line 121: `source_detail/vvaharness/util/scan_progress.py.sudo.md`.
- `from vvaharness.util.tokens import TOKENS, TokenUsage, estimate_tokens` at source line 122: `source_detail/vvaharness/util/tokens.py.sudo.md`.
- `from vvaharness.util.warn_once import warn_once` at source line 123: `source_detail/vvaharness/util/warn_once.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.client import _is_missing_thought_signature` at source line 327: `source_detail/vvaharness/backends/harness/deepagents/client.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.options.model_building import tls_carriers_for` at source line 502: `source_detail/vvaharness/backends/harness/deepagents/options/model_building.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.options import release_session` at source line 564: `source_detail/vvaharness/backends/harness/deepagents/options/__init__.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.evidence_gate import EvidenceGate` at source line 1087: `source_detail/vvaharness/backends/harness/deepagents/evidence_gate.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.model_call_budget import ModelCallBudget` at source line 1090: `source_detail/vvaharness/backends/harness/deepagents/model_call_budget.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.model_call_budget import ModelCallBudget` at source line 1109: `source_detail/vvaharness/backends/harness/deepagents/model_call_budget.py.sudo.md`.
- `from vvaharness.backends.llm import tool_adapter` at source line 1130: `source_detail/vvaharness/backends/llm/__init__.py.sudo.md`.
- `from vvaharness.backends.llm import tool_adapter` at source line 1130: `source_detail/vvaharness/backends/llm/tool_adapter.py.sudo.md`.
- `from vvaharness.backends.llm import cli_mcp` at source line 1042: `source_detail/vvaharness/backends/llm/__init__.py.sudo.md`.
- `from vvaharness.backends.llm import cli_mcp` at source line 1042: `source_detail/vvaharness/backends/llm/cli_mcp.py.sudo.md`.
- `from vvaharness.backends.llm import cli_mcp` at source line 1248: `source_detail/vvaharness/backends/llm/__init__.py.sudo.md`.
- `from vvaharness.backends.llm import cli_mcp` at source line 1248: `source_detail/vvaharness/backends/llm/cli_mcp.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../prompt_representation/vvaharness/backends/llm/deepagents.py.sudo.md). Exact strings in the evidence asset support this conversion.
