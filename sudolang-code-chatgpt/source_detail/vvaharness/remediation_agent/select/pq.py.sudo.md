# vvaharness/remediation_agent/select/pq.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/remediation_agent/select/pq.py.evidence.json`. SHA-256: `68f5ad72af723eaf3bc62cc4313b2be58efceb21fdd955c5b8ccd20d4aa88978`.

```sudo
// Source: vvaharness/remediation_agent/select/pq.py:15-20
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import heapq; preserve alias and import-time effects. Then Resolve source import import math; preserve alias and import-time effects. Then Resolve source import from collections.abc import Callable, Sequence; preserve alias and import-time effects.
// Source: vvaharness/remediation_agent/select/pq.py:21-35
In source order: Resolve source import from typing import TypeVar; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import console; preserve alias and import-time effects. Then Evaluate once TypeVar('T'); assign in source target order to T. Then For _BAND_SCORE, assign {'CRITICAL': 9.0, 'HIGH': 7.0, 'MEDIUM': 4.0, 'LOW': 1.0, 'INFO': 0.0}; source annotation dict[str, float].
// Source: vvaharness/remediation_agent/select/pq.py:38-40
// Source signature: band_score(severity: str | None) -> float
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn band_score(severity) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/select/pq.py:39-39
  In source order: Retain source documentation literal source_literal_39_4; it is not a model call.
  // Source: vvaharness/remediation_agent/select/pq.py:40-40
  End this invocation with _BAND_SCORE.get((severity or '').strip().upper(), 0.0).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/select/pq.py:43-66
// Source signature: select_top_by_cvss(items: Sequence[T], n: int | None, score_of: Callable[[T], float | None], *, severity_of: Callable[[T], str | None] | None=None) -> list[T]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn select_top_by_cvss(items, n, score_of, severity_of) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/select/pq.py:50-50
  In source order: Retain source documentation literal source_literal_50_4; it is not a model call.
  // Source: vvaharness/remediation_agent/select/pq.py:52-53
  if (the source predicate n is None or n <= 0 is truthy) {
    // Source: vvaharness/remediation_agent/select/pq.py:53-53
    End this invocation with list(items).
  }
  // Source: vvaharness/remediation_agent/select/pq.py:55-62
  // Source signature: _score(it: T) -> float
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _score(it) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/remediation_agent/select/pq.py:56-56
    In source order: Evaluate once score_of(it); assign in source target order to s.
    // Source: vvaharness/remediation_agent/select/pq.py:58-59
    if (the source predicate s is not None and (not math.isnan(s)) is truthy) {
      // Source: vvaharness/remediation_agent/select/pq.py:59-59
      End this invocation with float(s).
    }
    // Source: vvaharness/remediation_agent/select/pq.py:60-61
    In source order: Evaluate once severity_of(it) if severity_of is not None else getattr(it, 'severity', None); assign in source target order to sev.
    // Source: vvaharness/remediation_agent/select/pq.py:62-62
    End this invocation with band_score(sev).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/remediation_agent/select/pq.py:64-65
  In source order: For heap, assign [(-_score(it), i) for i, it in enumerate(items)]; source annotation list[tuple[float, int]]. Then Evaluate heapq.heapify(heap); retain side effects and discard the expression result.
  // Source: vvaharness/remediation_agent/select/pq.py:66-66
  End this invocation with [items[heapq.heappop(heap)[1]] for _ in range(min(n, len(heap)))].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/select/pq.py:69-84
// Source signature: select_top_logged(items: Sequence[T], n: int | None, score_of: Callable[[T], float | None], *, severity_of: Callable[[T], str | None] | None=None, log_prefix: str) -> list[T]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn select_top_logged(items, n, score_of, severity_of, log_prefix) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/select/pq.py:77-80
  In source order: Retain source documentation literal source_literal_77_4; it is not a model call. Then Evaluate once len(items); assign in source target order to total. Then Evaluate once select_top_by_cvss(items, n, score_of, severity_of=severity_of); assign in source target order to selected.
  // Source: vvaharness/remediation_agent/select/pq.py:81-83
  if (the source predicate n is not None and 0 < n < total is truthy) {
    // Source: vvaharness/remediation_agent/select/pq.py:82-83
    In source order: Evaluate console.write(source_template_82_22); retain side effects and discard the expression result.
  }
  // Source: vvaharness/remediation_agent/select/pq.py:84-84
  End this invocation with selected.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/select/pq.py:87-97
// Source signature: drop_non_main_channel(items: Sequence[T], *, log_prefix: str) -> list[T]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn drop_non_main_channel(items, log_prefix) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/select/pq.py:88-92
  In source order: Retain source documentation literal source_literal_88_4; it is not a model call. Then Evaluate once [it for it in items if (it.finding.channel or '').strip().casefold() != 'posture']; assign in source target order to kept. Then Evaluate once len(items) - len(kept); assign in source target order to skipped.
  // Source: vvaharness/remediation_agent/select/pq.py:93-96
  if (the source predicate skipped is truthy) {
    // Source: vvaharness/remediation_agent/select/pq.py:94-96
    In source order: Evaluate console.write(source_template_94_22); retain side effects and discard the expression result.
  }
  // Source: vvaharness/remediation_agent/select/pq.py:97-97
  End this invocation with kept.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.util import console` at source line 23: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import console` at source line 23: `source_detail/vvaharness/util/console.py.sudo.md`.
