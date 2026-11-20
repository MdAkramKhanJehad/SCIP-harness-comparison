# vvaharness/validation/tools/pattern_scanner.py — model instruction carriers

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
// Source: vvaharness/validation/tools/pattern_scanner.py:15-15
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Deterministic pattern scanner for validation subagents.
}
```

## pattern_scan — source lines 191–191

Source context: callable `pattern_scan`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/validation/tools/pattern_scanner.py:191-191
Constraints {
  The described operation advertises this return/result contract: bounded, secret-free match metadata followed by one scan summary; an unknown ``pattern_set`` returns a ``kind: "error"`` entry instead of raising.
}
```

