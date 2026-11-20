# vendor/context_graph_sdk/src/context_graph_sdk/query/contracts.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vendor/context_graph_sdk/src/context_graph_sdk/query/contracts.py.evidence.json`. SHA-256: `cb54cb9128e1dbb4c3a5d6acba6e5f40ab29d31bce3831ec1a82c2965ba51669`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/contracts.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import json; preserve alias and import-time effects. Then Resolve source import from dataclasses import dataclass; preserve alias and import-time effects. Then Resolve source import from enum import StrEnum; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/contracts.py:23-28
In source order: Resolve source import from context_graph_sdk.errors import ModelValidationError; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.models import FrozenMap, SnapshotLocator; preserve alias and import-time effects. Then Evaluate once 100000; assign in source target order to MAX_QUERY_ROWS. Then Evaluate once 16 * 1024 * 1024; assign in source target order to MAX_QUERY_BYTES. Then Evaluate once 256 * 1024; assign in source target order to MAX_REQUEST_BYTES.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/contracts.py:32-46
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/contracts.py:31-31
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/contracts.py:32-46
interface QueryLimits {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/contracts.py:33-36
  In source order: For timeout_seconds, declare without assigning a value; source annotation float. Then For memory_bytes, declare without assigning a value; source annotation int. Then For row_limit, declare without assigning a value; source annotation int. Then For byte_limit, declare without assigning a value; source annotation int.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/contracts.py:38-46
  // Source signature: __post_init__(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __post_init__(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/contracts.py:39-40
    if (the source predicate not 0 < self.timeout_seconds <= 3600 is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/contracts.py:40-40
      Raise ModelValidationError('timeout_seconds must be in (0, 3600]').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/contracts.py:41-42
    if (the source predicate self.memory_bytes <= 0 is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/contracts.py:42-42
      Raise ModelValidationError('memory_bytes must be positive').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/contracts.py:43-44
    if (the source predicate not 1 <= self.row_limit <= MAX_QUERY_ROWS is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/contracts.py:44-44
      Raise ModelValidationError(source_template_44_39).
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/contracts.py:45-46
    if (the source predicate not 1 <= self.byte_limit <= MAX_QUERY_BYTES is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/contracts.py:46-46
      Raise ModelValidationError(source_template_46_39).
    }
    If execution reaches this end, finish with the source implicit None result.
  }
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/contracts.py:50-85
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/contracts.py:49-49
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/contracts.py:50-85
interface QueryWorkerRequest {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/contracts.py:51-55
  In source order: For request_id, declare without assigning a value; source annotation str. Then For snapshot, declare without assigning a value; source annotation SnapshotLocator. Then For cypher, declare without assigning a value; source annotation str. Then For parameters, declare without assigning a value; source annotation FrozenMap. Then For limits, declare without assigning a value; source annotation QueryLimits.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/contracts.py:57-63
  // Source signature: __post_init__(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __post_init__(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/contracts.py:58-59
    if (the source predicate not self.request_id or len(self.request_id) > 128 is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/contracts.py:59-59
      Raise ModelValidationError('request_id must contain 1..128 characters').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/contracts.py:60-61
    if (the source predicate not self.cypher is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/contracts.py:61-61
      Raise ModelValidationError('cypher is required').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/contracts.py:62-63
    if (the source predicate self.encoded_size > MAX_REQUEST_BYTES is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/contracts.py:63-63
      Raise ModelValidationError('serialized query-worker request exceeds request bound').
    }
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/contracts.py:66-85
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/contracts.py:65-65
  Before creating this callable, evaluate and retain decorators top-to-bottom: property.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/contracts.py:66-85
  // Source signature: encoded_size(self) -> int
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn encoded_size(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/contracts.py:67-82
    In source order: Evaluate once {'requestId': self.request_id, 'snapshot': {'projectId': self.snapshot.project_id.value, 'snapshotId': self.snapshot.snapshot_id.value, 'databasePath': self.snapshot.database_path}, 'cypher': self.cypher, 'parameters': self.parameters.to_dict(), 'limits': {'timeoutSeconds': self.limits.timeout_seconds, 'memoryBytes': self.limits.memory_bytes, 'rowLimit': self.limits.row_limit, 'byteLimit': self.limits.byte_limit}}; assign in source target order to payload.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/contracts.py:83-85
    End this invocation with len(json.dumps(payload, ensure_ascii=True, separators=(',', ':'), sort_keys=True).encode()).
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/contracts.py:89-98
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/contracts.py:88-88
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/contracts.py:89-98
interface WorkerPoolLimits {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/contracts.py:90-92
  In source order: For max_workers, declare without assigning a value; source annotation int. Then For max_request_bytes, assign MAX_REQUEST_BYTES; source annotation int. Then For max_response_bytes, assign MAX_QUERY_BYTES; source annotation int.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/contracts.py:94-98
  // Source signature: __post_init__(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __post_init__(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/contracts.py:95-96
    if (the source predicate self.max_workers <= 0 is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/contracts.py:96-96
      Raise ModelValidationError('max_workers must be positive').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/contracts.py:97-98
    if (the source predicate self.max_request_bytes <= 0 or self.max_response_bytes <= 0 is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/contracts.py:98-98
      Raise ModelValidationError('worker IPC byte bounds must be positive').
    }
    If execution reaches this end, finish with the source implicit None result.
  }
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/contracts.py:101-103
interface TruncationReason {
  Describe the source Python type, preserving its base/metaclass expression order: StrEnum.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/contracts.py:102-103
  In source order: Evaluate once 'rows'; assign in source target order to ROWS. Then Evaluate once 'bytes'; assign in source target order to BYTES.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/contracts.py:107-120
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/contracts.py:106-106
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/contracts.py:107-120
interface QueryWorkerResult {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/contracts.py:108-112
  In source order: For request_id, declare without assigning a value; source annotation str. Then For rows, declare without assigning a value; source annotation tuple[FrozenMap, ...]. Then For serialized_bytes, declare without assigning a value; source annotation int. Then For truncated, assign False; source annotation bool. Then For truncation_reason, assign None; source annotation TruncationReason | None.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/contracts.py:114-120
  // Source signature: __post_init__(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __post_init__(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/contracts.py:115-116
    if (the source predicate not self.request_id is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/contracts.py:116-116
      Raise ModelValidationError('request_id is required').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/contracts.py:117-118
    if (the source predicate self.serialized_bytes < 0 is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/contracts.py:118-118
      Raise ModelValidationError('serialized_bytes cannot be negative').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/contracts.py:119-120
    if (the source predicate self.truncated != (self.truncation_reason is not None) is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/contracts.py:120-120
      Raise ModelValidationError('truncation reason must match truncated state').
    }
    If execution reaches this end, finish with the source implicit None result.
  }
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/contracts.py:124-134
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/contracts.py:123-123
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/contracts.py:124-134
interface WorkerHealth {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/contracts.py:125-128
  In source order: For process_id, declare without assigning a value; source annotation int. Then For rss_bytes, declare without assigning a value; source annotation int. Then For thread_count, declare without assigning a value; source annotation int. Then For file_descriptor_count, declare without assigning a value; source annotation int.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/contracts.py:130-134
  // Source signature: __post_init__(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __post_init__(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/contracts.py:131-132
    if (the source predicate self.process_id <= 0 is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/contracts.py:132-132
      Raise ModelValidationError('worker process_id must be positive').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/contracts.py:133-134
    if (the source predicate min(self.rss_bytes, self.thread_count, self.file_descriptor_count) < 0 is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/contracts.py:134-134
      Raise ModelValidationError('worker health values cannot be negative').
    }
    If execution reaches this end, finish with the source implicit None result.
  }
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
```

## Local import links

- `from context_graph_sdk.errors import ModelValidationError` at source line 23: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/errors.py.sudo.md`.
- `from context_graph_sdk.models import FrozenMap, SnapshotLocator` at source line 24: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/models.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../../../prompt_representation/vendor/context_graph_sdk/src/context_graph_sdk/query/contracts.py.sudo.md). Exact strings in the evidence asset support this conversion.
