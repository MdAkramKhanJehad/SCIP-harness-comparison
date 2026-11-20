# vendor/context_graph_sdk/src/context_graph_sdk/workspace/locking.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vendor/context_graph_sdk/src/context_graph_sdk/workspace/locking.py.evidence.json`. SHA-256: `32b69c54c814df92f74810fd64da0c8cc2c8e160b251b2be90a79b0e9d430d6d`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/locking.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import errno; preserve alias and import-time effects. Then Resolve source import import importlib; preserve alias and import-time effects. Then Resolve source import import os; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/locking.py:22-23
In source order: Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from typing import BinaryIO, Protocol, cast; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/locking.py:26-31
interface _PosixLocking {
  Describe the source Python type, preserving its base/metaclass expression order: Protocol.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/locking.py:27-29
  In source order: For LOCK_EX, declare without assigning a value; source annotation int. Then For LOCK_NB, declare without assigning a value; source annotation int. Then For LOCK_UN, declare without assigning a value; source annotation int.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/locking.py:31-31
  // Source signature: flock(self, file_descriptor: BinaryIO, operation: int) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn flock(self, file_descriptor, operation) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/locking.py:31-31
    In source order: Evaluate ...; retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/locking.py:34-38
interface _WindowsLocking {
  Describe the source Python type, preserving its base/metaclass expression order: Protocol.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/locking.py:35-36
  In source order: For LK_NBLCK, declare without assigning a value; source annotation int. Then For LK_UNLCK, declare without assigning a value; source annotation int.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/locking.py:38-38
  // Source signature: locking(self, file_descriptor: int, mode: int, byte_count: int) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn locking(self, file_descriptor, mode, byte_count) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/locking.py:38-38
    In source order: Evaluate ...; retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/locking.py:41-61
interface WorkspaceFileLock {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/locking.py:42-42
  In source order: Retain source documentation literal source_literal_42_4; it is not a model call.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/locking.py:44-52
  // Source signature: __init__(self, path: Path) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self, path) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/locking.py:45-46
    In source order: Evaluate once path.open('a+b'); assign in source target order to self._file. Then Evaluate once False; assign in source target order to self._locked.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/locking.py:47-52
    Perform the following protected operations {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/locking.py:48-49
      In source order: Evaluate _acquire_file_lock(self._file); retain side effects and discard the expression result. Then Evaluate once True; assign in source target order to self._locked.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/locking.py:50-52
    On the first matching source exception Exception, in handler order {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/locking.py:51-51
      In source order: Evaluate self._file.close(); retain side effects and discard the expression result.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/locking.py:52-52
      Raise the currently handled exception.
    }
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/locking.py:54-61
  // Source signature: release(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn release(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/locking.py:55-56
    if (the source predicate not self._locked is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/locking.py:56-56
      End this invocation with None.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/locking.py:57-61
    Perform the following protected operations {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/locking.py:58-58
      In source order: Evaluate _release_file_lock(self._file); retain side effects and discard the expression result.
    }
    On every exit from this protected/handler/normal-completion region {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/locking.py:60-61
      In source order: Evaluate once False; assign in source target order to self._locked. Then Evaluate self._file.close(); retain side effects and discard the expression result.
    }
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/locking.py:64-68
// Source signature: _acquire_file_lock(lock_file: BinaryIO) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _acquire_file_lock(lock_file) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/locking.py:65-67
  if (the source predicate os.name == 'nt' is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/locking.py:66-66
    In source order: Evaluate _acquire_windows_lock(lock_file); retain side effects and discard the expression result.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/locking.py:67-67
    End this invocation with None.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/locking.py:68-68
  In source order: Evaluate _acquire_posix_lock(lock_file); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/locking.py:71-75
// Source signature: _release_file_lock(lock_file: BinaryIO) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _release_file_lock(lock_file) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/locking.py:72-74
  if (the source predicate os.name == 'nt' is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/locking.py:73-73
    In source order: Evaluate _release_windows_lock(lock_file); retain side effects and discard the expression result.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/locking.py:74-74
    End this invocation with None.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/locking.py:75-75
  In source order: Evaluate _release_posix_lock(lock_file); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/locking.py:78-79
// Source signature: _load_posix_locking() -> _PosixLocking
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _load_posix_locking() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/locking.py:79-79
  End this invocation with cast(_PosixLocking, importlib.import_module('fcntl')).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/locking.py:82-89
// Source signature: _acquire_posix_lock(lock_file: BinaryIO) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _acquire_posix_lock(lock_file) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/locking.py:83-83
  In source order: Evaluate once _load_posix_locking(); assign in source target order to posix_locking.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/locking.py:84-89
  Perform the following protected operations {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/locking.py:85-85
    In source order: Evaluate posix_locking.flock(lock_file, posix_locking.LOCK_EX | posix_locking.LOCK_NB); retain side effects and discard the expression result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/locking.py:86-89
  On the first matching source exception OSError as exc, in handler order {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/locking.py:87-88
    if (the source predicate exc.errno in {errno.EACCES, errno.EAGAIN} is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/locking.py:88-88
      Raise BlockingIOError(errno.EWOULDBLOCK, 'workspace lock is already held') with explicit source cause exc.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/locking.py:89-89
    Raise the currently handled exception.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/locking.py:92-94
// Source signature: _release_posix_lock(lock_file: BinaryIO) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _release_posix_lock(lock_file) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/locking.py:93-94
  In source order: Evaluate once _load_posix_locking(); assign in source target order to posix_locking. Then Evaluate posix_locking.flock(lock_file, posix_locking.LOCK_UN); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/locking.py:97-98
// Source signature: _load_windows_locking() -> _WindowsLocking
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _load_windows_locking() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/locking.py:98-98
  End this invocation with cast(_WindowsLocking, importlib.import_module('msvcrt')).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/locking.py:101-112
// Source signature: _acquire_windows_lock(lock_file: BinaryIO) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _acquire_windows_lock(lock_file) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/locking.py:102-102
  In source order: Evaluate once _load_windows_locking(); assign in source target order to windows_locking.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/locking.py:103-105
  if (the source predicate os.fstat(lock_file.fileno()).st_size == 0 is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/locking.py:104-105
    In source order: Evaluate lock_file.write(b'\x00'); retain side effects and discard the expression result. Then Evaluate lock_file.flush(); retain side effects and discard the expression result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/locking.py:106-106
  In source order: Evaluate lock_file.seek(0); retain side effects and discard the expression result.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/locking.py:107-112
  Perform the following protected operations {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/locking.py:108-108
    In source order: Evaluate windows_locking.locking(lock_file.fileno(), windows_locking.LK_NBLCK, 1); retain side effects and discard the expression result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/locking.py:109-112
  On the first matching source exception OSError as exc, in handler order {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/locking.py:110-111
    if (the source predicate exc.errno in {errno.EACCES, errno.EAGAIN, errno.EDEADLK} is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/locking.py:111-111
      Raise BlockingIOError(errno.EWOULDBLOCK, 'workspace lock is already held') with explicit source cause exc.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/locking.py:112-112
    Raise the currently handled exception.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/locking.py:115-118
// Source signature: _release_windows_lock(lock_file: BinaryIO) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _release_windows_lock(lock_file) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/locking.py:116-118
  In source order: Evaluate once _load_windows_locking(); assign in source target order to windows_locking. Then Evaluate lock_file.seek(0); retain side effects and discard the expression result. Then Evaluate windows_locking.locking(lock_file.fileno(), windows_locking.LK_UNLCK, 1); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

No statically resolved in-checkout import; external calls remain explicit dependency boundaries.
