# vvaharness/remediation_agent/models/gates.py — model instruction carriers

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## source — source lines 30–30

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/remediation_agent/models/gates.py:30-30
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Gate A — attacker-controlled source identified
}
```

## sink — source lines 31–31

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/remediation_agent/models/gates.py:31-31
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Gate B — security-relevant sink reachable from source
}
```

## missing_control — source lines 32–32

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/remediation_agent/models/gates.py:32-32
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Gate C — missing/insufficient validation
}
```

