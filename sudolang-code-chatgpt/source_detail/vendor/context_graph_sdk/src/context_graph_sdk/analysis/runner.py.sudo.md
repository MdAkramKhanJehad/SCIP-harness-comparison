# vendor/context_graph_sdk/src/context_graph_sdk/analysis/runner.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vendor/context_graph_sdk/src/context_graph_sdk/analysis/runner.py.evidence.json`. SHA-256: `2623789980435e76e514f67a520e2d34143077ba463bd49859803fe1be36bcc7`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/runner.py:15-32
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from dataclasses import dataclass, field; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.analysis.communities import CommunityRecord, detect_communities; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.analysis.inputs import AnalysisInputs, inputs_from_records, inputs_from_snapshot; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/runner.py:33-42
In source order: Resolve source import from context_graph_sdk.analysis.processes import ProcessOptions, ProcessRecord, detect_processes; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.extractors.records import ExtractionResult; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.models import GraphEdge, GraphNode, GraphSnapshot, LocalRelationshipType, freeze_properties; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.resolution.context import ResolutionResult; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/runner.py:46-49
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/runner.py:45-45
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/runner.py:46-49
interface DerivedNode {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/runner.py:47-49
  In source order: For local_id, declare without assigning a value; source annotation str. Then For label, declare without assigning a value; source annotation str. Then For properties, declare without assigning a value; source annotation tuple[tuple[str, object], ...].
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/runner.py:53-57
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/runner.py:52-52
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/runner.py:53-57
interface DerivedEdge {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/runner.py:54-57
  In source order: For source_local_id, declare without assigning a value; source annotation str. Then For relationship, declare without assigning a value; source annotation LocalRelationshipType. Then For target_local_id, declare without assigning a value; source annotation str. Then For properties, assign (); source annotation tuple[tuple[str, object], ...].
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/runner.py:61-65
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/runner.py:60-60
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/runner.py:61-65
interface DerivedAnalysis {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/runner.py:62-65
  In source order: For nodes, assign field(default_factory=list[DerivedNode]); source annotation list[DerivedNode]. Then For edges, assign field(default_factory=list[DerivedEdge]); source annotation list[DerivedEdge]. Then For communities, assign field(default_factory=list[CommunityRecord]); source annotation list[CommunityRecord]. Then For processes, assign field(default_factory=list[ProcessRecord]); source annotation list[ProcessRecord].
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/runner.py:68-113
// Source signature: _derive(inputs: AnalysisInputs, process_options: ProcessOptions | None) -> DerivedAnalysis
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _derive(inputs, process_options) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/runner.py:69-71
  In source order: Evaluate once DerivedAnalysis(); assign in source target order to derived. Then Evaluate once detect_communities(inputs); assign in source target order to derived.communities. Then For community_of, assign {}; source annotation dict[str, str].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/runner.py:72-88
  for each community in derived.communities {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/runner.py:73-83
    In source order: Evaluate derived.nodes.append(DerivedNode(community.local_id, 'Community', (('modularity', community.modularity), ('name', community.name), ('size', community.size)))); retain side effects and discard the expression result.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/runner.py:84-88
    for each member_id in community.member_ids {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/runner.py:85-88
      In source order: Evaluate once community.name; assign in source target order to community_of[member_id]. Then Evaluate derived.edges.append(DerivedEdge(member_id, LocalRelationshipType.MEMBER_OF, community.local_id)); retain side effects and discard the expression result.
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/runner.py:90-90
  In source order: Evaluate once detect_processes(inputs, community_of, process_options); assign in source target order to derived.processes.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/runner.py:91-112
  for each process in derived.processes {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/runner.py:92-100
    In source order: For properties, assign [('callerCount', process.caller_count), ('entryPoint', process.entry_point_id), ('entryPointScore', process.entry_point_score), ('heuristicLabel', process.heuristic_label), ('importance', process.importance), ('name', process.name), ('stepCount', process.step_count)]; source annotation list[tuple[str, object]].
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/runner.py:101-102
    if (the source predicate process.cross_community is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/runner.py:102-102
      In source order: Evaluate properties.append(('crossCommunity', True)); retain side effects and discard the expression result.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/runner.py:103-103
    In source order: Evaluate derived.nodes.append(DerivedNode(process.local_id, 'Process', tuple(properties))); retain side effects and discard the expression result.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/runner.py:104-112
    for each (step_id, step_number) in process.steps {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/runner.py:105-112
      In source order: Evaluate derived.edges.append(DerivedEdge(step_id, LocalRelationshipType.STEP_IN_PROCESS, process.local_id, (('step', step_number),))); retain side effects and discard the expression result.
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/runner.py:113-113
  End this invocation with derived.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/runner.py:116-122
// Source signature: derive_analysis(extraction: ExtractionResult, resolution: ResolutionResult, process_options: ProcessOptions | None=None) -> DerivedAnalysis
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn derive_analysis(extraction, resolution, process_options) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/runner.py:121-121
  In source order: Retain source documentation literal source_literal_121_4; it is not a model call.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/runner.py:122-122
  End this invocation with _derive(inputs_from_records(extraction, resolution), process_options).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/runner.py:125-166
// Source signature: derive_snapshot(snapshot: GraphSnapshot, process_options: ProcessOptions | None=None) -> GraphSnapshot
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn derive_snapshot(snapshot, process_options) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/runner.py:128-130
  In source order: Retain source documentation literal source_literal_128_4; it is not a model call. Then Evaluate once _derive(inputs_from_snapshot(snapshot), process_options); assign in source target order to derived.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/runner.py:131-132
  if (the source predicate not derived.nodes and (not derived.edges) is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/runner.py:132-132
    End this invocation with snapshot.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/runner.py:133-135
  In source order: Evaluate once snapshot.project.project_id; assign in source target order to project_id. Then Evaluate once list(snapshot.nodes); assign in source target order to new_nodes. Then For nodes_by_local, assign {node.local_id: node for node in snapshot.nodes}; source annotation dict[str, GraphNode].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/runner.py:136-144
  for each derived_node in derived.nodes {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/runner.py:137-144
    In source order: Evaluate once GraphNode(project_id, derived_node.local_id, (derived_node.label,), freeze_properties(dict(derived_node.properties))); assign in source target order to node. Then Evaluate once node; assign in source target order to nodes_by_local[node.local_id]. Then Evaluate new_nodes.append(node); retain side effects and discard the expression result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/runner.py:145-145
  In source order: Evaluate once list(snapshot.edges); assign in source target order to new_edges.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/runner.py:146-159
  for each derived_edge in derived.edges {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/runner.py:147-148
    In source order: Evaluate once nodes_by_local.get(derived_edge.source_local_id); assign in source target order to source. Then Evaluate once nodes_by_local.get(derived_edge.target_local_id); assign in source target order to target.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/runner.py:149-150
    if (the source predicate source is None or target is None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/runner.py:150-150
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/runner.py:151-159
    In source order: Evaluate new_edges.append(GraphEdge(project_id, source.id, derived_edge.relationship.value, target.id, properties=freeze_properties(dict(derived_edge.properties)))); retain side effects and discard the expression result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/runner.py:160-166
  End this invocation with GraphSnapshot(snapshot.project, snapshot.snapshot_id, snapshot.analysis_version, tuple(new_nodes), tuple(new_edges)).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from context_graph_sdk.analysis.communities import CommunityRecord, detect_communities` at source line 27: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py.sudo.md`.
- `from context_graph_sdk.analysis.inputs import AnalysisInputs, inputs_from_records, inputs_from_snapshot` at source line 28: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/analysis/inputs.py.sudo.md`.
- `from context_graph_sdk.analysis.processes import ProcessOptions, ProcessRecord, detect_processes` at source line 33: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py.sudo.md`.
- `from context_graph_sdk.extractors.records import ExtractionResult` at source line 34: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py.sudo.md`.
- `from context_graph_sdk.models import GraphEdge, GraphNode, GraphSnapshot, LocalRelationshipType, freeze_properties` at source line 35: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/models.py.sudo.md`.
- `from context_graph_sdk.resolution.context import ResolutionResult` at source line 42: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py.sudo.md`.
