# vvaharness/util/config.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/util/config.py.evidence.json`. SHA-256: `96dc8ec873079c30d53d4cdd17698f41d6993c0d23a22860430b535993413092`.

```sudo
// Source: vvaharness/util/config.py:15-16
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects.
// Source: vvaharness/util/config.py:19-27
// Source signature: knob(cfg, path: str, default)
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn knob(cfg, path, default) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/config.py:20-22
  In source order: Retain source documentation literal source_literal_20_4; it is not a model call. Then Evaluate once cfg; assign in source target order to node.
  // Source: vvaharness/util/config.py:23-26
  for each part in path.split('.') {
    // Source: vvaharness/util/config.py:24-24
    In source order: Evaluate once getattr(node, part, None); assign in source target order to node.
    // Source: vvaharness/util/config.py:25-26
    if (the source predicate node is None is truthy) {
      // Source: vvaharness/util/config.py:26-26
      End this invocation with default.
    }
  }
  // Source: vvaharness/util/config.py:27-27
  End this invocation with node.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

No statically resolved in-checkout import; external calls remain explicit dependency boundaries.
