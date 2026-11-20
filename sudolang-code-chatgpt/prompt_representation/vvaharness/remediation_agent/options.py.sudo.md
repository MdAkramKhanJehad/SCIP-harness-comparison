# vvaharness/remediation_agent/options.py — model instruction carriers

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## VALID_MODES — source lines 22–22

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

```sudo
// Source: vvaharness/remediation_agent/options.py:22-22
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: report-only
}
```

## parse_options — source lines 39–39

Source context: callable `parse_options`; enclosing call `ValueError`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `mode; conversion=repr; format_spec=none`
- `VALID_MODES; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/remediation_agent/options.py:39-39
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: invalid --mode [dynamic source value: mode; conversion=repr; format_spec=none]; choose one of [dynamic source value: VALID_MODES; conversion=none; format_spec=none].
}
```

