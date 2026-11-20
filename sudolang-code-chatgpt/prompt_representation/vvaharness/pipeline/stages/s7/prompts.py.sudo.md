# vvaharness/pipeline/stages/s7/prompts.py — model instruction carriers

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## Requested collapse and independent-site decisions

Structured view of the same source instructions, not an additional pass or an assertion of model compliance.

```sudo
// Source: vvaharness/pipeline/stages/s7/prompts.py:23-66
Constraints {
  The model is asked to compare findings by whether one engineering fix closes both.
  if (distinct cwe values are not siblings in CWE-89/943/564, CWE-78/77, CWE-22/23/36, CWE-79/80 or CWE-862/285/284) {
    The model is instructed to keep the findings separate even if one control might touch both.
  } else if (one engineering edit fixes both findings) {
    The requested duplicate_of is the LOWER index.
    Eligible descriptions include relabeled defects, shared-helper fixes, global missing controls, cause/effect pairs and shared settings.
    The same-file approximately-30-line criterion additionally requires descriptions clearly concerning one issue; it is not a numeric deduplication guarantee.
  } else { The requested duplicate_of is -1. }
  if (the model is unsure) { It is asked to keep both. }
  for each decision, Constraints {
    independent_sites is requested false when one site fix fixes the others, and true when each would remain broken independently.
    if (duplicate_of == -1) { independent_sites is requested false. }
    This flag controls preservation of extra report locations, not the collapse decision.
  }
}
```

## SYSTEM — source lines 23–66

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s7/prompts.py:23-66
Constraints {
  The requested model role and scope are collapsing overlapping SAST findings that several independent reviewers raised against the same repository.
}
```

```sudo
// Source: vvaharness/pipeline/stages/s7/prompts.py:23-66
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: DECISION TEST: two findings are the SAME finding when one engineering fix closes both.
  The requested conditional/temporal rule is: If each needs its own code change, they are separate — even if the bug class and file are identical.
}
```

```sudo
// Source: vvaharness/pipeline/stages/s7/prompts.py:23-66
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Collapse it — set `duplicate_of` to the LOWER index — when any of these hold:
}
```

```sudo
// Source: vvaharness/pipeline/stages/s7/prompts.py:23-66
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Same defect, different label or line — e.g. "OS command exec" at L40 vs "shell injection" at L42.
}
```

```sudo
// Source: vvaharness/pipeline/stages/s7/prompts.py:23-66
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Both trace back to one shared helper / utility; the call sites differ but the fix lives in the helper.
}
```

```sudo
// Source: vvaharness/pipeline/stages/s7/prompts.py:23-66
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: One global control is absent (auth filter, CSRF token, output encoder) and each affected route was filed as its own ticket.
}
```

```sudo
// Source: vvaharness/pipeline/stages/s7/prompts.py:23-66
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: A cause/effect pair on one flow — "no input validation" filed alongside the resulting "SQLi" on the same sink.
}
```

```sudo
// Source: vvaharness/pipeline/stages/s7/prompts.py:23-66
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: One insecure setting or default surfaces at several read points.
}
```

```sudo
// Source: vvaharness/pipeline/stages/s7/prompts.py:23-66
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Same file, lines within ~30 of each other, and the descriptions clearly describe one issue from two angles.
}
```

```sudo
// Source: vvaharness/pipeline/stages/s7/prompts.py:23-66
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Keep it separate — `duplicate_of: -1` — when:
}
```

```sudo
// Source: vvaharness/pipeline/stages/s7/prompts.py:23-66
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: The fixes land in different functions/files and neither fix covers the other.
}
```

```sudo
// Source: vvaharness/pipeline/stages/s7/prompts.py:23-66
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Same CWE class repeated independently (e.g. two unrelated string-built SQL queries) — each one needs its own patch.
}
```

```sudo
// Source: vvaharness/pipeline/stages/s7/prompts.py:23-66
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: The two findings carry different `cwe` values. Different CWEs mean different defects and different fixes, even at the same file and line, and even when one control would plausibly touch both (one exception follows).
  The request retains this source rule, criterion or rationale, with its original modal force: A missing CSRF token is not a debug-mode leak; cleartext password storage is not an auth bypass.
  The requested model behavior excludes collapse across CWE ids.
  The request retains this source rule, criterion or rationale, with its original modal force: The one exception is sibling ids that name ONE weakness — CWE-89/943/564, CWE-78/77, CWE-22/23/36, CWE-79/80 and CWE-862/285/284 — which count as the same id; every other cross-CWE collapse the model propose is refused.
}
```

```sudo
// Source: vvaharness/pipeline/stages/s7/prompts.py:23-66
Constraints {
  The requested conditional/temporal rule is: For EVERY decision, also set `independent_sites` per its schema description.
  The request retains this source rule, criterion or rationale, with its original modal force: The test: "would fixing one site fix the others?" Yes → false.
  The request retains this source rule, criterion or rationale, with its original modal force: No — each site would still be broken after another site's fix → true.
  The request retains this source rule, criterion or rationale, with its original modal force: It never changes whether the model collapse; it only decides whether the collapsed members' locations survive on the survivor as extra call sites in the report.
  The request retains this source rule, criterion or rationale, with its original modal force: On a `duplicate_of: -1` row set false.
}
```

```sudo
// Source: vvaharness/pipeline/stages/s7/prompts.py:23-66
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Collapse only what ONE edit fixes.
  The requested conditional/temporal rule is: When the model are unsure, keep both: a kept duplicate costs a line in the report, a wrongly collapsed finding is a deleted vulnerability.
}
```

## build_payload — source lines 83–83

Source context: callable `build_payload`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s7/prompts.py:83-83
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: FINDINGS TO DEDUPLICATE:
}
```

## payload — source lines 78–78

Source context: callable `build_payload`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s7/prompts.py:78-78
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: exploit_scenario
}
```

## payload — source lines 80–80

Source context: callable `build_payload`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s7/prompts.py:80-80
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: source_ref
}
```

## payload — source lines 81–81

Source context: callable `build_payload`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s7/prompts.py:81-81
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: sink_ref
}
```

