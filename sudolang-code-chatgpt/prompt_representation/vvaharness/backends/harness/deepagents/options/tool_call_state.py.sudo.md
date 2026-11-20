# vvaharness/backends/harness/deepagents/options/tool_call_state.py — model instruction carriers

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
// Source: vvaharness/backends/harness/deepagents/options/tool_call_state.py:15-15
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Send back per-tool-call fields the endpoint put outside the OpenAI schema (Chat Completions).
}
```

## <module> — source lines 72–72

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/harness/deepagents/options/tool_call_state.py:72-72
Constraints {
  The advertised description supplied with this operation is a model-visible claim: ChatOpenAI that sends the extra fields the endpoint put on a tool call back on that call.
}
```

## _replay — source lines 57–57

Source context: callable `_replay`; enclosing call `sent.get`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/harness/deepagents/options/tool_call_state.py:57-57
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: tool_calls
}
```

