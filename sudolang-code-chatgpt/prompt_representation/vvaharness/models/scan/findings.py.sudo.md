# vvaharness/models/scan/findings.py — model instruction carriers

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## from_id — source lines 126–126

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/models/scan/findings.py:126-126
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: The FINDING id this link starts at (e.g. f3).
}
```

## to_id — source lines 127–127

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/models/scan/findings.py:127-127
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: The FINDING id this link leads to (e.g. f7).
}
```

## mechanism — source lines 129–130

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/models/scan/findings.py:129-130
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Concretely, what from_id produces that to_id consumes — a value, a privilege, a reachable state.
  The request retains this source rule, criterion or rationale, with its original modal force: Not a restatement of the two titles.
}
```

## file — source lines 132–132

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/models/scan/findings.py:132-132
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Repo-relative path of the code that shows this link holds.
}
```

## line — source lines 134–134

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/models/scan/findings.py:134-134
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Line in that file which shows it.
  The request retains this source rule, criterion or rationale, with its original modal force: Must be a real line.
}
```

