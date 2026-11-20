# vvaharness/remediation_agent/plugin_runner/__init__.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/remediation_agent/plugin_runner/__init__.py.evidence.json`. SHA-256: `163284d0db6e51070f0fc63a4ff5d34a194054f28a0e61dc70a1e22bc1cc78b5`.

```sudo
// Source: vvaharness/remediation_agent/plugin_runner/__init__.py:15-20
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import asyncio; preserve alias and import-time effects. Then Resolve source import import json; preserve alias and import-time effects. Then Resolve source import import os; preserve alias and import-time effects.
// Source: vvaharness/remediation_agent/plugin_runner/__init__.py:21-35
In source order: Resolve source import import threading; preserve alias and import-time effects. Then Resolve source import from collections.abc import Coroutine; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from typing import Any, TypeVar; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness import HarnessAssistantText, HarnessResult, HarnessToolResult, HarnessToolUse, StreamingOptions, SubagentDefinition, ToolPolicy, get_harness; preserve alias and import-time effects.
// Source: vvaharness/remediation_agent/plugin_runner/__init__.py:36-40
In source order: Resolve source import from vvaharness.backends.harness.deepagents.limits import RECURSION_HEADROOM; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.deepagents.model_call_budget import ModelCallBudget; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.provider_routing import credential_env_overrides; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.repeat_guard import guard_repeats; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm.cli import stream_trace; preserve alias and import-time effects.
// Source: vvaharness/remediation_agent/plugin_runner/__init__.py:41-49
In source order: Resolve source import from vvaharness.backends.llm.deepagents import markers_on, raise_if_refused; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm.models import ModelRefusal, call_timeout_error, model_refusal_from; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm.registry import agentic, use_responses_api_of; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm.registry import resolve as resolve_model; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.models import FixerResult, RemediationVerdict; preserve alias and import-time effects.
// Source: vvaharness/remediation_agent/plugin_runner/__init__.py:50-68
In source order: Resolve source import from vvaharness.remediation_agent.plugin_runner.handoff import FixerDispatchGuard; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.plugin_runner.helpers import _build_user, _coerce_verdict, _tools; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.plugin_runner.run import ENGINE_ID, Amended, EngineRequest, GuardedCall, apply_plugin, call_with_guards, checkpoint_record, engine_model, harness_amend; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.plugin_runner.trace import dump as _dump; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.plugin_runner.trace import dump_policy as _dump_policy; preserve alias and import-time effects.
// Source: vvaharness/remediation_agent/plugin_runner/__init__.py:69-77
In source order: Resolve source import from vvaharness.remediation_agent.policy import describe_escapes, escaping_symlinks; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.prompts import FIXER_SYSTEM, ORCHESTRATOR_SYSTEM, SYSTEM; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.target import RemediationTarget; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import console; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.json_extract import extract_json; preserve alias and import-time effects.
// Source: vvaharness/remediation_agent/plugin_runner/__init__.py:78-87
In source order: Resolve source import from vvaharness.util.tokens import TOKENS; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.warn_once import warn_once; preserve alias and import-time effects. Then Evaluate once ['ENGINE_ID', 'Amended', 'EngineRequest', 'GuardedCall', 'apply_plugin', 'call_with_guards', 'checkpoint_record', 'engine_model', 'harness_amend']; assign in source target order to __all__. Then Evaluate once TypeVar('_T'); assign in source target order to _T.
// Source: vvaharness/remediation_agent/plugin_runner/__init__.py:89-110
// Source signature: _run_sync(awaitable: Coroutine[Any, Any, _T]) -> _T
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _run_sync(awaitable) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:90-90
  In source order: Retain source documentation literal source_literal_90_4; it is not a model call.
  // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:91-94
  Perform the following protected operations {
    // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:92-92
    In source order: Evaluate asyncio.get_running_loop(); retain side effects and discard the expression result.
  }
  // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:93-94
  On the first matching source exception RuntimeError, in handler order {
    // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:94-94
    End this invocation with asyncio.run(awaitable).
  }
  // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:96-97
  In source order: For result, assign []; source annotation list[_T]. Then For error, assign []; source annotation list[BaseException].
  // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:99-103
  // Source signature: worker() -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn worker() {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:100-103
    Perform the following protected operations {
      // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:101-101
      In source order: Evaluate result.append(asyncio.run(awaitable)); retain side effects and discard the expression result.
    }
    // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:102-103
    On the first matching source exception BaseException as exc, in handler order {
      // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:103-103
      In source order: Evaluate error.append(exc); retain side effects and discard the expression result.
    }
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:105-107
  In source order: Evaluate once threading.Thread(target=worker, name='vvaharness-remediation', daemon=True); assign in source target order to thread. Then Evaluate thread.start(); retain side effects and discard the expression result. Then Evaluate thread.join(); retain side effects and discard the expression result.
  // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:108-109
  if (the source predicate error is truthy) {
    // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:109-109
    Raise error[0].
  }
  // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:110-110
  End this invocation with result[0].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/plugin_runner/__init__.py:113-115
// Source signature: _timeout_of(sr: Any) -> int
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _timeout_of(sr) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:114-114
  In source order: Retain source documentation literal source_literal_114_4; it is not a model call.
  // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:115-115
  End this invocation with int(getattr(sr, 'timeout', 3600) or 3600).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/plugin_runner/__init__.py:118-120
// Source signature: _max_model_calls_of(sr: Any) -> int
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _max_model_calls_of(sr) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:119-119
  In source order: Retain source documentation literal source_literal_119_4; it is not a model call.
  // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:120-120
  End this invocation with int(getattr(sr, 'max_model_calls', 0) or 0).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/plugin_runner/__init__.py:123-133
// Source signature: _remediate_call_budget(sr: Any) -> ModelCallBudget | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _remediate_call_budget(sr) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:124-125
  In source order: Retain source documentation literal source_literal_124_4; it is not a model call. Then Evaluate once _max_model_calls_of(sr); assign in source target order to limit.
  // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:126-127
  if (the source predicate limit <= 0 is truthy) {
    // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:127-127
    End this invocation with None.
  }
  // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:128-133
  End this invocation with ModelCallBudget(limit=limit, outcome_tools=frozenset({RemediationVerdict.__name__}), counter='s10_model_call_budget_final_turn', stage='s10').
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/plugin_runner/__init__.py:136-142
// Source signature: _debug_log(event: str, detail: str='') -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _debug_log(event, detail) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:137-138
  In source order: Retain source documentation literal source_literal_137_4; it is not a model call. Then Evaluate once os.environ.get('VVAHARNESS_DEBUG_LOG'); assign in source target order to path.
  // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:139-140
  if (the source predicate not path is truthy) {
    // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:140-140
    End this invocation with None.
  }
  // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:141-142
  Enter source context managers left-to-right: open(path, 'a', encoding='utf-8') bound to fh {
    // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:142-142
    In source order: Evaluate fh.write(source_template_142_17); retain side effects and discard the expression result.
  }
  Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/plugin_runner/__init__.py:145-152
// Source signature: _terminal_stats(terminal: HarnessResult) -> tuple[int, int, str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _terminal_stats(terminal) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:146-150
  In source order: Retain source documentation literal source_literal_146_4; it is not a model call. Then Evaluate once (getattr(terminal, 'state', None) or {}).get('messages', []); assign in source target order to messages. Then Evaluate once sum((len(getattr(m, 'tool_calls', None) or []) for m in messages)); assign in source target order to tool_calls. Then Evaluate once messages[-1] if messages else None; assign in source target order to last. Then Evaluate once bool(getattr(last, 'tool_calls', None)) and type(last).__name__ == 'AIMessage'; assign in source target order to pending.
  // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:151-151
  In source order: Evaluate once 'pending_tool_call(loop_truncated)' if pending else type(last).__name__ if last else 'empty'; assign in source target order to shape.
  // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:152-152
  End this invocation with (len(messages), tool_calls, shape).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/plugin_runner/__init__.py:155-170
// Source signature: _debug_terminal(terminal: HarnessResult) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _debug_terminal(terminal) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:156-156
  In source order: Retain source documentation literal source_literal_156_4; it is not a model call.
  // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:157-158
  if (the source predicate not os.environ.get('VVAHARNESS_DEBUG_LOG') is truthy) {
    // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:158-158
    End this invocation with None.
  }
  // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:159-163
  In source order: Evaluate once _terminal_stats(terminal); assign in source target order to (n_msgs, n_calls, shape). Then Evaluate _debug_log('TERMINAL.structured_is_none', str(terminal.structured is None)); retain side effects and discard the expression result. Then Evaluate _debug_log('TERMINAL.structured', repr(terminal.structured)[:600]); retain side effects and discard the expression result. Then Evaluate _debug_log('TERMINAL.result_text', repr(terminal.result_text)[:600]); retain side effects and discard the expression result. Then Evaluate _debug_log('TERMINAL.stats', source_template_163_33); retain side effects and discard the expression result.
  // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:164-170
  for each msg in (getattr(terminal, 'state', None) or {}).get('messages', [])[-8:] {
    // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:165-170
    In source order: Evaluate once getattr(msg, 'tool_calls', None) or []; assign in source target order to tool_calls. Then Evaluate _debug_log(source_template_167_12, source_template_168_12); retain side effects and discard the expression result.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/plugin_runner/__init__.py:173-187
// Source signature: _report_recursion_limit(terminal: HarnessResult, options: StreamingOptions) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _report_recursion_limit(terminal, options) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:174-186
  In source order: Retain source documentation literal source_literal_174_4; it is not a model call. Then Evaluate once _terminal_stats(terminal); assign in source target order to (n_msgs, n_calls, shape). Then Evaluate once (options.max_turns or 50) + RECURSION_HEADROOM; assign in source target order to limit. Then Evaluate once source_template_178_8; assign in source target order to msg. Then Evaluate console.write(msg); retain side effects and discard the expression result.
  // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:187-187
  In source order: Evaluate _debug_log('RECURSION_LIMIT_HIT', source_template_187_38); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/plugin_runner/__init__.py:190-196
// Source signature: _verdict_extraction_prompt() -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _verdict_extraction_prompt() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:191-191
  In source order: Evaluate once json.dumps(RemediationVerdict.model_json_schema(), separators=(',', ':')); assign in source target order to schema.
  // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:192-196
  End this invocation with source_template_193_8.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/plugin_runner/__init__.py:199-224
// Source signature: _extract_verdict_from_history(terminal: HarnessResult, options: StreamingOptions) -> dict | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _extract_verdict_from_history(terminal, options) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:202-206
  In source order: Retain source documentation literal source_literal_202_4; it is not a model call. Then Resolve source import from langchain_core.messages import HumanMessage; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.deepagents.options import build_model_cached; preserve alias and import-time effects. Then Evaluate once (getattr(terminal, 'state', None) or {}).get('messages', []); assign in source target order to messages.
  // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:207-208
  if (the source predicate not messages is truthy) {
    // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:208-208
    End this invocation with None.
  }
  // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:209-214
  In source order: Evaluate once build_model_cached(options.model, options.env, options.model_provider, use_responses_api=options.use_responses_api); assign in source target order to model.
  // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:215-224
  Perform the following protected operations {
    // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:216-217
    In source order: Evaluate once model.invoke([*messages, HumanMessage(content=_verdict_extraction_prompt())]); assign in source target order to response. Then Evaluate once extract_json(getattr(response, 'content', '') or ''); assign in source target order to data.
    // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:218-219
    if (the source predicate isinstance(data, dict) is truthy) {
      // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:219-219
      End this invocation with data.
    }
    // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:220-220
    In source order: Evaluate _debug_log('EXTRACTION_NOT_A_DICT', repr(data)[:200]); retain side effects and discard the expression result.
    // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:221-221
    End this invocation with None.
  }
  // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:222-224
  On the first matching source exception Exception as exc, in handler order {
    // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:223-223
    In source order: Evaluate _debug_log('EXTRACTION_FAILED', source_template_223_40); retain side effects and discard the expression result.
    // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:224-224
    End this invocation with None.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/plugin_runner/__init__.py:227-245
// Source signature: _attempt_extraction(terminal: HarnessResult, options: StreamingOptions) -> Any
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _attempt_extraction(terminal, options) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:228-237
  In source order: Retain source documentation literal source_literal_228_4; it is not a model call. Then Evaluate once sum((len(getattr(m, 'tool_calls', None) or []) for m in (getattr(terminal, 'state', None) or {}).get('messages', []))); assign in source target order to n_tool_calls. Then Evaluate console.write(source_template_234_8); retain side effects and discard the expression result. Then Evaluate once _extract_verdict_from_history(terminal, options); assign in source target order to extracted.
  // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:238-240
  if (the source predicate extracted is not None is truthy) {
    // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:239-239
    In source order: Evaluate _debug_log('EXTRACTION_RESULT', repr(extracted)[:400]); retain side effects and discard the expression result.
    // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:240-240
    End this invocation with extracted.
  }
  // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:241-244
  In source order: Evaluate console.write(source_template_242_8); retain side effects and discard the expression result.
  // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:245-245
  End this invocation with terminal.result_text or ''.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/plugin_runner/__init__.py:248-301
// Source signature: _consume_deepagents(prompt: str, options: StreamingOptions, *, verbose: bool) -> Any
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _consume_deepagents(prompt, options, verbose) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  This callable produces a coroutine or async generator; await/suspension positions remain in source expressions.
  // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:250-254
  In source order: Retain source documentation literal source_literal_250_4; it is not a model call. Then Resolve source import from vvaharness.backends.harness import HarnessProcessError; preserve alias and import-time effects. Then For terminal, assign None; source annotation HarnessResult | None. Then For recursion_error, assign None; source annotation BaseException | None. Then For refusal, assign None; source annotation ModelRefusal | None.
  // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:255-282
  Perform the following protected operations {
    // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:256-257
    In source order: Evaluate once guard_repeats(get_harness('deepagents').run_streaming(prompt, options), stage='s10', route='deepagents'); assign in source target order to stream.
    // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:258-273
    Obtain/advance the following source async iterator by awaiting, without inventing parallel dispatch.
    for each message in stream {
      // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:259-273
      if (the source predicate isinstance(message, HarnessResult) is truthy) {
        // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:260-260
        In source order: Evaluate once message; assign in source target order to terminal.
      }
      else {
        // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:261-273
        if (the source predicate isinstance(message, HarnessAssistantText) is truthy) {
          // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:262-262
          In source order: Evaluate _debug_log('ASSISTANT_TEXT', message.text[:200]); retain side effects and discard the expression result.
          // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:263-264
          if (the source predicate verbose is truthy) {
            // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:264-264
            In source order: Evaluate _dump('ASSISTANT', message.text); retain side effects and discard the expression result.
          }
        }
        else {
          // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:265-273
          if (the source predicate isinstance(message, HarnessToolUse) is truthy) {
            // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:266-266
            In source order: Evaluate _debug_log('TOOL_USE', source_template_266_39); retain side effects and discard the expression result.
            // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:267-268
            if (the source predicate verbose is truthy) {
              // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:268-268
              In source order: Evaluate _dump(source_template_268_26, str(message.input)); retain side effects and discard the expression result.
            }
          }
          else {
            // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:269-273
            if (the source predicate isinstance(message, HarnessToolResult) is truthy) {
              // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:271-271
              In source order: Evaluate _debug_log('TOOL_RESULT', str(message.content)[:200]); retain side effects and discard the expression result.
              // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:272-273
              if (the source predicate verbose is truthy) {
                // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:273-273
                In source order: Evaluate _dump('TOOL RESULT', str(message.content)); retain side effects and discard the expression result.
              }
            }
          }
        }
      }
    }
  }
  // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:274-282
  On the first matching source exception Exception as exc, in handler order {
    // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:277-279
    In source order: Evaluate once model_refusal_from(exc, route='deepagents', stage='s10'); assign in source target order to refusal. Then Evaluate once isinstance(exc, HarnessProcessError) and (getattr(exc, 'recursion_limited', False) or 'GraphRecursionError' in str(exc)); assign in source target order to recursion.
    // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:280-281
    if (the source predicate refusal is None and (not (recursion and terminal is not None)) is truthy) {
      // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:281-281
      Raise the currently handled exception.
    }
    // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:282-282
    In source order: Evaluate once exc; assign in source target order to recursion_error.
  }
  // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:283-285
  if (the source predicate refusal is not None is truthy) {
    // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:285-285
    Raise refusal.
  }
  // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:286-287
  if (the source predicate terminal is None is truthy) {
    // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:287-287
    Raise RuntimeError('DeepAgents remediation ended without a terminal result').
  }
  // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:288-290
  In source order: Evaluate _debug_terminal(terminal); retain side effects and discard the expression result. Then Evaluate raise_if_refused(terminal, tag='s10'); retain side effects and discard the expression result.
  // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:291-293
  if (the source predicate terminal.is_error and recursion_error is None is truthy) {
    // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:292-293
    Raise RuntimeError(source_template_293_12).
  }
  // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:294-295
  if (the source predicate terminal.structured is not None is truthy) {
    // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:295-295
    End this invocation with terminal.structured.
  }
  // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:296-297
  if (the source predicate recursion_error is not None is truthy) {
    // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:297-297
    In source order: Evaluate _report_recursion_limit(terminal, options); retain side effects and discard the expression result.
  }
  // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:298-298
  In source order: Evaluate once _attempt_extraction(terminal, options); assign in source target order to result.
  // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:299-300
  if (the source predicate result is not None or recursion_error is None is truthy) {
    // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:300-300
    End this invocation with result.
  }
  // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:301-301
  Raise recursion_error.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/plugin_runner/__init__.py:304-319
// Source signature: _consume_deepagents_bounded(prompt: str, options: StreamingOptions, *, verbose: bool, timeout: int) -> Any
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _consume_deepagents_bounded(prompt, options, verbose, timeout) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  This callable produces a coroutine or async generator; await/suspension positions remain in source expressions.
  // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:306-309
  In source order: Retain source documentation literal source_literal_306_4; it is not a model call. Then Evaluate once asyncio.timeout(timeout); assign in source target order to deadline.
  // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:310-319
  Perform the following protected operations {
    // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:311-312
    Await and enter source context managers left-to-right: deadline {
      // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:312-312
      End this invocation with await _consume_deepagents(prompt, options, verbose=verbose).
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics and await async exits.
  }
  // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:313-319
  On the first matching source exception TimeoutError as exc, in handler order {
    // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:315-316
    if (the source predicate not deadline.expired() is truthy) {
      // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:316-316
      Raise the currently handled exception.
    }
    // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:317-319
    Raise call_timeout_error(stage='s10', route='deepagents', budget_s=timeout, effort=None, cause_text=source_template_319_23) with explicit source cause exc.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/plugin_runner/__init__.py:322-327
// Source signature: _virtualize_deepagents_prompt(user: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _virtualize_deepagents_prompt(user) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:323-324
  In source order: Retain source documentation literal source_literal_323_4; it is not a model call. Then Evaluate once user.splitlines(); assign in source target order to lines.
  // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:325-326
  if (the source predicate lines and lines[0].startswith('REPOSITORY ROOT:') is truthy) {
    // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:326-326
    In source order: Evaluate once 'REPOSITORY ROOT: / (DeepAgents virtual workspace root)'; assign in source target order to lines[0].
  }
  // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:327-327
  End this invocation with source_literal_327_11.join(lines).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/plugin_runner/__init__.py:330-388
// Source signature: _invoke_deepagents(user: str, *, model_id: str, repo: Path, mode: str, sr: Any, cfg: Any, verbose: bool, provider: str | None=None, use_responses_api: bool | None=None, primary_file: str='') -> Any
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _invoke_deepagents(user, model_id, repo, mode, sr, cfg, verbose, provider, use_responses_api, primary_file) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:335-346
  In source order: Evaluate once tuple((t for t in _tools(cfg) if t != 'Bash')); assign in source target order to tools. Then Evaluate once mode == 'fix'; assign in source target order to fix_mode. Then Evaluate once {**os.environ, **credential_env_overrides(model_id, provider, sdk_cfg=getattr(cfg, 'sdk', None), openai_cfg=getattr(cfg, 'openai', None))}; assign in source target order to env. Then For agents, assign {}; source annotation dict[str, SubagentDefinition].
  // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:347-359
  if (the source predicate fix_mode is truthy) {
    // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:348-359
    In source order: Evaluate once tuple(dict.fromkeys((*tools, 'Edit'))); assign in source target order to fixer_tools. Then Evaluate once {'fixer': SubagentDefinition(name='fixer', description='Applies the security fix to the target file(s).', prompt=FIXER_SYSTEM, tools=fixer_tools, response_model=FixerResult, max_model_calls=_max_model_calls_of(sr))}; assign in source target order to agents.
  }
  // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:360-386
  In source order: Evaluate once StreamingOptions(model=model_id, model_provider=provider, use_responses_api=use_responses_api, cwd=repo, env=env, max_turns=getattr(sr, 'max_turns', 40), max_budget_usd=getattr(sr, 'max_budget_usd', 10.0), system_prompt=ORCHESTRATOR_SYSTEM if fix_mode else SYSTEM, tool_policy=ToolPolicy(allowed_tools=tools, disallowed_tools=('Bash',)), response_model=RemediationVerdict, force_verdict_only=True, allow_writes=fix_mode, writable_paths=(str(repo.resolve()),) if fix_mode else (), graph_name='remediation', agents=agents, parent_middleware=tuple((m for m in (FixerDispatchGuard(finding_context=user, primary_file=primary_file) if fix_mode else None, _remediate_call_budget(sr)) if m is not None)), cache_markers=markers_on(getattr(cfg, 'sdk', None))); assign in source target order to options.
  // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:387-388
  End this invocation with _run_sync(_consume_deepagents_bounded(user, options, verbose=verbose, timeout=_timeout_of(sr))).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/plugin_runner/__init__.py:392-394
In source order: For _WARNED_CLI_REDACTION, assign set(); source annotation set[str]. Then For _WARNED_SYMLINK_ESCAPE, assign set(); source annotation set[str].
// Source: vvaharness/remediation_agent/plugin_runner/__init__.py:397-432
// Source signature: _invoke_cli(user: str, *, cfg, repo: Path, mode: str, sr: Any, verbose: bool, tag: str) -> Any
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _invoke_cli(user, cfg, repo, mode, sr, verbose, tag) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:399-402
  In source order: Retain source documentation literal source_literal_399_4; it is not a model call. Then Evaluate once mode == 'fix'; assign in source target order to fix_mode. Then Evaluate once [t for t in _tools(cfg) if t != 'Bash']; assign in source target order to tools.
  // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:403-413
  if (the source predicate fix_mode is truthy) {
    // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:405-413
    In source order: Evaluate once list(dict.fromkeys([*tools, 'Edit', 'Write'])); assign in source target order to tools. Then Evaluate warn_once(_WARNED_CLI_REDACTION, 'cli-fix-redaction', source_literal_408_12); retain side effects and discard the expression result.
  }
  // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:414-432
  End this invocation with agentic(user, model=cfg.models.remediate, system_prompt=SYSTEM, allowed_tools=tools, cwd=str(repo), max_budget_usd=getattr(sr, 'max_budget_usd', 10.0), max_turns=getattr(sr, 'max_turns', 40), timeout=_timeout_of(sr), tag=tag, stream_cb=stream_trace if verbose else None, json_schema=RemediationVerdict.model_json_schema(), disallowed_tools=['Bash'], permission_mode='acceptEdits' if fix_mode else 'default', permission_prompts='none').
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/plugin_runner/__init__.py:435-458
// Source signature: _symlink_safe_mode(repo: Path, mode: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _symlink_safe_mode(repo, mode) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:436-444
  In source order: Retain source documentation literal source_literal_436_4; it is not a model call.
  // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:445-446
  if (the source predicate mode != 'fix' is truthy) {
    // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:446-446
    End this invocation with mode.
  }
  // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:447-447
  In source order: Evaluate once escaping_symlinks(repo); assign in source target order to escapes.
  // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:448-449
  if (the source predicate not escapes is truthy) {
    // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:449-449
    End this invocation with mode.
  }
  // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:450-457
  In source order: Evaluate warn_once(_WARNED_SYMLINK_ESCAPE, 'fix-symlink-escape', source_template_452_8); retain side effects and discard the expression result.
  // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:458-458
  End this invocation with 'report'.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/plugin_runner/__init__.py:461-505
// Source signature: _invoke(target: RemediationTarget, cfg, repo: Path, mode: str, verbose: bool=False, *, pre=None, ctx=None) -> Any
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _invoke(target, cfg, repo, mode, verbose, pre, ctx) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:463-467
  In source order: Retain source documentation literal source_literal_463_4; it is not a model call. Then Evaluate once getattr(cfg, 'step_remediate', None); assign in source target order to sr. Then Evaluate once _build_user(target, repo, mode, pre=pre, ctx=ctx); assign in source target order to user. Then Evaluate once resolve_model(cfg.models.remediate); assign in source target order to (model_id, via, _). Then Evaluate once getattr(cfg.models.remediate, 'provider', None); assign in source target order to provider.
  // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:468-468
  In source order: Evaluate once _symlink_safe_mode(repo, mode); assign in source target order to mode.
  // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:469-470
  if (the source predicate via == 'deepagents' is truthy) {
    // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:470-470
    In source order: Evaluate once _virtualize_deepagents_prompt(user); assign in source target order to user.
  }
  // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:471-472
  if (the source predicate verbose is truthy) {
    // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:472-472
    In source order: Evaluate _dump(source_template_472_14, user); retain side effects and discard the expression result.
  }
  // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:473-501
  Enter source context managers left-to-right: TOKENS.phase('remediation-agent-remediate') {
    // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:474-501
    if (the source predicate via == 'deepagents' is truthy) {
      // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:475-479
      In source order: Evaluate once _invoke_deepagents(user, model_id=model_id, repo=repo, mode=mode, sr=sr, cfg=cfg, verbose=verbose, provider=provider, use_responses_api=use_responses_api_of(cfg.models.remediate), primary_file=target.file); assign in source target order to raw.
    }
    else {
      // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:480-501
      if (the source predicate via == 'cli' is truthy) {
        // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:481-483
        In source order: Evaluate once _invoke_cli(user, cfg=cfg, repo=repo, mode=mode, sr=sr, verbose=verbose, tag=source_template_483_20); assign in source target order to raw.
      }
      else {
        // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:486-487
        In source order: Evaluate once mode == 'fix'; assign in source target order to fix_mode. Then Evaluate once [t for t in _tools(cfg) if t not in ('Edit', 'Write')]; assign in source target order to tools.
        // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:488-489
        if (the source predicate fix_mode is truthy) {
          // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:489-489
          In source order: Evaluate once list(dict.fromkeys([*tools, 'Edit', 'Write'])); assign in source target order to tools.
        }
        // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:490-501
        In source order: Evaluate once agentic(user, model=cfg.models.remediate, system_prompt=SYSTEM, allowed_tools=tools, cwd=str(repo), max_budget_usd=getattr(sr, 'max_budget_usd', 10.0), max_turns=getattr(sr, 'max_turns', 40), timeout=_timeout_of(sr), tag=source_template_499_20, stream_cb=stream_trace if verbose else None); assign in source target order to raw.
      }
    }
  }
  Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
  // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:502-504
  if (the source predicate verbose is truthy) {
    // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:503-504
    In source order: Evaluate once raw.model_dump_json() if isinstance(raw, RemediationVerdict) else str(raw); assign in source target order to body. Then Evaluate _dump(source_template_504_14, body); retain side effects and discard the expression result.
  }
  // Source: vvaharness/remediation_agent/plugin_runner/__init__.py:505-505
  End this invocation with raw.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.backends.harness import HarnessAssistantText, HarnessResult, HarnessToolResult, HarnessToolUse, StreamingOptions, SubagentDefinition, ToolPolicy, get_harness` at source line 26: `source_detail/vvaharness/backends/harness/__init__.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.limits import RECURSION_HEADROOM` at source line 36: `source_detail/vvaharness/backends/harness/deepagents/limits.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.model_call_budget import ModelCallBudget` at source line 37: `source_detail/vvaharness/backends/harness/deepagents/model_call_budget.py.sudo.md`.
