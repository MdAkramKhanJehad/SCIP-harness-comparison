# vvaharness/backends/llm/cli/cancel.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/backends/llm/cli/cancel.py.evidence.json`. SHA-256: `2af6b829982b7b16b5a873439910097705973c36be9c60318fe4d4a8df263132`.

```sudo
// Source: vvaharness/backends/llm/cli/cancel.py:15-20
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import os; preserve alias and import-time effects. Then Resolve source import import signal; preserve alias and import-time effects. Then Resolve source import import subprocess; preserve alias and import-time effects.
// Source: vvaharness/backends/llm/cli/cancel.py:21-34
In source order: Resolve source import import threading; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import logs; preserve alias and import-time effects. Then Evaluate once logs.get_logger(__name__); assign in source target order to log. Then Evaluate once threading.Event(); assign in source target order to _ABORT. Then Evaluate once threading.Lock(); assign in source target order to _LIVE_LOCK.
// Source: vvaharness/backends/llm/cli/cancel.py:35-35
In source order: For _LIVE, assign set(); source annotation set[subprocess.Popen].
// Source: vvaharness/backends/llm/cli/cancel.py:38-39
// Source signature: aborted() -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn aborted() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli/cancel.py:39-39
  End this invocation with _ABORT.is_set().
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cli/cancel.py:43-43
In source order: For _NEW_GROUP_KW, assign {} if os.name == 'nt' else {'start_new_session': True}; source annotation dict.
// Source: vvaharness/backends/llm/cli/cancel.py:46-70
// Source signature: _kill_tree(proc: subprocess.Popen) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _kill_tree(proc) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli/cancel.py:47-47
  In source order: Retain source documentation literal source_literal_47_4; it is not a model call.
  // Source: vvaharness/backends/llm/cli/cancel.py:49-50
  if (the source predicate proc.poll() is not None is truthy) {
    // Source: vvaharness/backends/llm/cli/cancel.py:50-50
    End this invocation with None.
  }
  // Source: vvaharness/backends/llm/cli/cancel.py:51-70
  Perform the following protected operations {
    // Source: vvaharness/backends/llm/cli/cancel.py:52-55
    if (the source predicate os.name == 'nt' is truthy) {
      // Source: vvaharness/backends/llm/cli/cancel.py:53-54
      In source order: Evaluate subprocess.run(['taskkill', '/F', '/T', '/PID', str(proc.pid)], capture_output=True, timeout=10); retain side effects and discard the expression result.
      // Source: vvaharness/backends/llm/cli/cancel.py:55-55
      End this invocation with None.
    }
    // Source: vvaharness/backends/llm/cli/cancel.py:56-59
    Perform the following protected operations {
      // Source: vvaharness/backends/llm/cli/cancel.py:57-57
      In source order: Evaluate once os.getpgid(proc.pid); assign in source target order to pgid.
    }
    // Source: vvaharness/backends/llm/cli/cancel.py:58-59
    On the first matching source exception (OSError, AttributeError), in handler order {
      // Source: vvaharness/backends/llm/cli/cancel.py:59-59
      In source order: Evaluate once None; assign in source target order to pgid.
    }
    // Source: vvaharness/backends/llm/cli/cancel.py:61-64
    if (the source predicate pgid is not None and pgid != os.getpgrp() is truthy) {
      // Source: vvaharness/backends/llm/cli/cancel.py:62-62
      In source order: Evaluate os.killpg(pgid, signal.SIGKILL); retain side effects and discard the expression result.
    }
    else {
      // Source: vvaharness/backends/llm/cli/cancel.py:64-64
      In source order: Evaluate proc.kill(); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/backends/llm/cli/cancel.py:65-70
  On the first matching source exception Exception, in handler order {
    // Source: vvaharness/backends/llm/cli/cancel.py:67-70
    Perform the following protected operations {
      // Source: vvaharness/backends/llm/cli/cancel.py:68-68
      In source order: Evaluate proc.kill(); retain side effects and discard the expression result.
    }
    // Source: vvaharness/backends/llm/cli/cancel.py:69-70
    On the first matching source exception Exception, in handler order {
      // Source: vvaharness/backends/llm/cli/cancel.py:70-70
      In source order: Perform no operation at this source statement.
    }
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cli/cancel.py:73-90
// Source signature: _stop_tree(proc: subprocess.Popen, grace: float) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _stop_tree(proc, grace) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli/cancel.py:74-74
  In source order: Retain source documentation literal source_literal_74_4; it is not a model call.
  // Source: vvaharness/backends/llm/cli/cancel.py:76-77
  if (the source predicate proc.poll() is not None is truthy) {
    // Source: vvaharness/backends/llm/cli/cancel.py:77-77
    End this invocation with None.
  }
  // Source: vvaharness/backends/llm/cli/cancel.py:78-80
  if (the source predicate os.name == 'nt' is truthy) {
    // Source: vvaharness/backends/llm/cli/cancel.py:79-79
    In source order: Evaluate _kill_tree(proc); retain side effects and discard the expression result.
    // Source: vvaharness/backends/llm/cli/cancel.py:80-80
    End this invocation with None.
  }
  // Source: vvaharness/backends/llm/cli/cancel.py:81-86
  Perform the following protected operations {
    // Source: vvaharness/backends/llm/cli/cancel.py:82-82
    In source order: Evaluate once os.getpgid(proc.pid); assign in source target order to pgid.
    // Source: vvaharness/backends/llm/cli/cancel.py:83-84
    if (the source predicate pgid != os.getpgrp() is truthy) {
      // Source: vvaharness/backends/llm/cli/cancel.py:84-84
      In source order: Evaluate os.killpg(pgid, signal.SIGINT); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/backends/llm/cli/cancel.py:85-86
  On the first matching source exception (OSError, AttributeError), in handler order {
    // Source: vvaharness/backends/llm/cli/cancel.py:86-86
    In source order: Perform no operation at this source statement.
  }
  // Source: vvaharness/backends/llm/cli/cancel.py:87-90
  Perform the following protected operations {
    // Source: vvaharness/backends/llm/cli/cancel.py:88-88
    In source order: Evaluate proc.wait(timeout=grace); retain side effects and discard the expression result.
  }
  // Source: vvaharness/backends/llm/cli/cancel.py:89-90
  On the first matching source exception subprocess.TimeoutExpired, in handler order {
    // Source: vvaharness/backends/llm/cli/cancel.py:90-90
    In source order: Evaluate _kill_tree(proc); retain side effects and discard the expression result.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cli/cancel.py:94-94
In source order: For _ABORT_HOOKS, assign []; source annotation list.
// Source: vvaharness/backends/llm/cli/cancel.py:97-100
// Source signature: register_abort_hook(fn) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn register_abort_hook(fn) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli/cancel.py:98-98
  In source order: Retain source documentation literal source_literal_98_4; it is not a model call.
  // Source: vvaharness/backends/llm/cli/cancel.py:99-100
  if (the source predicate fn not in _ABORT_HOOKS is truthy) {
    // Source: vvaharness/backends/llm/cli/cancel.py:100-100
    In source order: Evaluate _ABORT_HOOKS.append(fn); retain side effects and discard the expression result.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cli/cancel.py:103-116
// Source signature: abort() -> int
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn abort() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli/cancel.py:104-105
  In source order: Retain source documentation literal source_literal_104_4; it is not a model call. Then Evaluate _ABORT.set(); retain side effects and discard the expression result.
  // Source: vvaharness/backends/llm/cli/cancel.py:106-107
  Enter source context managers left-to-right: _LIVE_LOCK {
    // Source: vvaharness/backends/llm/cli/cancel.py:107-107
    In source order: Evaluate once list(_LIVE); assign in source target order to procs.
  }
  Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
  // Source: vvaharness/backends/llm/cli/cancel.py:108-109
  for each p in procs {
    // Source: vvaharness/backends/llm/cli/cancel.py:109-109
    In source order: Evaluate _kill_tree(p); retain side effects and discard the expression result.
  }
  // Source: vvaharness/backends/llm/cli/cancel.py:111-115
  for each hook in list(_ABORT_HOOKS) {
    // Source: vvaharness/backends/llm/cli/cancel.py:112-115
    Perform the following protected operations {
      // Source: vvaharness/backends/llm/cli/cancel.py:113-113
      In source order: Evaluate hook(); retain side effects and discard the expression result.
    }
    // Source: vvaharness/backends/llm/cli/cancel.py:114-115
    On the first matching source exception Exception, in handler order {
      // Source: vvaharness/backends/llm/cli/cancel.py:115-115
      In source order: Perform no operation at this source statement.
    }
  }
  // Source: vvaharness/backends/llm/cli/cancel.py:116-116
  End this invocation with len(procs).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cli/cancel.py:119-121
// Source signature: reset_abort() -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn reset_abort() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli/cancel.py:120-121
  In source order: Retain source documentation literal source_literal_120_4; it is not a model call. Then Evaluate _ABORT.clear(); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.util import logs` at source line 23: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import logs` at source line 23: `source_detail/vvaharness/util/logs.py.sudo.md`.
