# vvaharness/validation/session/launcher.py — model instruction carriers

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## Host-versus-model synthesis instruction branches

Structured view of the same source instructions, not an additional pass or an assertion of model compliance.

```sudo
// Source: vvaharness/validation/session/launcher.py:374-394
if (the source capability returns schema-validated reports) {
  Constraints { The model is asked not to synthesize, score or fill synthesized_gates; emit [] and let the host synthesize/score after the session. }
} else {
  Constraints {
    The model is asked to provide all four synthesized gates per finding using the supplied agreement/single-vote/conservative-disagreement rules.
    Scores/fix_status/merge_readiness are not requested as authoritative: the host recomputes them and ignores supplied values.
  }
}
These are branch-selected model requests. They coexist with older rule-file scoring language; executable host scoring is separately represented.
```

## _STRUCTURED_RETRY_SUBTYPE — source lines 412–412

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/validation/session/launcher.py:412-412
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: error_max_structured_output_retries
}
```

## _DEFAULT_VALIDATE_ENV_VARS — source lines 104–104

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/validation/session/launcher.py:104-104
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: ANTHROPIC_BASE_URL
}
```

## _DEFAULT_VALIDATE_ENV_VARS — source lines 105–105

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/validation/session/launcher.py:105-105
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: OPENAI_API_KEY
}
```

## _DEFAULT_VALIDATE_ENV_VARS — source lines 106–106

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/validation/session/launcher.py:106-106
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: OPENAI_BASE_URL
}
```

## _rules_section — source lines 363–365

Source context: callable `_rules_section`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `orchestrator_rules_text(); conversion=none; format_spec=none`

## Rules

```sudo
// Source: vvaharness/validation/session/launcher.py:363-365
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: These are the validation rules referred to above.
  The model is asked to adopt them as written.
}
```

```sudo
// Source: vvaharness/validation/session/launcher.py:363-365
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: orchestrator_rules_text(); conversion=none; format_spec=none]
}
```

## _synthesis_section — source lines 385–393

Source context: callable `_synthesis_section`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

## Synthesis boundary

```sudo
// Source: vvaharness/validation/session/launcher.py:385-393
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Fill `synthesized_gates` with one entry per finding, each carrying all four gates, applying the synthesis rules from the validation rules above: where two or more personas agree on a gate use that status; where only one evaluated it use that status; where they disagree take the LOWEST (most conservative) status and show both perspectives in the model's justification.
}
```

```sudo
// Source: vvaharness/validation/session/launcher.py:385-393
Constraints {
  The requested model behavior excludes compute scores. `raw_score`, `fix_status` and `merge_readiness` are recomputed on the host from the gate statuses you report, and the values you put in those fields are ignored.
}
```

## _load_system_prompt — source lines 406–408

Source context: callable `_load_system_prompt`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `path.read_text().rstrip(); conversion=none; format_spec=none`
- `_synthesis_section(config); conversion=none; format_spec=none`
- `_rules_section(config); conversion=none; format_spec=none`

```sudo
// Source: vvaharness/validation/session/launcher.py:406-408
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: path.read_text().rstrip(); conversion=none; format_spec=none]
}
```

```sudo
// Source: vvaharness/validation/session/launcher.py:406-408
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: _synthesis_section(config); conversion=none; format_spec=none]
}
```

```sudo
// Source: vvaharness/validation/session/launcher.py:406-408
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: _rules_section(config); conversion=none; format_spec=none]
}
```

## _resolve_binary — source lines 210–211

Source context: callable `_resolve_binary`; enclosing call `HarnessCLINotFoundError`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `binary; conversion=repr; format_spec=none`

```sudo
// Source: vvaharness/validation/session/launcher.py:210-211
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Claude binary [dynamic source value: binary; conversion=repr; format_spec=none] not found on an absolute, non-cwd PATH entry; configure agent.binary with an absolute installed executable path
}
```

## tmp — source lines 217–217

Source context: callable `_write_workspace_json`; enclosing call `dest.with_suffix`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `dest.suffix; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/validation/session/launcher.py:217-217
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: dest.suffix; conversion=none; format_spec=none].tmp
}
```

## gates — source lines 236–236

Source context: callable `_write_validation_outputs`; enclosing call `structured.get`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/validation/session/launcher.py:236-236
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: synthesized_gates
}
```

## target_status — source lines 237–237

Source context: callable `_write_validation_outputs`; enclosing call `structured.get`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/validation/session/launcher.py:237-237
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: target_jira_status
}
```

