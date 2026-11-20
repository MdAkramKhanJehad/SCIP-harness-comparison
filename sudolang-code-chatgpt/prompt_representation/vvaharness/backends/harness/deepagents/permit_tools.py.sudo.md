# vvaharness/backends/harness/deepagents/permit_tools.py — model instruction carriers

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
// Source: vvaharness/backends/harness/deepagents/permit_tools.py:15-15
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Middleware that refuses execution of any tool call outside a permitted set.
}
```

## <module> — source lines 39–39

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/harness/deepagents/permit_tools.py:39-39
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Refuse any tool call whose name is not in a fixed permitted set.
}
```

## __init__ — source lines 42–42

Source context: callable `__init__`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/harness/deepagents/permit_tools.py:42-42
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Allow only the tool names in *permitted* to execute; refuse the rest.
}
```

## _refusal — source lines 47–47

Source context: callable `_refusal`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/harness/deepagents/permit_tools.py:47-47
Constraints {
  The advertised description supplied with this operation is a model-visible claim: A synthetic error ToolMessage when the call is not permitted, else None.
}
```

## wrap_tool_call — source lines 68–68

Source context: callable `wrap_tool_call`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/harness/deepagents/permit_tools.py:68-68
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Execute the call only when permitted; otherwise return the refusal.
}
```

## awrap_tool_call — source lines 76–76

Source context: callable `awrap_tool_call`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/harness/deepagents/permit_tools.py:76-76
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Async counterpart of :meth:`wrap_tool_call`.
}
```

## _refusal — source lines 55–56

Source context: callable `_refusal`; enclosing call `ToolMessage`; keyword `content`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `name; conversion=repr; format_spec=none`

```sudo
// Source: vvaharness/backends/harness/deepagents/permit_tools.py:55-56
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Error: tool [dynamic source value: name; conversion=repr; format_spec=none] is not permitted in this session and was not executed.
}
```

