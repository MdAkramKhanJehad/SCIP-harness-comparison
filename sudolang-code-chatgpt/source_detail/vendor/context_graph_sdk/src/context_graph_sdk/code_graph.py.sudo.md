# vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py.evidence.json`. SHA-256: `931cf4dda1b27f0e9c1575b172f4559eea50e0478b6bd3932b8e1726a72fcdc4`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py:15-23
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import time; preserve alias and import-time effects. Then Resolve source import from collections.abc import Mapping; preserve alias and import-time effects. Then Resolve source import from typing import TYPE_CHECKING; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py:25-39
In source order: Resolve source import from context_graph_sdk.backends import GraphSchema, SchemaPattern; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.errors import QueryTimeoutError, StructuredQueryError, StructuredQueryLimitError; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.identity import ProjectId; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.models import CorrelationEndpointRole, FrozenMap, ProjectSnapshot, SnapshotInfo, freeze_properties; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.query import QueryLimits, QueryWorkerRequest, QueryWorkerResult; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py:40-57
In source order: Resolve source import from context_graph_sdk.query.context import ExecuteQuery, is_symbol_entity, project_context, select_entity; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.query.impact import project_impact; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.query.results import ContextLimits, ContextResult, CorrelationLimits, CorrelationMatch, CorrelationResult, ImpactDirection, ImpactLimits, ImpactResult, SymbolSelector; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py:59-60
if (the source predicate TYPE_CHECKING is truthy) {
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py:60-60
  In source order: Resolve source import from context_graph_sdk.api import Workspace; preserve alias and import-time effects.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py:63-66
// Source signature: _integer_value(value: object, context: str) -> int
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _integer_value(value, context) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py:64-65
  if (the source predicate not isinstance(value, int) is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py:65-65
    Raise StructuredQueryError(source_template_65_35).
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py:66-66
  End this invocation with value.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py:69-330
interface CodeGraph {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py:70-72
  // Source signature: __init__(self, workspace: Workspace, project_id: ProjectId) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self, workspace, project_id) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py:71-72
    In source order: Evaluate once workspace; assign in source target order to self._workspace. Then Evaluate once project_id; assign in source target order to self.project_id.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py:74-92
  // Source signature: cypher(self, query: str, parameters: Mapping[str, object] | None=None, limits: QueryLimits | None=None) -> QueryWorkerResult
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn cypher(self, query, parameters, limits) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py:80-80
    In source order: Evaluate once self._workspace._resolve_with_lease(self.project_id); assign in source target order to (snapshot, lease).
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py:81-92
    Perform the following protected operations {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py:82-88
      In source order: Evaluate once QueryWorkerRequest(self._workspace._next_request_id(), snapshot.locator, query, freeze_properties(parameters), limits or self._workspace.default_query_limits); assign in source target order to request.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py:89-89
      End this invocation with self._workspace._workers.execute(request).
    }
    On every exit from this protected/handler/normal-completion region {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py:91-92
      In source order: Evaluate lease.release(); retain side effects and discard the expression result. Then Evaluate self._workspace._collect_retired(); retain side effects and discard the expression result.
    }
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py:94-107
  // Source signature: context(self, selector: str | SymbolSelector, limits: ContextLimits | None=None) -> ContextResult
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn context(self, selector, limits) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py:99-100
    In source order: Evaluate once selector if isinstance(selector, SymbolSelector) else SymbolSelector(selector); assign in source target order to selected. Then Evaluate once self._workspace._resolve_with_lease(self.project_id); assign in source target order to (snapshot, lease).
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py:101-107
    Perform the following protected operations {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py:102-104
      End this invocation with project_context(self._structured_executor(snapshot), selected, limits or ContextLimits()).
    }
    On every exit from this protected/handler/normal-completion region {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py:106-107
      In source order: Evaluate lease.release(); retain side effects and discard the expression result. Then Evaluate self._workspace._collect_retired(); retain side effects and discard the expression result.
    }
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py:109-134
  // Source signature: impact(self, selector: str | SymbolSelector, direction: ImpactDirection | str, limits: ImpactLimits | None=None, relationship_types: tuple[str, ...] | None=None) -> ImpactResult
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn impact(self, selector, direction, limits, relationship_types) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py:116-116
    In source order: Evaluate once selector if isinstance(selector, SymbolSelector) else SymbolSelector(selector); assign in source target order to selected.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py:117-122
    Perform the following protected operations {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py:118-120
      In source order: Evaluate once direction if isinstance(direction, ImpactDirection) else ImpactDirection(direction); assign in source target order to selected_direction.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py:121-122
    On the first matching source exception ValueError as exc, in handler order {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py:122-122
      Raise StructuredQueryError(source_template_122_39) with explicit source cause exc.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py:123-123
    In source order: Evaluate once self._workspace._resolve_with_lease(self.project_id); assign in source target order to (snapshot, lease).
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py:124-134
    Perform the following protected operations {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py:125-131
      End this invocation with project_impact(self._structured_executor(snapshot), selected, selected_direction, limits or ImpactLimits(), relationship_types).
    }
    On every exit from this protected/handler/normal-completion region {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py:133-134
      In source order: Evaluate lease.release(); retain side effects and discard the expression result. Then Evaluate self._workspace._collect_retired(); retain side effects and discard the expression result.
    }
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py:136-214
  // Source signature: correlations(self, selector: str | SymbolSelector, limits: CorrelationLimits | None=None, *, target_context_limits: ContextLimits | None=None) -> CorrelationResult
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn correlations(self, selector, limits, target_context_limits) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py:143-146
    In source order: Evaluate once selector if isinstance(selector, SymbolSelector) else SymbolSelector(selector); assign in source target order to selected. Then Evaluate once limits or CorrelationLimits(); assign in source target order to selected_limits. Then Evaluate once self._workspace._resolve_with_lease(self.project_id); assign in source target order to (source_snapshot, source_lease). Then Evaluate once (); assign in source target order to target_leases.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py:147-214
    Perform the following protected operations {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py:148-156
      In source order: Evaluate once select_entity(self._structured_executor(source_snapshot), selected, selected_limits.candidate_limit); assign in source target order to source. Then Evaluate once self._workspace._resolve_correlations_with_leases(source.id, selected_limits.max_results); assign in source target order to (resolved, target_leases). Then For matches, assign []; source annotation list[CorrelationMatch].
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py:157-192
      for each item in resolved {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py:158-164
        In source order: Evaluate once item.correlation; assign in source target order to correlation. Then Evaluate once correlation.target if item.queried_endpoint == CorrelationEndpointRole.SOURCE else correlation.source; assign in source target order to related. Then Evaluate once None; assign in source target order to target_context.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py:165-177
        if (the source predicate target_context_limits is not None is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py:166-171
          In source order: Evaluate once self._structured_executor(item.related_snapshot); assign in source target order to target_executor. Then Evaluate once select_entity(target_executor, SymbolSelector(related.node_id), target_context_limits.candidate_limit); assign in source target order to target_entity.
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py:172-177
          if (the source predicate is_symbol_entity(target_entity) is truthy) {
            // Source: vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py:173-177
            In source order: Evaluate once project_context(target_executor, SymbolSelector(related.node_id), target_context_limits); assign in source target order to target_context.
          }
        }
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py:178-192
        In source order: Evaluate matches.append(CorrelationMatch(correlation.relationship_type, correlation.source, correlation.target, item.queried_endpoint, item.related_snapshot, correlation.provider_name, correlation.provider_version, correlation.confidence, correlation.reason, correlation.evidence, target_context)); retain side effects and discard the expression result.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py:193-209
      End this invocation with CorrelationResult(source, tuple(sorted(matches, key=lambda match: (match.relationship_type.value, match.source.project_id.value, match.source.node_id, match.target.project_id.value, match.target.node_id, match.queried_endpoint.value, match.provider_name)))).
    }
    On every exit from this protected/handler/normal-completion region {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py:211-212
      for each lease in target_leases {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py:212-212
        In source order: Evaluate lease.release(); retain side effects and discard the expression result.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py:213-214
      In source order: Evaluate source_lease.release(); retain side effects and discard the expression result. Then Evaluate self._workspace._collect_retired(); retain side effects and discard the expression result.
    }
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py:216-218
  // Source signature: info(self) -> SnapshotInfo
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn info(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py:217-217
    In source order: Retain source documentation literal source_literal_217_8; it is not a model call.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py:218-218
    End this invocation with self._workspace.snapshot_info(self.project_id).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py:220-295
  // Source signature: schema(self) -> GraphSchema
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn schema(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py:221-221
    In source order: Evaluate once self._workspace._resolve_with_lease(self.project_id); assign in source target order to (snapshot, lease).
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py:222-295
    Perform the following protected operations {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py:223-223
      In source order: Evaluate once self._workspace.default_query_limits; assign in source target order to limits.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py:225-237
      // Source signature: execute(query: str) -> tuple[FrozenMap, ...]
      Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
      fn execute(query) {
        Bind arguments/defaults/annotations exactly as the source signature specifies.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py:226-234
        In source order: Evaluate once self._workspace._workers.execute(QueryWorkerRequest(self._workspace._next_request_id(), snapshot.locator, query, freeze_properties(), limits)); assign in source target order to result.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py:235-236
        if (the source predicate result.truncated is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py:236-236
          Raise StructuredQueryLimitError('schema result exceeded query bounds').
        }
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py:237-237
        End this invocation with result.rows.
        If execution reaches this end, finish with the source implicit None result.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py:239-275
      In source order: Evaluate once tuple((str(row['value']) for row in execute('MATCH (n) UNWIND labels(n) AS value RETURN DISTINCT value ORDER BY value'))); assign in source target order to labels. Then Evaluate once tuple((str(row['value']) for row in execute('MATCH ()-[r]->() RETURN DISTINCT type(r) AS value ORDER BY value'))); assign in source target order to relationship_types. Then Evaluate once tuple((str(row['value']) for row in execute('MATCH (n) UNWIND keys(n) AS value RETURN DISTINCT value ORDER BY value'))); assign in source target order to node_keys. Then Evaluate once tuple((str(row['value']) for row in execute('MATCH ()-[r]->() UNWIND keys(r) AS value RETURN DISTINCT value ORDER BY value'))); assign in source target order to relationship_keys. Then Evaluate once tuple((SchemaPattern(str(row['source']), str(row['relationship']), str(row['target']), _integer_value(row['count'], 'schema pattern count')) for row in execute(source_literal_271_20))); assign in source target order to patterns.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py:276-277
      In source order: Evaluate once execute('MATCH (n) RETURN count(n) AS count'); assign in source target order to node_rows. Then Evaluate once execute('MATCH ()-[r]->() RETURN count(r) AS count'); assign in source target order to relationship_rows.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py:278-279
      if (the source predicate len(node_rows) != 1 or len(relationship_rows) != 1 is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py:279-279
        Raise StructuredQueryError('schema count query returned no row').
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py:280-283
      In source order: Evaluate once _integer_value(node_rows[0]['count'], 'schema node count'); assign in source target order to node_count. Then Evaluate once _integer_value(relationship_rows[0]['count'], 'schema relationship count'); assign in source target order to relationship_count.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py:284-292
      End this invocation with GraphSchema(labels, relationship_types, node_keys, relationship_keys, patterns, node_count, relationship_count).
    }
    On every exit from this protected/handler/normal-completion region {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py:294-295
      In source order: Evaluate lease.release(); retain side effects and discard the expression result. Then Evaluate self._workspace._collect_retired(); retain side effects and discard the expression result.
    }
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py:297-330
  // Source signature: _structured_executor(self, snapshot: ProjectSnapshot) -> ExecuteQuery
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _structured_executor(self, snapshot) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py:298-299
    In source order: Evaluate once self._workspace.default_query_limits; assign in source target order to base_limits. Then Evaluate once time.monotonic() + base_limits.timeout_seconds; assign in source target order to operation_deadline.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py:301-328
    // Source signature: execute(query: str, parameters: Mapping[str, object], row_limit: int) -> tuple[FrozenMap, ...]
    Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
    fn execute(query, parameters, row_limit) {
      Bind arguments/defaults/annotations exactly as the source signature specifies.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py:306-306
      In source order: Evaluate once operation_deadline - time.monotonic(); assign in source target order to remaining.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py:307-308
      if (the source predicate remaining <= 0 is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py:308-308
        Raise QueryTimeoutError('structured query operation exceeded deadline').
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py:309-322
      In source order: Evaluate once self._workspace._workers.execute(QueryWorkerRequest(self._workspace._next_request_id(), snapshot.locator, query, freeze_properties(parameters), QueryLimits(remaining, base_limits.memory_bytes, row_limit, base_limits.byte_limit))); assign in source target order to result.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py:323-327
      if (the source predicate result.truncated is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py:324-324
        In source order: Evaluate once result.truncation_reason.value if result.truncation_reason else 'unknown'; assign in source target order to reason.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py:325-327
        Raise StructuredQueryLimitError(source_template_326_20).
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py:328-328
      End this invocation with result.rows.
      If execution reaches this end, finish with the source implicit None result.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py:330-330
    End this invocation with execute.
    If execution reaches this end, finish with the source implicit None result.
  }
}
```

## Local import links

- `from context_graph_sdk.backends import GraphSchema, SchemaPattern` at source line 25: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/backends/__init__.py.sudo.md`.
- `from context_graph_sdk.errors import QueryTimeoutError, StructuredQueryError, StructuredQueryLimitError` at source line 26: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/errors.py.sudo.md`.
- `from context_graph_sdk.identity import ProjectId` at source line 31: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/identity.py.sudo.md`.
- `from context_graph_sdk.models import CorrelationEndpointRole, FrozenMap, ProjectSnapshot, SnapshotInfo, freeze_properties` at source line 32: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/models.py.sudo.md`.
- `from context_graph_sdk.query import QueryLimits, QueryWorkerRequest, QueryWorkerResult` at source line 39: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/query/__init__.py.sudo.md`.
- `from context_graph_sdk.query.context import ExecuteQuery, is_symbol_entity, project_context, select_entity` at source line 40: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/query/context.py.sudo.md`.
- `from context_graph_sdk.query.impact import project_impact` at source line 46: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/query/impact.py.sudo.md`.
- `from context_graph_sdk.query.results import ContextLimits, ContextResult, CorrelationLimits, CorrelationMatch, CorrelationResult, ImpactDirection, ImpactLimits, ImpactResult, SymbolSelector` at source line 47: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/query/results.py.sudo.md`.
- `from context_graph_sdk.api import Workspace` at source line 60: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/api.py.sudo.md`.
