# vvaharness/pipeline/stages/s8/outcomes.py — model instruction carriers

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## _LIFT_NOTE — source lines 244–244

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:244-244
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: _Severity aligned to the highest-severity finding in this path._
}
```

## _CAP_ANNOTATION — source lines 247–249

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:247-249
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Severity not raised for chain composition: this path's hops are not fully evidenced, or a step supplies no attacker capability.
}
```

## _PROSE_ID_NOTE — source lines 262–264

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:262-264
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: This chain's prose cites finding id(s) {ids} that name no finding in this report; they are printed as the reply wrote them.
}
```

## _SEV_MISMATCH_NOTE — source lines 368–370

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:368-370
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Model-assessed severity ({model}) differs from the CVSS/VulContextSeverity band ({shipped}) that determines the shipped rating.
}
```

## _PROSE_ID_RX — source lines 256–256

Source context: callable `<module>`; enclosing call `re.compile`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `_PROSE_ID_JOIN; conversion=none; format_spec=none`
- `_PROSE_ID_JOIN; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:256-256
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: (?<![\w./$-])f\d+(?:[dynamic source value: _PROSE_ID_JOIN; conversion=none; format_spec=none]f\d+)*\b(?![dynamic source value: _PROSE_ID_JOIN; conversion=none; format_spec=none]f\d|\.\w)
}
```

## _PROSE_ID_SPLIT_RX — source lines 257–257

Source context: callable `<module>`; enclosing call `re.compile`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `_PROSE_ID_JOIN; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:257-257
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: ([dynamic source value: _PROSE_ID_JOIN; conversion=none; format_spec=none])
}
```

## templated_summary — source lines 453–453

Source context: callable `templated_summary`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `len(ranked); conversion=none; format_spec=none`
- `bands; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:453-453
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: len(ranked); conversion=none; format_spec=none] verified finding(s): [dynamic source value: bands; conversion=none; format_spec=none].
}
```

## _coerce_str — source lines 90–90

Source context: callable `_coerce_str`; enclosing call `field_validator`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:90-90
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: finding_id
}
```

## _coerce_str — source lines 90–90

Source context: callable `_coerce_str`; enclosing call `field_validator`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:90-90
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: exploitability_notes
}
```

## _coerce_str — source lines 130–130

Source context: callable `_coerce_str`; enclosing call `field_validator`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:130-130
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: entry_reachability
}
```

## _coerce_str_list — source lines 136–136

Source context: callable `_coerce_str_list`; enclosing call `field_validator`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:136-136
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: blocked_by_controls
}
```

## _coerce_links — source lines 142–142

Source context: callable `_coerce_links`; enclosing call `field_validator`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:142-142
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: link_evidence
}
```

## finding_ids — source lines 211–211

Source context: callable `finding_ids`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `i; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:211-211
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: f[dynamic source value: i; conversion=none; format_spec=none]
}
```

## _model_or_derived_chain_severity — source lines 239–239

Source context: callable `_model_or_derived_chain_severity`; enclosing call `COUNTERS.bump`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:239-239
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s8_chain_severity_derived
}
```

## _SUMMARY_WORDING — source lines 305–305

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:305-305
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: \1chain list
}
```

## _SUMMARY_WORDING — source lines 307–307

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:307-307
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: link evidence
}
```

## templated_summary — source lines 447–447

Source context: callable `templated_summary`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:447-447
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: No verified findings.
}
```

## _positionally_filled — source lines 493–493

Source context: callable `_positionally_filled`; enclosing call `COUNTERS.bump`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:493-493
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s8_chain_links_positionally_filled
}
```

## gate_on — source lines 708–708

Source context: callable `hydrate_report`; enclosing call `knob`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:708-708
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: step8.severity_lift_gate
}
```

## checks_on — source lines 709–709

Source context: callable `hydrate_report`; enclosing call `knob`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:709-709
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: step8.chain_quality_checks
}
```

## dedup_on — source lines 710–710

Source context: callable `hydrate_report`; enclosing call `knob`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:710-710
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: step8.chain_dedup
}
```

## prose_ids — source lines 713–713

Source context: callable `hydrate_report`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `orig_to_sorted[i] + 1; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:713-713
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: #[dynamic source value: orig_to_sorted[i] + 1; conversion=none; format_spec=none]
}
```

## finding_id — source lines 73–73

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:73-73
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Echo the FINDING id the model were given, verbatim.
}
```

## severity — source lines 75–77

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:75-77
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: LEAVE EMPTY unless the model are deliberately overriding the severity shown. final_severity takes the VulContextSeverity or CVSS band ahead of this value, so for any finding that has one the model's word here is discarded.
  The request retains this source rule, criterion or rationale, with its original modal force: One of critical, high, medium, low, info.
}
```

## exploitability_notes — source lines 79–80

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:79-80
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: AT MOST TWO SENTENCES: why this severity differs, naming the control that applies or fails.
  The request retains this source rule, criterion or rationale, with its original modal force: Omit entirely when the model are only recording `feeds`.
}
```

