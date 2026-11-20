# vvaharness/pipeline/stages/s4/outcomes.py — model instruction carriers

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## _coerce_line — source lines 76–76

Source context: callable `_coerce_line`; enclosing call `field_validator`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/outcomes.py:76-76
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: sink_line
}
```

## _coerce_line — source lines 76–76

Source context: callable `_coerce_line`; enclosing call `field_validator`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/outcomes.py:76-76
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: line_end
}
```

## _coerce_repeat_lines — source lines 82–82

Source context: callable `_coerce_repeat_lines`; enclosing call `field_validator`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/outcomes.py:82-82
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: repeat_lines
}
```

## sink — source lines 267–267

Source context: callable `fan_out`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `f.file; conversion=none; format_spec=none`
- `f.sink_line; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s4/outcomes.py:267-267
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: f.file; conversion=none; format_spec=none]:[dynamic source value: f.sink_line; conversion=none; format_spec=none]
}
```

## cwe — source lines 35–35

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/outcomes.py:35-35
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Exactly one most-specific CWE id, e.g. CWE-89.
}
```

## file — source lines 36–36

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/outcomes.py:36-36
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Repo-relative path, from this threat's FILES list.
}
```

## line_start — source lines 37–39

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/outcomes.py:37-39
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: 1-indexed FIRST line of the weakness's span.
  The request retains this source rule, criterion or rationale, with its original modal force: For a handler or block the span may start at its decorator or signature — `sink_line`, not this field, names the dangerous statement itself.
}
```

## sink_line — source lines 40–43

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/outcomes.py:40-43
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Exact 1-indexed line of the single statement that embodies the defect — the dangerous call, query, render, write or cookie-set. 0 when no single statement does (e.g. a missing control).
}
```

## line_end — source lines 45–49

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/outcomes.py:45-49
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: 1-indexed LAST line of the weakness, inclusive — the end of the vulnerable statement, block or handler, NOT a repeat of line_start.
  The request retains this source rule, criterion or rationale, with its original modal force: Span the whole construct: an unguarded route runs from its decorator to the end of its function body.
  The model is asked to adopt 0 only when you genuinely cannot bound it.
}
```

## also_cwes — source lines 51–57

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/outcomes.py:51-57
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Other DISTINCT weakness classes present at this same location, as CWE ids.
  The request retains this source rule, criterion or rationale, with its original modal force: One location routinely holds several: a cookie set without HttpOnly (CWE-1004) is usually also set without Secure (CWE-614); a route with no CSRF token (CWE-352) often also has no authorization check (CWE-862).
  The request retains this source rule, criterion or rationale, with its original modal force: Each id here becomes its own reported finding at this line, so naming one costs a few characters and omitting it loses a real defect.
  The requested model behavior excludes list a parent or sibling of `cwe` that means the same thing — only genuinely different weaknesses.
}
```

## repeat_lines — source lines 59–64

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/outcomes.py:59-64
Constraints {
  The requested conditional/temporal rule is: When this IDENTICAL defect repeats at other call sites in the SAME file, the first line of every additional site — one integer each, no prose.
  The request retains this source rule, criterion or rationale, with its original modal force: The description the model already wrote is reused verbatim for each, so listing a site costs the model almost nothing while omitting it loses the finding entirely.
  The request retains this source rule, criterion or rationale, with its original modal force: Report the sites, never a summary of them: one finding whose line span swallows several call sites is wrong, and so is picking one site and dropping the rest.
  The request retains this source rule, criterion or rationale, with its original modal force: Leave empty only when the defect genuinely occurs once.
}
```

## preconditions — source lines 66–74

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/outcomes.py:66-74
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: What must independently be true, beyond reaching this code, for the weakness to be exploitable — one concrete condition per entry, not a restatement of `description`.
  The requested evidence/output includes the actual gate: the endpoint is reachable by an unauthenticated caller; a feature flag or config value is set a particular way; the attacker needs a specific input shape (a negative amount, an oversized payload, a crafted redirect target); the caller needs a particular role or an active session.
  The request retains this source rule, criterion or rationale, with its original modal force: A reviewer judging exploitability off the model's report alone needs these named, so listing one costs a few words while omitting it loses real context.
  The request retains this source rule, criterion or rationale, with its original modal force: Leave empty only when the weakness fires unconditionally on any input that reaches this code — never as a default for not having checked.
}
```

## vuln_class — source lines 91–91

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/outcomes.py:91-91
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Weakness class; unrecognized labels fold to OTHER.
}
```

## title — source lines 93–93

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/outcomes.py:93-93
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: One line, at most 12 words, naming the weakness and its location.
  The request retains this source rule, criterion or rationale, with its original modal force: No prose.
}
```

## severity — source lines 95–95

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/outcomes.py:95-95
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: One enum value. s6 re-scores every finding from a CVSS vector, so do not argue it here.
}
```

