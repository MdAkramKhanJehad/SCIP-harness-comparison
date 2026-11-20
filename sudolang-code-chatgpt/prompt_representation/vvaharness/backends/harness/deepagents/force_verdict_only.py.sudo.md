# vvaharness/backends/harness/deepagents/force_verdict_only.py — model instruction carriers

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## _report_now — source lines 52–53

Source context: callable `_report_now`; enclosing call `HumanMessage`; keyword `content`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `names; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/harness/deepagents/force_verdict_only.py:52-53
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: the model have finished working.
  The request retains this source rule, criterion or rationale, with its original modal force: Report the model's outcome NOW by calling [dynamic source value: names; conversion=none; format_spec=none] with the conclusion the model just reached.
  The request retains this source rule, criterion or rationale, with its original modal force: Every other tool has been withdrawn.
}
```

