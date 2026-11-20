# vvaharness/models/provenance.py — model instruction carriers

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## engine — source lines 36–36

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/models/provenance.py:36-36
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: engine identity, e.g. 'vvaharness.agentic'
}
```

## engine_version — source lines 37–37

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/models/provenance.py:37-37
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: version of that engine
}
```

## model — source lines 38–38

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/models/provenance.py:38-38
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: model id, when the engine used one
}
```

## backend — source lines 43–49

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/models/provenance.py:43-49
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: registry-qualified transport, e.g. 'llm:cli'. NOTE 'llm:deepagents' is S10 remediation on the deepagents route — a historical label, not an accurate one: that call executes on the HARNESS, not through the llm registry (which has no deepagents backend and raises on one).
  The request retains this source rule, criterion or rationale, with its original modal force: It is kept as-is because the (model, backend) pair is hashed into S10 resume checkpoint keys, so relabelling it would invalidate in-flight resume state. 'harness:deepagents' is S11 validation.
}
```

## turns — source lines 53–53

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/models/provenance.py:53-53
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: agent turns; None when unreported
}
```

## usd — source lines 54–54

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/models/provenance.py:54-54
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: spend in USD; None when unreported
}
```

## started — source lines 55–55

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/models/provenance.py:55-55
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: UTC start
}
```

## ended — source lines 56–56

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/models/provenance.py:56-56
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: UTC finish
}
```

