# vvaharness/backends/harness/registry.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/backends/harness/registry.py.evidence.json`. SHA-256: `c109694e83b07b7644b95c5b88dd9c90df890892e995a2e0c5c4b24cc60cf25b`.

```sudo
// Source: vvaharness/backends/harness/registry.py:15-22
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import sys; preserve alias and import-time effects. Then Resolve source import from typing import TYPE_CHECKING; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.harness import Harness; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/registry.py:24-25
if (the source predicate TYPE_CHECKING is truthy) {
  // Source: vvaharness/backends/harness/registry.py:25-25
  In source order: Resolve source import from collections.abc import Callable; preserve alias and import-time effects.
}
// Source: vvaharness/backends/harness/registry.py:28-33
// Source signature: _make_claude() -> Harness
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _make_claude() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/registry.py:29-31
  In source order: Resolve source import from vvaharness.backends.harness.claude.client import ClaudeHarness; preserve alias and import-time effects.
  // Source: vvaharness/backends/harness/registry.py:33-33
  End this invocation with ClaudeHarness().
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/registry.py:36-49
// Source signature: _make_deepagents() -> Harness
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _make_deepagents() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/registry.py:37-47
  Perform the following protected operations {
    // Source: vvaharness/backends/harness/registry.py:38-40
    In source order: Resolve source import from vvaharness.backends.harness.deepagents.client import DeepAgentHarness; preserve alias and import-time effects.
  }
  // Source: vvaharness/backends/harness/registry.py:41-47
  On the first matching source exception ImportError as exc, in handler order {
    // Source: vvaharness/backends/harness/registry.py:42-46
    In source order: Evaluate once source_template_43_12; assign in source target order to msg.
    // Source: vvaharness/backends/harness/registry.py:47-47
    Raise RuntimeError(msg) with explicit source cause exc.
  }
  // Source: vvaharness/backends/harness/registry.py:49-49
  End this invocation with DeepAgentHarness().
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/registry.py:52-56
In source order: For _BACKENDS, assign {'cli': _make_claude, 'sdk': _make_claude, 'deepagents': _make_deepagents}; source annotation dict[str, Callable[[], Harness]].
// Source: vvaharness/backends/harness/registry.py:59-66
// Source signature: get_harness(via: str | None=None) -> Harness
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn get_harness(via) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/registry.py:60-62
  In source order: Retain source documentation literal source_literal_60_4; it is not a model call. Then Evaluate once via or 'sdk'; assign in source target order to key. Then Evaluate once _BACKENDS.get(key); assign in source target order to factory.
  // Source: vvaharness/backends/harness/registry.py:63-65
  if (the source predicate factory is None is truthy) {
    // Source: vvaharness/backends/harness/registry.py:64-64
    In source order: Evaluate once ', '.join((source_template_64_26 for k in _BACKENDS)); assign in source target order to valid.
    // Source: vvaharness/backends/harness/registry.py:65-65
    Raise ValueError(source_template_65_25).
  }
  // Source: vvaharness/backends/harness/registry.py:66-66
  End this invocation with factory().
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/registry.py:69-69
In source order: Evaluate once ['get_harness']; assign in source target order to __all__.
```

## Local import links

- `from vvaharness.backends.harness.harness import Harness` at source line 22: `source_detail/vvaharness/backends/harness/harness.py.sudo.md`.
- `from vvaharness.backends.harness.claude.client import ClaudeHarness` at source line 29: `source_detail/vvaharness/backends/harness/claude/client.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.client import DeepAgentHarness` at source line 38: `source_detail/vvaharness/backends/harness/deepagents/client.py.sudo.md`.
