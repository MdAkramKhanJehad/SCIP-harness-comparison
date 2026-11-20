# vvaharness/plugins/semgrep/tools.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/plugins/semgrep/tools.py.evidence.json`. SHA-256: `234866aeb54ee96bd04f448c3226edd80c0389ce085a49c17c7fe6264c0b1b9b`.

```sudo
// Source: vvaharness/plugins/semgrep/tools.py:15-22
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from langchain_core.tools import BaseTool, tool; preserve alias and import-time effects. Then Resolve source import from vvaharness.codegraph.tools import GraphToolContext; preserve alias and import-time effects. Then Evaluate once 25; assign in source target order to _MAX_ROWS.
// Source: vvaharness/plugins/semgrep/tools.py:23-58
In source order: Evaluate once 40; assign in source target order to _MAX_TRACE_STEPS. Then Evaluate once source_literal_25_21; assign in source target order to _FINDINGS_FOR_FILE. Then Evaluate once source_literal_35_18; assign in source target order to _TRACE_FOR_RULE. Then Evaluate once source_literal_44_28; assign in source target order to _CALLERS_OF_FLAGGED_SINKS. Then Evaluate once source_literal_53_17; assign in source target order to _SCAN_COVERAGE.
// Source: vvaharness/plugins/semgrep/tools.py:61-67
// Source signature: _rows(gtx: GraphToolContext, query: str, params: dict) -> list[dict]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _rows(gtx, query, params) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/plugins/semgrep/tools.py:62-62
  In source order: Retain source documentation literal source_literal_62_4; it is not a model call.
  // Source: vvaharness/plugins/semgrep/tools.py:63-67
  Perform the following protected operations {
    // Source: vvaharness/plugins/semgrep/tools.py:64-64
    End this invocation with [r.to_dict() for r in gtx.handle.graph.cypher(query, params).rows].
  }
  // Source: vvaharness/plugins/semgrep/tools.py:65-67
  On the first matching source exception Exception as exc, in handler order {
    // Source: vvaharness/plugins/semgrep/tools.py:66-67
    End this invocation with [{'error': source_template_66_26, 'hint': 'no Semgrep subgraph in this scan; the enricher did not run'}].
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/plugins/semgrep/tools.py:70-78
// Source signature: semgrep_findings_tool(gtx: GraphToolContext) -> BaseTool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn semgrep_findings_tool(gtx) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/plugins/semgrep/tools.py:71-71
  In source order: Retain source documentation literal source_literal_71_4; it is not a model call.
  // Source: vvaharness/plugins/semgrep/tools.py:74-76
  // Source: vvaharness/plugins/semgrep/tools.py:73-73
  Before creating this callable, evaluate and retain decorators top-to-bottom: tool.
  // Source: vvaharness/plugins/semgrep/tools.py:74-76
  // Source signature: GraphSemgrepFindings(file: str) -> list[dict]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn GraphSemgrepFindings(file) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/plugins/semgrep/tools.py:75-75
    In source order: Retain source documentation literal source_literal_75_8; it is not a model call.
    // Source: vvaharness/plugins/semgrep/tools.py:76-76
    End this invocation with _rows(gtx, _FINDINGS_FOR_FILE, {'file': file}).
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vvaharness/plugins/semgrep/tools.py:78-78
  End this invocation with GraphSemgrepFindings.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/plugins/semgrep/tools.py:81-89
// Source signature: semgrep_trace_tool(gtx: GraphToolContext) -> BaseTool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn semgrep_trace_tool(gtx) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/plugins/semgrep/tools.py:82-82
  In source order: Retain source documentation literal source_literal_82_4; it is not a model call.
  // Source: vvaharness/plugins/semgrep/tools.py:85-87
  // Source: vvaharness/plugins/semgrep/tools.py:84-84
  Before creating this callable, evaluate and retain decorators top-to-bottom: tool.
  // Source: vvaharness/plugins/semgrep/tools.py:85-87
  // Source signature: GraphSemgrepTaintTrace(rule_id: str) -> list[dict]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn GraphSemgrepTaintTrace(rule_id) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/plugins/semgrep/tools.py:86-86
    In source order: Retain source documentation literal source_literal_86_8; it is not a model call.
    // Source: vvaharness/plugins/semgrep/tools.py:87-87
    End this invocation with _rows(gtx, _TRACE_FOR_RULE, {'rule_id': rule_id}).
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vvaharness/plugins/semgrep/tools.py:89-89
  End this invocation with GraphSemgrepTaintTrace.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/plugins/semgrep/tools.py:92-100
// Source signature: semgrep_sink_callers_tool(gtx: GraphToolContext) -> BaseTool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn semgrep_sink_callers_tool(gtx) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/plugins/semgrep/tools.py:93-93
  In source order: Retain source documentation literal source_literal_93_4; it is not a model call.
  // Source: vvaharness/plugins/semgrep/tools.py:96-98
  // Source: vvaharness/plugins/semgrep/tools.py:95-95
  Before creating this callable, evaluate and retain decorators top-to-bottom: tool.
  // Source: vvaharness/plugins/semgrep/tools.py:96-98
  // Source signature: GraphSemgrepSinkCallers(file: str) -> list[dict]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn GraphSemgrepSinkCallers(file) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/plugins/semgrep/tools.py:97-97
    In source order: Retain source documentation literal source_literal_97_8; it is not a model call.
    // Source: vvaharness/plugins/semgrep/tools.py:98-98
    End this invocation with _rows(gtx, _CALLERS_OF_FLAGGED_SINKS, {'file': file}).
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vvaharness/plugins/semgrep/tools.py:100-100
  End this invocation with GraphSemgrepSinkCallers.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/plugins/semgrep/tools.py:103-111
// Source signature: semgrep_coverage_tool(gtx: GraphToolContext) -> BaseTool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn semgrep_coverage_tool(gtx) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/plugins/semgrep/tools.py:104-104
  In source order: Retain source documentation literal source_literal_104_4; it is not a model call.
  // Source: vvaharness/plugins/semgrep/tools.py:107-109
  // Source: vvaharness/plugins/semgrep/tools.py:106-106
  Before creating this callable, evaluate and retain decorators top-to-bottom: tool.
  // Source: vvaharness/plugins/semgrep/tools.py:107-109
  // Source signature: GraphSemgrepCoverage() -> list[dict]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn GraphSemgrepCoverage() {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/plugins/semgrep/tools.py:108-108
    In source order: Retain source documentation literal source_literal_108_8; it is not a model call.
    // Source: vvaharness/plugins/semgrep/tools.py:109-109
    End this invocation with _rows(gtx, _SCAN_COVERAGE, {}).
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vvaharness/plugins/semgrep/tools.py:111-111
  End this invocation with GraphSemgrepCoverage.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/plugins/semgrep/tools.py:114-123
In source order: Evaluate once {'GraphSemgrepFindings': semgrep_findings_tool, 'GraphSemgrepTaintTrace': semgrep_trace_tool, 'GraphSemgrepSinkCallers': semgrep_sink_callers_tool, 'GraphSemgrepCoverage': semgrep_coverage_tool}; assign in source target order to SEMGREP_TOOLS. Then For SEMGREP_TOOL_NAMES, assign tuple(SEMGREP_TOOLS); source annotation tuple[str, ...]. Then Evaluate once ['SEMGREP_TOOLS', 'SEMGREP_TOOL_NAMES']; assign in source target order to __all__.
```

## Local import links

- `from vvaharness.codegraph.tools import GraphToolContext` at source line 20: `source_detail/vvaharness/codegraph/tools.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../prompt_representation/vvaharness/plugins/semgrep/tools.py.sudo.md). Exact strings in the evidence asset support this conversion.
