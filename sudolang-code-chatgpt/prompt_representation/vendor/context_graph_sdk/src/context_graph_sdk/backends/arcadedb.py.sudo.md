# vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py — model instruction carriers

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## query_readonly — source lines 284–284

Source context: callable `query_readonly`; enclosing call `ModelValidationError`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:284-284
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: row_limit must be positive
}
```

## resolve_correlations — source lines 559–559

Source context: callable `resolve_correlations`; enclosing call `ModelValidationError`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:559-559
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: correlation result limit must be positive
}
```

## warmup — source lines 128–128

Source context: callable `_database_call`; enclosing call `result.query`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:128-128
Constraints {
  The requested model reply must contain 1 AS value
}
```

