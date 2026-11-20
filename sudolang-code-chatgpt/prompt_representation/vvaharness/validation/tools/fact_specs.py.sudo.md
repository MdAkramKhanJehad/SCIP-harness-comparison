# vvaharness/validation/tools/fact_specs.py — model instruction carriers

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## <module> — source lines 15–15

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/validation/tools/fact_specs.py:15-15
Constraints {
  The advertised description supplied with this operation is a model-visible claim: S11's five fact tools as backend-neutral :class:`FactToolSpec`s.
}
```

## build_validation_fact_specs — source lines 53–53

Source context: callable `build_validation_fact_specs`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/validation/tools/fact_specs.py:53-53
Constraints {
  The advertised description supplied with this operation is a model-visible claim: The five S11 fact tools, bound to *workspace* (the staged diff + sources).
}
```

## _impact — source lines 95–95

Source context: callable `_impact`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/validation/tools/fact_specs.py:95-95
Constraints {
  The advertised description supplied with this operation is a model-visible claim: DiffImpactMap's payload, shaped exactly as the deepagents tool returns it.
}
```

## __all__ — source lines 103–103

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/validation/tools/fact_specs.py:103-103
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: build_validation_fact_specs
}
```

## _FILE_PATH_SCHEMA — source lines 37–37

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/validation/tools/fact_specs.py:37-37
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: file_path
}
```

## _FILE_PATH_SCHEMA — source lines 39–39

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/validation/tools/fact_specs.py:39-39
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: file_path
}
```

## _PATTERN_SET_SCHEMA — source lines 44–44

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/validation/tools/fact_specs.py:44-44
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: pattern_set
}
```

## _PATTERN_SET_SCHEMA — source lines 48–48

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/validation/tools/fact_specs.py:48-48
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: pattern_set
}
```

## _impact — source lines 98–98

Source context: callable `_impact`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/validation/tools/fact_specs.py:98-98
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: files_changed
}
```

## _impact — source lines 99–99

Source context: callable `_impact`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/validation/tools/fact_specs.py:99-99
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: trust_boundary_touched
}
```

## _FILE_PATH_SCHEMA — source lines 38–38

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/validation/tools/fact_specs.py:38-38
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Repo-relative path.
}
```

## _PATTERN_SET_SCHEMA — source lines 46–46

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/validation/tools/fact_specs.py:46-46
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Builtin set: "secret_exposure" or "insecure_value".
}
```

## build_validation_fact_specs — source lines 57–58

Source context: callable `build_validation_fact_specs`; enclosing call `FactToolSpec`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/validation/tools/fact_specs.py:57-58
Constraints {
  The requested model reply must contain whether *file_path* is in diff.patch and its changed line ranges.
}
```

## build_validation_fact_specs — source lines 64–64

Source context: callable `build_validation_fact_specs`; enclosing call `FactToolSpec`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/validation/tools/fact_specs.py:64-64
Constraints {
  The requested model reply must contain added line ranges for *file_path* from diff.patch.
}
```

## build_validation_fact_specs — source lines 70–71

Source context: callable `build_validation_fact_specs`; enclosing call `FactToolSpec`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/validation/tools/fact_specs.py:70-71
Constraints {
  The requested model reply must contain files changed by diff.patch and whether a trust boundary was touched.
}
```

## build_validation_fact_specs — source lines 77–80

Source context: callable `build_validation_fact_specs`; enclosing call `FactToolSpec`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/validation/tools/fact_specs.py:77-80
Constraints {
  The requested model reply must contain bounded, secret-free match metadata and a scan summary.
  The request retains this source rule, criterion or rationale, with its original modal force: Builtin sets: "secret_exposure", "insecure_value".
  The request retains this source rule, criterion or rationale, with its original modal force: The final item reports counts, limits, and whether results were truncated.
}
```

## build_validation_fact_specs — source lines 86–87

Source context: callable `build_validation_fact_specs`; enclosing call `FactToolSpec`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/validation/tools/fact_specs.py:86-87
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Inventory test files and detect negative/adversarial test markers.
}
```

