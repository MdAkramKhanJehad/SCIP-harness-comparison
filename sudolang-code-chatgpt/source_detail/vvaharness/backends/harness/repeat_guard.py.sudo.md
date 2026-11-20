# vvaharness/backends/harness/repeat_guard.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/backends/harness/repeat_guard.py.evidence.json`. SHA-256: `d6db64ff635533244952ed01a9c06f9c0e9e20760f48b4c3231281e188671251`.

```sudo
// Source: vvaharness/backends/harness/repeat_guard.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import contextlib; preserve alias and import-time effects. Then Resolve source import import json; preserve alias and import-time effects. Then Resolve source import from typing import TYPE_CHECKING, Final; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/repeat_guard.py:23-23
In source order: Resolve source import from vvaharness.backends.harness.models import HarnessToolUse, RepeatedToolCallError; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/repeat_guard.py:25-28
if (the source predicate TYPE_CHECKING is truthy) {
  // Source: vvaharness/backends/harness/repeat_guard.py:26-28
  In source order: Resolve source import from collections.abc import AsyncIterator; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.models import HarnessMessage; preserve alias and import-time effects.
}
// Source: vvaharness/backends/harness/repeat_guard.py:31-31
In source order: For REPEAT_CALL_LIMIT, assign 20; source annotation Final.
// Source: vvaharness/backends/harness/repeat_guard.py:34-37
// Source signature: _signature(msg: HarnessToolUse) -> tuple[str, str, str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _signature(msg) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/repeat_guard.py:35-35
  In source order: Retain source documentation literal source_literal_35_4; it is not a model call.
  // Source: vvaharness/backends/harness/repeat_guard.py:36-37
  End this invocation with (msg.agent or 'orchestrator', msg.name, json.dumps(msg.input, sort_keys=True, default=str)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/repeat_guard.py:40-45
// Source signature: _close(source: AsyncIterator[HarnessMessage]) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _close(source) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  This callable produces a coroutine or async generator; await/suspension positions remain in source expressions.
  // Source: vvaharness/backends/harness/repeat_guard.py:41-42
  In source order: Retain source documentation literal source_literal_41_4; it is not a model call. Then Evaluate once getattr(source, 'aclose', None); assign in source target order to aclose.
  // Source: vvaharness/backends/harness/repeat_guard.py:43-45
  if (the source predicate aclose is not None is truthy) {
    // Source: vvaharness/backends/harness/repeat_guard.py:44-45
    Enter source context managers left-to-right: contextlib.suppress(Exception) {
      // Source: vvaharness/backends/harness/repeat_guard.py:45-45
      In source order: Evaluate await aclose(); retain side effects and discard the expression result.
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/repeat_guard.py:48-68
// Source signature: guard_repeats(source: AsyncIterator[HarnessMessage], *, stage: str, route: str) -> AsyncIterator[HarnessMessage]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn guard_repeats(source, stage, route) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  This callable produces a coroutine or async generator; await/suspension positions remain in source expressions.
  // Source: vvaharness/backends/harness/repeat_guard.py:51-53
  In source order: Retain source documentation literal source_literal_51_4; it is not a model call. Then For last, assign None; source annotation tuple[str, str, str] | None. Then Evaluate once 0; assign in source target order to streak.
  // Source: vvaharness/backends/harness/repeat_guard.py:54-68
  Perform the following protected operations {
    // Source: vvaharness/backends/harness/repeat_guard.py:55-66
    Obtain/advance the following source async iterator by awaiting, without inventing parallel dispatch.
    for each msg in source {
      // Source: vvaharness/backends/harness/repeat_guard.py:56-65
      if (the source predicate isinstance(msg, HarnessToolUse) is truthy) {
        // Source: vvaharness/backends/harness/repeat_guard.py:57-59
        In source order: Evaluate once _signature(msg); assign in source target order to signature. Then Evaluate once streak + 1 if signature == last else 1; assign in source target order to streak. Then Evaluate once signature; assign in source target order to last.
        // Source: vvaharness/backends/harness/repeat_guard.py:60-65
        if (the source predicate streak >= REPEAT_CALL_LIMIT is truthy) {
          // Source: vvaharness/backends/harness/repeat_guard.py:61-65
          Raise RepeatedToolCallError(source_template_62_24, stage=stage, route=route, tool_name=msg.name, repeats=streak).
        }
      }
      // Source: vvaharness/backends/harness/repeat_guard.py:66-66
      In source order: Yield msg; suspend this generator until resumed.
    }
  }
  On every exit from this protected/handler/normal-completion region {
    // Source: vvaharness/backends/harness/repeat_guard.py:68-68
    In source order: Evaluate await _close(source); retain side effects and discard the expression result.
  }
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.backends.harness.models import HarnessToolUse, RepeatedToolCallError` at source line 23: `source_detail/vvaharness/backends/harness/models.py.sudo.md`.
- `from vvaharness.backends.harness.models import HarnessMessage` at source line 28: `source_detail/vvaharness/backends/harness/models.py.sudo.md`.
