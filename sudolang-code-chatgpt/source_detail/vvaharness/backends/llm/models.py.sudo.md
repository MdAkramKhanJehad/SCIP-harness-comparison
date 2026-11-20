# vvaharness/backends/llm/models.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/backends/llm/models.py.evidence.json`. SHA-256: `2edcaf0c818815ab6354cd4695cb436217c3db9252f0f3c60d4ea17524e8fb47`.

```sudo
// Source: vvaharness/backends/llm/models.py:15-23
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import random; preserve alias and import-time effects. Then Resolve source import import re; preserve alias and import-time effects. Then Resolve source import import threading; preserve alias and import-time effects.
// Source: vvaharness/backends/llm/models.py:24-28
In source order: Resolve source import import time; preserve alias and import-time effects. Then Resolve source import from collections.abc import Mapping, Sequence; preserve alias and import-time effects. Then Resolve source import from enum import StrEnum; preserve alias and import-time effects. Then Resolve source import from math import ceil; preserve alias and import-time effects. Then Resolve source import from typing import Any, Final, NamedTuple, NewType, Protocol, TypedDict, runtime_checkable; preserve alias and import-time effects.
// Source: vvaharness/backends/llm/models.py:30-37
In source order: Resolve source import from vvaharness.backends.harness.models import CallTimeoutError, EffortLevel, ProxyError; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.provider_routing import TRANSPORT_CHAT_COMPLETIONS, TRANSPORT_RESPONSES; preserve alias and import-time effects. Then Resolve source import from vvaharness.report.redact import redact; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.config import knob; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.counters import COUNTERS; preserve alias and import-time effects.
// Source: vvaharness/backends/llm/models.py:38-48
In source order: Resolve source import from vvaharness.util.exceptions import exception_chain; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.tokens import TokenUsage; preserve alias and import-time effects. Then Evaluate once NewType('ModulePath', str); assign in source target order to ModulePath. Then For RETRYABLE_STATUS, assign frozenset({429, 500, 502, 503, 504, 529}); source annotation Final[frozenset[int]]. Then For CLI_RETRYABLE_STATUS, assign RETRYABLE_STATUS - {500, 504}; source annotation Final[frozenset[int]].
// Source: vvaharness/backends/llm/models.py:52-56
In source order: For SERVER_ERROR_STATUS, assign RETRYABLE_STATUS - {429}; source annotation Final[frozenset[int]]. Then For PARAM_REJECTION_STATUS, assign frozenset({400, 422}); source annotation Final[frozenset[int]].
// Source: vvaharness/backends/llm/models.py:59-73
// Source signature: rejection_text(exc: BaseException) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn rejection_text(exc) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/models.py:60-62
  In source order: Retain source documentation literal source_literal_60_4; it is not a model call. Then Evaluate once getattr(exc, 'body', None); assign in source target order to body. Then Evaluate once body.get('detail') if isinstance(body, dict) else None; assign in source target order to detail.
  // Source: vvaharness/backends/llm/models.py:63-64
  if (the source predicate not isinstance(detail, list) is truthy) {
    // Source: vvaharness/backends/llm/models.py:64-64
    End this invocation with str(getattr(exc, 'message', None) or exc).
  }
  // Source: vvaharness/backends/llm/models.py:66-66
  In source order: For parts, assign []; source annotation list[str].
  // Source: vvaharness/backends/llm/models.py:67-72
  for each entry in detail {
    // Source: vvaharness/backends/llm/models.py:68-71
    if (the source predicate isinstance(entry, dict) is truthy) {
      // Source: vvaharness/backends/llm/models.py:69-69
      In source order: Evaluate once {k: v for k, v in entry.items() if k != 'input'}; assign in source target order to entry.
      // Source: vvaharness/backends/llm/models.py:70-71
      if (the source predicate isinstance(entry.get('loc'), list) is truthy) {
        // Source: vvaharness/backends/llm/models.py:71-71
        In source order: Evaluate once '.'.join(map(str, entry['loc'])); assign in source target order to entry['loc'].
      }
    }
    // Source: vvaharness/backends/llm/models.py:72-72
    In source order: Evaluate parts.append(str(entry)); retain side effects and discard the expression result.
  }
  // Source: vvaharness/backends/llm/models.py:73-73
  End this invocation with '; '.join(parts).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/models.py:76-83
// Source signature: is_param_rejection(exc: BaseException, *names: str) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn is_param_rejection(exc, names) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/models.py:77-77
  In source order: Retain source documentation literal source_literal_77_4; it is not a model call.
  // Source: vvaharness/backends/llm/models.py:78-82
  for each link in exception_chain(exc) {
    // Source: vvaharness/backends/llm/models.py:79-82
    if (the source predicate getattr(link, 'status_code', None) in PARAM_REJECTION_STATUS is truthy) {
      // Source: vvaharness/backends/llm/models.py:80-80
      In source order: Evaluate once rejection_text(link).lower(); assign in source target order to low.
      // Source: vvaharness/backends/llm/models.py:81-82
      if (the source predicate any((name in low for name in names)) is truthy) {
        // Source: vvaharness/backends/llm/models.py:82-82
        End this invocation with True.
      }
    }
  }
  // Source: vvaharness/backends/llm/models.py:83-83
  End this invocation with False.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/models.py:88-89
In source order: For PARAM_REJECTION_ERROR_TYPES, assign frozenset({'invalid_request_error', 'bad_request_error'}); source annotation Final[frozenset[str]].
// Source: vvaharness/backends/llm/models.py:92-100
// Source signature: is_gateway_wrapped_param_rejection(exc: BaseException) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn is_gateway_wrapped_param_rejection(exc) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/models.py:93-98
  In source order: Retain source documentation literal source_literal_93_4; it is not a model call.
  // Source: vvaharness/backends/llm/models.py:99-100
  End this invocation with getattr(exc, 'status_code', None) == 200 and getattr(exc, 'type', None) in PARAM_REJECTION_ERROR_TYPES.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/models.py:104-128
In source order: For RATE_LIMIT_TRANSIENT_RX, assign re.compile('rate.?limit|too many requests|overloaded|temporarily unavailable', re.IGNORECASE); source annotation Final[re.Pattern[str]]. Then For CLI_STATUS_429_RX, assign re.compile('\\b429\\b'); source annotation Final[re.Pattern[str]]. Then For SERVER_ERROR_TRANSIENT_RX, assign re.compile(source_literal_114_4, re.I); source annotation Final[re.Pattern[str]]. Then For CLI_CONN_TRANSIENT_RX, assign re.compile(source_literal_121_4, re.IGNORECASE); source annotation Final[re.Pattern[str]]. Then For DEFAULT_READ_TOOLS, assign ('Read', 'Glob', 'Grep'); source annotation Final[tuple[str, ...]].
// Source: vvaharness/backends/llm/models.py:131-144
In source order: For AGENTIC_MAX_TOKENS, assign 16000; source annotation Final. Then For RESPONSE_MODEL_VIAS, assign frozenset({'deepagents', 'sdk', 'openai', 'cli'}); source annotation Final[frozenset[str]]. Then For RESPONSE_MODEL_TOOL_NAME, assign 'emit_structured_response'; source annotation Final. Then For STRUCTURED_REASK_MAX, assign 2; source annotation Final. Then For CLI_STRUCTURED_OUTPUT_TOOL, assign 'StructuredOutput'; source annotation Final.
// Source: vvaharness/backends/llm/models.py:147-155
// Source signature: response_model_tool(response_model: type) -> dict
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn response_model_tool(response_model) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/models.py:148-150
  In source order: Retain source documentation literal source_literal_148_4; it is not a model call. Then Evaluate once response_model.model_json_schema(); assign in source target order to schema. Then Evaluate schema.pop('title', None); retain side effects and discard the expression result.
  // Source: vvaharness/backends/llm/models.py:151-155
  End this invocation with {'name': RESPONSE_MODEL_TOOL_NAME, 'description': source_template_153_23, 'input_schema': schema}.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/models.py:160-162
In source order: For STRUCTURED_PROSE_REASK, assign source_template_161_4; source annotation Final.
// Source: vvaharness/backends/llm/models.py:165-174
// Source signature: with_submit_instruction(system_prompt: str | None, response_model: type, *, tool_name: str=RESPONSE_MODEL_TOOL_NAME) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn with_submit_instruction(system_prompt, response_model, tool_name) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/models.py:167-173
  In source order: Retain source documentation literal source_literal_167_4; it is not a model call. Then Evaluate once source_template_172_12; assign in source target order to line.
  // Source: vvaharness/backends/llm/models.py:174-174
  End this invocation with source_template_174_11 if system_prompt else line.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/models.py:178-190
In source order: For DEEPAGENTS_MAX_PROMPT_TOKENS, assign 150000; source annotation Final. Then For TRUNCATION_RETRY_MULTIPLIER, assign 2; source annotation Final. Then For TRUNCATED_REPLIES_COUNTER, assign 'llm_truncated_replies'; source annotation Final. Then For LLM_TRUNCATED_BELOW_BUDGET_COUNTER, assign 'llm_truncated_below_budget'; source annotation Final. Then For TRUNCATED_RETRY_ATTEMPTED_COUNTER, assign 'llm_truncated_retry_attempted'; source annotation Final.
// Source: vvaharness/backends/llm/models.py:191-203
In source order: For TRUNCATED_RETRY_RECOVERED_COUNTER, assign 'llm_truncated_retry_recovered'; source annotation Final. Then For OPENAI_FINISH_LENGTH, assign 'length'; source annotation Final. Then For ANTHROPIC_STOP_MAX_TOKENS, assign 'max_tokens'; source annotation Final. Then For ANTHROPIC_STOP_CONTEXT_WINDOW, assign 'model_context_window_exceeded'; source annotation Final. Then For ANTHROPIC_STOP_REFUSAL, assign 'refusal'; source annotation Final.
// Source: vvaharness/backends/llm/models.py:206-210
In source order: For RESPONSES_INCOMPLETE_MAX_OUTPUT, assign 'max_output_tokens'; source annotation Final. Then For _TRUNCATED_FINISHES, assign frozenset({ANTHROPIC_STOP_MAX_TOKENS, ANTHROPIC_STOP_CONTEXT_WINDOW, OPENAI_FINISH_LENGTH, RESPONSES_INCOMPLETE_MAX_OUTPUT}); source annotation Final.
// Source: vvaharness/backends/llm/models.py:213-217
// Source signature: reply_finish(meta: Mapping[str, Any]) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn reply_finish(meta) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/models.py:214-215
  In source order: Retain source documentation literal source_literal_214_4; it is not a model call. Then Evaluate once meta.get('incomplete_details'); assign in source target order to details.
  // Source: vvaharness/backends/llm/models.py:216-217
  End this invocation with meta.get('stop_reason') or meta.get('finish_reason') or (details.get('reason') if isinstance(details, Mapping) else None).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/models.py:220-223
// Source signature: finish_truncated(finish: object | None) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn finish_truncated(finish) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/models.py:221-221
  In source order: Retain source documentation literal source_literal_221_4; it is not a model call.
  // Source: vvaharness/backends/llm/models.py:223-223
  End this invocation with isinstance(finish, str) and finish in _TRUNCATED_FINISHES.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/models.py:226-230
In source order: For CLI_TOKEN_CAP_RX, assign re.compile('exceeded the (\\d+) output token maximum', re.IGNORECASE); source annotation Final[re.Pattern[str]]. Then For CLI_CONTINUED_REPLIES_COUNTER, assign 'cli_continued_replies'; source annotation Final.
// Source: vvaharness/backends/llm/models.py:233-238
// Source signature: truncation_retry_max(requested: int, cap: int | None=None) -> int | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn truncation_retry_max(requested, cap) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/models.py:234-234
  In source order: Retain source documentation literal source_literal_234_4; it is not a model call.
  // Source: vvaharness/backends/llm/models.py:235-236
  if (the source predicate cap is not None and requested >= cap is truthy) {
    // Source: vvaharness/backends/llm/models.py:236-236
    End this invocation with None.
  }
  // Source: vvaharness/backends/llm/models.py:237-237
  In source order: Evaluate once requested * TRUNCATION_RETRY_MULTIPLIER; assign in source target order to doubled.
  // Source: vvaharness/backends/llm/models.py:238-238
  End this invocation with doubled if cap is None else min(doubled, cap).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/models.py:242-242
In source order: For RETRY_JITTER_SPREAD, assign 0.2; source annotation Final.
// Source: vvaharness/backends/llm/models.py:245-251
// Source signature: jittered_delay(seconds: float, *, spread: float=RETRY_JITTER_SPREAD, rng: random.Random | None=None) -> float
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn jittered_delay(seconds, spread, rng) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/models.py:247-250
  In source order: Retain source documentation literal source_literal_247_4; it is not a model call. Then Evaluate once rng if rng is not None else random; assign in source target order to r. Then Evaluate once 1.0 + r.uniform(-spread, spread); assign in source target order to factor.
  // Source: vvaharness/backends/llm/models.py:251-251
  End this invocation with max(0.0, seconds * factor).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/models.py:254-258
interface ClockKind {
  Describe the source Python type, preserving its base/metaclass expression order: StrEnum.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/llm/models.py:255-258
  In source order: Retain source documentation literal source_literal_255_4; it is not a model call. Then Evaluate once 'request'; assign in source target order to REQUEST. Then Evaluate once 'session'; assign in source target order to SESSION.
}
// Source: vvaharness/backends/llm/models.py:263-272
In source order: For EFFORT_TIME_FACTOR, assign {ClockKind.REQUEST: {EffortLevel.LOW: 1.0, EffortLevel.MEDIUM: 1.0, EffortLevel.HIGH: 1.0, EffortLevel.XHIGH: 1.1, EffortLevel.MAX: 1.2}, ClockKind.SESSION: {EffortLevel.LOW: 1.0, EffortLevel.MEDIUM: 1.0, EffortLevel.HIGH: 1.0, EffortLevel.XHIGH: 1.1, EffortLevel.MAX: 1.5}}; source annotation Final[dict[ClockKind, dict[EffortLevel, float]]].
// Source: vvaharness/backends/llm/models.py:275-285
// Source signature: effort_scaled_seconds(seconds: int | float | None, effort: str | None, *, kind: ClockKind) -> int | float | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn effort_scaled_seconds(seconds, effort, kind) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/models.py:277-277
  In source order: Retain source documentation literal source_literal_277_4; it is not a model call.
  // Source: vvaharness/backends/llm/models.py:279-280
  if (the source predicate seconds is None or seconds <= 0 is truthy) {
    // Source: vvaharness/backends/llm/models.py:280-280
    End this invocation with seconds.
  }
  // Source: vvaharness/backends/llm/models.py:281-281
  In source order: Evaluate once EffortLevel.parse(effort); assign in source target order to tier.
  // Source: vvaharness/backends/llm/models.py:282-283
  if (the source predicate tier is None is truthy) {
    // Source: vvaharness/backends/llm/models.py:283-283
    End this invocation with seconds.
  }
  // Source: vvaharness/backends/llm/models.py:284-284
  In source order: Evaluate once seconds * EFFORT_TIME_FACTOR[kind][tier]; assign in source target order to scaled.
  // Source: vvaharness/backends/llm/models.py:285-285
  End this invocation with ceil(scaled) if isinstance(seconds, int) else scaled.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/models.py:289-301
In source order: For DEFAULT_REQUEST_TIMEOUT_SECONDS, assign 900; source annotation Final. Then For TIMEOUT_STOP_GRACE_SECONDS, assign 20; source annotation Final. Then For TIMEOUT_MAX_RETRIES, assign 1; source annotation Final. Then For BUDGET_NEAR_RATIO, assign 0.75; source annotation Final. Then For LLM_CALL_TIMEOUTS_COUNTER, assign 'llm_call_timeouts'; source annotation Final.
// Source: vvaharness/backends/llm/models.py:304-317
In source order: For LLM_CALL_BUDGET_NEAR_COUNTER, assign 'llm_call_budget_near'; source annotation Final. Then For _BUDGET_NEAR_TIERS, assign frozenset({EffortLevel.XHIGH, EffortLevel.MAX}); source annotation Final[frozenset[EffortLevel]]. Then For PROXY_CAUSE_RX, assign re.compile(source_literal_313_4, re.IGNORECASE); source annotation Final.
// Source: vvaharness/backends/llm/models.py:320-322
// Source signature: cause_chain(e: BaseException) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn cause_chain(e) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/models.py:321-321
  In source order: Retain source documentation literal source_literal_321_4; it is not a model call.
  // Source: vvaharness/backends/llm/models.py:322-322
  End this invocation with ' <- '.join((source_template_322_23 for c in exception_chain(e)[1:])).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/models.py:325-330
// Source signature: proxy_detail(e: BaseException) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn proxy_detail(e) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/models.py:326-327
  In source order: Retain source documentation literal source_literal_326_4; it is not a model call. Then Evaluate once cause_chain(e); assign in source target order to detail.
  // Source: vvaharness/backends/llm/models.py:328-329
  if (the source predicate PROXY_CAUSE_RX.search(detail) or PROXY_CAUSE_RX.search(str(e)) is truthy) {
    // Source: vvaharness/backends/llm/models.py:329-329
    End this invocation with detail or str(e).
  }
  // Source: vvaharness/backends/llm/models.py:330-330
  End this invocation with None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/models.py:333-339
// Source signature: proxy_error(e: BaseException, *, backend: str) -> ProxyError | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn proxy_error(e, backend) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/models.py:334-335
  In source order: Retain source documentation literal source_literal_334_4; it is not a model call. Then Evaluate once proxy_detail(e); assign in source target order to detail.
  // Source: vvaharness/backends/llm/models.py:336-337
  if (the source predicate detail is None is truthy) {
    // Source: vvaharness/backends/llm/models.py:337-337
    End this invocation with None.
  }
  // Source: vvaharness/backends/llm/models.py:338-339
  End this invocation with ProxyError(redact(detail)[:400], status_code=407 if re.search('\\b407\\b', detail) else None, backend=backend).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/models.py:342-346
// Source signature: call_timeout_error(*, stage: str, route: str, budget_s: float | None, effort: str | None, cause_text: str) -> CallTimeoutError
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn call_timeout_error(stage, route, budget_s, effort, cause_text) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/models.py:344-345
  In source order: Retain source documentation literal source_literal_344_4; it is not a model call. Then Evaluate COUNTERS.bump(LLM_CALL_TIMEOUTS_COUNTER); retain side effects and discard the expression result.
  // Source: vvaharness/backends/llm/models.py:346-346
  End this invocation with CallTimeoutError(cause_text, stage=stage, route=route, budget_s=budget_s, effort=effort).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/models.py:349-356
// Source signature: note_budget_use(elapsed: float, budget_s: float | None, effort: str | None) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn note_budget_use(elapsed, budget_s, effort) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/models.py:350-350
  In source order: Retain source documentation literal source_literal_350_4; it is not a model call.
  // Source: vvaharness/backends/llm/models.py:351-352
  if (the source predicate not budget_s or budget_s <= 0 is truthy) {
    // Source: vvaharness/backends/llm/models.py:352-352
    End this invocation with None.
  }
  // Source: vvaharness/backends/llm/models.py:353-354
  if (the source predicate EffortLevel.parse(effort) not in _BUDGET_NEAR_TIERS is truthy) {
    // Source: vvaharness/backends/llm/models.py:354-354
    End this invocation with None.
  }
  // Source: vvaharness/backends/llm/models.py:355-356
  if (the source predicate elapsed >= BUDGET_NEAR_RATIO * budget_s is truthy) {
    // Source: vvaharness/backends/llm/models.py:356-356
    In source order: Evaluate COUNTERS.bump(LLM_CALL_BUDGET_NEAR_COUNTER); retain side effects and discard the expression result.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/models.py:359-379
// Source signature: _named_tools(tools: Sequence[str] | None, *, config_key: str) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _named_tools(tools, config_key) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/models.py:360-360
  In source order: Retain source documentation literal source_literal_360_4; it is not a model call.
  // Source: vvaharness/backends/llm/models.py:362-363
  if (the source predicate tools is None is truthy) {
    // Source: vvaharness/backends/llm/models.py:363-363
    End this invocation with list(DEFAULT_READ_TOOLS).
  }
  // Source: vvaharness/backends/llm/models.py:364-368
  if (the source predicate isinstance(tools, str) is truthy) {
    // Source: vvaharness/backends/llm/models.py:366-368
    Raise ValueError(source_template_367_12).
  }
  // Source: vvaharness/backends/llm/models.py:369-369
  In source order: Evaluate once list(tools); assign in source target order to named.
  // Source: vvaharness/backends/llm/models.py:370-374
  if (the source predicate not named is truthy) {
    // Source: vvaharness/backends/llm/models.py:371-374
    Raise ValueError(source_template_372_12).
  }
  // Source: vvaharness/backends/llm/models.py:375-378
  if (the source predicate any((not isinstance(t, str) for t in named)) is truthy) {
    // Source: vvaharness/backends/llm/models.py:376-378
    Raise ValueError(source_template_377_12).
  }
  // Source: vvaharness/backends/llm/models.py:379-379
  End this invocation with named.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/models.py:382-400
// Source signature: validate_detection_tools(tools: Sequence[str] | None, *, config_key: str, via: str | None=None) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn validate_detection_tools(tools, config_key, via) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/models.py:385-387
  In source order: Retain source documentation literal source_literal_385_4; it is not a model call. Then Evaluate once _named_tools(tools, config_key=config_key); assign in source target order to named.
  // Source: vvaharness/backends/llm/models.py:388-389
  if (the source predicate via == 'cli' is truthy) {
    // Source: vvaharness/backends/llm/models.py:389-389
    End this invocation with named.
  }
  // Source: vvaharness/backends/llm/models.py:390-390
  In source order: Evaluate once sorted((t for t in named if t not in DEFAULT_READ_TOOLS)); assign in source target order to bad.
  // Source: vvaharness/backends/llm/models.py:391-399
  if (the source predicate bad is truthy) {
    // Source: vvaharness/backends/llm/models.py:392-399
    Raise ValueError(source_template_393_12).
  }
  // Source: vvaharness/backends/llm/models.py:400-400
  End this invocation with named.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/models.py:403-408
interface ModelExtras {
  Describe the source Python type, preserving its base/metaclass expression order: TypedDict, total=False.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/llm/models.py:404-408
  In source order: Retain source documentation literal source_literal_404_4; it is not a model call. Then For temperature, declare without assigning a value; source annotation float. Then For thinking_budget, declare without assigning a value; source annotation int. Then For betas, declare without assigning a value; source annotation list[str].
}
// Source: vvaharness/backends/llm/models.py:411-416
interface ResolvedModel {
  Describe the source Python type, preserving its base/metaclass expression order: NamedTuple.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/llm/models.py:412-416
  In source order: Retain source documentation literal source_literal_412_4; it is not a model call. Then For model_id, declare without assigning a value; source annotation str. Then For via, declare without assigning a value; source annotation str. Then For extras, declare without assigning a value; source annotation ModelExtras.
}
// Source: vvaharness/backends/llm/models.py:419-429
interface EnvelopeResult {
  Describe the source Python type, preserving its base/metaclass expression order: NamedTuple.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/llm/models.py:420-426
  In source order: Retain source documentation literal source_literal_420_4; it is not a model call. Then For text, declare without assigning a value; source annotation str. Then For usage, declare without assigning a value; source annotation TokenUsage | None. Then For turns, assign None; source annotation int | None. Then For usd, assign None; source annotation float | None.
  // Source: vvaharness/backends/llm/models.py:427-429
  In source order: For stop_reason, assign None; source annotation str | None. Then For model_usage, assign None; source annotation dict | None.
}
// Source: vvaharness/backends/llm/models.py:433-433
In source order: Evaluate once bool | str; assign in source target order to VerifySsl.
// Source: vvaharness/backends/llm/models.py:436-445
interface CliConfig {
  Describe the source Python type, preserving its base/metaclass expression order: TypedDict.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/llm/models.py:437-442
  In source order: Retain source documentation literal source_literal_437_4; it is not a model call. Then For verify_ssl, declare without assigning a value; source annotation VerifySsl. Then For ca_cert, declare without assigning a value; source annotation str | None. Then For client_cert, declare without assigning a value; source annotation str | tuple[str, str] | None. Then For no_proxy, declare without assigning a value; source annotation str | None.
  // Source: vvaharness/backends/llm/models.py:443-445
  In source order: For effort, declare without assigning a value; source annotation str. Then For restricted, declare without assigning a value; source annotation bool.
}
// Source: vvaharness/backends/llm/models.py:448-461
interface SdkConfig {
  Describe the source Python type, preserving its base/metaclass expression order: TypedDict.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/llm/models.py:449-454
  In source order: Retain source documentation literal source_literal_449_4; it is not a model call. Then For api_key, declare without assigning a value; source annotation str | None. Then For base_url, declare without assigning a value; source annotation str | None. Then For verify_ssl, declare without assigning a value; source annotation VerifySsl. Then For ca_cert, declare without assigning a value; source annotation str | None.
  // Source: vvaharness/backends/llm/models.py:455-460
  In source order: For client_cert, declare without assigning a value; source annotation str | tuple[str, str] | None. Then For no_proxy, declare without assigning a value; source annotation str | None. Then For allow_api_key_fallback, declare without assigning a value; source annotation bool. Then For cache_min_block_tokens, declare without assigning a value; source annotation int | None. Then For cache_route, declare without assigning a value; source annotation str.
  // Source: vvaharness/backends/llm/models.py:461-461
  In source order: For cache_markers, declare without assigning a value; source annotation str | bool.
}
// Source: vvaharness/backends/llm/models.py:464-475
interface OpenAiConfig {
  Describe the source Python type, preserving its base/metaclass expression order: TypedDict.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/llm/models.py:465-470
  In source order: Retain source documentation literal source_literal_465_4; it is not a model call. Then For api_key, declare without assigning a value; source annotation str | None. Then For base_url, declare without assigning a value; source annotation str | None. Then For verify_ssl, declare without assigning a value; source annotation VerifySsl. Then For ca_cert, declare without assigning a value; source annotation str | None.
  // Source: vvaharness/backends/llm/models.py:472-475
  In source order: For organization, declare without assigning a value; source annotation str | None. Then For no_proxy, declare without assigning a value; source annotation str | None. Then For cache_markers, declare without assigning a value; source annotation str | bool.
}
// Source: vvaharness/backends/llm/models.py:478-479
interface GuardrailBlocked {
  Describe the source Python type, preserving its base/metaclass expression order: RuntimeError.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/llm/models.py:479-479
  In source order: Retain source documentation literal source_literal_479_4; it is not a model call.
}
// Source: vvaharness/backends/llm/models.py:482-491
interface ModelRefusal {
  Describe the source Python type, preserving its base/metaclass expression order: GuardrailBlocked.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/llm/models.py:483-483
  In source order: Retain source documentation literal source_literal_483_4; it is not a model call.
  // Source: vvaharness/backends/llm/models.py:486-491
  // Source signature: __init__(self, message: str='', *, route: str='', category: str | None=None) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self, message, route, category) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/llm/models.py:488-491
    In source order: Retain source documentation literal source_literal_488_8; it is not a model call. Then Evaluate super().__init__(message); retain side effects and discard the expression result. Then Evaluate once route; assign in source target order to self.route. Then Evaluate once category; assign in source target order to self.category.
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vvaharness/backends/llm/models.py:494-499
// Source signature: guardrail_gate_hit(e: GuardrailBlocked, hits: int, gate: int) -> tuple[int, str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn guardrail_gate_hit(e, hits, gate) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/models.py:495-495
  In source order: Retain source documentation literal source_literal_495_4; it is not a model call.
  // Source: vvaharness/backends/llm/models.py:497-498
  if (the source predicate isinstance(e, ModelRefusal) is truthy) {
    // Source: vvaharness/backends/llm/models.py:498-498
    End this invocation with (hits, 'model refusal, not gated').
  }
  // Source: vvaharness/backends/llm/models.py:499-499
  End this invocation with (hits + 1, source_template_499_21).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/models.py:503-507
In source order: For LLM_MODEL_REFUSALS_COUNTER, assign 'llm_model_refusals'; source annotation Final. Then For REFUSAL_RETRY_ATTEMPTED_COUNTER, assign 'llm_refusal_retry_attempted'; source annotation Final. Then For REFUSAL_RETRY_RECOVERED_COUNTER, assign 'llm_refusal_retry_recovered'; source annotation Final.
// Source: vvaharness/backends/llm/models.py:510-523
// Source signature: refusal_resend_allowed(cfg: object, model_cfg: object) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn refusal_resend_allowed(cfg, model_cfg) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/models.py:511-511
  In source order: Retain source documentation literal source_literal_511_4; it is not a model call.
  // Source: vvaharness/backends/llm/models.py:514-515
  if (the source predicate int(knob(cfg, 'refusal_retries', 1)) <= 0 is truthy) {
    // Source: vvaharness/backends/llm/models.py:515-515
    End this invocation with False.
  }
  // Source: vvaharness/backends/llm/models.py:516-522
  In source order: Resolve source import from vvaharness.backends.llm.registry import provider_of, resolve; preserve alias and import-time effects. Then Resolve source import from vvaharness.manifest import _resolved_route; preserve alias and import-time effects. Then Evaluate once resolve(model_cfg); assign in source target order to (model_id, via, _).
  // Source: vvaharness/backends/llm/models.py:523-523
  End this invocation with _resolved_route(via, model_id, provider_of(model_cfg)) == 'anthropic'.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/models.py:527-531
In source order: For _CYBER_POLICY_REJECTION_RX, assign re.compile('\\bcyber_policy\\b|flagged for possible cybersecurity risk', re.IGNORECASE); source annotation Final[re.Pattern[str]]. Then For _CYBER_POLICY_CATEGORY, assign 'cyber'; source annotation Final.
// Source: vvaharness/backends/llm/models.py:534-543
// Source signature: model_refusal(*, route: str, stage: str, category: str | None, detail: str='') -> ModelRefusal
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn model_refusal(route, stage, category, detail) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/models.py:536-540
  In source order: Retain source documentation literal source_literal_536_4; it is not a model call. Then Evaluate COUNTERS.bump(LLM_MODEL_REFUSALS_COUNTER); retain side effects and discard the expression result. Then Evaluate once source_template_538_12 if stage else ''; assign in source target order to where. Then Evaluate once source_template_540_11 if detail else ''; assign in source target order to tail.
  // Source: vvaharness/backends/llm/models.py:541-543
  End this invocation with ModelRefusal(source_template_542_8, route=route, category=category).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/models.py:546-548
// Source signature: _get(obj: object, key: str) -> object
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _get(obj, key) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/models.py:547-547
  In source order: Retain source documentation literal source_literal_547_4; it is not a model call.
  // Source: vvaharness/backends/llm/models.py:548-548
  End this invocation with obj.get(key) if isinstance(obj, Mapping) else getattr(obj, key, None).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/models.py:551-555
// Source signature: refusal_category(meta: Mapping[str, Any]) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn refusal_category(meta) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/models.py:552-554
  In source order: Retain source documentation literal source_literal_552_4; it is not a model call. Then Evaluate once _get(meta.get('stop_details'), 'category'); assign in source target order to category.
  // Source: vvaharness/backends/llm/models.py:555-555
  End this invocation with category if isinstance(category, str) else None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/models.py:558-564
// Source signature: ai_message_refused(message: object) -> tuple[bool, str | None]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn ai_message_refused(message) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/models.py:559-561
  In source order: Retain source documentation literal source_literal_559_4; it is not a model call. Then Evaluate once getattr(message, 'response_metadata', None); assign in source target order to meta.
  // Source: vvaharness/backends/llm/models.py:562-563
  if (the source predicate isinstance(meta, Mapping) and meta.get('stop_reason') == ANTHROPIC_STOP_REFUSAL is truthy) {
    // Source: vvaharness/backends/llm/models.py:563-563
    End this invocation with (True, refusal_category(meta)).
  }
  // Source: vvaharness/backends/llm/models.py:564-564
  End this invocation with (_openai_refused(message), None).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/models.py:567-574
// Source signature: _openai_refused(message: object) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _openai_refused(message) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/models.py:568-570
  In source order: Retain source documentation literal source_literal_568_4; it is not a model call. Then Evaluate once getattr(message, 'additional_kwargs', None); assign in source target order to extra. Then Evaluate once getattr(message, 'content', None); assign in source target order to content.
  // Source: vvaharness/backends/llm/models.py:571-574
  End this invocation with bool(isinstance(extra, Mapping) and extra.get('refusal') or (isinstance(content, list) and any((isinstance(b, Mapping) and b.get('type') == 'refusal' for b in content)))).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/models.py:577-588
// Source signature: _refusal_link(exc: BaseException) -> tuple[BaseException, str | None] | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _refusal_link(exc) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/models.py:578-578
  In source order: Retain source documentation literal source_literal_578_4; it is not a model call.
  // Source: vvaharness/backends/llm/models.py:579-587
  for each link in exception_chain(exc) {
    // Source: vvaharness/backends/llm/models.py:581-582
    In source order: Evaluate once getattr(link, 'status_code', None) is not None or getattr(link, 'body', None) is not None; assign in source target order to api_link.
    // Source: vvaharness/backends/llm/models.py:583-584
    if (the source predicate api_link and _CYBER_POLICY_REJECTION_RX.search(rejection_text(link)) is truthy) {
      // Source: vvaharness/backends/llm/models.py:584-584
      End this invocation with (link, _CYBER_POLICY_CATEGORY).
    }
    // Source: vvaharness/backends/llm/models.py:585-585
    In source order: Evaluate once ai_message_refused(getattr(link, 'ai_message', None)); assign in source target order to (refused, category).
    // Source: vvaharness/backends/llm/models.py:586-587
    if (the source predicate refused is truthy) {
      // Source: vvaharness/backends/llm/models.py:587-587
      End this invocation with (link, category).
    }
  }
  // Source: vvaharness/backends/llm/models.py:588-588
  End this invocation with None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/models.py:591-593
// Source signature: is_model_refusal_rejection(exc: BaseException) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn is_model_refusal_rejection(exc) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/models.py:592-592
  In source order: Retain source documentation literal source_literal_592_4; it is not a model call.
  // Source: vvaharness/backends/llm/models.py:593-593
  End this invocation with _refusal_link(exc) is not None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/models.py:596-603
// Source signature: model_refusal_from(exc: BaseException, *, route: str, stage: str) -> ModelRefusal | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn model_refusal_from(exc, route, stage) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/models.py:597-598
  In source order: Retain source documentation literal source_literal_597_4; it is not a model call. Then Evaluate once _refusal_link(exc); assign in source target order to found.
  // Source: vvaharness/backends/llm/models.py:599-600
  if (the source predicate found is None is truthy) {
    // Source: vvaharness/backends/llm/models.py:600-600
    End this invocation with None.
  }
  // Source: vvaharness/backends/llm/models.py:601-601
  In source order: Evaluate once found; assign in source target order to (link, category).
  // Source: vvaharness/backends/llm/models.py:602-603
  End this invocation with model_refusal(route=route, stage=stage, category=category, detail=rejection_text(link)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/models.py:609-621
In source order: For _REASONING_EFFORT_RX, assign re.compile('reasoning[\\s_.\\-]?effort'); source annotation Final[re.Pattern[str]]. Then For _REASONING_CONTAINER_MARKERS, assign ("unsupported parameter: 'reasoning'", "unknown parameter: 'reasoning'"); source annotation Final[tuple[str, ...]]. Then For _FIELD_UNSUPPORTED_MARKERS, assign ('unknown parameter', 'unsupported parameter', 'unrecognized request argument'); source annotation Final[tuple[str, ...]].
// Source: vvaharness/backends/llm/models.py:624-627
// Source signature: _is_effort_rejection_subject(text: str) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _is_effort_rejection_subject(text) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/models.py:625-625
  In source order: Retain source documentation literal source_literal_625_4; it is not a model call.
  // Source: vvaharness/backends/llm/models.py:626-627
  End this invocation with bool(_REASONING_EFFORT_RX.search(text) or any((marker in text for marker in _REASONING_CONTAINER_MARKERS))).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/models.py:630-639
// Source signature: _effort_rejection_text(exc: BaseException) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _effort_rejection_text(exc) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/models.py:631-631
  In source order: Retain source documentation literal source_literal_631_4; it is not a model call.
  // Source: vvaharness/backends/llm/models.py:632-638
  for each link in exception_chain(exc) {
    // Source: vvaharness/backends/llm/models.py:633-633
    In source order: Evaluate once getattr(link, 'status_code', None); assign in source target order to status.
    // Source: vvaharness/backends/llm/models.py:634-635
    if (the source predicate status not in PARAM_REJECTION_STATUS and (not is_gateway_wrapped_param_rejection(link)) is truthy) {
      // Source: vvaharness/backends/llm/models.py:635-635
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/backends/llm/models.py:636-636
    In source order: Evaluate once rejection_text(link).lower(); assign in source target order to text.
    // Source: vvaharness/backends/llm/models.py:637-638
    if (the source predicate _is_effort_rejection_subject(text) is truthy) {
      // Source: vvaharness/backends/llm/models.py:638-638
      End this invocation with text.
    }
  }
  // Source: vvaharness/backends/llm/models.py:639-639
  End this invocation with None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/models.py:643-644
In source order: For _TIER_VALUE_RX, assign re.compile('[\'\\"](?:none|low|medium|high|xhigh|max)[\'\\"]'); source annotation Final[re.Pattern[str]].
// Source: vvaharness/backends/llm/models.py:647-650
// Source signature: _is_value_list_rejection_text(text: str) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _is_value_list_rejection_text(text) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/models.py:648-648
  In source order: Retain source documentation literal source_literal_648_4; it is not a model call.
  // Source: vvaharness/backends/llm/models.py:649-650
  End this invocation with bool('supported values' in text or 'invalid value' in text or 'unsupported value' in text).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/models.py:653-655
// Source signature: _is_tier_rejection_text(text: str) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _is_tier_rejection_text(text) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/models.py:654-654
  In source order: Retain source documentation literal source_literal_654_4; it is not a model call.
  // Source: vvaharness/backends/llm/models.py:655-655
  End this invocation with _is_value_list_rejection_text(text) or bool(_TIER_VALUE_RX.search(text)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/models.py:658-681
// Source signature: _effort_rejection_class(text: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _effort_rejection_class(text) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/models.py:659-671
  In source order: Retain source documentation literal source_literal_659_4; it is not a model call.
  // Source: vvaharness/backends/llm/models.py:672-673
  if (the source predicate _is_value_list_rejection_text(text) is truthy) {
    // Source: vvaharness/backends/llm/models.py:673-673
    End this invocation with 'tier'.
  }
  // Source: vvaharness/backends/llm/models.py:674-675
  if (the source predicate re.search('\\btools?\\b', text) is truthy) {
    // Source: vvaharness/backends/llm/models.py:675-675
    End this invocation with 'tools_conflict'.
  }
  // Source: vvaharness/backends/llm/models.py:678-680
  In source order: Evaluate once not _TIER_VALUE_RX.search(text) and (any((marker in text for marker in _FIELD_UNSUPPORTED_MARKERS)) or 'not supported' in text); assign in source target order to is_field.
  // Source: vvaharness/backends/llm/models.py:681-681
  End this invocation with 'field' if is_field else 'tier'.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/models.py:684-693
// Source signature: classify_effort_rejection(exc: BaseException) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn classify_effort_rejection(exc) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/models.py:685-688
  In source order: Retain source documentation literal source_literal_685_4; it is not a model call.
  // Source: vvaharness/backends/llm/models.py:690-691
  if (the source predicate is_model_refusal_rejection(exc) is truthy) {
    // Source: vvaharness/backends/llm/models.py:691-691
    End this invocation with None.
  }
  // Source: vvaharness/backends/llm/models.py:692-692
  In source order: Evaluate once _effort_rejection_text(exc); assign in source target order to text.
  // Source: vvaharness/backends/llm/models.py:693-693
  End this invocation with None if text is None else _effort_rejection_class(text).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/models.py:696-698
// Source signature: is_reasoning_effort_rejection(exc: BaseException) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn is_reasoning_effort_rejection(exc) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/models.py:697-697
  In source order: Retain source documentation literal source_literal_697_4; it is not a model call.
  // Source: vvaharness/backends/llm/models.py:698-698
  End this invocation with classify_effort_rejection(exc) is not None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/models.py:702-706
In source order: For REASONING_EFFORT_LADDER, assign ('max', 'high', 'low'); source annotation Final[tuple[str, ...]]. Then For _LADDER_NEXT, assign {'max': 'high', 'xhigh': 'high', 'high': 'low', 'medium': 'low', 'none': 'low', 'low': None}; source annotation Final[dict[str, str | None]].
// Source: vvaharness/backends/llm/models.py:709-711
// Source signature: next_effort_tier(tier: str | None) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn next_effort_tier(tier) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/models.py:710-710
  In source order: Retain source documentation literal source_literal_710_4; it is not a model call.
  // Source: vvaharness/backends/llm/models.py:711-711
  End this invocation with _LADDER_NEXT.get(tier) if tier is not None else None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/models.py:719-730
In source order: For TRANSPORT_CHAT, assign TRANSPORT_CHAT_COMPLETIONS; source annotation Final. Then For _TIER_RANK, assign {tier: rank for rank, tier in enumerate(('none', 'minimal', 'low', 'medium', 'high', 'xhigh', 'max'))}; source annotation Final[dict[str, int]]. Then For _QUOTED_TOKEN_RX, assign re.compile('[\'\\"]([a-zA-Z]+)'); source annotation Final[re.Pattern[str]].
// Source: vvaharness/backends/llm/models.py:733-752
// Source signature: _listed_tiers(text: str) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _listed_tiers(text) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/models.py:734-742
  In source order: Retain source documentation literal source_literal_734_4; it is not a model call. Then Evaluate once []; assign in source target order to found. Then Evaluate once _is_value_list_rejection_text(text); assign in source target order to allow_prefix.
  // Source: vvaharness/backends/llm/models.py:743-751
  for each token in _QUOTED_TOKEN_RX.findall(text.lower()) {
    // Source: vvaharness/backends/llm/models.py:744-746
    if (the source predicate token in _TIER_RANK is truthy) {
      // Source: vvaharness/backends/llm/models.py:745-745
      In source order: Evaluate found.append(token); retain side effects and discard the expression result.
      // Source: vvaharness/backends/llm/models.py:746-746
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/backends/llm/models.py:747-748
    if (the source predicate not allow_prefix is truthy) {
      // Source: vvaharness/backends/llm/models.py:748-748
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/backends/llm/models.py:749-749
    In source order: Evaluate once [tier for tier in _TIER_RANK if tier.startswith(token)]; assign in source target order to prefix_matches.
    // Source: vvaharness/backends/llm/models.py:750-751
    if (the source predicate len(prefix_matches) == 1 is truthy) {
      // Source: vvaharness/backends/llm/models.py:751-751
      In source order: Evaluate found.append(prefix_matches[0]); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/backends/llm/models.py:752-752
  End this invocation with found.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/models.py:755-757
// Source signature: _tiers_key(model: str, tier: str, transport: str) -> tuple
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _tiers_key(model, tier, transport) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/models.py:756-756
  In source order: Retain source documentation literal source_literal_756_4; it is not a model call.
  // Source: vvaharness/backends/llm/models.py:757-757
  End this invocation with (model, tier) if transport == TRANSPORT_CHAT else (model, tier, transport).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/models.py:760-780
// Source signature: step_down(model: str, sent: str, exc: BaseException, transport: str=TRANSPORT_CHAT) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn step_down(model, sent, exc, transport) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/models.py:763-774
  In source order: Retain source documentation literal source_literal_763_4; it is not a model call. Then Evaluate EFFORT_REJECTIONS.tiers.add(_tiers_key(model, sent, transport)); retain side effects and discard the expression result. Then Evaluate once _effort_rejection_text(exc) or ''; assign in source target order to text. Then Evaluate once _TIER_RANK.get(sent, -1); assign in source target order to sent_rank. Then Evaluate once [t for t in _listed_tiers(text) if _TIER_RANK.get(t, -1) < sent_rank]; assign in source target order to listed_below.
  // Source: vvaharness/backends/llm/models.py:775-776
  if (the source predicate transport != TRANSPORT_CHAT is truthy) {
    // Source: vvaharness/backends/llm/models.py:776-776
    In source order: Evaluate once [t for t in listed_below if t != REASONING_OFF]; assign in source target order to listed_below.
  }
  // Source: vvaharness/backends/llm/models.py:777-777
  In source order: Evaluate once max(listed_below, key=_TIER_RANK.get) if listed_below else next_effort_tier(sent); assign in source target order to nxt.
  // Source: vvaharness/backends/llm/models.py:778-779
  if (the source predicate nxt is not None is truthy) {
    // Source: vvaharness/backends/llm/models.py:779-779
    In source order: Evaluate once nxt; assign in source target order to EFFORT_REJECTIONS.step_to[model, transport, sent].
  }
  // Source: vvaharness/backends/llm/models.py:780-780
  End this invocation with nxt.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/models.py:783-799
// Source signature: effort_after_rejections(model: str, tier: str | None, transport: str=TRANSPORT_CHAT) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn effort_after_rejections(model, tier, transport) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/models.py:786-790
  In source order: Retain source documentation literal source_literal_786_4; it is not a model call.
  // Source: vvaharness/backends/llm/models.py:791-798
  while (the source predicate tier is not None is truthy) {
    // Source: vvaharness/backends/llm/models.py:792-792
    In source order: Evaluate once EFFORT_REJECTIONS.step_to.get((model, transport, tier)); assign in source target order to learned.
    // Source: vvaharness/backends/llm/models.py:793-795
    if (the source predicate learned is not None is truthy) {
      // Source: vvaharness/backends/llm/models.py:794-794
      In source order: Evaluate once learned; assign in source target order to tier.
      // Source: vvaharness/backends/llm/models.py:795-795
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/backends/llm/models.py:796-797
    if (the source predicate _tiers_key(model, tier, transport) not in EFFORT_REJECTIONS.tiers is truthy) {
      // Source: vvaharness/backends/llm/models.py:797-797
      Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
    }
    // Source: vvaharness/backends/llm/models.py:798-798
    In source order: Evaluate once next_effort_tier(tier); assign in source target order to tier.
  }
  // Source: vvaharness/backends/llm/models.py:799-799
  End this invocation with tier.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/models.py:803-803
In source order: For REASONING_OFF, assign 'none'; source annotation Final.
// Source: vvaharness/backends/llm/models.py:806-851
interface _EffortRejections {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/llm/models.py:807-807
  In source order: Retain source documentation literal source_literal_807_4; it is not a model call.
  // Source: vvaharness/backends/llm/models.py:809-825
  // Source signature: __init__(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/llm/models.py:811-820
    In source order: For self.tiers, assign set(); source annotation set[tuple]. Then For self.field, assign set(); source annotation set[str]. Then For self.tools_off, assign set(); source annotation set[str]. Then For self.step_to, assign {}; source annotation dict[tuple[str, str, str], str]. Then For self.server_error_probed, assign set(); source annotation set[tuple].
    // Source: vvaharness/backends/llm/models.py:822-825
    In source order: For self.server_error_recovered, assign set(); source annotation set[tuple]. Then Evaluate once threading.Lock(); assign in source target order to self._probe_lock.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/llm/models.py:827-833
  // Source signature: probe_once(self, key: tuple) -> bool
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn probe_once(self, key) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/llm/models.py:828-828
    In source order: Retain source documentation literal source_literal_828_8; it is not a model call.
    // Source: vvaharness/backends/llm/models.py:829-833
    Enter source context managers left-to-right: self._probe_lock {
      // Source: vvaharness/backends/llm/models.py:830-831
      if (the source predicate key in self.server_error_probed is truthy) {
        // Source: vvaharness/backends/llm/models.py:831-831
        End this invocation with False.
      }
      // Source: vvaharness/backends/llm/models.py:832-832
      In source order: Evaluate self.server_error_probed.add(key); retain side effects and discard the expression result.
      // Source: vvaharness/backends/llm/models.py:833-833
      End this invocation with True.
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/llm/models.py:835-842
  // Source signature: recovered_twice(self, key: tuple) -> bool
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn recovered_twice(self, key) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/llm/models.py:836-836
    In source order: Retain source documentation literal source_literal_836_8; it is not a model call.
    // Source: vvaharness/backends/llm/models.py:837-842
    Enter source context managers left-to-right: self._probe_lock {
      // Source: vvaharness/backends/llm/models.py:838-839
      if (the source predicate key in self.server_error_recovered is truthy) {
        // Source: vvaharness/backends/llm/models.py:839-839
        End this invocation with True.
      }
      // Source: vvaharness/backends/llm/models.py:840-841
      In source order: Evaluate self.server_error_recovered.add(key); retain side effects and discard the expression result. Then Evaluate self.server_error_probed.discard(key); retain side effects and discard the expression result.
      // Source: vvaharness/backends/llm/models.py:842-842
      End this invocation with False.
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/llm/models.py:844-851
  // Source signature: clear(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn clear(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/llm/models.py:845-849
    In source order: Retain source documentation literal source_literal_845_8; it is not a model call. Then Evaluate self.tiers.clear(); retain side effects and discard the expression result. Then Evaluate self.field.clear(); retain side effects and discard the expression result. Then Evaluate self.tools_off.clear(); retain side effects and discard the expression result. Then Evaluate self.step_to.clear(); retain side effects and discard the expression result.
    // Source: vvaharness/backends/llm/models.py:850-851
    In source order: Evaluate self.server_error_probed.clear(); retain side effects and discard the expression result. Then Evaluate self.server_error_recovered.clear(); retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vvaharness/backends/llm/models.py:857-857
In source order: For EFFORT_REJECTIONS, assign _EffortRejections(); source annotation Final.
// Source: vvaharness/backends/llm/models.py:860-875
interface _TransportMemory {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/llm/models.py:861-861
  In source order: Retain source documentation literal source_literal_861_4; it is not a model call.
  // Source: vvaharness/backends/llm/models.py:863-869
  // Source signature: __init__(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/llm/models.py:865-869
    In source order: For self.chat_only, assign set(); source annotation set[str]. Then For self.responses_proven, assign set(); source annotation set[str]. Then For self.no_include, assign set(); source annotation set[str].
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/llm/models.py:871-875
  // Source signature: clear(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn clear(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/llm/models.py:872-875
    In source order: Retain source documentation literal source_literal_872_8; it is not a model call. Then Evaluate self.chat_only.clear(); retain side effects and discard the expression result. Then Evaluate self.responses_proven.clear(); retain side effects and discard the expression result. Then Evaluate self.no_include.clear(); retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vvaharness/backends/llm/models.py:881-881
In source order: For TRANSPORT_MEMORY, assign _TransportMemory(); source annotation Final.
// Source: vvaharness/backends/llm/models.py:884-895
// Source signature: turn_timeout(session_t0: float, session_budget: float | None, request_timeout: float) -> float
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn turn_timeout(session_t0, session_budget, request_timeout) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/models.py:886-891
  In source order: Retain source documentation literal source_literal_886_4; it is not a model call.
  // Source: vvaharness/backends/llm/models.py:892-893
  if (the source predicate session_budget is None is truthy) {
    // Source: vvaharness/backends/llm/models.py:893-893
    End this invocation with request_timeout.
  }
  // Source: vvaharness/backends/llm/models.py:894-894
  In source order: Evaluate once session_budget - (time.monotonic() - session_t0); assign in source target order to remaining.
  // Source: vvaharness/backends/llm/models.py:895-895
  End this invocation with min(request_timeout, max(1.0, remaining)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/models.py:898-905
// Source signature: turn_options(session_t0: float, session_budget: float | None, request_timeout: float) -> dict
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn turn_options(session_t0, session_budget, request_timeout) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/models.py:900-902
  In source order: Retain source documentation literal source_literal_900_4; it is not a model call. Then Evaluate once turn_timeout(session_t0, session_budget, request_timeout); assign in source target order to clocked. Then For options, assign {'timeout': clocked}; source annotation dict.
  // Source: vvaharness/backends/llm/models.py:903-904
  if (the source predicate session_budget is not None and request_timeout - clocked >= 1.0 is truthy) {
    // Source: vvaharness/backends/llm/models.py:904-904
    In source order: Evaluate once 0; assign in source target order to options['max_retries'].
  }
  // Source: vvaharness/backends/llm/models.py:905-905
  End this invocation with options.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/models.py:908-917
// Source signature: wait_overrun(wait: float, session_t0: float, session_budget: float | None, *, stage: str, route: str, effort: str | None) -> CallTimeoutError | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn wait_overrun(wait, session_t0, session_budget, stage, route, effort) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/models.py:912-912
  In source order: Retain source documentation literal source_literal_912_4; it is not a model call.
  // Source: vvaharness/backends/llm/models.py:913-914
  if (the source predicate session_budget is None or time.monotonic() - session_t0 + wait < session_budget is truthy) {
    // Source: vvaharness/backends/llm/models.py:914-914
    End this invocation with None.
  }
  // Source: vvaharness/backends/llm/models.py:915-917
  End this invocation with call_timeout_error(stage=stage, route=route, budget_s=session_budget, effort=effort, cause_text=source_template_917_19).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/models.py:923-926
In source order: For _SHAPE_REJECTION_MARKERS, assign ('unsupported parameter', 'unknown parameter'); source annotation Final[tuple[str, ...]]. Then For _NOT_FOUND_STATUS, assign 404; source annotation Final.
// Source: vvaharness/backends/llm/models.py:929-936
// Source signature: is_responses_shape_rejection(exc: BaseException) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn is_responses_shape_rejection(exc) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/models.py:930-930
  In source order: Retain source documentation literal source_literal_930_4; it is not a model call.
  // Source: vvaharness/backends/llm/models.py:931-933
  if (the source predicate any((getattr(link, 'status_code', None) == _NOT_FOUND_STATUS for link in exception_chain(exc))) is truthy) {
    // Source: vvaharness/backends/llm/models.py:933-933
    End this invocation with True.
  }
  // Source: vvaharness/backends/llm/models.py:934-935
  if (the source predicate classify_effort_rejection(exc) is not None is truthy) {
    // Source: vvaharness/backends/llm/models.py:935-935
    End this invocation with False.
  }
  // Source: vvaharness/backends/llm/models.py:936-936
  End this invocation with is_param_rejection(exc, *_SHAPE_REJECTION_MARKERS).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/models.py:940-949
// Source: vvaharness/backends/llm/models.py:939-939
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: runtime_checkable.
// Source: vvaharness/backends/llm/models.py:940-949
interface LlmBackend {
  Describe the source Python type, preserving its base/metaclass expression order: Protocol.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/llm/models.py:941-941
  In source order: Retain source documentation literal source_literal_941_4; it is not a model call.
  // Source: vvaharness/backends/llm/models.py:943-945
  // Source signature: prompt(self, user_prompt: str, *, model: str, **kwargs: Any) -> str
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn prompt(self, user_prompt, model, kwargs) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/llm/models.py:944-945
    In source order: Retain source documentation literal source_literal_944_8; it is not a model call. Then Evaluate ...; retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/llm/models.py:947-949
  // Source signature: agentic(self, user_prompt: str, *, model: str, **kwargs: Any) -> str
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn agentic(self, user_prompt, model, kwargs) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/llm/models.py:948-949
    In source order: Retain source documentation literal source_literal_948_8; it is not a model call. Then Evaluate ...; retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vvaharness/backends/llm/models.py:952-1039
In source order: Evaluate once ['AGENTIC_MAX_TOKENS', 'ANTHROPIC_STOP_CONTEXT_WINDOW', 'ANTHROPIC_STOP_MAX_TOKENS', 'ANTHROPIC_STOP_REFUSAL', 'BUDGET_NEAR_RATIO', 'CLI_CONN_TRANSIENT_RX', 'CLI_CONTINUED_REPLIES_COUNTER', 'CLI_RETRYABLE_STATUS', 'CLI_STATUS_429_RX', 'CLI_STRUCTURED_OUTPUT_TOOL', 'CLI_TOKEN_CAP_RX', 'DEEPAGENTS_MAX_PROMPT_TOKENS', 'DEFAULT_READ_TOOLS', 'DEFAULT_REQUEST_TIMEOUT_SECONDS', 'EFFORT_REJECTIONS', 'EFFORT_TIME_FACTOR', 'LLM_CALL_BUDGET_NEAR_COUNTER', 'LLM_CALL_TIMEOUTS_COUNTER', 'LLM_MODEL_REFUSALS_COUNTER', 'LLM_TRUNCATED_BELOW_BUDGET_COUNTER', 'OPENAI_FINISH_LENGTH', 'PARAM_REJECTION_ERROR_TYPES', 'PARAM_REJECTION_STATUS', 'PROXY_CAUSE_RX', 'RATE_LIMIT_TRANSIENT_RX', 'REASONING_EFFORT_LADDER', 'REASONING_OFF', 'REFUSAL_RETRY_ATTEMPTED_COUNTER', 'REFUSAL_RETRY_RECOVERED_COUNTER', 'RESPONSES_INCOMPLETE_MAX_OUTPUT', 'RESPONSE_MODEL_TOOL_NAME', 'RESPONSE_MODEL_VIAS', 'RETRYABLE_STATUS', 'RETRY_JITTER_SPREAD', 'SERVER_ERROR_STATUS', 'SERVER_ERROR_TRANSIENT_RX', 'STRUCTURED_PROSE_REASK', 'STRUCTURED_REASK_MAX', 'TIMEOUT_MAX_RETRIES', 'TIMEOUT_STOP_GRACE_SECONDS', 'TRANSPORT_CHAT', 'TRANSPORT_MEMORY', 'TRANSPORT_RESPONSES', 'TRUNCATED_REPLIES_COUNTER', 'TRUNCATED_RETRY_ATTEMPTED_COUNTER', 'TRUNCATED_RETRY_RECOVERED_COUNTER', 'TRUNCATION_RETRY_MULTIPLIER', 'ClockKind', 'GuardrailBlocked', 'LlmBackend', 'ModelExtras', 'ModelRefusal', 'ModulePath', 'ResolvedModel', 'ai_message_refused', 'call_timeout_error', 'cause_chain', 'classify_effort_rejection', 'effort_after_rejections', 'effort_scaled_seconds', 'finish_truncated', 'guardrail_gate_hit', 'is_gateway_wrapped_param_rejection', 'is_model_refusal_rejection', 'is_param_rejection', 'is_reasoning_effort_rejection', 'is_responses_shape_rejection', 'jittered_delay', 'model_refusal', 'model_refusal_from', 'next_effort_tier', 'note_budget_use', 'proxy_detail', 'proxy_error', 'refusal_category', 'refusal_resend_allowed', 'rejection_text', 'reply_finish', 'response_model_tool', 'step_down', 'truncation_retry_max', 'turn_options', 'turn_timeout', 'validate_detection_tools', 'wait_overrun', 'with_submit_instruction']; assign in source target order to __all__.
```

