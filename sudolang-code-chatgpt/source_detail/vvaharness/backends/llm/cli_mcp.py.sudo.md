# vvaharness/backends/llm/cli_mcp.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/backends/llm/cli_mcp.py.evidence.json`. SHA-256: `75c747f4649439a72b3e3cac3dda8b62c3762300f184fb219aa371badb5a0684`.

```sudo
// Source: vvaharness/backends/llm/cli_mcp.py:15-29
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import asyncio; preserve alias and import-time effects. Then Resolve source import import json; preserve alias and import-time effects. Then Resolve source import import os; preserve alias and import-time effects.
// Source: vvaharness/backends/llm/cli_mcp.py:30-38
In source order: Resolve source import import re; preserve alias and import-time effects. Then Resolve source import import time; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from typing import TYPE_CHECKING, Any, cast; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.models import AuthenticationError, ProxyError; preserve alias and import-time effects.
// Source: vvaharness/backends/llm/cli_mcp.py:39-54
In source order: Resolve source import from vvaharness.backends.llm import cli as _cli; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm.models import ANTHROPIC_STOP_REFUSAL, CLI_STRUCTURED_OUTPUT_TOOL, CLI_TOKEN_CAP_RX, TIMEOUT_STOP_GRACE_SECONDS, TRUNCATED_RETRY_RECOVERED_COUNTER, ClockKind, call_timeout_error, effort_scaled_seconds, model_refusal, note_budget_use; preserve alias and import-time effects. Then Resolve source import from vvaharness.report.redact import redact; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import console; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.counters import COUNTERS; preserve alias and import-time effects.
// Source: vvaharness/backends/llm/cli_mcp.py:55-58
In source order: Resolve source import from vvaharness.util.response_quality import check_response_quality; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.scan_progress import is_stage_only; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.tokens import TOKENS, TokenUsage; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.warn_once import warn_once; preserve alias and import-time effects.
// Source: vvaharness/backends/llm/cli_mcp.py:60-61
if (the source predicate TYPE_CHECKING is truthy) {
  // Source: vvaharness/backends/llm/cli_mcp.py:61-61
  In source order: Resolve source import from collections.abc import Sequence; preserve alias and import-time effects.
}
// Source: vvaharness/backends/llm/cli_mcp.py:64-71
In source order: Evaluate once 'vvah_facts'; assign in source target order to SERVER_NAME. Then Evaluate once source_template_65_14; assign in source target order to TOOL_PREFIX. Then For _WARNED, assign set(); source annotation set[str]. Then Evaluate once 'cli_mcp_evidence_gate_unenforced'; assign in source target order to EVIDENCE_UNENFORCED_COUNTER.
// Source: vvaharness/backends/llm/cli_mcp.py:74-80
// Source signature: available() -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn available() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli_mcp.py:75-75
  In source order: Retain source documentation literal source_literal_75_4; it is not a model call.
  // Source: vvaharness/backends/llm/cli_mcp.py:76-79
  Perform the following protected operations {
    // Source: vvaharness/backends/llm/cli_mcp.py:77-77
    In source order: Resolve source import import claude_agent_sdk; preserve alias and import-time effects.
  }
  // Source: vvaharness/backends/llm/cli_mcp.py:78-79
  On the first matching source exception Exception, in handler order {
    // Source: vvaharness/backends/llm/cli_mcp.py:79-79
    End this invocation with False.
  }
  // Source: vvaharness/backends/llm/cli_mcp.py:80-80
  End this invocation with True.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cli_mcp.py:83-85
// Source signature: mcp_name(bare: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn mcp_name(bare) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli_mcp.py:84-84
  In source order: Retain source documentation literal source_literal_84_4; it is not a model call.
  // Source: vvaharness/backends/llm/cli_mcp.py:85-85
  End this invocation with TOOL_PREFIX + bare.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cli_mcp.py:90-102
// Source signature: _materialize(tool_builder, *, model: str, cwd: str, fact_tools: Sequence[str]) -> list[Any]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _materialize(tool_builder, model, cwd, fact_tools) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli_mcp.py:92-96
  In source order: Retain source documentation literal source_literal_92_4; it is not a model call. Then Resolve source import from vvaharness.backends.harness import StreamingOptions; preserve alias and import-time effects. Then Evaluate once set(fact_tools); assign in source target order to wanted.
  // Source: vvaharness/backends/llm/cli_mcp.py:97-98
  if (the source predicate not wanted is truthy) {
    // Source: vvaharness/backends/llm/cli_mcp.py:98-98
    End this invocation with [].
  }
  // Source: vvaharness/backends/llm/cli_mcp.py:99-101
  In source order: Evaluate once StreamingOptions(model=model, cwd=Path(cwd), fact_tools=tuple(fact_tools)); assign in source target order to options. Then Evaluate once tool_builder(options, allowed_tools=()) or []; assign in source target order to built.
  // Source: vvaharness/backends/llm/cli_mcp.py:102-102
  End this invocation with [t for t in built if getattr(t, 'name', None) in wanted].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cli_mcp.py:105-112
// Source signature: _tool_schema(langchain_tool: Any) -> dict[str, Any]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _tool_schema(langchain_tool) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli_mcp.py:106-111
  In source order: Retain source documentation literal source_literal_106_4; it is not a model call. Then Evaluate once dict(getattr(langchain_tool, 'args', None) or {}); assign in source target order to args. Then Evaluate once [name for name, spec in args.items() if isinstance(spec, dict) and 'default' not in spec]; assign in source target order to required.
  // Source: vvaharness/backends/llm/cli_mcp.py:112-112
  End this invocation with {'type': 'object', 'properties': args, 'required': required}.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cli_mcp.py:115-124
// Source signature: _budget_refusal(parent_middleware: Sequence[Any], name: str) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _budget_refusal(parent_middleware, name) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli_mcp.py:116-116
  In source order: Retain source documentation literal source_literal_116_4; it is not a model call.
  // Source: vvaharness/backends/llm/cli_mcp.py:117-123
  for each mw in parent_middleware or () {
    // Source: vvaharness/backends/llm/cli_mcp.py:118-118
    In source order: Evaluate once getattr(mw, 'refusal_for', None); assign in source target order to refusal.
    // Source: vvaharness/backends/llm/cli_mcp.py:119-120
    if (the source predicate refusal is None is truthy) {
      // Source: vvaharness/backends/llm/cli_mcp.py:120-120
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/backends/llm/cli_mcp.py:121-121
    In source order: Evaluate once refusal(name); assign in source target order to text.
    // Source: vvaharness/backends/llm/cli_mcp.py:122-123
    if (the source predicate text is truthy) {
      // Source: vvaharness/backends/llm/cli_mcp.py:123-123
      End this invocation with text.
    }
  }
  // Source: vvaharness/backends/llm/cli_mcp.py:124-124
  End this invocation with None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cli_mcp.py:127-134
// Source signature: _required_fact_tools(parent_middleware: Sequence[Any]) -> frozenset[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _required_fact_tools(parent_middleware) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli_mcp.py:128-129
  In source order: Retain source documentation literal source_literal_128_4; it is not a model call. Then For required, assign set(); source annotation set[str].
  // Source: vvaharness/backends/llm/cli_mcp.py:130-133
  for each mw in parent_middleware or () {
    // Source: vvaharness/backends/llm/cli_mcp.py:131-131
    In source order: Evaluate once getattr(mw, 'required_tools', None); assign in source target order to names.
    // Source: vvaharness/backends/llm/cli_mcp.py:132-133
    if (the source predicate names is truthy) {
      // Source: vvaharness/backends/llm/cli_mcp.py:133-133
      In source order: Apply source augmented assignment required |= set(names) with source evaluation/in-place semantics.
    }
  }
  // Source: vvaharness/backends/llm/cli_mcp.py:134-134
  End this invocation with frozenset(required).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cli_mcp.py:137-146
// Source signature: _submit_guard(parent_middleware: Sequence[Any]) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _submit_guard(parent_middleware) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli_mcp.py:138-138
  In source order: Retain source documentation literal source_literal_138_4; it is not a model call.
  // Source: vvaharness/backends/llm/cli_mcp.py:139-145
  for each mw in parent_middleware or () {
    // Source: vvaharness/backends/llm/cli_mcp.py:140-140
    In source order: Evaluate once getattr(mw, 'hold_for_verdict', None); assign in source target order to hold.
    // Source: vvaharness/backends/llm/cli_mcp.py:141-142
    if (the source predicate hold is None is truthy) {
      // Source: vvaharness/backends/llm/cli_mcp.py:142-142
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/backends/llm/cli_mcp.py:143-143
    In source order: Evaluate once hold(); assign in source target order to text.
    // Source: vvaharness/backends/llm/cli_mcp.py:144-145
    if (the source predicate text is truthy) {
      // Source: vvaharness/backends/llm/cli_mcp.py:145-145
      End this invocation with text.
    }
  }
  // Source: vvaharness/backends/llm/cli_mcp.py:146-146
  End this invocation with None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cli_mcp.py:149-155
// Source signature: _log_tool_call(name: str, payload: dict[str, Any], tag_sfx: str) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _log_tool_call(name, payload, tag_sfx) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli_mcp.py:150-150
  In source order: Retain source documentation literal source_literal_150_4; it is not a model call.
  // Source: vvaharness/backends/llm/cli_mcp.py:152-153
  if (the source predicate is_stage_only() is truthy) {
    // Source: vvaharness/backends/llm/cli_mcp.py:153-153
    End this invocation with None.
  }
  // Source: vvaharness/backends/llm/cli_mcp.py:154-155
  In source order: Evaluate once len(payload['content'][0]['text']); assign in source target order to size. Then Evaluate console.write(source_template_155_18); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cli_mcp.py:158-195
// Source signature: _to_sdk_tools(langchain_tools: Sequence[Any], *, parent_middleware: Sequence[Any], called: set[str], tag: str | None=None) -> list[Any]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _to_sdk_tools(langchain_tools, parent_middleware, called, tag) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli_mcp.py:161-165
  In source order: Retain source documentation literal source_literal_161_4; it is not a model call. Then Resolve source import from claude_agent_sdk import tool as sdk_tool; preserve alias and import-time effects. Then Evaluate once source_template_164_14 if tag else ''; assign in source target order to tag_sfx. Then For out, assign []; source annotation list[Any].
  // Source: vvaharness/backends/llm/cli_mcp.py:166-194
  for each lc_tool in langchain_tools {
    // Source: vvaharness/backends/llm/cli_mcp.py:168-192
    // Source signature: _make(bound_tool=lc_tool, bound_name=lc_tool.name, bound_desc=(lc_tool.description or '').strip())
    Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
    fn _make(bound_tool, bound_name, bound_desc) {
      Bind arguments/defaults/annotations exactly as the source signature specifies.
      // Source: vvaharness/backends/llm/cli_mcp.py:172-190
      // Source: vvaharness/backends/llm/cli_mcp.py:170-171
      Before creating this callable, evaluate and retain decorators top-to-bottom: sdk_tool(bound_name, bound_desc or bound_name, _tool_schema(bound_tool)).
      // Source: vvaharness/backends/llm/cli_mcp.py:172-190
      // Source signature: _handler(args: dict[str, Any]) -> dict[str, Any]
      Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
      fn _handler(args) {
        Bind arguments/defaults/annotations exactly as the source signature specifies.
        This callable produces a coroutine or async generator; await/suspension positions remain in source expressions.
        // Source: vvaharness/backends/llm/cli_mcp.py:173-173
        In source order: Evaluate once _budget_refusal(parent_middleware, bound_name); assign in source target order to refusal.
        // Source: vvaharness/backends/llm/cli_mcp.py:174-175
        if (the source predicate refusal is not None is truthy) {
          // Source: vvaharness/backends/llm/cli_mcp.py:175-175
          End this invocation with _content(refusal, is_error=True).
        }
        // Source: vvaharness/backends/llm/cli_mcp.py:176-176
        In source order: Evaluate called.add(bound_name); retain side effects and discard the expression result.
        // Source: vvaharness/backends/llm/cli_mcp.py:177-180
        for each mw in parent_middleware or () {
          // Source: vvaharness/backends/llm/cli_mcp.py:178-178
          In source order: Evaluate once getattr(mw, 'note_call', None); assign in source target order to note.
          // Source: vvaharness/backends/llm/cli_mcp.py:179-180
          if (the source predicate note is not None is truthy) {
            // Source: vvaharness/backends/llm/cli_mcp.py:180-180
            In source order: Evaluate note(bound_name); retain side effects and discard the expression result.
          }
        }
        // Source: vvaharness/backends/llm/cli_mcp.py:181-187
        Perform the following protected operations {
          // Source: vvaharness/backends/llm/cli_mcp.py:183-183
          In source order: Evaluate once await asyncio.to_thread(bound_tool.invoke, dict(args)); assign in source target order to result.
        }
        // Source: vvaharness/backends/llm/cli_mcp.py:184-187
        On the first matching source exception Exception as exc, in handler order {
          // Source: vvaharness/backends/llm/cli_mcp.py:185-185
          In source order: Evaluate COUNTERS.bump(source_template_185_34); retain side effects and discard the expression result.
          // Source: vvaharness/backends/llm/cli_mcp.py:186-187
          End this invocation with _content(source_template_187_24, is_error=True).
        }
        // Source: vvaharness/backends/llm/cli_mcp.py:188-189
        In source order: Evaluate once _content(_serialize(result)); assign in source target order to payload. Then Evaluate _log_tool_call(bound_name, payload, tag_sfx); retain side effects and discard the expression result.
        // Source: vvaharness/backends/llm/cli_mcp.py:190-190
        End this invocation with payload.
        If execution reaches this end, finish with the source implicit None result.
      }
      At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
      // Source: vvaharness/backends/llm/cli_mcp.py:192-192
      End this invocation with _handler.
      If execution reaches this end, finish with the source implicit None result.
    }
    // Source: vvaharness/backends/llm/cli_mcp.py:194-194
    In source order: Evaluate out.append(_make()); retain side effects and discard the expression result.
  }
  // Source: vvaharness/backends/llm/cli_mcp.py:195-195
  End this invocation with out.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cli_mcp.py:198-203
// Source signature: _schema_for(response_model: type) -> dict[str, object]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _schema_for(response_model) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli_mcp.py:199-202
  In source order: Retain source documentation literal source_literal_199_4; it is not a model call. Then Evaluate once dict(response_model.model_json_schema()); assign in source target order to schema. Then Evaluate schema.pop('title', None); retain side effects and discard the expression result. Then Evaluate schema.pop('$schema', None); retain side effects and discard the expression result.
  // Source: vvaharness/backends/llm/cli_mcp.py:203-203
  End this invocation with schema.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cli_mcp.py:206-213
// Source signature: _serialize(result: object) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _serialize(result) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli_mcp.py:207-207
  In source order: Retain source documentation literal source_literal_207_4; it is not a model call.
  // Source: vvaharness/backends/llm/cli_mcp.py:208-209
  if (the source predicate isinstance(result, str) is truthy) {
    // Source: vvaharness/backends/llm/cli_mcp.py:209-209
    End this invocation with result.
  }
  // Source: vvaharness/backends/llm/cli_mcp.py:210-213
  Perform the following protected operations {
    // Source: vvaharness/backends/llm/cli_mcp.py:211-211
    End this invocation with json.dumps(result, default=str).
  }
  // Source: vvaharness/backends/llm/cli_mcp.py:212-213
  On the first matching source exception (TypeError, ValueError), in handler order {
    // Source: vvaharness/backends/llm/cli_mcp.py:213-213
    End this invocation with str(result).
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cli_mcp.py:216-227
// Source signature: _content(text: str, *, is_error: bool=False) -> dict[str, Any]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _content(text, is_error) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli_mcp.py:217-224
  In source order: Retain source documentation literal source_literal_217_4; it is not a model call. Then Resolve source import from vvaharness.backends.llm.agent_sdk import _redact_tool_output; preserve alias and import-time effects. Then For payload, assign {'content': [{'type': 'text', 'text': cast('str', _redact_tool_output(text))}]}; source annotation dict[str, Any].
  // Source: vvaharness/backends/llm/cli_mcp.py:225-226
  if (the source predicate is_error is truthy) {
    // Source: vvaharness/backends/llm/cli_mcp.py:226-226
    In source order: Evaluate once True; assign in source target order to payload['is_error'].
  }
  // Source: vvaharness/backends/llm/cli_mcp.py:227-227
  End this invocation with payload.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cli_mcp.py:232-235
// Source signature: _bridge_env() -> dict[str, str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _bridge_env() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli_mcp.py:233-233
  In source order: Retain source documentation literal source_literal_233_4; it is not a model call.
  // Source: vvaharness/backends/llm/cli_mcp.py:235-235
  End this invocation with {**os.environ, **_cli.env._tls_extra}.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cli_mcp.py:238-241
// Source signature: _session_env(extra_env: dict[str, str] | None, tier: str | None) -> dict[str, str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _session_env(extra_env, tier) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli_mcp.py:239-239
  In source order: Retain source documentation literal source_literal_239_4; it is not a model call.
  // Source: vvaharness/backends/llm/cli_mcp.py:241-241
  End this invocation with {**_bridge_env(), **(extra_env or {}), **_cli._session_pins(tier)}.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cli_mcp.py:244-398
// Source signature: _build_options(*, model: str, system_prompt: str | None, allowed_tools: Sequence[str] | None, cwd: str, mcp_tool_names: Sequence[str], max_turns: int | None, max_budget_usd: float | None, effort: str | None, allow_shell: bool, server: Any, response_model: type | None=None, parent_middleware: Sequence[Any]=(), extra_env: dict[str, str] | None=None) -> Any
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _build_options(model, system_prompt, allowed_tools, cwd, mcp_tool_names, max_turns, max_budget_usd, effort, allow_shell, server, response_model, parent_middleware, extra_env) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli_mcp.py:252-252
  In source order: Retain source documentation literal source_literal_252_4; it is not a model call.
  // Source: vvaharness/backends/llm/cli_mcp.py:253-265
  Perform the following protected operations {
    // Source: vvaharness/backends/llm/cli_mcp.py:254-257
    In source order: Resolve source import from claude_agent_sdk import ClaudeAgentOptions, HookMatcher; preserve alias and import-time effects.
  }
  // Source: vvaharness/backends/llm/cli_mcp.py:258-265
  On the first matching source exception ImportError as e, in handler order {
    // Source: vvaharness/backends/llm/cli_mcp.py:259-265
    Raise RuntimeError(source_literal_260_12) with explicit source cause e.
  }
  // Source: vvaharness/backends/llm/cli_mcp.py:266-272
  In source order: Resolve source import from vvaharness.backends.llm.agent_sdk import _build_redaction_hooks, _resolve_within_root; preserve alias and import-time effects. Then Evaluate once Path(cwd).resolve(); assign in source target order to root. Then Evaluate once _cli.session._bare_tool_names(allowed_tools); assign in source target order to native.
  // Source: vvaharness/backends/llm/cli_mcp.py:274-275
  if (the source predicate not allow_shell is truthy) {
    // Source: vvaharness/backends/llm/cli_mcp.py:275-275
    In source order: Evaluate once [n for n in native if n != 'Bash']; assign in source target order to native.
  }
  // Source: vvaharness/backends/llm/cli_mcp.py:276-278
  In source order: Evaluate once frozenset(native); assign in source target order to granted. Then Evaluate once frozenset((d.casefold() for d in _cli._READ_DENY_DIRS)); assign in source target order to deny_dirs_cf.
  // Source: vvaharness/backends/llm/cli_mcp.py:280-353
  // Source signature: _pre_tool_use_gate(input_data, tool_use_id, context)
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _pre_tool_use_gate(input_data, tool_use_id, context) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    This callable produces a coroutine or async generator; await/suspension positions remain in source expressions.
    // Source: vvaharness/backends/llm/cli_mcp.py:281-281
    In source order: Retain source documentation literal source_literal_281_8; it is not a model call.
    // Source: vvaharness/backends/llm/cli_mcp.py:293-298
    // Source signature: _deny(reason: str) -> dict
    Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
    fn _deny(reason) {
      Bind arguments/defaults/annotations exactly as the source signature specifies.
      // Source: vvaharness/backends/llm/cli_mcp.py:294-298
      End this invocation with {'hookSpecificOutput': {'hookEventName': 'PreToolUse', 'permissionDecision': 'deny', 'permissionDecisionReason': reason}}.
      If execution reaches this end, finish with the source implicit None result.
    }
    // Source: vvaharness/backends/llm/cli_mcp.py:300-353
    Perform the following protected operations {
      // Source: vvaharness/backends/llm/cli_mcp.py:301-302
      In source order: Evaluate once (input_data or {}).get('tool_name') or ''; assign in source target order to tool_name. Then Evaluate once (input_data or {}).get('tool_input') or {}; assign in source target order to tool_input.
      // Source: vvaharness/backends/llm/cli_mcp.py:304-306
      if (the source predicate tool_name.startswith(TOOL_PREFIX) is truthy) {
        // Source: vvaharness/backends/llm/cli_mcp.py:306-306
        End this invocation with {}.
      }
      // Source: vvaharness/backends/llm/cli_mcp.py:307-316
      if (the source predicate tool_name == CLI_STRUCTURED_OUTPUT_TOOL is truthy) {
        // Source: vvaharness/backends/llm/cli_mcp.py:309-311
        if (the source predicate response_model is None is truthy) {
          // Source: vvaharness/backends/llm/cli_mcp.py:310-311
          End this invocation with _deny(source_template_310_33).
        }
        // Source: vvaharness/backends/llm/cli_mcp.py:313-313
        In source order: Evaluate once _submit_guard(parent_middleware); assign in source target order to hold_text.
        // Source: vvaharness/backends/llm/cli_mcp.py:314-315
        if (the source predicate hold_text is not None is truthy) {
          // Source: vvaharness/backends/llm/cli_mcp.py:315-315
          End this invocation with _deny(hold_text).
        }
        // Source: vvaharness/backends/llm/cli_mcp.py:316-316
        End this invocation with {}.
      }
      // Source: vvaharness/backends/llm/cli_mcp.py:317-321
      if (the source predicate tool_name not in granted is truthy) {
        // Source: vvaharness/backends/llm/cli_mcp.py:318-321
        End this invocation with _deny(source_template_318_29).
      }
      // Source: vvaharness/backends/llm/cli_mcp.py:322-322
      In source order: Evaluate once ('file_path', 'path', 'notebook_path'); assign in source target order to keys.
      // Source: vvaharness/backends/llm/cli_mcp.py:323-327
      if (the source predicate tool_name == 'Glob' is truthy) {
        // Source: vvaharness/backends/llm/cli_mcp.py:324-324
        In source order: Evaluate once (*keys, 'pattern'); assign in source target order to keys.
      }
      else {
        // Source: vvaharness/backends/llm/cli_mcp.py:325-327
        if (the source predicate tool_name == 'Grep' is truthy) {
          // Source: vvaharness/backends/llm/cli_mcp.py:327-327
          In source order: Evaluate once (*keys, 'glob'); assign in source target order to keys.
        }
      }
      // Source: vvaharness/backends/llm/cli_mcp.py:328-328
      In source order: Evaluate once False; assign in source target order to found_path_arg.
      // Source: vvaharness/backends/llm/cli_mcp.py:329-344
      for each key in keys {
        // Source: vvaharness/backends/llm/cli_mcp.py:330-330
        In source order: Evaluate once tool_input.get(key); assign in source target order to raw.
        // Source: vvaharness/backends/llm/cli_mcp.py:331-332
        if (the source predicate not raw is truthy) {
          // Source: vvaharness/backends/llm/cli_mcp.py:332-332
          Continue the immediately enclosing source loop at its next iteration.
        }
        // Source: vvaharness/backends/llm/cli_mcp.py:333-334
        In source order: Evaluate once True; assign in source target order to found_path_arg. Then Evaluate once _resolve_within_root(root, raw); assign in source target order to resolved.
        // Source: vvaharness/backends/llm/cli_mcp.py:335-338
        if (the source predicate resolved is None is truthy) {
          // Source: vvaharness/backends/llm/cli_mcp.py:336-338
          End this invocation with _deny(source_template_336_33).
        }
        // Source: vvaharness/backends/llm/cli_mcp.py:340-340
        In source order: Evaluate once resolved.relative_to(root).parts; assign in source target order to parts.
        // Source: vvaharness/backends/llm/cli_mcp.py:341-344
        if (the source predicate parts and parts[0].casefold() in deny_dirs_cf is truthy) {
          // Source: vvaharness/backends/llm/cli_mcp.py:342-344
          End this invocation with _deny(source_template_342_33).
        }
      }
      // Source: vvaharness/backends/llm/cli_mcp.py:346-349
      if (the source predicate tool_name == 'Read' and (not found_path_arg) is truthy) {
        // Source: vvaharness/backends/llm/cli_mcp.py:347-349
        End this invocation with _deny(source_template_347_29).
      }
      // Source: vvaharness/backends/llm/cli_mcp.py:350-350
      End this invocation with {}.
    }
    // Source: vvaharness/backends/llm/cli_mcp.py:351-353
    On the first matching source exception Exception as exc, in handler order {
      // Source: vvaharness/backends/llm/cli_mcp.py:352-353
      End this invocation with _deny(source_template_352_25).
    }
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/llm/cli_mcp.py:356-387
  In source order: Evaluate once _build_redaction_hooks() or {}; assign in source target order to redaction_hooks. Then Evaluate once {**redaction_hooks, 'PreToolUse': [HookMatcher(hooks=[_pre_tool_use_gate])]}; assign in source target order to hooks. Then Evaluate once _cli._effective_effort(effort); assign in source target order to tier. Then Evaluate once ClaudeAgentOptions(model=model, cwd=str(root), env=_session_env(extra_env, tier), cli_path=_cli._CLAUDE_CMD[0], mcp_servers={SERVER_NAME: server}, strict_mcp_config=True, setting_sources=('user',), extra_args={'disable-slash-commands': None}, tools=native, allowed_tools=[*native, *mcp_tool_names], disallowed_tools=[*([] if allow_shell else ['Bash']), *(source_template_380_14 for d in _cli._READ_DENY_DIRS)], permission_mode='default', hooks=hooks, verbatim_prompts=True); assign in source target order to opts.
  // Source: vvaharness/backends/llm/cli_mcp.py:388-389
  if (the source predicate system_prompt is not None is truthy) {
    // Source: vvaharness/backends/llm/cli_mcp.py:389-389
    In source order: Evaluate once system_prompt; assign in source target order to opts.system_prompt.
  }
  // Source: vvaharness/backends/llm/cli_mcp.py:390-391
  if (the source predicate max_turns is not None is truthy) {
    // Source: vvaharness/backends/llm/cli_mcp.py:391-391
    In source order: Evaluate once int(max_turns); assign in source target order to opts.max_turns.
  }
  // Source: vvaharness/backends/llm/cli_mcp.py:392-393
  if (the source predicate max_budget_usd is not None is truthy) {
    // Source: vvaharness/backends/llm/cli_mcp.py:393-393
    In source order: Evaluate once float(max_budget_usd); assign in source target order to opts.max_budget_usd.
  }
  // Source: vvaharness/backends/llm/cli_mcp.py:394-395
  if (the source predicate tier is truthy) {
    // Source: vvaharness/backends/llm/cli_mcp.py:395-395
    In source order: Evaluate once tier; assign in source target order to opts.effort.
  }
  // Source: vvaharness/backends/llm/cli_mcp.py:396-397
  if (the source predicate response_model is not None is truthy) {
    // Source: vvaharness/backends/llm/cli_mcp.py:397-397
    In source order: Evaluate once {'type': 'json_schema', 'schema': _schema_for(response_model)}; assign in source target order to opts.output_format.
  }
  // Source: vvaharness/backends/llm/cli_mcp.py:398-398
  End this invocation with opts.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cli_mcp.py:403-404
interface _SessionTruncatedError {
  Describe the source Python type, preserving its base/metaclass expression order: Exception.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/llm/cli_mcp.py:404-404
  In source order: Retain source documentation literal source_literal_404_4; it is not a model call.
}
// Source: vvaharness/backends/llm/cli_mcp.py:408-409
interface _SessionResultError {
  Describe the source Python type, preserving its base/metaclass expression order: Exception.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/llm/cli_mcp.py:409-409
  In source order: Retain source documentation literal source_literal_409_4; it is not a model call.
}
// Source: vvaharness/backends/llm/cli_mcp.py:413-475
// Source signature: _run(*, user_prompt: str, opts: Any, timeout: float | None=None, tag: str | None=None, effort: str | None=None) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _run(user_prompt, opts, timeout, tag, effort) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  This callable produces a coroutine or async generator; await/suspension positions remain in source expressions.
  // Source: vvaharness/backends/llm/cli_mcp.py:415-425
  In source order: Retain source documentation literal source_literal_415_4; it is not a model call. Then Resolve source import from claude_agent_sdk import AssistantMessage, ClaudeSDKClient, TextBlock; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm.agent_sdk import drain_until_result; preserve alias and import-time effects. Then For parts, assign []; source annotation list[str].
  // Source: vvaharness/backends/llm/cli_mcp.py:427-439
  // Source signature: _on_message(message: Any) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _on_message(message) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/llm/cli_mcp.py:428-430
    if (the source predicate _cli.aborted() is truthy) {
      // Source: vvaharness/backends/llm/cli_mcp.py:430-430
      Raise RuntimeError('aborted by user (Ctrl-C)').
    }
    // Source: vvaharness/backends/llm/cli_mcp.py:431-439
    if (the source predicate isinstance(message, AssistantMessage) is truthy) {
      // Source: vvaharness/backends/llm/cli_mcp.py:432-439
      for each block in message.content {
        // Source: vvaharness/backends/llm/cli_mcp.py:433-439
        if (the source predicate isinstance(block, TextBlock) is truthy) {
          // Source: vvaharness/backends/llm/cli_mcp.py:434-439
          In source order: Evaluate parts.append(block.text); retain side effects and discard the expression result. Then Evaluate _cli.stream_trace(json.dumps({'type': 'assistant', 'message': {'content': [{'type': 'text', 'text': block.text}]}})); retain side effects and discard the expression result.
        }
      }
    }
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/llm/cli_mcp.py:441-441
  In source order: Evaluate once time.monotonic(); assign in source target order to started.
  // Source: vvaharness/backends/llm/cli_mcp.py:442-445
  Await and enter source context managers left-to-right: ClaudeSDKClient(options=opts) bound to client {
    // Source: vvaharness/backends/llm/cli_mcp.py:443-445
    In source order: Evaluate await client.query(user_prompt); retain side effects and discard the expression result. Then Evaluate once await drain_until_result(client, on_message=_on_message, timeout=timeout, grace=TIMEOUT_STOP_GRACE_SECONDS); assign in source target order to drained.
  }
  Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics and await async exits.
  // Source: vvaharness/backends/llm/cli_mcp.py:446-451
  In source order: Evaluate once time.monotonic() - started; assign in source target order to elapsed. Then Evaluate once drained.result; assign in source target order to result. Then Evaluate once cast('dict | None', result.usage) if result is not None else None; assign in source target order to usage. Then Evaluate once result.total_cost_usd if result is not None else None; assign in source target order to usd. Then Evaluate once result.num_turns if result is not None else None; assign in source target order to turns.
  // Source: vvaharness/backends/llm/cli_mcp.py:453-453
  In source order: Evaluate TOKENS.add(cast('TokenUsage', usage), usd=usd, turns=turns); retain side effects and discard the expression result.
  // Source: vvaharness/backends/llm/cli_mcp.py:455-458
  if (the source predicate drained.timed_out is truthy) {
    // Source: vvaharness/backends/llm/cli_mcp.py:456-458
    Raise call_timeout_error(stage=tag or '', route='cli-mcp', budget_s=timeout, effort=effort, cause_text=source_template_458_23).
  }
  // Source: vvaharness/backends/llm/cli_mcp.py:460-461
  In source order: Evaluate note_budget_use(elapsed, timeout, effort); retain side effects and discard the expression result. Then Evaluate once result.stop_reason if result is not None else None; assign in source target order to stop_reason.
  // Source: vvaharness/backends/llm/cli_mcp.py:462-463
  if (the source predicate stop_reason is truthy) {
    // Source: vvaharness/backends/llm/cli_mcp.py:463-463
    In source order: Evaluate console.write(source_template_463_22); retain side effects and discard the expression result.
  }
  // Source: vvaharness/backends/llm/cli_mcp.py:464-474
  In source order: Evaluate once result.result if result is not None else None; assign in source target order to result_text. Then Evaluate _check_terminal_result(stop_reason=stop_reason, is_error=result.is_error if result is not None else False, subtype=result.subtype if result is not None else None, api_error_status=result.api_error_status if result is not None else None, errors=result.errors if result is not None else None, result_text=result_text, tag=tag); retain side effects and discard the expression result. Then Evaluate once result.structured_output if result is not None else None; assign in source target order to structured. Then Evaluate _note_structured_miss(opts, structured); retain side effects and discard the expression result. Then Evaluate once _cli._structured_text({'structured_output': structured}); assign in source target order to structured_text.
  // Source: vvaharness/backends/llm/cli_mcp.py:475-475
  End this invocation with (structured_text or result_text or ''.join(parts)).strip().
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cli_mcp.py:478-488
// Source signature: _note_structured_miss(opts: Any, structured: object) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _note_structured_miss(opts, structured) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli_mcp.py:479-479
  In source order: Retain source documentation literal source_literal_479_4; it is not a model call.
  // Source: vvaharness/backends/llm/cli_mcp.py:482-483
  if (the source predicate opts.output_format is None or structured is not None is truthy) {
    // Source: vvaharness/backends/llm/cli_mcp.py:483-483
    End this invocation with None.
  }
  // Source: vvaharness/backends/llm/cli_mcp.py:484-488
  In source order: Evaluate COUNTERS.bump('cli_mcp_structured_output_missing'); retain side effects and discard the expression result. Then Evaluate warn_once(_WARNED, source_template_485_23, source_template_486_14); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cli_mcp.py:491-511
// Source signature: _check_terminal_result(*, stop_reason: str | None, is_error: bool, subtype: str | None, api_error_status: int | None, errors: list | None, result_text: str | None, tag: str | None=None) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _check_terminal_result(stop_reason, is_error, subtype, api_error_status, errors, result_text, tag) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli_mcp.py:495-495
  In source order: Retain source documentation literal source_literal_495_4; it is not a model call.
  // Source: vvaharness/backends/llm/cli_mcp.py:497-498
  if (the source predicate stop_reason == ANTHROPIC_STOP_REFUSAL is truthy) {
    // Source: vvaharness/backends/llm/cli_mcp.py:498-498
    Raise model_refusal(route='cli-mcp', stage=tag or '', category=None).
  }
  // Source: vvaharness/backends/llm/cli_mcp.py:500-501
  if (the source predicate stop_reason == _cli.ANTHROPIC_STOP_MAX_TOKENS is truthy) {
    // Source: vvaharness/backends/llm/cli_mcp.py:501-501
    Raise _SessionTruncatedError(stop_reason).
  }
  // Source: vvaharness/backends/llm/cli_mcp.py:502-511
  if (the source predicate is_error or (subtype and subtype != 'success') is truthy) {
    // Source: vvaharness/backends/llm/cli_mcp.py:503-504
    In source order: Evaluate once '; '.join((str(e) for e in errors or [] if e)) or ((result_text or '').strip() or 'no detail reported by the CLI'); assign in source target order to detail.
    // Source: vvaharness/backends/llm/cli_mcp.py:507-508
    if (the source predicate CLI_TOKEN_CAP_RX.search(detail) is truthy) {
      // Source: vvaharness/backends/llm/cli_mcp.py:508-508
      Raise _SessionTruncatedError(stop_reason).
    }
    // Source: vvaharness/backends/llm/cli_mcp.py:509-511
    Raise _SessionResultError(source_template_510_12).
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cli_mcp.py:514-524
// Source signature: _reraise_transport(exc: Exception, *, tag: str) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _reraise_transport(exc, tag) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli_mcp.py:515-517
  In source order: Retain source documentation literal source_literal_515_4; it is not a model call. Then Evaluate once redact(str(exc))[:400]; assign in source target order to text.
  // Source: vvaharness/backends/llm/cli_mcp.py:518-521
  if (the source predicate _cli._PROXY_FAILURE.search(text) is truthy) {
    // Source: vvaharness/backends/llm/cli_mcp.py:519-521
    Raise ProxyError(text, status_code=407 if re.search('\\b407\\b', text) else None, backend='cli') with explicit source cause exc.
  }
  // Source: vvaharness/backends/llm/cli_mcp.py:522-523
  if (the source predicate _cli._AUTH_FAILURE.search(text) is truthy) {
    // Source: vvaharness/backends/llm/cli_mcp.py:523-523
    Raise AuthenticationError(text, status_code=401, backend='cli') with explicit source cause exc.
  }
  // Source: vvaharness/backends/llm/cli_mcp.py:524-524
  Raise RuntimeError(source_template_524_23) with explicit source cause exc.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cli_mcp.py:527-545
// Source signature: _truncation_retry_budget(trunc_retried: int, *, tag: str | None, max_tokens: int | None=None) -> tuple[int, int | None]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _truncation_retry_budget(trunc_retried, tag, max_tokens) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli_mcp.py:529-529
  In source order: Retain source documentation literal source_literal_529_4; it is not a model call.
  // Source: vvaharness/backends/llm/cli_mcp.py:532-539
  if (the source predicate trunc_retried or max_tokens is truthy) {
    // Source: vvaharness/backends/llm/cli_mcp.py:533-533
    In source order: Evaluate once trunc_retried or max_tokens; assign in source target order to requested.
  }
  else {
    // Source: vvaharness/backends/llm/cli_mcp.py:535-539
    Perform the following protected operations {
      // Source: vvaharness/backends/llm/cli_mcp.py:536-537
      In source order: Evaluate once int(os.environ.get('CLAUDE_CODE_MAX_OUTPUT_TOKENS') or _cli.MODEL_MAX_OUTPUT_TOKENS); assign in source target order to requested.
    }
    // Source: vvaharness/backends/llm/cli_mcp.py:538-539
    On the first matching source exception (TypeError, ValueError), in handler order {
      // Source: vvaharness/backends/llm/cli_mcp.py:539-539
      In source order: Evaluate once _cli.MODEL_MAX_OUTPUT_TOKENS; assign in source target order to requested.
    }
  }
  // Source: vvaharness/backends/llm/cli_mcp.py:540-541
  In source order: Evaluate once None if trunc_retried else _cli.truncation_retry_max(requested, cap=_cli.MODEL_MAX_OUTPUT_TOKENS); assign in source target order to retry_at.
  // Source: vvaharness/backends/llm/cli_mcp.py:542-544
  if (the source predicate retry_at is not None is truthy) {
    // Source: vvaharness/backends/llm/cli_mcp.py:543-544
    In source order: Evaluate _cli._log_truncation_retry(tag=tag, requested=requested, retry_at=retry_at, label='cli-mcp'); retain side effects and discard the expression result.
  }
  // Source: vvaharness/backends/llm/cli_mcp.py:545-545
  End this invocation with (requested, retry_at).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cli_mcp.py:548-641
// Source signature: agentic_with_tools(user_prompt: str, *, model: str, system_prompt: str | None=None, allowed_tools: Sequence[str] | None=None, cwd: str, tool_builder: Any, fact_tools: Sequence[str]=(), parent_middleware: Sequence[Any]=(), max_turns: int | None=None, max_budget_usd: float | None=None, max_tokens: int | None=None, effort: str | None=None, allow_shell: bool=False, response_model: type | None=None, tag: str | None=None, timeout: float | None=None) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn agentic_with_tools(user_prompt, model, system_prompt, allowed_tools, cwd, tool_builder, fact_tools, parent_middleware, max_turns, max_budget_usd, max_tokens, effort, allow_shell, response_model, tag, timeout) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli_mcp.py:567-567
  In source order: Retain source documentation literal source_literal_567_4; it is not a model call.
  // Source: vvaharness/backends/llm/cli_mcp.py:569-574
  if (the source predicate not available() is truthy) {
    // Source: vvaharness/backends/llm/cli_mcp.py:570-574
    Raise RuntimeError(source_literal_571_12).
  }
  // Source: vvaharness/backends/llm/cli_mcp.py:575-577
  In source order: Resolve source import from claude_agent_sdk import create_sdk_mcp_server; preserve alias and import-time effects.
  // Source: vvaharness/backends/llm/cli_mcp.py:579-580
  if (the source predicate _cli.aborted() is truthy) {
    // Source: vvaharness/backends/llm/cli_mcp.py:580-580
    Raise RuntimeError('aborted by user (Ctrl-C)').
  }
  // Source: vvaharness/backends/llm/cli_mcp.py:582-583
  In source order: Evaluate once _materialize(tool_builder, model=model, cwd=cwd, fact_tools=fact_tools); assign in source target order to lc_tools.
  // Source: vvaharness/backends/llm/cli_mcp.py:584-589
  if (the source predicate not lc_tools is truthy) {
    // Source: vvaharness/backends/llm/cli_mcp.py:586-589
    Raise RuntimeError(source_template_587_12).
  }
  // Source: vvaharness/backends/llm/cli_mcp.py:591-599
  In source order: For called, assign set(); source annotation set[str]. Then Evaluate once _to_sdk_tools(lc_tools, parent_middleware=parent_middleware, called=called, tag=tag); assign in source target order to sdk_tools. Then Evaluate once create_sdk_mcp_server(SERVER_NAME, tools=sdk_tools); assign in source target order to server. Then Evaluate once [mcp_name(t.name) for t in lc_tools]; assign in source target order to wire_names. Then Evaluate once _cli._effective_effort(effort); assign in source target order to tier.
  // Source: vvaharness/backends/llm/cli_mcp.py:600-609
  In source order: Evaluate once effort_scaled_seconds(timeout, tier, kind=ClockKind.SESSION); assign in source target order to scaled_timeout. Then Evaluate once source_template_602_14 if tag else ''; assign in source target order to tag_sfx. Then Evaluate console.write(source_template_603_18); retain side effects and discard the expression result. Then Evaluate once 0; assign in source target order to trunc_retried. Then Evaluate once {'CLAUDE_CODE_MAX_OUTPUT_TOKENS': str(max_tokens)} if max_tokens else None; assign in source target order to extra_env.
  // Source: vvaharness/backends/llm/cli_mcp.py:610-637
  while (the source predicate True is truthy) {
    // Source: vvaharness/backends/llm/cli_mcp.py:611-617
    In source order: Evaluate once _build_options(model=model, system_prompt=system_prompt, allowed_tools=allowed_tools, cwd=cwd, mcp_tool_names=wire_names, max_turns=max_turns, max_budget_usd=max_budget_usd, effort=tier, allow_shell=allow_shell, server=server, response_model=response_model, parent_middleware=parent_middleware, extra_env=extra_env); assign in source target order to opts.
    // Source: vvaharness/backends/llm/cli_mcp.py:618-634
    Perform the following protected operations {
      // Source: vvaharness/backends/llm/cli_mcp.py:619-620
      In source order: Evaluate once asyncio.run(_run(user_prompt=user_prompt, opts=opts, timeout=scaled_timeout, tag=tag, effort=tier)); assign in source target order to text.
    }
    // Source: vvaharness/backends/llm/cli_mcp.py:621-629
    On the first matching source exception _SessionTruncatedError, in handler order {
      // Source: vvaharness/backends/llm/cli_mcp.py:622-623
      In source order: Evaluate once _truncation_retry_budget(trunc_retried, tag=tag, max_tokens=max_tokens); assign in source target order to (requested, retry_at).
      // Source: vvaharness/backends/llm/cli_mcp.py:624-627
      if (the source predicate retry_at is not None is truthy) {
        // Source: vvaharness/backends/llm/cli_mcp.py:625-626
        In source order: Evaluate once {'CLAUDE_CODE_MAX_OUTPUT_TOKENS': str(retry_at)}; assign in source target order to extra_env. Then Evaluate once retry_at; assign in source target order to trunc_retried.
        // Source: vvaharness/backends/llm/cli_mcp.py:627-627
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/backends/llm/cli_mcp.py:628-629
      Raise _cli._truncation_error(requested=requested, retried=trunc_retried, tag=tag, retry_at=retry_at) with explicit source cause None.
    }
    // Source: vvaharness/backends/llm/cli_mcp.py:630-631
    On the first matching source exception (AuthenticationError, ProxyError, RuntimeError, TimeoutError), in handler order {
      // Source: vvaharness/backends/llm/cli_mcp.py:631-631
      Raise the currently handled exception.
    }
    // Source: vvaharness/backends/llm/cli_mcp.py:632-634
    On the first matching source exception Exception as exc, in handler order {
      // Source: vvaharness/backends/llm/cli_mcp.py:633-633
      In source order: Evaluate _reraise_transport(exc, tag=tag or ''); retain side effects and discard the expression result.
      // Source: vvaharness/backends/llm/cli_mcp.py:634-634
      Raise the currently handled exception.
    }
    // Source: vvaharness/backends/llm/cli_mcp.py:635-636
    if (the source predicate trunc_retried is truthy) {
      // Source: vvaharness/backends/llm/cli_mcp.py:636-636
      In source order: Evaluate COUNTERS.bump(TRUNCATED_RETRY_RECOVERED_COUNTER); retain side effects and discard the expression result.
    }
    // Source: vvaharness/backends/llm/cli_mcp.py:637-637
    Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
  }
  // Source: vvaharness/backends/llm/cli_mcp.py:639-640
  In source order: Evaluate _report_evidence_degradation(parent_middleware, called, tag=tag or ''); retain side effects and discard the expression result. Then Evaluate check_response_quality(text, stage=tag or ''); retain side effects and discard the expression result.
  // Source: vvaharness/backends/llm/cli_mcp.py:641-641
  End this invocation with text.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cli_mcp.py:644-658
// Source signature: _report_evidence_degradation(parent_middleware: Sequence[Any], called: set[str], *, tag: str) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _report_evidence_degradation(parent_middleware, called, tag) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli_mcp.py:646-648
  In source order: Retain source documentation literal source_literal_646_4; it is not a model call. Then Evaluate once _required_fact_tools(parent_middleware); assign in source target order to required.
  // Source: vvaharness/backends/llm/cli_mcp.py:649-650
  if (the source predicate not required or required & called is truthy) {
    // Source: vvaharness/backends/llm/cli_mcp.py:650-650
    End this invocation with None.
  }
  // Source: vvaharness/backends/llm/cli_mcp.py:651-658
  In source order: Evaluate COUNTERS.bump(EVIDENCE_UNENFORCED_COUNTER); retain side effects and discard the expression result. Then Evaluate warn_once(_WARNED, source_template_653_17, source_template_654_8); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cli_mcp.py:661-668
In source order: Evaluate once ['EVIDENCE_UNENFORCED_COUNTER', 'SERVER_NAME', 'TOOL_PREFIX', 'agentic_with_tools', 'available', 'mcp_name']; assign in source target order to __all__.
```

