# vvaharness/backends/harness/harness.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/backends/harness/harness.py.evidence.json`. SHA-256: `23a0fe54b9bf74ebd91fe996d479c934b2b4ff140f98304057c7459a9fc98e55`.

```sudo
// Source: vvaharness/backends/harness/harness.py:15-27
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from abc import ABC, abstractmethod; preserve alias and import-time effects. Then Resolve source import from typing import TYPE_CHECKING; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.models import HarnessMessage, OneShotOptions, OneShotResult, StreamingOptions; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/harness.py:29-30
if (the source predicate TYPE_CHECKING is truthy) {
  // Source: vvaharness/backends/harness/harness.py:30-30
  In source order: Resolve source import from collections.abc import AsyncIterator; preserve alias and import-time effects.
}
// Source: vvaharness/backends/harness/harness.py:33-46
interface Harness {
  Describe the source Python type, preserving its base/metaclass expression order: ABC.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/harness/harness.py:34-34
  In source order: Retain source documentation literal source_literal_34_4; it is not a model call.
  // Source: vvaharness/backends/harness/harness.py:37-40
  // Source: vvaharness/backends/harness/harness.py:36-36
  Before creating this callable, evaluate and retain decorators top-to-bottom: abstractmethod.
  // Source: vvaharness/backends/harness/harness.py:37-40
  // Source signature: run_oneshot(self, prompt: str, options: OneShotOptions) -> OneShotResult
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn run_oneshot(self, prompt, options) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    This callable produces a coroutine or async generator; await/suspension positions remain in source expressions.
    // Source: vvaharness/backends/harness/harness.py:40-40
    In source order: Retain source documentation literal source_literal_40_8; it is not a model call.
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vvaharness/backends/harness/harness.py:43-46
  // Source: vvaharness/backends/harness/harness.py:42-42
  Before creating this callable, evaluate and retain decorators top-to-bottom: abstractmethod.
  // Source: vvaharness/backends/harness/harness.py:43-46
  // Source signature: run_streaming(self, prompt: str, options: StreamingOptions) -> AsyncIterator[HarnessMessage]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn run_streaming(self, prompt, options) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/harness.py:46-46
    In source order: Retain source documentation literal source_literal_46_8; it is not a model call.
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
}
```

## Local import links

- `from vvaharness.backends.harness.models import HarnessMessage, OneShotOptions, OneShotResult, StreamingOptions` at source line 22: `source_detail/vvaharness/backends/harness/models.py.sudo.md`.
