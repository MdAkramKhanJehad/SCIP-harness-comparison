# vendor/context_graph_sdk/src/context_graph_sdk/extractors/worker_entry.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vendor/context_graph_sdk/src/context_graph_sdk/extractors/worker_entry.py.evidence.json`. SHA-256: `57c12f19d09969c74f516ff3d692f1ffedcac1a96ebdd576f30898d67f21ebf7`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/worker_entry.py:15-22
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import os; preserve alias and import-time effects. Then Resolve source import import sys; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk._process import FrameReader, FrameWriter; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/worker_entry.py:25-39
// Source signature: main() -> int
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn main() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/worker_entry.py:26-27
  if (the source predicate len(sys.argv) != 4 is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/worker_entry.py:27-27
    End this invocation with 2.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/worker_entry.py:28-38
  In source order: Resolve source import from .worker import extraction_worker; preserve alias and import-time effects. Then Evaluate once FrameReader(sys.stdin.buffer); assign in source target order to requests. Then Evaluate once FrameWriter(sys.stdout.buffer); assign in source target order to responses. Then Evaluate extraction_worker(sys.argv[1], requests, responses, int(sys.argv[2]), int(sys.argv[3])); retain side effects and discard the expression result.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/worker_entry.py:39-39
  End this invocation with 0.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/worker_entry.py:42-51
// Source signature: _run() -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _run() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/worker_entry.py:43-47
  Perform the following protected operations {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/worker_entry.py:44-44
    In source order: Evaluate once main(); assign in source target order to code.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/worker_entry.py:45-47
  On the first matching source exception BaseException as error, in handler order {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/worker_entry.py:46-47
    In source order: Evaluate print(source_template_46_14, file=sys.stderr); retain side effects and discard the expression result. Then Evaluate once 1; assign in source target order to code.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/worker_entry.py:51-51
  In source order: Evaluate os._exit(code); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/worker_entry.py:54-55
if (the source predicate __name__ == '__main__' is truthy) {
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/worker_entry.py:55-55
  In source order: Evaluate _run(); retain side effects and discard the expression result.
}
```

## Local import links

- `from context_graph_sdk._process import FrameReader, FrameWriter` at source line 22: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/_process.py.sudo.md`.
- `from .worker import extraction_worker` at source line 28: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/extractors/worker.py.sudo.md`.
