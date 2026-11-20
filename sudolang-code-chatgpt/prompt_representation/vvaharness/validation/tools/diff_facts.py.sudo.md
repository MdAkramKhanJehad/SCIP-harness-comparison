# vvaharness/validation/tools/diff_facts.py — model instruction carriers

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
// Source: vvaharness/validation/tools/diff_facts.py:15-15
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Deterministic, read-only diff fact tools for validation subagents.
}
```

## <module> — source lines 50–50

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/validation/tools/diff_facts.py:50-50
Constraints {
  The advertised description supplied with this operation is a model-visible claim: One file's added line ranges, as parsed out of a unified diff.
}
```

## <module> — source lines 57–57

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/validation/tools/diff_facts.py:57-57
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Feed unified-diff lines in order, then call ``finish()`` for per-file changes.
}
```

## parse_diff_patch — source lines 122–122

Source context: callable `parse_diff_patch`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/validation/tools/diff_facts.py:122-122
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Parse ``diff.patch`` into per-file changes (added line ranges + deletion flag); ``errors="replace"`` so a non-UTF-8 byte can't kill the session over line-oriented markup.
}
```

## diff_touched — source lines 133–133

Source context: callable `diff_touched`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/validation/tools/diff_facts.py:133-133
Constraints {
  The described operation advertises this return/result contract: whether *file_path* is in ``diff.patch`` and which lines were added.
}
```

## changed_lines — source lines 141–141

Source context: callable `changed_lines`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/validation/tools/diff_facts.py:141-141
Constraints {
  The described operation advertises this return/result contract: added line ranges for *file_path* from ``diff.patch``.
}
```

## <module> — source lines 147–147

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/validation/tools/diff_facts.py:147-147
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Which files a diff changed, and whether any of them is a trust boundary.
}
```

## build_diff_impact_map — source lines 154–154

Source context: callable `build_diff_impact_map`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/validation/tools/diff_facts.py:154-154
Constraints {
  The described operation is advertised for list changed files and whether any is a trust-boundary path (auth/session/crypto/...).; this description alone does not request its invocation.
}
```

