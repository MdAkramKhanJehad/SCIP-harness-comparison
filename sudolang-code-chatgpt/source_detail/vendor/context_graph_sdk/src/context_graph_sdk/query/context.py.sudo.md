# vendor/context_graph_sdk/src/context_graph_sdk/query/context.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vendor/context_graph_sdk/src/context_graph_sdk/query/context.py.evidence.json`. SHA-256: `5edf7466307b2e73edd7a5358eb7d93b59e26ca8f52a84036bfcdb22bb925e85`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from collections import defaultdict; preserve alias and import-time effects. Then Resolve source import from collections.abc import Callable, Iterable, Mapping; preserve alias and import-time effects. Then Resolve source import from dataclasses import dataclass; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:22-41
In source order: Resolve source import from typing import cast; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.errors import StructuredQueryLimitError, SymbolAmbiguousError, SymbolNotFoundError; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.models import FrozenMap, PropertyValue; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.symbols import SYMBOL_LABELS; preserve alias and import-time effects. Then Resolve source import from .results import ContextLimits, ContextResult, EntityReference, RelationshipDirection, RelationshipGroup, SymbolSelector, TraversalPath, entity_sort_key; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:43-61
In source order: Evaluate once Callable[[str, Mapping[str, object], int], tuple[FrozenMap, ...]]; assign in source target order to ExecuteQuery. Then Evaluate once ('CALLS', 'DELEGATES_TO', 'SPAWNS'); assign in source target order to CALL_RELATIONSHIPS. Then Evaluate once ('ACCESSES', 'CALLS', 'DEFINES', 'DELEGATES_TO', 'DEPENDS_ON', 'HAS_METHOD', 'HAS_PROPERTY', 'IMPLEMENTS', 'IMPORTS', 'INHERITS', 'OVERRIDES', 'SPAWNS', 'STEP_IN_PROCESS', 'USES'); assign in source target order to CONTEXT_RELATIONSHIPS.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:65-69
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:64-64
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:65-69
interface _Neighbor {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:66-69
  In source order: For current_id, declare without assigning a value; source annotation str. Then For edge_id, declare without assigning a value; source annotation str. Then For relationship_type, declare without assigning a value; source annotation str. Then For entity, declare without assigning a value; source annotation EntityReference.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:73-75
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:72-72
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:73-75
interface _FrontierPath {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:74-75
  In source order: For nodes, declare without assigning a value; source annotation tuple[EntityReference, ...]. Then For relationships, declare without assigning a value; source annotation tuple[str, ...].
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:78-167
// Source signature: project_context(execute: ExecuteQuery, selector: SymbolSelector, limits: ContextLimits) -> ContextResult
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn project_context(execute, selector, limits) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:83-98
  In source order: Evaluate once select_symbol(execute, selector, limits.candidate_limit); assign in source target order to symbol. Then Evaluate once _neighbors(execute, (symbol.id,), RelationshipDirection.INCOMING, CONTEXT_RELATIONSHIPS, limits.max_edges); assign in source target order to incoming. Then Evaluate once _neighbors(execute, (symbol.id,), RelationshipDirection.OUTGOING, CONTEXT_RELATIONSHIPS, limits.max_edges); assign in source target order to outgoing. Then Evaluate once (*incoming, *outgoing); assign in source target order to immediate.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:99-100
  if (the source predicate len(immediate) > limits.max_edges is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:100-100
    Raise StructuredQueryLimitError('context relationship edge limit exceeded').
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:101-103
  In source order: Evaluate once _file_imports(execute, symbol, limits.group_limit); assign in source target order to imports. Then Evaluate once {neighbor.entity.id for neighbor in immediate}; assign in source target order to entities. Then Evaluate entities.update((entity.id for entity in imports)); retain side effects and discard the expression result.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:104-105
  if (the source predicate len(entities) + 1 > limits.max_nodes is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:105-105
    Raise StructuredQueryLimitError('context node limit exceeded').
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:107-107
  In source order: For groups, assign defaultdict(dict); source annotation dict[tuple[str, RelationshipDirection], dict[str, EntityReference]].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:108-113
  for each (direction, neighbors) in ((RelationshipDirection.INCOMING, incoming), (RelationshipDirection.OUTGOING, outgoing)) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:112-113
    for each neighbor in neighbors {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:113-113
      In source order: Evaluate once neighbor.entity; assign in source target order to groups[neighbor.relationship_type, direction][neighbor.entity.id].
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:114-116
  In source order: Evaluate once next((key for key, group in groups.items() if len(group) > limits.group_limit), None); assign in source target order to oversized_group.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:117-120
  if (the source predicate oversized_group is not None is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:118-120
    Raise StructuredQueryLimitError(source_template_119_12).
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:121-140
  In source order: Evaluate once tuple((RelationshipGroup(relationship, direction, tuple(sorted(group.values(), key=entity_sort_key))) for (relationship, direction), group in sorted(groups.items(), key=lambda item: (item[0][0], item[0][1].value)))); assign in source target order to relationship_groups. Then Evaluate once traverse_paths(execute, symbol, RelationshipDirection.OUTGOING, CALL_RELATIONSHIPS, limits.call_depth, limits.max_nodes, limits.max_edges, limits.max_paths); assign in source target order to call_paths.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:141-167
  End this invocation with ContextResult(symbol, _unique_entities((neighbor.entity for neighbor in incoming if neighbor.relationship_type in CALL_RELATIONSHIPS)), _unique_entities((neighbor.entity for neighbor in outgoing if neighbor.relationship_type in CALL_RELATIONSHIPS)), imports, _unique_entities((neighbor.entity for neighbor in incoming if neighbor.relationship_type in {'IMPLEMENTS', 'INHERITS'})), _unique_entities((neighbor.entity for neighbor in immediate if neighbor.relationship_type == 'STEP_IN_PROCESS' or 'Process' in neighbor.entity.labels)), relationship_groups, call_paths).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:170-187
// Source signature: _file_imports(execute: ExecuteQuery, symbol: EntityReference, limit: int) -> tuple[EntityReference, ...]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _file_imports(execute, symbol, limit) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:175-176
  if (the source predicate symbol.file_path is None is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:176-176
    End this invocation with ().
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:177-184
  In source order: Evaluate once source_literal_178_8; assign in source target order to query. Then Evaluate once execute(query, {'filePath': symbol.file_path, 'limit': limit + 1}, limit + 1); assign in source target order to rows.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:185-186
  if (the source predicate len(rows) > limit is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:186-186
    Raise StructuredQueryLimitError('context import limit exceeded').
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:187-187
  End this invocation with _unique_entities((_entity(row) for row in rows)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:190-193
// Source signature: is_symbol_entity(entity: EntityReference) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn is_symbol_entity(entity) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:191-193
  End this invocation with bool(SYMBOL_LABELS.difference({'Module'}).intersection(entity.labels)) or ('Symbol' in entity.labels and 'Module' in entity.labels).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:196-201
// Source signature: select_symbol(execute: ExecuteQuery, selector: SymbolSelector, candidate_limit: int) -> EntityReference
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn select_symbol(execute, selector, candidate_limit) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:201-201
  End this invocation with _select_entity(execute, selector, candidate_limit, symbol_only=True).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:204-209
// Source signature: select_entity(execute: ExecuteQuery, selector: SymbolSelector, candidate_limit: int) -> EntityReference
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn select_entity(execute, selector, candidate_limit) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:209-209
  End this invocation with _select_entity(execute, selector, candidate_limit, symbol_only=False).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:212-258
// Source signature: _select_entity(execute: ExecuteQuery, selector: SymbolSelector, candidate_limit: int, *, symbol_only: bool) -> EntityReference
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _select_entity(execute, selector, candidate_limit, symbol_only) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:219-220
  In source order: Evaluate once ['(n.id=$value OR n.localId=$value OR n.name=$value)']; assign in source target order to clauses. Then For parameters, assign {'value': selector.value}; source annotation dict[str, object].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:221-223
  if (the source predicate selector.file_path is not None is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:222-223
    In source order: Evaluate clauses.append('n.filePath=$filePath'); retain side effects and discard the expression result. Then Evaluate once selector.file_path; assign in source target order to parameters['filePath'].
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:224-226
  if (the source predicate selector.line is not None is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:225-226
    In source order: Evaluate clauses.append('n.startLine <= $line AND n.endLine >= $line'); retain side effects and discard the expression result. Then Evaluate once selector.line; assign in source target order to parameters['line'].
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:227-232
  if (the source predicate symbol_only is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:228-232
    In source order: Evaluate clauses.append("('Symbol' IN labels(n) OR any(label IN labels(n) WHERE label IN $symbolLabels))"); retain side effects and discard the expression result. Then Evaluate clauses.append("(NOT 'Module' IN labels(n) OR 'Symbol' IN labels(n))"); retain side effects and discard the expression result. Then Evaluate once sorted(SYMBOL_LABELS); assign in source target order to parameters['symbolLabels'].
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:233-252
  In source order: Evaluate once 'MATCH (n) WHERE ' + ' AND '.join(clauses) + source_literal_236_10; assign in source target order to query. Then Evaluate once candidate_limit + 1; assign in source target order to parameters['limit']. Then Evaluate once execute(query, parameters, candidate_limit + 1); assign in source target order to rows. Then Evaluate once {entity.id: entity for row in rows for entity in (_entity(row),) if not symbol_only or is_symbol_entity(entity)}; assign in source target order to candidates_by_id. Then Evaluate once {entity_id: entity for entity_id, entity in candidates_by_id.items() if entity.id == selector.value or entity.local_id == selector.value}; assign in source target order to exact.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:253-253
  In source order: Evaluate once tuple(sorted((exact or candidates_by_id).values(), key=entity_sort_key)); assign in source target order to candidates.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:254-255
  if (the source predicate not candidates is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:255-255
    Raise SymbolNotFoundError(selector.value).
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:256-257
  if (the source predicate len(candidates) > 1 is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:257-257
    Raise SymbolAmbiguousError(selector.value, tuple((entity.id for entity in candidates))).
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:258-258
  End this invocation with next(iter(candidates)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:261-324
// Source signature: traverse_paths(execute: ExecuteQuery, start: EntityReference, direction: RelationshipDirection, relationship_types: tuple[str, ...], max_depth: int, max_nodes: int, max_edges: int, max_paths: int) -> tuple[TraversalPath, ...]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn traverse_paths(execute, start, direction, relationship_types, max_depth, max_nodes, max_edges, max_paths) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:271-272
  if (the source predicate max_depth == 0 is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:272-272
    End this invocation with ().
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:273-277
  In source order: For paths, assign []; source annotation list[TraversalPath]. Then Evaluate once [_FrontierPath((start,), ())]; assign in source target order to frontier. Then Evaluate once (start,); assign in source target order to current_entities. Then Evaluate once {start.id}; assign in source target order to seen_nodes. Then For seen_edges, assign set(); source annotation set[str].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:278-278
  In source order: For seen_paths, assign set(); source annotation set[tuple[tuple[str, ...], tuple[str, ...]]].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:279-323
  for each _ in range(max_depth) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:280-287
    In source order: Evaluate once _neighbors(execute, tuple((entity.id for entity in current_entities)), direction, relationship_types, max_edges); assign in source target order to neighbors. Then For adjacency, assign defaultdict(list); source annotation dict[str, list[_Neighbor]].
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:288-290
    for each neighbor in neighbors {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:289-290
      In source order: Evaluate adjacency[neighbor.current_id].append(neighbor); retain side effects and discard the expression result. Then Evaluate seen_edges.add(neighbor.edge_id); retain side effects and discard the expression result.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:291-292
    if (the source predicate len(seen_edges) > max_edges is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:292-292
      Raise StructuredQueryLimitError('traversal edge limit exceeded').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:293-293
    In source order: For next_frontier, assign []; source annotation list[_FrontierPath].
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:294-318
    for each path in frontier {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:295-297
      In source order: Evaluate once path.nodes[-1].id; assign in source target order to current_id. Then Evaluate once path.nodes; assign in source target order to base_nodes. Then Evaluate once path.relationships; assign in source target order to base_relationships.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:298-318
      for each neighbor in sorted(adjacency.get(current_id, ()), key=lambda item: (item.entity.id, item.relationship_type, item.edge_id)) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:302-303
        if (the source predicate neighbor.entity.id in {entity.id for entity in base_nodes} is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:303-303
          Continue the immediately enclosing source loop at its next iteration.
        }
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:304-308
        In source order: Evaluate once TraversalPath((*base_nodes, neighbor.entity), (*base_relationships, neighbor.relationship_type)); assign in source target order to candidate. Then Evaluate once _path_key(candidate); assign in source target order to candidate_key.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:309-310
        if (the source predicate candidate_key in seen_paths is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:310-310
          Continue the immediately enclosing source loop at its next iteration.
        }
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:311-314
        In source order: Evaluate seen_paths.add(candidate_key); retain side effects and discard the expression result. Then Evaluate next_frontier.append(_FrontierPath(candidate.nodes, candidate.relationships)); retain side effects and discard the expression result. Then Evaluate paths.append(candidate); retain side effects and discard the expression result. Then Evaluate seen_nodes.add(neighbor.entity.id); retain side effects and discard the expression result.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:315-316
        if (the source predicate len(seen_nodes) > max_nodes is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:316-316
          Raise StructuredQueryLimitError('traversal node limit exceeded').
        }
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:317-318
        if (the source predicate len(paths) > max_paths is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:318-318
          Raise StructuredQueryLimitError('traversal path limit exceeded').
        }
      }
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:319-320
    if (the source predicate not next_frontier is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:320-320
      Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:321-323
    In source order: Evaluate next_frontier.sort(key=_frontier_key); retain side effects and discard the expression result. Then Evaluate once next_frontier; assign in source target order to frontier. Then Evaluate once tuple((path.nodes[-1] for path in next_frontier)); assign in source target order to current_entities.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:324-324
  End this invocation with tuple(sorted(paths, key=_path_key)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:327-367
// Source signature: _neighbors(execute: ExecuteQuery, current_ids: tuple[str, ...], direction: RelationshipDirection, relationship_types: tuple[str, ...], max_edges: int) -> tuple[_Neighbor, ...]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _neighbors(execute, current_ids, direction, relationship_types, max_edges) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:334-335
  if (the source predicate not current_ids is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:335-335
    End this invocation with ().
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:336-339
  if (the source predicate direction == RelationshipDirection.OUTGOING is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:337-337
    In source order: Evaluate once '(current)-[r]->(neighbor)'; assign in source target order to pattern.
  }
  else {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:339-339
    In source order: Evaluate once '(neighbor)-[r]->(current)'; assign in source target order to pattern.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:340-356
  In source order: Evaluate once source_template_341_8; assign in source target order to query. Then Evaluate once execute(query, {'ids': list(current_ids), 'relationships': list(relationship_types), 'limit': max_edges + 1}, max_edges + 1); assign in source target order to rows.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:357-358
  if (the source predicate len(rows) > max_edges is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:358-358
    Raise StructuredQueryLimitError('traversal edge limit exceeded').
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:359-367
  End this invocation with tuple((_Neighbor(str(row['currentId']), str(row['edgeId']), str(row['relationship']), _entity(row)) for row in rows)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:370-381
// Source signature: _entity(row: FrozenMap) -> EntityReference
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _entity(row) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:371-372
  In source order: Evaluate once row['labels']; assign in source target order to labels_value. Then Evaluate once tuple((str(label) for label in cast(tuple[PropertyValue, ...], labels_value))); assign in source target order to labels.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:373-381
  End this invocation with EntityReference(str(row['id']), str(row['localId']), str(row['name'] or ''), labels, str(row['filePath']) if row['filePath'] is not None else None, cast(int | None, row['startLine']), cast(int | None, row['endLine'])).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:384-388
// Source signature: _unique_entities(entities: Iterable[EntityReference]) -> tuple[EntityReference, ...]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _unique_entities(entities) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:385-385
  In source order: For unique, assign {}; source annotation dict[str, EntityReference].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:386-387
  for each entity in entities {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:387-387
    In source order: Evaluate once entity; assign in source target order to unique[entity.id].
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:388-388
  End this invocation with tuple(sorted(unique.values(), key=entity_sort_key)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:391-392
// Source signature: _path_key(path: TraversalPath) -> tuple[tuple[str, ...], tuple[str, ...]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _path_key(path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:392-392
  End this invocation with (tuple((entity.id for entity in path.nodes)), path.relationships).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:395-396
// Source signature: _frontier_key(path: _FrontierPath) -> tuple[tuple[str, ...], tuple[str, ...]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _frontier_key(path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/context.py:396-396
  End this invocation with (tuple((entity.id for entity in path.nodes)), path.relationships).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from context_graph_sdk.errors import StructuredQueryLimitError, SymbolAmbiguousError, SymbolNotFoundError` at source line 24: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/errors.py.sudo.md`.
- `from context_graph_sdk.models import FrozenMap, PropertyValue` at source line 29: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/models.py.sudo.md`.
- `from context_graph_sdk.symbols import SYMBOL_LABELS` at source line 30: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/symbols.py.sudo.md`.
- `from .results import ContextLimits, ContextResult, EntityReference, RelationshipDirection, RelationshipGroup, SymbolSelector, TraversalPath, entity_sort_key` at source line 32: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/query/results.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../../../prompt_representation/vendor/context_graph_sdk/src/context_graph_sdk/query/context.py.sudo.md). Exact strings in the evidence asset support this conversion.
