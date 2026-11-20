# vvaharness/util/counters.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/util/counters.py.evidence.json`. SHA-256: `97fd662e50243a377fd11a02f0fd052669132435c41de215d568dfc2df120b1b`.

```sudo
// Source: vvaharness/util/counters.py:15-19
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import threading; preserve alias and import-time effects.
// Source: vvaharness/util/counters.py:22-85
interface _Counters {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/util/counters.py:23-23
  In source order: Retain source documentation literal source_literal_23_4; it is not a model call.
  // Source: vvaharness/util/counters.py:25-31
  // Source signature: __init__(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/util/counters.py:26-31
    In source order: Evaluate once threading.Lock(); assign in source target order to self._lock. Then For self._ints, assign {}; source annotation dict[str, int]. Then For self._notes, assign {}; source annotation dict[str, str]. Then For self._retired_ints, assign {}; source annotation dict[str, int]. Then For self._retired_notes, assign {}; source annotation dict[str, str].
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/util/counters.py:34-41
  // Source signature: bump(self, name: str, n: int=1) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn bump(self, name, n) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/util/counters.py:35-41
    Enter source context managers left-to-right: self._lock {
      // Source: vvaharness/util/counters.py:36-40
      if (the source predicate name in self._notes or name in self._retired_notes is truthy) {
        // Source: vvaharness/util/counters.py:37-40
        Raise ValueError(source_template_38_20).
      }
      // Source: vvaharness/util/counters.py:41-41
      In source order: Evaluate once self._ints.get(name, 0) + n; assign in source target order to self._ints[name].
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/util/counters.py:43-51
  // Source signature: note(self, name: str, value: str) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn note(self, name, value) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/util/counters.py:44-44
    In source order: Retain source documentation literal source_literal_44_8; it is not a model call.
    // Source: vvaharness/util/counters.py:45-51
    Enter source context managers left-to-right: self._lock {
      // Source: vvaharness/util/counters.py:46-50
      if (the source predicate name in self._ints or name in self._retired_ints is truthy) {
        // Source: vvaharness/util/counters.py:47-50
        Raise ValueError(source_template_48_20).
      }
      // Source: vvaharness/util/counters.py:51-51
      In source order: Evaluate once value; assign in source target order to self._notes[name].
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/util/counters.py:53-55
  // Source signature: get(self, name: str, default: int=0) -> int
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn get(self, name, default) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/util/counters.py:54-55
    Enter source context managers left-to-right: self._lock {
      // Source: vvaharness/util/counters.py:55-55
      End this invocation with self._ints.get(name, default).
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/util/counters.py:57-59
  // Source signature: snapshot(self) -> dict
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn snapshot(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/util/counters.py:58-59
    Enter source context managers left-to-right: self._lock {
      // Source: vvaharness/util/counters.py:59-59
      End this invocation with {**self._ints, **self._notes}.
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/util/counters.py:61-67
  // Source signature: snapshot_cumulative(self) -> dict
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn snapshot_cumulative(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/util/counters.py:62-62
    In source order: Retain source documentation literal source_literal_62_8; it is not a model call.
    // Source: vvaharness/util/counters.py:63-67
    Enter source context managers left-to-right: self._lock {
      // Source: vvaharness/util/counters.py:64-64
      In source order: Evaluate once dict(self._retired_ints); assign in source target order to merged.
      // Source: vvaharness/util/counters.py:65-66
      for each (k, v) in self._ints.items() {
        // Source: vvaharness/util/counters.py:66-66
        In source order: Evaluate once merged.get(k, 0) + v; assign in source target order to merged[k].
      }
      // Source: vvaharness/util/counters.py:67-67
      End this invocation with {**merged, **self._retired_notes, **self._notes}.
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/util/counters.py:69-76
  // Source signature: reset(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn reset(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/util/counters.py:70-70
    In source order: Retain source documentation literal source_literal_70_8; it is not a model call.
    // Source: vvaharness/util/counters.py:71-76
    Enter source context managers left-to-right: self._lock {
      // Source: vvaharness/util/counters.py:72-73
      for each (k, v) in self._ints.items() {
        // Source: vvaharness/util/counters.py:73-73
        In source order: Evaluate once self._retired_ints.get(k, 0) + v; assign in source target order to self._retired_ints[k].
      }
      // Source: vvaharness/util/counters.py:74-76
      In source order: Evaluate self._retired_notes.update(self._notes); retain side effects and discard the expression result. Then Evaluate self._ints.clear(); retain side effects and discard the expression result. Then Evaluate self._notes.clear(); retain side effects and discard the expression result.
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/util/counters.py:78-85
  // Source signature: reset_all(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn reset_all(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/util/counters.py:79-79
    In source order: Retain source documentation literal source_literal_79_8; it is not a model call.
    // Source: vvaharness/util/counters.py:81-85
    Enter source context managers left-to-right: self._lock {
      // Source: vvaharness/util/counters.py:82-85
      In source order: Evaluate self._ints.clear(); retain side effects and discard the expression result. Then Evaluate self._notes.clear(); retain side effects and discard the expression result. Then Evaluate self._retired_ints.clear(); retain side effects and discard the expression result. Then Evaluate self._retired_notes.clear(); retain side effects and discard the expression result.
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vvaharness/util/counters.py:88-88
In source order: Evaluate once _Counters(); assign in source target order to COUNTERS.
```

## Local import links

No statically resolved in-checkout import; external calls remain explicit dependency boundaries.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../prompt_representation/vvaharness/util/counters.py.sudo.md). Exact strings in the evidence asset support this conversion.
