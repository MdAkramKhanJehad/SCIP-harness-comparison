# vvaharness/backends/harness/deepagents/model_call_budget.py — model instruction carriers

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## __init__ — source lines 47–47

Source context: callable `__init__`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/harness/deepagents/model_call_budget.py:47-47
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: model_call_budget_final_turn
}
```

## name — source lines 63–63

Source context: callable `name`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `self.__class__.__name__; conversion=none; format_spec=none`
- `self._counter; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/harness/deepagents/model_call_budget.py:63-63
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: self.__class__.__name__; conversion=none; format_spec=none][[dynamic source value: self._counter; conversion=none; format_spec=none]]
}
```

## _final_turn_notice — source lines 32–38

Source context: callable `_final_turn_notice`; enclosing call `HumanMessage`; keyword `content`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `limit; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/harness/deepagents/model_call_budget.py:32-38
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: FINAL TURN.
  The request retains this source rule, criterion or rationale, with its original modal force: the model have used the model's [dynamic source value: limit; conversion=none; format_spec=none] model calls for this unit, and every tool except the outcome report has been withdrawn — no further Read, Grep, execute or graph call will run.
}
```

```sudo
// Source: vvaharness/backends/harness/deepagents/model_call_budget.py:32-38
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Report the outcome object NOW from the evidence the model already hold.
  The request retains this source rule, criterion or rationale, with its original modal force: Findings the model have confirmed are kept; do not discard them because the model wanted one more lookup.
  The requested conditional/temporal rule is: If a question stayed open, say so in the rationale and set the verdict accordingly — `inconclusive` is honest, silence is not.
}
```

## _check_exhausted — source lines 91–92

Source context: callable `_check_exhausted`; enclosing call `ModelCallBudgetExhaustedError`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/harness/deepagents/model_call_budget.py:91-92
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: the forced final turn (every tool but the outcome withdrawn) still did not end the session on the outcome tool
}
```

