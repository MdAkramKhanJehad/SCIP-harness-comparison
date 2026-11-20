# vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py — model instruction carriers

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## run_bounded — source lines 252–252

Source context: callable `run_bounded`; enclosing call `ModelValidationError`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `MAX_EXTRACTION_PROCESSES; conversion=none; format_spec=none`

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:252-252
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: max_workers must be in [1, [dynamic source value: MAX_EXTRACTION_PROCESSES; conversion=none; format_spec=none]]
}
```

## run_bounded — source lines 254–254

Source context: callable `run_bounded`; enclosing call `ModelValidationError`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:254-254
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: file_timeout_seconds must be in (0, 3600]
}
```

## run_bounded — source lines 257–257

Source context: callable `run_bounded`; enclosing call `ModelValidationError`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `MAX_EXTRACTION_RESULT_BYTES; conversion=none; format_spec=none`

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:257-257
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: max_result_bytes must be in [1, [dynamic source value: MAX_EXTRACTION_RESULT_BYTES; conversion=none; format_spec=none]]
}
```

## run_bounded — source lines 268–268

Source context: callable `run_bounded`; enclosing call `ModelValidationError`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `MAX_AGGREGATE_TIMEOUT_SECONDS; conversion=none; format_spec=none`

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:268-268
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: aggregate_timeout_seconds must be in (0, [dynamic source value: MAX_AGGREGATE_TIMEOUT_SECONDS; conversion=none; format_spec=none]]
}
```