## feeds — source lines 82–87

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:82-87
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Ids of the findings this one SUPPLIES something to — a value, a privilege, a reachable state or an input the other finding needs — whether or not the model can evidence the link.
  The requested evidence/output includes every such id; chain the ones you can evidence with link_evidence, the rest stay here.
  The requested model behavior excludes a finding at the same file:line, and never a precondition or amplifier (a root container, a missing header): those stay in exploitability_notes.
}
```

## title — source lines 103–103

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:103-103
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: The chain in a few words, e.g. 'SSRF -> metadata creds -> S3'.
}
```

## steps — source lines 105–106

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:105-106
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: The FINDING ids in exploitation order, at least two.
  The request retains this source rule, criterion or rationale, with its original modal force: Ids only, no prose.
  The request retains this source rule, criterion or rationale, with its original modal force: Two findings at the SAME file and line are one code fact, never two steps.
}
```

## severity — source lines 108–109

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:108-109
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: LEAVE EMPTY.
  The request retains this source rule, criterion or rationale, with its original modal force: The host derives a chain's severity from its steps and the lift gate caps it at the strongest constituent finding, so a value here is discarded.
}
```

## blocked_by_controls — source lines 111–111

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:111-111
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Names of design controls that genuinely block this chain, if any.
}
```

## narrative — source lines 113–114

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:113-114
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: ONE sentence naming what the chain achieves that no single step does.
  The request retains this source rule, criterion or rationale, with its original modal force: The per-hop mechanism belongs in link_evidence, not here -- do not retell the steps.
}
```

## link_evidence — source lines 117–120

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:117-120
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: ONE entry per adjacent pair in `steps`, IN ORDER (so len(steps) - 1 entries).
  The request retains this source rule, criterion or rationale, with its original modal force: Leave from_id/to_id EMPTY -- position already says which pair the model mean and the host fills them.
  The request retains this source rule, criterion or rationale, with its original modal force: Give only `mechanism` and the file/line that shows the link holds.
  The request retains this source rule, criterion or rationale, with its original modal force: A link the model cannot evidence means the chain is not real: drop the chain, do not invent one.
}
```

## entry_reachability — source lines 122–123

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:122-123
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: How the FIRST step is reached by the attacker the model claim — cite the route/entry point and any binding or exposure fact the model were given.
}
```

## preconditions — source lines 125–127

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:125-127
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Non-default config or state this chain REQUIRES (e.g. 'requires --risk>=3, default is 1').
  The request retains this source rule, criterion or rationale, with its original modal force: These are surfaced to the report reader, so a chain that only works off-default must say so here.
}
```

## ranked_findings — source lines 159–162

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:159-162
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: SPARSE: an entry ONLY for a finding that feeds another one, or whose severity the model are changing from the CVSS-derived value shown.
  The request retains this source rule, criterion or rationale, with its original modal force: Omit every other finding -- omitted ones ship with their CVSS severity, which is already correct.
  The request retains this source rule, criterion or rationale, with its original modal force: An empty list is a valid answer.
  The requested model behavior excludes echo back findings you have nothing to add to.
}
```

## chains — source lines 164–165

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:164-165
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Chains of two or more findings.
  The request retains this source rule, criterion or rationale, with its original modal force: Empty is correct when no finding feeds another — an invented chain is worse than none.
}
```

## summary — source lines 167–169

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:167-169
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Executive summary, 2-4 sentences, written LAST: it may describe only the chains listed in `chains` and the ranking above — a path that is not a chain entry must not be claimed here.
}
```

## carried — source lines 194–194

Source context: callable `_salvage_entries`; enclosing call `data.get`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:194-194
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: chains_invalid
}
```

## data['chains_invalid'] — source lines 197–197

Source context: callable `_salvage_entries`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:197-197
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: chains_invalid
}
```

## _SUMMARY_WORDING — source lines 305–305

Source context: callable `<module>`; enclosing call `re.compile`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:305-305
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: \b(the )chains (?:array|list)\b
}
```

## _SUMMARY_WORDING — source lines 306–306

Source context: callable `<module>`; enclosing call `re.compile`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:306-306
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: \branked_findings\b
}
```

## _SUMMARY_WORDING — source lines 307–307

Source context: callable `<module>`; enclosing call `re.compile`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:307-307
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: \blink_evidence\b
}
```

## bands — source lines 451–451

Source context: callable `templated_summary`; enclosing call `', '.join`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `counts[s]; conversion=none; format_spec=none`
- `s.value; conversion=none; format_spec=none`

Formatting/composition call retained as source expression evidence:

````python
", ".join(f"{counts[s]} {s.value}" for s in SEV_RANK
                      if counts.get(s))
````

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:451-451
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: counts[s]; conversion=none; format_spec=none] [dynamic source value: s.value; conversion=none; format_spec=none]
}
```

