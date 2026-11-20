# vvaharness/backends/harness/deepagents/__init__.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/backends/harness/deepagents/__init__.py.evidence.json`. SHA-256: `f37128af9f222edd3200e38db4e98537192ad9ecd53305c061b643298df683e7`.

```sudo
// Source: vvaharness/backends/harness/deepagents/__init__.py:15-17
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from typing import TYPE_CHECKING; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/deepagents/__init__.py:19-20
if (the source predicate TYPE_CHECKING is truthy) {
  // Source: vvaharness/backends/harness/deepagents/__init__.py:20-20
  In source order: Resolve source import from vvaharness.backends.harness.deepagents.client import DeepAgentHarness; preserve alias and import-time effects.
}
// Source: vvaharness/backends/harness/deepagents/__init__.py:22-22
In source order: Evaluate once ['DeepAgentHarness']; assign in source target order to __all__.
// Source: vvaharness/backends/harness/deepagents/__init__.py:25-33
// Source signature: __getattr__(name: str) -> 'type[DeepAgentHarness]'
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn __getattr__(name) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/__init__.py:26-26
  In source order: Retain source documentation literal source_literal_26_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/__init__.py:27-32
  if (the source predicate name == 'DeepAgentHarness' is truthy) {
    // Source: vvaharness/backends/harness/deepagents/__init__.py:28-30
    In source order: Resolve source import from vvaharness.backends.harness.deepagents.client import DeepAgentHarness; preserve alias and import-time effects.
    // Source: vvaharness/backends/harness/deepagents/__init__.py:32-32
    End this invocation with DeepAgentHarness.
  }
  // Source: vvaharness/backends/harness/deepagents/__init__.py:33-33
  Raise AttributeError(source_template_33_25).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.backends.harness.deepagents.client import DeepAgentHarness` at source line 20: `source_detail/vvaharness/backends/harness/deepagents/client.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.client import DeepAgentHarness` at source line 28: `source_detail/vvaharness/backends/harness/deepagents/client.py.sudo.md`.
