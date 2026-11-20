# vvaharness/backends/llm/agent_sdk.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/backends/llm/agent_sdk.py.evidence.json`. SHA-256: `e11373a33fc378ad1bffebf248f2cc674fe892e454f4311e91ee2c366204691b`.

```sudo
// Source: vvaharness/backends/llm/agent_sdk.py:15-22
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import asyncio; preserve alias and import-time effects. Then Resolve source import import contextlib; preserve alias and import-time effects. Then Resolve source import import os; preserve alias and import-time effects.
// Source: vvaharness/backends/llm/agent_sdk.py:23-35
In source order: Resolve source import import time; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from typing import TYPE_CHECKING, NamedTuple, cast; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm.cli import _NO_REFUSAL_RESEND_ENV; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm.models import DEFAULT_READ_TOOLS, TIMEOUT_STOP_GRACE_SECONDS, ClockKind, call_timeout_error, effort_scaled_seconds, note_budget_use; preserve alias and import-time effects.
// Source: vvaharness/backends/llm/agent_sdk.py:36-39
In source order: Resolve source import from vvaharness.report.redact import redact_counts; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import console; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.git_paths import is_git_metadata; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.tokens import TOKENS, TokenUsage; preserve alias and import-time effects.
// Source: vvaharness/backends/llm/agent_sdk.py:41-42
if (the source predicate TYPE_CHECKING is truthy) {
  // Source: vvaharness/backends/llm/agent_sdk.py:42-42
  In source order: Resolve source import from claude_agent_sdk import ResultMessage; preserve alias and import-time effects.
}
// Source: vvaharness/backends/llm/agent_sdk.py:45-49
In source order: Evaluate once frozenset({'Edit', 'Write', 'MultiEdit', 'NotebookEdit'}); assign in source target order to _WRITE_TOOLS. Then Evaluate once frozenset({'Read', 'Glob', 'Grep', 'LS', 'NotebookRead'}); assign in source target order to _READ_TOOLS. Then Evaluate once _READ_TOOLS | frozenset({'Bash'}); assign in source target order to _REDACT_TOOLS.
// Source: vvaharness/backends/llm/agent_sdk.py:52-65
// Source signature: _resolve_within_root(root: Path, raw: object) -> Path | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _resolve_within_root(root, raw) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/agent_sdk.py:53-53
  In source order: Retain source documentation literal source_literal_53_4; it is not a model call.
  // Source: vvaharness/backends/llm/agent_sdk.py:54-55
  if (the source predicate not isinstance(raw, str) or not raw is truthy) {
    // Source: vvaharness/backends/llm/agent_sdk.py:55-55
    End this invocation with None.
  }
  // Source: vvaharness/backends/llm/agent_sdk.py:56-64
  Perform the following protected operations {
    // Source: vvaharness/backends/llm/agent_sdk.py:57-57
    In source order: Evaluate once Path(raw) if os.path.isabs(raw) else root / raw; assign in source target order to candidate.
    // Source: vvaharness/backends/llm/agent_sdk.py:59-60
    if (the source predicate candidate.is_symlink() is truthy) {
      // Source: vvaharness/backends/llm/agent_sdk.py:60-60
      End this invocation with None.
    }
    // Source: vvaharness/backends/llm/agent_sdk.py:61-62
    In source order: Evaluate once candidate.resolve(); assign in source target order to target. Then Evaluate target.relative_to(root); retain side effects and discard the expression result.
  }
  // Source: vvaharness/backends/llm/agent_sdk.py:63-64
  On the first matching source exception (OSError, ValueError), in handler order {
    // Source: vvaharness/backends/llm/agent_sdk.py:64-64
    End this invocation with None.
  }
  // Source: vvaharness/backends/llm/agent_sdk.py:65-65
  End this invocation with target.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/agent_sdk.py:68-70
// Source signature: _within_root(root: Path, raw: object) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _within_root(root, raw) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/agent_sdk.py:69-69
  In source order: Retain source documentation literal source_literal_69_4; it is not a model call.
  // Source: vvaharness/backends/llm/agent_sdk.py:70-70
  End this invocation with _resolve_within_root(root, raw) is not None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/agent_sdk.py:73-85
// Source signature: _sdk_env() -> dict[str, str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _sdk_env() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/agent_sdk.py:74-75
  In source order: Retain source documentation literal source_literal_74_4; it is not a model call. Then Evaluate once dict(os.environ); assign in source target order to env.
  // Source: vvaharness/backends/llm/agent_sdk.py:76-80
  if (the source predicate not env.get('ANTHROPIC_API_KEY') is truthy) {
    // Source: vvaharness/backends/llm/agent_sdk.py:77-78
    In source order: Evaluate once env.get('ANTHROPIC_AUTH_TOKEN') or env.get('ANTHROPIC_SDK_API_KEY'); assign in source target order to fallback.
    // Source: vvaharness/backends/llm/agent_sdk.py:79-80
    if (the source predicate fallback is truthy) {
      // Source: vvaharness/backends/llm/agent_sdk.py:80-80
      In source order: Evaluate once fallback; assign in source target order to env['ANTHROPIC_API_KEY'].
    }
  }
  // Source: vvaharness/backends/llm/agent_sdk.py:81-81
  In source order: Evaluate once env.get('ANTHROPIC_SDK_BASE_URL'); assign in source target order to sdk_base.
  // Source: vvaharness/backends/llm/agent_sdk.py:82-83
  if (the source predicate sdk_base and (not env.get('ANTHROPIC_BASE_URL')) is truthy) {
    // Source: vvaharness/backends/llm/agent_sdk.py:83-83
    In source order: Evaluate once sdk_base; assign in source target order to env['ANTHROPIC_BASE_URL'].
  }
  // Source: vvaharness/backends/llm/agent_sdk.py:85-85
  End this invocation with {**env, **_NO_REFUSAL_RESEND_ENV}.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/agent_sdk.py:89-89
In source order: Evaluate once frozenset({'filePath', 'file_path', 'filenames', 'path'}); assign in source target order to _TOOL_PATH_KEYS.
// Source: vvaharness/backends/llm/agent_sdk.py:92-102
// Source signature: _redact_tool_output(payload: object, *, carry: bool=True) -> object
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _redact_tool_output(payload, carry) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/agent_sdk.py:93-93
  In source order: Retain source documentation literal source_literal_93_4; it is not a model call.
  // Source: vvaharness/backends/llm/agent_sdk.py:94-96
  if (the source predicate isinstance(payload, str) is truthy) {
    // Source: vvaharness/backends/llm/agent_sdk.py:95-95
    In source order: Evaluate once redact_counts(payload, carry=carry); assign in source target order to (masked, _).
    // Source: vvaharness/backends/llm/agent_sdk.py:96-96
    End this invocation with masked.
  }
  // Source: vvaharness/backends/llm/agent_sdk.py:97-98
  if (the source predicate isinstance(payload, list) is truthy) {
    // Source: vvaharness/backends/llm/agent_sdk.py:98-98
    End this invocation with [_redact_tool_output(item, carry=carry) for item in payload].
  }
  // Source: vvaharness/backends/llm/agent_sdk.py:99-101
  if (the source predicate isinstance(payload, dict) is truthy) {
    // Source: vvaharness/backends/llm/agent_sdk.py:100-101
    End this invocation with {k: _redact_tool_output(v, carry=carry and k not in _TOOL_PATH_KEYS) for k, v in payload.items()}.
  }
  // Source: vvaharness/backends/llm/agent_sdk.py:102-102
  End this invocation with payload.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/agent_sdk.py:105-136
// Source signature: _build_redaction_hooks()
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _build_redaction_hooks() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/agent_sdk.py:106-106
  In source order: Retain source documentation literal source_literal_106_4; it is not a model call.
  // Source: vvaharness/backends/llm/agent_sdk.py:107-110
  Perform the following protected operations {
    // Source: vvaharness/backends/llm/agent_sdk.py:108-108
    In source order: Resolve source import from claude_agent_sdk import HookMatcher; preserve alias and import-time effects.
  }
  // Source: vvaharness/backends/llm/agent_sdk.py:109-110
  On the first matching source exception Exception, in handler order {
    // Source: vvaharness/backends/llm/agent_sdk.py:110-110
    End this invocation with None.
  }
  // Source: vvaharness/backends/llm/agent_sdk.py:112-131
  // Source signature: _post_tool_use(input_data, tool_use_id, context)
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _post_tool_use(input_data, tool_use_id, context) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    This callable produces a coroutine or async generator; await/suspension positions remain in source expressions.
    // Source: vvaharness/backends/llm/agent_sdk.py:113-131
    Perform the following protected operations {
      // Source: vvaharness/backends/llm/agent_sdk.py:114-114
      In source order: Evaluate once (input_data or {}).get('tool_name'); assign in source target order to tool_name.
      // Source: vvaharness/backends/llm/agent_sdk.py:115-116
      if (the source predicate tool_name not in _REDACT_TOOLS is truthy) {
        // Source: vvaharness/backends/llm/agent_sdk.py:116-116
        End this invocation with {}.
      }
      // Source: vvaharness/backends/llm/agent_sdk.py:117-117
      In source order: Evaluate once (input_data or {}).get('tool_response'); assign in source target order to response.
      // Source: vvaharness/backends/llm/agent_sdk.py:118-119
      if (the source predicate response is None is truthy) {
        // Source: vvaharness/backends/llm/agent_sdk.py:119-119
        End this invocation with {}.
      }
      // Source: vvaharness/backends/llm/agent_sdk.py:120-120
      In source order: Evaluate once _redact_tool_output(response); assign in source target order to masked.
      // Source: vvaharness/backends/llm/agent_sdk.py:121-122
      if (the source predicate masked == response is truthy) {
        // Source: vvaharness/backends/llm/agent_sdk.py:122-122
        End this invocation with {}.
      }
      // Source: vvaharness/backends/llm/agent_sdk.py:124-129
      End this invocation with {'hookSpecificOutput': {'hookEventName': 'PostToolUse', 'updatedToolOutput': masked}}.
    }
    // Source: vvaharness/backends/llm/agent_sdk.py:130-131
    On the first matching source exception Exception, in handler order {
      // Source: vvaharness/backends/llm/agent_sdk.py:131-131
      End this invocation with {}.
    }
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/llm/agent_sdk.py:133-136
  Perform the following protected operations {
    // Source: vvaharness/backends/llm/agent_sdk.py:134-134
    End this invocation with {'PostToolUse': [HookMatcher(hooks=[_post_tool_use])]}.
  }
  // Source: vvaharness/backends/llm/agent_sdk.py:135-136
  On the first matching source exception Exception, in handler order {
    // Source: vvaharness/backends/llm/agent_sdk.py:136-136
    End this invocation with None.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/agent_sdk.py:139-236
// Source signature: _build_options(*, model: str, system_prompt: str | None, allowed_tools: list[str], cwd: str, max_budget_usd: float | None, max_turns: int | None)
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _build_options(model, system_prompt, allowed_tools, cwd, max_budget_usd, max_turns) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/agent_sdk.py:142-142
  In source order: Retain source documentation literal source_literal_142_4; it is not a model call.
  // Source: vvaharness/backends/llm/agent_sdk.py:143-154
  Perform the following protected operations {
    // Source: vvaharness/backends/llm/agent_sdk.py:144-147
    In source order: Resolve source import from claude_agent_sdk import ClaudeAgentOptions, HookMatcher; preserve alias and import-time effects.
  }
  // Source: vvaharness/backends/llm/agent_sdk.py:148-154
  On the first matching source exception ImportError as e, in handler order {
    // Source: vvaharness/backends/llm/agent_sdk.py:149-154
    Raise RuntimeError(source_literal_150_12) with explicit source cause e.
  }
  // Source: vvaharness/backends/llm/agent_sdk.py:156-156
  In source order: Evaluate once Path(cwd).resolve(); assign in source target order to root.
  // Source: vvaharness/backends/llm/agent_sdk.py:158-205
  // Source signature: _pre_tool_use_gate(input_data, tool_use_id, context)
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _pre_tool_use_gate(input_data, tool_use_id, context) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    This callable produces a coroutine or async generator; await/suspension positions remain in source expressions.
    // Source: vvaharness/backends/llm/agent_sdk.py:159-159
    In source order: Retain source documentation literal source_literal_159_8; it is not a model call.
    // Source: vvaharness/backends/llm/agent_sdk.py:161-166
    // Source signature: _deny(reason: str) -> dict
    Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
    fn _deny(reason) {
      Bind arguments/defaults/annotations exactly as the source signature specifies.
      // Source: vvaharness/backends/llm/agent_sdk.py:162-166
      End this invocation with {'hookSpecificOutput': {'hookEventName': 'PreToolUse', 'permissionDecision': 'deny', 'permissionDecisionReason': reason}}.
      If execution reaches this end, finish with the source implicit None result.
    }
    // Source: vvaharness/backends/llm/agent_sdk.py:168-205
    Perform the following protected operations {
      // Source: vvaharness/backends/llm/agent_sdk.py:169-170
      In source order: Evaluate once (input_data or {}).get('tool_name') or ''; assign in source target order to tool_name. Then Evaluate once (input_data or {}).get('tool_input') or {}; assign in source target order to tool_input.
      // Source: vvaharness/backends/llm/agent_sdk.py:173-195
      if (the source predicate tool_name in _WRITE_TOOLS is truthy) {
        // Source: vvaharness/backends/llm/agent_sdk.py:174-174
        In source order: Evaluate once None; assign in source target order to raw, key_used.
        // Source: vvaharness/backends/llm/agent_sdk.py:175-179
        for each key in ('file_path', 'path', 'notebook_path') {
          // Source: vvaharness/backends/llm/agent_sdk.py:176-176
          In source order: Evaluate once tool_input.get(key); assign in source target order to val.
          // Source: vvaharness/backends/llm/agent_sdk.py:177-179
          if (the source predicate val is truthy) {
            // Source: vvaharness/backends/llm/agent_sdk.py:178-178
            In source order: Evaluate once (val, key); assign in source target order to (raw, key_used).
            // Source: vvaharness/backends/llm/agent_sdk.py:179-179
            Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
          }
        }
        // Source: vvaharness/backends/llm/agent_sdk.py:180-180
        In source order: Evaluate once _resolve_within_root(root, raw); assign in source target order to resolved.
        // Source: vvaharness/backends/llm/agent_sdk.py:181-184
        if (the source predicate resolved is None is truthy) {
          // Source: vvaharness/backends/llm/agent_sdk.py:182-184
          End this invocation with _deny(source_template_182_33).
        }
        // Source: vvaharness/backends/llm/agent_sdk.py:185-187
        if (the source predicate is_git_metadata(resolved.relative_to(root)) is truthy) {
          // Source: vvaharness/backends/llm/agent_sdk.py:186-187
          End this invocation with _deny(source_template_186_33).
        }
        // Source: vvaharness/backends/llm/agent_sdk.py:189-190
        In source order: Evaluate once dict(tool_input); assign in source target order to safe_input. Then Evaluate once str(resolved); assign in source target order to safe_input[key_used].
        // Source: vvaharness/backends/llm/agent_sdk.py:191-195
        End this invocation with {'hookSpecificOutput': {'hookEventName': 'PreToolUse', 'permissionDecision': 'allow', 'updatedInput': safe_input}}.
      }
      // Source: vvaharness/backends/llm/agent_sdk.py:197-198
      if (the source predicate tool_name in _READ_TOOLS is truthy) {
        // Source: vvaharness/backends/llm/agent_sdk.py:198-198
        End this invocation with {}.
      }
      // Source: vvaharness/backends/llm/agent_sdk.py:200-202
      End this invocation with _deny(source_template_200_25).
    }
    // Source: vvaharness/backends/llm/agent_sdk.py:203-205
    On the first matching source exception Exception as exc, in handler order {
      // Source: vvaharness/backends/llm/agent_sdk.py:204-205
      End this invocation with _deny(source_template_204_25).
    }
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/llm/agent_sdk.py:207-228
  In source order: Evaluate once _build_redaction_hooks() or {}; assign in source target order to redaction_hooks. Then Evaluate once {**redaction_hooks, 'PreToolUse': [HookMatcher(hooks=[_pre_tool_use_gate])]}; assign in source target order to hooks. Then Evaluate once ClaudeAgentOptions(model=model, cwd=str(root), env=_sdk_env(), permission_mode='default', setting_sources=['user'], strict_mcp_config=True, allowed_tools=list(allowed_tools), hooks=hooks, verbatim_prompts=True); assign in source target order to opts.
  // Source: vvaharness/backends/llm/agent_sdk.py:230-231
  if (the source predicate system_prompt is not None is truthy) {
    // Source: vvaharness/backends/llm/agent_sdk.py:231-231
    In source order: Evaluate once system_prompt; assign in source target order to opts.system_prompt.
  }
  // Source: vvaharness/backends/llm/agent_sdk.py:232-233
  if (the source predicate max_turns is not None is truthy) {
    // Source: vvaharness/backends/llm/agent_sdk.py:233-233
    In source order: Evaluate once int(max_turns); assign in source target order to opts.max_turns.
  }
  // Source: vvaharness/backends/llm/agent_sdk.py:234-235
  if (the source predicate max_budget_usd is not None is truthy) {
    // Source: vvaharness/backends/llm/agent_sdk.py:235-235
    In source order: Evaluate once float(max_budget_usd); assign in source target order to opts.max_budget_usd.
  }
  // Source: vvaharness/backends/llm/agent_sdk.py:236-236
  End this invocation with opts.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/agent_sdk.py:239-243
interface DrainResult {
  Describe the source Python type, preserving its base/metaclass expression order: NamedTuple.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/llm/agent_sdk.py:240-243
  In source order: Retain source documentation literal source_literal_240_4; it is not a model call. Then For result, declare without assigning a value; source annotation ResultMessage | None. Then For timed_out, declare without assigning a value; source annotation bool.
}
// Source: vvaharness/backends/llm/agent_sdk.py:246-254
// Source signature: _drain(client, on_message) -> ResultMessage | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _drain(client, on_message) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  This callable produces a coroutine or async generator; await/suspension positions remain in source expressions.
  // Source: vvaharness/backends/llm/agent_sdk.py:247-248
  In source order: Retain source documentation literal source_literal_247_4; it is not a model call. Then Resolve source import from claude_agent_sdk import ResultMessage; preserve alias and import-time effects.
  // Source: vvaharness/backends/llm/agent_sdk.py:250-253
  Obtain/advance the following source async iterator by awaiting, without inventing parallel dispatch.
  for each message in client.receive_response() {
    // Source: vvaharness/backends/llm/agent_sdk.py:251-251
    In source order: Evaluate on_message(message); retain side effects and discard the expression result.
    // Source: vvaharness/backends/llm/agent_sdk.py:252-253
    if (the source predicate isinstance(message, ResultMessage) is truthy) {
      // Source: vvaharness/backends/llm/agent_sdk.py:253-253
      End this invocation with message.
    }
  }
  // Source: vvaharness/backends/llm/agent_sdk.py:254-254
  End this invocation with None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/agent_sdk.py:257-281
// Source signature: drain_until_result(client, *, on_message, timeout: float | None, grace: float=TIMEOUT_STOP_GRACE_SECONDS) -> DrainResult
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn drain_until_result(client, on_message, timeout, grace) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  This callable produces a coroutine or async generator; await/suspension positions remain in source expressions.
  // Source: vvaharness/backends/llm/agent_sdk.py:259-259
  In source order: Retain source documentation literal source_literal_259_4; it is not a model call.
  // Source: vvaharness/backends/llm/agent_sdk.py:260-261
  if (the source predicate timeout is None or timeout <= 0 is truthy) {
    // Source: vvaharness/backends/llm/agent_sdk.py:261-261
    End this invocation with DrainResult(await _drain(client, on_message), False).
  }
  // Source: vvaharness/backends/llm/agent_sdk.py:263-263
  In source order: Evaluate once asyncio.timeout(timeout); assign in source target order to deadline.
  // Source: vvaharness/backends/llm/agent_sdk.py:264-269
  Perform the following protected operations {
    // Source: vvaharness/backends/llm/agent_sdk.py:265-266
    Await and enter source context managers left-to-right: deadline {
      // Source: vvaharness/backends/llm/agent_sdk.py:266-266
      End this invocation with DrainResult(await _drain(client, on_message), False).
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics and await async exits.
  }
  // Source: vvaharness/backends/llm/agent_sdk.py:267-269
  On the first matching source exception TimeoutError, in handler order {
    // Source: vvaharness/backends/llm/agent_sdk.py:268-269
    if (the source predicate not deadline.expired() is truthy) {
      // Source: vvaharness/backends/llm/agent_sdk.py:269-269
      Raise the currently handled exception.
    }
  }
  // Source: vvaharness/backends/llm/agent_sdk.py:270-271
  Enter source context managers left-to-right: contextlib.suppress(Exception) {
    // Source: vvaharness/backends/llm/agent_sdk.py:271-271
    In source order: Evaluate await client.interrupt(); retain side effects and discard the expression result.
  }
  Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
  // Source: vvaharness/backends/llm/agent_sdk.py:274-274
  In source order: Evaluate once asyncio.timeout(grace); assign in source target order to regrace.
  // Source: vvaharness/backends/llm/agent_sdk.py:275-281
  Perform the following protected operations {
    // Source: vvaharness/backends/llm/agent_sdk.py:276-277
    Await and enter source context managers left-to-right: regrace {
      // Source: vvaharness/backends/llm/agent_sdk.py:277-277
      End this invocation with DrainResult(await _drain(client, on_message), True).
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics and await async exits.
  }
  // Source: vvaharness/backends/llm/agent_sdk.py:278-281
  On the first matching source exception TimeoutError, in handler order {
    // Source: vvaharness/backends/llm/agent_sdk.py:279-280
    if (the source predicate not regrace.expired() is truthy) {
      // Source: vvaharness/backends/llm/agent_sdk.py:280-280
      Raise the currently handled exception.
    }
    // Source: vvaharness/backends/llm/agent_sdk.py:281-281
    End this invocation with DrainResult(None, True).
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/agent_sdk.py:284-320
// Source signature: _run(*, user_prompt: str, opts, timeout: float | None=None, tag: str | None=None, effort: str | None=None) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _run(user_prompt, opts, timeout, tag, effort) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  This callable produces a coroutine or async generator; await/suspension positions remain in source expressions.
  // Source: vvaharness/backends/llm/agent_sdk.py:286-293
  In source order: Retain source documentation literal source_literal_286_4; it is not a model call. Then Resolve source import from claude_agent_sdk import AssistantMessage, ClaudeSDKClient, TextBlock; preserve alias and import-time effects. Then For text_parts, assign []; source annotation list[str].
  // Source: vvaharness/backends/llm/agent_sdk.py:295-299
  // Source signature: _on_message(message) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _on_message(message) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/llm/agent_sdk.py:296-299
    if (the source predicate isinstance(message, AssistantMessage) is truthy) {
      // Source: vvaharness/backends/llm/agent_sdk.py:297-299
      for each block in message.content {
        // Source: vvaharness/backends/llm/agent_sdk.py:298-299
        if (the source predicate isinstance(block, TextBlock) is truthy) {
          // Source: vvaharness/backends/llm/agent_sdk.py:299-299
          In source order: Evaluate text_parts.append(block.text); retain side effects and discard the expression result.
        }
      }
    }
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/llm/agent_sdk.py:302-305
  In source order: Evaluate once effort_scaled_seconds(timeout, effort, kind=ClockKind.SESSION); assign in source target order to budget. Then Evaluate once time.monotonic(); assign in source target order to _start.
  // Source: vvaharness/backends/llm/agent_sdk.py:306-309
  Await and enter source context managers left-to-right: ClaudeSDKClient(options=opts) bound to client {
    // Source: vvaharness/backends/llm/agent_sdk.py:307-309
    In source order: Evaluate await client.query(user_prompt); retain side effects and discard the expression result. Then Evaluate once await drain_until_result(client, on_message=_on_message, timeout=budget, grace=TIMEOUT_STOP_GRACE_SECONDS); assign in source target order to drained.
  }
  Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics and await async exits.
  // Source: vvaharness/backends/llm/agent_sdk.py:311-311
  In source order: Evaluate once drained.result; assign in source target order to result.
  // Source: vvaharness/backends/llm/agent_sdk.py:312-313
  if (the source predicate result is not None and result.usage is truthy) {
    // Source: vvaharness/backends/llm/agent_sdk.py:313-313
    In source order: Evaluate TOKENS.add(cast('TokenUsage', result.usage)); retain side effects and discard the expression result.
  }
  // Source: vvaharness/backends/llm/agent_sdk.py:314-317
  if (the source predicate drained.timed_out is truthy) {
    // Source: vvaharness/backends/llm/agent_sdk.py:315-317
    Raise call_timeout_error(stage=tag or '', route='agent-sdk', budget_s=budget, effort=effort, cause_text=source_template_317_23).
  }
  // Source: vvaharness/backends/llm/agent_sdk.py:318-319
  In source order: Evaluate note_budget_use(time.monotonic() - _start, budget, effort); retain side effects and discard the expression result. Then Evaluate once result.result if result is not None else None; assign in source target order to result_text.
  // Source: vvaharness/backends/llm/agent_sdk.py:320-320
  End this invocation with (result_text or ''.join(text_parts)).strip().
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/agent_sdk.py:323-358
// Source signature: agentic(user_prompt: str, *, model: str, system_prompt: str | None=None, allowed_tools: list[str] | None=None, cwd: str, max_budget_usd: float | None=None, permission_mode: str='auto', max_turns: int | None=None, tag: str | None=None, timeout: float | None=None, effort: str | None=None) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn agentic(user_prompt, model, system_prompt, allowed_tools, cwd, max_budget_usd, permission_mode, max_turns, tag, timeout, effort) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/agent_sdk.py:337-337
  In source order: Retain source documentation literal source_literal_337_4; it is not a model call.
  // Source: vvaharness/backends/llm/agent_sdk.py:338-346
  Perform the following protected operations {
    // Source: vvaharness/backends/llm/agent_sdk.py:339-339
    In source order: Resolve source import import claude_agent_sdk; preserve alias and import-time effects.
  }
  // Source: vvaharness/backends/llm/agent_sdk.py:340-346
  On the first matching source exception ImportError as e, in handler order {
    // Source: vvaharness/backends/llm/agent_sdk.py:341-346
    Raise RuntimeError(source_literal_342_12) with explicit source cause e.
  }
  // Source: vvaharness/backends/llm/agent_sdk.py:348-356
  In source order: Evaluate once list(DEFAULT_READ_TOOLS) if allowed_tools is None else list(allowed_tools); assign in source target order to allowed. Then Evaluate once source_template_349_14 if tag else ''; assign in source target order to tag_sfx. Then Evaluate console.write(source_template_350_18); retain side effects and discard the expression result. Then Evaluate once _build_options(model=model, system_prompt=system_prompt, allowed_tools=allowed, cwd=cwd, max_budget_usd=max_budget_usd, max_turns=max_turns); assign in source target order to opts.
  // Source: vvaharness/backends/llm/agent_sdk.py:357-358
  End this invocation with asyncio.run(_run(user_prompt=user_prompt, opts=opts, timeout=timeout, tag=tag, effort=effort)).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.backends.llm.cli import _NO_REFUSAL_RESEND_ENV` at source line 27: `source_detail/vvaharness/backends/llm/cli/__init__.py.sudo.md`.
- `from vvaharness.backends.llm.models import DEFAULT_READ_TOOLS, TIMEOUT_STOP_GRACE_SECONDS, ClockKind, call_timeout_error, effort_scaled_seconds, note_budget_use` at source line 28: `source_detail/vvaharness/backends/llm/models.py.sudo.md`.
- `from vvaharness.report.redact import redact_counts` at source line 36: `source_detail/vvaharness/report/redact.py.sudo.md`.
- `from vvaharness.util import console` at source line 37: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import console` at source line 37: `source_detail/vvaharness/util/console.py.sudo.md`.
- `from vvaharness.util.git_paths import is_git_metadata` at source line 38: `source_detail/vvaharness/util/git_paths.py.sudo.md`.
- `from vvaharness.util.tokens import TOKENS, TokenUsage` at source line 39: `source_detail/vvaharness/util/tokens.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../prompt_representation/vvaharness/backends/llm/agent_sdk.py.sudo.md). Exact strings in the evidence asset support this conversion.
