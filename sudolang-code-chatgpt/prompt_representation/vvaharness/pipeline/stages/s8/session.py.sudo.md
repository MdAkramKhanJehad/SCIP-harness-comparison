# vvaharness/pipeline/stages/s8/session.py — model instruction carriers

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## _REPAIRABLE_RX — source lines 54–54

Source context: callable `<module>`; enclosing call `re.compile`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/session.py:54-54
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: \b(ranked_findings|chains)"?\s*(?::|=|\bis\b)\s*[\[{]
}
```

## limit — source lines 62–62

Source context: callable `_call_budget`; enclosing call `_cap_int`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/session.py:62-62
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: max_model_calls
}
```

## _replay_max_tokens — source lines 100–100

Source context: callable `_replay_max_tokens`; enclosing call `_cap_int`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/session.py:100-100
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: replay_max_tokens
}
```

## _call_budget — source lines 67–67

Source context: callable `_call_budget`; enclosing call `ModelCallBudget`; keyword `counter`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/session.py:67-67
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s8_model_call_budget_final_turn
}
```

## effort — source lines 74–74

Source context: callable `_agentic_leg`; enclosing call `knob`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/session.py:74-74
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: step8.effort
}
```

## _replay_leg — source lines 129–129

Source context: callable `_replay_leg`; enclosing call `_cold_call`; keyword `tag`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `TAG; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s8/session.py:129-129
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: TAG; conversion=none; format_spec=none] replay
}
```

## repair_call — source lines 146–146

Source context: callable `repair_call`; enclosing call `_cold_call`; keyword `tag`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `TAG; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s8/session.py:146-146
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: TAG; conversion=none; format_spec=none] json-repair
}
```

## effort — source lines 153–153

Source context: callable `chain_call`; enclosing call `knob`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/session.py:153-153
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: step8.effort
}
```

## _agentic_leg — source lines 84–84

Source context: callable `_agentic_leg`; enclosing call `_cap_int`; keyword `max_turns`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/session.py:84-84
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: max_turns
}
```

## _agentic_leg — source lines 87–87

Source context: callable `_agentic_leg`; enclosing call `knob`; keyword `max_output_tokens`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/session.py:87-87
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: step8.max_tokens
}
```

## _cold_call — source lines 117–117

Source context: callable `_cold_call`; enclosing call `_cap_int`; keyword `timeout`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/session.py:117-117
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: replay_timeout
}
```

## _dispatch — source lines 177–178

Source context: callable `_dispatch`; enclosing call `console.write`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `deadline; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s8/session.py:177-178
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [s8] deadline [dynamic source value: deadline; conversion=none; format_spec=none]s hit — replaying the chain analysis from the transcript
}
```

