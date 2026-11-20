# vvaharness/backends/llm/cli/envelope.py — model instruction carriers

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## _GUARDRAIL_REFUSALS — source lines 45–45

Source context: callable `<module>`; enclosing call `frozenset`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/cli/envelope.py:45-45
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: the model's request was not allowed
}
```

## refused — source lines 124–124

Source context: callable `_refusal_category_of`; enclosing call `e['message'].get`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/cli/envelope.py:124-124
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: stop_reason
}
```

## api — source lines 129–129

Source context: callable `_refusal_category_of`; enclosing call `next`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/cli/envelope.py:129-129
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: model_refusal_no_fallback
}
```

