# vvaharness/backends/harness/deepagents/options/subagents.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/backends/harness/deepagents/options/subagents.py.evidence.json`. SHA-256: `c8bc4e55cb3281d5a69effc7c48cbece7cc3761cb40fdee884f0c1f9ada9b87f`.

```sudo
// Source: vvaharness/backends/harness/deepagents/options/subagents.py:15-25
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from collections.abc import Mapping, Sequence; preserve alias and import-time effects. Then Resolve source import from deepagents.middleware.subagents import DEFAULT_GENERAL_PURPOSE_DESCRIPTION, DEFAULT_SUBAGENT_PROMPT; preserve alias and import-time effects. Then Resolve source import from langchain.agents.middleware.types import AgentMiddleware; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/deepagents/options/subagents.py:26-31
In source order: Resolve source import from langchain_core.tools import BaseTool; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.deepagents.exclude_tools import ExcludeTools; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.deepagents.force_verdict_only import ForceVerdictOnly; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.deepagents.model_call_budget import ModelCallBudget; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.deepagents.models import DELETE_TOOL_NAME, SubagentSpec; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/deepagents/options/subagents.py:32-41
In source order: Resolve source import from vvaharness.backends.harness.deepagents.options.filesystem import _skill_sources; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.deepagents.options.graph_builder import _CONNECTION_RETRY_MIDDLEWARE; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.deepagents.options.model_building import build_model_cached; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.deepagents.options.response_format import _strategy_for, _tool_name_for; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.deepagents.permit_tools import PermitTools; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/deepagents/options/subagents.py:42-58
In source order: Resolve source import from vvaharness.backends.harness.deepagents.prompt_caching import BlockMarkerPromptCaching; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.deepagents.redaction import read_only_middleware; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.deepagents.tools import build_tools; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.models import LEGACY_AGENT_TOOL, LOGICAL_TO_NATIVE, MUTATING_TOOLS, NATIVE_IMPLIED_READS, READ_TOOLS, OneShotOptions, StreamingOptions, SubagentDefinition, ToolPolicy; preserve alias and import-time effects. Then Evaluate once 'general-purpose'; assign in source target order to GENERAL_PURPOSE_NAME.
// Source: vvaharness/backends/harness/deepagents/options/subagents.py:61-63
// Source signature: _tool_policy(options: OneShotOptions | StreamingOptions) -> ToolPolicy
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _tool_policy(options) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/options/subagents.py:62-62
  In source order: Retain source documentation literal source_literal_62_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/options/subagents.py:63-63
  End this invocation with options.tool_policy if options.tool_policy is not None else ToolPolicy().
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/options/subagents.py:66-71
// Source signature: _build_session_tools(options: StreamingOptions, allowed_tools: tuple[str, ...]) -> list[BaseTool]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _build_session_tools(options, allowed_tools) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/options/subagents.py:69-70
  In source order: Retain source documentation literal source_literal_69_4; it is not a model call. Then Evaluate once options.tool_builder or build_tools; assign in source target order to builder.
  // Source: vvaharness/backends/harness/deepagents/options/subagents.py:71-71
  End this invocation with builder(options, allowed_tools=allowed_tools).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/options/subagents.py:74-81
// Source signature: _subagent_tools(subagent: SubagentDefinition, options: StreamingOptions) -> tuple[str, ...]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _subagent_tools(subagent, options) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/options/subagents.py:75-78
  In source order: Retain source documentation literal source_literal_75_4; it is not a model call. Then Evaluate once _tool_policy(options); assign in source target order to policy. Then Evaluate once subagent.tools if subagent.tools is not None else policy.allowed_tools; assign in source target order to allowed. Then Evaluate once set(subagent.disallowed_tools or policy.disallowed_tools); assign in source target order to denied.
  // Source: vvaharness/backends/harness/deepagents/options/subagents.py:79-80
  if (the source predicate not options.allow_writes is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/subagents.py:80-80
    In source order: Apply source augmented assignment denied |= MUTATING_TOOLS with source evaluation/in-place semantics.
  }
  // Source: vvaharness/backends/harness/deepagents/options/subagents.py:81-81
  End this invocation with tuple((t for t in allowed if t not in denied)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/options/subagents.py:84-92
// Source signature: _subagent_tool_names(subagent: SubagentDefinition, options: StreamingOptions) -> tuple[str, ...]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _subagent_tool_names(subagent, options) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/options/subagents.py:87-89
  In source order: Retain source documentation literal source_literal_87_4; it is not a model call. Then Evaluate once tuple(dict.fromkeys([*_subagent_tools(subagent, options), *options.fact_tools])); assign in source target order to granted. Then Evaluate once {LEGACY_AGENT_TOOL}; assign in source target order to excluded.
  // Source: vvaharness/backends/harness/deepagents/options/subagents.py:90-91
  if (the source predicate not options.allow_writes is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/subagents.py:91-91
    In source order: Apply source augmented assignment excluded |= MUTATING_TOOLS with source evaluation/in-place semantics.
  }
  // Source: vvaharness/backends/harness/deepagents/options/subagents.py:92-92
  End this invocation with tuple((t for t in granted if t not in excluded)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/options/subagents.py:95-103
// Source signature: _general_purpose_agent(options: StreamingOptions) -> SubagentDefinition
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _general_purpose_agent(options) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/options/subagents.py:96-97
  In source order: Retain source documentation literal source_literal_96_4; it is not a model call. Then Evaluate once tuple((t for t in _tool_policy(options).allowed_tools if t in READ_TOOLS)); assign in source target order to read_tools.
  // Source: vvaharness/backends/harness/deepagents/options/subagents.py:98-103
  End this invocation with SubagentDefinition(name=GENERAL_PURPOSE_NAME, description=DEFAULT_GENERAL_PURPOSE_DESCRIPTION, prompt=DEFAULT_SUBAGENT_PROMPT, tools=read_tools).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/options/subagents.py:106-113
// Source signature: _permitted_for_spec(tool_names: Sequence[str], tools: Sequence[BaseTool]) -> frozenset[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _permitted_for_spec(tool_names, tools) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/options/subagents.py:109-110
  In source order: Retain source documentation literal source_literal_109_4; it is not a model call. Then Evaluate once {LOGICAL_TO_NATIVE.get(t, t) for t in tool_names}; assign in source target order to native.
  // Source: vvaharness/backends/harness/deepagents/options/subagents.py:111-112
  if (the source predicate native & {LOGICAL_TO_NATIVE[r] for r in READ_TOOLS} is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/subagents.py:112-112
    In source order: Apply source augmented assignment native |= NATIVE_IMPLIED_READS with source evaluation/in-place semantics.
  }
  // Source: vvaharness/backends/harness/deepagents/options/subagents.py:113-113
  End this invocation with frozenset(native | {t.name for t in tools}).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/options/subagents.py:116-126
// Source signature: _subagent_budget(subagent: SubagentDefinition) -> ModelCallBudget | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _subagent_budget(subagent) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/options/subagents.py:117-118
  In source order: Retain source documentation literal source_literal_117_4; it is not a model call. Then Evaluate once subagent.max_model_calls or 0; assign in source target order to limit.
  // Source: vvaharness/backends/harness/deepagents/options/subagents.py:119-120
  if (the source predicate limit <= 0 is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/subagents.py:120-120
    End this invocation with None.
  }
  // Source: vvaharness/backends/harness/deepagents/options/subagents.py:121-122
  In source order: Evaluate once frozenset({_tool_name_for(subagent.response_model)}) if subagent.response_model is not None else frozenset(); assign in source target order to outcome.
  // Source: vvaharness/backends/harness/deepagents/options/subagents.py:123-126
  End this invocation with ModelCallBudget(limit=limit, outcome_tools=outcome, counter=source_template_125_16).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/options/subagents.py:129-151
// Source signature: _spec_middleware(tool_names: Sequence[str], tools: Sequence[BaseTool], options: object, budget: ModelCallBudget | None=None) -> list[AgentMiddleware]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _spec_middleware(tool_names, tools, options, budget) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/options/subagents.py:133-135
  In source order: Retain source documentation literal source_literal_133_4; it is not a model call. Then For middleware, declare without assigning a value; source annotation list[AgentMiddleware].
  // Source: vvaharness/backends/harness/deepagents/options/subagents.py:136-139
  if (the source predicate set(tool_names) & MUTATING_TOOLS is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/subagents.py:137-137
    In source order: Evaluate once [ExcludeTools(frozenset({DELETE_TOOL_NAME}))]; assign in source target order to middleware.
  }
  else {
    // Source: vvaharness/backends/harness/deepagents/options/subagents.py:139-139
    In source order: Evaluate once read_only_middleware(); assign in source target order to middleware.
  }
  // Source: vvaharness/backends/harness/deepagents/options/subagents.py:140-141
  if (the source predicate getattr(options, 'permitted_tool_calls', None) is not None is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/subagents.py:141-141
    In source order: Evaluate middleware.append(PermitTools(_permitted_for_spec(tool_names, tools))); retain side effects and discard the expression result.
  }
  // Source: vvaharness/backends/harness/deepagents/options/subagents.py:144-150
  In source order: Evaluate once ForceVerdictOnly() if getattr(options, 'force_verdict_only', False) else None; assign in source target order to verdict_only. Then Evaluate middleware.extend((m for m in (budget, verdict_only) if m is not None)); retain side effects and discard the expression result. Then Evaluate middleware.append(BlockMarkerPromptCaching(enabled=bool(getattr(options, 'cache_markers', True)))); retain side effects and discard the expression result. Then Evaluate middleware.append(_CONNECTION_RETRY_MIDDLEWARE); retain side effects and discard the expression result.
  // Source: vvaharness/backends/harness/deepagents/options/subagents.py:151-151
  End this invocation with middleware.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/options/subagents.py:154-196
// Source signature: get_subagent_specs(options: StreamingOptions, *, agents: Mapping[str, SubagentDefinition] | None=None) -> list[SubagentSpec]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn get_subagent_specs(options, agents) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/options/subagents.py:159-165
  In source order: Retain source documentation literal source_literal_159_4; it is not a model call. Then For configured, assign dict(options.agents if agents is None else agents); source annotation dict[str, SubagentDefinition]. Then Evaluate configured.setdefault(GENERAL_PURPOSE_NAME, _general_purpose_agent(options)); retain side effects and discard the expression result. Then For specs, assign []; source annotation list[SubagentSpec].
  // Source: vvaharness/backends/harness/deepagents/options/subagents.py:166-195
  for each (name, subagent) in configured.items() {
    // Source: vvaharness/backends/harness/deepagents/options/subagents.py:167-184
    In source order: Evaluate once _subagent_tool_names(subagent, options); assign in source target order to tool_names. Then Evaluate once _build_session_tools(options, tool_names); assign in source target order to tools. Then Evaluate once subagent.model or options.model; assign in source target order to subagent_model_id. Then Evaluate once build_model_cached(subagent_model_id, options.env, options.model_provider, use_responses_api=options.use_responses_api, think_in_prompt=options.think_in_prompt); assign in source target order to subagent_model. Then For spec, assign {'name': name, 'description': subagent.description, 'system_prompt': subagent.prompt, 'model': subagent_model, 'tools': tools}; source annotation SubagentSpec.
    // Source: vvaharness/backends/harness/deepagents/options/subagents.py:185-188
    In source order: Evaluate once _spec_middleware(tool_names, tools, options, budget=_subagent_budget(subagent)); assign in source target order to spec['middleware']. Then Evaluate once _skill_sources(getattr(options, 'skill_root', None), options.cwd); assign in source target order to sources.
    // Source: vvaharness/backends/harness/deepagents/options/subagents.py:189-190
    if (the source predicate sources is truthy) {
      // Source: vvaharness/backends/harness/deepagents/options/subagents.py:190-190
      In source order: Evaluate once sources; assign in source target order to spec['skills'].
    }
    // Source: vvaharness/backends/harness/deepagents/options/subagents.py:191-194
    if (the source predicate subagent.response_model is not None is truthy) {
      // Source: vvaharness/backends/harness/deepagents/options/subagents.py:192-194
      In source order: Evaluate once _strategy_for(subagent.response_model, subagent_model_id, options.model_provider); assign in source target order to spec['response_format'].
    }
    // Source: vvaharness/backends/harness/deepagents/options/subagents.py:195-195
    In source order: Evaluate specs.append(spec); retain side effects and discard the expression result.
  }
  // Source: vvaharness/backends/harness/deepagents/options/subagents.py:196-196
  End this invocation with specs.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.backends.harness.deepagents.exclude_tools import ExcludeTools` at source line 28: `source_detail/vvaharness/backends/harness/deepagents/exclude_tools.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.force_verdict_only import ForceVerdictOnly` at source line 29: `source_detail/vvaharness/backends/harness/deepagents/force_verdict_only.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.model_call_budget import ModelCallBudget` at source line 30: `source_detail/vvaharness/backends/harness/deepagents/model_call_budget.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.models import DELETE_TOOL_NAME, SubagentSpec` at source line 31: `source_detail/vvaharness/backends/harness/deepagents/models.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.options.filesystem import _skill_sources` at source line 32: `source_detail/vvaharness/backends/harness/deepagents/options/filesystem.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.options.graph_builder import _CONNECTION_RETRY_MIDDLEWARE` at source line 33: `source_detail/vvaharness/backends/harness/deepagents/options/graph_builder.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.options.model_building import build_model_cached` at source line 36: `source_detail/vvaharness/backends/harness/deepagents/options/model_building.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.options.response_format import _strategy_for, _tool_name_for` at source line 37: `source_detail/vvaharness/backends/harness/deepagents/options/response_format.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.permit_tools import PermitTools` at source line 41: `source_detail/vvaharness/backends/harness/deepagents/permit_tools.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.prompt_caching import BlockMarkerPromptCaching` at source line 42: `source_detail/vvaharness/backends/harness/deepagents/prompt_caching.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.redaction import read_only_middleware` at source line 43: `source_detail/vvaharness/backends/harness/deepagents/redaction.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.tools import build_tools` at source line 44: `source_detail/vvaharness/backends/harness/deepagents/tools.py.sudo.md`.
- `from vvaharness.backends.harness.models import LEGACY_AGENT_TOOL, LOGICAL_TO_NATIVE, MUTATING_TOOLS, NATIVE_IMPLIED_READS, READ_TOOLS, OneShotOptions, StreamingOptions, SubagentDefinition, ToolPolicy` at source line 45: `source_detail/vvaharness/backends/harness/models.py.sudo.md`.
