# vvaharness/backends/harness/transcript.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/backends/harness/transcript.py.evidence.json`. SHA-256: `cc7ce5b750d0acb28f11286dc38fe657a87978ede9a157e98ed737db03a618ef`.

```sudo
// Source: vvaharness/backends/harness/transcript.py:15-23
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import json; preserve alias and import-time effects. Then Resolve source import import os; preserve alias and import-time effects. Then Resolve source import import re; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/transcript.py:24-29
In source order: Resolve source import import threading; preserve alias and import-time effects. Then Resolve source import import time; preserve alias and import-time effects. Then Resolve source import from dataclasses import asdict, is_dataclass; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Evaluate once 'VVAHARNESS_TRANSCRIPT_DIR'; assign in source target order to _ENV_DIR.
// Source: vvaharness/backends/harness/transcript.py:30-32
In source order: Evaluate once re.compile('[^A-Za-z0-9._-]+'); assign in source target order to _UNSAFE. Then Evaluate once 0; assign in source target order to _SEQ. Then Evaluate once threading.Lock(); assign in source target order to _SEQ_LOCK.
// Source: vvaharness/backends/harness/transcript.py:35-38
// Source signature: transcript_dir() -> Path | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn transcript_dir() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/transcript.py:36-37
  In source order: Retain source documentation literal source_literal_36_4; it is not a model call. Then Evaluate once os.environ.get(_ENV_DIR, '').strip(); assign in source target order to raw.
  // Source: vvaharness/backends/harness/transcript.py:38-38
  End this invocation with Path(raw).expanduser() if raw else None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/transcript.py:41-46
// Source signature: _next_seq() -> int
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _next_seq() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/transcript.py:42-43
  In source order: Retain source documentation literal source_literal_42_4; it is not a model call. Then Bind names in module scope: _SEQ.
  // Source: vvaharness/backends/harness/transcript.py:44-46
  Enter source context managers left-to-right: _SEQ_LOCK {
    // Source: vvaharness/backends/harness/transcript.py:45-45
    In source order: Apply source augmented assignment _SEQ += 1 with source evaluation/in-place semantics.
    // Source: vvaharness/backends/harness/transcript.py:46-46
    End this invocation with _SEQ.
  }
  Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/transcript.py:49-52
// Source signature: _slug(text: str, *, fallback: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _slug(text, fallback) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/transcript.py:50-51
  In source order: Retain source documentation literal source_literal_50_4; it is not a model call. Then Evaluate once _UNSAFE.sub('-', (text or '').strip()).strip('-'); assign in source target order to cleaned.
  // Source: vvaharness/backends/harness/transcript.py:52-52
  End this invocation with cleaned[:60] or fallback.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/transcript.py:55-59
// Source signature: _jsonable(message: object) -> dict[str, object]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _jsonable(message) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/transcript.py:56-56
  In source order: Retain source documentation literal source_literal_56_4; it is not a model call.
  // Source: vvaharness/backends/harness/transcript.py:57-58
  if (the source predicate is_dataclass(message) and (not isinstance(message, type)) is truthy) {
    // Source: vvaharness/backends/harness/transcript.py:58-58
    End this invocation with asdict(message).
  }
  // Source: vvaharness/backends/harness/transcript.py:59-59
  End this invocation with {'kind': type(message).__name__, 'repr': repr(message)[:4000]}.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/transcript.py:62-96
interface Transcript {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/harness/transcript.py:63-63
  In source order: Retain source documentation literal source_literal_63_4; it is not a model call.
  // Source: vvaharness/backends/harness/transcript.py:65-71
  // Source signature: __init__(self, path: Path, *, meta: dict[str, object]) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self, path, meta) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/transcript.py:66-70
    In source order: Retain source documentation literal source_literal_66_8; it is not a model call. Then Evaluate once path; assign in source target order to self.path. Then Evaluate once threading.Lock(); assign in source target order to self._lock. Then Evaluate once time.monotonic(); assign in source target order to self._start. Then Evaluate once 0; assign in source target order to self._n.
    // Source: vvaharness/backends/harness/transcript.py:71-71
    In source order: Evaluate self._write({'kind': 'transcript_open', **meta}); retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/transcript.py:73-79
  // Source signature: _write(self, row: dict[str, object]) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _write(self, row) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/transcript.py:74-74
    In source order: Retain source documentation literal source_literal_74_8; it is not a model call.
    // Source: vvaharness/backends/harness/transcript.py:75-79
    Perform the following protected operations {
      // Source: vvaharness/backends/harness/transcript.py:76-77
      Enter source context managers left-to-right: self._lock; self.path.open('a', encoding='utf-8') bound to fh {
        // Source: vvaharness/backends/harness/transcript.py:77-77
        In source order: Evaluate fh.write(json.dumps(row, default=str) + source_literal_77_56); retain side effects and discard the expression result.
      }
      Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    }
    // Source: vvaharness/backends/harness/transcript.py:78-79
    On the first matching source exception (OSError, TypeError, ValueError), in handler order {
      // Source: vvaharness/backends/harness/transcript.py:79-79
      End this invocation with None.
    }
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/transcript.py:81-88
  // Source signature: add(self, message: object) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn add(self, message) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/transcript.py:82-88
    In source order: Retain source documentation literal source_literal_82_8; it is not a model call. Then Apply source augmented assignment self._n += 1 with source evaluation/in-place semantics. Then Evaluate self._write({'seq': self._n, 't': round(time.monotonic() - self._start, 3), **_jsonable(message)}); retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/transcript.py:90-96
  // Source signature: close(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn close(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/transcript.py:91-96
    In source order: Retain source documentation literal source_literal_91_8; it is not a model call. Then Evaluate self._write({'kind': 'transcript_close', 'messages': self._n, 'elapsed_s': round(time.monotonic() - self._start, 3)}); retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vvaharness/backends/harness/transcript.py:99-110
// Source signature: open_transcript(*, tag: str | None, model: str, graph_name: str='') -> Transcript | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn open_transcript(tag, model, graph_name) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/transcript.py:100-101
  In source order: Retain source documentation literal source_literal_100_4; it is not a model call. Then Evaluate once transcript_dir(); assign in source target order to root.
  // Source: vvaharness/backends/harness/transcript.py:102-103
  if (the source predicate root is None is truthy) {
    // Source: vvaharness/backends/harness/transcript.py:103-103
    End this invocation with None.
  }
  // Source: vvaharness/backends/harness/transcript.py:104-107
  Perform the following protected operations {
    // Source: vvaharness/backends/harness/transcript.py:105-105
    In source order: Evaluate root.mkdir(parents=True, exist_ok=True); retain side effects and discard the expression result.
  }
  // Source: vvaharness/backends/harness/transcript.py:106-107
  On the first matching source exception OSError, in handler order {
    // Source: vvaharness/backends/harness/transcript.py:107-107
    End this invocation with None.
  }
  // Source: vvaharness/backends/harness/transcript.py:108-108
  In source order: Evaluate once source_template_108_11; assign in source target order to name.
  // Source: vvaharness/backends/harness/transcript.py:109-110
  End this invocation with Transcript(root / name, meta={'tag': tag, 'model': model, 'graph_name': graph_name}).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/transcript.py:113-113
In source order: Evaluate once ['Transcript', 'open_transcript', 'transcript_dir']; assign in source target order to __all__.
```

## Local import links

No statically resolved in-checkout import; external calls remain explicit dependency boundaries.
