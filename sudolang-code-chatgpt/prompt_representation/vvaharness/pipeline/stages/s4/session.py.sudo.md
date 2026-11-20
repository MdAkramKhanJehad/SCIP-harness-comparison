# vvaharness/pipeline/stages/s4/session.py — model instruction carriers

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## _repair_prompt — source lines 188–192

Source context: callable `_repair_prompt`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `unit_id; conversion=repr; format_spec=none`
- `raw; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s4/session.py:188-192
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: REPAIR TASK: the previous reply was supposed to be a JSON object matching the InvestigationOutcome schema (unit_id, verdict, rationale, findings[]) but failed to parse.
  The requested model reply must contain ONLY the corrected JSON object. `unit_id` MUST be exactly [dynamic source value: unit_id; conversion=repr; format_spec=none].
  The request retains this source rule, criterion or rationale, with its original modal force: Preserve every finding and fact already present.
}
```

```sudo
// Source: vvaharness/pipeline/stages/s4/session.py:188-192
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: --- ORIGINAL REPLY --- [dynamic source value: raw; conversion=none; format_spec=none]
}
```

## tag — source lines 255–255

Source context: callable `_investigate_unit_once`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `unit.id; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s4/session.py:255-255
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s4 [dynamic source value: unit.id; conversion=none; format_spec=none]
}
```

## _batch_repair_prompt — source lines 381–385

Source context: callable `_batch_repair_prompt`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `unit_ids; conversion=none; format_spec=none`
- `raw; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s4/session.py:381-385
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: REPAIR TASK: the previous reply was supposed to be a JSON object {"outcomes": [...]} holding one InvestigationOutcome (unit_id, verdict, rationale, findings[]) for EACH of these units, but failed to parse.
  The requested model reply must contain ONLY the corrected JSON object.
  The request retains this source rule, criterion or rationale, with its original modal force: The `unit_id` values MUST be exactly these, one entry each: [dynamic source value: unit_ids; conversion=none; format_spec=none].
  The request retains this source rule, criterion or rationale, with its original modal force: Preserve every finding and fact already present.
}
```

```sudo
// Source: vvaharness/pipeline/stages/s4/session.py:381-385
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: --- ORIGINAL REPLY --- [dynamic source value: raw; conversion=none; format_spec=none]
}
```

## tag — source lines 407–407

Source context: callable `_batch_reply`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `len(batch); conversion=none; format_spec=none`
- `batch[0].id; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s4/session.py:407-407
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s4 batch[[dynamic source value: len(batch); conversion=none; format_spec=none]] [dynamic source value: batch[0].id; conversion=none; format_spec=none]
}
```

## limit — source lines 107–107

Source context: callable `_call_budget`; enclosing call `_cap_int`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/session.py:107-107
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: max_model_calls
}
```

## _tool_setup — source lines 166–166

Source context: callable `_tool_setup`; enclosing call `getattr`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/session.py:166-166
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: cwe_tools
}
```

## _replay_call — source lines 228–228

Source context: callable `_replay_call`; enclosing call `COUNTERS.bump`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/session.py:228-228
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s4_deadline_replay
}
```

## cap — source lines 342–342

Source context: callable `_cap_findings`; enclosing call `getattr`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/session.py:342-342
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: max_findings_per_run
}
```

## line_bucket — source lines 371–371

Source context: callable `investigate_unit`; enclosing call `getattr`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/session.py:371-371
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: line_bucket
}
```

## _batch_reply — source lines 457–457

Source context: callable `_batch_reply`; enclosing call `dispatch_or_retry_unforced`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `len(batch); conversion=none; format_spec=none`
- `batch[0].id; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s4/session.py:457-457
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: batch[[dynamic source value: len(batch); conversion=none; format_spec=none]] [dynamic source value: batch[0].id; conversion=none; format_spec=none]
}
```

## line_bucket — source lines 504–504

Source context: callable `investigate_batch`; enclosing call `getattr`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/session.py:504-504
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: line_bucket
}
```

## deepdive_tools — source lines 87–87

Source context: callable `deepdive_tools`; enclosing call `knob`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/session.py:87-87
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: step4.allowed_tools
}
```

## deepdive_tools — source lines 88–88

Source context: callable `deepdive_tools`; enclosing call `validate_detection_tools`; keyword `config_key`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/session.py:88-88
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: step4.allowed_tools
}
```

## _call_budget — source lines 112–112

Source context: callable `_call_budget`; enclosing call `ModelCallBudget`; keyword `counter`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/session.py:112-112
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s4_model_call_budget_final_turn
}
```

## declared — source lines 136–136

Source context: callable `_gate`; enclosing call `getattr`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/session.py:136-136
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: require_graph
}
```

## _gate — source lines 140–140

