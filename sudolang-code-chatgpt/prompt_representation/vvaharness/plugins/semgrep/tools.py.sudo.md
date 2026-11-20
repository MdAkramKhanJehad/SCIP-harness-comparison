# vvaharness/plugins/semgrep/tools.py — model instruction carriers

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## <module> — source lines 15–15

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/plugins/semgrep/tools.py:15-15
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Read-only tools over the Semgrep subgraph an enricher attached to the code graph.
}
```

## _FINDINGS_FOR_FILE — source lines 25–33

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/plugins/semgrep/tools.py:25-33
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: MATCH (subject)-[:FLAGGED_BY]->(f:SemgrepFinding)-[:DETECTED_BY]->(r:SemgrepRule) WHERE f.filePath = $file RETURN f.ruleId AS ruleId, f.filePath AS path, f.semgrepStartLine AS line, f.severity AS severity, subject.name AS symbol, r.cweIds AS cweIds, r.vulnerabilityClasses AS classes ORDER BY line, ruleId LIMIT 25
}
```

## _TRACE_FOR_RULE — source lines 35–42

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/plugins/semgrep/tools.py:35-42
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: MATCH (f:SemgrepFinding)-[trace:TRACE_TOUCHES]->(symbol) WHERE f.ruleId = $rule_id RETURN f.ruleId AS ruleId, trace.step AS step, trace.role AS role, trace.filePath AS path, trace.startLine AS line, symbol.name AS symbol ORDER BY step LIMIT 40
}
```

## _CALLERS_OF_FLAGGED_SINKS — source lines 44–51

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/plugins/semgrep/tools.py:44-51
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: MATCH (f:SemgrepFinding)-[trace:TRACE_TOUCHES]->(sink)<-[:CALLS]-(caller) WHERE trace.role = 'sink' AND f.filePath = $file RETURN f.ruleId AS ruleId, sink.name AS sink, caller.name AS caller, caller.filePath AS callerPath ORDER BY sink, caller LIMIT 25
}
```

## _SCAN_COVERAGE — source lines 53–58

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/plugins/semgrep/tools.py:53-58
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: MATCH (s:SemgrepScan) RETURN s.complete AS complete, s.findingCount AS findings, s.errorCount AS errors, s.skippedCount AS skipped LIMIT 1
}
```

## _rows — source lines 62–62

Source context: callable `_rows`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/plugins/semgrep/tools.py:62-62
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Bounded cypher rows as plain dicts, or a one-key error dict the model can act on.
}
```

## semgrep_findings_tool — source lines 71–71

Source context: callable `semgrep_findings_tool`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/plugins/semgrep/tools.py:71-71
Constraints {
  The described operation is advertised for builds ``GraphSemgrepFindings``, the per-file view of what Semgrep flagged.; this description alone does not request its invocation.
}
```

## semgrep_trace_tool — source lines 82–82

Source context: callable `semgrep_trace_tool`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/plugins/semgrep/tools.py:82-82
Constraints {
  The described operation is advertised for builds ``GraphSemgrepTaintTrace``, the ordered source-to-sink steps behind one finding.; this description alone does not request its invocation.
}
```

## semgrep_sink_callers_tool — source lines 93–93

Source context: callable `semgrep_sink_callers_tool`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/plugins/semgrep/tools.py:93-93
Constraints {
  The described operation is advertised for builds ``GraphSemgrepSinkCallers``, joining traced sinks onto the structural call graph.; this description alone does not request its invocation.
}
```

## semgrep_coverage_tool — source lines 104–104

Source context: callable `semgrep_coverage_tool`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/plugins/semgrep/tools.py:104-104
Constraints {
  The described operation is advertised for builds ``GraphSemgrepCoverage``, the scan's own completeness report.; this description alone does not request its invocation.
}
```

## __all__ — source lines 123–123

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/plugins/semgrep/tools.py:123-123
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: SEMGREP_TOOLS
}
```

## __all__ — source lines 123–123

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/plugins/semgrep/tools.py:123-123
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: SEMGREP_TOOL_NAMES
}
```

## GraphSemgrepFindings — source lines 75–75

Source context: callable `GraphSemgrepFindings`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/plugins/semgrep/tools.py:75-75
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Semgrep findings on *file*, each with its rule id, severity, enclosing symbol, and the rule's CWE ids.
  The advertised description supplied with this operation is a model-visible claim: Empty means Semgrep flagged nothing here, which is not proof the file is safe.
}
```

## GraphSemgrepTaintTrace — source lines 86–86

Source context: callable `GraphSemgrepTaintTrace`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/plugins/semgrep/tools.py:86-86
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Ordered taint steps for findings of *rule_id*, each step carrying an explicit role of source, intermediate or sink.
  The advertised description supplied with this operation is a model-visible claim: Semgrep reports representative routes, not every route, and an empty result means it recorded no explicit trace rather than that no flow exists.
}
```

## GraphSemgrepSinkCallers — source lines 97–97

Source context: callable `GraphSemgrepSinkCallers`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/plugins/semgrep/tools.py:97-97
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Functions that call a Semgrep-traced sink in *file* — the reachability question a finding alone cannot answer.
  The advertised description supplied with this operation is a model-visible claim: An empty caller list means nothing in the graph reaches that sink, so it is an entry point or unreachable.
}
```

## GraphSemgrepCoverage — source lines 108–108

Source context: callable `GraphSemgrepCoverage`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/plugins/semgrep/tools.py:108-108
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Whether this repository's Semgrep scan was complete, with its finding, error and skip counts.
  The advertised description supplied with this operation is a model-visible claim: A complete scan means no represented coverage loss; it is not a security assurance.
}
```

## GraphSemgrepTaintTrace — source lines 87–87

Source context: callable `GraphSemgrepTaintTrace`; enclosing call `_rows`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/plugins/semgrep/tools.py:87-87
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: rule_id
}
```

## _rows — source lines 66–66

Source context: callable `_rows`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `type(exc).__name__; conversion=none; format_spec=none`
- `exc; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/plugins/semgrep/tools.py:66-66
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: type(exc).__name__; conversion=none; format_spec=none]: [dynamic source value: exc; conversion=none; format_spec=none]
}
```

## _rows — source lines 67–67

Source context: callable `_rows`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/plugins/semgrep/tools.py:67-67
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: no Semgrep subgraph in this scan; the enricher did not run
}
```

