# vvaharness/backends/harness/deepagents/client.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/backends/harness/deepagents/client.py.evidence.json`. SHA-256: `724cb3f27f0a8aae78e69e4b43046e3d7166fe22fac46c6e50ee46707e3265f2`.

```sudo
// Source: vvaharness/backends/harness/deepagents/client.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import asyncio; preserve alias and import-time effects. Then Resolve source import import dataclasses; preserve alias and import-time effects. Then Resolve source import from collections.abc import AsyncIterator; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/deepagents/client.py:22-29
In source order: Resolve source import from typing import NamedTuple, cast; preserve alias and import-time effects. Then Resolve source import from uuid import uuid4; preserve alias and import-time effects. Then Resolve source import from langchain_core.messages import HumanMessage; preserve alias and import-time effects. Then Resolve source import from langchain_core.runnables import RunnableConfig; preserve alias and import-time effects. Then Resolve source import from langgraph.errors import GraphRecursionError; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/deepagents/client.py:30-48
In source order: Resolve source import from langgraph.graph.state import CompiledStateGraph; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.deepagents.models import DeepAgentsGraphState; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.deepagents.options import build_oneshot_options, build_streaming_agent, resumable; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.deepagents.options.model_building import _CHAT_COMPLETIONS_ONLY_MODELS, _FORCED_TOOL_CHOICE_UNSUPPORTED_MODELS, _openai_effort_kwargs, resolve_use_responses_api; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.deepagents.tool_choice_rejection import is_tool_choice_unsupported_rejection, learn_tool_choice_unsupported, rejected_model; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/deepagents/client.py:49-71
In source order: Resolve source import from vvaharness.backends.harness.deepagents.translate import make_terminal_result, translate_final_state, translate_stream_events; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.deepagents.usage import UsageAccumulator; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.harness import Harness; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.models import HarnessError, HarnessMessage, HarnessProcessError, HarnessSessionInit, OneShotOptions, OneShotResult, SessionNotResumableError, SessionOptions, StreamingOptions; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.provider_routing import TRANSPORT_CHAT_COMPLETIONS, TRANSPORT_RESPONSES, routes_to_anthropic; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/deepagents/client.py:72-88
In source order: Resolve source import from vvaharness.backends.llm.models import EFFORT_REJECTIONS, REASONING_OFF, SERVER_ERROR_STATUS, TRANSPORT_MEMORY, _tiers_key, call_timeout_error, classify_effort_rejection, is_model_refusal_rejection, is_responses_shape_rejection, next_effort_tier, step_down; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.counters import COUNTERS; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.exceptions import exception_chain; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.response_quality import is_connection_failure; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.tokens import TOKENS; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/deepagents/client.py:89-101
In source order: Resolve source import from vvaharness.util.warn_once import warn_once; preserve alias and import-time effects. Then For _EPHEMERAL_CACHE_CONTROL, assign {'type': 'ephemeral'}; source annotation dict[str, str]. Then Evaluate once 400; assign in source target order to _HTTP_BAD_REQUEST. Then For _RESPONSES_PROVEN_MODELS, assign TRANSPORT_MEMORY.responses_proven; source annotation set[str]. Then For _EFFORT_UNSUPPORTED_WARNED, assign set(); source annotation set[str].
// Source: vvaharness/backends/harness/deepagents/client.py:102-108
In source order: For _TRANSPORT_FALLBACK_WARNED, assign set(); source annotation set[str]. Then Evaluate once 'deepagents_responses_fallback'; assign in source target order to _RESPONSES_FALLBACK_COUNTER. Then Evaluate once 'thought_signature'; assign in source target order to _THOUGHT_SIGNATURE_MARKER.
// Source: vvaharness/backends/harness/deepagents/client.py:111-113
// Source signature: _is_reasoning_effort_rejection(exc: Exception) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _is_reasoning_effort_rejection(exc) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/client.py:112-112
  In source order: Retain source documentation literal source_literal_112_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/client.py:113-113
  End this invocation with classify_effort_rejection(exc) is not None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/client.py:116-148
// Source signature: _bounded_astream_events(stream: AsyncIterator[object], timeout: float | None, graph_name: str, effort: str | None) -> AsyncIterator[object]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _bounded_astream_events(stream, timeout, graph_name, effort) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  This callable produces a coroutine or async generator; await/suspension positions remain in source expressions.
  // Source: vvaharness/backends/harness/deepagents/client.py:119-125
  In source order: Retain source documentation literal source_literal_119_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/client.py:126-129
  if (the source predicate not timeout is truthy) {
    // Source: vvaharness/backends/harness/deepagents/client.py:127-128
    Obtain/advance the following source async iterator by awaiting, without inventing parallel dispatch.
    for each event in stream {
      // Source: vvaharness/backends/harness/deepagents/client.py:128-128
      In source order: Yield event; suspend this generator until resumed.
    }
    // Source: vvaharness/backends/harness/deepagents/client.py:129-129
    End this invocation with None.
  }
  // Source: vvaharness/backends/harness/deepagents/client.py:130-132
  In source order: Evaluate once asyncio.get_running_loop(); assign in source target order to loop. Then Evaluate once loop.time() + timeout; assign in source target order to deadline. Then Evaluate once stream.__aiter__(); assign in source target order to iterator.
  // Source: vvaharness/backends/harness/deepagents/client.py:133-148
  while (the source predicate True is truthy) {
    // Source: vvaharness/backends/harness/deepagents/client.py:134-134
    In source order: Evaluate once asyncio.timeout_at(deadline); assign in source target order to cm.
    // Source: vvaharness/backends/harness/deepagents/client.py:135-147
    Perform the following protected operations {
      // Source: vvaharness/backends/harness/deepagents/client.py:136-137
      Await and enter source context managers left-to-right: cm {
        // Source: vvaharness/backends/harness/deepagents/client.py:137-137
        In source order: Evaluate once await anext(iterator); assign in source target order to event.
      }
      Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics and await async exits.
    }
    // Source: vvaharness/backends/harness/deepagents/client.py:138-139
    On the first matching source exception StopAsyncIteration, in handler order {
      // Source: vvaharness/backends/harness/deepagents/client.py:139-139
      End this invocation with None.
    }
    // Source: vvaharness/backends/harness/deepagents/client.py:140-147
    On the first matching source exception TimeoutError, in handler order {
      // Source: vvaharness/backends/harness/deepagents/client.py:142-143
      if (the source predicate not cm.expired() is truthy) {
        // Source: vvaharness/backends/harness/deepagents/client.py:143-143
        Raise the currently handled exception.
      }
      // Source: vvaharness/backends/harness/deepagents/client.py:144-147
      Raise call_timeout_error(stage=graph_name, route='deepagents', budget_s=timeout, effort=effort, cause_text=source_template_146_27) with explicit source cause None.
    }
    // Source: vvaharness/backends/harness/deepagents/client.py:148-148
    In source order: Yield event; suspend this generator until resumed.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/client.py:151-164
// Source signature: _sent_effort_tier(options: SessionOptions) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _sent_effort_tier(options) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/client.py:152-156
  In source order: Retain source documentation literal source_literal_152_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/client.py:157-158
  if (the source predicate routes_to_anthropic(options.model, options.model_provider) is truthy) {
    // Source: vvaharness/backends/harness/deepagents/client.py:158-158
    End this invocation with None.
  }
  // Source: vvaharness/backends/harness/deepagents/client.py:159-163
  In source order: Evaluate once resolve_use_responses_api(options.model, options.model_provider, options.use_responses_api); assign in source target order to resolved_transport. Then Evaluate once _openai_effort_kwargs(options.model, options.effort, think_in_prompt=options.think_in_prompt, resolved_transport=bool(resolved_transport)); assign in source target order to kw.
  // Source: vvaharness/backends/harness/deepagents/client.py:164-164
  End this invocation with kw.get('reasoning_effort').
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/client.py:167-174
// Source signature: _tools_off_exhausted(model_id: str, sent_tier: str, cls: str) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _tools_off_exhausted(model_id, sent_tier, cls) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/client.py:168-172
  In source order: Retain source documentation literal source_literal_168_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/client.py:173-174
  End this invocation with model_id in EFFORT_REJECTIONS.tools_off and (cls == 'tools_conflict' or sent_tier == REASONING_OFF).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/client.py:177-202
// Source signature: _step_down_reasoning_effort(model_id: str, sent_tier: str, cls: str, exc: BaseException, *, transport: str) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _step_down_reasoning_effort(model_id, sent_tier, cls, exc, transport) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/client.py:180-184
  In source order: Retain source documentation literal source_literal_180_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/client.py:185-196
  if (the source predicate cls == 'field' is truthy) {
    // Source: vvaharness/backends/harness/deepagents/client.py:186-188
    In source order: Evaluate EFFORT_REJECTIONS.field.add(model_id); retain side effects and discard the expression result. Then Evaluate COUNTERS.bump('llm_effort_field_dropped'); retain side effects and discard the expression result. Then Evaluate once 'no field'; assign in source target order to next_value.
  }
  else {
    // Source: vvaharness/backends/harness/deepagents/client.py:189-196
    if (the source predicate cls == 'tools_conflict' is truthy) {
      // Source: vvaharness/backends/harness/deepagents/client.py:190-192
      In source order: Evaluate EFFORT_REJECTIONS.tools_off.add(model_id); retain side effects and discard the expression result. Then Evaluate COUNTERS.bump('llm_effort_tools_off'); retain side effects and discard the expression result. Then Evaluate once source_template_192_21; assign in source target order to next_value.
    }
    else {
      // Source: vvaharness/backends/harness/deepagents/client.py:194-196
      In source order: Evaluate once step_down(model_id, sent_tier, exc, transport); assign in source target order to stepped. Then Evaluate COUNTERS.bump('llm_effort_tier_stepped_down'); retain side effects and discard the expression result. Then Evaluate once source_template_196_21 if stepped is not None else 'no field'; assign in source target order to next_value.
    }
  }
  // Source: vvaharness/backends/harness/deepagents/client.py:197-202
  In source order: Evaluate warn_once(_EFFORT_UNSUPPORTED_WARNED, source_template_199_8, source_template_200_8); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/client.py:205-212
// Source signature: _is_persistent_server_error(exc: BaseException) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _is_persistent_server_error(exc) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/client.py:206-210
  In source order: Retain source documentation literal source_literal_206_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/client.py:211-212
  End this invocation with any((getattr(link, 'status_code', None) in SERVER_ERROR_STATUS for link in exception_chain(exc))).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/client.py:215-223
// Source signature: _effort_transport(options: SessionOptions) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _effort_transport(options) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/client.py:216-222
  In source order: Retain source documentation literal source_literal_216_4; it is not a model call. Then Evaluate once resolve_use_responses_api(options.model, options.model_provider, options.use_responses_api); assign in source target order to resolved.
  // Source: vvaharness/backends/harness/deepagents/client.py:223-223
  End this invocation with TRANSPORT_RESPONSES if resolved else TRANSPORT_CHAT_COMPLETIONS.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/client.py:226-235
// Source signature: _probe_lower_tier_once(model_id: str, sent_tier: str) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _probe_lower_tier_once(model_id, sent_tier) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/client.py:227-227
  In source order: Retain source documentation literal source_literal_227_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/client.py:230-231
  if (the source predicate sent_tier == REASONING_OFF is truthy) {
    // Source: vvaharness/backends/harness/deepagents/client.py:231-231
    End this invocation with None.
  }
  // Source: vvaharness/backends/harness/deepagents/client.py:232-232
  In source order: Evaluate once next_effort_tier(sent_tier); assign in source target order to nxt.
  // Source: vvaharness/backends/harness/deepagents/client.py:233-234
  if (the source predicate nxt is None or not EFFORT_REJECTIONS.probe_once((model_id, sent_tier)) is truthy) {
    // Source: vvaharness/backends/harness/deepagents/client.py:234-234
    End this invocation with None.
  }
  // Source: vvaharness/backends/harness/deepagents/client.py:235-235
  End this invocation with nxt.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/client.py:238-243
// Source signature: _responses_active(options: SessionOptions) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _responses_active(options) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/client.py:239-242
  In source order: Retain source documentation literal source_literal_239_4; it is not a model call. Then Evaluate once resolve_use_responses_api(options.model, options.model_provider, options.use_responses_api); assign in source target order to resolved.
  // Source: vvaharness/backends/harness/deepagents/client.py:243-243
  End this invocation with resolved is True and options.use_responses_api is None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/client.py:246-260
// Source signature: _record_server_error_recovery(options: SessionOptions, sent_tier: str, probed: str, probed_options: SessionOptions) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _record_server_error_recovery(options, sent_tier, probed, probed_options) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/client.py:249-249
  In source order: Retain source documentation literal source_literal_249_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/client.py:250-252
  if (the source predicate (learned := EFFORT_REJECTIONS.recovered_twice((options.model, sent_tier))) is truthy) {
    // Source: vvaharness/backends/harness/deepagents/client.py:251-252
    In source order: Evaluate EFFORT_REJECTIONS.tiers.add(_tiers_key(options.model, sent_tier, _effort_transport(options))); retain side effects and discard the expression result.
  }
  // Source: vvaharness/backends/harness/deepagents/client.py:253-258
  In source order: Evaluate COUNTERS.bump('llm_effort_tier_stepped_down_on_server_error'); retain side effects and discard the expression result. Then Evaluate warn_once(_EFFORT_UNSUPPORTED_WARNED, source_template_255_36, source_template_256_8); retain side effects and discard the expression result.
  // Source: vvaharness/backends/harness/deepagents/client.py:259-260
  if (the source predicate _responses_active(probed_options) is truthy) {
    // Source: vvaharness/backends/harness/deepagents/client.py:260-260
    In source order: Evaluate _RESPONSES_PROVEN_MODELS.add(options.model); retain side effects and discard the expression result.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/client.py:263-286
// Source signature: _probe_server_error_oneshot(options: OneShotOptions, content: str | list[str | dict[str, object]], sent_tier: str, exc: Exception) -> OneShotResult | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _probe_server_error_oneshot(options, content, sent_tier, exc) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  This callable produces a coroutine or async generator; await/suspension positions remain in source expressions.
  // Source: vvaharness/backends/harness/deepagents/client.py:267-272
  In source order: Retain source documentation literal source_literal_267_4; it is not a model call. Then Evaluate once _probe_lower_tier_once(options.model, sent_tier); assign in source target order to probed.
  // Source: vvaharness/backends/harness/deepagents/client.py:273-274
  if (the source predicate probed is None is truthy) {
    // Source: vvaharness/backends/harness/deepagents/client.py:274-274
    End this invocation with None.
  }
  // Source: vvaharness/backends/harness/deepagents/client.py:275-276
  In source order: Evaluate once dataclasses.replace(options, effort=probed); assign in source target order to probed_options. Then Evaluate once build_oneshot_options(probed_options); assign in source target order to (probed_graph, probed_config).
  // Source: vvaharness/backends/harness/deepagents/client.py:277-284
  Perform the following protected operations {
    // Source: vvaharness/backends/harness/deepagents/client.py:278-281
    In source order: Evaluate once await probed_graph.ainvoke({'messages': [HumanMessage(content=content)]}, config=cast(RunnableConfig, probed_config)); assign in source target order to probed_state.
  }
  // Source: vvaharness/backends/harness/deepagents/client.py:282-284
  On the first matching source exception Exception, in handler order {
    // Source: vvaharness/backends/harness/deepagents/client.py:284-284
    Raise exc with explicit source cause None.
  }
  // Source: vvaharness/backends/harness/deepagents/client.py:285-285
  In source order: Evaluate _record_server_error_recovery(options, sent_tier, probed, probed_options); retain side effects and discard the expression result.
  // Source: vvaharness/backends/harness/deepagents/client.py:286-286
  End this invocation with translate_final_state(cast('DeepAgentsGraphState', probed_state), oneshot=True).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/client.py:289-318
// Source signature: _recover_oneshot_exception(harness: DeepAgentHarness, prompt: str, options: OneShotOptions, sent_tier: str | None, exc: Exception) -> OneShotResult
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _recover_oneshot_exception(harness, prompt, options, sent_tier, exc) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  This callable produces a coroutine or async generator; await/suspension positions remain in source expressions.
  // Source: vvaharness/backends/harness/deepagents/client.py:293-297
  In source order: Retain source documentation literal source_literal_293_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/client.py:298-301
  if (the source predicate (unforced := _rejecting_models(exc, options)) is truthy) {
    // Source: vvaharness/backends/harness/deepagents/client.py:300-300
    In source order: Evaluate learn_tool_choice_unsupported(*unforced); retain side effects and discard the expression result.
    // Source: vvaharness/backends/harness/deepagents/client.py:301-301
    End this invocation with await harness.run_oneshot(prompt, options).
  }
  // Source: vvaharness/backends/harness/deepagents/client.py:302-306
  if (the source predicate sent_tier is not None and _is_persistent_server_error(exc) is truthy) {
    // Source: vvaharness/backends/harness/deepagents/client.py:303-304
    In source order: Evaluate once _marked_content(prompt, options.cache_prefix); assign in source target order to content. Then Evaluate once await _probe_server_error_oneshot(options, content, sent_tier, exc); assign in source target order to probed_result.
    // Source: vvaharness/backends/harness/deepagents/client.py:305-306
    if (the source predicate probed_result is not None is truthy) {
      // Source: vvaharness/backends/harness/deepagents/client.py:306-306
      End this invocation with probed_result.
    }
  }
  // Source: vvaharness/backends/harness/deepagents/client.py:307-308
  if (the source predicate not _should_fall_back(exc, options) is truthy) {
    // Source: vvaharness/backends/harness/deepagents/client.py:308-308
    Raise exc.
  }
  // Source: vvaharness/backends/harness/deepagents/client.py:310-310
  In source order: Evaluate _learn_chat_completions_only(options.model); retain side effects and discard the expression result.
  // Source: vvaharness/backends/harness/deepagents/client.py:311-318
  Perform the following protected operations {
    // Source: vvaharness/backends/harness/deepagents/client.py:312-312
    End this invocation with await harness.run_oneshot(prompt, options).
  }
  // Source: vvaharness/backends/harness/deepagents/client.py:313-318
  On the first matching source exception Exception as second_exc, in handler order {
    // Source: vvaharness/backends/harness/deepagents/client.py:315-315
    In source order: Evaluate _CHAT_COMPLETIONS_ONLY_MODELS.discard(options.model); retain side effects and discard the expression result.
    // Source: vvaharness/backends/harness/deepagents/client.py:316-317
    if (the source predicate _is_missing_thought_signature(second_exc) is truthy) {
      // Source: vvaharness/backends/harness/deepagents/client.py:317-317
      Raise second_exc with explicit source cause exc.
    }
    // Source: vvaharness/backends/harness/deepagents/client.py:318-318
    Raise exc with explicit source cause None.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/client.py:321-328
interface _StreamProbeContext {
  Describe the source Python type, preserving its base/metaclass expression order: NamedTuple.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/harness/deepagents/client.py:322-327
  In source order: Retain source documentation literal source_literal_322_4; it is not a model call. Then For sent_tier, declare without assigning a value; source annotation str. Then For error, declare without assigning a value; source annotation Exception. Then For session_id, declare without assigning a value; source annotation str. Then For seen_tool_ids, declare without assigning a value; source annotation set[str].
  // Source: vvaharness/backends/harness/deepagents/client.py:328-328
  In source order: For ns_to_agent, declare without assigning a value; source annotation dict[tuple[str, ...], str].
}
// Source: vvaharness/backends/harness/deepagents/client.py:331-362
// Source signature: _probe_server_error_streaming(prompt: str, options: StreamingOptions, probed: str, ctx: _StreamProbeContext) -> AsyncIterator[HarnessMessage]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _probe_server_error_streaming(prompt, options, probed, ctx) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  This callable produces a coroutine or async generator; await/suspension positions remain in source expressions.
  // Source: vvaharness/backends/harness/deepagents/client.py:334-342
  In source order: Retain source documentation literal source_literal_334_4; it is not a model call. Then Evaluate once dataclasses.replace(options, effort=probed); assign in source target order to probed_options. Then Evaluate once build_streaming_agent(probed_options); assign in source target order to (probed_graph, probed_config). Then Evaluate once cast(RunnableConfig, probed_config); assign in source target order to probed_runnable_config. Then Evaluate once UsageAccumulator(); assign in source target order to probed_usage_acc.
  // Source: vvaharness/backends/harness/deepagents/client.py:343-359
  Perform the following protected operations {
    // Source: vvaharness/backends/harness/deepagents/client.py:344-355
    Obtain/advance the following source async iterator by awaiting, without inventing parallel dispatch.
    for each event in probed_graph.astream({'messages': [HumanMessage(content=_marked_content(prompt, probed_options.cache_prefix))]}, config=probed_runnable_config, stream_mode='updates', subgraphs=True) {
      // Source: vvaharness/backends/harness/deepagents/client.py:351-351
      In source order: Evaluate probed_usage_acc.add_event(event); retain side effects and discard the expression result.
      // Source: vvaharness/backends/harness/deepagents/client.py:352-355
      Obtain/advance the following source async iterator by awaiting, without inventing parallel dispatch.
      for each message in translate_stream_events(event, ctx.seen_tool_ids, ctx.ns_to_agent) {
        // Source: vvaharness/backends/harness/deepagents/client.py:355-355
        In source order: Yield message; suspend this generator until resumed.
      }
    }
    // Source: vvaharness/backends/harness/deepagents/client.py:356-356
    In source order: Evaluate once await _final_state(probed_graph, probed_runnable_config); assign in source target order to probed_state.
  }
  // Source: vvaharness/backends/harness/deepagents/client.py:357-359
  On the first matching source exception Exception, in handler order {
    // Source: vvaharness/backends/harness/deepagents/client.py:359-359
    Raise ctx.error with explicit source cause None.
  }
  // Source: vvaharness/backends/harness/deepagents/client.py:360-362
  In source order: Evaluate _record_server_error_recovery(options, ctx.sent_tier, probed, probed_options); retain side effects and discard the expression result. Then Yield make_terminal_result(probed_state, session_id=ctx.session_id, stream_usage=probed_usage_acc.snapshot()); suspend this generator until resumed.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/client.py:365-374
// Source signature: _is_missing_thought_signature(exc: Exception) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _is_missing_thought_signature(exc) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/client.py:366-366
  In source order: Retain source documentation literal source_literal_366_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/client.py:368-372
  for each link in exception_chain(exc) {
    // Source: vvaharness/backends/harness/deepagents/client.py:369-370
    In source order: Evaluate once getattr(link, 'status_code', None); assign in source target order to status. Then Evaluate once str(getattr(link, 'message', link)).lower(); assign in source target order to body.
    // Source: vvaharness/backends/harness/deepagents/client.py:371-372
    if (the source predicate status == _HTTP_BAD_REQUEST and _THOUGHT_SIGNATURE_MARKER in body is truthy) {
      // Source: vvaharness/backends/harness/deepagents/client.py:372-372
      End this invocation with True.
    }
  }
  // Source: vvaharness/backends/harness/deepagents/client.py:373-373
  In source order: Evaluate once str(getattr(exc, 'stderr', '') or ''); assign in source target order to stderr.
  // Source: vvaharness/backends/harness/deepagents/client.py:374-374
  End this invocation with '400' in stderr and _THOUGHT_SIGNATURE_MARKER in stderr.lower().
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/client.py:377-384
// Source signature: _forcing_candidates(options: SessionOptions) -> tuple[str, ...]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _forcing_candidates(options) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/client.py:378-380
  In source order: Retain source documentation literal source_literal_378_4; it is not a model call. Then Evaluate once getattr(options, 'agents', None) or {}; assign in source target order to agents. Then Evaluate once [options.model, *(getattr(a, 'model', None) or options.model for a in agents.values())]; assign in source target order to ids.
  // Source: vvaharness/backends/harness/deepagents/client.py:381-384
  End this invocation with tuple(dict.fromkeys((m for m in ids if m and m not in _FORCED_TOOL_CHOICE_UNSUPPORTED_MODELS and routes_to_anthropic(m, options.model_provider)))).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/client.py:387-395
// Source signature: _rejecting_models(exc: Exception, options: SessionOptions) -> tuple[str, ...]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _rejecting_models(exc, options) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/client.py:388-388
  In source order: Retain source documentation literal source_literal_388_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/client.py:389-390
  if (the source predicate not (candidates := _forcing_candidates(options)) is truthy) {
    // Source: vvaharness/backends/harness/deepagents/client.py:390-390
    End this invocation with ().
  }
  // Source: vvaharness/backends/harness/deepagents/client.py:391-392
  if (the source predicate not is_tool_choice_unsupported_rejection(exc) is truthy) {
    // Source: vvaharness/backends/harness/deepagents/client.py:392-392
    End this invocation with ().
  }
  // Source: vvaharness/backends/harness/deepagents/client.py:394-394
  In source order: Evaluate once rejected_model(exc); assign in source target order to model.
  // Source: vvaharness/backends/harness/deepagents/client.py:395-395
  End this invocation with (model,) if model in candidates else candidates.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/client.py:398-419
// Source signature: _relearned_for_rerun(error: Exception, options: StreamingOptions, sent_tier: str | None, usage_acc: UsageAccumulator) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _relearned_for_rerun(error, options, sent_tier, usage_acc) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/client.py:400-400
  In source order: Retain source documentation literal source_literal_400_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/client.py:401-403
  if (the source predicate (unforced := _rejecting_models(error, options)) is truthy) {
    // Source: vvaharness/backends/harness/deepagents/client.py:402-402
    In source order: Evaluate learn_tool_choice_unsupported(*unforced); retain side effects and discard the expression result.
    // Source: vvaharness/backends/harness/deepagents/client.py:403-403
    End this invocation with True.
  }
  // Source: vvaharness/backends/harness/deepagents/client.py:404-405
  if (the source predicate sent_tier is None or (effort_cls := classify_effort_rejection(error)) is None is truthy) {
    // Source: vvaharness/backends/harness/deepagents/client.py:405-405
    End this invocation with False.
  }
  // Source: vvaharness/backends/harness/deepagents/client.py:406-416
  if (the source predicate _tools_off_exhausted(options.model, sent_tier, effort_cls) is truthy) {
    // Source: vvaharness/backends/harness/deepagents/client.py:407-409
    In source order: Evaluate EFFORT_REJECTIONS.tiers.add(_tiers_key(options.model, REASONING_OFF, _effort_transport(options))); retain side effects and discard the expression result. Then Evaluate _bank_partial_usage(usage_acc); retain side effects and discard the expression result.
    // Source: vvaharness/backends/harness/deepagents/client.py:410-416
    Raise HarnessProcessError(source_template_411_12, exit_code=1, stderr=str(error)) with explicit source cause error.
  }
  // Source: vvaharness/backends/harness/deepagents/client.py:417-418
  In source order: Evaluate _step_down_reasoning_effort(options.model, sent_tier, effort_cls, error, transport=_effort_transport(options)); retain side effects and discard the expression result.
  // Source: vvaharness/backends/harness/deepagents/client.py:419-419
  End this invocation with True.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/client.py:422-431
// Source signature: _should_fall_back(exc: Exception, options: SessionOptions) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _should_fall_back(exc, options) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/client.py:423-423
  In source order: Retain source documentation literal source_literal_423_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/client.py:426-428
  if (the source predicate is_model_refusal_rejection(exc) or is_connection_failure(exc) or (not _responses_active(options)) is truthy) {
    // Source: vvaharness/backends/harness/deepagents/client.py:428-428
    End this invocation with False.
  }
  // Source: vvaharness/backends/harness/deepagents/client.py:429-430
  if (the source predicate options.model not in _RESPONSES_PROVEN_MODELS is truthy) {
    // Source: vvaharness/backends/harness/deepagents/client.py:430-430
    End this invocation with True.
  }
  // Source: vvaharness/backends/harness/deepagents/client.py:431-431
  End this invocation with is_responses_shape_rejection(exc).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/client.py:434-443
// Source signature: _learn_chat_completions_only(model_id: str) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _learn_chat_completions_only(model_id) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/client.py:435-443
  In source order: Retain source documentation literal source_literal_435_4; it is not a model call. Then Evaluate _CHAT_COMPLETIONS_ONLY_MODELS.add(model_id); retain side effects and discard the expression result. Then Evaluate COUNTERS.bump(_RESPONSES_FALLBACK_COUNTER); retain side effects and discard the expression result. Then Evaluate warn_once(_TRANSPORT_FALLBACK_WARNED, model_id, source_template_441_8); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/client.py:446-451
// Source signature: _bank_partial_usage(usage_acc: UsageAccumulator) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _bank_partial_usage(usage_acc) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/client.py:447-449
  In source order: Retain source documentation literal source_literal_447_4; it is not a model call. Then Evaluate once usage_acc.snapshot(); assign in source target order to snapshot.
  // Source: vvaharness/backends/harness/deepagents/client.py:450-451
  if (the source predicate snapshot is not None is truthy) {
    // Source: vvaharness/backends/harness/deepagents/client.py:451-451
    In source order: Evaluate TOKENS.add(snapshot, turns=snapshot.get('turns')); retain side effects and discard the expression result.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/client.py:454-466
// Source signature: _marked_content(prompt: str, cache_prefix: str | None) -> str | list[str | dict[str, object]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _marked_content(prompt, cache_prefix) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/client.py:457-457
  In source order: Retain source documentation literal source_literal_457_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/client.py:458-459
  if (the source predicate not cache_prefix is truthy) {
    // Source: vvaharness/backends/harness/deepagents/client.py:459-459
    End this invocation with prompt.
  }
  // Source: vvaharness/backends/harness/deepagents/client.py:461-465
  In source order: For blocks, assign [{'type': 'text', 'text': cache_prefix, 'cache_control': dict(_EPHEMERAL_CACHE_CONTROL)}, {'type': 'text', 'text': prompt}]; source annotation list[str | dict[str, object]].
  // Source: vvaharness/backends/harness/deepagents/client.py:466-466
  End this invocation with blocks.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/client.py:469-477
// Source signature: _final_state(graph: CompiledStateGraph, config: RunnableConfig) -> DeepAgentsGraphState
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _final_state(graph, config) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  This callable produces a coroutine or async generator; await/suspension positions remain in source expressions.
  // Source: vvaharness/backends/harness/deepagents/client.py:472-472
  In source order: Retain source documentation literal source_literal_472_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/client.py:473-476
  Perform the following protected operations {
    // Source: vvaharness/backends/harness/deepagents/client.py:474-474
    In source order: Evaluate once await graph.aget_state(config); assign in source target order to snapshot.
  }
  // Source: vvaharness/backends/harness/deepagents/client.py:475-476
  On the first matching source exception ValueError, in handler order {
    // Source: vvaharness/backends/harness/deepagents/client.py:476-476
    End this invocation with {}.
  }
  // Source: vvaharness/backends/harness/deepagents/client.py:477-477
  End this invocation with cast('DeepAgentsGraphState', getattr(snapshot, 'values', None) or {}).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/client.py:480-662
interface DeepAgentHarness {
  Describe the source Python type, preserving its base/metaclass expression order: Harness.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/harness/deepagents/client.py:481-481
  In source order: Retain source documentation literal source_literal_481_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/client.py:483-515
  // Source signature: run_oneshot(self, prompt: str, options: OneShotOptions) -> OneShotResult
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn run_oneshot(self, prompt, options) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    This callable produces a coroutine or async generator; await/suspension positions remain in source expressions.
    // Source: vvaharness/backends/harness/deepagents/client.py:486-491
    In source order: Retain source documentation literal source_literal_486_8; it is not a model call. Then Evaluate once _sent_effort_tier(options); assign in source target order to sent_tier. Then Evaluate once build_oneshot_options(options); assign in source target order to (graph, config). Then Evaluate once _marked_content(prompt, options.cache_prefix); assign in source target order to content. Then Evaluate once _responses_active(options); assign in source target order to responses_active.
    // Source: vvaharness/backends/harness/deepagents/client.py:492-512
    Perform the following protected operations {
      // Source: vvaharness/backends/harness/deepagents/client.py:493-496
      In source order: Evaluate once await graph.ainvoke({'messages': [HumanMessage(content=content)]}, config=cast(RunnableConfig, config)); assign in source target order to state.
    }
    // Source: vvaharness/backends/harness/deepagents/client.py:497-512
    On the first matching source exception Exception as exc, in handler order {
      // Source: vvaharness/backends/harness/deepagents/client.py:498-511
      if (the source predicate sent_tier is not None and (effort_cls := classify_effort_rejection(exc)) is not None is truthy) {
        // Source: vvaharness/backends/harness/deepagents/client.py:500-507
        if (the source predicate _tools_off_exhausted(options.model, sent_tier, effort_cls) is truthy) {
          // Source: vvaharness/backends/harness/deepagents/client.py:501-502
          In source order: Evaluate EFFORT_REJECTIONS.tiers.add(_tiers_key(options.model, REASONING_OFF, _effort_transport(options))); retain side effects and discard the expression result.
          // Source: vvaharness/backends/harness/deepagents/client.py:503-507
          Raise RuntimeError(source_template_504_24) with explicit source cause exc.
        }
        // Source: vvaharness/backends/harness/deepagents/client.py:508-510
        In source order: Evaluate _step_down_reasoning_effort(options.model, sent_tier, effort_cls, exc, transport=_effort_transport(options)); retain side effects and discard the expression result.
        // Source: vvaharness/backends/harness/deepagents/client.py:511-511
        End this invocation with await self.run_oneshot(prompt, options).
      }
      // Source: vvaharness/backends/harness/deepagents/client.py:512-512
      End this invocation with await _recover_oneshot_exception(self, prompt, options, sent_tier, exc).
    }
    // Source: vvaharness/backends/harness/deepagents/client.py:513-514
    if (the source predicate responses_active is truthy) {
      // Source: vvaharness/backends/harness/deepagents/client.py:514-514
      In source order: Evaluate _RESPONSES_PROVEN_MODELS.add(options.model); retain side effects and discard the expression result.
    }
    // Source: vvaharness/backends/harness/deepagents/client.py:515-515
    End this invocation with translate_final_state(cast('DeepAgentsGraphState', state), oneshot=True).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/deepagents/client.py:517-550
  // Source signature: resume_streaming(self, instruction: str, options: StreamingOptions) -> AsyncIterator[HarnessMessage]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn resume_streaming(self, instruction, options) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/client.py:520-524
    In source order: Retain source documentation literal source_literal_520_8; it is not a model call. Then Evaluate once resumable(options.session_id); assign in source target order to held.
    // Source: vvaharness/backends/harness/deepagents/client.py:525-528
    if (the source predicate held is None is truthy) {
      // Source: vvaharness/backends/harness/deepagents/client.py:526-528
      Raise SessionNotResumableError(source_template_527_16).
    }
    // Source: vvaharness/backends/harness/deepagents/client.py:529-530
    In source order: Evaluate once held; assign in source target order to (graph, config). Then Evaluate once cast(RunnableConfig, config); assign in source target order to runnable_config.
    // Source: vvaharness/backends/harness/deepagents/client.py:532-548
    // Source signature: _gen() -> AsyncIterator[HarnessMessage]
    Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
    fn _gen() {
      Bind arguments/defaults/annotations exactly as the source signature specifies.
      This callable produces a coroutine or async generator; await/suspension positions remain in source expressions.
      // Source: vvaharness/backends/harness/deepagents/client.py:533-535
      In source order: For seen_tool_ids, assign set(); source annotation set[str]. Then For ns_to_agent, assign {}; source annotation dict[tuple[str, ...], str]. Then Evaluate once UsageAccumulator(); assign in source target order to usage_acc.
      // Source: vvaharness/backends/harness/deepagents/client.py:536-544
      Obtain/advance the following source async iterator by awaiting, without inventing parallel dispatch.
      for each event in graph.astream({'messages': [HumanMessage(content=instruction)]}, config=runnable_config, stream_mode='updates', subgraphs=True) {
        // Source: vvaharness/backends/harness/deepagents/client.py:542-542
        In source order: Evaluate usage_acc.add_event(event); retain side effects and discard the expression result.
        // Source: vvaharness/backends/harness/deepagents/client.py:543-544
        Obtain/advance the following source async iterator by awaiting, without inventing parallel dispatch.
        for each message in translate_stream_events(event, seen_tool_ids, ns_to_agent) {
          // Source: vvaharness/backends/harness/deepagents/client.py:544-544
          In source order: Yield message; suspend this generator until resumed.
        }
      }
      // Source: vvaharness/backends/harness/deepagents/client.py:545-548
      In source order: Evaluate once await _final_state(graph, runnable_config); assign in source target order to state. Then Yield make_terminal_result(state, session_id=options.session_id, stream_usage=usage_acc.snapshot()); suspend this generator until resumed.
      If execution reaches this end, finish with the source implicit None result.
    }
    // Source: vvaharness/backends/harness/deepagents/client.py:550-550
    End this invocation with _gen().
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/deepagents/client.py:552-662
  // Source signature: run_streaming(self, prompt: str, options: StreamingOptions) -> AsyncIterator[HarnessMessage]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn run_streaming(self, prompt, options) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/client.py:555-558
    In source order: Retain source documentation literal source_literal_555_8; it is not a model call. Then Evaluate once _sent_effort_tier(options); assign in source target order to sent_tier. Then Evaluate once build_streaming_agent(options); assign in source target order to (graph, config). Then Evaluate once cast(RunnableConfig, config); assign in source target order to runnable_config.
    // Source: vvaharness/backends/harness/deepagents/client.py:560-660
    // Source signature: _gen() -> AsyncIterator[HarnessMessage]
    Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
    fn _gen() {
      Bind arguments/defaults/annotations exactly as the source signature specifies.
      This callable produces a coroutine or async generator; await/suspension positions remain in source expressions.
      // Source: vvaharness/backends/harness/deepagents/client.py:562-568
      In source order: Evaluate once options.session_id or uuid4().hex; assign in source target order to session_id. Then For seen_tool_ids, assign set(); source annotation set[str]. Then For ns_to_agent, assign {}; source annotation dict[tuple[str, ...], str]. Then Evaluate once UsageAccumulator(); assign in source target order to usage_acc. Then Evaluate once _responses_active(options); assign in source target order to responses_active.
      // Source: vvaharness/backends/harness/deepagents/client.py:569-660
      Perform the following protected operations {
        // Source: vvaharness/backends/harness/deepagents/client.py:570-581
        In source order: Yield HarnessSessionInit(session_id=session_id); suspend this generator until resumed. Then Evaluate once graph.astream({'messages': [HumanMessage(content=_marked_content(prompt, options.cache_prefix))]}, config=runnable_config, stream_mode='updates', subgraphs=True); assign in source target order to stream. Then Evaluate once _bounded_astream_events(stream, options.timeout, options.graph_name, options.effort); assign in source target order to bounded_stream.
        // Source: vvaharness/backends/harness/deepagents/client.py:582-587
        Obtain/advance the following source async iterator by awaiting, without inventing parallel dispatch.
        for each event in bounded_stream {
          // Source: vvaharness/backends/harness/deepagents/client.py:583-583
          In source order: Evaluate usage_acc.add_event(event); retain side effects and discard the expression result.
          // Source: vvaharness/backends/harness/deepagents/client.py:584-587
          Obtain/advance the following source async iterator by awaiting, without inventing parallel dispatch.
          for each message in translate_stream_events(event, seen_tool_ids, ns_to_agent) {
            // Source: vvaharness/backends/harness/deepagents/client.py:587-587
            In source order: Yield message; suspend this generator until resumed.
          }
        }
        // Source: vvaharness/backends/harness/deepagents/client.py:588-589
        if (the source predicate responses_active is truthy) {
          // Source: vvaharness/backends/harness/deepagents/client.py:589-589
          In source order: Evaluate _RESPONSES_PROVEN_MODELS.add(options.model); retain side effects and discard the expression result.
        }
        // Source: vvaharness/backends/harness/deepagents/client.py:590-593
        In source order: Evaluate once await _final_state(graph, runnable_config); assign in source target order to state. Then Yield make_terminal_result(state, session_id=session_id, stream_usage=usage_acc.snapshot()); suspend this generator until resumed.
      }
      // Source: vvaharness/backends/harness/deepagents/client.py:594-595
      On the first matching source exception HarnessError, in handler order {
        // Source: vvaharness/backends/harness/deepagents/client.py:595-595
        Raise the currently handled exception.
      }
      // Source: vvaharness/backends/harness/deepagents/client.py:596-660
      On the first matching source exception Exception as error, in handler order {
        // Source: vvaharness/backends/harness/deepagents/client.py:597-601
        if (the source predicate _relearned_for_rerun(error, options, sent_tier, usage_acc) is truthy) {
          // Source: vvaharness/backends/harness/deepagents/client.py:598-598
          In source order: Evaluate _bank_partial_usage(usage_acc); retain side effects and discard the expression result.
          // Source: vvaharness/backends/harness/deepagents/client.py:599-600
          Obtain/advance the following source async iterator by awaiting, without inventing parallel dispatch.
          for each message in self.run_streaming(prompt, options) {
            // Source: vvaharness/backends/harness/deepagents/client.py:600-600
            In source order: Yield message; suspend this generator until resumed.
          }
          // Source: vvaharness/backends/harness/deepagents/client.py:601-601
          End this invocation with None.
        }
        // Source: vvaharness/backends/harness/deepagents/client.py:602-604
        In source order: Evaluate once _probe_lower_tier_once(options.model, sent_tier) if sent_tier is not None and _is_persistent_server_error(error) else None; assign in source target order to probed.
        // Source: vvaharness/backends/harness/deepagents/client.py:605-613
        if (the source predicate probed is not None and sent_tier is not None is truthy) {
          // Source: vvaharness/backends/harness/deepagents/client.py:606-608
          In source order: Evaluate _bank_partial_usage(usage_acc); retain side effects and discard the expression result. Then Evaluate once _StreamProbeContext(sent_tier, error, session_id, seen_tool_ids, ns_to_agent); assign in source target order to ctx.
          // Source: vvaharness/backends/harness/deepagents/client.py:609-612
          Obtain/advance the following source async iterator by awaiting, without inventing parallel dispatch.
          for each message in _probe_server_error_streaming(prompt, options, probed, ctx) {
            // Source: vvaharness/backends/harness/deepagents/client.py:612-612
            In source order: Yield message; suspend this generator until resumed.
          }
          // Source: vvaharness/backends/harness/deepagents/client.py:613-613
          End this invocation with None.
        }
        // Source: vvaharness/backends/harness/deepagents/client.py:614-643
        if (the source predicate _should_fall_back(error, options) is truthy) {
          // Source: vvaharness/backends/harness/deepagents/client.py:616-617
          In source order: Evaluate _learn_chat_completions_only(options.model); retain side effects and discard the expression result. Then Evaluate _bank_partial_usage(usage_acc); retain side effects and discard the expression result.
          // Source: vvaharness/backends/harness/deepagents/client.py:618-642
          Perform the following protected operations {
            // Source: vvaharness/backends/harness/deepagents/client.py:619-620
            Obtain/advance the following source async iterator by awaiting, without inventing parallel dispatch.
            for each message in self.run_streaming(prompt, options) {
              // Source: vvaharness/backends/harness/deepagents/client.py:620-620
              In source order: Yield message; suspend this generator until resumed.
            }
          }
          // Source: vvaharness/backends/harness/deepagents/client.py:621-642
          On the first matching source exception Exception as second_error, in handler order {
            // Source: vvaharness/backends/harness/deepagents/client.py:623-623
            In source order: Evaluate _CHAT_COMPLETIONS_ONLY_MODELS.discard(options.model); retain side effects and discard the expression result.
            // Source: vvaharness/backends/harness/deepagents/client.py:624-636
            if (the source predicate _is_missing_thought_signature(second_error) is truthy) {
              // Source: vvaharness/backends/harness/deepagents/client.py:626-628
              In source order: Evaluate once getattr(second_error, 'stderr', None) or str(second_error); assign in source target order to detail.
              // Source: vvaharness/backends/harness/deepagents/client.py:629-636
              Raise HarnessProcessError(source_template_630_32, exit_code=1, stderr=detail, recursion_limited=isinstance(second_error, GraphRecursionError)) with explicit source cause second_error.
            }
            // Source: vvaharness/backends/harness/deepagents/client.py:637-642
            Raise HarnessProcessError(source_template_638_28, exit_code=1, stderr=str(error), recursion_limited=isinstance(error, GraphRecursionError)) with explicit source cause error.
          }
          // Source: vvaharness/backends/harness/deepagents/client.py:643-643
          End this invocation with None.
        }
        // Source: vvaharness/backends/harness/deepagents/client.py:645-645
        In source order: Evaluate once isinstance(error, GraphRecursionError); assign in source target order to recursion_limited.
        // Source: vvaharness/backends/harness/deepagents/client.py:646-653
        if (the source predicate recursion_limited is truthy) {
          // Source: vvaharness/backends/harness/deepagents/client.py:647-650
          In source order: Evaluate once await _final_state(graph, runnable_config); assign in source target order to state. Then Yield make_terminal_result(state, session_id=session_id, stream_usage=usage_acc.snapshot()); suspend this generator until resumed.
        }
        else {
          // Source: vvaharness/backends/harness/deepagents/client.py:653-653
          In source order: Evaluate _bank_partial_usage(usage_acc); retain side effects and discard the expression result.
        }
        // Source: vvaharness/backends/harness/deepagents/client.py:655-660
        Raise HarnessProcessError(source_template_656_20, exit_code=1, stderr=str(error), recursion_limited=recursion_limited) with explicit source cause error.
      }
      If execution reaches this end, finish with the source implicit None result.
    }
    // Source: vvaharness/backends/harness/deepagents/client.py:662-662
    End this invocation with _gen().
    If execution reaches this end, finish with the source implicit None result.
  }
}
```

