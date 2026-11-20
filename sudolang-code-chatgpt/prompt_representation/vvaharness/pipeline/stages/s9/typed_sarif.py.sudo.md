# vvaharness/pipeline/stages/s9/typed_sarif.py — model instruction carriers

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## posture_channel — source lines 175–175

Source context: callable `build_sarif`; enclosing call `knob`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s9/typed_sarif.py:175-175
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: output.posture_channel
}
```

## build_sarif — source lines 411–413

Source context: callable `build_sarif`; enclosing call `notifications.append`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `truncated; conversion=none; format_spec=none`
- `health['threats_total']; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s9/typed_sarif.py:411-413
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: truncated; conversion=none; format_spec=none] threat(s) exceeded the step2.max_threats cap and were never investigated; threatsTotal counts only the [dynamic source value: health['threats_total']; conversion=none; format_spec=none] that remained
}
```

## build_sarif — source lines 405–405

Source context: callable `build_sarif`; enclosing call `notifications.append`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

```sudo
// Source: vvaharness/pipeline/stages/s9/typed_sarif.py:405-405
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: report degraded (no reason recorded)
}
```

