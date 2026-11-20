# vvaharness/pipeline/stages/s4/batching.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/pipeline/stages/s4/batching.py.evidence.json`. SHA-256: `1a742853917b54d4c967e77590a7ca3862e5be4541cb81fabce909d37215a853`.

```sudo
// Source: vvaharness/pipeline/stages/s4/batching.py:15-19
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from vvaharness.models import InvestigationUnit, UnitSize; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s4/batching.py:22-24
// Source signature: _overlap(a: InvestigationUnit, b: InvestigationUnit) -> int
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _overlap(a, b) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s4/batching.py:23-23
  In source order: Retain source documentation literal source_literal_23_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s4/batching.py:24-24
  End this invocation with len(set(a.files) & set(b.files)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s4/batching.py:27-31
// Source signature: _best_partner(seed: list[InvestigationUnit], pool: list[InvestigationUnit]) -> InvestigationUnit
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _best_partner(seed, pool) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s4/batching.py:29-30
  In source order: Retain source documentation literal source_literal_29_4; it is not a model call. Then Evaluate once {f for u in seed for f in u.files}; assign in source target order to seed_files.
  // Source: vvaharness/pipeline/stages/s4/batching.py:31-31
  End this invocation with min(pool, key=lambda u: (-len(seed_files & set(u.files)), u.risk_rank, u.id)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s4/batching.py:34-48
// Source signature: plan_batches(units: list[InvestigationUnit], size: int) -> list[list[InvestigationUnit]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn plan_batches(units, size) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s4/batching.py:35-35
  In source order: Retain source documentation literal source_literal_35_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s4/batching.py:36-37
  if (the source predicate size <= 1 is truthy) {
    // Source: vvaharness/pipeline/stages/s4/batching.py:37-37
    End this invocation with [[u] for u in units].
  }
  // Source: vvaharness/pipeline/stages/s4/batching.py:38-42
  In source order: Evaluate once sorted(units, key=lambda u: (u.risk_rank, u.id)); assign in source target order to ordered. Then Evaluate once [[u] for u in ordered if u.size == UnitSize.LARGE]; assign in source target order to large. Then Evaluate once [u for u in ordered if u.size != UnitSize.LARGE]; assign in source target order to pool. Then For batches, assign []; source annotation list[list[InvestigationUnit]].
  // Source: vvaharness/pipeline/stages/s4/batching.py:43-47
  while (the source predicate pool is truthy) {
    // Source: vvaharness/pipeline/stages/s4/batching.py:44-44
    In source order: Evaluate once [pool.pop(0)]; assign in source target order to batch.
    // Source: vvaharness/pipeline/stages/s4/batching.py:45-46
    while (the source predicate pool and len(batch) < size is truthy) {
      // Source: vvaharness/pipeline/stages/s4/batching.py:46-46
      In source order: Evaluate batch.append(pool.pop(pool.index(_best_partner(batch, pool)))); retain side effects and discard the expression result.
    }
    // Source: vvaharness/pipeline/stages/s4/batching.py:47-47
    In source order: Evaluate batches.append(batch); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s4/batching.py:48-48
  End this invocation with batches + large.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.models import InvestigationUnit, UnitSize` at source line 19: `source_detail/vvaharness/models/__init__.py.sudo.md`.