Source context: callable `_gate`; enclosing call `warn_once`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/session.py:140-140
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s4-require-graph
}
```

## _gate — source lines 141–144

Source context: callable `_gate`; enclosing call `warn_once`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/session.py:141-144
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: WARN [s4]: step4.require_graph is on but the code graph is absent or degenerate (zero edges, or fewer nodes than step0.min_graph_nodes_for_gate) — standing the graph-tool requirement down; the todo-list gate still applies.
}
```

## _gate — source lines 152–152

Source context: callable `_gate`; enclosing call `EvidenceGate`; keyword `counter`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/session.py:152-152
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s4_evidence_gate_rejected
}
```

## middleware — source lines 164–164

Source context: callable `_tool_setup`; enclosing call `_budget`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/session.py:164-164
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: graph_tool_budget
}
```

## middleware — source lines 165–165

Source context: callable `_tool_setup`; enclosing call `_budget`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/session.py:165-165
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s4_graph_tool_budget_exhausted
}
```

## _replay_call — source lines 235–235

Source context: callable `_replay_call`; enclosing call `_deepagents.dispatch_prompt`; keyword `tag`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `tag; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s4/session.py:235-235
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: tag; conversion=none; format_spec=none] replay
}
```

## _investigate_unit_once — source lines 312–313

Source context: callable `_investigate_unit_once`; enclosing call `console.write`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `unit.id; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s4/session.py:312-313
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [s4] [dynamic source value: unit.id; conversion=none; format_spec=none]: primary reply did not parse; attempting one bounded repair re-ask
}
```

## _investigate_unit_once — source lines 314–315

Source context: callable `_investigate_unit_once`; enclosing call `_errlog.log`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/session.py:314-315
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: primary reply did not parse as an InvestigationOutcome
}
```

## _investigate_unit_once — source lines 317–317

Source context: callable `_investigate_unit_once`; enclosing call `COUNTERS.bump`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/session.py:317-317
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s4_outcome_repaired_attempt
}
```

## _investigate_unit_once — source lines 334–335

Source context: callable `_investigate_unit_once`; enclosing call `RuntimeError`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `unit.id; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s4/session.py:334-335
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s4-deepdive: [dynamic source value: unit.id; conversion=none; format_spec=none]'s session reply did not parse as an InvestigationOutcome, even after repair
}
```

## _cap_findings — source lines 346–346

Source context: callable `_cap_findings`; enclosing call `COUNTERS.bump`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/session.py:346-346
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s4_findings_truncated
}
```

## _dedup_by_key — source lines 362–362

Source context: callable `_dedup_by_key`; enclosing call `COUNTERS.bump`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/session.py:362-362
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s4_unit_key_deduped
}
```

## investigate_unit — source lines 370–370

Source context: callable `investigate_unit`; enclosing call `RuntimeError`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/session.py:370-370
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: aborted by user (Ctrl-C)
}
```

## investigate_batch — source lines 472–473

Source context: callable `investigate_batch`; enclosing call `console.write`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `len(batch); conversion=none; format_spec=none`
- `batch[0].id; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s4/session.py:472-473
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [s4] batch[[dynamic source value: len(batch); conversion=none; format_spec=none]] [dynamic source value: batch[0].id; conversion=none; format_spec=none]: shared session reply did not parse; attempting one bounded repair re-ask
}
```

## investigate_batch — source lines 474–474

Source context: callable `investigate_batch`; enclosing call `_errlog.log`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `len(batch); conversion=none; format_spec=none`
- `batch[0].id; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s4/session.py:474-474
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: batch[[dynamic source value: len(batch); conversion=none; format_spec=none]] [dynamic source value: batch[0].id; conversion=none; format_spec=none]
}
```

## investigate_batch — source lines 475–475

Source context: callable `investigate_batch`; enclosing call `_errlog.log`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/session.py:475-475
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: shared session reply did not parse as InvestigationOutcomes
}
```

## investigate_batch — source lines 477–477

Source context: callable `investigate_batch`; enclosing call `COUNTERS.bump`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/session.py:477-477
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s4_batch_repaired_attempt
}
```

## investigate_batch — source lines 495–496

Source context: callable `investigate_batch`; enclosing call `RuntimeError`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `ids; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s4/session.py:495-496
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s4-deepdive: the shared session for [dynamic source value: ids; conversion=none; format_spec=none] returned no parseable InvestigationOutcomes, even after repair
}
```

## stats['merged_by_unit'] — source lines 510–510

Source context: callable `investigate_batch`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/session.py:510-510
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: merged_by_unit
}
```

## _gate — source lines 134–134

Source context: callable `_gate`; enclosing call `getattr`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/session.py:134-134
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: evidence_gate
}
```

## _gate — source lines 148–148

Source context: callable `_gate`; enclosing call `COUNTERS.bump`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/session.py:148-148
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: evidence_gate_stood_down_degenerate_graph
}
```

## _gate — source lines 151–151

Source context: callable `_gate`; enclosing call `_cap_int`; keyword `max_rejections`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/session.py:151-151
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: evidence_gate_refusals
}
```

## _tool_setup — source lines 169–169

