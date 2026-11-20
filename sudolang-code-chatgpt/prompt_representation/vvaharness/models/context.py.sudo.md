# vvaharness/models/context.py — model instruction carriers

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## required_gates — source lines 31–31

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/models/context.py:31-31
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: gates a validator must answer
}
```

## weights — source lines 32–32

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/models/context.py:32-32
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: per-gate weight
}
```

## critical — source lines 34–34

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/models/context.py:34-34
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: gates whose failure caps the verdict
}
```

## ready_at — source lines 36–36

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/models/context.py:36-36
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: score at or above which a fix is ready
}
```

## conditional_at — source lines 38–38

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/models/context.py:38-38
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: score at or above which a fix is ready with conditions
}
```

## msg — source lines 47–49

Source context: callable `_gates_and_weights_agree`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `only_required; conversion=none; format_spec=none`
- `only_weighted; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/models/context.py:47-49
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: ScoringPolicy gate sets disagree: required-only=[dynamic source value: only_required; conversion=none; format_spec=none], weighted-only=[dynamic source value: only_weighted; conversion=none; format_spec=none].
  The request retains this source rule, criterion or rationale, with its original modal force: A gate this host scores must be one it asked for, and vice versa.
}
```