## Local import links

- `from vvaharness.backends.harness.deepagents.models import DeepAgentsGraphState` at source line 32: `source_detail/vvaharness/backends/harness/deepagents/models.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.options import build_oneshot_options, build_streaming_agent, resumable` at source line 33: `source_detail/vvaharness/backends/harness/deepagents/options/__init__.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.options.model_building import _CHAT_COMPLETIONS_ONLY_MODELS, _FORCED_TOOL_CHOICE_UNSUPPORTED_MODELS, _openai_effort_kwargs, resolve_use_responses_api` at source line 38: `source_detail/vvaharness/backends/harness/deepagents/options/model_building.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.tool_choice_rejection import is_tool_choice_unsupported_rejection, learn_tool_choice_unsupported, rejected_model` at source line 44: `source_detail/vvaharness/backends/harness/deepagents/tool_choice_rejection.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.translate import make_terminal_result, translate_final_state, translate_stream_events` at source line 49: `source_detail/vvaharness/backends/harness/deepagents/translate.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.usage import UsageAccumulator` at source line 54: `source_detail/vvaharness/backends/harness/deepagents/usage.py.sudo.md`.
- `from vvaharness.backends.harness.harness import Harness` at source line 55: `source_detail/vvaharness/backends/harness/harness.py.sudo.md`.
- `from vvaharness.backends.harness.models import HarnessError, HarnessMessage, HarnessProcessError, HarnessSessionInit, OneShotOptions, OneShotResult, SessionNotResumableError, SessionOptions, StreamingOptions` at source line 56: `source_detail/vvaharness/backends/harness/models.py.sudo.md`.
- `from vvaharness.backends.harness.provider_routing import TRANSPORT_CHAT_COMPLETIONS, TRANSPORT_RESPONSES, routes_to_anthropic` at source line 67: `source_detail/vvaharness/backends/harness/provider_routing.py.sudo.md`.
- `from vvaharness.backends.llm.models import EFFORT_REJECTIONS, REASONING_OFF, SERVER_ERROR_STATUS, TRANSPORT_MEMORY, _tiers_key, call_timeout_error, classify_effort_rejection, is_model_refusal_rejection, is_responses_shape_rejection, next_effort_tier, step_down` at source line 72: `source_detail/vvaharness/backends/llm/models.py.sudo.md`.
- `from vvaharness.util.counters import COUNTERS` at source line 85: `source_detail/vvaharness/util/counters.py.sudo.md`.
- `from vvaharness.util.exceptions import exception_chain` at source line 86: `source_detail/vvaharness/util/exceptions.py.sudo.md`.
- `from vvaharness.util.response_quality import is_connection_failure` at source line 87: `source_detail/vvaharness/util/response_quality.py.sudo.md`.
- `from vvaharness.util.tokens import TOKENS` at source line 88: `source_detail/vvaharness/util/tokens.py.sudo.md`.
- `from vvaharness.util.warn_once import warn_once` at source line 89: `source_detail/vvaharness/util/warn_once.py.sudo.md`.
