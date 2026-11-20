# vvaharness/pipeline/stages/s6/session.py — model instruction carriers

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## _VERDICT_TOKENS — source lines 79–79

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s6/session.py:79-79
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: TRUE_POSITIVE
}
```

## _VERDICT_TOKENS — source lines 79–79

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s6/session.py:79-79
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: FALSE_POSITIVE
}
```

## tag — source lines 304–304

Source context: callable `verify_batch`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `len(items); conversion=none; format_spec=none`
- `ids[0]; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s6/session.py:304-304
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s6 verify[[dynamic source value: len(items); conversion=none; format_spec=none]] [dynamic source value: ids[0]; conversion=none; format_spec=none]
}
```

## repair_tag — source lines 338–338

Source context: callable `verify_batch`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `tag; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s6/session.py:338-338
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: tag; conversion=none; format_spec=none] json-repair
}
```

## limit — source lines 113–113

Source context: callable `_call_budget`; enclosing call `_cap_int`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s6/session.py:113-113
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: max_model_calls
}
```

## _replay_leg — source lines 229–229

Source context: callable `_replay_leg`; enclosing call `COUNTERS.bump`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s6/session.py:229-229
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s6_deadline_replay
}
```

## _replay_leg — source lines 246–246

Source context: callable `_replay_leg`; enclosing call `console.write`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `tag; conversion=none; format_spec=none`
- `time.monotonic() - started; conversion=none; format_spec=f'.1f'`

```sudo
// Source: vvaharness/pipeline/stages/s6/session.py:246-246
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [s6-verify] [dynamic source value: tag; conversion=none; format_spec=none]: replay returned in [dynamic source value: time.monotonic() - started; conversion=none; format_spec=f'.1f']s
}
```

## verify_batch — source lines 336–336

Source context: callable `verify_batch`; enclosing call `COUNTERS.bump`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s6/session.py:336-336
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s6_outcome_repaired_attempt
}
```

## _graph_enabled — source lines 96–96

Source context: callable `_graph_enabled`; enclosing call `getattr`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s6/session.py:96-96
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: graph_tools
}
```

## _graph_enabled — source lines 104–107

Source context: callable `_graph_enabled`; enclosing call `warn_once`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `reason; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s6/session.py:104-107
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: WARN [s6]: step6_verify.graph_tools is on but [dynamic source value: reason; conversion=none; format_spec=none] — verifying without the graph tools, and NOT telling the model about tools it cannot call.
  The request retains this source rule, criterion or rationale, with its original modal force: Route models.verify via: deepagents, sdk or openai to use them.
}
```

## _call_budget — source lines 119–119

Source context: callable `_call_budget`; enclosing call `ModelCallBudget`; keyword `counter`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s6/session.py:119-119
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s6_model_call_budget_final_turn
}
```

## limit — source lines 138–138

Source context: callable `_tool_setup`; enclosing call `_cap_int`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s6/session.py:138-138
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: graph_tool_budget
}
```

## _tool_setup — source lines 143–143

Source context: callable `_tool_setup`; enclosing call `getattr`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s6/session.py:143-143
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: require_graph
}
```

## _load_code — source lines 166–166

Source context: callable `_load_code`; enclosing call `getattr`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s6/session.py:166-166
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: inline_source
}
```

## _effort — source lines 184–184

Source context: callable `_effort`; enclosing call `knob`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s6/session.py:184-184
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: step6_verify.effort
}
```

## out — source lines 240–240

Source context: callable `_replay_leg`; enclosing call `_deepagents.dispatch_prompt`; keyword `tag`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `tag; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s6/session.py:240-240
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: tag; conversion=none; format_spec=none] replay
}
```

## verify_batch — source lines 325–325

Source context: callable `verify_batch`; enclosing call `COUNTERS.bump`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s6/session.py:325-325
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s6_outcome_repair_skipped_abandoned
}
```

## verify_batch — source lines 329–331

Source context: callable `verify_batch`; enclosing call `console.write`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `tag; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s6/session.py:329-331
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [s6-verify] [dynamic source value: tag; conversion=none; format_spec=none]: primary reply had no verdict material; skipping the repair re-ask (it can only restate a verdict that was never reached)
}
```

## verify_batch — source lines 332–332

Source context: callable `verify_batch`; enclosing call `_errlog.log`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s6/session.py:332-332
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: primary reply had no verdict material
}
```

## verify_batch — source lines 334–334

Source context: callable `verify_batch`; enclosing call `COUNTERS.bump`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s6/session.py:334-334
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s6_outcome_repair_skipped_no_verdict
}
```

