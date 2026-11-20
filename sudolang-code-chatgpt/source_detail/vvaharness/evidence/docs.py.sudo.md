# vvaharness/evidence/docs.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/evidence/docs.py.evidence.json`. SHA-256: `cc90f2e64cbcb641507e91424235d313c8957f0e3cca97a90cd19cb73e4bdc53`.

```sudo
// Source: vvaharness/evidence/docs.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import re; preserve alias and import-time effects. Then Resolve source import from pathlib import Path, PurePosixPath; preserve alias and import-time effects. Then Resolve source import from vvaharness.evidence.read import _read_capped; preserve alias and import-time effects.
// Source: vvaharness/evidence/docs.py:24-36
In source order: Evaluate once ('THREAT_MODEL.md', 'SECURITY.md', 'ARCHITECTURE.md', 'README.md', 'README.rst', 'README.txt', 'README', 'CHANGELOG.md', 'CHANGELOG'); assign in source target order to _DOC_CANDIDATES. Then Evaluate once re.compile('(analysis|architecture|design|migration|specification|spec|threat|security|dataflow|data[_-]?flow|interface)', re.IGNORECASE); assign in source target order to _DOC_NAME_RX. Then Evaluate once 8; assign in source target order to _DOC_EXTRA_MAX.
// Source: vvaharness/evidence/docs.py:39-52
// Source signature: _breadth_pass(root: Path, found: list[tuple[str, Path]], doc_cap: int) -> tuple[list[tuple[str, str]], int]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _breadth_pass(root, found, doc_cap) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/evidence/docs.py:41-43
  In source order: Retain source documentation literal source_literal_41_4; it is not a model call. Then For docs, assign []; source annotation list[tuple[str, str]]. Then Evaluate once doc_cap; assign in source target order to budget.
  // Source: vvaharness/evidence/docs.py:44-51
  for each (name, p) in found {
    // Source: vvaharness/evidence/docs.py:45-46
    if (the source predicate budget <= 0 is truthy) {
      // Source: vvaharness/evidence/docs.py:46-46
      Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
    }
    // Source: vvaharness/evidence/docs.py:47-48
    In source order: Evaluate once min(doc_cap, max(1000, budget // 3)); assign in source target order to sub_cap. Then Evaluate once _read_capped(root, p, sub_cap); assign in source target order to body.
    // Source: vvaharness/evidence/docs.py:49-51
    if (the source predicate body is truthy) {
      // Source: vvaharness/evidence/docs.py:50-51
      In source order: Evaluate docs.append((name, body)); retain side effects and discard the expression result. Then Apply source augmented assignment budget -= len(body) with source evaluation/in-place semantics.
    }
  }
  // Source: vvaharness/evidence/docs.py:52-52
  End this invocation with (docs, budget).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/evidence/docs.py:55-62
// Source signature: _grow_one(root: Path, name: str, body: str, doc_cap: int, budget: int) -> tuple[str, int]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _grow_one(root, name, body, doc_cap, budget) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/evidence/docs.py:56-57
  In source order: Retain source documentation literal source_literal_56_4; it is not a model call. Then Evaluate once root / name; assign in source target order to p.
  // Source: vvaharness/evidence/docs.py:58-59
  if (the source predicate not p.is_file() is truthy) {
    // Source: vvaharness/evidence/docs.py:59-59
    End this invocation with (body, 0).
  }
  // Source: vvaharness/evidence/docs.py:60-61
  In source order: Evaluate once _read_capped(root, p, min(doc_cap, len(body) + budget)); assign in source target order to bigger. Then Evaluate once len(bigger) - len(body); assign in source target order to grown.
  // Source: vvaharness/evidence/docs.py:62-62
  End this invocation with (bigger, grown) if grown > 0 else (body, 0).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/evidence/docs.py:65-77
// Source signature: _grow_round(root: Path, docs: list[tuple[str, str]], budget: int, doc_cap: int) -> tuple[int, bool]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _grow_round(root, docs, budget, doc_cap) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/evidence/docs.py:67-68
  In source order: Retain source documentation literal source_literal_67_4; it is not a model call. Then Evaluate once False; assign in source target order to grew.
  // Source: vvaharness/evidence/docs.py:69-76
  for each (i, (name, body)) in enumerate(list(docs)) {
    // Source: vvaharness/evidence/docs.py:70-71
    if (the source predicate budget <= 0 is truthy) {
      // Source: vvaharness/evidence/docs.py:71-71
      Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
    }
    // Source: vvaharness/evidence/docs.py:72-72
    In source order: Evaluate once _grow_one(root, name, body, doc_cap, budget); assign in source target order to (bigger, spent).
    // Source: vvaharness/evidence/docs.py:73-76
    if (the source predicate spent > 0 is truthy) {
      // Source: vvaharness/evidence/docs.py:74-76
      In source order: Evaluate once (name, bigger); assign in source target order to docs[i]. Then Apply source augmented assignment budget -= spent with source evaluation/in-place semantics. Then Evaluate once True; assign in source target order to grew.
    }
  }
  // Source: vvaharness/evidence/docs.py:77-77
  End this invocation with (budget, grew).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/evidence/docs.py:80-89
// Source signature: _grow_pass(root: Path, docs: list[tuple[str, str]], budget: int, doc_cap: int) -> list[tuple[str, str]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _grow_pass(root, docs, budget, doc_cap) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/evidence/docs.py:82-83
  In source order: Retain source documentation literal source_literal_82_4; it is not a model call. Then Evaluate once 0; assign in source target order to guard.
  // Source: vvaharness/evidence/docs.py:84-88
  while (the source predicate budget > 0 and guard < len(docs) is truthy) {
    // Source: vvaharness/evidence/docs.py:85-85
    In source order: Evaluate once _grow_round(root, docs, budget, doc_cap); assign in source target order to (budget, grew).
    // Source: vvaharness/evidence/docs.py:86-87
    if (the source predicate not grew is truthy) {
      // Source: vvaharness/evidence/docs.py:87-87
      Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
    }
    // Source: vvaharness/evidence/docs.py:88-88
    In source order: Apply source augmented assignment guard += 1 with source evaluation/in-place semantics.
  }
  // Source: vvaharness/evidence/docs.py:89-89
  End this invocation with docs.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/evidence/docs.py:92-99
// Source signature: _select_extra_docs(full_files: list[str], seen: set[str]) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _select_extra_docs(full_files, seen) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/evidence/docs.py:93-93
  In source order: Retain source documentation literal source_literal_93_4; it is not a model call.
  // Source: vvaharness/evidence/docs.py:94-99
  End this invocation with sorted((rel for rel in full_files if PurePosixPath(rel).suffix.lower() in ('.md', '.rst') and rel not in seen and _DOC_NAME_RX.search(PurePosixPath(rel).stem)))[:_DOC_EXTRA_MAX].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/evidence/docs.py:102-115
// Source signature: _extra_docs(root: Path, full_files: list[str], seen: set[str], budget: int) -> list[tuple[str, str]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _extra_docs(root, full_files, seen, budget) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/evidence/docs.py:104-107
  In source order: Retain source documentation literal source_literal_104_4; it is not a model call. Then Evaluate once _select_extra_docs(full_files, seen); assign in source target order to extras. Then Evaluate once max(1000, budget // (len(extras) or 1)); assign in source target order to per_cap. Then For docs, assign []; source annotation list[tuple[str, str]].
  // Source: vvaharness/evidence/docs.py:108-114
  for each rel in extras {
    // Source: vvaharness/evidence/docs.py:109-110
    if (the source predicate budget <= 0 is truthy) {
      // Source: vvaharness/evidence/docs.py:110-110
      Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
    }
    // Source: vvaharness/evidence/docs.py:111-111
    In source order: Evaluate once _read_capped(root, root / rel, min(budget, per_cap)); assign in source target order to body.
    // Source: vvaharness/evidence/docs.py:112-114
    if (the source predicate body is truthy) {
      // Source: vvaharness/evidence/docs.py:113-114
      In source order: Evaluate docs.append((rel, body)); retain side effects and discard the expression result. Then Apply source augmented assignment budget -= len(body) with source evaluation/in-place semantics.
    }
  }
  // Source: vvaharness/evidence/docs.py:115-115
  End this invocation with docs.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/evidence/docs.py:118-125
// Source signature: gather_docs(root: Path, full_files: list[str], doc_cap: int) -> list[tuple[str, str]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn gather_docs(root, full_files, doc_cap) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/evidence/docs.py:119-123
  In source order: Retain source documentation literal source_literal_119_4; it is not a model call. Then Evaluate once [(name, root / name) for name in _DOC_CANDIDATES if (root / name).is_file()]; assign in source target order to found. Then Evaluate once _breadth_pass(root, found, doc_cap); assign in source target order to (docs, budget). Then Evaluate once _grow_pass(root, docs, budget, doc_cap); assign in source target order to docs. Then Evaluate once doc_cap - sum((len(b) for _, b in docs)); assign in source target order to budget.
  // Source: vvaharness/evidence/docs.py:124-124
  In source order: Evaluate once {n for n, _ in docs}; assign in source target order to seen.
  // Source: vvaharness/evidence/docs.py:125-125
  End this invocation with docs + _extra_docs(root, full_files, seen, budget).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.evidence.read import _read_capped` at source line 21: `source_detail/vvaharness/evidence/read.py.sudo.md`.