## ranked — source lines 465–466

Source context: callable `deterministic_report`; enclosing call `ranked_finding`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:465-466
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: (enrichment unavailable — severity from CVSS or the detection label)
}
```

## deterministic_report — source lines 481–482

Source context: callable `deterministic_report`; enclosing call `FinalReport`; keyword `degraded_reason`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `enrichment_failure; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:481-482
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: chain/narrative enrichment unavailable: [dynamic source value: enrichment_failure; conversion=none; format_spec=none]
}
```

## _build_chain — source lines 512–512

Source context: callable `_build_chain`; enclosing call `COUNTERS.bump`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:512-512
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s8_chain_links_origin_dropped
}
```

## _build_chain — source lines 525–525

Source context: callable `_build_chain`; enclosing call `COUNTERS.bump`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:525-525
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s8_chain_step_id_unknown
}
```

## _build_chain — source lines 530–530

Source context: callable `_build_chain`; enclosing call `COUNTERS.bump`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:530-530
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s8_chain_hop_same_location
}
```

## extra — source lines 539–539

Source context: callable `_build_chain`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `len(unknown) - 20; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:539-539
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: (+[dynamic source value: len(unknown) - 20; conversion=none; format_spec=none] more)
}
```

## why — source lines 541–542

Source context: callable `_build_chain`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:541-542
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: outside this pass's view (not in the verified set, or not sent to the windowed enrichment call)
}
```

## why — source lines 543–543

Source context: callable `_build_chain`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:543-543
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: not in the verified set
}
```

## _build_chain — source lines 568–568

Source context: callable `_build_chain`; enclosing call `COUNTERS.bump`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:568-568
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s8_chain_links_unplaced
}
```

## _build_chain — source lines 588–588

Source context: callable `_build_chain`; enclosing call `COUNTERS.bump`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:588-588
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s8_chain_prose_id_unresolved
}
```

## decision — source lines 619–619

Source context: callable `_build_chain`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:619-619
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: lift_withheld
}
```

## hydrate_report — source lines 725–725

Source context: callable `hydrate_report`; enclosing call `COUNTERS.bump`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:725-725
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s8_chain_prose_id_unresolved
}
```

## hydrate_report — source lines 742–742

Source context: callable `hydrate_report`; enclosing call `COUNTERS.bump`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:742-742
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s8_chain_dropped
}
```

## _coerce_links — source lines 151–151

Source context: callable `_coerce_links`; enclosing call `COUNTERS.bump`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:151-151
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s8_link_evidence_entry_invalid
}
```

## _salvage_entries — source lines 183–183

Source context: callable `_salvage_entries`; enclosing call `COUNTERS.bump`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:183-183
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s8_chains_key_absent
}
```

## _salvage_entries — source lines 185–185

Source context: callable `_salvage_entries`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:185-185
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: ranked_findings
}
```

## members — source lines 287–287

Source context: callable `_one`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `n; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:287-287
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: f[dynamic source value: n; conversion=none; format_spec=none]
}
```

## final_severity — source lines 363–363

Source context: callable `final_severity`; enclosing call `getattr`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:363-363
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: vsvs_rating
}
```

## final_severity — source lines 364–364

Source context: callable `final_severity`; enclosing call `getattr`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:364-364
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: cvss_rating
}
```

## _build_chain — source lines 533–533

Source context: callable `_build_chain`; enclosing call `COUNTERS.bump`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:533-533
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s8_chain_dropped_unresolved_steps
}
```

## _build_chain — source lines 534–534

Source context: callable `_build_chain`; enclosing call `COUNTERS.bump`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:534-534
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s8_chain_dropped_same_location
}
```

## narrative — source lines 544–546

Source context: callable `_build_chain`; enclosing call `f'{narrative}\n\n_Note: this chain referenced finding ids {shown}{extra} that were {why}; they have been omitted from the path above._'.strip`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `narrative; conversion=none; format_spec=none`
- `shown; conversion=none; format_spec=none`
- `extra; conversion=none; format_spec=none`
- `why; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:544-546
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: narrative; conversion=none; format_spec=none]
}
```

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:544-546
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: _Note: this chain referenced finding ids [dynamic source value: shown; conversion=none; format_spec=none][dynamic source value: extra; conversion=none; format_spec=none] that were [dynamic source value: why; conversion=none; format_spec=none]; they have been omitted from the path above._
}
```

## _build_chain — source lines 614–614

Source context: callable `_build_chain`; enclosing call `COUNTERS.bump`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:614-614
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s8_chain_severity_lifted
}
```

## _build_chain — source lines 618–618