## description — source lines 97–99

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/outcomes.py:97-99
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: AT MOST TWO SENTENCES: the defect and why it is one.
  The request retains this source rule, criterion or rationale, with its original modal force: The code is quoted for the reader already — do not restate it, do not repeat the title, and do not re-derive the exploit (exploit_scenario covers that) or the fix (recommendation covers that).
}
```

## exploit_scenario — source lines 101–106

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/outcomes.py:101-106
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Concrete input -> impact, in at most five sentences.
  The request retains this source rule, criterion or rationale, with its original modal force: Every application feature, flow or component the scenario relies on or leads to (a password-reset flow, an admin panel, mail sending, a file store) must be one the model saw in this repository's code; where the follow-on depends on one the model did not see, write it conditionally ('if the application offers a password reset') or stop at the impact the code shows.
  The request retains this source rule, criterion or rationale, with its original modal force: A consequence the code does not support is a false claim, not a stronger finding.
}
```

## recommendation — source lines 108–109

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/outcomes.py:108-109
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: AT MOST TWO SENTENCES: the concrete change, naming the API or control to use.
  The request retains this source rule, criterion or rationale, with its original modal force: No restatement of the defect, no alternatives list, no code block.
}
```

## unit_id — source lines 113–113

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/outcomes.py:113-113
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Echo the UNIT id the model were given, verbatim.
}
```

## verdict — source lines 115–116

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/outcomes.py:115-116
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: refuted = the model read the whole surface and the claim does not hold; say why in rationale. inconclusive = the model could not reach the evidence.
  The requested model behavior excludes use confirmed as a default.
}
```

## rationale — source lines 117–117

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/outcomes.py:117-117
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Why, in 1-3 sentences.
  The request retains this source rule, criterion or rationale, with its original modal force: Required for refuted.
}
```

## findings — source lines 119–120

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/outcomes.py:119-120
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: EVERY distinct weakness class the model have evidence for — a list, not one.
  The request retains this source rule, criterion or rationale, with its original modal force: Empty is correct and expected when verdict is refuted.
}
```

## outcomes — source lines 125–126

Source context: callable `<module>`; enclosing call `Field`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/outcomes.py:125-126
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: ONE entry per UNIT the model were given, each echoing that unit's own id.
  The request retains this source rule, criterion or rationale, with its original modal force: Report every unit, including the ones the model refuted — a unit the model omit is recorded as uninvestigated, not clean.
}
```

## split_batch_reply — source lines 173–173

Source context: callable `split_batch_reply`; enclosing call `COUNTERS.bump`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/outcomes.py:173-173
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s4_batch_unit_omitted
}
```

## _bump_parse_failure — source lines 187–187

Source context: callable `_bump_parse_failure`; enclosing call `COUNTERS.bump`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/outcomes.py:187-187
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s4_outcome_truncated
}
```

## _bump_parse_failure — source lines 189–189

Source context: callable `_bump_parse_failure`; enclosing call `COUNTERS.bump`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/outcomes.py:189-189
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s4_outcome_malformed
}
```

## _resolved_cwe — source lines 211–211

Source context: callable `_resolved_cwe`; enclosing call `COUNTERS.bump`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/outcomes.py:211-211
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s4_finding_cwe_backfilled
}
```

## _extra_cwes — source lines 241–241

Source context: callable `_extra_cwes`; enclosing call `COUNTERS.bump`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/outcomes.py:241-241
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s4_finding_extra_cwe_collapsed
}
```

## _extra_cwes — source lines 244–244

Source context: callable `_extra_cwes`; enclosing call `COUNTERS.bump`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/outcomes.py:244-244
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s4_finding_extra_cwes_capped
}
```

## max_extra — source lines 258–258

Source context: callable `fan_out`; enclosing call `knob`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/outcomes.py:258-258
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: step4.max_extra_cwes
}
```

## fan_out — source lines 261–261

Source context: callable `fan_out`; enclosing call `COUNTERS.bump`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/outcomes.py:261-261
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s4_finding_repeat_sites
}
```

## fan_out — source lines 262–262

Source context: callable `fan_out`; enclosing call `COUNTERS.bump`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/outcomes.py:262-262
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s4_finding_with_repeats
}
```

## fan_out — source lines 264–264

Source context: callable `fan_out`; enclosing call `COUNTERS.bump`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/outcomes.py:264-264
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s4_finding_extra_cwes
}
```

## fan_out — source lines 265–265

Source context: callable `fan_out`; enclosing call `COUNTERS.bump`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/outcomes.py:265-265
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s4_finding_with_extra_cwes
}
```

## fan_out — source lines 269–269

Source context: callable `fan_out`; enclosing call `COUNTERS.bump`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/outcomes.py:269-269
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s4_finding_sink_line
}
```

## reduce_outcomes — source lines 299–299

Source context: callable `reduce_outcomes`; enclosing call `COUNTERS.bump`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/outcomes.py:299-299
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s4_unit_no_outcome
}
```

## split_batch_reply — source lines 168–168

Source context: callable `split_batch_reply`; enclosing call `COUNTERS.bump`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/outcomes.py:168-168
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s4_batch_unit_id_invented
}
```

## reduce_outcomes — source lines 284–284

Source context: callable `reduce_outcomes`; enclosing call `COUNTERS.bump`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/outcomes.py:284-284
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s4_unit_id_invented
}
```

