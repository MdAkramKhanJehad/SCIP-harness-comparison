# vvaharness/remediation_agent/plugin_runner/__init__.py — model instruction carriers

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## msg — source lines 178–184

Source context: callable `_report_recursion_limit`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `options.model; conversion=none; format_spec=none`
- `limit; conversion=none; format_spec=none`
- `options.max_turns; conversion=none; format_spec=none`
- `RECURSION_HEADROOM; conversion=none; format_spec=none`
- `n_calls; conversion=none; format_spec=none`
- `n_msgs; conversion=none; format_spec=none`
- `shape; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/remediation_agent/plugin_runner/__init__.py:178-184
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [deepagents] [dynamic source value: options.model; conversion=none; format_spec=none] HIT THE LANGGRAPH RECURSION LIMIT (recursion_limit=[dynamic source value: limit; conversion=none; format_spec=none] = step_remediate.max_turns([dynamic source value: options.max_turns; conversion=none; format_spec=none]) + [dynamic source value: RECURSION_HEADROOM; conversion=none; format_spec=none]).
  The request retains this source rule, criterion or rationale, with its original modal force: The tool loop was truncated mid-flight after [dynamic source value: n_calls; conversion=none; format_spec=none] tool call(s) / [dynamic source value: n_msgs; conversion=none; format_spec=none] message(s) (last=[dynamic source value: shape; conversion=none; format_spec=none]), so the agent never reached a final turn and produced NO structured verdict. ACTION: set step_remediate.max_model_calls (e.g. 20) to force a final verdict turn well before this limit; raising max_turns only raises the limit and lengthens the loop.
}
```

## _verdict_extraction_prompt — source lines 193–195

Source context: callable `_verdict_extraction_prompt`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `schema; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/remediation_agent/plugin_runner/__init__.py:193-195
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: the model completed remediation work above but did not emit a structured verdict.
  The request retains this source rule, criterion or rationale, with its original modal force: Based solely on the work the model did, return ONLY a JSON object — no prose, no markdown fences — matching exactly this JSON Schema: [dynamic source value: schema; conversion=none; format_spec=none]
}
```

## lines[0] — source lines 326–326

Source context: callable `_virtualize_deepagents_prompt`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/remediation_agent/plugin_runner/__init__.py:326-326
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: REPOSITORY ROOT: / (DeepAgents virtual workspace root)
}
```

## _virtualize_deepagents_prompt — source lines 325–325

Source context: callable `_virtualize_deepagents_prompt`; enclosing call `lines[0].startswith`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/remediation_agent/plugin_runner/__init__.py:325-325
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: REPOSITORY ROOT:
}
```

## agents — source lines 352–352

Source context: callable `_invoke_deepagents`; enclosing call `SubagentDefinition`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/remediation_agent/plugin_runner/__init__.py:352-352
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Applies the security fix to the target file(s).
}
```

