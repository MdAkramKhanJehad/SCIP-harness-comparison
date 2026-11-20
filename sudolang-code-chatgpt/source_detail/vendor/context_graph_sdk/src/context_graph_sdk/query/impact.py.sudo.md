# vendor/context_graph_sdk/src/context_graph_sdk/query/impact.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vendor/context_graph_sdk/src/context_graph_sdk/query/impact.py.evidence.json`. SHA-256: `b79c9a6357792c8688f14f9038b8ab267349a1657fcd843da4c9fec5ee04c76c`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/impact.py:15-30
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.errors import StructuredQueryError; preserve alias and import-time effects. Then Resolve source import from .context import ExecuteQuery, select_symbol, traverse_paths; preserve alias and import-time effects. Then Resolve source import from .results import EntityReference, ImpactDirection, ImpactLimits, ImpactResult, RelationshipDirection, SymbolSelector, entity_sort_key; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/impact.py:32-44
In source order: Evaluate once ('ACCESSES', 'CALLS', 'DELEGATES_TO', 'DEPENDS_ON', 'IMPLEMENTS', 'IMPORTS', 'INHERITS', 'OVERRIDES', 'SPAWNS', 'USES'); assign in source target order to IMPACT_RELATIONSHIPS. Then Evaluate once frozenset(IMPACT_RELATIONSHIPS); assign in source target order to _IMPACT_RELATIONSHIP_SET.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/impact.py:47-84
// Source signature: project_impact(execute: ExecuteQuery, selector: SymbolSelector, direction: ImpactDirection, limits: ImpactLimits, relationship_types: tuple[str, ...] | None=None) -> ImpactResult
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn project_impact(execute, selector, direction, limits, relationship_types) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/impact.py:54-55
  In source order: Evaluate once relationship_types or IMPACT_RELATIONSHIPS; assign in source target order to selected_types. Then Evaluate once sorted(set(selected_types).difference(_IMPACT_RELATIONSHIP_SET)); assign in source target order to unsupported.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/impact.py:56-57
  if (the source predicate unsupported is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/impact.py:57-57
    Raise StructuredQueryError(source_template_57_35).
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/impact.py:58-75
  In source order: Evaluate once tuple(sorted(set(selected_types))); assign in source target order to selected_types. Then Evaluate once select_symbol(execute, selector, limits.candidate_limit); assign in source target order to symbol. Then Evaluate once RelationshipDirection.INCOMING if direction == ImpactDirection.UPSTREAM else RelationshipDirection.OUTGOING; assign in source target order to traversal_direction. Then Evaluate once traverse_paths(execute, symbol, traversal_direction, selected_types, limits.max_depth, limits.max_nodes, limits.max_edges, limits.max_paths); assign in source target order to paths. Then For affected, assign {}; source annotation dict[str, EntityReference].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/impact.py:76-78
  for each path in paths {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/impact.py:77-78
    for each entity in path.nodes[1:] {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/impact.py:78-78
      In source order: Evaluate once entity; assign in source target order to affected[entity.id].
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/impact.py:79-84
  End this invocation with ImpactResult(symbol, direction, tuple(sorted(affected.values(), key=entity_sort_key)), paths).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from context_graph_sdk.errors import StructuredQueryError` at source line 19: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/errors.py.sudo.md`.
- `from .context import ExecuteQuery, select_symbol, traverse_paths` at source line 21: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/query/context.py.sudo.md`.
- `from .results import EntityReference, ImpactDirection, ImpactLimits, ImpactResult, RelationshipDirection, SymbolSelector, entity_sort_key` at source line 22: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/query/results.py.sudo.md`.
