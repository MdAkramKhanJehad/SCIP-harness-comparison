# vvaharness/rules/kb_tools.py — model instruction carriers

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
// Source: vvaharness/rules/kb_tools.py:15-15
Constraints {
  The advertised description supplied with this operation is a model-visible claim: The CWE knowledge base as a fact tool, composed via ``compose_tool_builders``.
}
```

## _note_unknown_cwe — source lines 34–34

Source context: callable `_note_unknown_cwe`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/rules/kb_tools.py:34-34
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Record *cwe_id* among this run's KB misses, as the comma-joined `note` fact.
}
```

## CweGuidance — source lines 47–47

Source context: callable `CweGuidance`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/rules/kb_tools.py:47-47
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Sanitizers, non-sanitizers and FP checks known for one CWE id, e.g. 'CWE-89'.
}
```

## build_kb_tool_builder — source lines 59–59

Source context: callable `build_kb_tool_builder`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/rules/kb_tools.py:59-59
Constraints {
  The described operation advertises this return/result contract: a ``ToolBuilder`` contributing ``CweGuidance`` when fact-gated in.
}
```

## CweGuidance — source lines 49–49

Source context: callable `CweGuidance`; enclosing call `COUNTERS.bump`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/rules/kb_tools.py:49-49
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s4_cwe_guidance_called
}
```

## CweGuidance — source lines 53–53

Source context: callable `CweGuidance`; enclosing call `COUNTERS.bump`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/rules/kb_tools.py:53-53
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s4_cwe_guidance_unknown_cwe
}
```

