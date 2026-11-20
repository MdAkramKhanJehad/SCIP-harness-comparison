# vvaharness/backends/harness/claude/facts.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/backends/harness/claude/facts.py.evidence.json`. SHA-256: `1d34c575aa25deab468ab61841f9b22a6f8e89cf7ab37489f6fbaafc3b8403af`.

```sudo
// Source: vvaharness/backends/harness/claude/facts.py:15-24
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import json; preserve alias and import-time effects. Then Resolve source import from typing import TYPE_CHECKING, Any; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.models import MCP_TOOL_PREFIX; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/claude/facts.py:26-32
if (the source predicate TYPE_CHECKING is truthy) {
  // Source: vvaharness/backends/harness/claude/facts.py:27-32
  In source order: Resolve source import from collections.abc import Sequence; preserve alias and import-time effects. Then Resolve source import from claude_agent_sdk import SdkMcpTool; preserve alias and import-time effects. Then Resolve source import from claude_agent_sdk.types import McpSdkServerConfig; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.models import FactToolSpec; preserve alias and import-time effects.
}
// Source: vvaharness/backends/harness/claude/facts.py:35-39
In source order: Evaluate once 'facts'; assign in source target order to SERVER_NAME. Then Evaluate once source_template_36_14; assign in source target order to TOOL_PREFIX. Then Evaluate once 'SubmitPersonaReport'; assign in source target order to SUBMIT_TOOL.
// Source: vvaharness/backends/harness/claude/facts.py:42-44
// Source signature: mcp_name(bare: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn mcp_name(bare) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/claude/facts.py:43-43
  In source order: Retain source documentation literal source_literal_43_4; it is not a model call.
  // Source: vvaharness/backends/harness/claude/facts.py:44-44
  End this invocation with TOOL_PREFIX + bare.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/claude/facts.py:47-54
// Source signature: rewrite_tool_names(names: Sequence[str] | None, bridged: Sequence[str]) -> list[str] | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn rewrite_tool_names(names, bridged) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/claude/facts.py:49-49
  In source order: Retain source documentation literal source_literal_49_4; it is not a model call.
  // Source: vvaharness/backends/harness/claude/facts.py:51-52
  if (the source predicate names is None is truthy) {
    // Source: vvaharness/backends/harness/claude/facts.py:52-52
    End this invocation with None.
  }
  // Source: vvaharness/backends/harness/claude/facts.py:53-53
  In source order: Evaluate once set(bridged); assign in source target order to bridged_set.
  // Source: vvaharness/backends/harness/claude/facts.py:54-54
  End this invocation with [mcp_name(n) if n in bridged_set else n for n in names].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/claude/facts.py:57-80
interface PersonaReportCollector {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/harness/claude/facts.py:58-58
  In source order: Retain source documentation literal source_literal_58_4; it is not a model call.
  // Source: vvaharness/backends/harness/claude/facts.py:60-62
  // Source signature: __init__(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/claude/facts.py:61-62
    In source order: Retain source documentation literal source_literal_61_8; it is not a model call. Then For self._reports, assign []; source annotation list[dict].
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/claude/facts.py:64-71
  // Source signature: add(self, report: dict) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn add(self, report) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/claude/facts.py:65-71
    In source order: Retain source documentation literal source_literal_65_8; it is not a model call. Then Evaluate once (report.get('persona'), report.get('tracking_id')); assign in source target order to key. Then Evaluate once [r for r in self._reports if (r.get('persona'), r.get('tracking_id')) != key]; assign in source target order to self._reports. Then Evaluate self._reports.append(report); retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/claude/facts.py:74-76
  // Source: vvaharness/backends/harness/claude/facts.py:73-73
  Before creating this callable, evaluate and retain decorators top-to-bottom: property.
  // Source: vvaharness/backends/harness/claude/facts.py:74-76
  // Source signature: reports(self) -> list[dict]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn reports(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/claude/facts.py:75-75
    In source order: Retain source documentation literal source_literal_75_8; it is not a model call.
    // Source: vvaharness/backends/harness/claude/facts.py:76-76
    End this invocation with list(self._reports).
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vvaharness/backends/harness/claude/facts.py:78-80
  // Source signature: __len__(self) -> int
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __len__(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/claude/facts.py:79-79
    In source order: Retain source documentation literal source_literal_79_8; it is not a model call.
    // Source: vvaharness/backends/harness/claude/facts.py:80-80
    End this invocation with len(self._reports).
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vvaharness/backends/harness/claude/facts.py:83-88
// Source signature: _content(text: str, *, is_error: bool=False) -> dict[str, Any]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _content(text, is_error) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/claude/facts.py:84-85
  In source order: Retain source documentation literal source_literal_84_4; it is not a model call. Then For payload, assign {'content': [{'type': 'text', 'text': text}]}; source annotation dict[str, Any].
  // Source: vvaharness/backends/harness/claude/facts.py:86-87
  if (the source predicate is_error is truthy) {
    // Source: vvaharness/backends/harness/claude/facts.py:87-87
    In source order: Evaluate once True; assign in source target order to payload['is_error'].
  }
  // Source: vvaharness/backends/harness/claude/facts.py:88-88
  End this invocation with payload.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/claude/facts.py:91-98
// Source signature: _serialize(result: object) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _serialize(result) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/claude/facts.py:92-92
  In source order: Retain source documentation literal source_literal_92_4; it is not a model call.
  // Source: vvaharness/backends/harness/claude/facts.py:93-94
  if (the source predicate isinstance(result, str) is truthy) {
    // Source: vvaharness/backends/harness/claude/facts.py:94-94
    End this invocation with result.
  }
  // Source: vvaharness/backends/harness/claude/facts.py:95-98
  Perform the following protected operations {
    // Source: vvaharness/backends/harness/claude/facts.py:96-96
    End this invocation with json.dumps(result, default=str).
  }
  // Source: vvaharness/backends/harness/claude/facts.py:97-98
  On the first matching source exception (TypeError, ValueError), in handler order {
    // Source: vvaharness/backends/harness/claude/facts.py:98-98
    End this invocation with str(result).
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/claude/facts.py:101-114
// Source signature: _fact_tool(spec: FactToolSpec, sdk_tool: Any) -> SdkMcpTool[Any]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _fact_tool(spec, sdk_tool) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/claude/facts.py:102-102
  In source order: Retain source documentation literal source_literal_102_4; it is not a model call.
  // Source: vvaharness/backends/harness/claude/facts.py:104-112
  // Source: vvaharness/backends/harness/claude/facts.py:103-103
  Before creating this callable, evaluate and retain decorators top-to-bottom: sdk_tool(spec.name, spec.description, dict(spec.input_schema)).
  // Source: vvaharness/backends/harness/claude/facts.py:104-112
  // Source signature: _handler(args: dict[str, Any]) -> dict[str, Any]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _handler(args) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    This callable produces a coroutine or async generator; await/suspension positions remain in source expressions.
    // Source: vvaharness/backends/harness/claude/facts.py:105-111
    Perform the following protected operations {
      // Source: vvaharness/backends/harness/claude/facts.py:107-109
      In source order: Resolve source import import asyncio; preserve alias and import-time effects. Then Evaluate once await asyncio.to_thread(spec.fn, **dict(args)); assign in source target order to result.
    }
    // Source: vvaharness/backends/harness/claude/facts.py:110-111
    On the first matching source exception Exception as exc, in handler order {
      // Source: vvaharness/backends/harness/claude/facts.py:111-111
      End this invocation with _content(source_template_111_28, is_error=True).
    }
    // Source: vvaharness/backends/harness/claude/facts.py:112-112
    End this invocation with _content(_serialize(result)).
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vvaharness/backends/harness/claude/facts.py:114-114
  End this invocation with _handler.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/claude/facts.py:117-143
// Source signature: _submit_tool(report_model: type, collector: PersonaReportCollector, sdk_tool: Any) -> SdkMcpTool[Any]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _submit_tool(report_model, collector, sdk_tool) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/claude/facts.py:119-123
  In source order: Retain source documentation literal source_literal_119_4; it is not a model call. Then Resolve source import from vvaharness.backends.harness.claude.options import _sanitize_schema; preserve alias and import-time effects.
  // Source: vvaharness/backends/harness/claude/facts.py:131-141
  // Source: vvaharness/backends/harness/claude/facts.py:125-130
  Before creating this callable, evaluate and retain decorators top-to-bottom: sdk_tool(SUBMIT_TOOL, source_template_126_14, _sanitize_schema(report_model.model_json_schema())).
  // Source: vvaharness/backends/harness/claude/facts.py:131-141
  // Source signature: _submit(args: dict[str, Any]) -> dict[str, Any]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _submit(args) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    This callable produces a coroutine or async generator; await/suspension positions remain in source expressions.
    // Source: vvaharness/backends/harness/claude/facts.py:132-139
    Perform the following protected operations {
      // Source: vvaharness/backends/harness/claude/facts.py:133-133
      In source order: Evaluate once report_model.model_validate(dict(args)); assign in source target order to report.
    }
    // Source: vvaharness/backends/harness/claude/facts.py:134-139
    On the first matching source exception Exception as exc, in handler order {
      // Source: vvaharness/backends/harness/claude/facts.py:136-139
      End this invocation with _content(source_template_137_16, is_error=True).
    }
    // Source: vvaharness/backends/harness/claude/facts.py:140-140
    In source order: Evaluate collector.add(report.model_dump(mode='json')); retain side effects and discard the expression result.
    // Source: vvaharness/backends/harness/claude/facts.py:141-141
    End this invocation with _content('Report accepted.').
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vvaharness/backends/harness/claude/facts.py:143-143
  End this invocation with _submit.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/claude/facts.py:146-162
// Source signature: build_fact_tools(specs: Sequence[FactToolSpec], *, report_model: type | None=None) -> tuple[list[SdkMcpTool[Any]], list[str], PersonaReportCollector]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn build_fact_tools(specs, report_model) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/claude/facts.py:149-156
  In source order: Retain source documentation literal source_literal_149_4; it is not a model call. Then Resolve source import from claude_agent_sdk import tool as sdk_tool; preserve alias and import-time effects. Then Evaluate once PersonaReportCollector(); assign in source target order to collector. Then Evaluate once [_fact_tool(spec, sdk_tool) for spec in specs]; assign in source target order to tools. Then Evaluate once [mcp_name(spec.name) for spec in specs]; assign in source target order to names.
  // Source: vvaharness/backends/harness/claude/facts.py:158-160
  if (the source predicate report_model is not None is truthy) {
    // Source: vvaharness/backends/harness/claude/facts.py:159-160
    In source order: Evaluate tools.append(_submit_tool(report_model, collector, sdk_tool)); retain side effects and discard the expression result. Then Evaluate names.append(mcp_name(SUBMIT_TOOL)); retain side effects and discard the expression result.
  }
  // Source: vvaharness/backends/harness/claude/facts.py:162-162
  End this invocation with (tools, names, collector).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/claude/facts.py:165-174
// Source signature: build_fact_mcp(specs: Sequence[FactToolSpec], *, report_model: type | None=None) -> tuple[McpSdkServerConfig, list[str], PersonaReportCollector]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn build_fact_mcp(specs, report_model) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/claude/facts.py:168-173
  In source order: Retain source documentation literal source_literal_168_4; it is not a model call. Then Resolve source import from claude_agent_sdk import create_sdk_mcp_server; preserve alias and import-time effects. Then Evaluate once build_fact_tools(specs, report_model=report_model); assign in source target order to (tools, names, collector).
  // Source: vvaharness/backends/harness/claude/facts.py:174-174
  End this invocation with (create_sdk_mcp_server(SERVER_NAME, tools=tools), names, collector).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/claude/facts.py:178-199
In source order: Evaluate once source_template_179_4; assign in source target order to SUBMIT_PROMPT_SUFFIX. Then Evaluate once ['SERVER_NAME', 'SUBMIT_PROMPT_SUFFIX', 'SUBMIT_TOOL', 'TOOL_PREFIX', 'PersonaReportCollector', 'build_fact_mcp', 'build_fact_tools', 'mcp_name', 'rewrite_tool_names']; assign in source target order to __all__.
```

## Local import links

- `from vvaharness.backends.harness.models import MCP_TOOL_PREFIX` at source line 24: `source_detail/vvaharness/backends/harness/models.py.sudo.md`.
- `from vvaharness.backends.harness.models import FactToolSpec` at source line 32: `source_detail/vvaharness/backends/harness/models.py.sudo.md`.
- `from vvaharness.backends.harness.claude.options import _sanitize_schema` at source line 121: `source_detail/vvaharness/backends/harness/claude/options.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../../prompt_representation/vvaharness/backends/harness/claude/facts.py.sudo.md). Exact strings in the evidence asset support this conversion.
