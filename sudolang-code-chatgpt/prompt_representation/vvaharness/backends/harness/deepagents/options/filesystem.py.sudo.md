# vvaharness/backends/harness/deepagents/options/filesystem.py — model instruction carriers

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## _WRITE_REFUSED — source lines 84–84

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/harness/deepagents/options/filesystem.py:84-84
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: write operations are disabled on detection sessions: {path}
}
```

## _GIT_WRITE_REFUSED — source lines 250–250

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/harness/deepagents/options/filesystem.py:250-250
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: writes into version-control metadata (.git) are refused: {path}
}
```

## msg — source lines 343–343

Source context: callable `_skill_sources`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `root; conversion=none; format_spec=none`
- `base; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/harness/deepagents/options/filesystem.py:343-343
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: skill_root [dynamic source value: root; conversion=none; format_spec=none] must live under the session cwd [dynamic source value: base; conversion=none; format_spec=none]
}
```

## _filesystem_permissions — source lines 66–66

Source context: callable `_filesystem_permissions`; enclosing call `ValueError`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `raw; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/harness/deepagents/options/filesystem.py:66-66
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: writable path escapes harness cwd: [dynamic source value: raw; conversion=none; format_spec=none]
}
```

