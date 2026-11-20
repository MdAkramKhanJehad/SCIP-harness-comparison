# vvaharness/backends/harness/claude/options.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/backends/harness/claude/options.py.evidence.json`. SHA-256: `9599d65938641fff4faee39ec7b1313318bfbc2b0ffc48071f0a7a12b727929c`.

```sudo
// Source: vvaharness/backends/harness/claude/options.py:15-30
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from collections.abc import Collection, Mapping, Sequence; preserve alias and import-time effects. Then Resolve source import from typing import Any, Literal, cast; preserve alias and import-time effects. Then Resolve source import from claude_agent_sdk import AgentDefinition, CanUseTool, ClaudeAgentOptions, HookMatcher, PermissionResultAllow, PermissionResultDeny, ToolPermissionContext; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/claude/options.py:31-44
In source order: Resolve source import from claude_agent_sdk.types import SettingSource as SdkSettingSource; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.models import EffortLevel, OneShotOptions, SettingSource, StreamingOptions, SubagentDefinition; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.permissions import PermissionsPolicy; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm.cli import _NO_REFUSAL_RESEND_ENV; preserve alias and import-time effects. Then Evaluate once 'facts'; assign in source target order to FACT_SERVER_NAME.
// Source: vvaharness/backends/harness/claude/options.py:45-48
In source order: Evaluate once source_template_45_19; assign in source target order to FACT_TOOL_PREFIX. Then Evaluate once ('Agent', 'Task'); assign in source target order to SUBAGENT_DISPATCH_TOOLS. Then Evaluate once Literal['low', 'medium', 'high', 'xhigh', 'max']; assign in source target order to _SdkEffort.
// Source: vvaharness/backends/harness/claude/options.py:51-54
// Source signature: _to_effort(effort: str | None) -> _SdkEffort | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _to_effort(effort) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/claude/options.py:52-53
  In source order: Retain source documentation literal source_literal_52_4; it is not a model call. Then Evaluate once EffortLevel.parse(effort); assign in source target order to parsed.
  // Source: vvaharness/backends/harness/claude/options.py:54-54
  End this invocation with cast(_SdkEffort, parsed.value) if parsed is not None else None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/claude/options.py:57-66
// Source signature: _to_setting_sources(sources: tuple[str, ...]) -> list[SdkSettingSource]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _to_setting_sources(sources) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/claude/options.py:58-59
  In source order: Retain source documentation literal source_literal_58_4; it is not a model call. Then For out, assign []; source annotation list[SdkSettingSource].
  // Source: vvaharness/backends/harness/claude/options.py:60-65
  for each s in sources {
    // Source: vvaharness/backends/harness/claude/options.py:61-64
    Perform the following protected operations {
      // Source: vvaharness/backends/harness/claude/options.py:62-62
      In source order: Evaluate once SettingSource(s); assign in source target order to member.
    }
    // Source: vvaharness/backends/harness/claude/options.py:63-64
    On the first matching source exception ValueError, in handler order {
      // Source: vvaharness/backends/harness/claude/options.py:64-64
      Raise ValueError(source_template_64_29) with explicit source cause None.
    }
    // Source: vvaharness/backends/harness/claude/options.py:65-65
    In source order: Evaluate out.append(cast(SdkSettingSource, member.value)); retain side effects and discard the expression result.
  }
  // Source: vvaharness/backends/harness/claude/options.py:66-66
  End this invocation with out.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/claude/options.py:69-83
// Source signature: _permissions_callback(policy: PermissionsPolicy) -> CanUseTool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _permissions_callback(policy) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/claude/options.py:70-70
  In source order: Retain source documentation literal source_literal_70_4; it is not a model call.
  // Source: vvaharness/backends/harness/claude/options.py:71-81
  // Source signature: gate(tool_name: str, input_data: dict[str, object], _context: ToolPermissionContext) -> PermissionResultAllow | PermissionResultDeny
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn gate(tool_name, input_data, _context) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    This callable produces a coroutine or async generator; await/suspension positions remain in source expressions.
    // Source: vvaharness/backends/harness/claude/options.py:76-76
    In source order: Evaluate once policy.evaluate(tool_name, input_data); assign in source target order to decision.
    // Source: vvaharness/backends/harness/claude/options.py:77-78
    if (the source predicate decision.allow is truthy) {
      // Source: vvaharness/backends/harness/claude/options.py:78-78
      End this invocation with PermissionResultAllow(updated_input=input_data).
    }
    // Source: vvaharness/backends/harness/claude/options.py:79-81
    End this invocation with PermissionResultDeny(message=decision.reason, interrupt=decision.interrupt).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/claude/options.py:83-83
  End this invocation with cast(CanUseTool, gate).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/claude/options.py:86-111
// Source signature: _to_agent_definition(subagent: SubagentDefinition, *, bridged_tools: Sequence[str]=()) -> AgentDefinition
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _to_agent_definition(subagent, bridged_tools) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/claude/options.py:88-97
  In source order: Retain source documentation literal source_literal_88_4; it is not a model call. Then Resolve source import from vvaharness.backends.harness.claude.facts import SUBMIT_TOOL, mcp_name, rewrite_tool_names; preserve alias and import-time effects. Then Evaluate once rewrite_tool_names(list(subagent.tools) if subagent.tools is not None else None, bridged_tools); assign in source target order to tools.
  // Source: vvaharness/backends/harness/claude/options.py:98-101
  if (the source predicate tools is not None and SUBMIT_TOOL in bridged_tools is truthy) {
    // Source: vvaharness/backends/harness/claude/options.py:99-99
    In source order: Evaluate once mcp_name(SUBMIT_TOOL); assign in source target order to submit_name.
    // Source: vvaharness/backends/harness/claude/options.py:100-101
    if (the source predicate submit_name not in tools is truthy) {
      // Source: vvaharness/backends/harness/claude/options.py:101-101
      In source order: Evaluate once [*tools, submit_name]; assign in source target order to tools.
    }
  }
  // Source: vvaharness/backends/harness/claude/options.py:103-111
  End this invocation with AgentDefinition(description=subagent.description, prompt=subagent.prompt, tools=tools, disallowedTools=list(subagent.disallowed_tools) if subagent.disallowed_tools is not None else None, model=subagent.model, skills=list(subagent.skills) if subagent.skills is not None else None).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/claude/options.py:114-131
// Source signature: _foreground_subagent_hook(agent_names: Collection[str]) -> Any
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _foreground_subagent_hook(agent_names) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/claude/options.py:115-116
  In source order: Retain source documentation literal source_literal_115_4; it is not a model call. Then Evaluate once frozenset(agent_names); assign in source target order to names.
  // Source: vvaharness/backends/harness/claude/options.py:118-129
  // Source signature: hook(input_data: Any, _tool_use_id: str | None, _context: Any) -> dict[str, Any]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn hook(input_data, _tool_use_id, _context) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    This callable produces a coroutine or async generator; await/suspension positions remain in source expressions.
    // Source: vvaharness/backends/harness/claude/options.py:120-120
    In source order: Evaluate once (input_data or {}).get('tool_input') or {}; assign in source target order to tool_input.
    // Source: vvaharness/backends/harness/claude/options.py:121-124
    if (the source predicate (input_data or {}).get('tool_name') not in SUBAGENT_DISPATCH_TOOLS or tool_input.get('subagent_type') not in names or tool_input.get('run_in_background') is False is truthy) {
      // Source: vvaharness/backends/harness/claude/options.py:124-124
      End this invocation with {}.
    }
    // Source: vvaharness/backends/harness/claude/options.py:125-129
    End this invocation with {'hookSpecificOutput': {'hookEventName': 'PreToolUse', 'permissionDecision': 'allow', 'updatedInput': {**tool_input, 'run_in_background': False}}}.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/claude/options.py:131-131
  End this invocation with hook.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/claude/options.py:134-150
// Source signature: _apply_foreground_subagents(opts: ClaudeAgentOptions, options: StreamingOptions, fact_tool_names: Sequence[str]) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _apply_foreground_subagents(opts, options, fact_tool_names) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/claude/options.py:136-140
  In source order: Retain source documentation literal source_literal_136_4; it is not a model call. Then Resolve source import from vvaharness.backends.harness.claude.facts import SUBMIT_TOOL, mcp_name; preserve alias and import-time effects.
  // Source: vvaharness/backends/harness/claude/options.py:142-143
  if (the source predicate not options.agents or mcp_name(SUBMIT_TOOL) not in fact_tool_names is truthy) {
    // Source: vvaharness/backends/harness/claude/options.py:143-143
    End this invocation with None.
  }
  // Source: vvaharness/backends/harness/claude/options.py:144-150
  In source order: Evaluate once dict(opts.hooks or {}); assign in source target order to hooks. Then Evaluate once [*hooks.get('PreToolUse', []), HookMatcher(matcher='|'.join(SUBAGENT_DISPATCH_TOOLS), hooks=[_foreground_subagent_hook(options.agents)])]; assign in source target order to hooks['PreToolUse']. Then Evaluate once hooks; assign in source target order to opts.hooks.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/claude/options.py:153-155
// Source signature: _build_output_format(schema: Mapping[str, object]) -> dict[str, object]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _build_output_format(schema) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/claude/options.py:154-154
  In source order: Retain source documentation literal source_literal_154_4; it is not a model call.
  // Source: vvaharness/backends/harness/claude/options.py:155-155
  End this invocation with {'type': 'json_schema', 'schema': dict(schema)}.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/claude/options.py:158-160
// Source signature: _sanitize_schema(schema: Mapping[str, object]) -> dict[str, object]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _sanitize_schema(schema) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/claude/options.py:159-159
  In source order: Retain source documentation literal source_literal_159_4; it is not a model call.
  // Source: vvaharness/backends/harness/claude/options.py:160-160
  End this invocation with {key: value for key, value in schema.items() if key != '$schema'}.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/claude/options.py:163-174
// Source signature: _resolve_output_schema(options: OneShotOptions | StreamingOptions) -> dict[str, object] | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _resolve_output_schema(options) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/claude/options.py:166-166
  In source order: Retain source documentation literal source_literal_166_4; it is not a model call.
  // Source: vvaharness/backends/harness/claude/options.py:167-168
  if (the source predicate options.output_schema is not None is truthy) {
    // Source: vvaharness/backends/harness/claude/options.py:168-168
    End this invocation with _sanitize_schema(options.output_schema).
  }
  // Source: vvaharness/backends/harness/claude/options.py:169-169
  In source order: Evaluate once getattr(options.response_model, 'model_json_schema', None); assign in source target order to dump.
  // Source: vvaharness/backends/harness/claude/options.py:170-171
  if (the source predicate not callable(dump) is truthy) {
    // Source: vvaharness/backends/harness/claude/options.py:171-171
    End this invocation with None.
  }
  // Source: vvaharness/backends/harness/claude/options.py:173-173
  In source order: Evaluate once dump(); assign in source target order to schema.
  // Source: vvaharness/backends/harness/claude/options.py:174-174
  End this invocation with _sanitize_schema(schema) if isinstance(schema, Mapping) else None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/claude/options.py:177-197
// Source signature: _base_opts(options: OneShotOptions | StreamingOptions) -> ClaudeAgentOptions
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _base_opts(options) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/claude/options.py:178-188
  In source order: Retain source documentation literal source_literal_178_4; it is not a model call. Then Evaluate once ClaudeAgentOptions(model=options.model, cwd=options.cwd, env={**options.env, **_NO_REFUSAL_RESEND_ENV}, effort=_to_effort(options.effort), verbatim_prompts=True); assign in source target order to opts.
  // Source: vvaharness/backends/harness/claude/options.py:190-191
  if (the source predicate options.cli_path is truthy) {
    // Source: vvaharness/backends/harness/claude/options.py:191-191
    In source order: Evaluate once options.cli_path; assign in source target order to opts.cli_path.
  }
  // Source: vvaharness/backends/harness/claude/options.py:192-193
  if (the source predicate options.system_prompt is not None is truthy) {
    // Source: vvaharness/backends/harness/claude/options.py:193-193
    In source order: Evaluate once options.system_prompt; assign in source target order to opts.system_prompt.
  }
  // Source: vvaharness/backends/harness/claude/options.py:194-196
  if (the source predicate options.tool_policy is not None is truthy) {
    // Source: vvaharness/backends/harness/claude/options.py:195-196
    In source order: Evaluate once list(options.tool_policy.allowed_tools); assign in source target order to opts.allowed_tools. Then Evaluate once list(options.tool_policy.disallowed_tools); assign in source target order to opts.disallowed_tools.
  }
  // Source: vvaharness/backends/harness/claude/options.py:197-197
  End this invocation with opts.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/claude/options.py:200-207
// Source signature: _apply_agents(opts: ClaudeAgentOptions, options: StreamingOptions, *, bridged_tools: Sequence[str]=()) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _apply_agents(opts, options, bridged_tools) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/claude/options.py:202-202
  In source order: Retain source documentation literal source_literal_202_4; it is not a model call.
  // Source: vvaharness/backends/harness/claude/options.py:203-207
  if (the source predicate options.agents is truthy) {
    // Source: vvaharness/backends/harness/claude/options.py:204-207
    In source order: Evaluate once {name: _to_agent_definition(a, bridged_tools=bridged_tools) for name, a in options.agents.items()}; assign in source target order to opts.agents.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/claude/options.py:210-217
// Source signature: _apply_fact_server(opts: ClaudeAgentOptions, fact_server: object | None, fact_tool_names: Sequence[str]) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _apply_fact_server(opts, fact_server, fact_tool_names) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/claude/options.py:212-212
  In source order: Retain source documentation literal source_literal_212_4; it is not a model call.
  // Source: vvaharness/backends/harness/claude/options.py:213-214
  if (the source predicate fact_server is None is truthy) {
    // Source: vvaharness/backends/harness/claude/options.py:214-214
    End this invocation with None.
  }
  // Source: vvaharness/backends/harness/claude/options.py:215-217
  In source order: Evaluate once {FACT_SERVER_NAME: fact_server}; assign in source target order to opts.mcp_servers. Then Evaluate once True; assign in source target order to opts.strict_mcp_config. Then Evaluate once [*(opts.allowed_tools or []), *fact_tool_names]; assign in source target order to opts.allowed_tools.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/claude/options.py:220-229
// Source signature: build_oneshot_sdk_options(options: OneShotOptions) -> ClaudeAgentOptions
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn build_oneshot_sdk_options(options) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/claude/options.py:221-225
  In source order: Retain source documentation literal source_literal_221_4; it is not a model call. Then Evaluate once _base_opts(options); assign in source target order to opts. Then Evaluate once options.max_turns; assign in source target order to opts.max_turns. Then Evaluate once 'default'; assign in source target order to opts.permission_mode. Then Evaluate once None; assign in source target order to opts.setting_sources.
  // Source: vvaharness/backends/harness/claude/options.py:226-226
  In source order: Evaluate once _resolve_output_schema(options); assign in source target order to schema.
  // Source: vvaharness/backends/harness/claude/options.py:227-228
  if (the source predicate schema is not None is truthy) {
    // Source: vvaharness/backends/harness/claude/options.py:228-228
    In source order: Evaluate once _build_output_format(schema); assign in source target order to opts.output_format.
  }
  // Source: vvaharness/backends/harness/claude/options.py:229-229
  End this invocation with opts.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/claude/options.py:232-256
// Source signature: build_streaming_sdk_options(options: StreamingOptions, *, fact_server: object | None=None, fact_tool_names: Sequence[str]=()) -> ClaudeAgentOptions
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn build_streaming_sdk_options(options, fact_server, fact_tool_names) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/claude/options.py:237-238
  In source order: Retain source documentation literal source_literal_237_4; it is not a model call. Then Evaluate once _base_opts(options); assign in source target order to opts.
  // Source: vvaharness/backends/harness/claude/options.py:239-240
  if (the source predicate options.max_turns is not None is truthy) {
    // Source: vvaharness/backends/harness/claude/options.py:240-240
    In source order: Evaluate once options.max_turns; assign in source target order to opts.max_turns.
  }
  // Source: vvaharness/backends/harness/claude/options.py:241-242
  if (the source predicate options.max_budget_usd is not None is truthy) {
    // Source: vvaharness/backends/harness/claude/options.py:242-242
    In source order: Evaluate once options.max_budget_usd; assign in source target order to opts.max_budget_usd.
  }
  // Source: vvaharness/backends/harness/claude/options.py:243-244
  if (the source predicate options.setting_sources is not None is truthy) {
    // Source: vvaharness/backends/harness/claude/options.py:244-244
    In source order: Evaluate once _to_setting_sources(options.setting_sources); assign in source target order to opts.setting_sources.
  }
  // Source: vvaharness/backends/harness/claude/options.py:245-246
  if (the source predicate options.permissions is not None is truthy) {
    // Source: vvaharness/backends/harness/claude/options.py:246-246
    In source order: Evaluate once _permissions_callback(options.permissions); assign in source target order to opts.can_use_tool.
  }
  // Source: vvaharness/backends/harness/claude/options.py:248-248
  In source order: Evaluate once _resolve_output_schema(options); assign in source target order to schema.
  // Source: vvaharness/backends/harness/claude/options.py:249-250
  if (the source predicate schema is not None is truthy) {
    // Source: vvaharness/backends/harness/claude/options.py:250-250
    In source order: Evaluate once _build_output_format(schema); assign in source target order to opts.output_format.
  }
  // Source: vvaharness/backends/harness/claude/options.py:251-255
  In source order: Evaluate _apply_fact_server(opts, fact_server, fact_tool_names); retain side effects and discard the expression result. Then Evaluate _apply_agents(opts, options, bridged_tools=[name.removeprefix(FACT_TOOL_PREFIX) for name in fact_tool_names]); retain side effects and discard the expression result. Then Evaluate _apply_foreground_subagents(opts, options, fact_tool_names); retain side effects and discard the expression result.
  // Source: vvaharness/backends/harness/claude/options.py:256-256
  End this invocation with opts.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.backends.harness.models import EffortLevel, OneShotOptions, SettingSource, StreamingOptions, SubagentDefinition` at source line 33: `source_detail/vvaharness/backends/harness/models.py.sudo.md`.
- `from vvaharness.backends.harness.permissions import PermissionsPolicy` at source line 40: `source_detail/vvaharness/backends/harness/permissions.py.sudo.md`.
- `from vvaharness.backends.llm.cli import _NO_REFUSAL_RESEND_ENV` at source line 41: `source_detail/vvaharness/backends/llm/cli/__init__.py.sudo.md`.
- `from vvaharness.backends.harness.claude.facts import SUBMIT_TOOL, mcp_name, rewrite_tool_names` at source line 89: `source_detail/vvaharness/backends/harness/claude/facts.py.sudo.md`.
- `from vvaharness.backends.harness.claude.facts import SUBMIT_TOOL, mcp_name` at source line 137: `source_detail/vvaharness/backends/harness/claude/facts.py.sudo.md`.
