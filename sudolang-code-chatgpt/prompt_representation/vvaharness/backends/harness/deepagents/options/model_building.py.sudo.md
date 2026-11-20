# vvaharness/backends/harness/deepagents/options/model_building.py — model instruction carriers

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## REASON_IN_PROMPT — source lines 365–367

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/harness/deepagents/options/model_building.py:365-367
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: REASONING: think it through in writing before the model answer.
  The requested evidence/output includes each candidate, the control or framework default that would refute it, and discard what does not hold.
  The request retains this source rule, criterion or rationale, with its original modal force: Keep it compact -- no restating the input, no recap of the model's own steps.
}
```

## _NO_REASON_IN_PROMPT_RX — source lines 374–374

Source context: callable `<module>`; enclosing call `re.compile`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/harness/deepagents/options/model_building.py:374-374
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: claude-(?:sonnet-5-5|opus-5|fable-5)(?!\d)
}
```

