# vendor/context_graph_sdk/src/context_graph_sdk/identity.py — model instruction carriers

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## _validate_named_id — source lines 30–30

Source context: callable `_validate_named_id`; enclosing call `ModelValidationError`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `kind; conversion=none; format_spec=none`
- `maximum; conversion=none; format_spec=none`

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/identity.py:30-30
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: kind; conversion=none; format_spec=none] must contain 1..[dynamic source value: maximum; conversion=none; format_spec=none] characters
}
```

## validate_local_id — source lines 60–60

Source context: callable `validate_local_id`; enclosing call `ModelValidationError`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/identity.py:60-60
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: local_id must contain 1..512 characters
}
```

