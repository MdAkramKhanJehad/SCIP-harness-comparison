# vvaharness/remediation_agent/plugin_runner/handoff.py — model instruction carriers

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## _refusal — source lines 58–58

Source context: callable `_refusal`; enclosing call `ToolMessage`; keyword `content`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `detail; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/remediation_agent/plugin_runner/handoff.py:58-58
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Fixer dispatch was not executed: [dynamic source value: detail; conversion=none; format_spec=none]
}
```

## _prepare — source lines 77–77

Source context: callable `_prepare`; enclosing call `self._refusal`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

```sudo
// Source: vvaharness/remediation_agent/plugin_runner/handoff.py:77-77
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: the fixer already returned a completed result; do not retry
}
```

## wrap_tool_call — source lines 165–165

Source context: callable `wrap_tool_call`; enclosing call `self._refusal`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

```sudo
// Source: vvaharness/remediation_agent/plugin_runner/handoff.py:165-165
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: retry once
}
```

## wrap_tool_call — source lines 165–165

Source context: callable `wrap_tool_call`; enclosing call `self._refusal`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

```sudo
// Source: vvaharness/remediation_agent/plugin_runner/handoff.py:165-165
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: retry exhausted
}
```

## awrap_tool_call — source lines 189–189

Source context: callable `awrap_tool_call`; enclosing call `self._refusal`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

```sudo
// Source: vvaharness/remediation_agent/plugin_runner/handoff.py:189-189
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: retry once
}
```

## awrap_tool_call — source lines 189–189

Source context: callable `awrap_tool_call`; enclosing call `self._refusal`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

```sudo
// Source: vvaharness/remediation_agent/plugin_runner/handoff.py:189-189
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: retry exhausted
}
```

