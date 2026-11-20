# vvaharness/pipeline/stages/s7/collapse.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/pipeline/stages/s7/collapse.py.evidence.json`. SHA-256: `b36c8f30d252e6fc60db38fe1202f77a1415569cb4e804fb2d5ce44a0ed7bee3`.

```sudo
// Source: vvaharness/pipeline/stages/s7/collapse.py:16-22
In source order: Retain source documentation literal source_literal_16_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import re; preserve alias and import-time effects. Then Resolve source import from vvaharness.models import DupLocation, Finding, VulnClass; preserve alias and import-time effects. Then Resolve source import from vvaharness.rules.cwe import _GENERIC_PARENT_CWES, norm_cwe, weakness_key; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s7/collapse.py:23-33
In source order: Resolve source import from vvaharness.util.counters import COUNTERS; preserve alias and import-time effects. Then Evaluate once 'trivial: same site, shared weakness within line tolerance'; assign in source target order to TRIVIAL_REASON. Then Evaluate once {VulnClass.LOGIC}; assign in source target order to STRICT_CWE_CLASS. Then Evaluate once frozenset({VulnClass.OTHER, VulnClass.LOGIC}); assign in source target order to CATCH_ALL_VULN_CLASS. Then Evaluate once 0.15; assign in source target order to MIN_TITLE_OVERLAP.
// Source: vvaharness/pipeline/stages/s7/collapse.py:35-38
In source order: Evaluate once frozenset({'via', 'the', 'and', 'with', 'to', 'of', 'on', 'no', 'or', 'for', 'is', 'by', 'without', 'all', 'in', 'a', 'an', 'from', 'into', 'that', 'this', 'its'}); assign in source target order to _TITLE_STOPWORDS.
// Source: vvaharness/pipeline/stages/s7/collapse.py:41-44
// Source signature: _title_tokens(title: str) -> frozenset[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _title_tokens(title) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s7/collapse.py:42-43
  In source order: Retain source documentation literal source_literal_42_4; it is not a model call. Then Evaluate once re.findall('[a-z0-9]+', title.lower()); assign in source target order to words.
  // Source: vvaharness/pipeline/stages/s7/collapse.py:44-44
  End this invocation with frozenset((w for w in words if len(w) > 2 and w not in _TITLE_STOPWORDS)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s7/collapse.py:47-52
// Source signature: title_overlap(a: Finding, b: Finding) -> float
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn title_overlap(a, b) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s7/collapse.py:48-49
  In source order: Retain source documentation literal source_literal_48_4; it is not a model call. Then Evaluate once (_title_tokens(a.title), _title_tokens(b.title)); assign in source target order to (ta, tb).
  // Source: vvaharness/pipeline/stages/s7/collapse.py:50-51
  if (the source predicate not ta or not tb is truthy) {
    // Source: vvaharness/pipeline/stages/s7/collapse.py:51-51
    End this invocation with 1.0.
  }
  // Source: vvaharness/pipeline/stages/s7/collapse.py:52-52
  End this invocation with len(ta & tb) / len(ta | tb).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s7/collapse.py:56-62
// Source signature: cwe_conflict(a: Finding, b: Finding) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn cwe_conflict(a, b) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s7/collapse.py:57-57
  In source order: Retain source documentation literal source_literal_57_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s7/collapse.py:58-59
  if (the source predicate not (a.cwe and b.cwe) is truthy) {
    // Source: vvaharness/pipeline/stages/s7/collapse.py:59-59
    End this invocation with False.
  }
  // Source: vvaharness/pipeline/stages/s7/collapse.py:60-60
  In source order: Evaluate once (weakness_key(a.cwe), weakness_key(b.cwe)); assign in source target order to (key_a, key_b).
  // Source: vvaharness/pipeline/stages/s7/collapse.py:62-62
  End this invocation with key_a is None or key_a != key_b.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s7/collapse.py:65-77
// Source signature: dup_location(f: Finding, reasoning: str) -> DupLocation
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn dup_location(f, reasoning) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s7/collapse.py:66-66
  In source order: Retain source documentation literal source_literal_66_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s7/collapse.py:67-77
  End this invocation with DupLocation(file=f.file, line_start=f.line_start, line_end=f.line_end, vuln_class=f.vuln_class, title=f.title, chunk_id=f.chunk_id, source_ref=f.source_ref, sink_ref=f.sink_ref, reasoning=reasoning).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s7/collapse.py:80-89
// Source signature: dedup_locations(locs: list) -> list
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn dedup_locations(locs) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s7/collapse.py:81-83
  In source order: Retain source documentation literal source_literal_81_4; it is not a model call. Then For seen, assign set(); source annotation set. Then For out, assign []; source annotation list.
  // Source: vvaharness/pipeline/stages/s7/collapse.py:84-88
  for each d in locs {
    // Source: vvaharness/pipeline/stages/s7/collapse.py:85-85
    In source order: Evaluate once (d.file, d.line_start, d.line_end); assign in source target order to key.
    // Source: vvaharness/pipeline/stages/s7/collapse.py:86-88
    if (the source predicate key not in seen is truthy) {
      // Source: vvaharness/pipeline/stages/s7/collapse.py:87-88
      In source order: Evaluate seen.add(key); retain side effects and discard the expression result. Then Evaluate out.append(d); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/pipeline/stages/s7/collapse.py:89-89
  End this invocation with out.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s7/collapse.py:92-97
// Source signature: _inherit_main_channel(dup: Finding, canonical: Finding) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _inherit_main_channel(dup, canonical) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s7/collapse.py:93-93
  In source order: Retain source documentation literal source_literal_93_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s7/collapse.py:95-97
  if (the source predicate dup.channel == 'main' and canonical.channel != 'main' is truthy) {
    // Source: vvaharness/pipeline/stages/s7/collapse.py:96-97
    In source order: Evaluate once 'main'; assign in source target order to canonical.channel. Then Evaluate COUNTERS.bump('s7_dedup_channel_inherited_main'); retain side effects and discard the expression result.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s7/collapse.py:100-106
// Source signature: _inherit_cluster_cwe(dup: Finding, canonical: Finding) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _inherit_cluster_cwe(dup, canonical) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s7/collapse.py:101-103
  In source order: Retain source documentation literal source_literal_101_4; it is not a model call. Then Evaluate once weakness_key(canonical.cwe); assign in source target order to key.
  // Source: vvaharness/pipeline/stages/s7/collapse.py:104-106
  if (the source predicate key and key == norm_cwe(dup.cwe) and (key != norm_cwe(canonical.cwe)) is truthy) {
    // Source: vvaharness/pipeline/stages/s7/collapse.py:105-106
    In source order: Evaluate once key; assign in source target order to canonical.cwe. Then Evaluate COUNTERS.bump('s7_dedup_cwe_inherited'); retain side effects and discard the expression result.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s7/collapse.py:109-114
// Source signature: _inherit_vuln_class(dup: Finding, canonical: Finding) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _inherit_vuln_class(dup, canonical) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s7/collapse.py:110-110
  In source order: Retain source documentation literal source_literal_110_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s7/collapse.py:112-114
  if (the source predicate canonical.vuln_class in CATCH_ALL_VULN_CLASS and dup.vuln_class not in CATCH_ALL_VULN_CLASS is truthy) {
    // Source: vvaharness/pipeline/stages/s7/collapse.py:114-114
    In source order: Evaluate once dup.vuln_class; assign in source target order to canonical.vuln_class.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s7/collapse.py:117-155
// Source signature: attach_duplicates(findings: list[Finding], canonical_of: dict[int, int], reasoning: dict[int, str], keep_same_site: set[int] | None=None) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn attach_duplicates(findings, canonical_of, reasoning, keep_same_site) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s7/collapse.py:120-120
  In source order: Retain source documentation literal source_literal_120_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s7/collapse.py:121-126
  // Source signature: root(i: int) -> int
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn root(i) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/pipeline/stages/s7/collapse.py:122-122
    In source order: Evaluate once set(); assign in source target order to seen.
    // Source: vvaharness/pipeline/stages/s7/collapse.py:123-125
    while (the source predicate i in canonical_of and i not in seen is truthy) {
      // Source: vvaharness/pipeline/stages/s7/collapse.py:124-125
      In source order: Evaluate seen.add(i); retain side effects and discard the expression result. Then Evaluate once canonical_of[i]; assign in source target order to i.
    }
    // Source: vvaharness/pipeline/stages/s7/collapse.py:126-126
    End this invocation with i.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/pipeline/stages/s7/collapse.py:127-127
  In source order: For roots, assign set(); source annotation set[int].
  // Source: vvaharness/pipeline/stages/s7/collapse.py:128-153
  for each (j, parent) in canonical_of.items() {
    // Source: vvaharness/pipeline/stages/s7/collapse.py:129-133
    In source order: Evaluate once root(parent); assign in source target order to r. Then Evaluate roots.add(r); retain side effects and discard the expression result. Then Evaluate once (findings[j], findings[r]); assign in source target order to (dj, rf). Then Evaluate _inherit_main_channel(dj, rf); retain side effects and discard the expression result. Then Evaluate _inherit_cluster_cwe(dj, rf); retain side effects and discard the expression result.
    // Source: vvaharness/pipeline/stages/s7/collapse.py:134-137
    In source order: Evaluate _inherit_vuln_class(dj, rf); retain side effects and discard the expression result. Then Evaluate once dj.file == rf.file and dj.line_start <= rf.line_end and (rf.line_start <= dj.line_end); assign in source target order to same_site.
    // Source: vvaharness/pipeline/stages/s7/collapse.py:138-150
    if (the source predicate not same_site is truthy) {
      // Source: vvaharness/pipeline/stages/s7/collapse.py:139-141
      In source order: Evaluate rf.duplicates.append(dup_location(dj, reasoning.get(j, 'duplicate'))); retain side effects and discard the expression result.
    }
    else {
      // Source: vvaharness/pipeline/stages/s7/collapse.py:142-150
      if (the source predicate keep_same_site is not None is truthy) {
        // Source: vvaharness/pipeline/stages/s7/collapse.py:144-150
        if (the source predicate j in keep_same_site and dj.line_start != rf.line_start is truthy) {
          // Source: vvaharness/pipeline/stages/s7/collapse.py:145-148
          In source order: Evaluate rf.duplicates.append(dup_location(dj, reasoning.get(j, 'duplicate'))); retain side effects and discard the expression result. Then Evaluate COUNTERS.bump('s7_dedup_same_site_kept'); retain side effects and discard the expression result.
        }
        else {
          // Source: vvaharness/pipeline/stages/s7/collapse.py:150-150
          In source order: Evaluate COUNTERS.bump('s7_dedup_same_site_discarded'); retain side effects and discard the expression result.
        }
      }
    }
    // Source: vvaharness/pipeline/stages/s7/collapse.py:151-153
    if (the source predicate dj.duplicates is truthy) {
      // Source: vvaharness/pipeline/stages/s7/collapse.py:152-153
      In source order: Evaluate rf.duplicates.extend(dj.duplicates); retain side effects and discard the expression result. Then Evaluate once []; assign in source target order to dj.duplicates.
    }
  }
  // Source: vvaharness/pipeline/stages/s7/collapse.py:154-155
  for each r in roots {
    // Source: vvaharness/pipeline/stages/s7/collapse.py:155-155
    In source order: Evaluate once dedup_locations(findings[r].duplicates); assign in source target order to findings[r].duplicates.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s7/collapse.py:158-222
// Source signature: collapse_trivial(findings: list[Finding], line_tol: int, group_lines: list[int] | None=None, min_title_overlap: float=MIN_TITLE_OVERLAP) -> dict[int, int]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn collapse_trivial(findings, line_tol, group_lines, min_title_overlap) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s7/collapse.py:161-163
  In source order: Retain source documentation literal source_literal_161_4; it is not a model call. Then Evaluate once len(findings); assign in source target order to n.
  // Source: vvaharness/pipeline/stages/s7/collapse.py:165-168
  // Source signature: group_line(i: int) -> int
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn group_line(i) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/pipeline/stages/s7/collapse.py:166-167
    if (the source predicate group_lines is not None and i < len(group_lines) is truthy) {
      // Source: vvaharness/pipeline/stages/s7/collapse.py:167-167
      End this invocation with group_lines[i].
    }
    // Source: vvaharness/pipeline/stages/s7/collapse.py:168-168
    End this invocation with findings[i].line_start.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/pipeline/stages/s7/collapse.py:171-177
  In source order: Evaluate once [group_line(i) for i in range(n)]; assign in source target order to glines. Then Evaluate once [(glines[i], findings[i].line_end + glines[i] - findings[i].line_start) for i in range(n)]; assign in source target order to spans. Then For canonical_of, assign {}; source annotation dict[int, int].
  // Source: vvaharness/pipeline/stages/s7/collapse.py:178-221
  for each j in range(n) {
    // Source: vvaharness/pipeline/stages/s7/collapse.py:179-180
    if (the source predicate j in canonical_of is truthy) {
      // Source: vvaharness/pipeline/stages/s7/collapse.py:180-180
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/pipeline/stages/s7/collapse.py:181-181
    In source order: Evaluate once findings[j]; assign in source target order to b.
    // Source: vvaharness/pipeline/stages/s7/collapse.py:182-221
    for each i in range(j) {
      // Source: vvaharness/pipeline/stages/s7/collapse.py:183-184
      if (the source predicate i in canonical_of is truthy) {
        // Source: vvaharness/pipeline/stages/s7/collapse.py:184-184
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/pipeline/stages/s7/collapse.py:185-185
      In source order: Evaluate once findings[i]; assign in source target order to a.
      // Source: vvaharness/pipeline/stages/s7/collapse.py:186-187
      if (the source predicate a.file != b.file is truthy) {
        // Source: vvaharness/pipeline/stages/s7/collapse.py:187-187
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/pipeline/stages/s7/collapse.py:188-189
      In source order: Evaluate once a.vuln_class != b.vuln_class; assign in source target order to cross_class. Then Evaluate once False; assign in source target order to shared_weakness.
      // Source: vvaharness/pipeline/stages/s7/collapse.py:190-193
      if (the source predicate a.cwe and b.cwe is truthy) {
        // Source: vvaharness/pipeline/stages/s7/collapse.py:191-193
        In source order: Evaluate once (weakness_key(a.cwe), weakness_key(b.cwe)); assign in source target order to (key_a, key_b). Then Evaluate once key_a is not None and key_a == key_b and (key_a not in _GENERIC_PARENT_CWES); assign in source target order to shared_weakness.
      }
      // Source: vvaharness/pipeline/stages/s7/collapse.py:195-196
      if (the source predicate cross_class and (not shared_weakness) is truthy) {
        // Source: vvaharness/pipeline/stages/s7/collapse.py:196-196
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/pipeline/stages/s7/collapse.py:198-202
      if (the source predicate a.cwe and b.cwe is truthy) {
        // Source: vvaharness/pipeline/stages/s7/collapse.py:199-200
        if (the source predicate cwe_conflict(a, b) is truthy) {
          // Source: vvaharness/pipeline/stages/s7/collapse.py:200-200
          Continue the immediately enclosing source loop at its next iteration.
        }
      }
      else {
        // Source: vvaharness/pipeline/stages/s7/collapse.py:201-202
        if (the source predicate a.vuln_class in STRICT_CWE_CLASS is truthy) {
          // Source: vvaharness/pipeline/stages/s7/collapse.py:202-202
          Continue the immediately enclosing source loop at its next iteration.
        }
      }
      // Source: vvaharness/pipeline/stages/s7/collapse.py:212-214
      if (the source predicate title_overlap(a, b) < min_title_overlap is truthy) {
        // Source: vvaharness/pipeline/stages/s7/collapse.py:213-213
        In source order: Evaluate COUNTERS.bump('s7_trivial_collapse_deferred_unlike_titles'); retain side effects and discard the expression result.
        // Source: vvaharness/pipeline/stages/s7/collapse.py:214-214
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/pipeline/stages/s7/collapse.py:215-216
      In source order: Evaluate once abs(glines[i] - glines[j]) <= line_tol; assign in source target order to close. Then Evaluate once spans[i][0] <= spans[j][1] and spans[j][0] <= spans[i][1]; assign in source target order to overlap.
      // Source: vvaharness/pipeline/stages/s7/collapse.py:217-221
      if (the source predicate close or overlap is truthy) {
        // Source: vvaharness/pipeline/stages/s7/collapse.py:218-219
        if (the source predicate cross_class is truthy) {
          // Source: vvaharness/pipeline/stages/s7/collapse.py:219-219
          In source order: Evaluate COUNTERS.bump('s7_trivial_collapse_cross_class_merged'); retain side effects and discard the expression result.
        }
        // Source: vvaharness/pipeline/stages/s7/collapse.py:220-220
        In source order: Evaluate once i; assign in source target order to canonical_of[j].
        // Source: vvaharness/pipeline/stages/s7/collapse.py:221-221
        Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
      }
    }
  }
  // Source: vvaharness/pipeline/stages/s7/collapse.py:222-222
  End this invocation with canonical_of.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.models import DupLocation, Finding, VulnClass` at source line 21: `source_detail/vvaharness/models/__init__.py.sudo.md`.
- `from vvaharness.rules.cwe import _GENERIC_PARENT_CWES, norm_cwe, weakness_key` at source line 22: `source_detail/vvaharness/rules/cwe.py.sudo.md`.
- `from vvaharness.util.counters import COUNTERS` at source line 23: `source_detail/vvaharness/util/counters.py.sudo.md`.
