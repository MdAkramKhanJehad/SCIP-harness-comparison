# vendor/context_graph_sdk/src/context_graph_sdk/_process.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vendor/context_graph_sdk/src/context_graph_sdk/_process.py.evidence.json`. SHA-256: `8dd7cfefe5d459d494ff2f885f680e7e885a1968c0f37b9889f22e2db1f1f7ef`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import os; preserve alias and import-time effects. Then Resolve source import import struct; preserve alias and import-time effects. Then Resolve source import import subprocess; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:22-26
In source order: Resolve source import import sys; preserve alias and import-time effects. Then Resolve source import import threading; preserve alias and import-time effects. Then Resolve source import from collections import deque; preserve alias and import-time effects. Then Resolve source import from collections.abc import Callable; preserve alias and import-time effects. Then Resolve source import from contextlib import suppress; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:27-30
In source order: Resolve source import from typing import BinaryIO, Protocol, cast; preserve alias and import-time effects. Then Evaluate once struct.Struct('!I'); assign in source target order to _FRAME_HEADER. Then Evaluate once (1 << _FRAME_HEADER.size * 8) - 1; assign in source target order to _MAX_FRAME_BYTES.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:33-36
interface ByteReader {
  Describe the source Python type, preserving its base/metaclass expression order: Protocol.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:34-34
  // Source signature: recv_bytes(self, maximum: int) -> bytes
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn recv_bytes(self, maximum) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:34-34
    In source order: Evaluate ...; retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:36-36
  // Source signature: close(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn close(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:36-36
    In source order: Evaluate ...; retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:39-42
interface ByteWriter {
  Describe the source Python type, preserving its base/metaclass expression order: Protocol.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:40-40
  // Source signature: send_bytes(self, payload: bytes) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn send_bytes(self, payload) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:40-40
    In source order: Evaluate ...; retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:42-42
  // Source signature: close(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn close(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:42-42
    In source order: Evaluate ...; retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:45-59
interface FrameReader {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:46-46
  In source order: Retain source documentation literal source_literal_46_4; it is not a model call.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:48-49
  // Source signature: __init__(self, stream: BinaryIO) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self, stream) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:49-49
    In source order: Evaluate once stream; assign in source target order to self._stream.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:51-56
  // Source signature: recv_bytes(self, maximum: int) -> bytes
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn recv_bytes(self, maximum) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:52-53
    In source order: Evaluate once _read_exact(self._stream, _FRAME_HEADER.size); assign in source target order to header. Then Evaluate once _FRAME_HEADER.unpack(header)[0]; assign in source target order to size.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:54-55
    if (the source predicate size > maximum is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:55-55
      Raise OSError(source_template_55_26).
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:56-56
    End this invocation with _read_exact(self._stream, size).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:58-59
  // Source signature: close(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn close(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:59-59
    In source order: Evaluate self._stream.close(); retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:62-78
interface FrameWriter {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:63-63
  In source order: Retain source documentation literal source_literal_63_4; it is not a model call.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:65-67
  // Source signature: __init__(self, stream: BinaryIO) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self, stream) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:66-67
    In source order: Evaluate once stream; assign in source target order to self._stream. Then Evaluate once threading.Lock(); assign in source target order to self._lock.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:69-75
  // Source signature: send_bytes(self, payload: bytes) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn send_bytes(self, payload) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:70-71
    if (the source predicate len(payload) > _MAX_FRAME_BYTES is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:71-71
      Raise ValueError('payload exceeds framing limit').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:72-75
    Enter source context managers left-to-right: self._lock {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:73-75
      In source order: Evaluate _write_all(self._stream, _FRAME_HEADER.pack(len(payload))); retain side effects and discard the expression result. Then Evaluate _write_all(self._stream, payload); retain side effects and discard the expression result. Then Evaluate self._stream.flush(); retain side effects and discard the expression result.
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:77-78
  // Source signature: close(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn close(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:78-78
    In source order: Evaluate self._stream.close(); retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:81-158
interface StdioChannel {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:82-82
  In source order: Retain source documentation literal source_literal_82_4; it is not a model call.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:84-103
  // Source signature: __init__(self, request_stream: BinaryIO, response_stream: BinaryIO, maximum_response_bytes: int, on_response: Callable[[StdioChannel], None] | None=None) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self, request_stream, response_stream, maximum_response_bytes, on_response) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:91-95
    In source order: Evaluate once FrameWriter(request_stream); assign in source target order to self._request. Then Evaluate once FrameReader(response_stream); assign in source target order to self._response. Then Evaluate once maximum_response_bytes; assign in source target order to self._maximum_response_bytes. Then Evaluate once on_response; assign in source target order to self._on_response. Then Evaluate once threading.Condition(); assign in source target order to self._condition.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:96-103
    In source order: For self._messages, assign deque(); source annotation deque[bytes | BaseException]. Then Evaluate once False; assign in source target order to self._closed. Then Evaluate once threading.Thread(target=self._read_responses, name='context-graph-worker-reader', daemon=True); assign in source target order to self._reader. Then Evaluate self._reader.start(); retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:105-106
  // Source signature: send_bytes(self, payload: bytes) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn send_bytes(self, payload) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:106-106
    In source order: Evaluate self._request.send_bytes(payload); retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:108-110
  // Source signature: poll(self, timeout: float) -> bool
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn poll(self, timeout) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:109-110
    Enter source context managers left-to-right: self._condition {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:110-110
      End this invocation with self._condition.wait_for(lambda: bool(self._messages), timeout).
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:112-121
  // Source signature: recv_bytes(self, maximum: int) -> bytes
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn recv_bytes(self, maximum) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:113-116
    Enter source context managers left-to-right: self._condition {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:114-115
      if (the source predicate not self._messages is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:115-115
        Raise BlockingIOError('worker response is not ready').
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:116-116
      In source order: Evaluate once self._messages.popleft(); assign in source target order to message.
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:117-118
    if (the source predicate isinstance(message, BaseException) is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:118-118
      Raise message.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:119-120
    if (the source predicate len(message) > maximum is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:120-120
      Raise OSError(source_template_120_26).
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:121-121
    End this invocation with message.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:123-125
  // Source signature: close_request(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn close_request(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:124-125
    Enter source context managers left-to-right: suppress(OSError) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:125-125
      In source order: Evaluate self._request.close(); retain side effects and discard the expression result.
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:127-136
  // Source signature: close(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn close(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:128-131
    Enter source context managers left-to-right: self._condition {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:129-130
      if (the source predicate self._closed is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:130-130
        End this invocation with None.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:131-131
      In source order: Evaluate once True; assign in source target order to self._closed.
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:132-132
    In source order: Evaluate self.close_request(); retain side effects and discard the expression result.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:133-134
    Enter source context managers left-to-right: suppress(OSError) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:134-134
      In source order: Evaluate self._response.close(); retain side effects and discard the expression result.
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:135-136
    if (the source predicate threading.current_thread() is not self._reader is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:136-136
      In source order: Evaluate self._reader.join(2.0); retain side effects and discard the expression result.
    }
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:138-158
  // Source signature: _read_responses(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _read_responses(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:139-158
    while (the source predicate True is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:140-145
      Perform the following protected operations {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:141-143
        In source order: For message, assign self._response.recv_bytes(self._maximum_response_bytes); source annotation bytes | BaseException.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:144-145
      On the first matching source exception BaseException as error, in handler order {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:145-145
        In source order: Evaluate once error; assign in source target order to message.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:146-153
      Enter source context managers left-to-right: self._condition {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:147-148
        if (the source predicate self._closed is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:148-148
          End this invocation with None.
        }
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:149-151
        if (the source predicate self._messages is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:150-151
          In source order: Evaluate once OSError('worker produced more than one pending response'); assign in source target order to message. Then Evaluate self._messages.clear(); retain side effects and discard the expression result.
        }
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:152-153
        In source order: Evaluate self._messages.append(message); retain side effects and discard the expression result. Then Evaluate self._condition.notify_all(); retain side effects and discard the expression result.
      }
      Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:154-156
      if (the source predicate self._on_response is not None is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:155-156
        Enter source context managers left-to-right: suppress(Exception) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:156-156
          In source order: Evaluate self._on_response(self); retain side effects and discard the expression result.
        }
        Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:157-158
      if (the source predicate isinstance(message, BaseException) is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:158-158
        End this invocation with None.
      }
    }
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:161-202
// Source signature: spawn_stdio_worker(module: str, *arguments: str, maximum_response_bytes: int=64 * 1024 * 1024, on_response: Callable[[StdioChannel], None] | None=None) -> tuple[subprocess.Popen[bytes], StdioChannel]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn spawn_stdio_worker(module, maximum_response_bytes, on_response, arguments) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:167-186
  In source order: Retain source documentation literal source_literal_167_4; it is not a model call. Then Evaluate once subprocess.Popen([sys.executable, '-m', module, *arguments], stdin=subprocess.PIPE, stdout=subprocess.PIPE, close_fds=os.name == 'nt', bufsize=0); assign in source target order to process.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:187-189
  if (the source predicate process.stdin is None or process.stdout is None is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:188-188
    In source order: Evaluate _terminate_failed_spawn(process); retain side effects and discard the expression result.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:189-189
    Raise RuntimeError('worker standard streams were not created').
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:190-201
  Perform the following protected operations {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:191-196
    In source order: Evaluate once StdioChannel(cast(BinaryIO, process.stdin), cast(BinaryIO, process.stdout), maximum_response_bytes, on_response); assign in source target order to channel.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:197-201
  On the first matching source exception Exception, in handler order {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:198-200
    In source order: Evaluate process.stdin.close(); retain side effects and discard the expression result. Then Evaluate process.stdout.close(); retain side effects and discard the expression result. Then Evaluate _terminate_failed_spawn(process); retain side effects and discard the expression result.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:201-201
    Raise the currently handled exception.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:202-202
  End this invocation with (process, channel).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:205-214
// Source signature: _read_exact(stream: BinaryIO, size: int) -> bytes
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _read_exact(stream, size) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:206-207
  In source order: For chunks, assign []; source annotation list[bytes]. Then Evaluate once size; assign in source target order to remaining.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:208-213
  while (the source predicate remaining is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:209-209
    In source order: Evaluate once stream.read(remaining); assign in source target order to chunk.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:210-211
    if (the source predicate not chunk is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:211-211
      Raise EOFError.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:212-213
    In source order: Evaluate chunks.append(chunk); retain side effects and discard the expression result. Then Apply source augmented assignment remaining -= len(chunk) with source evaluation/in-place semantics.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:214-214
  End this invocation with b''.join(chunks).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:217-223
// Source signature: _write_all(stream: BinaryIO, payload: bytes) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _write_all(stream, payload) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:218-218
  In source order: Evaluate once memoryview(payload); assign in source target order to view.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:219-223
  while (the source predicate view is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:220-220
    In source order: Evaluate once stream.write(view); assign in source target order to written.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:221-222
    if (the source predicate written is None or written <= 0 is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:222-222
      Raise BrokenPipeError('worker stream closed during write').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:223-223
    In source order: Evaluate once view[written:]; assign in source target order to view.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:226-235
// Source signature: _terminate_failed_spawn(process: subprocess.Popen[bytes]) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _terminate_failed_spawn(process) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:227-228
  if (the source predicate process.poll() is not None is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:228-228
    End this invocation with None.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:229-229
  In source order: Evaluate process.terminate(); retain side effects and discard the expression result.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:230-231
  Enter source context managers left-to-right: suppress(subprocess.TimeoutExpired) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:231-231
    In source order: Evaluate process.wait(5.0); retain side effects and discard the expression result.
  }
  Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:232-235
  if (the source predicate process.poll() is None is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:233-233
    In source order: Evaluate process.kill(); retain side effects and discard the expression result.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:234-235
    Enter source context managers left-to-right: suppress(subprocess.TimeoutExpired) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/_process.py:235-235
      In source order: Evaluate process.wait(2.0); retain side effects and discard the expression result.
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
  }
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

No statically resolved in-checkout import; external calls remain explicit dependency boundaries.
