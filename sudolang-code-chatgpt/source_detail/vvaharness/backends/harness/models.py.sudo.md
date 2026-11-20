# vvaharness/backends/harness/models.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/backends/harness/models.py.evidence.json`. SHA-256: `a8ae2c8e255aa3d22b94e08b87c23bb590bb46dc7455b41cc09fab85b2611b0d`.

```sudo
// Source: vvaharness/backends/harness/models.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from collections.abc import Callable, Mapping; preserve alias and import-time effects. Then Resolve source import from dataclasses import dataclass, field; preserve alias and import-time effects. Then Resolve source import from enum import StrEnum; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/models.py:22-27
In source order: Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from typing import TYPE_CHECKING, Any, Final, Literal; preserve alias and import-time effects. Then Resolve source import from pydantic import BaseModel; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.tokens import TokenUsage; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/models.py:29-32
if (the source predicate TYPE_CHECKING is truthy) {
  // Source: vvaharness/backends/harness/models.py:30-32
  In source order: Resolve source import from langchain.agents.middleware.types import AgentMiddleware; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.permissions import PermissionsPolicy; preserve alias and import-time effects.
}
// Source: vvaharness/backends/harness/models.py:36-54
In source order: For LOGICAL_TO_NATIVE, assign {'Read': 'read_file', 'Grep': 'grep', 'Glob': 'glob', 'Edit': 'edit_file', 'Write': 'write_file'}; source annotation Final[Mapping[str, str]]. Then For READ_TOOLS, assign frozenset({'Read', 'Grep', 'Glob'}); source annotation Final[frozenset[str]]. Then For ORCHESTRATION_TOOLS, assign frozenset({'Agent', 'Task', 'TodoWrite', 'Skill'}); source annotation Final[frozenset[str]]. Then For MUTATING_TOOLS, assign frozenset({'Bash', 'Edit', 'NotebookEdit', 'Write'}); source annotation Final[frozenset[str]]. Then For READ_ONLY_TOOLS, assign READ_TOOLS | ORCHESTRATION_TOOLS; source annotation Final[frozenset[str]].
// Source: vvaharness/backends/harness/models.py:57-71
In source order: For UNCONDITIONALLY_DENIED_TOOLS, assign MUTATING_TOOLS - {'Write', 'Bash'}; source annotation Final[frozenset[str]]. Then For NATIVE_WRITE_TOOLS, assign frozenset((LOGICAL_TO_NATIVE[name] for name in MUTATING_TOOLS if name in LOGICAL_TO_NATIVE)); source annotation Final[frozenset[str]]. Then For NATIVE_CONTENT_TOOLS, assign frozenset({'read_file', 'grep'}); source annotation Final[frozenset[str]]. Then For NATIVE_IMPLIED_READS, assign frozenset({'ls'}); source annotation Final[frozenset[str]]. Then For NATIVE_SHELL_TOOL, assign 'execute'; source annotation Final.
// Source: vvaharness/backends/harness/models.py:74-77
In source order: For LEGACY_AGENT_TOOL, assign 'Agent'; source annotation Final. Then For MCP_TOOL_PREFIX, assign 'mcp__'; source annotation Final.
// Source: vvaharness/backends/harness/models.py:80-95
interface EffortLevel {
  Describe the source Python type, preserving its base/metaclass expression order: StrEnum.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/harness/models.py:81-86
  In source order: Retain source documentation literal source_literal_81_4; it is not a model call. Then Evaluate once 'low'; assign in source target order to LOW. Then Evaluate once 'medium'; assign in source target order to MEDIUM. Then Evaluate once 'high'; assign in source target order to HIGH. Then Evaluate once 'xhigh'; assign in source target order to XHIGH.
  // Source: vvaharness/backends/harness/models.py:87-87
  In source order: Evaluate once 'max'; assign in source target order to MAX.
  // Source: vvaharness/backends/harness/models.py:90-95
  // Source: vvaharness/backends/harness/models.py:89-89
  Before creating this callable, evaluate and retain decorators top-to-bottom: classmethod.
  // Source: vvaharness/backends/harness/models.py:90-95
  // Source signature: parse(cls, value: str | None) -> EffortLevel | None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn parse(cls, value) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/models.py:91-91
    In source order: Retain source documentation literal source_literal_91_8; it is not a model call.
    // Source: vvaharness/backends/harness/models.py:92-95
    Perform the following protected operations {
      // Source: vvaharness/backends/harness/models.py:93-93
      End this invocation with cls(value).
    }
    // Source: vvaharness/backends/harness/models.py:94-95
    On the first matching source exception ValueError, in handler order {
      // Source: vvaharness/backends/harness/models.py:95-95
      End this invocation with None.
    }
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
}
// Source: vvaharness/backends/harness/models.py:98-103
interface SettingSource {
  Describe the source Python type, preserving its base/metaclass expression order: StrEnum.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/harness/models.py:99-103
  In source order: Retain source documentation literal source_literal_99_4; it is not a model call. Then Evaluate once 'user'; assign in source target order to USER. Then Evaluate once 'project'; assign in source target order to PROJECT. Then Evaluate once 'local'; assign in source target order to LOCAL.
}
// Source: vvaharness/backends/harness/models.py:106-110
interface Provider {
  Describe the source Python type, preserving its base/metaclass expression order: StrEnum.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/harness/models.py:107-110
  In source order: Retain source documentation literal source_literal_107_4; it is not a model call. Then Evaluate once 'anthropic'; assign in source target order to ANTHROPIC. Then Evaluate once 'openai'; assign in source target order to OPENAI.
}
// Source: vvaharness/backends/harness/models.py:114-118
// Source: vvaharness/backends/harness/models.py:113-113
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vvaharness/backends/harness/models.py:114-118
interface ToolPolicy {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/harness/models.py:115-118
  In source order: Retain source documentation literal source_literal_115_4; it is not a model call. Then For allowed_tools, assign (); source annotation tuple[str, ...]. Then For disallowed_tools, assign (); source annotation tuple[str, ...].
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vvaharness/backends/harness/models.py:122-130
// Source: vvaharness/backends/harness/models.py:121-121
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vvaharness/backends/harness/models.py:122-130
interface FactToolSpec {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/harness/models.py:123-130
  In source order: Retain source documentation literal source_literal_123_4; it is not a model call. Then For name, declare without assigning a value; source annotation str. Then For description, declare without assigning a value; source annotation str. Then For input_schema, declare without assigning a value; source annotation dict[str, Any]. Then For fn, declare without assigning a value; source annotation Callable[..., Any].
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vvaharness/backends/harness/models.py:134-146
// Source: vvaharness/backends/harness/models.py:133-133
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vvaharness/backends/harness/models.py:134-146
interface SubagentDefinition {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/harness/models.py:135-140
  In source order: Retain source documentation literal source_literal_135_4; it is not a model call. Then For name, declare without assigning a value; source annotation str. Then For description, declare without assigning a value; source annotation str. Then For prompt, declare without assigning a value; source annotation str. Then For tools, assign None; source annotation tuple[str, ...] | None.
  // Source: vvaharness/backends/harness/models.py:141-146
  In source order: For disallowed_tools, assign None; source annotation tuple[str, ...] | None. Then For model, assign None; source annotation str | None. Then For skills, assign None; source annotation tuple[str, ...] | None. Then For response_model, assign None; source annotation type | None. Then For max_model_calls, assign None; source annotation int | None.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vvaharness/backends/harness/models.py:150-155
// Source: vvaharness/backends/harness/models.py:149-149
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vvaharness/backends/harness/models.py:150-155
interface PermissionDecision {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/harness/models.py:151-155
  In source order: Retain source documentation literal source_literal_151_4; it is not a model call. Then For allow, declare without assigning a value; source annotation bool. Then For reason, assign ''; source annotation str. Then For interrupt, assign False; source annotation bool.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vvaharness/backends/harness/models.py:159-159
In source order: Evaluate once Callable[..., list[Any]]; assign in source target order to ToolBuilder.
// Source: vvaharness/backends/harness/models.py:162-172
// Source signature: compose_tool_builders(*builders: ToolBuilder | None) -> ToolBuilder
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn compose_tool_builders(builders) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/models.py:163-164
  In source order: Retain source documentation literal source_literal_163_4; it is not a model call. Then Evaluate once [b for b in builders if b is not None]; assign in source target order to live.
  // Source: vvaharness/backends/harness/models.py:166-170
  // Source signature: _build(*args: Any, **kwargs: Any) -> list[Any]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _build(args, kwargs) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/models.py:167-167
    In source order: For out, assign []; source annotation list[Any].
    // Source: vvaharness/backends/harness/models.py:168-169
    for each b in live {
      // Source: vvaharness/backends/harness/models.py:169-169
      In source order: Evaluate out.extend(b(*args, **kwargs) or []); retain side effects and discard the expression result.
    }
    // Source: vvaharness/backends/harness/models.py:170-170
    End this invocation with out.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/models.py:172-172
  End this invocation with _build.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/models.py:176-176
In source order: For DEFAULT_GRAPH_NAME, assign 'agent'; source annotation Final.
// Source: vvaharness/backends/harness/models.py:180-221
// Source: vvaharness/backends/harness/models.py:179-179
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass.
// Source: vvaharness/backends/harness/models.py:180-221
interface SessionOptions {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/harness/models.py:181-187
  In source order: Retain source documentation literal source_literal_181_4; it is not a model call. Then For model, declare without assigning a value; source annotation str. Then For cwd, declare without assigning a value; source annotation Path. Then For env, assign field(default_factory=dict); source annotation dict[str, str]. Then For model_provider, assign None; source annotation str | None.
  // Source: vvaharness/backends/harness/models.py:188-195
  In source order: For effort, assign None; source annotation str | None. Then For think_in_prompt, assign False; source annotation bool. Then For use_responses_api, assign None; source annotation bool | None. Then For system_prompt, assign None; source annotation str | None. Then For tool_policy, assign None; source annotation ToolPolicy | None.
  // Source: vvaharness/backends/harness/models.py:196-204
  In source order: For cli_path, assign None; source annotation str | None. Then For response_model, assign None; source annotation type | None. Then For tool_builder, assign None; source annotation ToolBuilder | None. Then For fact_tools, assign (); source annotation tuple[str, ...]. Then For fact_tool_specs, assign (); source annotation tuple[FactToolSpec, ...].
  // Source: vvaharness/backends/harness/models.py:206-213
  In source order: For allow_writes, assign False; source annotation bool. Then For writable_paths, assign (); source annotation tuple[str, ...]. Then For skill_root, assign None; source annotation Path | None. Then For graph_name, assign DEFAULT_GRAPH_NAME; source annotation str. Then For max_output_tokens, assign None; source annotation int | None.
  // Source: vvaharness/backends/harness/models.py:215-221
  In source order: For output_cap, assign None; source annotation int | None. Then For cache_markers, assign True; source annotation bool. Then For parent_middleware, assign (); source annotation tuple[AgentMiddleware, ...]. Then For force_verdict_only, assign False; source annotation bool.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vvaharness/backends/harness/models.py:225-231
// Source: vvaharness/backends/harness/models.py:224-224
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass.
// Source: vvaharness/backends/harness/models.py:225-231
interface OneShotOptions {
  Describe the source Python type, preserving its base/metaclass expression order: SessionOptions.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/harness/models.py:226-231
  In source order: Retain source documentation literal source_literal_226_4; it is not a model call. Then For max_turns, assign 15; source annotation int. Then For output_schema, assign None; source annotation Mapping[str, object] | None. Then For cache_prefix, assign None; source annotation str | None.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vvaharness/backends/harness/models.py:235-257
// Source: vvaharness/backends/harness/models.py:234-234
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass.
// Source: vvaharness/backends/harness/models.py:235-257
interface StreamingOptions {
  Describe the source Python type, preserving its base/metaclass expression order: SessionOptions.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/harness/models.py:236-244
  In source order: Retain source documentation literal source_literal_236_4; it is not a model call. Then For max_turns, assign None; source annotation int | None. Then For max_budget_usd, assign None; source annotation float | None. Then For timeout, assign None; source annotation float | None. Then For allow_shell, assign False; source annotation bool.
  // Source: vvaharness/backends/harness/models.py:245-250
  In source order: For setting_sources, assign None; source annotation tuple[str, ...] | None. Then For permissions, assign None; source annotation PermissionsPolicy | None. Then For agents, assign field(default_factory=dict); source annotation dict[str, SubagentDefinition]. Then For output_schema, assign None; source annotation dict[str, object] | None. Then For permitted_tool_calls, assign None; source annotation frozenset[str] | None.
  // Source: vvaharness/backends/harness/models.py:252-257
  In source order: For cache_prefix, assign None; source annotation str | None. Then For session_id, assign ''; source annotation str.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vvaharness/backends/harness/models.py:261-266
// Source: vvaharness/backends/harness/models.py:260-260
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass.
// Source: vvaharness/backends/harness/models.py:261-266
interface HarnessSessionInit {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/harness/models.py:262-266
  In source order: Retain source documentation literal source_literal_262_4; it is not a model call. Then For kind, assign 'session_init'; source annotation Literal['session_init']. Then For session_id, assign ''; source annotation str. Then For raw, assign field(default_factory=dict); source annotation dict[str, object].
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vvaharness/backends/harness/models.py:271-277
// Source: vvaharness/backends/harness/models.py:270-270
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass.
// Source: vvaharness/backends/harness/models.py:271-277
interface HarnessAssistantText {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/harness/models.py:272-277
  In source order: Retain source documentation literal source_literal_272_4; it is not a model call. Then For kind, assign 'assistant_text'; source annotation Literal['assistant_text']. Then For text, assign ''; source annotation str. Then For agent, assign None; source annotation str | None. Then For namespace, assign None; source annotation tuple[str, ...] | None.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vvaharness/backends/harness/models.py:281-289
// Source: vvaharness/backends/harness/models.py:280-280
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass.
// Source: vvaharness/backends/harness/models.py:281-289
interface HarnessToolUse {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/harness/models.py:282-287
  In source order: Retain source documentation literal source_literal_282_4; it is not a model call. Then For kind, assign 'tool_use'; source annotation Literal['tool_use']. Then For tool_id, assign ''; source annotation str. Then For name, assign ''; source annotation str. Then For input, assign field(default_factory=dict); source annotation dict[str, object].
  // Source: vvaharness/backends/harness/models.py:288-289
  In source order: For agent, assign None; source annotation str | None. Then For namespace, assign None; source annotation tuple[str, ...] | None.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vvaharness/backends/harness/models.py:293-300
// Source: vvaharness/backends/harness/models.py:292-292
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass.
// Source: vvaharness/backends/harness/models.py:293-300
interface HarnessToolResult {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/harness/models.py:294-299
  In source order: Retain source documentation literal source_literal_294_4; it is not a model call. Then For kind, assign 'tool_result'; source annotation Literal['tool_result']. Then For is_error, assign False; source annotation bool. Then For content, assign None; source annotation object. Then For agent, assign None; source annotation str | None.
  // Source: vvaharness/backends/harness/models.py:300-300
  In source order: For namespace, assign None; source annotation tuple[str, ...] | None.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vvaharness/backends/harness/models.py:304-326
// Source: vvaharness/backends/harness/models.py:303-303
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass.
// Source: vvaharness/backends/harness/models.py:304-326
interface HarnessResult {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/harness/models.py:305-311
  In source order: Retain source documentation literal source_literal_305_4; it is not a model call. Then For kind, assign 'result'; source annotation Literal['result']. Then For subtype, assign ''; source annotation str. Then For is_error, assign False; source annotation bool. Then For session_id, assign None; source annotation str | None.
  // Source: vvaharness/backends/harness/models.py:312-318
  In source order: For result_text, assign None; source annotation str | None. Then For structured, assign None; source annotation BaseModel | None. Then For errors, assign None; source annotation list[str] | None. Then For usage, assign None; source annotation TokenUsage | None. Then For total_cost_usd, assign None; source annotation float | None.
  // Source: vvaharness/backends/harness/models.py:320-326
  In source order: For state, assign None; source annotation object. Then For truncated, assign False; source annotation bool. Then For refused, assign False; source annotation bool. Then For refusal_category, assign None; source annotation str | None.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vvaharness/backends/harness/models.py:329-335
In source order: Evaluate once HarnessSessionInit | HarnessAssistantText | HarnessToolUse | HarnessToolResult | HarnessResult; assign in source target order to HarnessMessage.
// Source: vvaharness/backends/harness/models.py:339-353
// Source: vvaharness/backends/harness/models.py:338-338
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass.
// Source: vvaharness/backends/harness/models.py:339-353
interface OneShotResult {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/harness/models.py:340-345
  In source order: Retain source documentation literal source_literal_340_4; it is not a model call. Then For is_error, assign False; source annotation bool. Then For subtype, assign ''; source annotation str. Then For result_text, assign None; source annotation str | None. Then For structured, assign None; source annotation BaseModel | None.
  // Source: vvaharness/backends/harness/models.py:347-353
  In source order: For usage, assign None; source annotation TokenUsage | None. Then For total_cost_usd, assign None; source annotation float | None. Then For truncated, assign False; source annotation bool. Then For refused, assign False; source annotation bool. Then For refusal_category, assign None; source annotation str | None.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vvaharness/backends/harness/models.py:356-357
interface HarnessError {
  Describe the source Python type, preserving its base/metaclass expression order: Exception.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/harness/models.py:357-357
  In source order: Retain source documentation literal source_literal_357_4; it is not a model call.
}
// Source: vvaharness/backends/harness/models.py:360-365
interface SessionNotResumableError {
  Describe the source Python type, preserving its base/metaclass expression order: HarnessError.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/harness/models.py:361-365
  In source order: Retain source documentation literal source_literal_361_4; it is not a model call.
}
// Source: vvaharness/backends/harness/models.py:368-369
interface HarnessCLINotFoundError {
  Describe the source Python type, preserving its base/metaclass expression order: HarnessError.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/harness/models.py:369-369
  In source order: Retain source documentation literal source_literal_369_4; it is not a model call.
}
// Source: vvaharness/backends/harness/models.py:372-373
interface HarnessConnectionError {
  Describe the source Python type, preserving its base/metaclass expression order: HarnessError.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/harness/models.py:373-373
  In source order: Retain source documentation literal source_literal_373_4; it is not a model call.
}
// Source: vvaharness/backends/harness/models.py:376-392
interface HarnessProcessError {
  Describe the source Python type, preserving its base/metaclass expression order: HarnessError.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/harness/models.py:377-377
  In source order: Retain source documentation literal source_literal_377_4; it is not a model call.
  // Source: vvaharness/backends/harness/models.py:379-392
  // Source signature: __init__(self, message: str, exit_code: int | None=None, stderr: str | None=None, *, recursion_limited: bool=False) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self, message, exit_code, stderr, recursion_limited) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/models.py:387-392
    In source order: Retain source documentation literal source_literal_387_8; it is not a model call. Then Evaluate super().__init__(message); retain side effects and discard the expression result. Then Evaluate once exit_code; assign in source target order to self.exit_code. Then Evaluate once stderr; assign in source target order to self.stderr. Then Evaluate once recursion_limited; assign in source target order to self.recursion_limited.
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vvaharness/backends/harness/models.py:395-396
interface HarnessJSONDecodeError {
  Describe the source Python type, preserving its base/metaclass expression order: HarnessError.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/harness/models.py:396-396
  In source order: Retain source documentation literal source_literal_396_4; it is not a model call.
}
// Source: vvaharness/backends/harness/models.py:399-400
interface HarnessMessageParseError {
  Describe the source Python type, preserving its base/metaclass expression order: HarnessError.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/harness/models.py:400-400
  In source order: Retain source documentation literal source_literal_400_4; it is not a model call.
}
// Source: vvaharness/backends/harness/models.py:403-420
In source order: Evaluate once source_literal_403_20; assign in source target order to _AUTH_REMEDIATION. Then Evaluate once source_literal_412_21; assign in source target order to _PROXY_REMEDIATION.
// Source: vvaharness/backends/harness/models.py:423-445
interface AuthenticationError {
  Describe the source Python type, preserving its base/metaclass expression order: HarnessError.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/harness/models.py:424-426
  In source order: Retain source documentation literal source_literal_424_4; it is not a model call. Then For error_code, assign 'VVAH-E001'; source annotation str.
  // Source: vvaharness/backends/harness/models.py:428-445
  // Source signature: __init__(self, message: str, *, status_code: int | None=None, backend: str='') -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self, message, status_code, backend) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/models.py:435-445
    In source order: Retain source documentation literal source_literal_435_8; it is not a model call. Then Evaluate once source_template_437_12 + (source_template_438_15 if status_code else '') + (source_template_439_15 if backend else '') + source_template_440_14 + _AUTH_REMEDIATION; assign in source target order to full. Then Evaluate super().__init__(full); retain side effects and discard the expression result. Then Evaluate once status_code; assign in source target order to self.status_code. Then Evaluate once backend; assign in source target order to self.backend.
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vvaharness/backends/harness/models.py:448-470
interface ProxyError {
  Describe the source Python type, preserving its base/metaclass expression order: HarnessConnectionError.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/harness/models.py:449-451
  In source order: Retain source documentation literal source_literal_449_4; it is not a model call. Then For error_code, assign 'VVAH-E002'; source annotation str.
  // Source: vvaharness/backends/harness/models.py:453-470
  // Source signature: __init__(self, message: str, *, status_code: int | None=None, backend: str='') -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self, message, status_code, backend) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/models.py:460-470
    In source order: Retain source documentation literal source_literal_460_8; it is not a model call. Then Evaluate once source_template_462_12 + (source_template_463_15 if status_code else '') + (source_template_464_15 if backend else '') + source_template_465_14 + _PROXY_REMEDIATION; assign in source target order to full. Then Evaluate super().__init__(full); retain side effects and discard the expression result. Then Evaluate once status_code; assign in source target order to self.status_code. Then Evaluate once backend; assign in source target order to self.backend.
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vvaharness/backends/harness/models.py:473-498
interface DegenerateResponseError {
  Describe the source Python type, preserving its base/metaclass expression order: HarnessError.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/harness/models.py:474-476
  In source order: Retain source documentation literal source_literal_474_4; it is not a model call. Then For error_code, assign 'VVAH-E003'; source annotation str.
  // Source: vvaharness/backends/harness/models.py:478-498
  // Source signature: __init__(self, message: str, *, stage: str='', response_len: int=0, threshold: int=0, consecutive: int=0) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self, message, stage, response_len, threshold, consecutive) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/models.py:487-495
    In source order: Retain source documentation literal source_literal_487_8; it is not a model call. Then Evaluate once (source_template_489_13 if stage else '') + (source_template_490_15 if threshold else '') + (source_template_491_15 if consecutive else ''); assign in source target order to detail. Then Evaluate once source_template_493_15; assign in source target order to full. Then Evaluate super().__init__(full); retain side effects and discard the expression result. Then Evaluate once stage; assign in source target order to self.stage.
    // Source: vvaharness/backends/harness/models.py:496-498
    In source order: Evaluate once response_len; assign in source target order to self.response_len. Then Evaluate once threshold; assign in source target order to self.threshold. Then Evaluate once consecutive; assign in source target order to self.consecutive.
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vvaharness/backends/harness/models.py:501-524
interface OversizePromptError {
  Describe the source Python type, preserving its base/metaclass expression order: HarnessError.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/harness/models.py:502-505
  In source order: Retain source documentation literal source_literal_502_4; it is not a model call. Then For error_code, assign 'VVAH-E004'; source annotation str.
  // Source: vvaharness/backends/harness/models.py:507-524
  // Source signature: __init__(self, message: str, *, stage: str='', estimated_tokens: int=0, limit: int=0) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self, message, stage, estimated_tokens, limit) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/models.py:515-522
    In source order: Retain source documentation literal source_literal_515_8; it is not a model call. Then Evaluate once (source_template_517_13 if stage else '') + (source_template_518_15 if limit else ''); assign in source target order to detail. Then Evaluate once source_template_520_15; assign in source target order to full. Then Evaluate super().__init__(full); retain side effects and discard the expression result. Then Evaluate once stage; assign in source target order to self.stage.
    // Source: vvaharness/backends/harness/models.py:523-524
    In source order: Evaluate once estimated_tokens; assign in source target order to self.estimated_tokens. Then Evaluate once limit; assign in source target order to self.limit.
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vvaharness/backends/harness/models.py:528-528
In source order: For TRUNCATED_BELOW_BUDGET_RATIO, assign 0.5; source annotation Final.
// Source: vvaharness/backends/harness/models.py:531-535
// Source signature: truncated_below_budget(produced: int | None, requested: int) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn truncated_below_budget(produced, requested) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/models.py:532-532
  In source order: Retain source documentation literal source_literal_532_4; it is not a model call.
  // Source: vvaharness/backends/harness/models.py:534-535
  End this invocation with produced is not None and requested > 0 and (produced < requested * TRUNCATED_BELOW_BUDGET_RATIO).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/models.py:538-576
interface TruncatedResponseError {
  Describe the source Python type, preserving its base/metaclass expression order: HarnessError.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/harness/models.py:539-541
  In source order: Retain source documentation literal source_literal_539_4; it is not a model call. Then For error_code, assign 'VVAH-E005'; source annotation str.
  // Source: vvaharness/backends/harness/models.py:543-576
  // Source signature: __init__(self, message: str, *, stage: str='', requested: int=0, retried: int=0, produced: int | None=None, reasoning_tokens: int | None=None) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self, message, stage, requested, retried, produced, reasoning_tokens) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/models.py:553-562
    In source order: Retain source documentation literal source_literal_553_8; it is not a model call. Then Evaluate once (source_template_555_13 if stage else '') + (source_template_556_15 if requested else '') + (source_template_557_15 if retried else '') + (source_template_558_15 if produced is not None else '') + (source_template_559_15 if reasoning_tokens is not None else ''); assign in source target order to detail. Then Evaluate once ''; assign in source target order to hint.
    // Source: vvaharness/backends/harness/models.py:563-569
    if (the source predicate truncated_below_budget(produced, requested) is truthy) {
      // Source: vvaharness/backends/harness/models.py:564-569
      In source order: Evaluate once source_template_565_16; assign in source target order to hint.
    }
    // Source: vvaharness/backends/harness/models.py:570-574
    In source order: Evaluate once source_template_570_15; assign in source target order to full. Then Evaluate super().__init__(full); retain side effects and discard the expression result. Then Evaluate once stage; assign in source target order to self.stage. Then Evaluate once requested; assign in source target order to self.requested. Then Evaluate once retried; assign in source target order to self.retried.
    // Source: vvaharness/backends/harness/models.py:575-576
    In source order: Evaluate once produced; assign in source target order to self.produced. Then Evaluate once reasoning_tokens; assign in source target order to self.reasoning_tokens.
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vvaharness/backends/harness/models.py:579-598
In source order: Evaluate once source_literal_579_26; assign in source target order to _TOOL_STATE_REMEDIATION.
// Source: vvaharness/backends/harness/models.py:601-625
interface ToolStateNotRoundTrippedError {
  Describe the source Python type, preserving its base/metaclass expression order: HarnessError.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/harness/models.py:602-605
  In source order: Retain source documentation literal source_literal_602_4; it is not a model call. Then For error_code, assign 'VVAH-E006'; source annotation str.
  // Source: vvaharness/backends/harness/models.py:607-625
  // Source signature: __init__(self, message: str, *, stage: str='', model_id: str='') -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self, message, stage, model_id) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/models.py:614-624
    In source order: Retain source documentation literal source_literal_614_8; it is not a model call. Then Evaluate once (source_template_616_13 if model_id else '') + (source_template_617_15 if stage else ''); assign in source target order to detail. Then Evaluate once source_template_620_12 + _TOOL_STATE_REMEDIATION; assign in source target order to full. Then Evaluate super().__init__(full); retain side effects and discard the expression result. Then Evaluate once stage; assign in source target order to self.stage.
    // Source: vvaharness/backends/harness/models.py:625-625
    In source order: Evaluate once model_id; assign in source target order to self.model_id.
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vvaharness/backends/harness/models.py:628-649
interface ModelCallBudgetExhaustedError {
  Describe the source Python type, preserving its base/metaclass expression order: HarnessError.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/harness/models.py:629-632
  In source order: Retain source documentation literal source_literal_629_4; it is not a model call. Then For error_code, assign 'VVAH-E007'; source annotation str.
  // Source: vvaharness/backends/harness/models.py:634-649
  // Source signature: __init__(self, message: str, *, stage: str='', limit: int=0) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self, message, stage, limit) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/models.py:641-648
    In source order: Retain source documentation literal source_literal_641_8; it is not a model call. Then Evaluate once (source_template_643_13 if stage else '') + (source_template_644_15 if limit else ''); assign in source target order to detail. Then Evaluate once source_template_646_15; assign in source target order to full. Then Evaluate super().__init__(full); retain side effects and discard the expression result. Then Evaluate once stage; assign in source target order to self.stage.
    // Source: vvaharness/backends/harness/models.py:649-649
    In source order: Evaluate once limit; assign in source target order to self.limit.
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vvaharness/backends/harness/models.py:652-684
interface CallTimeoutError {
  Describe the source Python type, preserving its base/metaclass expression order: HarnessError, TimeoutError.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/harness/models.py:653-657
  In source order: Retain source documentation literal source_literal_653_4; it is not a model call. Then For error_code, assign 'VVAH-E008'; source annotation str.
  // Source: vvaharness/backends/harness/models.py:659-684
  // Source signature: __init__(self, message: str, *, stage: str='', route: str='', budget_s: float | None=None, effort: str | None=None) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self, message, stage, route, budget_s, effort) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/models.py:668-680
    In source order: Retain source documentation literal source_literal_668_8; it is not a model call. Then Evaluate once source_template_669_17 if budget_s is not None else 'unbounded'; assign in source target order to budget. Then Evaluate once (source_template_671_13 if stage else '') + (source_template_672_15 if route else '') + source_template_673_14 + (source_template_674_15 if effort else ''); assign in source target order to detail. Then Evaluate once source_template_677_12; assign in source target order to full. Then Evaluate super().__init__(full); retain side effects and discard the expression result.
    // Source: vvaharness/backends/harness/models.py:681-684
    In source order: Evaluate once stage; assign in source target order to self.stage. Then Evaluate once route; assign in source target order to self.route. Then Evaluate once budget_s; assign in source target order to self.budget_s. Then Evaluate once effort; assign in source target order to self.effort.
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vvaharness/backends/harness/models.py:687-716
interface RepeatedToolCallError {
  Describe the source Python type, preserving its base/metaclass expression order: HarnessError.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/harness/models.py:688-690
  In source order: Retain source documentation literal source_literal_688_4; it is not a model call. Then For error_code, assign 'VVAH-E009'; source annotation str.
  // Source: vvaharness/backends/harness/models.py:692-716
  // Source signature: __init__(self, message: str, *, stage: str='', route: str='', tool_name: str='', repeats: int=0) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self, message, stage, route, tool_name, repeats) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/models.py:701-713
    In source order: Retain source documentation literal source_literal_701_8; it is not a model call. Then Evaluate once (source_template_703_13 if stage else '') + (source_template_704_15 if route else '') + (source_template_705_15 if tool_name else '') + (source_template_706_15 if repeats else ''); assign in source target order to detail. Then Evaluate once source_template_709_12; assign in source target order to full. Then Evaluate super().__init__(full); retain side effects and discard the expression result. Then Evaluate once stage; assign in source target order to self.stage.
    // Source: vvaharness/backends/harness/models.py:714-716
    In source order: Evaluate once route; assign in source target order to self.route. Then Evaluate once tool_name; assign in source target order to self.tool_name. Then Evaluate once repeats; assign in source target order to self.repeats.
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vvaharness/backends/harness/models.py:722-725
// Source signature: is_halt_error(exc: BaseException) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn is_halt_error(exc) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/models.py:723-723
  In source order: Retain source documentation literal source_literal_723_4; it is not a model call.
  // Source: vvaharness/backends/harness/models.py:725-725
  End this invocation with isinstance(exc, (AuthenticationError, ProxyError)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/models.py:728-730
// Source signature: is_token_error(exc: BaseException) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn is_token_error(exc) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/models.py:729-729
  In source order: Retain source documentation literal source_literal_729_4; it is not a model call.
  // Source: vvaharness/backends/harness/models.py:730-730
  End this invocation with isinstance(exc, AuthenticationError).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/models.py:733-782
In source order: Evaluate once ['DEFAULT_GRAPH_NAME', 'LEGACY_AGENT_TOOL', 'LOGICAL_TO_NATIVE', 'MCP_TOOL_PREFIX', 'MUTATING_TOOLS', 'NATIVE_CONTENT_TOOLS', 'NATIVE_IMPLIED_READS', 'NATIVE_SHELL_TOOL', 'NATIVE_WRITE_TOOLS', 'ORCHESTRATION_TOOLS', 'READ_ONLY_TOOLS', 'READ_TOOLS', 'UNCONDITIONALLY_DENIED_TOOLS', 'AuthenticationError', 'CallTimeoutError', 'DegenerateResponseError', 'EffortLevel', 'FactToolSpec', 'HarnessAssistantText', 'HarnessCLINotFoundError', 'HarnessConnectionError', 'HarnessError', 'HarnessJSONDecodeError', 'HarnessMessage', 'HarnessMessageParseError', 'HarnessProcessError', 'HarnessResult', 'HarnessSessionInit', 'HarnessToolResult', 'HarnessToolUse', 'OneShotOptions', 'OneShotResult', 'OversizePromptError', 'PermissionDecision', 'ProxyError', 'SessionNotResumableError', 'SessionOptions', 'SettingSource', 'StreamingOptions', 'SubagentDefinition', 'ToolBuilder', 'ToolPolicy', 'ToolStateNotRoundTrippedError', 'TruncatedResponseError', 'compose_tool_builders', 'is_halt_error', 'is_token_error', 'truncated_below_budget']; assign in source target order to __all__.
```

## Local import links

- `from vvaharness.util.tokens import TokenUsage` at source line 27: `source_detail/vvaharness/util/tokens.py.sudo.md`.
- `from vvaharness.backends.harness.permissions import PermissionsPolicy` at source line 32: `source_detail/vvaharness/backends/harness/permissions.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../prompt_representation/vvaharness/backends/harness/models.py.sudo.md). Exact strings in the evidence asset support this conversion.
