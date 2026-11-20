# vvaharness/remediation_agent/models/change.py — model instruction carriers

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## file — source lines 22–22

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/remediation_agent/models/change.py:22-22
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: repo-relative path that was edited
}
```

## summary — source lines 23–23

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/remediation_agent/models/change.py:23-23
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: what changed and why (≤ 2 sentences)
}
```

