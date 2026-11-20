# vendor/context_graph_sdk/src/context_graph_sdk/workspace/contracts.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vendor/context_graph_sdk/src/context_graph_sdk/workspace/contracts.py.evidence.json`. SHA-256: `a954bba40f165de031b2155cfd617ec5569a9fe1b32ca184864d1c43e443bf3c`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/contracts.py:15-22
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from contextlib import AbstractContextManager; preserve alias and import-time effects. Then Resolve source import from typing import Protocol, runtime_checkable; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.models import SnapshotLocator; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/contracts.py:26-33
// Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/contracts.py:25-25
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: runtime_checkable.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/contracts.py:26-33
interface SnapshotLease {
  Describe the source Python type, preserving its base/metaclass expression order: Protocol.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/contracts.py:28-28
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/contracts.py:27-27
  Before creating this callable, evaluate and retain decorators top-to-bottom: property.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/contracts.py:28-28
  // Source signature: locator(self) -> SnapshotLocator
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn locator(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/contracts.py:28-28
    In source order: Evaluate ...; retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/contracts.py:31-31
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/contracts.py:30-30
  Before creating this callable, evaluate and retain decorators top-to-bottom: property.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/contracts.py:31-31
  // Source signature: released(self) -> bool
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn released(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/contracts.py:31-31
    In source order: Evaluate ...; retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/contracts.py:33-33
  // Source signature: release(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn release(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/contracts.py:33-33
    In source order: Evaluate ...; retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/contracts.py:37-44
// Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/contracts.py:36-36
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: runtime_checkable.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/contracts.py:37-44
interface SnapshotLeaseManager {
  Describe the source Python type, preserving its base/metaclass expression order: Protocol.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/contracts.py:38-38
  In source order: Retain source documentation literal source_literal_38_4; it is not a model call.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/contracts.py:40-40
  // Source signature: acquire(self, locator: SnapshotLocator) -> AbstractContextManager[SnapshotLease]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn acquire(self, locator) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/contracts.py:40-40
    In source order: Evaluate ...; retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/contracts.py:42-42
  // Source signature: active_count(self, locator: SnapshotLocator) -> int
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn active_count(self, locator) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/contracts.py:42-42
    In source order: Evaluate ...; retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/contracts.py:44-44
  // Source signature: close(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn close(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/contracts.py:44-44
    In source order: Evaluate ...; retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
```

## Local import links

- `from context_graph_sdk.models import SnapshotLocator` at source line 22: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/models.py.sudo.md`.