Source context: callable `_tool_setup`; enclosing call `_budget`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/session.py:169-169
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: cwe_tool_budget
}
```

## _tool_setup — source lines 170–170

Source context: callable `_tool_setup`; enclosing call `_budget`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/session.py:170-170
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s4_cwe_tool_budget_exhausted
}
```

## _load_code — source lines 180–180

Source context: callable `_load_code`; enclosing call `getattr`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/session.py:180-180
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: inline_source
}
```

## _deadline_seconds — source lines 202–202

Source context: callable `_deadline_seconds`; enclosing call `knob`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/session.py:202-202
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: step4.deadline
}
```

## _deadline_bounded — source lines 218–219

Source context: callable `_deadline_bounded`; enclosing call `console.write`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `tag; conversion=none; format_spec=none`
- `seconds; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s4/session.py:218-219
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [s4] [dynamic source value: tag; conversion=none; format_spec=none]: deadline [dynamic source value: seconds; conversion=none; format_spec=none]s hit — resuming the session for its outcome
}
```

## _replay_call — source lines 236–236

Source context: callable `_replay_call`; enclosing call `_cap_int`; keyword `max_tokens`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/session.py:236-236
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: replay_max_tokens
}
```

## _replay_call — source lines 237–237

Source context: callable `_replay_call`; enclosing call `_cap_int`; keyword `timeout`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/session.py:237-237
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: replay_timeout
}
```

## initial — source lines 266–266

Source context: callable `_dispatch`; enclosing call `_cap_int`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/session.py:266-266
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: max_model_calls
}
```

## _investigate_unit_once — source lines 315–315

Source context: callable `_investigate_unit_once`; enclosing call `_errlog.log`; keyword `reason`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/session.py:315-315
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s4_outcome_repair_attempted
}
```

## repaired — source lines 324–324

Source context: callable `_investigate_unit_once`; enclosing call `_deepagents.dispatch_prompt`; keyword `tag`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `unit.id; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s4/session.py:324-324
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s4 [dynamic source value: unit.id; conversion=none; format_spec=none] json-repair
}
```

## _investigate_unit_once — source lines 332–332

Source context: callable `_investigate_unit_once`; enclosing call `COUNTERS.bump`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/session.py:332-332
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s4_outcome_repaired_ok
}
```

## code — source lines 400–400

Source context: callable `_batch_reply`; enclosing call `getattr`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/session.py:400-400
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: inline_source
}
```

## initial — source lines 419–419

Source context: callable `_dispatch`; enclosing call `_cap_int`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/session.py:419-419
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: max_model_calls
}
```

## investigate_batch — source lines 476–476

Source context: callable `investigate_batch`; enclosing call `_errlog.log`; keyword `reason`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/session.py:476-476
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s4_batch_repair_attempted
}
```

## repaired — source lines 484–484

Source context: callable `investigate_batch`; enclosing call `_deepagents.dispatch_prompt`; keyword `tag`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `len(batch); conversion=none; format_spec=none`
- `batch[0].id; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s4/session.py:484-484
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s4 batch[[dynamic source value: len(batch); conversion=none; format_spec=none]] [dynamic source value: batch[0].id; conversion=none; format_spec=none] json-repair
}
```

## investigate_batch — source lines 493–493

Source context: callable `investigate_batch`; enclosing call `COUNTERS.bump`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/session.py:493-493
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s4_batch_repaired_ok
}
```

## investigate_batch — source lines 513–513

Source context: callable `investigate_batch`; enclosing call `COUNTERS.bump`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `verdict; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s4/session.py:513-513
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s4_batch_member_[dynamic source value: verdict; conversion=none; format_spec=none]
}
```

## _agentic — source lines 297–297

Source context: callable `_agentic`; enclosing call `_cap_int`; keyword `max_turns`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/session.py:297-297
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: max_turns
}
```

## _agentic — source lines 450–450

Source context: callable `_agentic`; enclosing call `_cap_int`; keyword `max_turns`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/session.py:450-450
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: max_turns
}
```

## _deadline_bounded — source lines 222–222

Source context: callable `_deadline_bounded`; enclosing call `_cap_int`; keyword `timeout`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/session.py:222-222
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: resume_timeout
}
```

## _agentic — source lines 293–293

Source context: callable `_agentic`; enclosing call `knob`; keyword `max_output_tokens`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/session.py:293-293
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: step4.max_tokens
}
```

## repaired — source lines 326–326

Source context: callable `_investigate_unit_once`; enclosing call `knob`; keyword `max_tokens`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/session.py:326-326
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: step4.max_tokens
}
```

## _agentic — source lines 446–446

Source context: callable `_agentic`; enclosing call `knob`; keyword `max_output_tokens`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/session.py:446-446
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: step4.max_tokens
}
```

## repaired — source lines 486–486

Source context: callable `investigate_batch`; enclosing call `knob`; keyword `max_tokens`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/session.py:486-486
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: step4.max_tokens
}
```

