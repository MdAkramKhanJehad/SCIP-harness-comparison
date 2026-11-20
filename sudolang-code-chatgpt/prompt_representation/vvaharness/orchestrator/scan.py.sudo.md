# vvaharness/orchestrator/scan.py — model instruction carriers

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## _remediate_preflight — source lines 1151–1151

Source context: callable `_remediate_preflight`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

```sudo
// Source: vvaharness/orchestrator/scan.py:1151-1151
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: models.remediate must be set
}
```

## _validate_preflight — source lines 1186–1186

Source context: callable `_validate_preflight`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

```sudo
// Source: vvaharness/orchestrator/scan.py:1186-1186
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: models.validate.orchestrator must be set
}
```

## _prune_ev_replays — source lines 174–174

Source context: callable `_prune_ev_replays`; enclosing call `getattr`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/orchestrator/scan.py:174-174
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: ev_collection
}
```

## _ev_oob_selftest — source lines 280–282

Source context: callable `_ev_oob_selftest`; enclosing call `console.mark`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `'reachable' if ok else 'NOT reachable'; conversion=none; format_spec=none`
- `mgr.advertised_url; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/orchestrator/scan.py:280-282
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [ev-oob] listener [dynamic source value: 'reachable' if ok else 'NOT reachable'; conversion=none; format_spec=none] (self-test [dynamic source value: mgr.advertised_url; conversion=none; format_spec=none]); the target must be able to reach this URL
}
```

## _clause — source lines 927–928

Source context: callable `scan_repo`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `_n_halted; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/orchestrator/scan.py:927-928
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s4 halted early: [dynamic source value: _n_halted; conversion=none; format_spec=none] unit(s) not analyzed (expired/invalid credentials or a broken proxy/TLS path)
}
```

## scan_repo — source lines 1063–1063

Source context: callable `scan_repo`; enclosing call `console.write`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `out_path; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/orchestrator/scan.py:1063-1063
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Report: [dynamic source value: out_path; conversion=none; format_spec=none]
}
```

## _prune_ev_replays — source lines 180–181

Source context: callable `_prune_ev_replays`; enclosing call `console.write`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `removed; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/orchestrator/scan.py:180-181
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [s6-ev] pruned [dynamic source value: removed; conversion=none; format_spec=none] replay bundle(s) for finding(s) collapsed by dedup
}
```

## _clause — source lines 909–909

Source context: callable `scan_repo`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `_stage_id; conversion=none; format_spec=none`
- `redact(_msg); conversion=none; format_spec=none`

```sudo
// Source: vvaharness/orchestrator/scan.py:909-909
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: _stage_id; conversion=none; format_spec=none] failed: [dynamic source value: redact(_msg); conversion=none; format_spec=none]
}
```

## _clause — source lines 910–910

Source context: callable `scan_repo`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `_stage_id; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/orchestrator/scan.py:910-910
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: _stage_id; conversion=none; format_spec=none] failed
}
```

## scan_repo — source lines 918–921

Source context: callable `scan_repo`; enclosing call `console.mark`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `', '.join(_starved); conversion=none; format_spec=none`
- `len(report.findings); conversion=none; format_spec=none`

```sudo
// Source: vvaharness/orchestrator/scan.py:918-921
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: investigation incomplete: [dynamic source value: ', '.join(_starved); conversion=none; format_spec=none] failed.
  The request retains this source rule, criterion or rationale, with its original modal force: The [dynamic source value: len(report.findings); conversion=none; format_spec=none] finding(s) below are NOT a trustworthy result for this repo -- a stage that should have found work never ran to completion.
  The request retains this source rule, criterion or rationale, with its original modal force: See degraded_reason.
}
```

