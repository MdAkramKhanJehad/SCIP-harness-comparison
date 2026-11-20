# vvaharness/backends/harness/claude/client.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/backends/harness/claude/client.py.evidence.json`. SHA-256: `04be1f27a29f76e86eb707a6266490865d4cb3eca8fbbaba16d345854ed65441`.

```sudo
// Source: vvaharness/backends/harness/claude/client.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import asyncio; preserve alias and import-time effects. Then Resolve source import import contextlib; preserve alias and import-time effects. Then Resolve source import import json; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/claude/client.py:22-34
In source order: Resolve source import from collections.abc import AsyncIterator; preserve alias and import-time effects. Then Resolve source import from typing import cast; preserve alias and import-time effects. Then Resolve source import from claude_agent_sdk import ClaudeSDKClient, CLIConnectionError, CLIJSONDecodeError, CLINotFoundError, ProcessError, ResultMessage; preserve alias and import-time effects. Then Resolve source import from claude_agent_sdk._errors import MessageParseError; preserve alias and import-time effects. Then Resolve source import from pydantic import BaseModel; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/claude/client.py:36-43
In source order: Resolve source import from vvaharness.backends.harness.claude.facts import build_fact_mcp; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.claude.models import SDK_ERROR_MAP; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.claude.options import build_oneshot_sdk_options, build_streaming_sdk_options; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.claude.translate import translate, validate_structured; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.harness import Harness; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/claude/client.py:44-54
In source order: Resolve source import from vvaharness.backends.harness.models import HarnessCLINotFoundError, HarnessMessage, HarnessProcessError, HarnessResult, OneShotOptions, OneShotResult, StreamingOptions; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm.models import TIMEOUT_STOP_GRACE_SECONDS, call_timeout_error; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.tokens import TOKENS, TokenUsage; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/claude/client.py:57-66
// Source signature: _persona_report_model() -> type | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _persona_report_model() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/claude/client.py:58-58
  In source order: Retain source documentation literal source_literal_58_4; it is not a model call.
  // Source: vvaharness/backends/harness/claude/client.py:60-65
  Perform the following protected operations {
    // Source: vvaharness/backends/harness/claude/client.py:61-63
    In source order: Resolve source import from vvaharness.validation.models.persona_report import PersonaReport; preserve alias and import-time effects.
  }
  // Source: vvaharness/backends/harness/claude/client.py:64-65
  On the first matching source exception Exception, in handler order {
    // Source: vvaharness/backends/harness/claude/client.py:65-65
    End this invocation with None.
  }
  // Source: vvaharness/backends/harness/claude/client.py:66-66
  End this invocation with PersonaReport.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/claude/client.py:69-111
// Source signature: _extract_sdk_persona_reports(session_id: str, cwd: object) -> list[dict]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _extract_sdk_persona_reports(session_id, cwd) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/claude/client.py:70-70
  In source order: Retain source documentation literal source_literal_70_4; it is not a model call.
  // Source: vvaharness/backends/harness/claude/client.py:71-77
  Perform the following protected operations {
    // Source: vvaharness/backends/harness/claude/client.py:72-75
    In source order: Resolve source import from claude_agent_sdk import get_subagent_messages, list_subagents; preserve alias and import-time effects.
  }
  // Source: vvaharness/backends/harness/claude/client.py:76-77
  On the first matching source exception ImportError, in handler order {
    // Source: vvaharness/backends/harness/claude/client.py:77-77
    End this invocation with [].
  }
  // Source: vvaharness/backends/harness/claude/client.py:78-111
  Perform the following protected operations {
    // Source: vvaharness/backends/harness/claude/client.py:79-81
    In source order: Evaluate once list_subagents(session_id, directory=str(cwd)); assign in source target order to agent_ids. Then For reports, assign []; source annotation list[dict]. Then For seen, assign set(); source annotation set[tuple].
    // Source: vvaharness/backends/harness/claude/client.py:82-107
    for each agent_id in agent_ids {
      // Source: vvaharness/backends/harness/claude/client.py:83-83
      In source order: Evaluate once get_subagent_messages(session_id, agent_id, directory=str(cwd)); assign in source target order to messages.
      // Source: vvaharness/backends/harness/claude/client.py:84-85
      if (the source predicate not messages is truthy) {
        // Source: vvaharness/backends/harness/claude/client.py:85-85
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/backends/harness/claude/client.py:86-107
      for each msg in reversed(messages) {
        // Source: vvaharness/backends/harness/claude/client.py:87-95
        In source order: Evaluate once getattr(msg, 'message', {}) or {}; assign in source target order to raw. Then Evaluate once raw.get('content', []) if isinstance(raw, dict) else []; assign in source target order to content. Then Evaluate once next((b.get('text', '') for b in content if isinstance(b, dict) and b.get('type') == 'text'), ''); assign in source target order to text. Then Evaluate once text.find('```json'); assign in source target order to start. Then Evaluate once text.find('```', start + 7) if start >= 0 else -1; assign in source target order to end.
        // Source: vvaharness/backends/harness/claude/client.py:96-97
        if (the source predicate start < 0 or end <= start is truthy) {
          // Source: vvaharness/backends/harness/claude/client.py:97-97
          Continue the immediately enclosing source loop at its next iteration.
        }
        // Source: vvaharness/backends/harness/claude/client.py:98-106
        Perform the following protected operations {
          // Source: vvaharness/backends/harness/claude/client.py:99-99
          In source order: Evaluate once json.loads(text[start + 7:end].strip()); assign in source target order to data.
          // Source: vvaharness/backends/harness/claude/client.py:100-104
          if (the source predicate isinstance(data, dict) and 'persona' in data and ('gates' in data) is truthy) {
            // Source: vvaharness/backends/harness/claude/client.py:101-101
            In source order: Evaluate once (data.get('persona'), data.get('tracking_id')); assign in source target order to key.
            // Source: vvaharness/backends/harness/claude/client.py:102-104
            if (the source predicate key not in seen is truthy) {
              // Source: vvaharness/backends/harness/claude/client.py:103-104
              In source order: Evaluate seen.add(key); retain side effects and discard the expression result. Then Evaluate reports.append(data); retain side effects and discard the expression result.
            }
          }
        }
        // Source: vvaharness/backends/harness/claude/client.py:105-106
        On the first matching source exception (ValueError, json.JSONDecodeError), in handler order {
          // Source: vvaharness/backends/harness/claude/client.py:106-106
          In source order: Perform no operation at this source statement.
        }
        // Source: vvaharness/backends/harness/claude/client.py:107-107
        Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
      }
    }
  }
  // Source: vvaharness/backends/harness/claude/client.py:108-109
  On the first matching source exception Exception, in handler order {
    // Source: vvaharness/backends/harness/claude/client.py:109-109
    End this invocation with [].
  }
  Only when the protected body falls through normally, without exception, return, break or continue {
    // Source: vvaharness/backends/harness/claude/client.py:111-111
    End this invocation with reports.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/claude/client.py:114-120
// Source signature: _merge_persona_reports(submitted: list[dict], scraped: list[dict]) -> list[dict]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _merge_persona_reports(submitted, scraped) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/claude/client.py:115-115
  In source order: Retain source documentation literal source_literal_115_4; it is not a model call.
  // Source: vvaharness/backends/harness/claude/client.py:116-117
  // Source signature: key(report: dict) -> tuple
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn key(report) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/claude/client.py:117-117
    End this invocation with (report.get('persona'), report.get('tracking_id')).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/claude/client.py:119-119
  In source order: Evaluate once {key(r) for r in submitted}; assign in source target order to have.
  // Source: vvaharness/backends/harness/claude/client.py:120-120
  End this invocation with [*submitted, *(r for r in scraped if key(r) not in have)].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/claude/client.py:123-134
// Source signature: _wrap_sdk_error(e: Exception) -> Exception
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _wrap_sdk_error(e) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/claude/client.py:124-124
  In source order: Retain source documentation literal source_literal_124_4; it is not a model call.
  // Source: vvaharness/backends/harness/claude/client.py:125-130
  if (the source predicate isinstance(e, ProcessError) is truthy) {
    // Source: vvaharness/backends/harness/claude/client.py:126-130
    End this invocation with HarnessProcessError(str(e), exit_code=getattr(e, 'exit_code', None), stderr=getattr(e, 'stderr', None)).
  }
  // Source: vvaharness/backends/harness/claude/client.py:131-133
  for each (sdk_type, harness_type) in SDK_ERROR_MAP {
    // Source: vvaharness/backends/harness/claude/client.py:132-133
    if (the source predicate isinstance(e, sdk_type) is truthy) {
      // Source: vvaharness/backends/harness/claude/client.py:133-133
      End this invocation with harness_type(str(e)).
    }
  }
  // Source: vvaharness/backends/harness/claude/client.py:134-134
  End this invocation with e.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/claude/client.py:137-279
interface ClaudeHarness {
  Describe the source Python type, preserving its base/metaclass expression order: Harness.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/harness/claude/client.py:138-138
  In source order: Retain source documentation literal source_literal_138_4; it is not a model call.
  // Source: vvaharness/backends/harness/claude/client.py:140-184
  // Source signature: run_oneshot(self, prompt: str, options: OneShotOptions) -> OneShotResult
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn run_oneshot(self, prompt, options) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    This callable produces a coroutine or async generator; await/suspension positions remain in source expressions.
    // Source: vvaharness/backends/harness/claude/client.py:143-143
    In source order: Retain source documentation literal source_literal_143_8; it is not a model call.
    // Source: vvaharness/backends/harness/claude/client.py:144-146
    if (the source predicate options.cache_prefix is truthy) {
      // Source: vvaharness/backends/harness/claude/client.py:146-146
      In source order: Evaluate once options.cache_prefix + prompt; assign in source target order to prompt.
    }
    // Source: vvaharness/backends/harness/claude/client.py:147-151
    In source order: Evaluate once build_oneshot_sdk_options(options); assign in source target order to sdk_opts. Then For result_text, assign None; source annotation str | None. Then For structured, assign None; source annotation BaseModel | None. Then Evaluate once ''; assign in source target order to subtype. Then Evaluate once False; assign in source target order to is_error.
    // Source: vvaharness/backends/harness/claude/client.py:152-153
    In source order: For usage, assign None; source annotation TokenUsage | None. Then For total_cost_usd, assign None; source annotation float | None.
    // Source: vvaharness/backends/harness/claude/client.py:154-175
    Perform the following protected operations {
      // Source: vvaharness/backends/harness/claude/client.py:155-169
      Await and enter source context managers left-to-right: ClaudeSDKClient(options=sdk_opts) bound to client {
        // Source: vvaharness/backends/harness/claude/client.py:156-156
        In source order: Evaluate await client.query(prompt); retain side effects and discard the expression result.
        // Source: vvaharness/backends/harness/claude/client.py:157-169
        Obtain/advance the following source async iterator by awaiting, without inventing parallel dispatch.
        for each message in client.receive_response() {
          // Source: vvaharness/backends/harness/claude/client.py:158-169
          if (the source predicate isinstance(message, ResultMessage) is truthy) {
            // Source: vvaharness/backends/harness/claude/client.py:159-165
            In source order: Evaluate once message.subtype; assign in source target order to subtype. Then Evaluate once bool(message.is_error); assign in source target order to is_error. Then Evaluate once message.result; assign in source target order to result_text. Then Evaluate once validate_structured(message.structured_output, options.response_model); assign in source target order to structured. Then Evaluate once cast('TokenUsage | None', message.usage); assign in source target order to usage.
            // Source: vvaharness/backends/harness/claude/client.py:166-168
            In source order: Evaluate once message.total_cost_usd; assign in source target order to total_cost_usd. Then Evaluate TOKENS.add(usage, usd=total_cost_usd); retain side effects and discard the expression result.
            // Source: vvaharness/backends/harness/claude/client.py:169-169
            Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
          }
        }
      }
      Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics and await async exits.
    }
    // Source: vvaharness/backends/harness/claude/client.py:170-173
    On the first matching source exception CLINotFoundError, in handler order {
      // Source: vvaharness/backends/harness/claude/client.py:171-173
      Raise HarnessCLINotFoundError('Claude CLI binary not found') with explicit source cause None.
    }
    // Source: vvaharness/backends/harness/claude/client.py:174-175
    On the first matching source exception (ProcessError, CLIConnectionError, CLIJSONDecodeError, MessageParseError) as e, in handler order {
      // Source: vvaharness/backends/harness/claude/client.py:175-175
      Raise _wrap_sdk_error(e) with explicit source cause e.
    }
    // Source: vvaharness/backends/harness/claude/client.py:177-184
    End this invocation with OneShotResult(is_error=is_error, subtype=subtype, result_text=result_text, structured=structured, usage=usage, total_cost_usd=total_cost_usd).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/claude/client.py:186-279
  // Source signature: run_streaming(self, prompt: str, options: StreamingOptions) -> AsyncIterator[HarnessMessage]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn run_streaming(self, prompt, options) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/claude/client.py:189-193
    In source order: Retain source documentation literal source_literal_189_8; it is not a model call. Then Evaluate once None; assign in source target order to fact_server. Then For fact_tool_names, assign []; source annotation list[str]. Then Evaluate once None; assign in source target order to collector.
    // Source: vvaharness/backends/harness/claude/client.py:194-196
    if (the source predicate options.fact_tool_specs is truthy) {
      // Source: vvaharness/backends/harness/claude/client.py:195-196
      In source order: Evaluate once build_fact_mcp(options.fact_tool_specs, report_model=_persona_report_model()); assign in source target order to (fact_server, fact_tool_names, collector).
    }
    // Source: vvaharness/backends/harness/claude/client.py:197-198
    In source order: Evaluate once build_streaming_sdk_options(options, fact_server=fact_server, fact_tool_names=fact_tool_names); assign in source target order to sdk_opts.
    // Source: vvaharness/backends/harness/claude/client.py:199-201
    if (the source predicate options.cache_prefix is truthy) {
      // Source: vvaharness/backends/harness/claude/client.py:201-201
      In source order: Evaluate once options.cache_prefix + prompt; assign in source target order to prompt.
    }
    // Source: vvaharness/backends/harness/claude/client.py:203-220
    // Source signature: _translate_message(message: object) -> list[HarnessMessage]
    Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
    fn _translate_message(message) {
      Bind arguments/defaults/annotations exactly as the source signature specifies.
      // Source: vvaharness/backends/harness/claude/client.py:204-205
      In source order: Retain source documentation literal source_literal_204_12; it is not a model call. Then For translated_list, assign []; source annotation list[HarnessMessage].
      // Source: vvaharness/backends/harness/claude/client.py:206-219
      for each translated in translate(message, options.response_model) {
        // Source: vvaharness/backends/harness/claude/client.py:207-218
        if (the source predicate isinstance(translated, HarnessResult) is truthy) {
          // Source: vvaharness/backends/harness/claude/client.py:209-210
          In source order: Evaluate once collector.reports if collector else []; assign in source target order to persona_dicts. Then Evaluate once len(options.agents) if options.agents else 1; assign in source target order to expected.
          // Source: vvaharness/backends/harness/claude/client.py:211-216
          if (the source predicate len(persona_dicts) < expected and translated.session_id is truthy) {
            // Source: vvaharness/backends/harness/claude/client.py:212-216
            In source order: Evaluate once _merge_persona_reports(persona_dicts, _extract_sdk_persona_reports(translated.session_id, options.cwd)); assign in source target order to persona_dicts.
          }
          // Source: vvaharness/backends/harness/claude/client.py:217-218
          if (the source predicate persona_dicts is truthy) {
            // Source: vvaharness/backends/harness/claude/client.py:218-218
            In source order: Evaluate once {'sdk_persona_reports': persona_dicts}; assign in source target order to translated.state.
          }
        }
        // Source: vvaharness/backends/harness/claude/client.py:219-219
        In source order: Evaluate translated_list.append(translated); retain side effects and discard the expression result.
      }
      // Source: vvaharness/backends/harness/claude/client.py:220-220
      End this invocation with translated_list.
      If execution reaches this end, finish with the source implicit None result.
    }
    // Source: vvaharness/backends/harness/claude/client.py:222-277
    // Source signature: _gen() -> AsyncIterator[HarnessMessage]
    Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
    fn _gen() {
      Bind arguments/defaults/annotations exactly as the source signature specifies.
      This callable produces a coroutine or async generator; await/suspension positions remain in source expressions.
      // Source: vvaharness/backends/harness/claude/client.py:226-226
      In source order: Evaluate once False; assign in source target order to expired.
      // Source: vvaharness/backends/harness/claude/client.py:227-271
      Perform the following protected operations {
        // Source: vvaharness/backends/harness/claude/client.py:228-265
        Await and enter source context managers left-to-right: ClaudeSDKClient(options=sdk_opts) bound to client {
          // Source: vvaharness/backends/harness/claude/client.py:229-229
          In source order: Evaluate await client.query(prompt); retain side effects and discard the expression result.
          // Source: vvaharness/backends/harness/claude/client.py:230-265
          if (the source predicate options.timeout is truthy) {
            // Source: vvaharness/backends/harness/claude/client.py:231-233
            In source order: Evaluate once asyncio.get_running_loop(); assign in source target order to loop. Then Evaluate once loop.time() + options.timeout; assign in source target order to deadline. Then Evaluate once client.receive_response().__aiter__(); assign in source target order to iterator.
            // Source: vvaharness/backends/harness/claude/client.py:234-252
            while (the source predicate True is truthy) {
              // Source: vvaharness/backends/harness/claude/client.py:238-238
              In source order: Evaluate once asyncio.timeout_at(deadline); assign in source target order to cm.
              // Source: vvaharness/backends/harness/claude/client.py:239-250
              Perform the following protected operations {
                // Source: vvaharness/backends/harness/claude/client.py:240-241
                Await and enter source context managers left-to-right: cm {
                  // Source: vvaharness/backends/harness/claude/client.py:241-241
                  In source order: Evaluate once await iterator.__anext__(); assign in source target order to message.
                }
                Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics and await async exits.
              }
              // Source: vvaharness/backends/harness/claude/client.py:242-243
              On the first matching source exception StopAsyncIteration, in handler order {
                // Source: vvaharness/backends/harness/claude/client.py:243-243
                Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
              }
              // Source: vvaharness/backends/harness/claude/client.py:244-250
              On the first matching source exception TimeoutError, in handler order {
                // Source: vvaharness/backends/harness/claude/client.py:247-248
                if (the source predicate not cm.expired() is truthy) {
                  // Source: vvaharness/backends/harness/claude/client.py:248-248
                  Raise the currently handled exception.
                }
                // Source: vvaharness/backends/harness/claude/client.py:249-249
                In source order: Evaluate once True; assign in source target order to expired.
                // Source: vvaharness/backends/harness/claude/client.py:250-250
                Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
              }
              // Source: vvaharness/backends/harness/claude/client.py:251-252
              for each translated in _translate_message(message) {
                // Source: vvaharness/backends/harness/claude/client.py:252-252
                In source order: Yield translated; suspend this generator until resumed.
              }
            }
            // Source: vvaharness/backends/harness/claude/client.py:253-261
            if (the source predicate expired is truthy) {
              // Source: vvaharness/backends/harness/claude/client.py:254-255
              Enter source context managers left-to-right: contextlib.suppress(Exception) {
                // Source: vvaharness/backends/harness/claude/client.py:255-255
                In source order: Evaluate await client.interrupt(); retain side effects and discard the expression result.
              }
              Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
              // Source: vvaharness/backends/harness/claude/client.py:258-261
              Enter source context managers left-to-right: contextlib.suppress(TimeoutError) {
                // Source: vvaharness/backends/harness/claude/client.py:259-261
                Await and enter source context managers left-to-right: asyncio.timeout(TIMEOUT_STOP_GRACE_SECONDS) {
                  // Source: vvaharness/backends/harness/claude/client.py:260-261
                  Obtain/advance the following source async iterator by awaiting, without inventing parallel dispatch.
                  for each _ in client.receive_response() {
                    // Source: vvaharness/backends/harness/claude/client.py:261-261
                    In source order: Perform no operation at this source statement.
                  }
                }
                Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics and await async exits.
              }
              Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
            }
          }
          else {
            // Source: vvaharness/backends/harness/claude/client.py:263-265
            Obtain/advance the following source async iterator by awaiting, without inventing parallel dispatch.
            for each message in client.receive_response() {
              // Source: vvaharness/backends/harness/claude/client.py:264-265
              for each translated in _translate_message(message) {
                // Source: vvaharness/backends/harness/claude/client.py:265-265
                In source order: Yield translated; suspend this generator until resumed.
              }
            }
          }
        }
        Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics and await async exits.
      }
      // Source: vvaharness/backends/harness/claude/client.py:266-269
      On the first matching source exception CLINotFoundError, in handler order {
        // Source: vvaharness/backends/harness/claude/client.py:267-269
        Raise HarnessCLINotFoundError('Claude CLI binary not found') with explicit source cause None.
      }
      // Source: vvaharness/backends/harness/claude/client.py:270-271
      On the first matching source exception (ProcessError, CLIConnectionError, CLIJSONDecodeError, MessageParseError) as e, in handler order {
        // Source: vvaharness/backends/harness/claude/client.py:271-271
        Raise _wrap_sdk_error(e) with explicit source cause e.
      }
      // Source: vvaharness/backends/harness/claude/client.py:272-277
      if (the source predicate expired is truthy) {
        // Source: vvaharness/backends/harness/claude/client.py:274-277
        Raise call_timeout_error(stage=options.graph_name, route='claude', budget_s=options.timeout, effort=options.effort, cause_text=source_template_277_31).
      }
      If execution reaches this end, finish with the source implicit None result.
    }
    // Source: vvaharness/backends/harness/claude/client.py:279-279
    End this invocation with _gen().
    If execution reaches this end, finish with the source implicit None result.
  }
}
```

