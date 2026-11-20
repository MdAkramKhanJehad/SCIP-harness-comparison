# vvaharness/backends/harness/deepagents/tools.py — model instruction carriers

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
// Source: vvaharness/backends/harness/deepagents/tools.py:15-15
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Logical->native tool-name resolution for the DeepAgents backend.
}
```

## _warn_unknown_tools — source lines 46–46

Source context: callable `_warn_unknown_tools`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/harness/deepagents/tools.py:46-46
Constraints {
  The advertised description supplied with this operation is a model-visible claim: WARN once per distinct allow-listed name that resolves to no tool at all.
}
```

## _allowed_tool_names — source lines 63–63

Source context: callable `_allowed_tool_names`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/harness/deepagents/tools.py:63-63
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Resolve the effective allow-list: explicit *allowed_tools* else the policy's.
}
```

## native_tool_names — source lines 71–71

Source context: callable `native_tool_names`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/harness/deepagents/tools.py:71-71
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Resolve the logical allow-list to the native names this backend exposes.
}
```

## session_tool_names — source lines 80–80

Source context: callable `session_tool_names`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/harness/deepagents/tools.py:80-80
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Names of the caller-built session tools, for the executor permit set.
}
```

## build_tools — source lines 106–106

Source context: callable `build_tools`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/harness/deepagents/tools.py:106-106
Constraints {
  The described operation is advertised for build only the tools DeepAgents does not already provide.; this description alone does not request its invocation.
}
```

