# vvaharness/injectors/cve_feed.py — model instruction carriers

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## load_cves — source lines 59–59

Source context: callable `load_cves`; enclosing call `TypeError`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `type(items).__name__; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/injectors/cve_feed.py:59-59
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: CVE feed payload must be a list, got [dynamic source value: type(items).__name__; conversion=none; format_spec=none]
}
```

