# vvaharness/backends/harness/deepagents/options/graph_builder.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/backends/harness/deepagents/options/graph_builder.py.evidence.json`. SHA-256: `19340b142dfbbfdbda20ba514e515cdaeae87b9a7c83aa01fd283d1c4719cd91`.

```sudo
// Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import threading; preserve alias and import-time effects. Then Resolve source import import typing; preserve alias and import-time effects. Then Resolve source import import warnings; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:22-27
In source order: Resolve source import from contextlib import contextmanager; preserve alias and import-time effects. Then Resolve source import from dataclasses import replace; preserve alias and import-time effects. Then Resolve source import from enum import Enum; preserve alias and import-time effects. Then Resolve source import from typing import TYPE_CHECKING, Any; preserve alias and import-time effects. Then Resolve source import from deepagents import create_deep_agent; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:28-35
In source order: Resolve source import from deepagents.backends import FilesystemBackend; preserve alias and import-time effects. Then Resolve source import from deepagents.middleware.filesystem import FilesystemPermission; preserve alias and import-time effects. Then Resolve source import from deepagents.profiles.harness.harness_profiles import _HARNESS_PROFILES, _ensure_harness_profiles_loaded; preserve alias and import-time effects. Then Resolve source import from langchain.agents.middleware import ModelRetryMiddleware; preserve alias and import-time effects. Then Resolve source import from langchain.agents.middleware.types import AgentMiddleware, ExtendedModelResponse, ModelResponse; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:36-40
In source order: Resolve source import from langchain.agents.structured_output import StructuredOutputValidationError, ToolStrategy; preserve alias and import-time effects. Then Resolve source import from langchain_core.exceptions import ModelInvalidRequestError; preserve alias and import-time effects. Then Resolve source import from langchain_core.messages import ToolMessage; preserve alias and import-time effects. Then Resolve source import from langchain_core.tools import BaseTool; preserve alias and import-time effects. Then Resolve source import from langgraph.checkpoint.memory import MemorySaver; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:41-46
In source order: Resolve source import from langgraph.checkpoint.serde.jsonplus import JsonPlusSerializer; preserve alias and import-time effects. Then Resolve source import from langgraph.graph.state import CompiledStateGraph; preserve alias and import-time effects. Then Resolve source import from pydantic import BaseModel; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.deepagents.exclude_tools import ExcludeTools; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.deepagents.invalid_tool_args import RepairInvalidToolArgs; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:47-55
In source order: Resolve source import from vvaharness.backends.harness.deepagents.limits import MODEL_MAX_OUTPUT_TOKENS; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.deepagents.models import DELETE_TOOL_NAME, SubagentSpec; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.deepagents.options.model_building import REASON_IN_PROMPT, build_model_cached, reasons_in_prompt; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.deepagents.options.response_format import submit_instructed_prompt; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.deepagents.permit_tools import PermitTools; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:56-63
In source order: Resolve source import from vvaharness.backends.harness.deepagents.profiles import register_vvah_harness_profiles, stage_profile_suffix; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.deepagents.prompt_caching import BlockMarkerPromptCaching; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.deepagents.redaction import read_only_middleware; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.deepagents.translate import reply_truncated; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.deepagents.usage import SessionUsage, aggregate_usage_metadata; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:64-73
In source order: Resolve source import from vvaharness.backends.harness.models import TruncatedResponseError; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm.models import TRUNCATED_RETRY_ATTEMPTED_COUNTER, TRUNCATED_RETRY_RECOVERED_COUNTER, proxy_detail, truncation_retry_max; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm.openai import _payload_shape; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import console, logs; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import errlog as _errlog; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:74-78
In source order: Resolve source import from vvaharness.util.counters import COUNTERS; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.events import Event; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.response_quality import is_connection_failure; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.scan_progress import is_stage_only; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.tokens import TOKENS; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:80-88
In source order: Evaluate once logs.get_logger(__name__); assign in source target order to log. Then Evaluate warnings.filterwarnings('once', message='tool_choice is forced but thinking is enabled', category=UserWarning); retain side effects and discard the expression result.
// Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:90-98
if (the source predicate TYPE_CHECKING is truthy) {
  // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:91-98
  In source order: Resolve source import from collections.abc import Awaitable, Callable, Generator; preserve alias and import-time effects. Then Resolve source import from langchain.agents.middleware.types import ModelCallResult, ModelRequest, ToolCallRequest; preserve alias and import-time effects. Then Resolve source import from langgraph.types import Command; preserve alias and import-time effects.
}
// Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:101-101
In source order: Evaluate once threading.Lock(); assign in source target order to _BUILD_LOCK.
// Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:105-107
// Source signature: _connection_retryable(exc: Exception) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _connection_retryable(exc) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:106-106
  In source order: Retain source documentation literal source_literal_106_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:107-107
  End this invocation with is_connection_failure(exc) and proxy_detail(exc) is None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:111-114
In source order: Evaluate once ModelRetryMiddleware(max_retries=3, initial_delay=5, backoff_factor=2, max_delay=60, retry_on=_connection_retryable, on_failure='error'); assign in source target order to _CONNECTION_RETRY_MIDDLEWARE.
// Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:117-145
interface LogToolCalls {
  Describe the source Python type, preserving its base/metaclass expression order: AgentMiddleware.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:118-118
  In source order: Retain source documentation literal source_literal_118_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:121-123
  // Source signature: __init__(self, tag: str | None=None) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self, tag) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:122-123
    In source order: Evaluate super().__init__(); retain side effects and discard the expression result. Then Evaluate once tag; assign in source target order to self._tag.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:125-133
  // Source signature: _log(self, request: ToolCallRequest, result: ToolMessage | Command[Any]) -> ToolMessage | Command[Any]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _log(self, request, result) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:127-132
    if (the source predicate not is_stage_only() is truthy) {
      // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:128-132
      In source order: Evaluate once request.tool_call.get('name') or ''; assign in source target order to name. Then Evaluate once getattr(result, 'content', ''); assign in source target order to content. Then Evaluate once len(content) if isinstance(content, str) else 0; assign in source target order to n. Then Evaluate once source_template_131_21 if self._tag else ''; assign in source target order to suffix. Then Evaluate console.write(source_template_132_26); retain side effects and discard the expression result.
    }
    // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:133-133
    End this invocation with result.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:135-139
  // Source signature: wrap_tool_call(self, request: ToolCallRequest, handler: Callable[[ToolCallRequest], ToolMessage | Command[Any]]) -> ToolMessage | Command[Any]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn wrap_tool_call(self, request, handler) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:139-139
    End this invocation with self._log(request, handler(request)).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:141-145
  // Source signature: awrap_tool_call(self, request: ToolCallRequest, handler: Callable[[ToolCallRequest], Awaitable[ToolMessage | Command[Any]]]) -> ToolMessage | Command[Any]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn awrap_tool_call(self, request, handler) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    This callable produces a coroutine or async generator; await/suspension positions remain in source expressions.
    // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:145-145
    End this invocation with self._log(request, await handler(request)).
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:149-162
// Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:148-148
Before creating this callable, evaluate and retain decorators top-to-bottom: contextmanager.
// Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:149-162
// Source signature: _restaged_harness_profiles(stage: str | None, *, blank: bool) -> Generator[None]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _restaged_harness_profiles(stage, blank) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:150-153
  In source order: Retain source documentation literal source_literal_150_4; it is not a model call. Then Evaluate _ensure_harness_profiles_loaded(); retain side effects and discard the expression result. Then Evaluate once dict(_HARNESS_PROFILES); assign in source target order to saved.
  // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:154-157
  for each (key, profile) in saved.items() {
    // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:155-155
    In source order: Evaluate once '' if blank else stage_profile_suffix(stage, key); assign in source target order to suffix.
    // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:156-157
    if (the source predicate suffix is not None is truthy) {
      // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:157-157
      In source order: Evaluate once replace(profile, system_prompt_suffix=suffix); assign in source target order to _HARNESS_PROFILES[key].
    }
  }
  // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:158-162
  Perform the following protected operations {
    // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:159-159
    In source order: Yield None; suspend this generator until resumed.
  }
  On every exit from this protected/handler/normal-completion region {
    // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:161-162
    In source order: Evaluate _HARNESS_PROFILES.clear(); retain side effects and discard the expression result. Then Evaluate _HARNESS_PROFILES.update(saved); retain side effects and discard the expression result.
  }
  If execution reaches this end, finish with the source implicit None result.
}
At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
// Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:165-171
// Source signature: _result_messages(result: ModelCallResult) -> list
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _result_messages(result) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:166-166
  In source order: Retain source documentation literal source_literal_166_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:167-168
  if (the source predicate isinstance(result, ExtendedModelResponse) is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:168-168
    In source order: Evaluate once result.model_response; assign in source target order to result.
  }
  // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:169-170
  if (the source predicate isinstance(result, ModelResponse) is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:170-170
    End this invocation with result.result.
  }
  // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:171-171
  End this invocation with [result].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:174-284
interface CapOutputTokens {
  Describe the source Python type, preserving its base/metaclass expression order: AgentMiddleware.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:175-175
  In source order: Retain source documentation literal source_literal_175_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:178-184
  // Source signature: __init__(self, max_tokens: int, *, tag: str | None=None, cap: int | None=None) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self, max_tokens, tag, cap) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:180-184
    In source order: Retain source documentation literal source_literal_180_8; it is not a model call. Then Evaluate super().__init__(); retain side effects and discard the expression result. Then Evaluate once max_tokens; assign in source target order to self._max_tokens. Then Evaluate once tag; assign in source target order to self._tag. Then Evaluate once cap if cap is not None else MODEL_MAX_OUTPUT_TOKENS; assign in source target order to self._cap_ceiling.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:186-189
  // Source signature: _cap(self, request: ModelRequest, max_tokens: int) -> ModelRequest
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _cap(self, request, max_tokens) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:187-189
    End this invocation with request.override(model_settings={**request.model_settings, 'max_tokens': max_tokens}).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:191-192
  // Source signature: _retry_at(self) -> int | None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _retry_at(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:192-192
    End this invocation with truncation_retry_max(self._max_tokens, cap=self._cap_ceiling).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:194-199
  // Source signature: _bank(self, discarded: ModelCallResult) -> SessionUsage | None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _bank(self, discarded) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:195-196
    In source order: Retain source documentation literal source_literal_195_8; it is not a model call. Then Evaluate once aggregate_usage_metadata(_result_messages(discarded)); assign in source target order to usage.
    // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:197-198
    if (the source predicate usage is truthy) {
      // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:198-198
      In source order: Evaluate TOKENS.add(usage, turns=usage.get('turns')); retain side effects and discard the expression result.
    }
    // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:199-199
    End this invocation with usage.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:201-211
  // Source signature: _log_retry(self, retry_at: int, usage: SessionUsage | None) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _log_retry(self, retry_at, usage) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:202-211
    In source order: Evaluate once usage.get('output_tokens') if usage else None; assign in source target order to produced. Then Evaluate COUNTERS.bump(TRUNCATED_RETRY_ATTEMPTED_COUNTER); retain side effects and discard the expression result. Then Evaluate log.warning(Event.TRUNCATED_RETRY, route='deepagents', max_tokens=self._max_tokens, retry_at=retry_at); retain side effects and discard the expression result. Then Evaluate _errlog.log(self._tag or 'deepagents', self._tag or 'truncation', source_template_208_12, error_code=TruncatedResponseError.error_code, recovered=True, produced=produced); retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:213-220
  // Source signature: _truncation_retry_at(self, discarded: ModelCallResult) -> int | None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _truncation_retry_at(self, discarded) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:214-214
    In source order: Retain source documentation literal source_literal_214_8; it is not a model call.
    // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:215-216
    if (the source predicate not reply_truncated(_result_messages(discarded)) is truthy) {
      // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:216-216
      End this invocation with None.
    }
    // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:217-217
    In source order: Evaluate once self._retry_at(); assign in source target order to retry_at.
    // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:218-219
    if (the source predicate retry_at is not None is truthy) {
      // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:219-219
      In source order: Evaluate self._log_retry(retry_at, self._bank(discarded)); retain side effects and discard the expression result.
    }
    // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:220-220
    End this invocation with retry_at.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:222-232
  // Source signature: _rejected(self, exc: StructuredOutputValidationError) -> int | None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _rejected(self, exc) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:223-226
    In source order: Retain source documentation literal source_literal_223_8; it is not a model call. Then Evaluate once self._bank(exc.ai_message); assign in source target order to usage.
    // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:227-228
    if (the source predicate not reply_truncated([exc.ai_message]) is truthy) {
      // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:228-228
      End this invocation with None.
    }
    // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:229-229
    In source order: Evaluate once self._retry_at(); assign in source target order to retry_at.
    // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:230-231
    if (the source predicate retry_at is not None is truthy) {
      // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:231-231
      In source order: Evaluate self._log_retry(retry_at, usage); retain side effects and discard the expression result.
    }
    // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:232-232
    End this invocation with retry_at.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:235-239
  // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:234-234
  Before creating this callable, evaluate and retain decorators top-to-bottom: staticmethod.
  // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:235-239
  // Source signature: _accepted(retried: ModelCallResult) -> ModelCallResult
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _accepted(retried) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:236-236
    In source order: Retain source documentation literal source_literal_236_8; it is not a model call.
    // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:237-238
    if (the source predicate not reply_truncated(_result_messages(retried)) is truthy) {
      // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:238-238
      In source order: Evaluate COUNTERS.bump(TRUNCATED_RETRY_RECOVERED_COUNTER); retain side effects and discard the expression result.
    }
    // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:239-239
    End this invocation with retried.
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:242-248
  // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:241-241
  Before creating this callable, evaluate and retain decorators top-to-bottom: contextmanager.
  // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:242-248
  // Source signature: _banking_rejected_final(self) -> Generator[None]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _banking_rejected_final(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:243-243
    In source order: Retain source documentation literal source_literal_243_8; it is not a model call.
    // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:244-248
    Perform the following protected operations {
      // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:245-245
      In source order: Yield None; suspend this generator until resumed.
    }
    // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:246-248
    On the first matching source exception StructuredOutputValidationError as exc, in handler order {
      // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:247-247
      In source order: Evaluate self._bank(exc.ai_message); retain side effects and discard the expression result.
      // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:248-248
      Raise the currently handled exception.
    }
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:250-265
  // Source signature: wrap_model_call(self, request: ModelRequest, handler: Callable[[ModelRequest], ModelCallResult]) -> ModelCallResult
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn wrap_model_call(self, request, handler) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:253-253
    In source order: Retain source documentation literal source_literal_253_8; it is not a model call.
    // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:254-263
    Perform the following protected operations {
      // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:255-255
      In source order: Evaluate once handler(self._cap(request, self._max_tokens)); assign in source target order to result.
    }
    // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:256-259
    On the first matching source exception StructuredOutputValidationError as exc, in handler order {
      // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:257-257
      In source order: Evaluate once self._rejected(exc); assign in source target order to retry_at.
      // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:258-259
      if (the source predicate retry_at is None is truthy) {
        // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:259-259
        Raise the currently handled exception.
      }
    }
    Only when the protected body falls through normally, without exception, return, break or continue {
      // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:261-261
      In source order: Evaluate once self._truncation_retry_at(result); assign in source target order to retry_at.
      // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:262-263
      if (the source predicate retry_at is None is truthy) {
        // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:263-263
        End this invocation with result.
      }
    }
    // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:264-265
    Enter source context managers left-to-right: self._banking_rejected_final() {
      // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:265-265
      End this invocation with self._accepted(handler(self._cap(request, retry_at))).
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:267-284
  // Source signature: awrap_model_call(self, request: ModelRequest, handler: Callable[[ModelRequest], Awaitable[ModelCallResult]]) -> ModelCallResult
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn awrap_model_call(self, request, handler) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    This callable produces a coroutine or async generator; await/suspension positions remain in source expressions.
    // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:272-272
    In source order: Retain source documentation literal source_literal_272_8; it is not a model call.
    // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:273-282
    Perform the following protected operations {
      // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:274-274
      In source order: Evaluate once await handler(self._cap(request, self._max_tokens)); assign in source target order to result.
    }
    // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:275-278
    On the first matching source exception StructuredOutputValidationError as exc, in handler order {
      // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:276-276
      In source order: Evaluate once self._rejected(exc); assign in source target order to retry_at.
      // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:277-278
      if (the source predicate retry_at is None is truthy) {
        // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:278-278
        Raise the currently handled exception.
      }
    }
    Only when the protected body falls through normally, without exception, return, break or continue {
      // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:280-280
      In source order: Evaluate once self._truncation_retry_at(result); assign in source target order to retry_at.
      // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:281-282
      if (the source predicate retry_at is None is truthy) {
        // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:282-282
        End this invocation with result.
      }
    }
    // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:283-284
    Enter source context managers left-to-right: self._banking_rejected_final() {
      // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:284-284
      End this invocation with self._accepted(await handler(self._cap(request, retry_at))).
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:287-322
interface LogInvalidRequestShape {
  Describe the source Python type, preserving its base/metaclass expression order: AgentMiddleware.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:288-288
  In source order: Retain source documentation literal source_literal_288_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:290-293
  // Source signature: __init__(self, *, tag: str | None=None) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self, tag) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:291-293
    In source order: Retain source documentation literal source_literal_291_8; it is not a model call. Then Evaluate super().__init__(); retain side effects and discard the expression result. Then Evaluate once tag; assign in source target order to self._tag.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:295-300
  // Source signature: _log_shape(self, request: ModelRequest, exc: ModelInvalidRequestError) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _log_shape(self, request, exc) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:297-300
    In source order: Evaluate _errlog.log(self._tag or 'deepagents', self._tag or 'invalid-request', _payload_shape([{'content': m.content} for m in request.messages], str(exc)), reason='deepagents_invalid_request_shape', recovered=True); retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:302-310
  // Source signature: wrap_model_call(self, request: ModelRequest, handler: Callable[[ModelRequest], ModelCallResult]) -> ModelCallResult
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn wrap_model_call(self, request, handler) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:305-305
    In source order: Retain source documentation literal source_literal_305_8; it is not a model call.
    // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:306-310
    Perform the following protected operations {
      // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:307-307
      End this invocation with handler(request).
    }
    // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:308-310
    On the first matching source exception ModelInvalidRequestError as exc, in handler order {
      // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:309-309
      In source order: Evaluate self._log_shape(request, exc); retain side effects and discard the expression result.
      // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:310-310
      Raise the currently handled exception.
    }
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:312-322
  // Source signature: awrap_model_call(self, request: ModelRequest, handler: Callable[[ModelRequest], Awaitable[ModelCallResult]]) -> ModelCallResult
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn awrap_model_call(self, request, handler) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    This callable produces a coroutine or async generator; await/suspension positions remain in source expressions.
    // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:317-317
    In source order: Retain source documentation literal source_literal_317_8; it is not a model call.
    // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:318-322
    Perform the following protected operations {
      // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:319-319
      End this invocation with await handler(request).
    }
    // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:320-322
    On the first matching source exception ModelInvalidRequestError as exc, in handler order {
      // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:321-321
      In source order: Evaluate self._log_shape(request, exc); retain side effects and discard the expression result.
      // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:322-322
      Raise the currently handled exception.
    }
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:325-337
// Source signature: _leaf_serde_classes(annotation: Any) -> list[type]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _leaf_serde_classes(annotation) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:326-326
  In source order: Retain source documentation literal source_literal_326_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:327-328
  if (the source predicate annotation is None is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:328-328
    End this invocation with [].
  }
  // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:329-329
  In source order: Evaluate once typing.get_args(annotation); assign in source target order to args.
  // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:330-334
  if (the source predicate args is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:331-331
    In source order: For out, assign []; source annotation list[type].
    // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:332-333
    for each arg in args {
      // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:333-333
      In source order: Evaluate out.extend(_leaf_serde_classes(arg)); retain side effects and discard the expression result.
    }
    // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:334-334
    End this invocation with out.
  }
  // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:335-336
  if (the source predicate isinstance(annotation, type) and issubclass(annotation, (BaseModel, Enum)) is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:336-336
    End this invocation with [annotation].
  }
  // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:337-337
  End this invocation with [].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:340-355
// Source signature: _reachable_serde_classes(root: type) -> list[tuple[str, str]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _reachable_serde_classes(root) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:341-344
  In source order: Retain source documentation literal source_literal_341_4; it is not a model call. Then For seen, assign set(); source annotation set[type]. Then For stack, assign [root]; source annotation list[type].
  // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:345-354
  while (the source predicate stack is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:346-346
    In source order: Evaluate once stack.pop(); assign in source target order to cls.
    // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:347-348
    if (the source predicate cls in seen is truthy) {
      // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:348-348
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:349-349
    In source order: Evaluate seen.add(cls); retain side effects and discard the expression result.
    // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:350-354
    if (the source predicate issubclass(cls, BaseModel) is truthy) {
      // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:351-354
      for each field in cls.model_fields.values() {
        // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:352-354
        for each nested in _leaf_serde_classes(field.annotation) {
          // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:353-354
          if (the source predicate nested not in seen is truthy) {
            // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:354-354
            In source order: Evaluate stack.append(nested); retain side effects and discard the expression result.
          }
        }
      }
    }
  }
  // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:355-355
  End this invocation with [(cls.__module__, cls.__name__) for cls in seen].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:358-458
// Source signature: _create_agent(model_id: str, env: dict[str, str], system_prompt: str | None, tools: list[BaseTool], *, name: str, skills: list[str] | None, permissions: list[FilesystemPermission], model_provider: str | None=None, redact_reads: bool=False, backend: FilesystemBackend | None=None, response_model: type | None=None, response_format: ToolStrategy | type | None=None, subagents: list[SubagentSpec] | None=None, extra_excluded_tools: frozenset[str] | None=None, max_output_tokens: int | None=None, output_cap: int | None=None, permitted_tool_calls: frozenset[str] | None=None, strip_harness_suffix: bool=False, cache_markers: bool=True, cache_tail: bool=True, parent_middleware: tuple[AgentMiddleware, ...]=(), effort: str | None=None, use_responses_api: bool | None=None, think_in_prompt: bool=False) -> CompiledStateGraph
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _create_agent(model_id, env, system_prompt, tools, name, skills, permissions, model_provider, redact_reads, backend, response_model, response_format, subagents, extra_excluded_tools, max_output_tokens, output_cap, permitted_tool_calls, strip_harness_suffix, cache_markers, cache_tail, parent_middleware, effort, use_responses_api, think_in_prompt) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:385-386
  In source order: Retain source documentation literal source_literal_385_4; it is not a model call. Then For checkpointer, declare without assigning a value; source annotation MemorySaver.
  // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:387-394
  if (the source predicate response_model is None is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:388-388
    In source order: Evaluate once MemorySaver(); assign in source target order to checkpointer.
  }
  else {
    // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:391-394
    In source order: Evaluate once _reachable_serde_classes(response_model); assign in source target order to allowed_models. Then Evaluate once MemorySaver(serde=JsonPlusSerializer(allowed_msgpack_modules=allowed_models)); assign in source target order to checkpointer.
  }
  // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:395-415
  In source order: Evaluate once build_model_cached(model_id, env, model_provider, effort, use_responses_api); assign in source target order to model. Then Evaluate once submit_instructed_prompt(system_prompt, model, response_model, response_format); assign in source target order to system_prompt. Then Evaluate register_vvah_harness_profiles(); retain side effects and discard the expression result. Then For kwargs, assign {'model': build_model_cached(model_id, env, model_provider, effort, use_responses_api, think_in_prompt=think_in_prompt), 'system_prompt': (system_prompt or '') + REASON_IN_PROMPT if think_in_prompt and reasons_in_prompt(model_id, model_provider) else system_prompt, 'tools': tools, 'name': name, 'permissions': permissions, 'checkpointer': checkpointer}; source annotation dict[str, Any].
  // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:417-418
  if (the source predicate skills is not None is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:418-418
    In source order: Evaluate once skills; assign in source target order to kwargs['skills'].
  }
  // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:420-421
  In source order: For extra, assign extra_excluded_tools or frozenset(); source annotation frozenset[str]. Then For middleware, declare without assigning a value; source annotation list[AgentMiddleware].
  // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:422-428
  if (the source predicate redact_reads is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:423-423
    In source order: Evaluate once [*read_only_middleware(extra), *parent_middleware]; assign in source target order to middleware.
  }
  else {
    // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:425-428
    In source order: Evaluate once [ExcludeTools(frozenset({DELETE_TOOL_NAME}) | extra), *parent_middleware]; assign in source target order to middleware.
  }
  // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:430-431
  In source order: Evaluate middleware.append(RepairInvalidToolArgs()); retain side effects and discard the expression result. Then Evaluate middleware.append(LogInvalidRequestShape(tag=name)); retain side effects and discard the expression result.
  // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:433-434
  if (the source predicate max_output_tokens is not None is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:434-434
    In source order: Evaluate middleware.append(CapOutputTokens(max_output_tokens, tag=name, cap=output_cap)); retain side effects and discard the expression result.
  }
  // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:436-437
  if (the source predicate permitted_tool_calls is not None is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:437-437
    In source order: Evaluate middleware.append(PermitTools(permitted_tool_calls)); retain side effects and discard the expression result.
  }
  // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:439-443
  In source order: Evaluate middleware.append(BlockMarkerPromptCaching(enabled=cache_markers, mark_tail=cache_tail)); retain side effects and discard the expression result. Then Evaluate middleware.append(LogToolCalls(tag=name)); retain side effects and discard the expression result.
  // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:447-448
  if (the source predicate not name.startswith('preflight') is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:448-448
    In source order: Evaluate middleware.append(_CONNECTION_RETRY_MIDDLEWARE); retain side effects and discard the expression result.
  }
  // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:449-449
  In source order: Evaluate once middleware; assign in source target order to kwargs['middleware'].
  // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:450-451
  if (the source predicate response_format is not None is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:451-451
    In source order: Evaluate once response_format; assign in source target order to kwargs['response_format'].
  }
  // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:452-453
  if (the source predicate subagents is not None is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:453-453
    In source order: Evaluate once subagents; assign in source target order to kwargs['subagents'].
  }
  // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:454-455
  if (the source predicate backend is not None is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:455-455
    In source order: Evaluate once backend; assign in source target order to kwargs['backend'].
  }
  // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:457-458
  Enter source context managers left-to-right: _BUILD_LOCK; _restaged_harness_profiles(name, blank=strip_harness_suffix) {
    // Source: vvaharness/backends/harness/deepagents/options/graph_builder.py:458-458
    End this invocation with create_deep_agent(**kwargs).
  }
  Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.backends.harness.deepagents.exclude_tools import ExcludeTools` at source line 45: `source_detail/vvaharness/backends/harness/deepagents/exclude_tools.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.invalid_tool_args import RepairInvalidToolArgs` at source line 46: `source_detail/vvaharness/backends/harness/deepagents/invalid_tool_args.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.limits import MODEL_MAX_OUTPUT_TOKENS` at source line 47: `source_detail/vvaharness/backends/harness/deepagents/limits.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.models import DELETE_TOOL_NAME, SubagentSpec` at source line 48: `source_detail/vvaharness/backends/harness/deepagents/models.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.options.model_building import REASON_IN_PROMPT, build_model_cached, reasons_in_prompt` at source line 49: `source_detail/vvaharness/backends/harness/deepagents/options/model_building.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.options.response_format import submit_instructed_prompt` at source line 54: `source_detail/vvaharness/backends/harness/deepagents/options/response_format.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.permit_tools import PermitTools` at source line 55: `source_detail/vvaharness/backends/harness/deepagents/permit_tools.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.profiles import register_vvah_harness_profiles, stage_profile_suffix` at source line 56: `source_detail/vvaharness/backends/harness/deepagents/profiles.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.prompt_caching import BlockMarkerPromptCaching` at source line 60: `source_detail/vvaharness/backends/harness/deepagents/prompt_caching.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.redaction import read_only_middleware` at source line 61: `source_detail/vvaharness/backends/harness/deepagents/redaction.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.translate import reply_truncated` at source line 62: `source_detail/vvaharness/backends/harness/deepagents/translate.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.usage import SessionUsage, aggregate_usage_metadata` at source line 63: `source_detail/vvaharness/backends/harness/deepagents/usage.py.sudo.md`.
