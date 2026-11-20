# vendor/context_graph_sdk/src/context_graph_sdk/query/contracts.py — model instruction carriers

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## __post_init__ — source lines 40–40

Source context: callable `__post_init__`; enclosing call `ModelValidationError`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/contracts.py:40-40
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: timeout_seconds must be in (0, 3600]
}
```

## __post_init__ — source lines 42–42

Source context: callable `__post_init__`; enclosing call `ModelValidationError`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/contracts.py:42-42
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: memory_bytes must be positive
}
```

## __post_init__ — source lines 44–44

Source context: callable `__post_init__`; enclosing call `ModelValidationError`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `MAX_QUERY_ROWS; conversion=none; format_spec=none`

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/contracts.py:44-44
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: row_limit must be in [1, [dynamic source value: MAX_QUERY_ROWS; conversion=none; format_spec=none]]
}
```

## __post_init__ — source lines 46–46

Source context: callable `__post_init__`; enclosing call `ModelValidationError`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `MAX_QUERY_BYTES; conversion=none; format_spec=none`

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/contracts.py:46-46
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: byte_limit must be in [1, [dynamic source value: MAX_QUERY_BYTES; conversion=none; format_spec=none]]
}
```

## __post_init__ — source lines 59–59

Source context: callable `__post_init__`; enclosing call `ModelValidationError`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/contracts.py:59-59
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: request_id must contain 1..128 characters
}
```

## __post_init__ — source lines 96–96

Source context: callable `__post_init__`; enclosing call `ModelValidationError`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/contracts.py:96-96
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: max_workers must be positive
}
```

## __post_init__ — source lines 98–98

Source context: callable `__post_init__`; enclosing call `ModelValidationError`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/contracts.py:98-98
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: worker IPC byte bounds must be positive
}
```

## __post_init__ — source lines 120–120

Source context: callable `__post_init__`; enclosing call `ModelValidationError`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/contracts.py:120-120
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: truncation reason must match truncated state
}
```

## __post_init__ — source lines 132–132

Source context: callable `__post_init__`; enclosing call `ModelValidationError`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/contracts.py:132-132
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: worker process_id must be positive
}
```

