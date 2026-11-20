# vvaharness/backends/harness/deepagents/tools.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/backends/harness/deepagents/tools.py.evidence.json`. SHA-256: `621f51ebb5a101746541c0645db2f47779f551566ee6ad496aea960e5f3edbee`.

```sudo
// Source: vvaharness/backends/harness/deepagents/tools.py:15-32
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from typing import TYPE_CHECKING, Final; preserve alias and import-time effects. Then Resolve source import from langchain_core.tools import BaseTool; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.models import LOGICAL_TO_NATIVE, MCP_TOOL_PREFIX, MUTATING_TOOLS, ORCHESTRATION_TOOLS, StreamingOptions, ToolPolicy; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/deepagents/tools.py:33-33
In source order: Resolve source import from vvaharness.util.warn_once import warn_once; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/deepagents/tools.py:35-36
if (the source predicate TYPE_CHECKING is truthy) {
  // Source: vvaharness/backends/harness/deepagents/tools.py:36-36
  In source order: Resolve source import from collections.abc import Sequence; preserve alias and import-time effects.
}
// Source: vvaharness/backends/harness/deepagents/tools.py:39-42
In source order: For _UNMAPPED_BY_DESIGN, assign ORCHESTRATION_TOOLS | MUTATING_TOOLS; source annotation Final[frozenset[str]]. Then For _WARNED_UNKNOWN_TOOLS, assign set(); source annotation set[str].
// Source: vvaharness/backends/harness/deepagents/tools.py:45-57
// Source signature: _warn_unknown_tools(options: StreamingOptions, allowed: set[str]) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _warn_unknown_tools(options, allowed) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/tools.py:46-48
  In source order: Retain source documentation literal source_literal_46_4; it is not a model call. Then Evaluate once LOGICAL_TO_NATIVE.keys() | _UNMAPPED_BY_DESIGN | set(options.fact_tools); assign in source target order to known.
  // Source: vvaharness/backends/harness/deepagents/tools.py:49-57
  for each name in sorted(allowed - known) {
    // Source: vvaharness/backends/harness/deepagents/tools.py:50-51
    if (the source predicate name.startswith(MCP_TOOL_PREFIX) is truthy) {
      // Source: vvaharness/backends/harness/deepagents/tools.py:51-51
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/backends/harness/deepagents/tools.py:52-57
    In source order: Evaluate warn_once(_WARNED_UNKNOWN_TOOLS, name, source_template_55_12); retain side effects and discard the expression result.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/tools.py:60-65
// Source signature: _allowed_tool_names(options: StreamingOptions, allowed_tools: Sequence[str] | None) -> set[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _allowed_tool_names(options, allowed_tools) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/tools.py:63-64
  In source order: Retain source documentation literal source_literal_63_4; it is not a model call. Then Evaluate once options.tool_policy if options.tool_policy is not None else ToolPolicy(); assign in source target order to policy.
  // Source: vvaharness/backends/harness/deepagents/tools.py:65-65
  End this invocation with set(allowed_tools if allowed_tools is not None else policy.allowed_tools).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/tools.py:68-76
// Source signature: native_tool_names(options: StreamingOptions, allowed_tools: Sequence[str] | None) -> tuple[str, ...]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn native_tool_names(options, allowed_tools) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/tools.py:71-73
  In source order: Retain source documentation literal source_literal_71_4; it is not a model call. Then Evaluate once _allowed_tool_names(options, allowed_tools); assign in source target order to allowed. Then Evaluate _warn_unknown_tools(options, allowed); retain side effects and discard the expression result.
  // Source: vvaharness/backends/harness/deepagents/tools.py:74-76
  End this invocation with tuple((native for logical, native in LOGICAL_TO_NATIVE.items() if logical in allowed)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/tools.py:79-98
// Source signature: session_tool_names(tools: Sequence[BaseTool]) -> frozenset[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn session_tool_names(tools) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/tools.py:80-91
  In source order: Retain source documentation literal source_literal_80_4; it is not a model call. Then Resolve source import from vvaharness.backends.harness.deepagents.models import ALL_NATIVE_TOOLS; preserve alias and import-time effects. Then Evaluate once frozenset((name for name in (getattr(tool, 'name', None) for tool in tools) if isinstance(name, str))); assign in source target order to names. Then Evaluate once names & ALL_NATIVE_TOOLS; assign in source target order to reserved.
  // Source: vvaharness/backends/harness/deepagents/tools.py:92-97
  if (the source predicate reserved is truthy) {
    // Source: vvaharness/backends/harness/deepagents/tools.py:93-97
    Raise ValueError(source_template_94_12).
  }
  // Source: vvaharness/backends/harness/deepagents/tools.py:98-98
  End this invocation with names.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/tools.py:101-109
// Source signature: build_tools(options: StreamingOptions, *, allowed_tools: Sequence[str] | None) -> list[BaseTool]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn build_tools(options, allowed_tools) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/tools.py:106-108
  In source order: Retain source documentation literal source_literal_106_4; it is not a model call. Then Evaluate _warn_unknown_tools(options, _allowed_tool_names(options, allowed_tools)); retain side effects and discard the expression result.
  // Source: vvaharness/backends/harness/deepagents/tools.py:109-109
  End this invocation with [].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/tools.py:112-112
In source order: Evaluate once ['build_tools', 'native_tool_names', 'session_tool_names']; assign in source target order to __all__.
```

## Local import links

- `from vvaharness.backends.harness.models import LOGICAL_TO_NATIVE, MCP_TOOL_PREFIX, MUTATING_TOOLS, ORCHESTRATION_TOOLS, StreamingOptions, ToolPolicy` at source line 25: `source_detail/vvaharness/backends/harness/models.py.sudo.md`.
- `from vvaharness.util.warn_once import warn_once` at source line 33: `source_detail/vvaharness/util/warn_once.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.models import ALL_NATIVE_TOOLS` at source line 82: `source_detail/vvaharness/backends/harness/deepagents/models.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../../prompt_representation/vvaharness/backends/harness/deepagents/tools.py.sudo.md). Exact strings in the evidence asset support this conversion.