- `from vvaharness.backends.harness.models import TruncatedResponseError` at source line 64: `source_detail/vvaharness/backends/harness/models.py.sudo.md`.
- `from vvaharness.backends.llm.models import TRUNCATED_RETRY_ATTEMPTED_COUNTER, TRUNCATED_RETRY_RECOVERED_COUNTER, proxy_detail, truncation_retry_max` at source line 65: `source_detail/vvaharness/backends/llm/models.py.sudo.md`.
- `from vvaharness.backends.llm.openai import _payload_shape` at source line 71: `source_detail/vvaharness/backends/llm/openai.py.sudo.md`.
- `from vvaharness.util import console, logs` at source line 72: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import console, logs` at source line 72: `source_detail/vvaharness/util/console.py.sudo.md`.
- `from vvaharness.util import console, logs` at source line 72: `source_detail/vvaharness/util/logs.py.sudo.md`.
- `from vvaharness.util import errlog as _errlog` at source line 73: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import errlog as _errlog` at source line 73: `source_detail/vvaharness/util/errlog.py.sudo.md`.
- `from vvaharness.util.counters import COUNTERS` at source line 74: `source_detail/vvaharness/util/counters.py.sudo.md`.
- `from vvaharness.util.events import Event` at source line 75: `source_detail/vvaharness/util/events.py.sudo.md`.
- `from vvaharness.util.response_quality import is_connection_failure` at source line 76: `source_detail/vvaharness/util/response_quality.py.sudo.md`.
- `from vvaharness.util.scan_progress import is_stage_only` at source line 77: `source_detail/vvaharness/util/scan_progress.py.sudo.md`.
- `from vvaharness.util.tokens import TOKENS` at source line 78: `source_detail/vvaharness/util/tokens.py.sudo.md`.
