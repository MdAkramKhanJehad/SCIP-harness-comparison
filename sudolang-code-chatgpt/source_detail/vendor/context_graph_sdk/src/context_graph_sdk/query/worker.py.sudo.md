# vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py.evidence.json`. SHA-256: `13abc6ec1634f22b505cbd012f2c35edfadf98d126921f2553b303987f899ef6`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import json; preserve alias and import-time effects. Then Resolve source import import os; preserve alias and import-time effects. Then Resolve source import import subprocess; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:22-26
In source order: Resolve source import import threading; preserve alias and import-time effects. Then Resolve source import import time; preserve alias and import-time effects. Then Resolve source import from dataclasses import dataclass; preserve alias and import-time effects. Then Resolve source import from functools import cache; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:27-49
In source order: Resolve source import from typing import Any, Protocol, cast, runtime_checkable; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk._process import ByteReader, ByteWriter, StdioChannel, spawn_stdio_worker; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.errors import QueryCancelledError, QueryError, QueryProtocolError, QueryResourceLimitError, QueryTimeoutError, QueryValidationError, QueryWorkerError, SnapshotLifecycleError; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.models import FrozenMap, freeze_properties; preserve alias and import-time effects. Then Resolve source import from .contracts import QueryLimits, QueryWorkerRequest, QueryWorkerResult, TruncationReason, WorkerHealth, WorkerPoolLimits; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:50-58
In source order: Resolve source import from .protocol import decode_error, decode_request, decode_result, encode_error, encode_request, encode_result; preserve alias and import-time effects. Then Resolve source import from .readonly import validate_readonly_cypher; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:62-78
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:61-61
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: runtime_checkable.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:62-78
interface QueryWorkerManager {
  Describe the source Python type, preserving its base/metaclass expression order: Protocol.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:64-64
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:63-63
  Before creating this callable, evaluate and retain decorators top-to-bottom: property.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:64-64
  // Source signature: limits(self) -> WorkerPoolLimits
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn limits(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:64-64
    In source order: Evaluate ...; retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:66-68
  // Source signature: authorize(self, locator_path: str, fingerprint: str, node_count: int=0, edge_count: int=0) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn authorize(self, locator_path, fingerprint, node_count, edge_count) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:68-68
    In source order: Evaluate ...; retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:70-70
  // Source signature: revoke(self, locator_path: str) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn revoke(self, locator_path) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:70-70
    In source order: Evaluate ...; retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:72-72
  // Source signature: execute(self, request: QueryWorkerRequest) -> QueryWorkerResult
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn execute(self, request) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:72-72
    In source order: Evaluate ...; retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:74-74
  // Source signature: cancel(self, request_id: str) -> bool
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn cancel(self, request_id) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:74-74
    In source order: Evaluate ...; retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:76-76
  // Source signature: health(self) -> tuple[WorkerHealth, ...]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn health(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:76-76
    In source order: Evaluate ...; retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:78-78
  // Source signature: close(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn close(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:78-78
    In source order: Evaluate ...; retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:81-162
// Source signature: run_worker_loop(requests: ByteReader, responses: ByteWriter, maximum_request_bytes: int) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn run_worker_loop(requests, responses, maximum_request_bytes) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:84-86
  In source order: Resolve source import from context_graph_sdk.backends.arcadedb import ArcadeDBBackendFactory; preserve alias and import-time effects. Then Evaluate once False; assign in source target order to barrier_proven.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:87-162
  while (the source predicate True is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:88-95
    Perform the following protected operations {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:90-90
      In source order: Evaluate once requests.recv_bytes(maximum_request_bytes + 1); assign in source target order to frame.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:91-92
    On the first matching source exception EOFError, in handler order {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:92-92
      End this invocation with None.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:93-95
    On the first matching source exception OSError as exc, in handler order {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:94-94
      In source order: Evaluate responses.send_bytes(encode_error(None, 'PROTOCOL_ERROR', str(exc))); retain side effects and discard the expression result.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:95-95
      End this invocation with None.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:96-97
    In source order: Evaluate once None; assign in source target order to backend. Then For request_id, assign None; source annotation str | None.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:98-162
    Perform the following protected operations {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:99-101
      In source order: Evaluate once decode_request(frame); assign in source target order to request. Then Evaluate once request.request_id; assign in source target order to request_id. Then Evaluate once ArcadeDBBackendFactory().open_project(request.snapshot); assign in source target order to backend.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:102-118
      if (the source predicate not barrier_proven is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:103-117
        Perform the following protected operations {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:104-110
          In source order: Evaluate tuple(backend.query_readonly("CREATE (:QueryWorkerWriteProbe {id:'forbidden'})", freeze_properties(), 1)); retain side effects and discard the expression result.
        }
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:111-115
        On the first matching source exception Exception as exc, in handler order {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:112-115
          if (the source predicate 'QueryNotIdempotentException' not in str(exc) is truthy) {
            // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:113-115
            Raise QueryWorkerError('engine idempotency barrier returned unexpected error') with explicit source cause exc.
          }
        }
        Only when the protected body falls through normally, without exception, return, break or continue {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:117-117
          Raise QueryWorkerError('engine accepted mutation through readonly query path').
        }
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:118-118
        In source order: Evaluate once True; assign in source target order to barrier_proven.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:120-123
      In source order: For rows, assign []; source annotation list[FrozenMap]. Then Evaluate once 2; assign in source target order to serialized_bytes. Then Evaluate once False; assign in source target order to truncated. Then For reason, assign None; source annotation TruncationReason | None.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:124-139
      for each row in backend.query_readonly(request.cypher, request.parameters, request.limits.row_limit + 1) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:127-129
        In source order: Evaluate once len(json.dumps(row.to_dict(), separators=(',', ':'), sort_keys=True).encode()); assign in source target order to row_bytes.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:130-133
        if (the source predicate len(rows) >= request.limits.row_limit is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:131-132
          In source order: Evaluate once True; assign in source target order to truncated. Then Evaluate once TruncationReason.ROWS; assign in source target order to reason.
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:133-133
          Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
        }
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:134-137
        if (the source predicate serialized_bytes + row_bytes > request.limits.byte_limit is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:135-136
          In source order: Evaluate once True; assign in source target order to truncated. Then Evaluate once TruncationReason.BYTES; assign in source target order to reason.
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:137-137
          Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
        }
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:138-139
        In source order: Evaluate rows.append(row); retain side effects and discard the expression result. Then Apply source augmented assignment serialized_bytes += row_bytes with source evaluation/in-place semantics.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:140-147
      In source order: Evaluate once QueryWorkerResult(request.request_id, tuple(rows), serialized_bytes, truncated, reason); assign in source target order to result. Then Evaluate once encode_result(result); assign in source target order to response.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:148-153
      if (the source predicate len(response) > request.limits.byte_limit is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:149-151
        In source order: Evaluate responses.send_bytes(encode_error(request_id, 'RESOURCE_LIMIT', 'serialized response exceeds bound')); retain side effects and discard the expression result.
      }
      else {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:153-153
        In source order: Evaluate responses.send_bytes(response); retain side effects and discard the expression result.
      }
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:154-155
    On the first matching source exception QueryProtocolError as exc, in handler order {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:155-155
      In source order: Evaluate responses.send_bytes(encode_error(request_id, 'PROTOCOL_ERROR', str(exc))); retain side effects and discard the expression result.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:156-159
    On the first matching source exception Exception as exc, in handler order {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:157-159
      In source order: Evaluate responses.send_bytes(encode_error(request_id, 'QUERY_ERROR', source_template_158_56)); retain side effects and discard the expression result.
    }
    On every exit from this protected/handler/normal-completion region {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:161-162
      if (the source predicate backend is not None is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:162-162
        In source order: Evaluate backend.close(); retain side effects and discard the expression result.
      }
    }
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:166-169
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:165-165
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:166-169
interface _AuthorizedSnapshot {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:167-169
  In source order: For fingerprint, declare without assigning a value; source annotation str. Then For node_count, declare without assigning a value; source annotation int. Then For edge_count, declare without assigning a value; source annotation int.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:172-173
In source order: Evaluate once QueryLimits(30.0, 1024 * 1024 * 1024, 2, 16384); assign in source target order to _RECOVERY_LIMITS. Then Evaluate once 0.1 if Path('/proc/self/status').exists() else 0.5; assign in source target order to _RSS_SAMPLE_INTERVAL_SECONDS.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:176-454
interface SpawnQueryWorkerManager {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:177-177
  In source order: Retain source documentation literal source_literal_177_4; it is not a model call.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:179-190
  // Source signature: __init__(self, limits: WorkerPoolLimits | None=None) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self, limits) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:180-180
    In source order: Evaluate once limits or WorkerPoolLimits(1); assign in source target order to self._limits.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:181-182
    if (the source predicate self._limits.max_workers != 1 is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:182-182
      Raise ValueError('SpawnQueryWorkerManager supports exactly one query worker').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:183-187
    In source order: For self._connection, assign None; source annotation StdioChannel | None. Then For self._process, assign None; source annotation subprocess.Popen[bytes] | None. Then For self._authorized, assign {}; source annotation dict[str, _AuthorizedSnapshot]. Then Evaluate once threading.Lock(); assign in source target order to self._execution_lock. Then Evaluate once threading.Lock(); assign in source target order to self._state_lock.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:188-190
    In source order: For self._current_request_id, assign None; source annotation str | None. Then For self._cancelled_requests, assign set(); source annotation set[str]. Then Evaluate once False; assign in source target order to self._closed.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:193-194
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:192-192
  Before creating this callable, evaluate and retain decorators top-to-bottom: property.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:193-194
  // Source signature: limits(self) -> WorkerPoolLimits
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn limits(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:194-194
    End this invocation with self._limits.
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:196-202
  // Source signature: authorize(self, locator_path: str, fingerprint: str, node_count: int=0, edge_count: int=0) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn authorize(self, locator_path, fingerprint, node_count, edge_count) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:199-202
    Enter source context managers left-to-right: self._state_lock {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:200-202
      In source order: Evaluate once _AuthorizedSnapshot(fingerprint, node_count, edge_count); assign in source target order to self._authorized[locator_path].
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:204-206
  // Source signature: revoke(self, locator_path: str) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn revoke(self, locator_path) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:205-206
    Enter source context managers left-to-right: self._state_lock {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:206-206
      In source order: Evaluate self._authorized.pop(locator_path, None); retain side effects and discard the expression result.
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:208-223
  // Source signature: execute(self, request: QueryWorkerRequest) -> QueryWorkerResult
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn execute(self, request) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:209-209
    In source order: Evaluate validate_readonly_cypher(request.cypher); retain side effects and discard the expression result.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:210-211
    Enter source context managers left-to-right: self._state_lock {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:211-211
      In source order: Evaluate once request.snapshot.database_path in self._authorized; assign in source target order to authorized.
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:212-213
    if (the source predicate not authorized is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:213-213
      Raise QueryValidationError('snapshot locator is not authorized').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:214-223
    Enter source context managers left-to-right: self._execution_lock {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:215-215
      In source order: Evaluate self._ensure_worker(); retain side effects and discard the expression result.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:216-217
      Enter source context managers left-to-right: self._state_lock {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:217-217
        In source order: Evaluate once request.request_id; assign in source target order to self._current_request_id.
      }
      Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:218-223
      Perform the following protected operations {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:219-219
        End this invocation with self._exchange(request).
      }
      On every exit from this protected/handler/normal-completion region {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:221-223
        Enter source context managers left-to-right: self._state_lock {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:222-223
          In source order: Evaluate self._cancelled_requests.discard(request.request_id); retain side effects and discard the expression result. Then Evaluate once None; assign in source target order to self._current_request_id.
        }
        Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
      }
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:225-233
  // Source signature: cancel(self, request_id: str) -> bool
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn cancel(self, request_id) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:226-230
    Enter source context managers left-to-right: self._state_lock {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:227-228
      if (the source predicate self._current_request_id != request_id is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:228-228
        End this invocation with False.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:229-230
      In source order: Evaluate self._cancelled_requests.add(request_id); retain side effects and discard the expression result. Then Evaluate once self._process; assign in source target order to process.
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:231-232
    if (the source predicate process is not None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:232-232
      In source order: Evaluate _terminate_process(process); retain side effects and discard the expression result.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:233-233
    End this invocation with True.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:235-246
  // Source signature: health(self) -> tuple[WorkerHealth, ...]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn health(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:236-236
    In source order: Evaluate once self._process; assign in source target order to process.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:237-238
    if (the source predicate process is None or process.poll() is not None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:238-238
      End this invocation with ().
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:239-246
    End this invocation with (WorkerHealth(process.pid, _rss_bytes(process.pid) or 0, _thread_count(process.pid), _fd_count(process.pid)),).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:248-255
  // Source signature: close(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn close(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:249-249
    In source order: Evaluate once True; assign in source target order to self._closed.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:250-251
    Enter source context managers left-to-right: self._state_lock {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:251-251
      In source order: Evaluate once self._current_request_id; assign in source target order to request_id.
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:252-253
    if (the source predicate request_id is not None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:253-253
      In source order: Evaluate self.cancel(request_id); retain side effects and discard the expression result.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:254-255
    Enter source context managers left-to-right: self._execution_lock {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:255-255
      In source order: Evaluate self._close_worker(); retain side effects and discard the expression result.
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:257-348
  // Source signature: _exchange(self, request: QueryWorkerRequest, *, verify_on_termination: bool=True) -> QueryWorkerResult
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _exchange(self, request, verify_on_termination) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:260-261
    In source order: Evaluate once self._connection; assign in source target order to connection. Then Evaluate once self._process; assign in source target order to process.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:262-263
    if (the source predicate connection is None or process is None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:263-263
      Raise QueryWorkerError('query worker is unavailable').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:264-264
    In source order: Evaluate once encode_request(request); assign in source target order to frame.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:265-266
    if (the source predicate len(frame) > self._limits.max_request_bytes is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:266-266
      Raise QueryProtocolError('serialized request exceeds worker pool bound').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:267-269
    In source order: Evaluate connection.send_bytes(frame); retain side effects and discard the expression result. Then Evaluate once time.monotonic() + request.limits.timeout_seconds; assign in source target order to deadline. Then Evaluate once 0.0; assign in source target order to next_rss_sample.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:270-314
    while (the source predicate not connection.poll(0.01) is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:271-271
      In source order: Evaluate once time.monotonic(); assign in source target order to now.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:272-281
      if (the source predicate process.poll() is not None is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:273-273
        In source order: Evaluate once process.returncode; assign in source target order to exit_code.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:274-276
        Enter source context managers left-to-right: self._state_lock {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:275-276
          In source order: Evaluate once request.request_id in self._cancelled_requests; assign in source target order to cancelled. Then Evaluate self._cancelled_requests.discard(request.request_id); retain side effects and discard the expression result.
        }
        Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:277-278
        In source order: Evaluate self._close_worker(); retain side effects and discard the expression result. Then Evaluate self._verify_after_kill(request); retain side effects and discard the expression result.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:279-280
        if (the source predicate cancelled is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:280-280
          Raise QueryCancelledError('query request was cancelled').
        }
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:281-281
        Raise QueryWorkerError(source_template_281_39).
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:282-283
      Enter source context managers left-to-right: self._state_lock {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:283-283
        In source order: Evaluate once request.request_id in self._cancelled_requests; assign in source target order to cancellation_pending.
      }
      Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:284-292
      if (the source predicate cancellation_pending is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:285-286
        if (the source predicate now < deadline is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:286-286
          Continue the immediately enclosing source loop at its next iteration.
        }
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:287-287
        In source order: Evaluate self._terminate_worker(); retain side effects and discard the expression result.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:288-289
        if (the source predicate verify_on_termination is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:289-289
          In source order: Evaluate self._verify_after_kill(request); retain side effects and discard the expression result.
        }
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:290-291
        Enter source context managers left-to-right: self._state_lock {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:291-291
          In source order: Evaluate self._cancelled_requests.discard(request.request_id); retain side effects and discard the expression result.
        }
        Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:292-292
        Raise QueryCancelledError('query request cancellation exceeded deadline').
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:293-309
      if (the source predicate now >= next_rss_sample is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:294-295
        In source order: Evaluate once _rss_bytes(process.pid); assign in source target order to rss. Then Evaluate once now + _RSS_SAMPLE_INTERVAL_SECONDS; assign in source target order to next_rss_sample.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:296-304
        if (the source predicate rss is None is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:297-298
          Enter source context managers left-to-right: self._state_lock {
            // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:298-298
            In source order: Evaluate once request.request_id in self._cancelled_requests; assign in source target order to cancellation_pending.
          }
          Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:299-300
          if (the source predicate cancellation_pending is truthy) {
            // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:300-300
            Continue the immediately enclosing source loop at its next iteration.
          }
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:301-301
          In source order: Evaluate self._terminate_worker(); retain side effects and discard the expression result.
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:302-303
          if (the source predicate verify_on_termination is truthy) {
            // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:303-303
            In source order: Evaluate self._verify_after_kill(request); retain side effects and discard the expression result.
          }
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:304-304
          Raise QueryResourceLimitError('query worker memory could not be measured').
        }
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:305-309
        if (the source predicate rss > request.limits.memory_bytes is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:306-306
          In source order: Evaluate self._terminate_worker(); retain side effects and discard the expression result.
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:307-308
          if (the source predicate verify_on_termination is truthy) {
            // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:308-308
            In source order: Evaluate self._verify_after_kill(request); retain side effects and discard the expression result.
          }
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:309-309
          Raise QueryResourceLimitError('query worker exceeded memory limit').
        }
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:310-314
      if (the source predicate now >= deadline is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:311-311
        In source order: Evaluate self._terminate_worker(); retain side effects and discard the expression result.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:312-313
        if (the source predicate verify_on_termination is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:313-313
          In source order: Evaluate self._verify_after_kill(request); retain side effects and discard the expression result.
        }
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:314-314
        Raise QueryTimeoutError('query worker exceeded deadline').
      }
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:315-318
    Enter source context managers left-to-right: self._state_lock {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:316-316
      In source order: Evaluate once request.request_id in self._cancelled_requests; assign in source target order to cancelled.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:317-318
      if (the source predicate cancelled is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:318-318
        In source order: Evaluate self._cancelled_requests.discard(request.request_id); retain side effects and discard the expression result.
      }
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:319-322
    if (the source predicate cancelled is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:320-321
      In source order: Evaluate self._close_worker(); retain side effects and discard the expression result. Then Evaluate self._verify_after_kill(request); retain side effects and discard the expression result.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:322-322
      Raise QueryCancelledError('query request was cancelled').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:323-323
    In source order: Evaluate once _rss_bytes(process.pid); assign in source target order to final_rss.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:324-329
    if (the source predicate final_rss is None or final_rss > request.limits.memory_bytes is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:325-325
      In source order: Evaluate self._terminate_worker(); retain side effects and discard the expression result.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:326-327
      if (the source predicate verify_on_termination is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:327-327
        In source order: Evaluate self._verify_after_kill(request); retain side effects and discard the expression result.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:328-328
      In source order: Evaluate once 'could not be measured' if final_rss is None else 'exceeded memory limit'; assign in source target order to detail.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:329-329
      Raise QueryResourceLimitError(source_template_329_42).
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:330-336
    Perform the following protected operations {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:332-332
      In source order: Evaluate once connection.recv_bytes(self._limits.max_response_bytes + 1); assign in source target order to frame.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:333-336
    On the first matching source exception (EOFError, OSError) as exc, in handler order {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:334-335
      In source order: Evaluate self._close_worker(); retain side effects and discard the expression result. Then Evaluate self._verify_after_kill(request); retain side effects and discard the expression result.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:336-336
      Raise QueryWorkerError('query worker closed without a response') with explicit source cause exc.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:337-337
    In source order: Evaluate once decode_error(frame); assign in source target order to error.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:338-344
    if (the source predicate error is not None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:339-339
      In source order: Evaluate once error; assign in source target order to (_, code, message).
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:340-341
      if (the source predicate code == 'PROTOCOL_ERROR' is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:341-341
        Raise QueryProtocolError(message).
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:342-343
      if (the source predicate code == 'RESOURCE_LIMIT' is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:343-343
        Raise QueryResourceLimitError(message).
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:344-344
      Raise QueryError(message).
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:345-345
    In source order: Evaluate once decode_result(frame); assign in source target order to result.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:346-347
    if (the source predicate result.request_id != request.request_id is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:347-347
      Raise QueryProtocolError('worker response request_id mismatch').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:348-348
    End this invocation with result.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:350-408
  // Source signature: _verify_after_kill(self, request: QueryWorkerRequest) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _verify_after_kill(self, request) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:351-352
    if (the source predicate self._closed is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:352-352
      End this invocation with None.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:353-408
    Perform the following protected operations {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:354-355
      Enter source context managers left-to-right: self._state_lock {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:355-355
        In source order: Evaluate once self._authorized[request.snapshot.database_path]; assign in source target order to expected.
      }
      Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:356-358
      In source order: Evaluate once os.path.join(request.snapshot.database_path, '.context-graph-sdk-fingerprint'); assign in source target order to fingerprint_path.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:359-360
      Enter source context managers left-to-right: open(fingerprint_path, encoding='utf-8') bound to fingerprint_file {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:360-360
        In source order: For sidecar, assign json.load(fingerprint_file); source annotation object.
      }
      Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:361-362
      if (the source predicate not isinstance(sidecar, dict) is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:362-362
        Raise SnapshotLifecycleError('snapshot integrity sidecar is invalid').
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:363-366
      In source order: Evaluate once cast(dict[str, object], sidecar); assign in source target order to integrity. Then Evaluate once integrity.get('fingerprint'); assign in source target order to actual_fingerprint. Then Evaluate once integrity.get('nodeCount'); assign in source target order to actual_nodes. Then Evaluate once integrity.get('edgeCount'); assign in source target order to actual_edges.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:367-374
      if (the source predicate actual_fingerprint != expected.fingerprint or actual_nodes != expected.node_count or actual_edges != expected.edge_count is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:372-374
        Raise SnapshotLifecycleError('snapshot integrity sidecar changed after worker termination').
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:375-393
      In source order: Evaluate self._ensure_worker(); retain side effects and discard the expression result. Then Evaluate once QueryWorkerRequest(source_template_377_16, request.snapshot, 'MATCH (n) RETURN count(n) AS nodes', freeze_properties(), _RECOVERY_LIMITS); assign in source target order to verification. Then Evaluate once self._exchange(verification, verify_on_termination=False); assign in source target order to node_result. Then Evaluate once self._exchange(QueryWorkerRequest(source_template_386_20, request.snapshot, 'MATCH ()-[r]->() RETURN count(r) AS edges', freeze_properties(), _RECOVERY_LIMITS), verify_on_termination=False); assign in source target order to edge_result.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:394-403
      if (the source predicate len(node_result.rows) != 1 or _row_count(node_result.rows[0], 'nodes') != expected.node_count or len(edge_result.rows) != 1 or (_row_count(edge_result.rows[0], 'edges') != expected.edge_count) is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:400-400
        In source order: Evaluate self._terminate_worker(); retain side effects and discard the expression result.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:401-403
        Raise SnapshotLifecycleError('snapshot logical counts changed after worker termination').
      }
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:404-405
    On the first matching source exception SnapshotLifecycleError, in handler order {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:405-405
      Raise the currently handled exception.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:406-408
    On the first matching source exception Exception as exc, in handler order {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:407-407
      In source order: Evaluate self._terminate_worker(); retain side effects and discard the expression result.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:408-408
      Raise SnapshotLifecycleError('snapshot recovery verification failed') with explicit source cause exc.
    }
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:410-423
  // Source signature: _ensure_worker(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _ensure_worker(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:411-412
    if (the source predicate self._closed is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:412-412
      Raise QueryWorkerError('query worker manager is closed').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:413-414
    if (the source predicate self._process is not None and self._process.poll() is None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:414-414
      End this invocation with None.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:415-423
    In source order: Evaluate self._close_worker(); retain side effects and discard the expression result. Then Evaluate once spawn_stdio_worker('context_graph_sdk.query.worker_entry', str(self._limits.max_request_bytes), maximum_response_bytes=self._limits.max_response_bytes + 1); assign in source target order to (process, channel). Then Evaluate once channel; assign in source target order to self._connection. Then Evaluate once process; assign in source target order to self._process.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:425-430
  // Source signature: _terminate_worker(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _terminate_worker(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:426-426
    In source order: Evaluate once self._process; assign in source target order to process.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:427-428
    if (the source predicate process is None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:428-428
      End this invocation with None.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:429-430
    In source order: Evaluate _terminate_process(process); retain side effects and discard the expression result. Then Evaluate self._dispose_process(); retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:432-448
  // Source signature: _close_worker(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _close_worker(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:433-433
    In source order: Evaluate once self._process; assign in source target order to process.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:434-435
    if (the source predicate process is None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:435-435
      End this invocation with None.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:436-437
    if (the source predicate self._connection is not None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:437-437
      In source order: Evaluate self._connection.close_request(); retain side effects and discard the expression result.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:438-447
    if (the source predicate process.poll() is None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:439-447
      Perform the following protected operations {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:440-440
        In source order: Evaluate process.wait(2.0); retain side effects and discard the expression result.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:441-447
      On the first matching source exception subprocess.TimeoutExpired, in handler order {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:442-442
        In source order: Evaluate process.terminate(); retain side effects and discard the expression result.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:443-447
        Perform the following protected operations {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:444-444
          In source order: Evaluate process.wait(5.0); retain side effects and discard the expression result.
        }
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:445-447
        On the first matching source exception subprocess.TimeoutExpired, in handler order {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:446-447
          In source order: Evaluate process.kill(); retain side effects and discard the expression result. Then Evaluate process.wait(2.0); retain side effects and discard the expression result.
        }
      }
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:448-448
    In source order: Evaluate self._dispose_process(); retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:450-454
  // Source signature: _dispose_process(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _dispose_process(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:451-452
    if (the source predicate self._connection is not None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:452-452
      In source order: Evaluate self._connection.close(); retain side effects and discard the expression result.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:453-454
    In source order: Evaluate once None; assign in source target order to self._connection. Then Evaluate once None; assign in source target order to self._process.
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:457-468
// Source signature: _terminate_process(process: subprocess.Popen[bytes]) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _terminate_process(process) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:458-459
  if (the source predicate process.poll() is not None is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:459-459
    End this invocation with None.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:460-460
  In source order: Evaluate process.terminate(); retain side effects and discard the expression result.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:461-468
  Perform the following protected operations {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:462-462
    In source order: Evaluate process.wait(5.0); retain side effects and discard the expression result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:463-468
  On the first matching source exception subprocess.TimeoutExpired, in handler order {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:464-464
    In source order: Evaluate process.kill(); retain side effects and discard the expression result.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:465-468
    Perform the following protected operations {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:466-466
      In source order: Evaluate process.wait(2.0); retain side effects and discard the expression result.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:467-468
    On the first matching source exception subprocess.TimeoutExpired as exc, in handler order {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:468-468
      Raise QueryWorkerError('query worker did not exit after kill escalation') with explicit source cause exc.
    }
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:471-475
// Source signature: _row_count(row: FrozenMap, key: str) -> int
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _row_count(row, key) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:472-472
  In source order: Evaluate once row[key]; assign in source target order to value.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:473-474
  if (the source predicate not isinstance(value, int) is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:474-474
    Raise SnapshotLifecycleError(source_template_474_37).
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:475-475
  End this invocation with value.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:478-498
// Source signature: _rss_bytes(pid: int | None) -> int | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _rss_bytes(pid) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:479-480
  if (the source predicate pid is None is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:480-480
    End this invocation with None.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:481-482
  if (the source predicate os.name == 'nt' is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:482-482
    End this invocation with _windows_rss_bytes(pid).
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:483-483
  In source order: Evaluate once Path(source_template_483_18); assign in source target order to status.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:484-498
  Perform the following protected operations {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:485-488
    if (the source predicate status.exists() is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:486-488
      for each line in status.read_text().splitlines() {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:487-488
        if (the source predicate line.startswith('VmRSS:') is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:488-488
          End this invocation with int(line.split()[1]) * 1024.
        }
      }
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:489-495
    In source order: Evaluate once subprocess.run(['ps', '-o', 'rss=', '-p', str(pid)], capture_output=True, text=True, check=False); assign in source target order to result. Then Evaluate once result.stdout.strip(); assign in source target order to value.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:496-496
    End this invocation with int(value) * 1024 if value.isdigit() else None.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:497-498
  On the first matching source exception (OSError, ValueError, subprocess.SubprocessError), in handler order {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:498-498
    End this invocation with None.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:501-514
// Source signature: _thread_count(pid: int) -> int
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _thread_count(pid) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:502-504
  if (the source predicate os.name == 'nt' is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:504-504
    End this invocation with 0.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:505-505
  In source order: Evaluate once Path(source_template_505_17); assign in source target order to tasks.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:506-514
  Perform the following protected operations {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:507-508
    if (the source predicate tasks.is_dir() is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:508-508
      End this invocation with sum((1 for _ in tasks.iterdir())).
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:509-511
    In source order: Evaluate once subprocess.run(['ps', '-M', '-p', str(pid)], capture_output=True, text=True, check=False); assign in source target order to result.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:512-512
    End this invocation with max(0, len(result.stdout.splitlines()) - 1).
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:513-514
  On the first matching source exception (OSError, subprocess.SubprocessError), in handler order {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:514-514
    End this invocation with 0.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:517-530
// Source signature: _fd_count(pid: int) -> int
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _fd_count(pid) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:518-520
  if (the source predicate os.name == 'nt' is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:520-520
    End this invocation with _windows_handle_count(pid).
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:521-521
  In source order: Evaluate once Path(source_template_521_23); assign in source target order to descriptors.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:522-530
  Perform the following protected operations {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:523-524
    if (the source predicate descriptors.is_dir() is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:524-524
      End this invocation with sum((1 for _ in descriptors.iterdir())).
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:525-527
    In source order: Evaluate once subprocess.run(['lsof', '-p', str(pid)], capture_output=True, text=True, check=False); assign in source target order to result.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:528-528
    End this invocation with max(0, len(result.stdout.splitlines()) - 1).
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:529-530
  On the first matching source exception (OSError, subprocess.SubprocessError), in handler order {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:530-530
    End this invocation with 0.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:534-571
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:533-533
Before creating this callable, evaluate and retain decorators top-to-bottom: cache.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:534-571
// Source signature: _windows_process_api() -> tuple[Any, Any, type[Any]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _windows_process_api() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:535-536
  In source order: Resolve source import import ctypes; preserve alias and import-time effects. Then Resolve source import from ctypes import wintypes; preserve alias and import-time effects.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:538-550
  interface ProcessMemoryCounters {
    Describe the source Python type, preserving its base/metaclass expression order: ctypes.Structure.
    Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:539-550
    In source order: Evaluate once [('cb', wintypes.DWORD), ('PageFaultCount', wintypes.DWORD), ('PeakWorkingSetSize', ctypes.c_size_t), ('WorkingSetSize', ctypes.c_size_t), ('QuotaPeakPagedPoolUsage', ctypes.c_size_t), ('QuotaPagedPoolUsage', ctypes.c_size_t), ('QuotaPeakNonPagedPoolUsage', ctypes.c_size_t), ('QuotaNonPagedPoolUsage', ctypes.c_size_t), ('PagefileUsage', ctypes.c_size_t), ('PeakPagefileUsage', ctypes.c_size_t)]; assign in source target order to _fields_.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:552-552
  In source order: Evaluate once vars(ctypes).get('WinDLL'); assign in source target order to win_dll.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:553-554
  if (the source predicate not callable(win_dll) is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:554-554
    Raise OSError('Windows DLL loading is unavailable').
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:555-559
  In source order: For kernel32, assign win_dll('kernel32', use_last_error=True); source annotation Any. Then For psapi, assign win_dll('psapi', use_last_error=True); source annotation Any. Then Evaluate once [wintypes.DWORD, wintypes.BOOL, wintypes.DWORD]; assign in source target order to kernel32.OpenProcess.argtypes. Then Evaluate once wintypes.HANDLE; assign in source target order to kernel32.OpenProcess.restype. Then Evaluate once [wintypes.HANDLE]; assign in source target order to kernel32.CloseHandle.argtypes.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:560-570
  In source order: Evaluate once [wintypes.HANDLE, ctypes.POINTER(wintypes.DWORD)]; assign in source target order to kernel32.GetProcessHandleCount.argtypes. Then Evaluate once wintypes.BOOL; assign in source target order to kernel32.GetProcessHandleCount.restype. Then Evaluate once [wintypes.HANDLE, ctypes.POINTER(ProcessMemoryCounters), wintypes.DWORD]; assign in source target order to psapi.GetProcessMemoryInfo.argtypes. Then Evaluate once wintypes.BOOL; assign in source target order to psapi.GetProcessMemoryInfo.restype.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:571-571
  End this invocation with (kernel32, psapi, ProcessMemoryCounters).
  If execution reaches this end, finish with the source implicit None result.
}
At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:574-591
// Source signature: _windows_rss_bytes(pid: int) -> int | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _windows_rss_bytes(pid) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:575-591
  Perform the following protected operations {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:576-579
    In source order: Resolve source import import ctypes; preserve alias and import-time effects. Then Evaluate once _windows_process_api(); assign in source target order to (kernel32, psapi, counters_type). Then Evaluate once kernel32.OpenProcess(4096, False, pid); assign in source target order to handle.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:580-581
    if (the source predicate not handle is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:581-581
      End this invocation with None.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:582-589
    Perform the following protected operations {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:583-584
      In source order: Evaluate once counters_type(); assign in source target order to counters. Then Evaluate once ctypes.sizeof(counters); assign in source target order to counters.cb.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:585-586
      if (the source predicate not psapi.GetProcessMemoryInfo(handle, ctypes.byref(counters), counters.cb) is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:586-586
        End this invocation with None.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:587-587
      End this invocation with int(counters.WorkingSetSize).
    }
    On every exit from this protected/handler/normal-completion region {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:589-589
      In source order: Evaluate kernel32.CloseHandle(handle); retain side effects and discard the expression result.
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:590-591
  On the first matching source exception (AttributeError, OSError, ValueError), in handler order {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:591-591
    End this invocation with None.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:594-611
// Source signature: _windows_handle_count(pid: int) -> int
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _windows_handle_count(pid) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:595-611
  Perform the following protected operations {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:596-600
    In source order: Resolve source import import ctypes; preserve alias and import-time effects. Then Resolve source import from ctypes import wintypes; preserve alias and import-time effects. Then Evaluate once _windows_process_api(); assign in source target order to (kernel32, _, _). Then Evaluate once kernel32.OpenProcess(4096, False, pid); assign in source target order to handle.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:601-602
    if (the source predicate not handle is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:602-602
      End this invocation with 0.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:603-609
    Perform the following protected operations {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:604-604
      In source order: Evaluate once wintypes.DWORD(); assign in source target order to count.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:605-606
      if (the source predicate not kernel32.GetProcessHandleCount(handle, ctypes.byref(count)) is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:606-606
        End this invocation with 0.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:607-607
      End this invocation with int(count.value).
    }
    On every exit from this protected/handler/normal-completion region {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:609-609
      In source order: Evaluate kernel32.CloseHandle(handle); retain side effects and discard the expression result.
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:610-611
  On the first matching source exception (AttributeError, OSError, ValueError), in handler order {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/worker.py:611-611
    End this invocation with 0.
  }
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from context_graph_sdk._process import ByteReader, ByteWriter, StdioChannel, spawn_stdio_worker` at source line 29: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/_process.py.sudo.md`.
- `from context_graph_sdk.errors import QueryCancelledError, QueryError, QueryProtocolError, QueryResourceLimitError, QueryTimeoutError, QueryValidationError, QueryWorkerError, SnapshotLifecycleError` at source line 30: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/errors.py.sudo.md`.
- `from context_graph_sdk.models import FrozenMap, freeze_properties` at source line 40: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/models.py.sudo.md`.
- `from .contracts import QueryLimits, QueryWorkerRequest, QueryWorkerResult, TruncationReason, WorkerHealth, WorkerPoolLimits` at source line 42: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/query/contracts.py.sudo.md`.
- `from .protocol import decode_error, decode_request, decode_result, encode_error, encode_request, encode_result` at source line 50: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/query/protocol.py.sudo.md`.
- `from .readonly import validate_readonly_cypher` at source line 58: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/query/readonly.py.sudo.md`.
- `from context_graph_sdk.backends.arcadedb import ArcadeDBBackendFactory` at source line 84: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py.sudo.md`.
