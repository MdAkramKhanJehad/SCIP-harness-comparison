# vvaharness/backends/llm/registry.py — model instruction carriers

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## resolve — source lines 113–113

Source context: callable `resolve`; enclosing call `ValueError`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `model_cfg; conversion=repr; format_spec=none`

```sudo
// Source: vvaharness/backends/llm/registry.py:113-113
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Model config must be a string or have an `id` field: got [dynamic source value: model_cfg; conversion=repr; format_spec=none]
}
```

## prompt — source lines 212–212

Source context: callable `prompt`; enclosing call `kw.get`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/registry.py:212-212
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: max_tokens
}
```

## kw['max_tokens'] — source lines 213–213

Source context: callable `prompt`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/registry.py:213-213
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: max_tokens
}
```

## kw['output_cap'] — source lines 216–216

Source context: callable `prompt`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/registry.py:216-216
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: output_cap
}
```

## _prefix — source lines 220–220

Source context: callable `prompt`; enclosing call `kw.get`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/registry.py:220-220
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: cache_prefix
}
```

## kw['max_tokens'] — source lines 213–213

Source context: callable `prompt`; enclosing call `int`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/registry.py:213-213
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: max_tokens
}
```

## prompt — source lines 228–228

Source context: callable `prompt`; enclosing call `kw.get`; keyword `system_prompt`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/registry.py:228-228
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: system_prompt
}
```

