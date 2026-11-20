# vendor/context_graph_sdk/src/context_graph_sdk/query/protocol.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vendor/context_graph_sdk/src/context_graph_sdk/query/protocol.py.evidence.json`. SHA-256: `cd90a554a78c02fd72f138f3e3f6be606511d157b20e03ffac53d187be784c66`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/protocol.py:15-22
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import json; preserve alias and import-time effects. Then Resolve source import from typing import Any, cast; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.errors import QueryProtocolError; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/protocol.py:23-26
In source order: Resolve source import from context_graph_sdk.identity import ProjectId, SnapshotId; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.models import SnapshotLocator, freeze_properties; preserve alias and import-time effects. Then Resolve source import from .contracts import QueryLimits, QueryWorkerRequest, QueryWorkerResult, TruncationReason; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/protocol.py:29-46
// Source signature: encode_request(request: QueryWorkerRequest) -> bytes
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn encode_request(request) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/protocol.py:30-45
  In source order: Evaluate once {'requestId': request.request_id, 'snapshot': {'projectId': request.snapshot.project_id.value, 'snapshotId': request.snapshot.snapshot_id.value, 'databasePath': request.snapshot.database_path}, 'cypher': request.cypher, 'parameters': request.parameters.to_dict(), 'limits': {'timeoutSeconds': request.limits.timeout_seconds, 'memoryBytes': request.limits.memory_bytes, 'rowLimit': request.limits.row_limit, 'byteLimit': request.limits.byte_limit}}; assign in source target order to payload.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/protocol.py:46-46
  End this invocation with json.dumps(payload, separators=(',', ':'), sort_keys=True).encode().
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/protocol.py:49-80
// Source signature: decode_request(frame: bytes) -> QueryWorkerRequest
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn decode_request(frame) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/protocol.py:50-80
  Perform the following protected operations {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/protocol.py:51-51
    In source order: Evaluate once json.loads(frame); assign in source target order to decoded.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/protocol.py:52-53
    if (the source predicate not isinstance(decoded, dict) is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/protocol.py:53-53
      Raise TypeError('request frame must be an object').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/protocol.py:54-54
    In source order: Evaluate once cast(dict[str, Any], decoded); assign in source target order to payload.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/protocol.py:55-56
    if (the source predicate set(payload) != {'requestId', 'snapshot', 'cypher', 'parameters', 'limits'} is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/protocol.py:56-56
      Raise ValueError('request frame contains missing or unknown fields').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/protocol.py:57-58
    In source order: Evaluate once cast(dict[str, Any], payload['snapshot']); assign in source target order to snapshot. Then Evaluate once cast(dict[str, Any], payload['limits']); assign in source target order to limits.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/protocol.py:59-60
    if (the source predicate set(snapshot) != {'projectId', 'snapshotId', 'databasePath'} is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/protocol.py:60-60
      Raise ValueError('snapshot locator contains missing or unknown fields').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/protocol.py:61-62
    if (the source predicate set(limits) != {'timeoutSeconds', 'memoryBytes', 'rowLimit', 'byteLimit'} is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/protocol.py:62-62
      Raise ValueError('query limits contain missing or unknown fields').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/protocol.py:63-78
    End this invocation with QueryWorkerRequest(str(payload['requestId']), SnapshotLocator(ProjectId(str(snapshot['projectId'])), SnapshotId(str(snapshot['snapshotId'])), str(snapshot['databasePath'])), str(payload['cypher']), freeze_properties(cast(dict[str, object], payload['parameters'])), QueryLimits(float(limits['timeoutSeconds']), int(limits['memoryBytes']), int(limits['rowLimit']), int(limits['byteLimit']))).
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/protocol.py:79-80
  On the first matching source exception (KeyError, TypeError, ValueError, json.JSONDecodeError) as exc, in handler order {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/protocol.py:80-80
    Raise QueryProtocolError(source_template_80_33) with explicit source cause exc.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/protocol.py:83-91
// Source signature: encode_result(result: QueryWorkerResult) -> bytes
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn encode_result(result) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/protocol.py:84-90
  In source order: Evaluate once {'requestId': result.request_id, 'rows': [row.to_dict() for row in result.rows], 'serializedBytes': result.serialized_bytes, 'truncated': result.truncated, 'truncationReason': result.truncation_reason.value if result.truncation_reason else None}; assign in source target order to payload.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/protocol.py:91-91
  End this invocation with json.dumps(payload, separators=(',', ':'), sort_keys=True).encode().
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/protocol.py:94-117
// Source signature: decode_result(frame: bytes) -> QueryWorkerResult
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn decode_result(frame) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/protocol.py:95-117
  Perform the following protected operations {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/protocol.py:96-96
    In source order: Evaluate once json.loads(frame); assign in source target order to decoded.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/protocol.py:97-98
    if (the source predicate not isinstance(decoded, dict) is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/protocol.py:98-98
      Raise TypeError('result frame must be an object').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/protocol.py:99-99
    In source order: Evaluate once cast(dict[str, Any], decoded); assign in source target order to payload.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/protocol.py:100-107
    if (the source predicate set(payload) != {'requestId', 'rows', 'serializedBytes', 'truncated', 'truncationReason'} is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/protocol.py:107-107
      Raise ValueError('result frame contains missing or unknown fields').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/protocol.py:108-108
    In source order: Evaluate once payload.get('truncationReason'); assign in source target order to reason.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/protocol.py:109-115
    End this invocation with QueryWorkerResult(str(payload['requestId']), tuple((freeze_properties(cast(dict[str, object], row)) for row in payload['rows'])), int(payload['serializedBytes']), bool(payload['truncated']), TruncationReason(str(reason)) if reason else None).
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/protocol.py:116-117
  On the first matching source exception (KeyError, TypeError, ValueError, json.JSONDecodeError) as exc, in handler order {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/protocol.py:117-117
    Raise QueryProtocolError(source_template_117_33) with explicit source cause exc.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/protocol.py:120-125
// Source signature: encode_error(request_id: str | None, code: str, message: str) -> bytes
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn encode_error(request_id, code, message) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/protocol.py:121-125
  End this invocation with json.dumps({'requestId': request_id, 'error': code, 'message': message}, separators=(',', ':'), sort_keys=True).encode().
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/protocol.py:128-140
// Source signature: decode_error(frame: bytes) -> tuple[str | None, str, str] | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn decode_error(frame) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/protocol.py:129-132
  Perform the following protected operations {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/protocol.py:130-130
    In source order: Evaluate once cast(dict[str, Any], json.loads(frame)); assign in source target order to payload.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/protocol.py:131-132
  On the first matching source exception (TypeError, ValueError, json.JSONDecodeError) as exc, in handler order {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/protocol.py:132-132
    Raise QueryProtocolError(source_template_132_33) with explicit source cause exc.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/protocol.py:133-134
  if (the source predicate 'error' not in payload is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/protocol.py:134-134
    End this invocation with None.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/protocol.py:135-135
  In source order: Evaluate once payload.get('requestId'); assign in source target order to request_id.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/protocol.py:136-140
  End this invocation with (str(request_id) if request_id is not None else None, str(payload['error']), str(payload.get('message', ''))).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from context_graph_sdk.errors import QueryProtocolError` at source line 22: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/errors.py.sudo.md`.
- `from context_graph_sdk.identity import ProjectId, SnapshotId` at source line 23: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/identity.py.sudo.md`.
- `from context_graph_sdk.models import SnapshotLocator, freeze_properties` at source line 24: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/models.py.sudo.md`.
- `from .contracts import QueryLimits, QueryWorkerRequest, QueryWorkerResult, TruncationReason` at source line 26: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/query/contracts.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../../../prompt_representation/vendor/context_graph_sdk/src/context_graph_sdk/query/protocol.py.sudo.md). Exact strings in the evidence asset support this conversion.
