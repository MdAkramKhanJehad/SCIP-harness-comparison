# vvaharness/models/remediation.py — model instruction carriers

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## _REPORT_ONLY — source lines 28–28

Source context: callable `<module>`; enclosing call `frozenset`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

```sudo
// Source: vvaharness/models/remediation.py:28-28
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: report-only
}
```

## file — source lines 37–37

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/models/remediation.py:37-37
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: repo-relative path that was edited
}
```

## summary — source lines 38–38

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/models/remediation.py:38-38
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: what changed and why
}
```

## kind — source lines 47–47

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/models/remediation.py:47-47
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: what the engine did
}
```

## summary — source lines 48–48

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/models/remediation.py:48-48
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: human-readable account of the attempt
}
```

## disposition — source lines 50–50

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/models/remediation.py:50-50
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: why nothing was applied; required when kind is no_action
}
```

## diff — source lines 53–53

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/models/remediation.py:53-53
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: unified diff, when the engine produced one
}
```

## files_touched — source lines 54–54

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/models/remediation.py:54-54
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: advisory list of edits
}
```

## changes — source lines 55–55

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/models/remediation.py:55-55
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: per-file rationale
}
```

## gates — source lines 56–56

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/models/remediation.py:56-56
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: evidence gates asserted
}
```

## root_cause — source lines 57–57

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/models/remediation.py:57-57
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: why the vulnerability existed
}
```

## remaining_risks — source lines 58–58

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/models/remediation.py:58-58
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: what the fix does not cover
}
```

## recommendations — source lines 59–59

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/models/remediation.py:59-59
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: code-level follow-ups
}
```

## external_ref — source lines 60–60

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/models/remediation.py:60-60
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: pull-request URL, for engines that open one
}
```

## produced_by — source lines 61–61

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/models/remediation.py:61-61
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: attributable origin
}
```

## outcome — source lines 78–78

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/models/remediation.py:78-78
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: what the engine claims it achieved
}
```

## summary — source lines 79–79

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/models/remediation.py:79-79
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: human-readable account of the attempt
}
```

## root_cause — source lines 80–80

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/models/remediation.py:80-80
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: why the vulnerability existed
}
```

## changes — source lines 81–81

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/models/remediation.py:81-81
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: per-file rationale
}
```

## gates — source lines 82–82

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/models/remediation.py:82-82
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: evidence gates asserted
}
```

## remaining_risks — source lines 83–83

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/models/remediation.py:83-83
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: what the fix does not cover
}
```

## recommendations — source lines 84–84

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/models/remediation.py:84-84
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: code-level follow-ups
}
```

## produced_by — source lines 85–85

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/models/remediation.py:85-85
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: attributable origin
}
```

