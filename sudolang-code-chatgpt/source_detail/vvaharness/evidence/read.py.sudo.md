# vvaharness/evidence/read.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/evidence/read.py.evidence.json`. SHA-256: `56fe34b173e46148a5df0e668780b5ea90b996315c56c56e834996da8f8d1980`.

```sudo
// Source: vvaharness/evidence/read.py:15-20
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import errlog as _errlog; preserve alias and import-time effects.
// Source: vvaharness/evidence/read.py:23-33
// Source signature: _contained(root: Path, p: Path) -> Path | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _contained(root, p) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/evidence/read.py:24-24
  In source order: Retain source documentation literal source_literal_24_4; it is not a model call.
  // Source: vvaharness/evidence/read.py:25-28
  Perform the following protected operations {
    // Source: vvaharness/evidence/read.py:26-26
    In source order: Evaluate once p.resolve(strict=True); assign in source target order to rp.
  }
  // Source: vvaharness/evidence/read.py:27-28
  On the first matching source exception OSError, in handler order {
    // Source: vvaharness/evidence/read.py:28-28
    End this invocation with None.
  }
  // Source: vvaharness/evidence/read.py:29-32
  Perform the following protected operations {
    // Source: vvaharness/evidence/read.py:30-30
    In source order: Evaluate once root.resolve(strict=True); assign in source target order to rroot.
  }
  // Source: vvaharness/evidence/read.py:31-32
  On the first matching source exception OSError, in handler order {
    // Source: vvaharness/evidence/read.py:32-32
    End this invocation with None.
  }
  // Source: vvaharness/evidence/read.py:33-33
  End this invocation with rp if rp.is_relative_to(rroot) else None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/evidence/read.py:36-39
// Source signature: _cap_text(txt: str, cap_chars: int) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _cap_text(txt, cap_chars) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/evidence/read.py:37-38
  if (the source predicate len(txt) > cap_chars is truthy) {
    // Source: vvaharness/evidence/read.py:38-38
    End this invocation with txt[:cap_chars] + source_template_38_33.
  }
  // Source: vvaharness/evidence/read.py:39-39
  End this invocation with txt.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/evidence/read.py:42-58
// Source signature: _read_capped(root: Path, p: Path, cap_chars: int, *, whole_or_nothing: bool=False) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _read_capped(root, p, cap_chars, whole_or_nothing) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/evidence/read.py:44-45
  In source order: Retain source documentation literal source_literal_44_4; it is not a model call. Then Evaluate once _contained(root, p); assign in source target order to rp.
  // Source: vvaharness/evidence/read.py:46-51
  if (the source predicate rp is None is truthy) {
    // Source: vvaharness/evidence/read.py:48-50
    In source order: Evaluate _errlog.log('s2', 'containment', source_template_49_20, reason='containment_refused', recovered=True); retain side effects and discard the expression result.
    // Source: vvaharness/evidence/read.py:51-51
    End this invocation with ''.
  }
  // Source: vvaharness/evidence/read.py:52-55
  Perform the following protected operations {
    // Source: vvaharness/evidence/read.py:53-53
    In source order: Evaluate once rp.read_text(encoding='utf-8', errors='replace'); assign in source target order to txt.
  }
  // Source: vvaharness/evidence/read.py:54-55
  On the first matching source exception Exception, in handler order {
    // Source: vvaharness/evidence/read.py:55-55
    In source order: Evaluate once ''; assign in source target order to txt.
  }
  // Source: vvaharness/evidence/read.py:56-57
  if (the source predicate whole_or_nothing and len(txt) > cap_chars is truthy) {
    // Source: vvaharness/evidence/read.py:57-57
    End this invocation with ''.
  }
  // Source: vvaharness/evidence/read.py:58-58
  End this invocation with _cap_text(txt, cap_chars).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.util import errlog as _errlog` at source line 20: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import errlog as _errlog` at source line 20: `source_detail/vvaharness/util/errlog.py.sudo.md`.
