# vvaharness/backends/harness/deepagents/options/streaming.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/backends/harness/deepagents/options/streaming.py.evidence.json`. SHA-256: `2285a52dd5871f083c49dce08b0d05cba4468627e0e20a5d72b3d70ea6cb1a69`.

```sudo
// Source: vvaharness/backends/harness/deepagents/options/streaming.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import os; preserve alias and import-time effects. Then Resolve source import import threading; preserve alias and import-time effects. Then Resolve source import from typing import TYPE_CHECKING; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/deepagents/options/streaming.py:23-37
In source order: Resolve source import from langgraph.graph.state import CompiledStateGraph; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.deepagents.force_verdict_only import ForceVerdictOnly; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.deepagents.limits import RECURSION_HEADROOM; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.deepagents.models import ALL_NATIVE_TOOLS, SUBAGENT_DISPATCH_TOOL, CompiledGraph, SubagentSpec; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.deepagents.options.filesystem import _filesystem_permissions, _session_backend, _skill_sources; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/deepagents/options/streaming.py:38-46
In source order: Resolve source import from vvaharness.backends.harness.deepagents.options.graph_builder import _create_agent; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.deepagents.options.response_format import _response_format; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.deepagents.options.subagents import _build_session_tools, _tool_policy, get_subagent_specs; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.deepagents.tools import session_tool_names; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.models import READ_TOOLS, StreamingOptions; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/deepagents/options/streaming.py:48-49
if (the source predicate TYPE_CHECKING is truthy) {
  // Source: vvaharness/backends/harness/deepagents/options/streaming.py:49-49
  In source order: Resolve source import from langchain_core.tools import BaseTool; preserve alias and import-time effects.
}
// Source: vvaharness/backends/harness/deepagents/options/streaming.py:52-54
// Source signature: build_subagents(options: StreamingOptions) -> list[SubagentSpec]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn build_subagents(options) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/options/streaming.py:53-53
  In source order: Retain source documentation literal source_literal_53_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/options/streaming.py:54-54
  End this invocation with get_subagent_specs(options).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/options/streaming.py:57-62
// Source signature: _middleware_tool_names(options: StreamingOptions) -> frozenset[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _middleware_tool_names(options) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/options/streaming.py:58-59
  In source order: Retain source documentation literal source_literal_58_4; it is not a model call. Then For names, assign set(); source annotation set[str].
  // Source: vvaharness/backends/harness/deepagents/options/streaming.py:60-61
  for each mw in options.parent_middleware {
    // Source: vvaharness/backends/harness/deepagents/options/streaming.py:61-61
    In source order: Evaluate names.update((t.name for t in getattr(mw, 'tools', ()) or ())); retain side effects and discard the expression result.
  }
  // Source: vvaharness/backends/harness/deepagents/options/streaming.py:62-62
  End this invocation with frozenset(names).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/options/streaming.py:65-75
// Source signature: _permitted_tool_calls(options: StreamingOptions, session_tools: list[BaseTool]) -> frozenset[str] | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _permitted_tool_calls(options, session_tools) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/options/streaming.py:68-68
  In source order: Retain source documentation literal source_literal_68_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/options/streaming.py:69-70
  if (the source predicate options.permitted_tool_calls is None is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/streaming.py:70-70
    End this invocation with None.
  }
  // Source: vvaharness/backends/harness/deepagents/options/streaming.py:71-72
  In source order: Evaluate once options.permitted_tool_calls | session_tool_names(session_tools) | _middleware_tool_names(options); assign in source target order to permitted.
  // Source: vvaharness/backends/harness/deepagents/options/streaming.py:73-74
  if (the source predicate options.agents is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/streaming.py:74-74
    In source order: Apply source augmented assignment permitted |= frozenset({SUBAGENT_DISPATCH_TOOL}) with source evaluation/in-place semantics.
  }
  // Source: vvaharness/backends/harness/deepagents/options/streaming.py:75-75
  End this invocation with permitted.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/options/streaming.py:78-86
// Source signature: _extra_excluded_tools(options: StreamingOptions) -> frozenset[str] | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _extra_excluded_tools(options) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/options/streaming.py:79-79
  In source order: Retain source documentation literal source_literal_79_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/options/streaming.py:81-82
  if (the source predicate options.permitted_tool_calls is None is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/streaming.py:82-82
    End this invocation with None.
  }
  // Source: vvaharness/backends/harness/deepagents/options/streaming.py:83-83
  In source order: Evaluate once ALL_NATIVE_TOOLS - options.permitted_tool_calls; assign in source target order to excluded.
  // Source: vvaharness/backends/harness/deepagents/options/streaming.py:84-85
  if (the source predicate options.agents is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/streaming.py:85-85
    End this invocation with excluded.
  }
  // Source: vvaharness/backends/harness/deepagents/options/streaming.py:86-86
  End this invocation with excluded | frozenset({SUBAGENT_DISPATCH_TOOL}).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/options/streaming.py:89-125
// Source signature: _build_streaming_graph(options: StreamingOptions) -> CompiledStateGraph
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _build_streaming_graph(options) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/options/streaming.py:90-94
  In source order: Retain source documentation literal source_literal_90_4; it is not a model call. Then Evaluate once build_subagents(options); assign in source target order to subagent_specs. Then Evaluate once tuple((t for t in _tool_policy(options).allowed_tools if t in READ_TOOLS)); assign in source target order to parent_tools. Then Evaluate once _build_session_tools(options, parent_tools); assign in source target order to tools.
  // Source: vvaharness/backends/harness/deepagents/options/streaming.py:95-125
  End this invocation with _create_agent(model_id=options.model, env=options.env, think_in_prompt=options.think_in_prompt, system_prompt=options.system_prompt, tools=tools, name=options.graph_name, skills=_skill_sources(options.skill_root, options.cwd), permissions=_filesystem_permissions(options), model_provider=options.model_provider, redact_reads=bool(subagent_specs) or not options.allow_writes, backend=_session_backend(options), response_model=options.response_model, response_format=_response_format(options.response_model, options.model, options.model_provider), subagents=subagent_specs, extra_excluded_tools=_extra_excluded_tools(options), permitted_tool_calls=_permitted_tool_calls(options, tools), max_output_tokens=options.max_output_tokens, output_cap=options.output_cap, cache_markers=options.cache_markers, cache_tail=True, parent_middleware=(*options.parent_middleware, *((ForceVerdictOnly(),) if options.force_verdict_only else ())), effort=options.effort, use_responses_api=options.use_responses_api).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/options/streaming.py:129-130
In source order: For _SESSIONS, assign {}; source annotation dict[str, CompiledGraph]. Then Evaluate once threading.Lock(); assign in source target order to _SESSIONS_LOCK.
// Source: vvaharness/backends/harness/deepagents/options/streaming.py:133-149
// Source signature: build_streaming_agent(options: StreamingOptions) -> CompiledGraph
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn build_streaming_agent(options) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/options/streaming.py:134-143
  In source order: Retain source documentation literal source_literal_134_4; it is not a model call. Then Evaluate once _build_streaming_graph(options); assign in source target order to graph. Then Evaluate once CompiledGraph(graph=graph, config={'configurable': {'thread_id': options.session_id or os.urandom(8).hex()}, 'recursion_limit': (options.max_turns or 50) + RECURSION_HEADROOM}); assign in source target order to compiled.
  // Source: vvaharness/backends/harness/deepagents/options/streaming.py:144-148
  if (the source predicate options.session_id is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/streaming.py:147-148
    Enter source context managers left-to-right: _SESSIONS_LOCK {
      // Source: vvaharness/backends/harness/deepagents/options/streaming.py:148-148
      In source order: Evaluate once compiled; assign in source target order to _SESSIONS[options.session_id].
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
  }
  // Source: vvaharness/backends/harness/deepagents/options/streaming.py:149-149
  End this invocation with compiled.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/options/streaming.py:152-155
// Source signature: resumable(session_id: str) -> CompiledGraph | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn resumable(session_id) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/options/streaming.py:153-153
  In source order: Retain source documentation literal source_literal_153_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/options/streaming.py:154-155
  Enter source context managers left-to-right: _SESSIONS_LOCK {
    // Source: vvaharness/backends/harness/deepagents/options/streaming.py:155-155
    End this invocation with _SESSIONS.get(session_id).
  }
  Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/options/streaming.py:158-161
// Source signature: release_session(session_id: str) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn release_session(session_id) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/options/streaming.py:159-159
  In source order: Retain source documentation literal source_literal_159_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/options/streaming.py:160-161
  Enter source context managers left-to-right: _SESSIONS_LOCK {
    // Source: vvaharness/backends/harness/deepagents/options/streaming.py:161-161
    In source order: Evaluate _SESSIONS.pop(session_id, None); retain side effects and discard the expression result.
  }
  Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.backends.harness.deepagents.force_verdict_only import ForceVerdictOnly` at source line 25: `source_detail/vvaharness/backends/harness/deepagents/force_verdict_only.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.limits import RECURSION_HEADROOM` at source line 26: `source_detail/vvaharness/backends/harness/deepagents/limits.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.models import ALL_NATIVE_TOOLS, SUBAGENT_DISPATCH_TOOL, CompiledGraph, SubagentSpec` at source line 27: `source_detail/vvaharness/backends/harness/deepagents/models.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.options.filesystem import _filesystem_permissions, _session_backend, _skill_sources` at source line 33: `source_detail/vvaharness/backends/harness/deepagents/options/filesystem.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.options.graph_builder import _create_agent` at source line 38: `source_detail/vvaharness/backends/harness/deepagents/options/graph_builder.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.options.response_format import _response_format` at source line 39: `source_detail/vvaharness/backends/harness/deepagents/options/response_format.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.options.subagents import _build_session_tools, _tool_policy, get_subagent_specs` at source line 40: `source_detail/vvaharness/backends/harness/deepagents/options/subagents.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.tools import session_tool_names` at source line 45: `source_detail/vvaharness/backends/harness/deepagents/tools.py.sudo.md`.
- `from vvaharness.backends.harness.models import READ_TOOLS, StreamingOptions` at source line 46: `source_detail/vvaharness/backends/harness/models.py.sudo.md`.
