# vvaharness/pipeline/stages/s7/outcomes.py — model instruction carriers

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## _coerce_flag — source lines 48–48

Source context: callable `_coerce_flag`; enclosing call `field_validator`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s7/outcomes.py:48-48
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: independent_sites
}
```

## index — source lines 33–33

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s7/outcomes.py:33-33
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Echo the FINDING index the model were given, verbatim.
}
```

## duplicate_of — source lines 35–37

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s7/outcomes.py:35-37
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: The index of the finding this one duplicates — always LOWER than `index`, because the lowest index of a group is always the canonical one.
  The model is asked to adopt -1 when this finding is not a duplicate of anything, which is the common answer.
}
```

## reasoning — source lines 39–40

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s7/outcomes.py:39-40
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: One sentence.
  The request retains this source rule, criterion or rationale, with its original modal force: For a duplicate, name the single fix that closes both; for a non-duplicate, name the fix this one needs that no other finding's fix covers.
}
```

## independent_sites — source lines 43–46

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s7/outcomes.py:43-46
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: For a duplicate: true when each finding in the group is an independently fixable defect at its own dangerous operation — fixing one site would not fix the others, so the member's location must survive on the survivor as an extra call site.
  The request retains this source rule, criterion or rationale, with its original modal force: False when one root-cause or control fix covers every member.
  The request retains this source rule, criterion or rationale, with its original modal force: Always false on a non-duplicate.
}
```

## decisions — source lines 57–58

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s7/outcomes.py:57-58
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: ONE entry per FINDING index the model were given, in ascending order.
  The request retains this source rule, criterion or rationale, with its original modal force: An index the model omit is kept as its own separate finding — safe, but it means nobody ruled on it, so judge every one.
}
```

## parse_decisions — source lines 94–94

Source context: callable `parse_decisions`; enclosing call `COUNTERS.bump`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s7/outcomes.py:94-94
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s7_dedup_index_omitted
}
```

## parse_decisions — source lines 80–80

Source context: callable `parse_decisions`; enclosing call `COUNTERS.bump`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s7/outcomes.py:80-80
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s7_dedup_parse_miss
}
```

## parse_decisions — source lines 84–84

Source context: callable `parse_decisions`; enclosing call `_errlog.log`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s7/outcomes.py:84-84
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: semantic-parse
}
```

## parse_decisions — source lines 85–85

Source context: callable `parse_decisions`; enclosing call `_errlog.log`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `n; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s7/outcomes.py:85-85
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: reply did not parse as dedup decisions (n=[dynamic source value: n; conversion=none; format_spec=none])
}
```