## Local import links

- `from vvaharness.backends.harness.models import CallTimeoutError, EffortLevel, ProxyError` at source line 30: `source_detail/vvaharness/backends/harness/models.py.sudo.md`.
- `from vvaharness.backends.harness.provider_routing import TRANSPORT_CHAT_COMPLETIONS, TRANSPORT_RESPONSES` at source line 31: `source_detail/vvaharness/backends/harness/provider_routing.py.sudo.md`.
- `from vvaharness.report.redact import redact` at source line 35: `source_detail/vvaharness/report/redact.py.sudo.md`.
- `from vvaharness.util.config import knob` at source line 36: `source_detail/vvaharness/util/config.py.sudo.md`.
- `from vvaharness.util.counters import COUNTERS` at source line 37: `source_detail/vvaharness/util/counters.py.sudo.md`.
- `from vvaharness.util.exceptions import exception_chain` at source line 38: `source_detail/vvaharness/util/exceptions.py.sudo.md`.
- `from vvaharness.util.tokens import TokenUsage` at source line 39: `source_detail/vvaharness/util/tokens.py.sudo.md`.
- `from vvaharness.backends.llm.registry import provider_of, resolve` at source line 516: `source_detail/vvaharness/backends/llm/registry.py.sudo.md`.
- `from vvaharness.manifest import _resolved_route` at source line 520: `source_detail/vvaharness/manifest.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../prompt_representation/vvaharness/backends/llm/models.py.sudo.md). Exact strings in the evidence asset support this conversion.
