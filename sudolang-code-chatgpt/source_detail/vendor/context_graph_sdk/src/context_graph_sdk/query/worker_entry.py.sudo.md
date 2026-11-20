# vendor/context_graph_sdk/src/context_graph_sdk/query/worker_entry.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vendor/context_graph_sdk/src/context_graph_sdk/query/worker_entry.py.evidence.json`. SHA-256: `c294dafc950d77b009cecdc556abe24ede9db15dd6a74486f4c873e4c1a52402`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker_entry.py:15-22
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import os; preserve alias and import-time effects. Then Resolve source import import sys; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk._process import FrameReader, FrameWriter; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker_entry.py:25-37
// Source signature: main() -> int
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn main() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker_entry.py:26-27
  if (the source predicate len(sys.argv) != 2 is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker_entry.py:27-27
    End this invocation with 2.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker_entry.py:28-31
  In source order: Resolve source import from .worker import run_worker_loop; preserve alias and import-time effects. Then Evaluate once FrameReader(sys.stdin.buffer); assign in source target order to requests. Then Evaluate once FrameWriter(sys.stdout.buffer); assign in source target order to responses.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker_entry.py:32-36
  Perform the following protected operations {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker_entry.py:33-33
    In source order: Evaluate run_worker_loop(requests, responses, int(sys.argv[1])); retain side effects and discard the expression result.
  }
  On every exit from this protected/handler/normal-completion region {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker_entry.py:35-36
    In source order: Evaluate requests.close(); retain side effects and discard the expression result. Then Evaluate responses.close(); retain side effects and discard the expression result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker_entry.py:37-37
  End this invocation with 0.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker_entry.py:40-48
// Source signature: _run() -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _run() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker_entry.py:41-45
  Perform the following protected operations {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker_entry.py:42-42
    In source order: Evaluate once main(); assign in source target order to code.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker_entry.py:43-45
  On the first matching source exception BaseException as error, in handler order {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker_entry.py:44-45
    In source order: Evaluate print(source_template_44_14, file=sys.stderr); retain side effects and discard the expression result. Then Evaluate once 1; assign in source target order to code.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker_entry.py:48-48
  In source order: Evaluate os._exit(code); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker_entry.py:51-52
if (the source predicate __name__ == '__main__' is truthy) {
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker_entry.py:52-52
  In source order: Evaluate _run(); retain side effects and discard the expression result.
}
```

## Local import links

- `from context_graph_sdk._process import FrameReader, FrameWriter` at source line 22: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/_process.py.sudo.md`.
- `from .worker import run_worker_loop` at source line 28: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py.sudo.md`.