## Local import links

- `from vvaharness.backends.harness.claude.facts import build_fact_mcp` at source line 36: `source_detail/vvaharness/backends/harness/claude/facts.py.sudo.md`.
- `from vvaharness.backends.harness.claude.models import SDK_ERROR_MAP` at source line 37: `source_detail/vvaharness/backends/harness/claude/models.py.sudo.md`.
- `from vvaharness.backends.harness.claude.options import build_oneshot_sdk_options, build_streaming_sdk_options` at source line 38: `source_detail/vvaharness/backends/harness/claude/options.py.sudo.md`.
- `from vvaharness.backends.harness.claude.translate import translate, validate_structured` at source line 42: `source_detail/vvaharness/backends/harness/claude/translate.py.sudo.md`.
- `from vvaharness.backends.harness.harness import Harness` at source line 43: `source_detail/vvaharness/backends/harness/harness.py.sudo.md`.
- `from vvaharness.backends.harness.models import HarnessCLINotFoundError, HarnessMessage, HarnessProcessError, HarnessResult, OneShotOptions, OneShotResult, StreamingOptions` at source line 44: `source_detail/vvaharness/backends/harness/models.py.sudo.md`.
- `from vvaharness.backends.llm.models import TIMEOUT_STOP_GRACE_SECONDS, call_timeout_error` at source line 53: `source_detail/vvaharness/backends/llm/models.py.sudo.md`.
- `from vvaharness.util.tokens import TOKENS, TokenUsage` at source line 54: `source_detail/vvaharness/util/tokens.py.sudo.md`.
- `from vvaharness.validation.models.persona_report import PersonaReport` at source line 61: `source_detail/vvaharness/validation/models/persona_report.py.sudo.md`.
