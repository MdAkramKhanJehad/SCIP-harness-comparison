# vvaharness/remediation_agent/report_parser/fields.py — model instruction carriers

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## parse_finding_fields — source lines 143–143

Source context: callable `parse_finding_fields`; enclosing call `secs.get`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/remediation_agent/report_parser/fields.py:143-143
Constraints {
  The advertised description supplied with this operation is a model-visible claim: description
}
```

## to_scan_finding — source lines 55–55

Source context: callable `to_scan_finding`; enclosing call `ScanFinding`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/remediation_agent/report_parser/fields.py:55-55
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: description
}
```

