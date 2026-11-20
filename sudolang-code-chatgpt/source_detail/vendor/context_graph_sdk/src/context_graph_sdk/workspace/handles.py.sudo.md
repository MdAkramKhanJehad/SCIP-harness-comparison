# vendor/context_graph_sdk/src/context_graph_sdk/workspace/handles.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vendor/context_graph_sdk/src/context_graph_sdk/workspace/handles.py.evidence.json`. SHA-256: `d3075f89749d169db3ced3f28a351581a09aee553203f471496e6450ed3d1005`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/handles.py:15-29
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import threading; preserve alias and import-time effects. Then Resolve source import import time; preserve alias and import-time effects. Then Resolve source import from contextlib import AbstractContextManager; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/handles.py:30-32
In source order: Resolve source import from types import TracebackType; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.models import SnapshotLocator; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/handles.py:35-55
interface _SnapshotLease {
  Describe the source Python type, preserving its base/metaclass expression order: AbstractContextManager['_SnapshotLease'].
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/handles.py:36-39
  // Source signature: __init__(self, registry: SnapshotLeaseRegistry, locator: SnapshotLocator) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self, registry, locator) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/handles.py:37-39
    In source order: Evaluate once registry; assign in source target order to self._registry. Then Evaluate once locator; assign in source target order to self.locator. Then Evaluate once False; assign in source target order to self.released.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/handles.py:41-42
  // Source signature: __enter__(self) -> _SnapshotLease
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __enter__(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/handles.py:42-42
    End this invocation with self.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/handles.py:44-50
  // Source signature: __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: TracebackType | None) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __exit__(self, exc_type, exc_value, traceback) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/handles.py:50-50
    In source order: Evaluate self.release(); retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/handles.py:52-55
  // Source signature: release(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn release(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/handles.py:53-55
    if (the source predicate not self.released is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/handles.py:54-55
      In source order: Evaluate self._registry._release(self.locator); retain side effects and discard the expression result. Then Evaluate once True; assign in source target order to self.released.
    }
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/handles.py:58-100
interface SnapshotLeaseRegistry {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/handles.py:59-62
  // Source signature: __init__(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/handles.py:60-62
    In source order: For self._counts, assign {}; source annotation dict[str, int]. Then Evaluate once threading.Condition(); assign in source target order to self._condition. Then Evaluate once False; assign in source target order to self._closed.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/handles.py:64-70
  // Source signature: acquire(self, locator: SnapshotLocator) -> AbstractContextManager[_SnapshotLease]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn acquire(self, locator) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/handles.py:65-69
    Enter source context managers left-to-right: self._condition {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/handles.py:66-67
      if (the source predicate self._closed is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/handles.py:67-67
        Raise RuntimeError('snapshot lease registry is closed').
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/handles.py:68-69
      In source order: Evaluate once locator.database_path; assign in source target order to key. Then Evaluate once self._counts.get(key, 0) + 1; assign in source target order to self._counts[key].
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/handles.py:70-70
    End this invocation with _SnapshotLease(self, locator).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/handles.py:72-74
  // Source signature: active_count(self, locator: SnapshotLocator) -> int
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn active_count(self, locator) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/handles.py:73-74
    Enter source context managers left-to-right: self._condition {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/handles.py:74-74
      End this invocation with self._counts.get(locator.database_path, 0).
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/handles.py:76-84
  // Source signature: wait_for_zero(self, timeout_seconds: float) -> bool
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn wait_for_zero(self, timeout_seconds) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/handles.py:77-77
    In source order: Evaluate once time.monotonic() + timeout_seconds; assign in source target order to deadline.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/handles.py:78-84
    Enter source context managers left-to-right: self._condition {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/handles.py:79-83
      while (the source predicate self._counts is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/handles.py:80-80
        In source order: Evaluate once deadline - time.monotonic(); assign in source target order to remaining.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/handles.py:81-82
        if (the source predicate remaining <= 0 is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/handles.py:82-82
          End this invocation with False.
        }
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/handles.py:83-83
        In source order: Evaluate self._condition.wait(remaining); retain side effects and discard the expression result.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/handles.py:84-84
      End this invocation with True.
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/handles.py:86-90
  // Source signature: close(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn close(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/handles.py:87-90
    Enter source context managers left-to-right: self._condition {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/handles.py:88-89
      if (the source predicate self._counts is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/handles.py:89-89
        Raise RuntimeError('cannot close lease registry with active leases').
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/handles.py:90-90
      In source order: Evaluate once True; assign in source target order to self._closed.
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/handles.py:92-100
  // Source signature: _release(self, locator: SnapshotLocator) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _release(self, locator) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/handles.py:93-100
    Enter source context managers left-to-right: self._condition {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/handles.py:94-95
      In source order: Evaluate once locator.database_path; assign in source target order to key. Then Evaluate once self._counts.get(key, 0); assign in source target order to count.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/handles.py:96-99
      if (the source predicate count <= 1 is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/handles.py:97-97
        In source order: Evaluate self._counts.pop(key, None); retain side effects and discard the expression result.
      }
      else {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/handles.py:99-99
        In source order: Evaluate once count - 1; assign in source target order to self._counts[key].
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/handles.py:100-100
      In source order: Evaluate self._condition.notify_all(); retain side effects and discard the expression result.
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    If execution reaches this end, finish with the source implicit None result.
  }
}
```

## Local import links

- `from context_graph_sdk.models import SnapshotLocator` at source line 32: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/models.py.sudo.md`.
