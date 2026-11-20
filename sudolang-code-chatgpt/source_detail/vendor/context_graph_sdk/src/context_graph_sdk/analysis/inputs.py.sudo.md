# vendor/context_graph_sdk/src/context_graph_sdk/analysis/inputs.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vendor/context_graph_sdk/src/context_graph_sdk/analysis/inputs.py.evidence.json`. SHA-256: `a049d88e98f8f42defc0f5d991aa70ad5cd82929636e0e294ac127ae8221b97c`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/inputs.py:15-28
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from dataclasses import dataclass, field; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.extractors.records import ExtractionResult; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.models import GraphSnapshot, LocalRelationshipType; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/inputs.py:29-40
In source order: Resolve source import from context_graph_sdk.resolution.context import ResolutionResult; preserve alias and import-time effects. Then Evaluate once (LocalRelationshipType.CALLS.value, LocalRelationshipType.SPAWNS.value, LocalRelationshipType.DELEGATES_TO.value); assign in source target order to ANALYSIS_RELATIONSHIPS. Then Evaluate once ('Method', 'Function', 'Class'); assign in source target order to _ANALYSIS_LABEL_PRIORITY.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/inputs.py:44-51
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/inputs.py:43-43
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/inputs.py:44-51
interface AnalysisNode {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/inputs.py:45-49
  In source order: For id, declare without assigning a value; source annotation str. Then For name, declare without assigning a value; source annotation str. Then For label, declare without assigning a value; source annotation str. Then For file_path, declare without assigning a value; source annotation str. Then For is_exported, declare without assigning a value; source annotation bool.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/inputs.py:50-51
  In source order: For language, declare without assigning a value; source annotation str. Then For owner_name, assign ''; source annotation str.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/inputs.py:55-60
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/inputs.py:54-54
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/inputs.py:55-60
interface AnalysisInputs {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/inputs.py:56-60
  In source order: For nodes, assign field(default_factory=dict[str, AnalysisNode]); source annotation dict[str, AnalysisNode]. Then For edges, assign field(default_factory=list[tuple[str, str, str, float]]); source annotation list[tuple[str, str, str, float]].
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/inputs.py:63-88
// Source signature: inputs_from_records(extraction: ExtractionResult, resolution: ResolutionResult) -> AnalysisInputs
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn inputs_from_records(extraction, resolution) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/inputs.py:66-66
  In source order: Evaluate once AnalysisInputs(); assign in source target order to inputs.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/inputs.py:67-77
  for each (_, file_result) in extraction.files {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/inputs.py:68-77
    for each symbol in file_result.symbols {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/inputs.py:69-77
      In source order: Evaluate once AnalysisNode(symbol.id, symbol.name, symbol.label, symbol.file_path, symbol.is_exported, symbol.language, symbol.owner_name); assign in source target order to inputs.nodes[symbol.id].
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/inputs.py:78-87
  for each edge in resolution.edges {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/inputs.py:79-80
    if (the source predicate edge.relationship.value not in ANALYSIS_RELATIONSHIPS is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/inputs.py:80-80
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/inputs.py:81-81
    In source order: Evaluate once 1.0; assign in source target order to confidence.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/inputs.py:82-84
    for each (key, value) in edge.properties {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/inputs.py:83-84
      if (the source predicate key == 'confidence' and isinstance(value, (int, float)) is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/inputs.py:84-84
        In source order: Evaluate once float(value); assign in source target order to confidence.
      }
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/inputs.py:85-87
    In source order: Evaluate inputs.edges.append((edge.source_local_id, edge.target_local_id, edge.relationship.value, confidence)); retain side effects and discard the expression result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/inputs.py:88-88
  End this invocation with inputs.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/inputs.py:91-141
// Source signature: inputs_from_snapshot(snapshot: GraphSnapshot) -> AnalysisInputs
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn inputs_from_snapshot(snapshot) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/inputs.py:92-96
  In source order: Retain source documentation literal source_literal_92_4; it is not a model call. Then Evaluate once AnalysisInputs(); assign in source target order to inputs. Then For local_by_global, assign {}; source annotation dict[str, str]. Then For owners, assign {}; source annotation dict[str, str].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/inputs.py:97-99
  for each edge in snapshot.edges {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/inputs.py:98-99
    if (the source predicate edge.relationship_type == LocalRelationshipType.HAS_METHOD.value is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/inputs.py:99-99
      In source order: Evaluate once edge.source_id; assign in source target order to owners[edge.target_id].
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/inputs.py:100-100
  In source order: For names_by_global, assign {}; source annotation dict[str, str].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/inputs.py:101-105
  for each node in snapshot.nodes {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/inputs.py:102-103
    In source order: Evaluate once node.properties.to_dict(); assign in source target order to properties. Then Evaluate once properties.get('name'); assign in source target order to name.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/inputs.py:104-105
    if (the source predicate isinstance(name, str) is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/inputs.py:105-105
      In source order: Evaluate once name; assign in source target order to names_by_global[node.id].
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/inputs.py:106-128
  for each node in snapshot.nodes {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/inputs.py:107-108
    In source order: Evaluate once node.properties.to_dict(); assign in source target order to properties. Then Evaluate once properties.get('name'); assign in source target order to name.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/inputs.py:109-110
    if (the source predicate not isinstance(name, str) or not name is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/inputs.py:110-110
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/inputs.py:111-115
    In source order: Evaluate once properties.get('filePath'); assign in source target order to file_path. Then Evaluate once properties.get('language'); assign in source target order to language. Then Evaluate once properties.get('isExported'); assign in source target order to exported. Then Evaluate once owners.get(node.id); assign in source target order to owner_global. Then Evaluate once node.local_id; assign in source target order to local_by_global[node.id].
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/inputs.py:116-128
    In source order: Evaluate once next((candidate for candidate in _ANALYSIS_LABEL_PRIORITY if candidate in node.labels), node.labels[0] if node.labels else ''); assign in source target order to label. Then Evaluate once AnalysisNode(node.local_id, name, label, file_path if isinstance(file_path, str) else '', bool(exported) if isinstance(exported, bool) else False, language if isinstance(language, str) else '', names_by_global.get(owner_global, '') if owner_global else ''); assign in source target order to inputs.nodes[node.local_id].
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/inputs.py:129-140
  for each edge in snapshot.edges {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/inputs.py:130-131
    if (the source predicate edge.relationship_type not in ANALYSIS_RELATIONSHIPS is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/inputs.py:131-131
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/inputs.py:132-133
    In source order: Evaluate once local_by_global.get(edge.source_id); assign in source target order to source. Then Evaluate once local_by_global.get(edge.target_id); assign in source target order to target.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/inputs.py:134-135
    if (the source predicate source is None or target is None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/inputs.py:135-135
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/inputs.py:136-137
    In source order: Evaluate once 1.0; assign in source target order to confidence. Then Evaluate once edge.properties.to_dict().get('confidence'); assign in source target order to raw.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/inputs.py:138-139
    if (the source predicate isinstance(raw, (int, float)) is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/inputs.py:139-139
      In source order: Evaluate once float(raw); assign in source target order to confidence.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/inputs.py:140-140
    In source order: Evaluate inputs.edges.append((source, target, edge.relationship_type, confidence)); retain side effects and discard the expression result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/inputs.py:141-141
  End this invocation with inputs.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from context_graph_sdk.extractors.records import ExtractionResult` at source line 27: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py.sudo.md`.
- `from context_graph_sdk.models import GraphSnapshot, LocalRelationshipType` at source line 28: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/models.py.sudo.md`.
- `from context_graph_sdk.resolution.context import ResolutionResult` at source line 29: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py.sudo.md`.
