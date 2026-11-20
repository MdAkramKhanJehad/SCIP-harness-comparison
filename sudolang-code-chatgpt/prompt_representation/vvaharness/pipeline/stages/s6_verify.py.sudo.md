# vvaharness/pipeline/stages/s6_verify.py — model instruction carriers

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## _PREMISE_IMPORT_RX — source lines 620–623

Source context: callable `<module>`; enclosing call `re.compile`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

```sudo
// Source: vvaharness/pipeline/stages/s6_verify.py:620-623
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [`'\"]?([A-Za-z_]\w*(?:\.[A-Za-z_]\w*)*)[`'\"]?(?:\s+module)?\s+(?:is\s+not|isn't|is\s+never|never)\s+imported\b|\b(?:not|never|no|without|missing)\s+(?:an?\s+)?import(?:s|ed|ing)?\b(?:\s+(?:of|for))?\s+([A-Za-z_]\w*(?:\.[A-Za-z_]\w*)*)
}
```

## __init__ — source lines 99–99

Source context: callable `__init__`; enclosing call `ValueError`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

```sudo
// Source: vvaharness/pipeline/stages/s6_verify.py:99-99
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: max_workers must be greater than 0
}
```

## _run_wave — source lines 523–525

Source context: callable `_run_wave`; enclosing call `TimeoutError`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `parallel; conversion=none; format_spec=none`
- `ceiling; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s6_verify.py:523-525
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: batch never started: all [dynamic source value: parallel; conversion=none; format_spec=none] worker(s) held by ceiling-expired batches for [dynamic source value: ceiling; conversion=none; format_spec=none]s
}
```

