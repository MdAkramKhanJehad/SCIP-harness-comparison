# vvaharness/evidence/_grouping.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/evidence/_grouping.py.evidence.json`. SHA-256: `4ba60d82d10df546eb27dcf7aaa44c138d6d85c7f2e47c25fc820c7a9e85cc99`.

```sudo
// Source: vvaharness/evidence/_grouping.py:15-20
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from collections.abc import Sequence; preserve alias and import-time effects. Then Resolve source import from itertools import zip_longest; preserve alias and import-time effects. Then Resolve source import from typing import TypeVar; preserve alias and import-time effects.
// Source: vvaharness/evidence/_grouping.py:22-22
In source order: Evaluate once TypeVar('_T'); assign in source target order to _T.
// Source: vvaharness/evidence/_grouping.py:25-36
// Source signature: _round_robin_select(groups: dict[str, list[_T]], max_total: int, keys: Sequence[str] | None=None) -> list[tuple[str, _T]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _round_robin_select(groups, max_total, keys) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/evidence/_grouping.py:27-30
  In source order: Retain source documentation literal source_literal_27_4; it is not a model call. Then Evaluate once list(keys) if keys is not None else list(groups); assign in source target order to ordered_keys. Then Evaluate once zip_longest(*(groups[k] for k in ordered_keys)); assign in source target order to rows. Then For selected, assign []; source annotation list[tuple[str, _T]].
  // Source: vvaharness/evidence/_grouping.py:31-35
  for each row in rows {
    // Source: vvaharness/evidence/_grouping.py:32-33
    In source order: Evaluate once zip(ordered_keys, row, strict=True); assign in source target order to pairs. Then Evaluate selected.extend(((k, item) for k, item in pairs if item is not None)); retain side effects and discard the expression result.
    // Source: vvaharness/evidence/_grouping.py:34-35
    if (the source predicate len(selected) >= max_total is truthy) {
      // Source: vvaharness/evidence/_grouping.py:35-35
      Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
    }
  }
  // Source: vvaharness/evidence/_grouping.py:36-36
  End this invocation with selected[:max_total].
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

No statically resolved in-checkout import; external calls remain explicit dependency boundaries.
