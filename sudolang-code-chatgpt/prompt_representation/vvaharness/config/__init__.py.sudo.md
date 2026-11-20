# vvaharness/config/__init__.py — model instruction carriers

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## _check_refusal_retries — source lines 914–915

Source context: callable `_check_refusal_retries`; enclosing call `ConfigPolicyError`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `p; conversion=none; format_spec=none`
- `_REFUSAL_RETRIES_MAX; conversion=none; format_spec=none`
- `value; conversion=repr; format_spec=none`

```sudo
// Source: vvaharness/config/__init__.py:914-915
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: config [dynamic source value: p; conversion=none; format_spec=none]: refusal_retries must be an integer from 0 to [dynamic source value: _REFUSAL_RETRIES_MAX; conversion=none; format_spec=none] (got [dynamic source value: value; conversion=repr; format_spec=none]); each extra resend repeats a prompt the model already refused
}
```

## _require_overlay_trust — source lines 739–743

Source context: callable `_require_overlay_trust`; enclosing call `ConfigPolicyError`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `local; conversion=none; format_spec=none`
- `local; conversion=none; format_spec=none`
- `NO_LOCAL_CONFIG_ENV; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/config/__init__.py:739-743
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: config overlay [dynamic source value: local; conversion=none; format_spec=none] is not trusted: it must be owned by the invoking user (or root) and not group/world-writable.
  The request retains this source rule, criterion or rationale, with its original modal force: Fix with `chmod go-w [dynamic source value: local; conversion=none; format_spec=none]` (and `chown` it to yourself if needed), or set [dynamic source value: NO_LOCAL_CONFIG_ENV; conversion=none; format_spec=none] to skip the overlay.
}
```

## _local_overlay — source lines 763–763

Source context: callable `_local_overlay`; enclosing call `ValueError`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `local; conversion=none; format_spec=none`
- `type(over).__name__; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/config/__init__.py:763-763
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: config [dynamic source value: local; conversion=none; format_spec=none] must be a YAML mapping, got [dynamic source value: type(over).__name__; conversion=none; format_spec=none]
}
```

## read_primary — source lines 864–864

Source context: callable `read_primary`; enclosing call `ConfigPathError`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `p; conversion=none; format_spec=none`
- `type(raw).__name__; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/config/__init__.py:864-864
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: config [dynamic source value: p; conversion=none; format_spec=none] must be a YAML mapping, got [dynamic source value: type(raw).__name__; conversion=none; format_spec=none]
}
```

## apply_step1_overlay — source lines 981–982

Source context: callable `apply_step1_overlay`; enclosing call `ValueError`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `p; conversion=repr; format_spec=none`

```sudo
// Source: vvaharness/config/__init__.py:981-982
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: step1 overlay must be a local path; refusing network/UNC path [dynamic source value: p; conversion=repr; format_spec=none] (reading it could leak credentials over SMB)
}
```

## apply_step1_overlay — source lines 1002–1002

Source context: callable `apply_step1_overlay`; enclosing call `ValueError`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `p; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/config/__init__.py:1002-1002
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: step1 overlay [dynamic source value: p; conversion=none; format_spec=none] must be a YAML mapping
}
```