## verify_batch — source lines 354–354

Source context: callable `verify_batch`; enclosing call `COUNTERS.bump`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s6/session.py:354-354
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s6_outcome_repaired_ok
}
```

## deadline — source lines 204–204

Source context: callable `_dispatch`; enclosing call `knob`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s6/session.py:204-204
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: step6_verify.batch_deadline
}
```

## _dispatch — source lines 212–213

Source context: callable `_dispatch`; enclosing call `console.write`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `tag; conversion=none; format_spec=none`
- `deadline; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s6/session.py:212-213
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [s6-verify] [dynamic source value: tag; conversion=none; format_spec=none]: deadline [dynamic source value: deadline; conversion=none; format_spec=none]s hit — resuming the session for the verdicts
}
```

## verify_batch — source lines 333–333

Source context: callable `verify_batch`; enclosing call `_errlog.log`; keyword `reason`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s6/session.py:333-333
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s6_outcome_repair_skipped_no_verdict
}
```

## _tool_setup — source lines 148–148

Source context: callable `_tool_setup`; enclosing call `warn_once`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s6/session.py:148-148
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s6-require-graph
}
```

## _tool_setup — source lines 149–152

Source context: callable `_tool_setup`; enclosing call `warn_once`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s6/session.py:149-152
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: WARN [s6]: step6_verify.require_graph is on but the code graph is absent or degenerate (zero edges, or fewer nodes than step0.min_graph_nodes_for_gate) — standing the graph-tool requirement down.
}
```

## _tool_setup — source lines 153–153

Source context: callable `_tool_setup`; enclosing call `COUNTERS.bump`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s6/session.py:153-153
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: evidence_gate_stood_down_degenerate_graph
}
```

## out — source lines 241–241

Source context: callable `_replay_leg`; enclosing call `knob`; keyword `max_tokens`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s6/session.py:241-241
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: step6_verify.replay_max_tokens
}
```

## out — source lines 242–242

Source context: callable `_replay_leg`; enclosing call `knob`; keyword `timeout`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s6/session.py:242-242
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: step6_verify.replay_timeout
}
```

## _agentic_leg — source lines 280–280

Source context: callable `_agentic_leg`; enclosing call `getattr`; keyword `max_budget_usd`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s6/session.py:280-280
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: max_budget_usd
}
```

## _agentic_leg — source lines 281–281

Source context: callable `_agentic_leg`; enclosing call `getattr`; keyword `max_turns`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s6/session.py:281-281
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: max_turns
}
```

## _tool_setup — source lines 142–142

Source context: callable `_tool_setup`; enclosing call `ToolCallBudget`; keyword `counter`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s6/session.py:142-142
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s6_graph_tool_budget_exhausted
}
```

## _tool_setup — source lines 157–157

Source context: callable `_tool_setup`; enclosing call `EvidenceGate`; keyword `counter`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s6/session.py:157-157
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s6_evidence_gate_rejected
}
```

## _dispatch — source lines 221–221

Source context: callable `_dispatch`; enclosing call `_cap_int`; keyword `timeout`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s6/session.py:221-221
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: resume_timeout
}
```

## _agentic_leg — source lines 286–286

Source context: callable `_agentic_leg`; enclosing call `knob`; keyword `max_output_tokens`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s6/session.py:286-286
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: step6_verify.max_tokens
}
```

## repaired — source lines 349–349

Source context: callable `verify_batch`; enclosing call `knob`; keyword `max_tokens`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s6/session.py:349-349
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: step6_verify.max_tokens
}
```

## _tool_setup — source lines 156–156

Source context: callable `_tool_setup`; enclosing call `_cap_int`; keyword `max_rejections`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s6/session.py:156-156
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: evidence_gate_refusals
}
```

## _agentic_leg — source lines 270–270

Source context: callable `_agentic_leg`; enclosing call `knob`; keyword `trait_stamps`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s6/session.py:270-270
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: step6_verify.trait_stamps
}
```

## _agentic_leg — source lines 271–271

Source context: callable `_agentic_leg`; enclosing call `knob`; keyword `reframe`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s6/session.py:271-271
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: step6_verify.reframe_enabled
}
```

## _agentic_leg — source lines 289–289

Source context: callable `_agentic_leg`; enclosing call `knob`; keyword `timeout`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s6/session.py:289-289
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: step6_verify.batch_deadline
}
```

