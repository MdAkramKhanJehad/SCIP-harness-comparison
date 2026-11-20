# vvaharness/orchestrator/cleanup.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/orchestrator/cleanup.py.evidence.json`. SHA-256: `f9f99807e4f1664822a17265b959020f1909d005958b5cb4589187e76fecc5bb`.

```sudo
// Source: vvaharness/orchestrator/cleanup.py:16-21
In source order: Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import logs; preserve alias and import-time effects. Then Retain source documentation literal source_literal_19_0; it is not a model call. Then Resolve source import import os; preserve alias and import-time effects. Then Resolve source import import shutil; preserve alias and import-time effects.
// Source: vvaharness/orchestrator/cleanup.py:22-28
In source order: Resolve source import import stat; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from vvaharness.orchestrator.artifacts import CASE_DIR_NAME, SCAN_DIR_NAME; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.events import Event; preserve alias and import-time effects. Then Evaluate once logs.get_logger(__name__); assign in source target order to log.
// Source: vvaharness/orchestrator/cleanup.py:31-39
// Source signature: _rmtree_rw(path: Path) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _rmtree_rw(path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/cleanup.py:32-32
  In source order: Retain source documentation literal source_literal_32_4; it is not a model call.
  // Source: vvaharness/orchestrator/cleanup.py:33-38
  // Source signature: _on_err(func, p, exc_info)
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _on_err(func, p, exc_info) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/orchestrator/cleanup.py:34-38
    Perform the following protected operations {
      // Source: vvaharness/orchestrator/cleanup.py:35-36
      In source order: Evaluate os.chmod(p, stat.S_IWRITE); retain side effects and discard the expression result. Then Evaluate func(p); retain side effects and discard the expression result.
    }
    // Source: vvaharness/orchestrator/cleanup.py:37-38
    On the first matching source exception Exception, in handler order {
      // Source: vvaharness/orchestrator/cleanup.py:38-38
      In source order: Perform no operation at this source statement.
    }
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/orchestrator/cleanup.py:39-39
  In source order: Evaluate shutil.rmtree(path, onerror=_on_err); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/cleanup.py:43-43
In source order: Evaluate once (SCAN_DIR_NAME, CASE_DIR_NAME); assign in source target order to _CLONE_KEEP_DEFAULT.
// Source: vvaharness/orchestrator/cleanup.py:46-48
// Source signature: _preserve_set(cfg) -> set[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _preserve_set(cfg) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/cleanup.py:47-47
  In source order: Evaluate once getattr(getattr(cfg, 'output', None), 'preserve_on_cleanup', None); assign in source target order to vals.
  // Source: vvaharness/orchestrator/cleanup.py:48-48
  End this invocation with set(vals) if vals else set(_CLONE_KEEP_DEFAULT).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/cleanup.py:51-70
// Source signature: _purge_clone(root: Path, keep: set[str]) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _purge_clone(root, keep) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/cleanup.py:52-52
  In source order: Retain source documentation literal source_literal_52_4; it is not a model call.
  // Source: vvaharness/orchestrator/cleanup.py:53-54
  if (the source predicate not root.exists() is truthy) {
    // Source: vvaharness/orchestrator/cleanup.py:54-54
    End this invocation with None.
  }
  // Source: vvaharness/orchestrator/cleanup.py:55-65
  for each child in root.iterdir() {
    // Source: vvaharness/orchestrator/cleanup.py:56-57
    if (the source predicate child.name in keep is truthy) {
      // Source: vvaharness/orchestrator/cleanup.py:57-57
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/orchestrator/cleanup.py:58-65
    if (the source predicate child.is_dir() is truthy) {
      // Source: vvaharness/orchestrator/cleanup.py:59-59
      In source order: Evaluate _rmtree_rw(child); retain side effects and discard the expression result.
    }
    else {
      // Source: vvaharness/orchestrator/cleanup.py:61-64
      Perform the following protected operations {
        // Source: vvaharness/orchestrator/cleanup.py:62-62
        In source order: Evaluate os.chmod(child, stat.S_IWRITE); retain side effects and discard the expression result.
      }
      // Source: vvaharness/orchestrator/cleanup.py:63-64
      On the first matching source exception OSError, in handler order {
        // Source: vvaharness/orchestrator/cleanup.py:64-64
        In source order: Perform no operation at this source statement.
      }
      // Source: vvaharness/orchestrator/cleanup.py:65-65
      In source order: Evaluate child.unlink(missing_ok=True); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/orchestrator/cleanup.py:68-68
  In source order: Evaluate once [c.name for c in root.iterdir() if c.name not in keep]; assign in source target order to leftover.
  // Source: vvaharness/orchestrator/cleanup.py:69-70
  if (the source predicate leftover is truthy) {
    // Source: vvaharness/orchestrator/cleanup.py:70-70
    In source order: Evaluate log.warning(Event.PURGE_LEFTOVER, root=root, count=len(leftover), items=sorted(leftover)); retain side effects and discard the expression result.
  }
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.util import logs` at source line 17: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import logs` at source line 17: `source_detail/vvaharness/util/logs.py.sudo.md`.
- `from vvaharness.orchestrator.artifacts import CASE_DIR_NAME, SCAN_DIR_NAME` at source line 25: `source_detail/vvaharness/orchestrator/artifacts.py.sudo.md`.
- `from vvaharness.util.events import Event` at source line 26: `source_detail/vvaharness/util/events.py.sudo.md`.
