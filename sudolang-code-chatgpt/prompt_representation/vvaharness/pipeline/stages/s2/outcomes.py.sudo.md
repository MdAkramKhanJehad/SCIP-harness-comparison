# vvaharness/pipeline/stages/s2/outcomes.py — model instruction carriers

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## t.id — source lines 45–45

Source context: callable `_finalize_threats`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `i; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s2/outcomes.py:45-45
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: T[dynamic source value: i; conversion=none; format_spec=none]
}
```

## _finalize_threats — source lines 56–57

Source context: callable `_finalize_threats`; enclosing call `console.write`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `emitted - len(dropped); conversion=none; format_spec=none`
- `emitted; conversion=none; format_spec=none`
- `len(tm.threats); conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s2/outcomes.py:56-57
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [s2] surface_files: [dynamic source value: emitted - len(dropped); conversion=none; format_spec=none] of [dynamic source value: emitted; conversion=none; format_spec=none] path(s) across [dynamic source value: len(tm.threats); conversion=none; format_spec=none] threat(s) resolved to an in-scope file
}
```

## _finalize_threats — source lines 60–60

Source context: callable `_finalize_threats`; enclosing call `COUNTERS.bump`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s2/outcomes.py:60-60
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s2_surface_files_dropped
}
```

## _OUTPUT_CAPS — source lines 75–75

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s2/outcomes.py:75-75
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: max_threats
}
```

## _OUTPUT_CAPS — source lines 76–76

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s2/outcomes.py:76-76
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: max_assets
}
```

## _OUTPUT_CAPS — source lines 76–76

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s2/outcomes.py:76-76
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s2_assets_truncated
}
```

## _OUTPUT_CAPS — source lines 77–77

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s2/outcomes.py:77-77
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: trust_boundaries
}
```

## _OUTPUT_CAPS — source lines 77–77

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s2/outcomes.py:77-77
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: max_trust_boundaries
}
```

## _OUTPUT_CAPS — source lines 77–77

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s2/outcomes.py:77-77
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s2_trust_boundaries_truncated
}
```

## _parse_threat_model — source lines 38–40

Source context: callable `_parse_threat_model`; enclosing call `ValueError`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `sorted(data.keys())[:8]; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s2/outcomes.py:38-40
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: extracted JSON object has none of the threat-model fields (got keys: [dynamic source value: sorted(data.keys())[:8]; conversion=none; format_spec=none]) — likely a sub-object of a truncated or malformed response
}
```

## _finalize_threats — source lines 68–69

Source context: callable `_finalize_threats`; enclosing call `_errlog.log`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s2/outcomes.py:68-69
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: every surface_files path was rejected — no threat keeps a validated surface; s3 will mint no investigation unit
}
```

## _warn_output_caps — source lines 91–91

Source context: callable `_warn_output_caps`; enclosing call `log.warning`; keyword `cap`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `key; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s2/outcomes.py:91-91
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: step2.[dynamic source value: key; conversion=none; format_spec=none]
}
```

