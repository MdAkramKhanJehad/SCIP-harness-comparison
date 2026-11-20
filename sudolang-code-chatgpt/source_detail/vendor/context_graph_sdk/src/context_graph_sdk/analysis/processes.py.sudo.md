# vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py.evidence.json`. SHA-256: `945c98bb8950cdeb23a94afe743978f4d53818ac077770c2434f33fd6f5d11c9`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import hashlib; preserve alias and import-time effects. Then Resolve source import import math; preserve alias and import-time effects. Then Resolve source import import posixpath; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:22-35
In source order: Resolve source import from dataclasses import dataclass, field; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.analysis.entry_points import ORCHESTRATOR_MAX_CALLERS, ORCHESTRATOR_MIN_CALLEES, entry_point_score, heuristic_label, is_command_dir, is_test_file; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.analysis.inputs import AnalysisInputs, AnalysisNode; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.errors import ModelValidationError; preserve alias and import-time effects. Then Evaluate once 10; assign in source target order to _PAGERANK_ITERATIONS.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:36-38
In source order: Evaluate once 0.85; assign in source target order to _PAGERANK_DAMPING. Then Evaluate once 10000; assign in source target order to DEFAULT_MAX_PROCESSES. Then Evaluate once 100000; assign in source target order to MAX_PROCESS_LIMIT.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:42-48
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:41-41
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:42-48
interface ProcessOptions {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:43-47
  In source order: For max_depth, assign 10; source annotation int. Then For max_branching, assign 4; source annotation int. Then For min_steps, assign 3; source annotation int. Then For max_processes, assign DEFAULT_MAX_PROCESSES; source annotation int. Then For min_confidence, assign 0.5; source annotation float.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:48-48
  In source order: For exclude_tests, assign True; source annotation bool.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:52-63
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:51-51
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:52-63
interface ProcessRecord {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:53-57
  In source order: For local_id, declare without assigning a value; source annotation str. Then For name, declare without assigning a value; source annotation str. Then For entry_point_id, declare without assigning a value; source annotation str. Then For heuristic_label, declare without assigning a value; source annotation str. Then For step_count, declare without assigning a value; source annotation int.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:58-62
  In source order: For caller_count, declare without assigning a value; source annotation int. Then For entry_point_score, declare without assigning a value; source annotation float. Then For importance, declare without assigning a value; source annotation float. Then For cross_community, declare without assigning a value; source annotation bool. Then For communities, declare without assigning a value; source annotation tuple[str, ...].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:63-63
  In source order: For steps, declare without assigning a value; source annotation tuple[tuple[str, int], ...].
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:66-110
interface FlowGraph {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:67-67
  In source order: Retain source documentation literal source_literal_67_4; it is not a model call.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:69-86
  // Source signature: __init__(self, inputs: AnalysisInputs, community_of: dict[str, str]) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self, inputs, community_of) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:74-77
    In source order: For self.symbols, assign inputs.nodes; source annotation dict[str, AnalysisNode]. Then Evaluate once community_of; assign in source target order to self.community_of. Then For self.outgoing, assign {}; source annotation dict[str, list[tuple[str, str, float]]]. Then For self.incoming, assign {}; source annotation dict[str, list[tuple[str, str, float]]].
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:78-82
    for each (source_id, target_id, relationship, confidence) in inputs.edges {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:79-80
      if (the source predicate source_id not in inputs.nodes or target_id not in inputs.nodes is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:80-80
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:81-82
      In source order: Evaluate self.outgoing.setdefault(source_id, []).append((target_id, relationship, confidence)); retain side effects and discard the expression result. Then Evaluate self.incoming.setdefault(target_id, []).append((source_id, relationship, confidence)); retain side effects and discard the expression result.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:83-84
    for each bucket in self.outgoing.values() {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:84-84
      In source order: Evaluate bucket.sort(key=lambda item: (-item[2], item[0])); retain side effects and discard the expression result.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:85-86
    for each bucket in self.incoming.values() {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:86-86
      In source order: Evaluate bucket.sort(); retain side effects and discard the expression result.
    }
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:88-93
  // Source signature: callable_ids(self) -> list[str]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn callable_ids(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:89-93
    End this invocation with sorted((symbol_id for symbol_id, symbol in self.symbols.items() if symbol.label in ('Function', 'Method'))).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:95-96
  // Source signature: incoming_of(self, node: str, relationship: str) -> list[str]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn incoming_of(self, node, relationship) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:96-96
    End this invocation with [source for source, rel, _ in self.incoming.get(node, []) if rel == relationship].
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:98-99
  // Source signature: outgoing_count(self, node: str, *relationships: str) -> int
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn outgoing_count(self, node, relationships) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:99-99
    End this invocation with sum((1 for _, rel, _ in self.outgoing.get(node, []) if rel in relationships)).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:101-110
  // Source signature: production_callers(self, node: str, relationships: tuple[str, ...]) -> int
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn production_callers(self, node, relationships) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:102-102
    In source order: Evaluate once 0; assign in source target order to count.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:103-109
    for each (source, rel, _) in self.incoming.get(node, []) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:104-105
      if (the source predicate rel not in relationships is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:105-105
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:106-106
      In source order: Evaluate once self.symbols.get(source); assign in source target order to symbol.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:107-108
      if (the source predicate symbol is not None and is_test_file(symbol.file_path) is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:108-108
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:109-109
      In source order: Apply source augmented assignment count += 1 with source evaluation/in-place semantics.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:110-110
    End this invocation with count.
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:113-121
// Source signature: _find_entry_points(graph: FlowGraph, exclude_tests: bool) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _find_entry_points(graph, exclude_tests) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:114-114
  In source order: For entry_points, assign []; source annotation list[str].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:115-120
  for each node in graph.callable_ids() {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:116-116
    In source order: Evaluate once graph.symbols[node]; assign in source target order to symbol.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:117-118
    if (the source predicate exclude_tests and is_test_file(symbol.file_path) is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:118-118
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:119-120
    if (the source predicate not graph.incoming_of(node, 'CALLS') is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:120-120
      In source order: Evaluate entry_points.append(node); retain side effects and discard the expression result.
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:121-121
  End this invocation with entry_points.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:124-138
// Source signature: _find_orchestrators(graph: FlowGraph, existing: set[str], exclude_tests: bool) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _find_orchestrators(graph, existing, exclude_tests) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:125-126
  In source order: For orchestrators, assign []; source annotation list[str]. Then Evaluate once ('CALLS', 'SPAWNS', 'DELEGATES_TO'); assign in source target order to all_relationships.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:127-137
  for each node in graph.callable_ids() {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:128-129
    if (the source predicate node in existing is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:129-129
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:130-130
    In source order: Evaluate once graph.symbols[node]; assign in source target order to symbol.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:131-132
    if (the source predicate exclude_tests and is_test_file(symbol.file_path) is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:132-132
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:133-133
    In source order: Evaluate once graph.production_callers(node, all_relationships); assign in source target order to production.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:134-135
    if (the source predicate production == 0 or production > ORCHESTRATOR_MAX_CALLERS is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:135-135
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:136-137
    if (the source predicate graph.outgoing_count(node, *all_relationships) >= ORCHESTRATOR_MIN_CALLEES is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:137-137
      In source order: Evaluate orchestrators.append(node); retain side effects and discard the expression result.
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:138-138
  End this invocation with orchestrators.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:141-154
// Source signature: _find_spawn_targets(graph: FlowGraph, existing: set[str], exclude_tests: bool) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _find_spawn_targets(graph, existing, exclude_tests) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:142-143
  In source order: For targets, assign []; source annotation list[str]. Then For seen, assign set(); source annotation set[str].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:144-153
  for each node in graph.callable_ids() {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:145-146
    if (the source predicate node in existing or node in seen is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:146-146
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:147-148
    if (the source predicate not graph.incoming_of(node, 'SPAWNS') is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:148-148
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:149-150
    In source order: Evaluate seen.add(node); retain side effects and discard the expression result. Then Evaluate once graph.symbols[node]; assign in source target order to symbol.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:151-152
    if (the source predicate exclude_tests and is_test_file(symbol.file_path) is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:152-152
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:153-153
    In source order: Evaluate targets.append(node); retain side effects and discard the expression result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:154-154
  End this invocation with targets.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:157-173
// Source signature: _find_delegate_targets(graph: FlowGraph, existing: set[str], exclude_tests: bool) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _find_delegate_targets(graph, existing, exclude_tests) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:158-158
  In source order: For targets, assign []; source annotation list[str].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:159-172
  for each node in graph.callable_ids() {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:160-161
    if (the source predicate node in existing is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:161-161
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:162-163
    if (the source predicate not graph.incoming_of(node, 'DELEGATES_TO') is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:163-163
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:164-164
    In source order: Evaluate once graph.symbols[node]; assign in source target order to symbol.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:165-166
    if (the source predicate exclude_tests and is_test_file(symbol.file_path) is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:166-166
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:167-168
    if (the source predicate graph.incoming_of(node, 'CALLS') is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:168-168
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:169-169
    In source order: Evaluate once graph.outgoing_count(node, 'CALLS') + graph.outgoing_count(node, 'SPAWNS'); assign in source target order to callees.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:170-171
    if (the source predicate callees < 3 is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:171-171
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:172-172
    In source order: Evaluate targets.append(node); retain side effects and discard the expression result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:173-173
  End this invocation with targets.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:177-185
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:176-176
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:177-185
interface _RawProcess {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:178-182
  In source order: For entry_point, declare without assigning a value; source annotation str. Then For steps, declare without assigning a value; source annotation list[tuple[str, int, int]]. Then For visited, declare without assigning a value; source annotation set[str]. Then For communities, declare without assigning a value; source annotation tuple[str, ...]. Then For cross_community, declare without assigning a value; source annotation bool.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:183-185
  In source order: For caller_count, declare without assigning a value; source annotation int. Then For importance, assign 0.0; source annotation float. Then For steps_set, assign field(default_factory=set[str]); source annotation set[str].
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:188-197
// Source signature: _spawn_sibling_counts(graph: FlowGraph) -> dict[str, int]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _spawn_sibling_counts(graph) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:189-189
  In source order: For fanout, assign {}; source annotation dict[str, int].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:190-191
  for each (source, edges) in graph.outgoing.items() {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:191-191
    In source order: Evaluate once sum((1 for _, rel, _ in edges if rel == 'SPAWNS')); assign in source target order to fanout[source].
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:192-192
  In source order: For siblings, assign {}; source annotation dict[str, int].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:193-196
  for each (target, edges) in graph.incoming.items() {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:194-196
    for each (source, rel, _) in edges {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:195-196
      if (the source predicate rel == 'SPAWNS' is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:196-196
        In source order: Evaluate once max(siblings.get(target, 0), fanout.get(source, 0)); assign in source target order to siblings[target].
      }
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:197-197
  End this invocation with siblings.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:200-206
// Source signature: _external_callers(graph: FlowGraph, node: str, visited: set[str], seen: set[str]) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _external_callers(graph, node, visited, seen) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:201-201
  In source order: For callers, assign []; source annotation list[str].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:202-205
  for each (source, _, _) in graph.incoming.get(node, []) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:203-205
    if (the source predicate source not in visited and source not in seen is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:204-205
      In source order: Evaluate seen.add(source); retain side effects and discard the expression result. Then Evaluate callers.append(source); retain side effects and discard the expression result.
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:206-206
  End this invocation with callers.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:209-407
// Source signature: detect_processes(inputs: AnalysisInputs, community_of: dict[str, str], options: ProcessOptions | None=None) -> list[ProcessRecord]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn detect_processes(inputs, community_of, options) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:214-214
  In source order: Evaluate once options or ProcessOptions(); assign in source target order to options.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:215-216
  if (the source predicate not 1 <= options.max_processes <= MAX_PROCESS_LIMIT is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:216-216
    Raise ModelValidationError(source_template_216_35).
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:217-222
  In source order: Evaluate once FlowGraph(inputs, community_of); assign in source target order to graph. Then Evaluate once _find_entry_points(graph, options.exclude_tests); assign in source target order to entry_points. Then Evaluate once set(entry_points); assign in source target order to existing. Then Evaluate once _find_orchestrators(graph, existing, options.exclude_tests); assign in source target order to orchestrators. Then Evaluate entry_points.extend(orchestrators); retain side effects and discard the expression result.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:223-227
  In source order: Evaluate existing.update(orchestrators); retain side effects and discard the expression result. Then Evaluate once _find_spawn_targets(graph, existing, options.exclude_tests); assign in source target order to spawn_targets. Then Evaluate entry_points.extend(spawn_targets); retain side effects and discard the expression result. Then Evaluate existing.update(spawn_targets); retain side effects and discard the expression result. Then Evaluate once _find_delegate_targets(graph, existing, options.exclude_tests); assign in source target order to delegate_targets.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:228-234
  In source order: Evaluate entry_points.extend(delegate_targets); retain side effects and discard the expression result. Then Evaluate entry_points.sort(); retain side effects and discard the expression result. Then Evaluate once set(orchestrators); assign in source target order to orchestrator_set. Then Evaluate once _spawn_sibling_counts(graph); assign in source target order to spawn_siblings. Then For seen_fingerprints, assign set(); source annotation set[str].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:235-235
  In source order: For raw_processes, assign []; source annotation list[_RawProcess].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:236-290
  for each entry_point in entry_points {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:237-238
    if (the source predicate len(raw_processes) >= options.max_processes is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:238-238
      Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:239-243
    In source order: Evaluate once {entry_point}; assign in source target order to visited. Then For steps, assign []; source annotation list[tuple[str, int, int]]. Then For queue, assign [(entry_point, 0)]; source annotation list[tuple[str, int]]. Then Evaluate once 0; assign in source target order to head. Then Evaluate once 0; assign in source target order to step_number.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:244-264
    while (the source predicate head < len(queue) is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:245-248
      In source order: Evaluate once queue[head]; assign in source target order to (node, depth). Then Apply source augmented assignment head += 1 with source evaluation/in-place semantics. Then Apply source augmented assignment step_number += 1 with source evaluation/in-place semantics. Then Evaluate steps.append((node, step_number, depth)); retain side effects and discard the expression result.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:249-250
      if (the source predicate depth >= options.max_depth is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:250-250
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:251-252
      In source order: Evaluate once options.max_branching * 2 if depth == 0 else options.max_branching; assign in source target order to branch_limit. Then Evaluate once 0; assign in source target order to branch_count.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:253-264
      for each (target, _, confidence) in graph.outgoing.get(node, []) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:254-255
        if (the source predicate branch_count >= branch_limit is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:255-255
          Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
        }
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:258-259
        if (the source predicate 0 < confidence < options.min_confidence is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:259-259
          Continue the immediately enclosing source loop at its next iteration.
        }
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:260-261
        if (the source predicate target in visited is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:261-261
          Continue the immediately enclosing source loop at its next iteration.
        }
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:262-264
        In source order: Evaluate visited.add(target); retain side effects and discard the expression result. Then Evaluate queue.append((target, depth + 1)); retain side effects and discard the expression result. Then Apply source augmented assignment branch_count += 1 with source evaluation/in-place semantics.
      }
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:266-267
    if (the source predicate len(steps) < options.min_steps is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:267-267
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:268-270
    In source order: Evaluate once hashlib.sha256('\x00'.join(sorted((node for node, _, _ in steps))).encode()).hexdigest()[:32]; assign in source target order to fingerprint.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:271-272
    if (the source predicate fingerprint in seen_fingerprints is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:272-272
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:273-276
    In source order: Evaluate seen_fingerprints.add(fingerprint); retain side effects and discard the expression result. Then Evaluate once {community_of[node] for node, _, _ in steps if node in community_of}; assign in source target order to community_set. Then For caller_seen, assign set(); source annotation set[str].
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:277-278
    for each (node, _, _) in steps {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:278-278
      In source order: Evaluate _external_callers(graph, node, visited, caller_seen); retain side effects and discard the expression result.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:280-290
    In source order: Evaluate raw_processes.append(_RawProcess(entry_point, steps, visited, tuple(sorted(community_set)), len(community_set) > 1, len(caller_seen), steps_set={node for node, _, _ in steps})); retain side effects and discard the expression result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:292-292
  In source order: For step_flow_count, assign {}; source annotation dict[str, int].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:293-295
  for each raw in raw_processes {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:294-295
    for each (node, _, _) in raw.steps {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:295-295
      In source order: Evaluate once step_flow_count.get(node, 0) + 1; assign in source target order to step_flow_count[node].
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:297-355
  for each raw in raw_processes {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:298-300
    In source order: Evaluate once 0.0; assign in source target order to effective_callers. Then Evaluate once 0.0; assign in source target order to effective_steps. Then Evaluate once set(); assign in source target order to caller_seen.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:301-310
    for each (node, _, depth) in raw.steps {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:302-305
      In source order: Evaluate once max(step_flow_count.get(node, 1), 1); assign in source target order to share. Then Evaluate once 1.0 / share ** (1.0 / 3.0); assign in source target order to step_weight. Then Evaluate once 1.0 / (depth + 1) / math.sqrt(share); assign in source target order to caller_weight. Then Apply source augmented assignment effective_steps += step_weight with source evaluation/in-place semantics.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:306-310
      for each caller in _external_callers(graph, node, raw.visited, caller_seen) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:307-307
        In source order: Evaluate once graph.symbols.get(caller); assign in source target order to symbol.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:308-309
        if (the source predicate symbol is not None and is_test_file(symbol.file_path) is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:309-309
          Continue the immediately enclosing source loop at its next iteration.
        }
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:310-310
        In source order: Apply source augmented assignment effective_callers += caller_weight with source evaluation/in-place semantics.
      }
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:312-320
    In source order: Evaluate once {posixpath.dirname(graph.symbols[node].file_path) for node, _, _ in raw.steps if graph.symbols[node].file_path}; assign in source target order to packages. Then Evaluate packages.discard(''); retain side effects and discard the expression result. Then Evaluate once graph.outgoing_count(raw.entry_point, 'CALLS'); assign in source target order to entry_fanout. Then Evaluate once graph.production_callers(raw.entry_point, ('CALLS', 'SPAWNS')); assign in source target order to entry_production_callers. Then Evaluate once graph.symbols[raw.entry_point]; assign in source target order to entry_symbol.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:321-326
    In source order: Evaluate once entry_symbol.file_path; assign in source target order to entry_path. Then Evaluate once float(len(raw.steps)); assign in source target order to raw_reach. Then Evaluate once (math.log1p(effective_callers) + 0.3 * math.log1p(raw_reach)) * math.log1p(effective_steps); assign in source target order to importance.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:327-329
    if (the source predicate raw.steps is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:328-329
      In source order: Evaluate once effective_steps / len(raw.steps); assign in source target order to exclusivity. Then Apply source augmented assignment importance *= 1.0 + 0.3 * math.sqrt(exclusivity) with source evaluation/in-place semantics.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:330-331
    if (the source predicate raw.cross_community is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:331-331
      In source order: Apply source augmented assignment importance *= 1.5 with source evaluation/in-place semantics.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:332-333
    if (the source predicate len(packages) > 2 is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:333-333
      In source order: Apply source augmented assignment importance *= 1.0 + 0.3 * math.log1p(len(packages) - 2) with source evaluation/in-place semantics.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:334-335
    if (the source predicate entry_fanout > 1 is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:335-335
      In source order: Apply source augmented assignment importance *= 1.0 + 0.15 * math.log1p(entry_fanout) with source evaluation/in-place semantics.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:336-337
    if (the source predicate entry_production_callers > 1 is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:337-337
      In source order: Apply source augmented assignment importance *= 1.0 + 0.2 * math.log1p(entry_production_callers) with source evaluation/in-place semantics.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:338-338
    In source order: Evaluate once spawn_siblings.get(raw.entry_point, 0); assign in source target order to siblings.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:339-340
    if (the source predicate siblings > 0 is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:340-340
      In source order: Apply source augmented assignment importance *= 1.0 + 0.5 / math.sqrt(max(siblings, 1)) with source evaluation/in-place semantics.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:342-342
    In source order: Evaluate once heuristic_label(entry_symbol.name); assign in source target order to entry_label.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:343-348
    if (the source predicate raw.entry_point in orchestrator_set and entry_label not in ('Create operation', 'Initialization') and (not is_command_dir(entry_path)) is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:348-348
      In source order: Apply source augmented assignment importance *= 1.5 with source evaluation/in-place semantics.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:349-350
    if (the source predicate entry_label in ('Create operation', 'Initialization') is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:350-350
      In source order: Apply source augmented assignment importance *= 0.2 with source evaluation/in-place semantics.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:351-352
    if (the source predicate is_command_dir(entry_path) is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:352-352
      In source order: Apply source augmented assignment importance *= 0.5 with source evaluation/in-place semantics.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:353-354
    if (the source predicate entry_path and is_test_file(entry_path) is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:354-354
      In source order: Apply source augmented assignment importance *= 0.1 with source evaluation/in-place semantics.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:355-355
    In source order: Evaluate once importance; assign in source target order to raw.importance.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:358-362
  In source order: Evaluate once {raw.entry_point: index for index, raw in enumerate(raw_processes)}; assign in source target order to entry_to_index. Then Evaluate once flow_rank_topology([[node for node, _, _ in raw.steps] for raw in raw_processes], entry_to_index); assign in source target order to (invokers, out_degree). Then Evaluate once [raw.importance for raw in raw_processes]; assign in source target order to rank.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:363-370
  for each _ in range(_PAGERANK_ITERATIONS) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:364-364
    In source order: Evaluate once [0.0] * len(raw_processes); assign in source target order to new_rank.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:365-369
    for each (index, raw) in enumerate(raw_processes) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:366-366
      In source order: Evaluate once (1 - _PAGERANK_DAMPING) * raw.importance; assign in source target order to new_rank[index].
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:367-369
      for each invoker in invokers[index] {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:368-369
        if (the source predicate out_degree[invoker] > 0 is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:369-369
          In source order: Apply source augmented assignment new_rank[index] += _PAGERANK_DAMPING * rank[invoker] / out_degree[invoker] with source evaluation/in-place semantics.
        }
      }
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:370-370
    In source order: Evaluate once new_rank; assign in source target order to rank.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:371-375
  for each (index, raw) in enumerate(raw_processes) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:372-375
    if (the source predicate raw.importance > 0 is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:373-373
      In source order: Evaluate once rank[index] / raw.importance; assign in source target order to ratio.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:374-375
      if (the source predicate ratio > 1.0 is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:375-375
        In source order: Apply source augmented assignment raw.importance *= 1.0 + math.log1p(ratio - 1.0) with source evaluation/in-place semantics.
      }
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:377-377
  In source order: For records, assign []; source annotation list[ProcessRecord].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:378-406
  for each raw in raw_processes {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:379-406
    In source order: Evaluate once graph.symbols[raw.entry_point]; assign in source target order to entry_symbol. Then Evaluate once entry_point_score(entry_symbol.name, entry_symbol.language, entry_symbol.is_exported, len(graph.incoming_of(raw.entry_point, 'CALLS')), graph.outgoing_count(raw.entry_point, 'CALLS'), entry_symbol.file_path).score; assign in source target order to score. Then Evaluate records.append(ProcessRecord(local_id=source_template_392_25, name=_qualified_flow_name(entry_symbol), entry_point_id=raw.entry_point, heuristic_label=heuristic_label(entry_symbol.name), step_count=len(raw.steps), caller_count=raw.caller_count, entry_point_score=score, importance=raw.importance, cross_community=raw.cross_community, communities=raw.communities, steps=tuple(((node, number) for node, number, _ in raw.steps)))); retain side effects and discard the expression result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:407-407
  End this invocation with records.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:410-428
// Source signature: flow_rank_topology(flow_steps: list[list[str]], entry_to_index: dict[str, int]) -> tuple[list[list[int]], list[int]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn flow_rank_topology(flow_steps, entry_to_index) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:413-421
  In source order: Retain source documentation literal source_literal_413_4; it is not a model call. Then For invokers, assign [[] for _ in flow_steps]; source annotation list[list[int]]. Then For out_degree, assign [0] * len(flow_steps); source annotation list[int].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:422-427
  for each (index, steps) in enumerate(flow_steps) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:423-427
    for each node in steps {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:424-424
      In source order: Evaluate once entry_to_index.get(node); assign in source target order to target.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:425-427
      if (the source predicate target is not None and target != index is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:426-427
        In source order: Evaluate invokers[target].append(index); retain side effects and discard the expression result. Then Apply source augmented assignment out_degree[index] += 1 with source evaluation/in-place semantics.
      }
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:428-428
  End this invocation with (invokers, out_degree).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:431-442
// Source signature: _qualified_flow_name(entry: AnalysisNode) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _qualified_flow_name(entry) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:432-432
  In source order: Evaluate once ''; assign in source target order to package.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:433-436
  if (the source predicate entry.file_path is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:434-434
    In source order: Evaluate once posixpath.dirname(entry.file_path); assign in source target order to directory.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:435-436
    if (the source predicate directory not in ('.', '/', '') is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:436-436
      In source order: Evaluate once posixpath.basename(directory); assign in source target order to package.
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:437-441
  In source order: Evaluate once [part for part in (package, entry.owner_name if entry.label == 'Method' else '', entry.name) if part]; assign in source target order to parts.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py:442-442
  End this invocation with '.'.join(parts) + '-flow'.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from context_graph_sdk.analysis.entry_points import ORCHESTRATOR_MAX_CALLERS, ORCHESTRATOR_MIN_CALLEES, entry_point_score, heuristic_label, is_command_dir, is_test_file` at source line 24: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/analysis/entry_points.py.sudo.md`.
- `from context_graph_sdk.analysis.inputs import AnalysisInputs, AnalysisNode` at source line 32: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/analysis/inputs.py.sudo.md`.
- `from context_graph_sdk.errors import ModelValidationError` at source line 33: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/errors.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../../../prompt_representation/vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py.sudo.md). Exact strings in the evidence asset support this conversion.
