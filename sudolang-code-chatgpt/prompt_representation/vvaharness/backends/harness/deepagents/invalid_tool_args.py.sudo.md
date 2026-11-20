# vvaharness/backends/harness/deepagents/invalid_tool_args.py — model instruction carriers

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
// Source: vvaharness/backends/harness/deepagents/invalid_tool_args.py:15-15
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Middleware that repairs a tool call langchain could not parse as JSON.
}
```

## _repair_block — source lines 36–36

Source context: callable `_repair_block`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/harness/deepagents/invalid_tool_args.py:36-36
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Clear the raw ``arguments`` string on the Responses-leg ``function_call`` block it names.
}
```

## _record_invalid_call — source lines 47–47

Source context: callable `_record_invalid_call`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/harness/deepagents/invalid_tool_args.py:47-47
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Count *invalid* once per call id; its paired error ToolMessage, or None when one exists.
}
```

## _repair_message — source lines 61–65

Source context: callable `_repair_message`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/harness/deepagents/invalid_tool_args.py:61-65
Constraints {
  The advertised description supplied with this operation is a model-visible claim: *message* with every invalid tool call moved into ``tool_calls`` with ``args={}``.
}
```

```sudo
// Source: vvaharness/backends/harness/deepagents/invalid_tool_args.py:61-65
Constraints {
  The advertised description supplied with this operation is a model-visible claim: An id-less call is left in ``invalid_tool_calls`` untouched: ``ToolMessage`` requires a ``tool_call_id``, and langchain's own repair skips exactly this case the same way.
}
```

## _repair — source lines 93–93

Source context: callable `_repair`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/harness/deepagents/invalid_tool_args.py:93-93
Constraints {
  The advertised description supplied with this operation is a model-visible claim: *messages* with every invalid tool call repaired, or ``None`` when nothing changed.
}
```

## <module> — source lines 110–110

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/harness/deepagents/invalid_tool_args.py:110-110
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Repair an unparsable tool call before the next model call sees it again.
}
```

## __init__ — source lines 113–113

Source context: callable `__init__`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/harness/deepagents/invalid_tool_args.py:113-113
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Track which call ids were already counted, so a resent call id counts once.
}
```

## wrap_model_call — source lines 124–124

Source context: callable `wrap_model_call`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/harness/deepagents/invalid_tool_args.py:124-124
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Repair any invalid tool call in the outgoing request, then call the model.
}
```

## awrap_model_call — source lines 132–132

Source context: callable `awrap_model_call`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/harness/deepagents/invalid_tool_args.py:132-132
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Async counterpart of :meth:`wrap_model_call`.
}
```

## _repair_block — source lines 37–37

Source context: callable `_repair_block`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/harness/deepagents/invalid_tool_args.py:37-37
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: function_call
}
```

## _record_invalid_call — source lines 54–54

Source context: callable `_record_invalid_call`; enclosing call `ToolMessage`; keyword `content`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `error; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/harness/deepagents/invalid_tool_args.py:54-54
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: ERROR: tool arguments were not valid JSON: [dynamic source value: error; conversion=none; format_spec=none]
}
```

## _repair_block — source lines 38–38

Source context: callable `_repair_block`; enclosing call `block.get`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/harness/deepagents/invalid_tool_args.py:38-38
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: call_id
}
```

## _repair_message — source lines 76–76

Source context: callable `_repair_message`; enclosing call `new_tool_calls.append`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/harness/deepagents/invalid_tool_args.py:76-76
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: tool_call
}
```

## repaired — source lines 85–85

Source context: callable `_repair_message`; enclosing call `message.model_copy`; keyword `update`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/harness/deepagents/invalid_tool_args.py:85-85
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: tool_calls
}
```

## repaired — source lines 85–85

Source context: callable `_repair_message`; enclosing call `message.model_copy`; keyword `update`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/harness/deepagents/invalid_tool_args.py:85-85
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: invalid_tool_calls
}
```

