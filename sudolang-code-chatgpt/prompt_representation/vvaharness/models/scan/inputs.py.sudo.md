# vvaharness/models/scan/inputs.py — model instruction carriers

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## to_prompt_block — source lines 80–85

Source context: callable `to_prompt_block`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `self.application_id; conversion=none; format_spec=none`
- `self.name or '(unnamed)'; conversion=none; format_spec=none`
- `'YES' if self.externally_facing else 'NO'; conversion=none; format_spec=none`
- `', '.join(sens) or 'standard'; conversion=none; format_spec=none`
- `self.source; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/models/scan/inputs.py:80-85
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: CMDB APPLICATION PROFILE:
}
```

```sudo
// Source: vvaharness/models/scan/inputs.py:80-85
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Application ID: [dynamic source value: self.application_id; conversion=none; format_spec=none]
}
```

```sudo
// Source: vvaharness/models/scan/inputs.py:80-85
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Name: [dynamic source value: self.name or '(unnamed)'; conversion=none; format_spec=none]
}
```

```sudo
// Source: vvaharness/models/scan/inputs.py:80-85
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Externally facing: [dynamic source value: 'YES' if self.externally_facing else 'NO'; conversion=none; format_spec=none]
}
```

```sudo
// Source: vvaharness/models/scan/inputs.py:80-85
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Data sensitivity: [dynamic source value: ', '.join(sens) or 'standard'; conversion=none; format_spec=none]
}
```

```sudo
// Source: vvaharness/models/scan/inputs.py:80-85
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Source: [dynamic source value: self.source; conversion=none; format_spec=none]
}
```

## to_prompt_block — source lines 76–76

Source context: callable `to_prompt_block`; enclosing call `sens.append`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/models/scan/inputs.py:76-76
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: PCI-scoped
}
```

## to_prompt_block — source lines 77–77

Source context: callable `to_prompt_block`; enclosing call `sens.append`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/models/scan/inputs.py:77-77
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: processes PAN
}
```

## to_prompt_block — source lines 78–78

Source context: callable `to_prompt_block`; enclosing call `sens.append`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/models/scan/inputs.py:78-78
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: handles PII
}
```