## Local import links

- `from vvaharness.backends.harness.models import AuthenticationError, ProxyError` at source line 35: `source_detail/vvaharness/backends/harness/models.py.sudo.md`.
- `from vvaharness.backends.llm import cli as _cli` at source line 39: `source_detail/vvaharness/backends/llm/__init__.py.sudo.md`.
- `from vvaharness.backends.llm import cli as _cli` at source line 39: `source_detail/vvaharness/backends/llm/cli/__init__.py.sudo.md`.
- `from vvaharness.backends.llm.models import ANTHROPIC_STOP_REFUSAL, CLI_STRUCTURED_OUTPUT_TOOL, CLI_TOKEN_CAP_RX, TIMEOUT_STOP_GRACE_SECONDS, TRUNCATED_RETRY_RECOVERED_COUNTER, ClockKind, call_timeout_error, effort_scaled_seconds, model_refusal, note_budget_use` at source line 40: `source_detail/vvaharness/backends/llm/models.py.sudo.md`.
- `from vvaharness.report.redact import redact` at source line 52: `source_detail/vvaharness/report/redact.py.sudo.md`.
- `from vvaharness.util import console` at source line 53: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import console` at source line 53: `source_detail/vvaharness/util/console.py.sudo.md`.
- `from vvaharness.util.counters import COUNTERS` at source line 54: `source_detail/vvaharness/util/counters.py.sudo.md`.
- `from vvaharness.util.response_quality import check_response_quality` at source line 55: `source_detail/vvaharness/util/response_quality.py.sudo.md`.
- `from vvaharness.util.scan_progress import is_stage_only` at source line 56: `source_detail/vvaharness/util/scan_progress.py.sudo.md`.
- `from vvaharness.util.tokens import TOKENS, TokenUsage` at source line 57: `source_detail/vvaharness/util/tokens.py.sudo.md`.
- `from vvaharness.util.warn_once import warn_once` at source line 58: `source_detail/vvaharness/util/warn_once.py.sudo.md`.
- `from vvaharness.backends.harness import StreamingOptions` at source line 94: `source_detail/vvaharness/backends/harness/__init__.py.sudo.md`.
- `from vvaharness.backends.llm.agent_sdk import _redact_tool_output` at source line 218: `source_detail/vvaharness/backends/llm/agent_sdk.py.sudo.md`.
- `from vvaharness.backends.llm.agent_sdk import _build_redaction_hooks, _resolve_within_root` at source line 266: `source_detail/vvaharness/backends/llm/agent_sdk.py.sudo.md`.
- `from vvaharness.backends.llm.agent_sdk import drain_until_result` at source line 423: `source_detail/vvaharness/backends/llm/agent_sdk.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../prompt_representation/vvaharness/backends/llm/cli_mcp.py.sudo.md). Exact strings in the evidence asset support this conversion.