- `from vvaharness.backends.harness.provider_routing import credential_env_overrides` at source line 38: `source_detail/vvaharness/backends/harness/provider_routing.py.sudo.md`.
- `from vvaharness.backends.harness.repeat_guard import guard_repeats` at source line 39: `source_detail/vvaharness/backends/harness/repeat_guard.py.sudo.md`.
- `from vvaharness.backends.llm.cli import stream_trace` at source line 40: `source_detail/vvaharness/backends/llm/cli/__init__.py.sudo.md`.
- `from vvaharness.backends.llm.deepagents import markers_on, raise_if_refused` at source line 41: `source_detail/vvaharness/backends/llm/deepagents.py.sudo.md`.
- `from vvaharness.backends.llm.models import ModelRefusal, call_timeout_error, model_refusal_from` at source line 42: `source_detail/vvaharness/backends/llm/models.py.sudo.md`.
- `from vvaharness.backends.llm.registry import agentic, use_responses_api_of` at source line 47: `source_detail/vvaharness/backends/llm/registry.py.sudo.md`.
- `from vvaharness.backends.llm.registry import resolve as resolve_model` at source line 48: `source_detail/vvaharness/backends/llm/registry.py.sudo.md`.
- `from vvaharness.remediation_agent.models import FixerResult, RemediationVerdict` at source line 49: `source_detail/vvaharness/remediation_agent/models/__init__.py.sudo.md`.
- `from vvaharness.remediation_agent.plugin_runner.handoff import FixerDispatchGuard` at source line 50: `source_detail/vvaharness/remediation_agent/plugin_runner/handoff.py.sudo.md`.
- `from vvaharness.remediation_agent.plugin_runner.helpers import _build_user, _coerce_verdict, _tools` at source line 51: `source_detail/vvaharness/remediation_agent/plugin_runner/helpers.py.sudo.md`.
- `from vvaharness.remediation_agent.plugin_runner.run import ENGINE_ID, Amended, EngineRequest, GuardedCall, apply_plugin, call_with_guards, checkpoint_record, engine_model, harness_amend` at source line 56: `source_detail/vvaharness/remediation_agent/plugin_runner/run.py.sudo.md`.
- `from vvaharness.remediation_agent.plugin_runner.trace import dump as _dump` at source line 67: `source_detail/vvaharness/remediation_agent/plugin_runner/trace.py.sudo.md`.
- `from vvaharness.remediation_agent.plugin_runner.trace import dump_policy as _dump_policy` at source line 68: `source_detail/vvaharness/remediation_agent/plugin_runner/trace.py.sudo.md`.
- `from vvaharness.remediation_agent.policy import describe_escapes, escaping_symlinks` at source line 69: `source_detail/vvaharness/remediation_agent/policy/__init__.py.sudo.md`.
- `from vvaharness.remediation_agent.prompts import FIXER_SYSTEM, ORCHESTRATOR_SYSTEM, SYSTEM` at source line 70: `source_detail/vvaharness/remediation_agent/prompts.py.sudo.md`.
- `from vvaharness.remediation_agent.target import RemediationTarget` at source line 75: `source_detail/vvaharness/remediation_agent/target.py.sudo.md`.
- `from vvaharness.util import console` at source line 76: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import console` at source line 76: `source_detail/vvaharness/util/console.py.sudo.md`.
- `from vvaharness.util.json_extract import extract_json` at source line 77: `source_detail/vvaharness/util/json_extract.py.sudo.md`.
- `from vvaharness.util.tokens import TOKENS` at source line 78: `source_detail/vvaharness/util/tokens.py.sudo.md`.
- `from vvaharness.util.warn_once import warn_once` at source line 79: `source_detail/vvaharness/util/warn_once.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.options import build_model_cached` at source line 205: `source_detail/vvaharness/backends/harness/deepagents/options/__init__.py.sudo.md`.
- `from vvaharness.backends.harness import HarnessProcessError` at source line 251: `source_detail/vvaharness/backends/harness/__init__.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../prompt_representation/vvaharness/remediation_agent/plugin_runner/__init__.py.sudo.md). Exact strings in the evidence asset support this conversion.