## _rules_section — source lines 357–360

Source context: callable `_rules_section`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

## Rules

```sudo
// Source: vvaharness/validation/session/launcher.py:357-360
Constraints {
  The model is asked to adopt the rules auto-loaded from `.claude/rules/`.
  The request retains this source rule, criterion or rationale, with its original modal force: They define persona isolation, anti-manipulation safeguards, evidence requirements, gate definitions, weights, and decision thresholds.
}
```

## _synthesis_section — source lines 378–382

Source context: callable `_synthesis_section`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

## Synthesis boundary

```sudo
// Source: vvaharness/validation/session/launcher.py:378-382
Constraints {
  The requested model behavior excludes synthesize across personas, compute scores, or fill `synthesized_gates` — the host performs deterministic synthesis and scoring from the structured persona reports after you finish.
  The request retains this source rule, criterion or rationale, with its original modal force: Always emit `synthesized_gates` as an empty list `[]`.
}
```

## prompt_file — source lines 399–399

Source context: callable `_load_system_prompt`; enclosing call `getattr`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/validation/session/launcher.py:399-399
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: system_prompt_file
}
```

## _failure_reason — source lines 418–418

Source context: callable `_failure_reason`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `exit_code; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/validation/session/launcher.py:418-418
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: validation session produced no terminal result (exit=[dynamic source value: exit_code; conversion=none; format_spec=none])
}
```

## parts — source lines 419–419

Source context: callable `_failure_reason`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `terminal.subtype; conversion=repr; format_spec=none`

```sudo
// Source: vvaharness/validation/session/launcher.py:419-419
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: validation session ended with subtype=[dynamic source value: terminal.subtype; conversion=repr; format_spec=none]
}
```

## _run_and_check — source lines 576–576

Source context: callable `_run_and_check`; enclosing call `log.debug`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/validation/session/launcher.py:576-576
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Session %s completed (observed_sid=%s)
}
```

## launch_session — source lines 616–616

Source context: callable `launch_session`; enclosing call `log.info`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/validation/session/launcher.py:616-616
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Launching validation session %s for %s in %s
}
```

## status — source lines 136–136

Source context: callable `_heartbeat_ticker`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/validation/session/launcher.py:136-136
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: waiting on model
}
```

## status — source lines 136–136

Source context: callable `_heartbeat_ticker`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/validation/session/launcher.py:136-136
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: in progress
}
```

## _heartbeat_ticker — source lines 138–139

Source context: callable `_heartbeat_ticker`; enclosing call `console.write`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `case_label; conversion=none; format_spec=none`
- `status; conversion=none; format_spec=none`
- `elapsed; conversion=none; format_spec=none`
- `quiet_now; conversion=none; format_spec=none`
- `counts; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/validation/session/launcher.py:138-139
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [s11] heartbeat: [dynamic source value: case_label; conversion=none; format_spec=none] [dynamic source value: status; conversion=none; format_spec=none]; [dynamic source value: elapsed; conversion=none; format_spec=none]s elapsed, last activity [dynamic source value: quiet_now; conversion=none; format_spec=none]s ago; tool calls: [dynamic source value: counts; conversion=none; format_spec=none]
}
```

## _resolve_binary — source lines 195–195

Source context: callable `_resolve_binary`; enclosing call `HarnessCLINotFoundError`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `binary; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/validation/session/launcher.py:195-195
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Claude binary does not exist: [dynamic source value: binary; conversion=none; format_spec=none]
}
```

## _resolve_binary — source lines 198–198

Source context: callable `_resolve_binary`; enclosing call `HarnessCLINotFoundError`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `binary; conversion=repr; format_spec=none`

```sudo
// Source: vvaharness/validation/session/launcher.py:198-198
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Claude binary must be an absolute path or a bare executable name: [dynamic source value: binary; conversion=repr; format_spec=none]
}
```

## _write_validation_outputs — source lines 233–233

Source context: callable `_write_validation_outputs`; enclosing call `log.warning`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/validation/session/launcher.py:233-233
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: structured validation output is not a dict; skipping host write
}
```

## _write_host_synthesized_gates — source lines 270–270