Source context: callable `_build_chain`; enclosing call `COUNTERS.bump`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:618-618
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s8_chain_lift_suppressed
}
```

## _build_chain — source lines 622–622

Source context: callable `_build_chain`; enclosing call `COUNTERS.bump`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:622-622
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s8_chain_severity_under_hops
}
```

## _build_chain — source lines 635–635

Source context: callable `_build_chain`; enclosing call `Chain`; keyword `title`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:635-635
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Unnamed chain
}
```

## _build_chain — source lines 646–646

Source context: callable `_build_chain`; enclosing call `Chain`; keyword `link_coverage`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `resolved_links; conversion=none; format_spec=none`
- `hops; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:646-646
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: resolved_links; conversion=none; format_spec=none]/[dynamic source value: hops; conversion=none; format_spec=none]
}
```

## note — source lines 698–698

Source context: callable `hydrate_report`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:698-698
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: (not sent to the enrichment pass — report windowed)
}
```

## hydrate_report — source lines 721–721

Source context: callable `hydrate_report`; enclosing call `COUNTERS.bump`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:721-721
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s8_chain_prose_id_unresolved
}
```

## hydrate_report — source lines 751–751

Source context: callable `hydrate_report`; enclosing call `COUNTERS.bump`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:751-751
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s8_chain_link_unpromoted
}
```

## hydrate_report — source lines 757–757

Source context: callable `hydrate_report`; enclosing call `COUNTERS.bump`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:757-757
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s8_chain_deduped
}
```

## hydrate_report — source lines 760–760

Source context: callable `hydrate_report`; enclosing call `COUNTERS.bump`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:760-760
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s8_chain_near_duplicate
}
```

## _salvage_entries — source lines 191–191

Source context: callable `_salvage_entries`; enclosing call `COUNTERS.bump`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `field; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:191-191
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s8_[dynamic source value: field; conversion=none; format_spec=none]_entry_invalid
}
```

## _positionally_filled — source lines 494–494

Source context: callable `_positionally_filled`; enclosing call `ln.model_copy`; keyword `update`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:494-494
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: from_id
}
```

## _positionally_filled — source lines 494–494

Source context: callable `_positionally_filled`; enclosing call `ln.model_copy`; keyword `update`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:494-494
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: to_id
}
```

## item — source lines 511–511

Source context: callable `_build_chain`; enclosing call `item.model_copy`; keyword `update`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:511-511
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: link_evidence
}
```

## narrative — source lines 615–615

Source context: callable `_build_chain`; enclosing call `f'{narrative}\n\n{_LIFT_NOTE}'.strip`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `narrative; conversion=none; format_spec=none`
- `_LIFT_NOTE; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:615-615
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: narrative; conversion=none; format_spec=none]
}
```

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:615-615
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: _LIFT_NOTE; conversion=none; format_spec=none]
}
```

## _build_chain — source lines 624–624

Source context: callable `_build_chain`; enclosing call `COUNTERS.bump`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:624-624
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s8_chain_severity_raised
}
```

## decision — source lines 629–629

Source context: callable `_build_chain`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:629-629
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: self_raise_capped
}
```

## hydrate_report — source lines 668–668

Source context: callable `hydrate_report`; enclosing call `COUNTERS.bump`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:668-668
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s8_ranked_finding_id_unknown
}
```

## hydrate_report — source lines 669–669

Source context: callable `hydrate_report`; enclosing call `COUNTERS.bump`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:669-669
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s8_ranked_finding_id_repeated
}
```

## hydrate_report — source lines 676–676

Source context: callable `hydrate_report`; enclosing call `COUNTERS.bump`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:676-676
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s8_chain_feeds_id_unknown
}
```

## dropped_out — source lines 436–436

Source context: callable `_sort_and_remap`; enclosing call `d.model_copy`; keyword `update`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:436-436
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: canonical_idx
}
```

## _build_chain — source lines 563–563

Source context: callable `_build_chain`; enclosing call `LinkEvidence`; keyword `from_id`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `src + 1; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:563-563
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: #[dynamic source value: src + 1; conversion=none; format_spec=none]
}
```

## _build_chain — source lines 563–563

Source context: callable `_build_chain`; enclosing call `LinkEvidence`; keyword `to_id`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `dst + 1; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:563-563
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: #[dynamic source value: dst + 1; conversion=none; format_spec=none]
}
```

## _build_chain — source lines 628–628

Source context: callable `_build_chain`; enclosing call `COUNTERS.bump`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:628-628
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s8_chain_severity_capped
}
```

## op — source lines 391–391

Source context: callable `offensive_rank`; enclosing call `getattr`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:391-391
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: offensive_priority
}
```

## _build_chain — source lines 581–581

Source context: callable `_build_chain`; enclosing call `item.model_copy`; keyword `update`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:581-581
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: link_evidence
}
```

