# vvaharness/backends/harness/deepagents/tool_choice_rejection.py — model instruction carriers

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## <module> — source lines 15–19

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/harness/deepagents/tool_choice_rejection.py:15-19
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Anthropic models that reject a forced tool_choice with a 400: classified, learned, seeded.
}
```

```sudo
// Source: vvaharness/backends/harness/deepagents/tool_choice_rejection.py:15-19
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Free of ``options.*`` imports, so ForceVerdictOnly (which options/streaming.py imports) can use it as well as the client.
}
```

## is_tool_choice_unsupported_rejection — source lines 44–44

Source context: callable `is_tool_choice_unsupported_rejection`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/harness/deepagents/tool_choice_rejection.py:44-44
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Whether *exc* is the API rejecting a forced tool_choice outright for this model.
}
```

## rejected_model — source lines 55–55

Source context: callable `rejected_model`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/harness/deepagents/tool_choice_rejection.py:55-55
Constraints {
  The advertised description supplied with this operation is a model-visible claim: The ``model`` of the request *exc* rejected, when the SDK error still carries it.
}
```

## learn_tool_choice_unsupported — source lines 71–71

Source context: callable `learn_tool_choice_unsupported`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/harness/deepagents/tool_choice_rejection.py:71-71
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Record each of *model_ids* as rejecting forced tool_choice, count it, and warn once.
}
```

