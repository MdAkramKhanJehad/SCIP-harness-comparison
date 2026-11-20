# vvaharness/backends/harness/deepagents/exclude_tools.py — model instruction carriers

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## <module> — source lines 15–15

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/harness/deepagents/exclude_tools.py:15-15
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Middleware that withholds a fixed set of tools from every model request.
}
```

## _tool_name — source lines 31–31

Source context: callable `_tool_name`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/harness/deepagents/exclude_tools.py:31-31
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Name of a BaseTool or dict-shaped tool spec.
}
```

## <module> — source lines 37–37

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/harness/deepagents/exclude_tools.py:37-37
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Withhold named tools from the model's request.
}
```

## __init__ — source lines 40–40

Source context: callable `__init__`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/harness/deepagents/exclude_tools.py:40-40
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Withhold the tools named in *excluded* from every model request.
}
```

## wrap_model_call — source lines 51–51

Source context: callable `wrap_model_call`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/harness/deepagents/exclude_tools.py:51-51
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Call the model with the excluded tools removed from the request.
}
```

## awrap_model_call — source lines 59–59

Source context: callable `awrap_model_call`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/harness/deepagents/exclude_tools.py:59-59
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Async counterpart of :meth:`wrap_model_call`.
}
```

