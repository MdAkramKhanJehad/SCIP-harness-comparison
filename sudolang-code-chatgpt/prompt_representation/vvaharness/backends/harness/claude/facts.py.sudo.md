# vvaharness/backends/harness/claude/facts.py — model instruction carriers

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## SUBMIT_PROMPT_SUFFIX — source lines 179–186

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `mcp_name(SUBMIT_TOOL); conversion=none; format_spec=none`

## Report submission (this run)

```sudo
// Source: vvaharness/backends/harness/claude/facts.py:179-186
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Submit the model's final report by calling the `[dynamic source value: mcp_name(SUBMIT_TOOL); conversion=none; format_spec=none]` tool with the report object as its arguments.
  The request retains this source rule, criterion or rationale, with its original modal force: It is validated on submission and will tell the model which fields to fix if it is rejected.
  The request retains this source rule, criterion or rationale, with its original modal force: Print the same report as a ```json block as well, so it is visible in the transcript.
}
```

```sudo
// Source: vvaharness/backends/harness/claude/facts.py:179-186
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: the model's fact tools are named with an `mcp__facts__` prefix on this run: `mcp__facts__DiffTouched`, `mcp__facts__ChangedLines`, `mcp__facts__DiffImpactMap`, `mcp__facts__PatternScan`, `mcp__facts__TestInventory`.
}
```

## _submit — source lines 126–129

Source context: callable `_submit`; enclosing call `sdk_tool`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `report_model.__name__; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/harness/claude/facts.py:126-129
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Submit the model's final [dynamic source value: report_model.__name__; conversion=none; format_spec=none].
  The request retains this source rule, criterion or rationale, with its original modal force: Call this exactly once, as the model's last action.
  The request retains this source rule, criterion or rationale, with its original modal force: The report is validated on submission; if it is rejected, fix the named fields and call this again.
}
```

## _submit — source lines 141–141

Source context: callable `_submit`; enclosing call `_content`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

```sudo
// Source: vvaharness/backends/harness/claude/facts.py:141-141
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Report accepted.
}
```

## _submit — source lines 137–138

Source context: callable `_submit`; enclosing call `_content`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `report_model.__name__; conversion=none; format_spec=none`
- `exc; conversion=none; format_spec=none`
- `SUBMIT_TOOL; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/harness/claude/facts.py:137-138
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Report rejected — not a valid [dynamic source value: report_model.__name__; conversion=none; format_spec=none]: [dynamic source value: exc; conversion=none; format_spec=none].
  The request retains this source rule, criterion or rationale, with its original modal force: Fix the fields named above and call [dynamic source value: SUBMIT_TOOL; conversion=none; format_spec=none] again.
}
```

