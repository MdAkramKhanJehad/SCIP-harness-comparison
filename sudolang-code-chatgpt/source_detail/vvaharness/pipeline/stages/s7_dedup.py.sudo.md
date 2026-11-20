# vvaharness/pipeline/stages/s7_dedup.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/pipeline/stages/s7_dedup.py.evidence.json`. SHA-256: `436ed80c23854bfaea87ff8023dd924dd4443da942fabd4d6f5fe04dca6ea5b1`.

```sudo
// Source: vvaharness/pipeline/stages/s7_dedup.py:16-26
In source order: Retain source documentation literal source_literal_16_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from vvaharness.models import ContextPackage, DroppedFinding, Finding; preserve alias and import-time effects. Then Resolve source import from vvaharness.pipeline.stages.s7.collapse import TRIVIAL_REASON, attach_duplicates, collapse_trivial, cwe_conflict; preserve alias and import-time effects. Then Resolve source import from vvaharness.pipeline.stages.s7.session import semantic_dedup; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s7_dedup.py:27-32
In source order: Resolve source import from vvaharness.util import console, logs; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.config import knob; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.counters import COUNTERS; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.events import Event; preserve alias and import-time effects. Then Evaluate once logs.get_logger(__name__); assign in source target order to log.
// Source: vvaharness/pipeline/stages/s7_dedup.py:35-59
// Source signature: prefilter(findings: list[Finding], line_tol: int, group_lines: list[int] | None=None) -> tuple[list[Finding], list[DroppedFinding]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn prefilter(findings, line_tol, group_lines) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s7_dedup.py:38-38
  In source order: Retain source documentation literal source_literal_38_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s7_dedup.py:39-40
  if (the source predicate len(findings) <= 1 is truthy) {
    // Source: vvaharness/pipeline/stages/s7_dedup.py:40-40
    End this invocation with (list(findings), []).
  }
  // Source: vvaharness/pipeline/stages/s7_dedup.py:43-58
  In source order: Evaluate once collapse_trivial(findings, line_tol, group_lines); assign in source target order to canonical_of. Then Evaluate attach_duplicates(findings, canonical_of, {j: TRIVIAL_REASON for j in canonical_of}); retain side effects and discard the expression result. Then Evaluate once [f for i, f in enumerate(findings) if i not in canonical_of]; assign in source target order to keep. Then Evaluate once [DroppedFinding(file=f.file, line=f.line_start, vuln_class=f.vuln_class, title=f.title, chunk_id=f.chunk_id, reason='DUPLICATE', detail=TRIVIAL_REASON) for i, f in enumerate(findings) if i in canonical_of]; assign in source target order to dropped.
  // Source: vvaharness/pipeline/stages/s7_dedup.py:59-59
  End this invocation with (keep, dropped).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s7_dedup.py:62-138
// Source signature: run(verified: list[Finding], cfg, *, label: str='s7-dedup', ctx: ContextPackage) -> tuple[list[Finding], list[DroppedFinding]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn run(verified, cfg, label, ctx) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s7_dedup.py:64-64
  In source order: Retain source documentation literal source_literal_64_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s7_dedup.py:65-66
  if (the source predicate len(verified) <= 1 is truthy) {
    // Source: vvaharness/pipeline/stages/s7_dedup.py:66-66
    End this invocation with (list(verified), []).
  }
  // Source: vvaharness/pipeline/stages/s7_dedup.py:68-76
  In source order: Evaluate once getattr(cfg.step7_dedup, 'line_tolerance', 3); assign in source target order to line_tol. Then Evaluate once [int(getattr(f, 'pre_anchor_line', 0)) or int(f.line_start) for f in verified]; assign in source target order to group_lines. Then Evaluate once collapse_trivial(verified, line_tol, group_lines); assign in source target order to canonical_of. Then For reasoning, assign {j: TRIVIAL_REASON for j in canonical_of}; source annotation dict[int, str]. Then Evaluate once [i for i in range(len(verified)) if i not in canonical_of]; assign in source target order to unresolved.
  // Source: vvaharness/pipeline/stages/s7_dedup.py:77-82
  In source order: Evaluate console.counts(label, 'pre-filter', trivial_dups=len(canonical_of), unresolved=len(unresolved)); retain side effects and discard the expression result. Then For keep_same_site, assign set() if knob(cfg, 'step7_dedup.per_sink_keep', True) else None; source annotation set[int] | None.
  // Source: vvaharness/pipeline/stages/s7_dedup.py:83-85
  if (the source predicate keep_same_site is not None is truthy) {
    // Source: vvaharness/pipeline/stages/s7_dedup.py:85-85
    In source order: Evaluate keep_same_site.update(canonical_of); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s7_dedup.py:87-90
  // Source signature: root(i: int) -> int
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn root(i) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/pipeline/stages/s7_dedup.py:88-89
    while (the source predicate i in canonical_of is truthy) {
      // Source: vvaharness/pipeline/stages/s7_dedup.py:89-89
      In source order: Evaluate once canonical_of[i]; assign in source target order to i.
    }
    // Source: vvaharness/pipeline/stages/s7_dedup.py:90-90
    End this invocation with i.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/pipeline/stages/s7_dedup.py:92-112
  if (the source predicate len(unresolved) >= 2 and getattr(cfg.step7_dedup, 'semantic', True) is truthy) {
    // Source: vvaharness/pipeline/stages/s7_dedup.py:93-94
    In source order: Evaluate once semantic_dedup(verified, unresolved, cfg, ctx=ctx, label=label); assign in source target order to sem. Then Evaluate once 0; assign in source target order to blocked.
    // Source: vvaharness/pipeline/stages/s7_dedup.py:95-109
    for each (local_idx, local_canon, why, independent_sites) in sem {
      // Source: vvaharness/pipeline/stages/s7_dedup.py:97-98
      In source order: Evaluate once unresolved[local_idx]; assign in source target order to g_idx. Then Evaluate once unresolved[local_canon]; assign in source target order to g_canon.
      // Source: vvaharness/pipeline/stages/s7_dedup.py:99-100
      if (the source predicate g_idx in canonical_of or g_canon >= g_idx is truthy) {
        // Source: vvaharness/pipeline/stages/s7_dedup.py:100-100
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/pipeline/stages/s7_dedup.py:102-104
      if (the source predicate cwe_conflict(verified[g_idx], verified[root(g_canon)]) is truthy) {
        // Source: vvaharness/pipeline/stages/s7_dedup.py:103-103
        In source order: Apply source augmented assignment blocked += 1 with source evaluation/in-place semantics.
        // Source: vvaharness/pipeline/stages/s7_dedup.py:104-104
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/pipeline/stages/s7_dedup.py:105-106
      In source order: Evaluate once g_canon; assign in source target order to canonical_of[g_idx]. Then Evaluate once why; assign in source target order to reasoning[g_idx].
      // Source: vvaharness/pipeline/stages/s7_dedup.py:108-109
      if (the source predicate independent_sites and keep_same_site is not None is truthy) {
        // Source: vvaharness/pipeline/stages/s7_dedup.py:109-109
        In source order: Evaluate keep_same_site.add(g_idx); retain side effects and discard the expression result.
      }
    }
    // Source: vvaharness/pipeline/stages/s7_dedup.py:110-112
    if (the source predicate blocked is truthy) {
      // Source: vvaharness/pipeline/stages/s7_dedup.py:111-112
      In source order: Evaluate COUNTERS.bump('s7_dedup_cwe_conflict_blocked', blocked); retain side effects and discard the expression result. Then Evaluate log.warning(Event.S7_CWE_CONFLICT_BLOCKED, stage=label, blocked=blocked); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/pipeline/stages/s7_dedup.py:115-118
  In source order: Evaluate attach_duplicates(verified, canonical_of, reasoning, keep_same_site=keep_same_site); retain side effects and discard the expression result. Then For canonical, assign []; source annotation list[Finding]. Then For new_index_of, assign {}; source annotation dict[int, int].
  // Source: vvaharness/pipeline/stages/s7_dedup.py:119-122
  for each (i, f) in enumerate(verified) {
    // Source: vvaharness/pipeline/stages/s7_dedup.py:120-122
    if (the source predicate i not in canonical_of is truthy) {
      // Source: vvaharness/pipeline/stages/s7_dedup.py:121-122
      In source order: Evaluate once len(canonical); assign in source target order to new_index_of[i]. Then Evaluate canonical.append(f); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/pipeline/stages/s7_dedup.py:124-124
  In source order: For dropped, assign []; source annotation list[DroppedFinding].
  // Source: vvaharness/pipeline/stages/s7_dedup.py:125-134
  for each (i, f) in enumerate(verified) {
    // Source: vvaharness/pipeline/stages/s7_dedup.py:126-134
    if (the source predicate i in canonical_of is truthy) {
      // Source: vvaharness/pipeline/stages/s7_dedup.py:127-134
      In source order: Evaluate once root(i); assign in source target order to r. Then Evaluate dropped.append(DroppedFinding(file=f.file, line=f.line_start, vuln_class=f.vuln_class, title=f.title, chunk_id=f.chunk_id, reason='DUPLICATE', detail=reasoning.get(i, 'duplicate'), canonical_idx=new_index_of.get(r))); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/pipeline/stages/s7_dedup.py:136-137
  In source order: Evaluate console.counts(label, 'done', canonical=len(canonical), duplicates_collapsed=len(dropped)); retain side effects and discard the expression result.
  // Source: vvaharness/pipeline/stages/s7_dedup.py:138-138
  End this invocation with (canonical, dropped).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.models import ContextPackage, DroppedFinding, Finding` at source line 19: `source_detail/vvaharness/models/__init__.py.sudo.md`.
- `from vvaharness.pipeline.stages.s7.collapse import TRIVIAL_REASON, attach_duplicates, collapse_trivial, cwe_conflict` at source line 20: `source_detail/vvaharness/pipeline/stages/s7/collapse.py.sudo.md`.
- `from vvaharness.pipeline.stages.s7.session import semantic_dedup` at source line 26: `source_detail/vvaharness/pipeline/stages/s7/session.py.sudo.md`.
- `from vvaharness.util import console, logs` at source line 27: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import console, logs` at source line 27: `source_detail/vvaharness/util/console.py.sudo.md`.
- `from vvaharness.util import console, logs` at source line 27: `source_detail/vvaharness/util/logs.py.sudo.md`.
- `from vvaharness.util.config import knob` at source line 28: `source_detail/vvaharness/util/config.py.sudo.md`.
- `from vvaharness.util.counters import COUNTERS` at source line 29: `source_detail/vvaharness/util/counters.py.sudo.md`.
- `from vvaharness.util.events import Event` at source line 30: `source_detail/vvaharness/util/events.py.sudo.md`.
