# vvaharness/backends/llm/tool_adapter.py — model instruction carriers

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
// Source: vvaharness/backends/llm/tool_adapter.py:15-15
Constraints {
  The advertised description supplied with this operation is a model-visible claim: In-process langchain-tool adapter: caller fact tools on `via: sdk` / `via: openai`.
}
```

## _materialize — source lines 46–46

Source context: callable `_materialize`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/llm/tool_adapter.py:46-46
Constraints {
  The described operation is advertised for run the caller's ``ToolBuilder`` and keep only its fact tools.; this description alone does not request its invocation.
}
```

## _tool_schema — source lines 59–59

Source context: callable `_tool_schema`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/llm/tool_adapter.py:59-59
Constraints {
  The advertised description supplied with this operation is a model-visible claim: The JSON-schema object for a langchain tool's arguments.
}
```

## _anthropic_schema — source lines 69–69

Source context: callable `_anthropic_schema`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/llm/tool_adapter.py:69-69
Constraints {
  The advertised description supplied with this operation is a model-visible claim: One Anthropic Messages tool schema for a langchain tool.
}
```

## _budget_refusal — source lines 77–77

Source context: callable `_budget_refusal`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/llm/tool_adapter.py:77-77
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Refusal text when one of the caller's own budgets has no allowance left.
}
```

## _required_fact_tools — source lines 89–89

Source context: callable `_required_fact_tools`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/llm/tool_adapter.py:89-89
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Tool names the caller's EvidenceGate would have demanded before a verdict.
}
```

## _serialize — source lines 99–99

Source context: callable `_serialize`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/llm/tool_adapter.py:99-99
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Render a tool result as text, JSON when it is structured.
}
```

## <module> — source lines 110–110

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/llm/tool_adapter.py:110-110
Constraints {
  The advertised description supplied with this operation is a model-visible claim: The materialised tools for one session, in the shape both agentic loops accept.
}
```

## build — source lines 224–224

Source context: callable `build`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/llm/tool_adapter.py:224-224
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Adapt the caller's ``tool_builder`` for one ``sdk``/``openai`` agentic session.
}
```

## _validation_error — source lines 124–124

Source context: callable `_validation_error`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/llm/tool_adapter.py:124-124
Constraints {
  The advertised description supplied with this operation is a model-visible claim: *args* checked against *lc_tool*'s schema, or ``None`` when it has none or passes.
}
```

## _tool_fault — source lines 136–136

Source context: callable `_tool_fault`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/llm/tool_adapter.py:136-136
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Count, log, and format a tool fault as the adapter's standard error string.
}
```

## _rejected — source lines 144–144

Source context: callable `_rejected`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/llm/tool_adapter.py:144-144
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Validation or budget rejection text for this call, or ``None`` to proceed.
}
```

## dispatch — source lines 156–156

Source context: callable `dispatch`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/llm/tool_adapter.py:156-156
Constraints {
  The described operation is advertised for run one adapted tool, or return ``None`` so the loop's localtools get the name.; this description alone does not request its invocation.
}
```

## exhausted_tools — source lines 185–185

Source context: callable `exhausted_tools`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/llm/tool_adapter.py:185-185
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Union of every metered tool name whose caller-owned budget is now spent.
}
```

## submit_guard — source lines 195–195

Source context: callable `submit_guard`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/llm/tool_adapter.py:195-195
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Text to hand back as a tool result instead of the verdict, or ``None`` to allow it.
}
```

## report_evidence_degradation — source lines 206–206

Source context: callable `report_evidence_degradation`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/llm/tool_adapter.py:206-206
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Count and announce a verdict that shipped without ever consulting a required tool.
}
```

## refusal — source lines 79–79

Source context: callable `_budget_refusal`; enclosing call `getattr`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/tool_adapter.py:79-79
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: refusal_for
}
```