Source context: callable `_write_host_synthesized_gates`; enclosing call `log.warning`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/validation/session/launcher.py:270-270
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: terminal harness state is not a dict; skipping host synthesis
}
```

## _write_host_synthesized_gates — source lines 275–276

Source context: callable `_write_host_synthesized_gates`; enclosing call `console.write`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `', '.join(missing); conversion=none; format_spec=none`

```sudo
// Source: vvaharness/validation/session/launcher.py:275-276
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [s11] no report from [dynamic source value: ', '.join(missing); conversion=none; format_spec=none]; gates that need their vote cannot reach consensus
}
```

## _write_host_synthesized_gates — source lines 278–278

Source context: callable `_write_host_synthesized_gates`; enclosing call `log.warning`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/validation/session/launcher.py:278-278
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: no valid persona reports extracted; skipping host synthesis
}
```

## _orchestrator_call_budget — source lines 294–294

Source context: callable `_orchestrator_call_budget`; enclosing call `ModelCallBudget`; keyword `counter`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/validation/session/launcher.py:294-294
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s11_orchestrator_model_call_budget_final_turn
}
```

## _failure_reason — source lines 422–424

Source context: callable `_failure_reason`; enclosing call `parts.append`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/validation/session/launcher.py:422-424
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: the model never returned a response matching the validation schema -- either schema-validation retries were exhausted, or a model fallback retracted the response and no retry replaced it
}
```

## _run_and_check — source lines 551–551

Source context: callable `_run_and_check`; enclosing call `log.error`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/validation/session/launcher.py:551-551
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Session %s exited with code %d
}
```

## _run_and_check — source lines 572–573

Source context: callable `_run_and_check`; enclosing call `ValidationSessionError`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/validation/session/launcher.py:572-573
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: validation session reported success but returned no structured output and no terminal state; no validation_report.json could be written
}
```

## _write_workspace_json — source lines 223–223

Source context: callable `_write_workspace_json`; enclosing call `log.exception`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/validation/session/launcher.py:223-223
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: cannot write %s
}
```

## _write_validation_outputs — source lines 242–242

Source context: callable `_write_validation_outputs`; enclosing call `_write_workspace_json`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/validation/session/launcher.py:242-242
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: target_jira_status
}
```

## _stream_session — source lines 505–505

Source context: callable `_stream_session`; enclosing call `ValidationSessionError`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `type(e).__name__; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/validation/session/launcher.py:505-505
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Harness error: [dynamic source value: type(e).__name__; conversion=none; format_spec=none]
}
```

## _raise_if_session_refused — source lines 522–522

Source context: callable `_raise_if_session_refused`; enclosing call `ValidationSessionError`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `exc; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/validation/session/launcher.py:522-522
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: validation session ended on a refused turn: [dynamic source value: exc; conversion=none; format_spec=none]
}
```

## counts — source lines 133–133

Source context: callable `_heartbeat_ticker`; enclosing call `' '.join`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `agent; conversion=none; format_spec=none`
- `n; conversion=none; format_spec=none`

Formatting/composition call retained as source expression evidence:

````python
" ".join(
            f"{agent}={n}" for agent, n in sorted(state.tool_counts.items())
        )
````

```sudo
// Source: vvaharness/validation/session/launcher.py:133-133
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: agent; conversion=none; format_spec=none]=[dynamic source value: n; conversion=none; format_spec=none]
}
```

## _persona_overrides — source lines 181–181

Source context: callable `_persona_overrides`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/validation/session/launcher.py:181-181
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: security-architect
}
```

## _persona_overrides — source lines 182–182

Source context: callable `_persona_overrides`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/validation/session/launcher.py:182-182
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: penetration-tester
}
```

## _persona_overrides — source lines 183–183

Source context: callable `_persona_overrides`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/validation/session/launcher.py:183-183
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: cross-repo-analyzer
}
```

## _synthesize_gates — source lines 257–257

Source context: callable `_synthesize_gates`; enclosing call `synthesized.append`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/validation/session/launcher.py:257-257
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: tracking_id
}
```

## _bounded_stream — source lines 455–455

Source context: callable `_bounded_stream`; enclosing call `call_timeout_error`; keyword `cause_text`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `timeout + _BACKSTOP_GRACE_S; conversion=none; format_spec=f'g'`

```sudo
// Source: vvaharness/validation/session/launcher.py:455-455
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: validation session timed out after [dynamic source value: timeout + _BACKSTOP_GRACE_S; conversion=none; format_spec=f'g']s
}
```

## _stream_session — source lines 507–507

Source context: callable `_stream_session`; enclosing call `getattr`; keyword `exit_code`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/validation/session/launcher.py:507-507
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: exit_code
}
```

