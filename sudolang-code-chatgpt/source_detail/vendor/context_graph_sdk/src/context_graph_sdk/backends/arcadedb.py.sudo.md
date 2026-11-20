# vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py.evidence.json`. SHA-256: `dc7674afdaa504b309fb5d89311093a06165f1b64edf2822acaf68293aae841e`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:15-25
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import hashlib; preserve alias and import-time effects. Then Resolve source import import importlib; preserve alias and import-time effects. Then Resolve source import import json; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:26-30
In source order: Resolve source import import os; preserve alias and import-time effects. Then Resolve source import import re; preserve alias and import-time effects. Then Resolve source import import shutil; preserve alias and import-time effects. Then Resolve source import import tempfile; preserve alias and import-time effects. Then Resolve source import import threading; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:31-35
In source order: Resolve source import from collections.abc import Iterator; preserve alias and import-time effects. Then Resolve source import from contextlib import AbstractContextManager, suppress; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from types import TracebackType; preserve alias and import-time effects. Then Resolve source import from typing import Any, cast; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:37-63
In source order: Resolve source import from context_graph_sdk.backends.base import CatalogBackend, CatalogWriteTransaction, GraphBackend, GraphWriteTransaction; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.errors import ModelValidationError; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.identity import ProjectId, SnapshotId; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.models import AnalysisVersion, CatalogPublication, CorrelationEdge, CorrelationEndpointRole, CorrelationType, FrozenMap, GraphEdge, GraphNode, NodeRef, ProjectMetadata, ProjectSnapshot, ProviderManifest, ResolvedCorrelation, SnapshotLocator, freeze_properties; preserve alias and import-time effects. Then Evaluate once re.compile('^[A-Za-z_][A-Za-z0-9_]*$'); assign in source target order to _IDENTIFIER.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:64-69
In source order: Evaluate once 10000; assign in source target order to _MAX_WRITE_BATCH. Then Evaluate once 5000; assign in source target order to _MAX_CATALOG_CORRELATIONS. Then Evaluate once '_cgml_'; assign in source target order to _COMBINATION_TYPE_PREFIX. Then Evaluate once threading.Lock(); assign in source target order to _ARCADE_START_LOCK. Then Evaluate once False; assign in source target order to _arcade_logging_configured.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:70-70
In source order: For _arcade_log_filters, assign []; source annotation list[Any].
// Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:73-74
// Source signature: _arcade() -> Any
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _arcade() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:74-74
  End this invocation with importlib.import_module('arcadedb_embedded').
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:77-105
// Source signature: _configure_java_logging() -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _configure_java_logging() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:78-78
  In source order: Bind names in module scope: _arcade_logging_configured.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:79-80
  if (the source predicate _arcade_logging_configured is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:80-80
    End this invocation with None.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:81-81
  In source order: Evaluate once importlib.import_module('jpype'); assign in source target order to jpype.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:82-83
  if (the source predicate not jpype.isJVMStarted() is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:83-83
    End this invocation with None.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:84-87
  In source order: Evaluate once jpype.JClass('java.util.logging.Level').WARNING; assign in source target order to level. Then Evaluate once jpype.JClass('java.util.logging.Logger'); assign in source target order to logger_class. Then Evaluate once logger_class.getLogger(''); assign in source target order to root. Then Evaluate root.setLevel(level); retain side effects and discard the expression result.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:88-99
  for each handler in root.getHandlers() {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:89-90
    In source order: Evaluate handler.setLevel(level); retain side effects and discard the expression result. Then Evaluate once handler.getFilter(); assign in source target order to existing_filter.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:92-95
    // Source signature: is_loggable(record: Any, existing: Any=existing_filter) -> bool
    Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
    fn is_loggable(record, existing) {
      Bind arguments/defaults/annotations exactly as the source signature specifies.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:93-94
      if (the source predicate 'GraalVM Polyglot Engine: no languages found' in str(record.getMessage()) is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:94-94
        End this invocation with False.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:95-95
      End this invocation with existing is None or bool(existing.isLoggable(record)).
      If execution reaches this end, finish with the source implicit None result.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:97-99
    In source order: Evaluate once jpype.JProxy('java.util.logging.Filter', dict(isLoggable=is_loggable)); assign in source target order to filter_proxy. Then Evaluate handler.setFilter(filter_proxy); retain side effects and discard the expression result. Then Evaluate _arcade_log_filters.append(filter_proxy); retain side effects and discard the expression result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:102-105
  In source order: Evaluate logger_class.getLogger('com.arcadedb.query.polyglot.GraalPolyglotEngine').setLevel(jpype.JClass('java.util.logging.Level').SEVERE); retain side effects and discard the expression result. Then Evaluate once True; assign in source target order to _arcade_logging_configured.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:108-155
// Source signature: _database_call(operation: str, path: str) -> Any
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _database_call(operation, path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:109-111
  In source order: Retain source documentation literal source_literal_109_4; it is not a model call. Then Evaluate once _arcade(); assign in source target order to arcade. Then Evaluate once importlib.import_module('jpype'); assign in source target order to jpype.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:112-155
  Enter source context managers left-to-right: _ARCADE_START_LOCK {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:113-115
    if (the source predicate jpype.isJVMStarted() is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:114-114
      In source order: Evaluate _configure_java_logging(); retain side effects and discard the expression result.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:115-115
      End this invocation with getattr(arcade, operation)(path).
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:117-118
    In source order: For failure, assign None; source annotation BaseException | None. Then For result, assign None; source annotation Any.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:119-142
    Enter source context managers left-to-right: tempfile.TemporaryFile() bound to captured {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:120-120
      In source order: Evaluate once os.dup(2); assign in source target order to saved_stderr.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:121-140
      Perform the following protected operations {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:122-122
        In source order: Evaluate os.dup2(captured.fileno(), 2); retain side effects and discard the expression result.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:123-137
        Perform the following protected operations {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:124-128
          In source order: Evaluate once getattr(arcade, operation)(path); assign in source target order to result. Then Evaluate once result.query('opencypher', 'RETURN 1 AS value', {}); assign in source target order to warmup.
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:129-132
          Perform the following protected operations {
            // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:130-130
            In source order: Evaluate tuple(warmup); retain side effects and discard the expression result.
          }
          On every exit from this protected/handler/normal-completion region {
            // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:132-132
            In source order: Evaluate warmup.close(); retain side effects and discard the expression result.
          }
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:133-133
          In source order: Evaluate _configure_java_logging(); retain side effects and discard the expression result.
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:134-135
          Enter source context managers left-to-right: suppress(Exception) {
            // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:135-135
            In source order: Evaluate jpype.JClass('java.lang.System').err.flush(); retain side effects and discard the expression result.
          }
          Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
        }
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:136-137
        On the first matching source exception BaseException as error, in handler order {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:137-137
          In source order: Evaluate once error; assign in source target order to failure.
        }
      }
      On every exit from this protected/handler/normal-completion region {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:139-140
        In source order: Evaluate os.dup2(saved_stderr, 2); retain side effects and discard the expression result. Then Evaluate os.close(saved_stderr); retain side effects and discard the expression result.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:141-142
      In source order: Evaluate captured.seek(0); retain side effects and discard the expression result. Then Evaluate once captured.read().decode('utf-8', errors='replace').strip(); assign in source target order to diagnostics.
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:143-146
    if (the source predicate failure is not None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:144-145
      if (the source predicate diagnostics is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:145-145
        In source order: Evaluate failure.add_note(source_template_145_33); retain side effects and discard the expression result.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:146-146
      Raise failure.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:147-152
    In source order: Evaluate once source_literal_147_21.join((line for line in diagnostics.splitlines() if 'Using incubator modules: jdk.incubator.vector' not in line and 'GraalVM Polyglot Engine: no languages found' not in line)); assign in source target order to actionable.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:153-154
    if (the source predicate actionable is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:154-154
      In source order: Evaluate os.write(2, source_template_154_24.encode()); retain side effects and discard the expression result.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:155-155
    End this invocation with result.
  }
  Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:158-161
// Source signature: _identifier(value: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _identifier(value) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:159-160
  if (the source predicate not _IDENTIFIER.fullmatch(value) is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:160-160
    Raise ModelValidationError(source_template_160_35).
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:161-161
  End this invocation with value.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:164-169
// Source signature: _rows(result: Any) -> Iterator[FrozenMap]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _rows(result) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:165-169
  Perform the following protected operations {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:166-167
    for each row in result {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:167-167
      In source order: Yield freeze_properties(cast(dict[str, object], row.to_dict())); suspend this generator until resumed.
    }
  }
  On every exit from this protected/handler/normal-completion region {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:169-169
    In source order: Evaluate result.close(); retain side effects and discard the expression result.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:172-264
interface ArcadeGraphWriteTransaction {
  Describe the source Python type, preserving its base/metaclass expression order: AbstractContextManager['ArcadeGraphWriteTransaction'].
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:173-180
  // Source signature: __init__(self, database: Any, locator: SnapshotLocator) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self, database, locator) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:174-178
    In source order: Evaluate once database; assign in source target order to self._database. Then Evaluate once locator; assign in source target order to self._locator. Then Evaluate once False; assign in source target order to self._finished. Then For self._vertex_types, assign set(); source annotation set[str]. Then For self._combination_types, assign {}; source annotation dict[tuple[str, ...], str].
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:179-180
    In source order: For self._nodes, assign []; source annotation list[GraphNode]. Then For self._edges, assign []; source annotation list[GraphEdge].
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:182-183
  // Source signature: __enter__(self) -> ArcadeGraphWriteTransaction
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __enter__(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:183-183
    End this invocation with self.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:185-192
  // Source signature: __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: TracebackType | None) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __exit__(self, exc_type, exc_value, traceback) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:191-192
    if (the source predicate not self._finished is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:192-192
      In source order: Evaluate self.rollback(); retain side effects and discard the expression result.
    }
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:194-197
  // Source signature: write_nodes(self, nodes: tuple[GraphNode, ...]) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn write_nodes(self, nodes) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:195-196
    if (the source predicate len(nodes) > _MAX_WRITE_BATCH is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:196-196
      Raise ModelValidationError('node write batch exceeds adapter bound').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:197-197
    In source order: Evaluate self._nodes.extend(nodes); retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:199-202
  // Source signature: write_edges(self, edges: tuple[GraphEdge, ...]) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn write_edges(self, edges) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:200-201
    if (the source predicate len(edges) > _MAX_WRITE_BATCH is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:201-201
      Raise ModelValidationError('edge write batch exceeds adapter bound').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:202-202
    In source order: Evaluate self._edges.extend(edges); retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:204-224
  // Source signature: _vertex_type(self, labels: tuple[str, ...]) -> str
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _vertex_type(self, labels) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:205-205
    In source order: Evaluate once tuple((_identifier(label) for label in labels)); assign in source target order to validated.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:206-209
    for each label in validated {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:207-209
      if (the source predicate label not in self._vertex_types is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:208-209
        In source order: Evaluate self._database.schema.get_or_create_vertex_type(label); retain side effects and discard the expression result. Then Evaluate self._vertex_types.add(label); retain side effects and discard the expression result.
      }
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:210-211
    if (the source predicate len(validated) == 1 is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:211-211
      End this invocation with validated[0].
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:212-212
    In source order: Evaluate once self._combination_types.get(validated); assign in source target order to combination.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:213-214
    if (the source predicate combination is not None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:214-214
      End this invocation with combination.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:215-219
    In source order: Evaluate once hashlib.sha256('\x00'.join(validated).encode()).hexdigest(); assign in source target order to digest. Then Evaluate once source_template_216_22; assign in source target order to combination. Then Evaluate once self._database.schema; assign in source target order to schema. Then Evaluate once schema.exists_type(combination); assign in source target order to existed. Then Evaluate once schema.get_or_create_vertex_type(combination); assign in source target order to concrete.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:220-222
    if (the source predicate not existed is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:221-222
      for each label in validated {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:222-222
        In source order: Evaluate concrete.addSuperType(label); retain side effects and discard the expression result.
      }
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:223-223
    In source order: Evaluate once combination; assign in source target order to self._combination_types[validated].
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:224-224
    End this invocation with combination.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:226-259
  // Source signature: commit(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn commit(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:227-227
    In source order: For vertices, assign {}; source annotation dict[str, Any].
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:228-229
    for each relationship in sorted({edge.relationship_type for edge in self._edges}) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:229-229
      In source order: Evaluate self._database.schema.get_or_create_edge_type(_identifier(relationship)); retain side effects and discard the expression result.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:230-258
    Enter source context managers left-to-right: self._database.graph_batch(expected_edge_count=len(self._edges), use_wal=True, wal_flush='yes_full') bound to batch {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:235-248
      for each node in self._nodes {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:236-248
        In source order: Evaluate once node.properties.to_dict(); assign in source target order to properties. Then Evaluate properties.update({'id': node.id, 'localId': node.local_id, 'projectId': node.project_id.value, 'snapshotId': self._locator.snapshot_id.value, 'labels': list(node.labels)}); retain side effects and discard the expression result. Then Evaluate once batch.create_vertex(self._vertex_type(node.labels), **properties); assign in source target order to vertices[node.id].
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:249-258
      for each edge in self._edges {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:250-258
        In source order: Evaluate once _identifier(edge.relationship_type); assign in source target order to relationship. Then Evaluate once edge.properties.to_dict(); assign in source target order to properties. Then Evaluate properties.update({'id': edge.id, 'projectId': edge.project_id.value}); retain side effects and discard the expression result. Then Evaluate batch.new_edge(vertices[edge.source_id], relationship, vertices[edge.target_id], **properties); retain side effects and discard the expression result.
      }
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:259-259
    In source order: Evaluate once True; assign in source target order to self._finished.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:261-264
  // Source signature: rollback(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn rollback(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:262-264
    In source order: Evaluate self._nodes.clear(); retain side effects and discard the expression result. Then Evaluate self._edges.clear(); retain side effects and discard the expression result. Then Evaluate once True; assign in source target order to self._finished.
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:267-298
interface ArcadeGraphBackend {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:268-271
  // Source signature: __init__(self, database: Any, locator: SnapshotLocator | None=None) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self, database, locator) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:269-271
    In source order: Evaluate once database; assign in source target order to self._database. Then Evaluate once locator; assign in source target order to self._locator. Then Evaluate once False; assign in source target order to self._closed.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:273-277
  // Source signature: begin_write(self) -> AbstractContextManager[GraphWriteTransaction]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn begin_write(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:274-274
    In source order: Evaluate self._ensure_open(); retain side effects and discard the expression result.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:275-276
    if (the source predicate self._locator is None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:276-276
      Raise RuntimeError('catalog backend does not support graph writes').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:277-277
    End this invocation with ArcadeGraphWriteTransaction(self._database, self._locator).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:279-289
  // Source signature: query_readonly(self, cypher: str, parameters: FrozenMap, row_limit: int) -> Iterator[FrozenMap]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn query_readonly(self, cypher, parameters, row_limit) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:282-282
    In source order: Evaluate self._ensure_open(); retain side effects and discard the expression result.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:283-284
    if (the source predicate row_limit <= 0 is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:284-284
      Raise ModelValidationError('row_limit must be positive').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:285-285
    In source order: Evaluate once self._database.query('opencypher', cypher, parameters.to_dict()); assign in source target order to result.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:286-289
    for each (index, row) in enumerate(_rows(result)) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:287-288
      if (the source predicate index >= row_limit is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:288-288
        Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:289-289
      In source order: Yield row; suspend this generator until resumed.
    }
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:291-294
  // Source signature: close(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn close(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:292-294
    if (the source predicate not self._closed is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:293-294
      In source order: Evaluate self._database.close(); retain side effects and discard the expression result. Then Evaluate once True; assign in source target order to self._closed.
    }
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:296-298
  // Source signature: _ensure_open(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _ensure_open(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:297-298
    if (the source predicate self._closed is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:298-298
      Raise RuntimeError('backend is closed').
    }
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:301-464
interface ArcadeCatalogWriteTransaction {
  Describe the source Python type, preserving its base/metaclass expression order: AbstractContextManager['ArcadeCatalogWriteTransaction'].
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:302-305
  // Source signature: __init__(self, database: Any) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self, database) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:303-305
    In source order: Evaluate once database; assign in source target order to self._database. Then Evaluate once False; assign in source target order to self._finished. Then Evaluate database.begin(); retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:307-308
  // Source signature: __enter__(self) -> ArcadeCatalogWriteTransaction
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __enter__(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:308-308
    End this invocation with self.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:310-317
  // Source signature: __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: TracebackType | None) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __exit__(self, exc_type, exc_value, traceback) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:316-317
    if (the source predicate not self._finished is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:317-317
      In source order: Evaluate self.rollback(); retain side effects and discard the expression result.
    }
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:319-449
  // Source signature: publish(self, publication: CatalogPublication) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn publish(self, publication) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:320-337
    In source order: Evaluate once publication.snapshot.project.project_id.value; assign in source target order to project_id. Then Evaluate self._database.command('opencypher', 'MATCH (a:NodeRef)-[r]->(b:NodeRef) WHERE a.projectId=$project OR b.projectId=$project DELETE r', {'project': project_id}); retain side effects and discard the expression result. Then Evaluate self._database.command('opencypher', 'MATCH (n:NodeRef {projectId:$project}) DETACH DELETE n', {'project': project_id}); retain side effects and discard the expression result. Then Evaluate self._database.command('opencypher', 'MATCH (s:ProjectSnapshot {projectId:$project}) SET s.accepted=false', {'project': project_id}); retain side effects and discard the expression result. Then Evaluate once publication.snapshot; assign in source target order to snapshot.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:338-355
    In source order: Evaluate self._database.command('opencypher', source_literal_340_12, {'key': source_template_344_23, 'project': project_id, 'snapshot': snapshot.snapshot_id.value, 'path': snapshot.locator.database_path, 'display': snapshot.project.display_name, 'sourcePath': snapshot.project.source_path, 'sourceUrl': snapshot.project.source_url, 'revision': snapshot.project.revision, 'sdk': snapshot.analysis_version.sdk_version, 'components': json.dumps(snapshot.analysis_version.components)}); retain side effects and discard the expression result.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:356-375
    for each ref in publication.node_refs {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:357-362
      In source order: Evaluate once _node_ref_key(ref); assign in source target order to key. Then Evaluate once self._database.query('opencypher', 'MATCH (n:NodeRef {key:$key}) RETURN count(n) AS n', {'key': key}); assign in source target order to existing. Then Evaluate once next(iter(existing)).get('n'); assign in source target order to count. Then Evaluate existing.close(); retain side effects and discard the expression result.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:363-375
      if (the source predicate int(count) == 0 is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:364-375
        In source order: Evaluate self._database.command('opencypher', 'CREATE (:NodeRef {key:$key,nodeId:$node,projectId:$project,snapshotId:$snapshot,localId:$local})', {'key': key, 'node': ref.node_id, 'project': ref.project_id.value, 'snapshot': ref.snapshot_id.value, 'local': ref.local_id}); retain side effects and discard the expression result.
      }
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:376-379
    for each ref in publication.node_refs {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:377-377
      In source order: Evaluate once _node_ref_key(ref); assign in source target order to key.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:378-379
      if (the source predicate self._count('MATCH (n:NodeRef {key:$key}) RETURN count(n) AS n', {'key': key}) != 1 is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:379-379
        Raise RuntimeError(source_template_379_35).
      }
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:380-425
    for each correlation in publication.correlations {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:381-385
      In source order: Evaluate once correlation.target if correlation.source.project_id.value == project_id else correlation.source; assign in source target order to peer.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:386-395
      if (the source predicate self._count('MATCH (s:ProjectSnapshot {projectId:$project,snapshotId:$snapshot,accepted:true}) RETURN count(s) AS n', {'project': peer.project_id.value, 'snapshot': peer.snapshot_id.value}) != 1 is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:395-395
        Raise RuntimeError('correlation peer snapshot is no longer accepted').
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:396-416
      In source order: Evaluate once correlation.relationship_type.value; assign in source target order to relationship. Then Evaluate once _correlation_key(correlation); assign in source target order to correlation_key. Then Evaluate self._database.command('opencypher', source_template_400_16, {'source': _node_ref_key(correlation.source), 'target': _node_ref_key(correlation.target), 'properties': {'key': correlation_key, 'sourceKey': _node_ref_key(correlation.source), 'targetKey': _node_ref_key(correlation.target), 'providerName': correlation.provider_name, 'providerVersion': correlation.provider_version, 'confidence': correlation.confidence, 'reason': correlation.reason, 'evidence': correlation.evidence.to_dict()}}); retain side effects and discard the expression result.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:417-425
      if (the source predicate self._count('MATCH ()-[r {key:$key}]->() RETURN count(r) AS n', {'key': correlation_key}) != 1 is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:423-425
        Raise RuntimeError(source_template_424_20).
      }
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:426-434
    In source order: Evaluate self._database.command('opencypher', 'MATCH (n:NodeRef) WHERE NOT EXISTS { MATCH (n)--() } DETACH DELETE n'); retain side effects and discard the expression result. Then Evaluate self._database.command('opencypher', 'MATCH (m:ProviderManifest {projectId:$project}) DETACH DELETE m', {'project': project_id}); retain side effects and discard the expression result.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:435-446
    for each manifest in publication.provider_manifests {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:436-446
      In source order: Evaluate self._database.command('opencypher', 'CREATE (:ProviderManifest {projectId:$project,snapshotId:$snapshot,providerName:$name,providerVersion:$version})', {'project': manifest.project_id.value, 'snapshot': manifest.snapshot_id.value, 'name': manifest.provider_name, 'version': manifest.provider_version}); retain side effects and discard the expression result.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:447-449
    In source order: Evaluate self._database.command('opencypher', 'MATCH (s:ProjectSnapshot {accepted:false}) DETACH DELETE s'); retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:451-456
  // Source signature: _count(self, query: str, parameters: dict[str, object]) -> int
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _count(self, query, parameters) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:452-452
    In source order: Evaluate once self._database.query('opencypher', query, parameters); assign in source target order to result.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:453-456
    Perform the following protected operations {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:454-454
      End this invocation with int(next(iter(result)).get('n')).
    }
    On every exit from this protected/handler/normal-completion region {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:456-456
      In source order: Evaluate result.close(); retain side effects and discard the expression result.
    }
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:458-460
  // Source signature: commit(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn commit(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:459-460
    In source order: Evaluate self._database.commit(); retain side effects and discard the expression result. Then Evaluate once True; assign in source target order to self._finished.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:462-464
  // Source signature: rollback(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn rollback(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:463-464
    In source order: Evaluate self._database.rollback(); retain side effects and discard the expression result. Then Evaluate once True; assign in source target order to self._finished.
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:467-673
interface ArcadeCatalogBackend {
  Describe the source Python type, preserving its base/metaclass expression order: ArcadeGraphBackend.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:469-475
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:468-468
  Before creating this callable, evaluate and retain decorators top-to-bottom: classmethod.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:469-475
  // Source signature: create(cls, database: Any) -> ArcadeCatalogBackend
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn create(cls, database) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:470-470
    In source order: Evaluate once cls(database); assign in source target order to backend.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:471-472
    for each type_name in ('ProjectSnapshot', 'NodeRef', 'ProviderManifest') {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:472-472
      In source order: Evaluate database.schema.get_or_create_vertex_type(type_name); retain side effects and discard the expression result.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:473-474
    for each relationship in CorrelationType {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:474-474
      In source order: Evaluate database.schema.get_or_create_edge_type(relationship.value); retain side effects and discard the expression result.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:475-475
    End this invocation with backend.
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:477-479
  // Source signature: begin_publication(self) -> AbstractContextManager[CatalogWriteTransaction]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn begin_publication(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:478-478
    In source order: Evaluate self._ensure_open(); retain side effects and discard the expression result.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:479-479
    End this invocation with ArcadeCatalogWriteTransaction(self._database).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:481-494
  // Source signature: accepted_snapshot(self, project_id: ProjectId) -> ProjectSnapshot | None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn accepted_snapshot(self, project_id) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:482-491
    In source order: Evaluate once self._database.query('opencypher', source_literal_484_12, {'project': project_id.value}); assign in source target order to result. Then Evaluate once list(result); assign in source target order to rows. Then Evaluate result.close(); retain side effects and discard the expression result.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:492-493
    if (the source predicate not rows is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:493-493
      End this invocation with None.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:494-494
    End this invocation with _project_snapshot_from_row(project_id, rows[0]).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:496-510
  // Source signature: accepted_snapshots(self) -> tuple[ProjectSnapshot, ...]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn accepted_snapshots(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:497-503
    In source order: Evaluate once self._database.query('opencypher', source_literal_499_12); assign in source target order to result.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:504-510
    Perform the following protected operations {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:505-508
      End this invocation with tuple((_project_snapshot_from_row(ProjectId(str(row.get('project'))), row) for row in result)).
    }
    On every exit from this protected/handler/normal-completion region {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:510-510
      In source order: Evaluate result.close(); retain side effects and discard the expression result.
    }
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:512-521
  // Source signature: project_snapshot_count(self, project_id: ProjectId) -> int
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn project_snapshot_count(self, project_id) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:513-517
    In source order: Evaluate once self._database.query('opencypher', 'MATCH (s:ProjectSnapshot {projectId:$project}) RETURN count(s) AS n', {'project': project_id.value}); assign in source target order to result.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:518-521
    Perform the following protected operations {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:519-519
      End this invocation with int(next(iter(result)).get('n')).
    }
    On every exit from this protected/handler/normal-completion region {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:521-521
      In source order: Evaluate result.close(); retain side effects and discard the expression result.
    }
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:523-532
  // Source signature: node_ref_count(self, project_id: ProjectId) -> int
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn node_ref_count(self, project_id) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:524-528
    In source order: Evaluate once self._database.query('opencypher', 'MATCH (n:NodeRef {projectId:$project}) RETURN count(n) AS n', {'project': project_id.value}); assign in source target order to result.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:529-532
    Perform the following protected operations {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:530-530
      End this invocation with int(next(iter(result)).get('n')).
    }
    On every exit from this protected/handler/normal-completion region {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:532-532
      In source order: Evaluate result.close(); retain side effects and discard the expression result.
    }
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:534-553
  // Source signature: provider_manifests(self, project_id: ProjectId) -> tuple[ProviderManifest, ...]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn provider_manifests(self, project_id) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:535-541
    In source order: Evaluate once self._database.query('opencypher', source_literal_537_12, {'project': project_id.value}); assign in source target order to result.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:542-553
    Perform the following protected operations {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:543-551
      End this invocation with tuple((ProviderManifest(project_id, SnapshotId(str(row.get('snapshot'))), str(row.get('name')), str(row.get('version'))) for row in result)).
    }
    On every exit from this protected/handler/normal-completion region {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:553-553
      In source order: Evaluate result.close(); retain side effects and discard the expression result.
    }
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:555-627
  // Source signature: resolve_correlations(self, node_id: str, result_limit: int) -> tuple[ResolvedCorrelation, ...]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn resolve_correlations(self, node_id, result_limit) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:558-559
    if (the source predicate result_limit <= 0 is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:559-559
      Raise ModelValidationError('correlation result limit must be positive').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:560-560
    In source order: Evaluate self._database.begin(); retain side effects and discard the expression result.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:561-627
    Perform the following protected operations {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:562-581
      In source order: Evaluate once self._database.query('opencypher', source_literal_564_16, {'node': node_id, 'limit': result_limit + 1}); assign in source target order to result. Then Evaluate once list(result); assign in source target order to rows. Then Evaluate result.close(); retain side effects and discard the expression result.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:582-583
      if (the source predicate len(rows) > result_limit is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:583-583
        Raise ModelValidationError('correlation result limit exceeded').
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:584-584
      In source order: For resolved, assign []; source annotation list[ResolvedCorrelation].
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:585-624
      for each row in rows {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:586-599
        In source order: Evaluate once NodeRef(ProjectId(str(row.get('sourceProject'))), SnapshotId(str(row.get('sourceSnapshot'))), str(row.get('sourceLocal')), str(row.get('sourceNode'))); assign in source target order to queried. Then Evaluate once ProjectId(str(row.get('targetProject'))); assign in source target order to related_project. Then Evaluate once NodeRef(related_project, SnapshotId(str(row.get('snapshot'))), str(row.get('targetLocal')), str(row.get('targetNode'))); assign in source target order to related. Then Evaluate once str(row.get('queriedKey')); assign in source target order to queried_key.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:600-607
        if (the source predicate queried_key == str(row.get('sourceKey')) is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:601-602
          In source order: Evaluate once CorrelationEndpointRole.SOURCE; assign in source target order to role. Then Evaluate once (queried, related); assign in source target order to (original_source, original_target).
        }
        else {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:603-607
          if (the source predicate queried_key == str(row.get('targetKey')) is truthy) {
            // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:604-605
            In source order: Evaluate once CorrelationEndpointRole.TARGET; assign in source target order to role. Then Evaluate once (related, queried); assign in source target order to (original_source, original_target).
          }
          else {
            // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:607-607
            Raise RuntimeError('correlation direction metadata is missing').
          }
        }
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:608-624
        In source order: Evaluate once CorrelationEdge(original_source, CorrelationType(str(row.get('relationship'))), original_target, str(row.get('providerName')), str(row.get('providerVersion')), float(row.get('confidence')), str(row.get('reason')), freeze_properties(cast(dict[str, object], row.get('evidence') or {}))); assign in source target order to correlation. Then Evaluate resolved.append(ResolvedCorrelation(correlation, role, _project_snapshot_from_row(related_project, row))); retain side effects and discard the expression result.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:625-625
      End this invocation with tuple(resolved).
    }
    On every exit from this protected/handler/normal-completion region {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:627-627
      In source order: Evaluate self._database.rollback(); retain side effects and discard the expression result.
    }
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:629-673
  // Source signature: correlations_touching(self, project_id: ProjectId) -> tuple[CorrelationEdge, ...]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn correlations_touching(self, project_id) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:630-642
    In source order: Evaluate once self._database.query('opencypher', source_literal_632_12, {'project': project_id.value, 'limit': _MAX_CATALOG_CORRELATIONS + 1}); assign in source target order to result. Then For correlations, assign []; source annotation list[CorrelationEdge].
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:643-670
    Perform the following protected operations {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:644-668
      for each row in result {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:645-668
        In source order: Evaluate once NodeRef(ProjectId(str(row.get('sourceProject'))), SnapshotId(str(row.get('sourceSnapshot'))), str(row.get('sourceLocal')), str(row.get('sourceNode'))); assign in source target order to source. Then Evaluate once NodeRef(ProjectId(str(row.get('targetProject'))), SnapshotId(str(row.get('targetSnapshot'))), str(row.get('targetLocal')), str(row.get('targetNode'))); assign in source target order to target. Then Evaluate correlations.append(CorrelationEdge(source, CorrelationType(str(row.get('relationship'))), target, str(row.get('providerName')), str(row.get('providerVersion')), float(row.get('confidence')), str(row.get('reason')), freeze_properties(cast(dict[str, object], row.get('evidence') or {})))); retain side effects and discard the expression result.
      }
    }
    On every exit from this protected/handler/normal-completion region {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:670-670
      In source order: Evaluate result.close(); retain side effects and discard the expression result.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:671-672
    if (the source predicate len(correlations) > _MAX_CATALOG_CORRELATIONS is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:672-672
      Raise ModelValidationError('accepted touching correlation count exceeds bound').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:673-673
    End this invocation with tuple(correlations).
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:676-695
interface ArcadeDBBackendFactory {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:677-677
  In source order: Retain source documentation literal source_literal_677_4; it is not a model call.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:679-682
  // Source signature: create_project(self, locator: SnapshotLocator) -> GraphBackend
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn create_project(self, locator) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:680-681
    In source order: Evaluate once Path(locator.database_path); assign in source target order to path. Then Evaluate path.parent.mkdir(parents=True, exist_ok=True); retain side effects and discard the expression result.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:682-682
    End this invocation with ArcadeGraphBackend(_database_call('create_database', str(path)), locator).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:684-685
  // Source signature: open_project(self, locator: SnapshotLocator) -> GraphBackend
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn open_project(self, locator) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:685-685
    End this invocation with ArcadeGraphBackend(_database_call('open_database', locator.database_path), locator).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:687-689
  // Source signature: create_catalog(self, path: Path) -> CatalogBackend
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn create_catalog(self, path) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:688-688
    In source order: Evaluate path.parent.mkdir(parents=True, exist_ok=True); retain side effects and discard the expression result.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:689-689
    End this invocation with ArcadeCatalogBackend.create(_database_call('create_database', str(path))).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:691-692
  // Source signature: open_catalog(self, path: Path) -> CatalogBackend
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn open_catalog(self, path) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:692-692
    End this invocation with ArcadeCatalogBackend.create(_database_call('open_database', str(path))).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:694-695
  // Source signature: delete_project(self, locator: SnapshotLocator) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn delete_project(self, locator) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:695-695
    In source order: Evaluate shutil.rmtree(locator.database_path, ignore_errors=False); retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:698-714
// Source signature: _project_snapshot_from_row(project_id: ProjectId, row: Any) -> ProjectSnapshot
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _project_snapshot_from_row(project_id, row) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:699-701
  In source order: Evaluate once SnapshotId(str(row.get('snapshot'))); assign in source target order to snapshot_id. Then Evaluate once SnapshotLocator(project_id, snapshot_id, str(row.get('path'))); assign in source target order to locator. Then Evaluate once tuple((tuple(item) for item in json.loads(str(row.get('components'))))); assign in source target order to components.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:702-714
  End this invocation with ProjectSnapshot(ProjectMetadata(project_id, str(row.get('display')), source_path=_optional_string(row.get('sourcePath')), source_url=_optional_string(row.get('sourceUrl')), revision=_optional_string(row.get('revision'))), snapshot_id, locator, AnalysisVersion(str(row.get('sdk')), cast(tuple[tuple[str, str], ...], components)), True).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:717-718
// Source signature: _optional_string(value: object) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _optional_string(value) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:718-718
  End this invocation with None if value is None else str(value).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:721-722
// Source signature: _node_ref_key(ref: NodeRef) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _node_ref_key(ref) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:722-722
  End this invocation with source_template_722_11.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:725-735
// Source signature: _correlation_key(correlation: CorrelationEdge) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _correlation_key(correlation) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:726-734
  In source order: Evaluate once '\x00'.join((_node_ref_key(correlation.source), correlation.relationship_type.value, _node_ref_key(correlation.target), correlation.provider_name, correlation.provider_version)); assign in source target order to identity.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py:735-735
  End this invocation with hashlib.sha256(identity.encode()).hexdigest().
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from context_graph_sdk.backends.base import CatalogBackend, CatalogWriteTransaction, GraphBackend, GraphWriteTransaction` at source line 37: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/backends/base.py.sudo.md`.
- `from context_graph_sdk.errors import ModelValidationError` at source line 43: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/errors.py.sudo.md`.
- `from context_graph_sdk.identity import ProjectId, SnapshotId` at source line 44: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/identity.py.sudo.md`.
- `from context_graph_sdk.models import AnalysisVersion, CatalogPublication, CorrelationEdge, CorrelationEndpointRole, CorrelationType, FrozenMap, GraphEdge, GraphNode, NodeRef, ProjectMetadata, ProjectSnapshot, ProviderManifest, ResolvedCorrelation, SnapshotLocator, freeze_properties` at source line 45: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/models.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../../../prompt_representation/vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py.sudo.md). Exact strings in the evidence asset support this conversion.
