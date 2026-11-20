# vvaharness/backends/llm/cli_mcp.py — model instruction carriers

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## refusal — source lines 118–118

Source context: callable `_budget_refusal`; enclosing call `getattr`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/cli_mcp.py:118-118
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: refusal_for
}
```

## _pre_tool_use_gate — source lines 342–344

Source context: callable `_pre_tool_use_gate`; enclosing call `_deny`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `tool_name; conversion=none; format_spec=none`
- `raw; conversion=repr; format_spec=none`
- `parts[0]; conversion=repr; format_spec=none`

```sudo
// Source: vvaharness/backends/llm/cli_mcp.py:342-344
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: tool_name; conversion=none; format_spec=none] target [dynamic source value: raw; conversion=repr; format_spec=none] falls under the internal [dynamic source value: parts[0]; conversion=repr; format_spec=none] directory, which is never readable in a scan session.
}
```

## opts — source lines 380–380

Source context: callable `_build_options`; enclosing call `ClaudeAgentOptions`; keyword `disallowed_tools`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `d; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/llm/cli_mcp.py:380-380
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Read(./[dynamic source value: d; conversion=none; format_spec=none]/**)
}
```

