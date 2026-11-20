# vvaharness/backends/harness/deepagents/options/graph_config.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/backends/harness/deepagents/options/graph_config.py.evidence.json`. SHA-256: `dcd51cc89ac69d59945fb0d344c4446f30829aa4bd6371ece873e05da8486f06`.

```sudo
// Source: vvaharness/backends/harness/deepagents/options/graph_config.py:15-22
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import os; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.deepagents.models import GraphInvokeConfig; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.models import OneShotOptions, StreamingOptions; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/deepagents/options/graph_config.py:25-30
// Source signature: _make_config(options: OneShotOptions | StreamingOptions, buffer: int) -> GraphInvokeConfig
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _make_config(options, buffer) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/options/graph_config.py:26-27
  In source order: Retain source documentation literal source_literal_26_4; it is not a model call. Then For config, assign {'configurable': {'thread_id': os.urandom(8).hex()}}; source annotation GraphInvokeConfig.
  // Source: vvaharness/backends/harness/deepagents/options/graph_config.py:28-29
  if (the source predicate options.max_turns is not None is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/graph_config.py:29-29
    In source order: Evaluate once options.max_turns + buffer; assign in source target order to config['recursion_limit'].
  }
  // Source: vvaharness/backends/harness/deepagents/options/graph_config.py:30-30
  End this invocation with config.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.backends.harness.deepagents.models import GraphInvokeConfig` at source line 21: `source_detail/vvaharness/backends/harness/deepagents/models.py.sudo.md`.
- `from vvaharness.backends.harness.models import OneShotOptions, StreamingOptions` at source line 22: `source_detail/vvaharness/backends/harness/models.py.sudo.md`.
