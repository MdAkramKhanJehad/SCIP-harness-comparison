# vvaharness/backends/harness/deepagents/options/oneshot.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/backends/harness/deepagents/options/oneshot.py.evidence.json`. SHA-256: `2613b7fba5d49989c710064a10e64fab5423405677fe7df00356a1c4a562401c`.

```sudo
// Source: vvaharness/backends/harness/deepagents/options/oneshot.py:15-27
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from typing import TYPE_CHECKING, cast; preserve alias and import-time effects. Then Resolve source import from langgraph.graph.state import CompiledStateGraph; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.deepagents.models import ALL_NATIVE_TOOLS, SUBAGENT_DISPATCH_TOOL, CompiledGraph; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/deepagents/options/oneshot.py:28-42
In source order: Resolve source import from vvaharness.backends.harness.deepagents.options.filesystem import _filesystem_permissions, _session_backend, _skill_sources; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.deepagents.options.graph_builder import _create_agent; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.deepagents.options.graph_config import _make_config; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.deepagents.options.response_format import _oneshot_response_format; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.deepagents.options.subagents import _build_session_tools, _tool_policy, get_subagent_specs; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/deepagents/options/oneshot.py:43-48
In source order: Resolve source import from vvaharness.backends.harness.deepagents.tools import session_tool_names; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.models import LOGICAL_TO_NATIVE, OneShotOptions, StreamingOptions; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/deepagents/options/oneshot.py:50-51
if (the source predicate TYPE_CHECKING is truthy) {
  // Source: vvaharness/backends/harness/deepagents/options/oneshot.py:51-51
  In source order: Resolve source import from langchain_core.tools import BaseTool; preserve alias and import-time effects.
}
// Source: vvaharness/backends/harness/deepagents/options/oneshot.py:54-62
// Source signature: _granted_natives(options: OneShotOptions) -> frozenset[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _granted_natives(options) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/options/oneshot.py:55-55
  In source order: Retain source documentation literal source_literal_55_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/options/oneshot.py:56-57
  if (the source predicate options.tool_policy is None is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/oneshot.py:57-57
    End this invocation with frozenset().
  }
  // Source: vvaharness/backends/harness/deepagents/options/oneshot.py:58-62
  End this invocation with frozenset((LOGICAL_TO_NATIVE[logical] for logical in options.tool_policy.allowed_tools if logical in LOGICAL_TO_NATIVE)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/options/oneshot.py:65-71
// Source signature: _oneshot_excluded_tools(options: OneShotOptions) -> frozenset[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _oneshot_excluded_tools(options) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/options/oneshot.py:66-68
  In source order: Retain source documentation literal source_literal_66_4; it is not a model call. Then Evaluate once frozenset({SUBAGENT_DISPATCH_TOOL}); assign in source target order to task.
  // Source: vvaharness/backends/harness/deepagents/options/oneshot.py:69-70
  if (the source predicate options.tool_policy is None is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/oneshot.py:70-70
    End this invocation with task.
  }
  // Source: vvaharness/backends/harness/deepagents/options/oneshot.py:71-71
  End this invocation with ALL_NATIVE_TOOLS - _granted_natives(options) | task.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/options/oneshot.py:74-82
// Source signature: _oneshot_permitted_tools(options: OneShotOptions, session_tools: list[BaseTool]) -> frozenset[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _oneshot_permitted_tools(options, session_tools) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/options/oneshot.py:77-79
  In source order: Retain source documentation literal source_literal_77_4; it is not a model call. Then Evaluate once session_tool_names(session_tools); assign in source target order to custom.
  // Source: vvaharness/backends/harness/deepagents/options/oneshot.py:80-81
  if (the source predicate options.tool_policy is None is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/oneshot.py:81-81
    End this invocation with ALL_NATIVE_TOOLS | custom.
  }
  // Source: vvaharness/backends/harness/deepagents/options/oneshot.py:82-82
  End this invocation with _granted_natives(options) | custom.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/options/oneshot.py:85-122
// Source signature: _build_oneshot_graph(options: OneShotOptions) -> CompiledStateGraph
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _build_oneshot_graph(options) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/options/oneshot.py:86-91
  In source order: Retain source documentation literal source_literal_86_4; it is not a model call. Then Evaluate once cast(StreamingOptions, options); assign in source target order to streaming_view. Then Evaluate once _tool_policy(options); assign in source target order to policy. Then Evaluate once _build_session_tools(streaming_view, tuple(policy.allowed_tools)); assign in source target order to tools. Then Evaluate once get_subagent_specs(streaming_view, agents={}); assign in source target order to subagents.
  // Source: vvaharness/backends/harness/deepagents/options/oneshot.py:92-122
  End this invocation with _create_agent(model_id=options.model, env=options.env, think_in_prompt=options.think_in_prompt, system_prompt=options.system_prompt, tools=tools, name=source_template_98_13, skills=_skill_sources(options.skill_root, options.cwd) or None, permissions=_filesystem_permissions(options), model_provider=options.model_provider, redact_reads=not options.allow_writes, backend=_session_backend(options), response_model=options.response_model, response_format=_oneshot_response_format(options), subagents=subagents, extra_excluded_tools=_oneshot_excluded_tools(options), max_output_tokens=options.max_output_tokens, output_cap=options.output_cap, permitted_tool_calls=_oneshot_permitted_tools(options, tools), cache_markers=options.cache_markers, cache_tail=False, strip_harness_suffix=True, effort=options.effort, use_responses_api=options.use_responses_api, parent_middleware=options.parent_middleware).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/options/oneshot.py:125-128
// Source signature: build_oneshot_options(options: OneShotOptions) -> CompiledGraph
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn build_oneshot_options(options) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/options/oneshot.py:126-127
  In source order: Retain source documentation literal source_literal_126_4; it is not a model call. Then Evaluate once _build_oneshot_graph(options); assign in source target order to graph.
  // Source: vvaharness/backends/harness/deepagents/options/oneshot.py:128-128
  End this invocation with CompiledGraph(graph=graph, config=_make_config(options, buffer=5)).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.backends.harness.deepagents.models import ALL_NATIVE_TOOLS, SUBAGENT_DISPATCH_TOOL, CompiledGraph` at source line 23: `source_detail/vvaharness/backends/harness/deepagents/models.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.options.filesystem import _filesystem_permissions, _session_backend, _skill_sources` at source line 28: `source_detail/vvaharness/backends/harness/deepagents/options/filesystem.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.options.graph_builder import _create_agent` at source line 33: `source_detail/vvaharness/backends/harness/deepagents/options/graph_builder.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.options.graph_config import _make_config` at source line 34: `source_detail/vvaharness/backends/harness/deepagents/options/graph_config.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.options.response_format import _oneshot_response_format` at source line 35: `source_detail/vvaharness/backends/harness/deepagents/options/response_format.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.options.subagents import _build_session_tools, _tool_policy, get_subagent_specs` at source line 38: `source_detail/vvaharness/backends/harness/deepagents/options/subagents.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.tools import session_tool_names` at source line 43: `source_detail/vvaharness/backends/harness/deepagents/tools.py.sudo.md`.
- `from vvaharness.backends.harness.models import LOGICAL_TO_NATIVE, OneShotOptions, StreamingOptions` at source line 44: `source_detail/vvaharness/backends/harness/models.py.sudo.md`.
