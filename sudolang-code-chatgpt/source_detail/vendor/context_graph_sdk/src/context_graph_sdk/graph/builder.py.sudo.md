# vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py.evidence.json`. SHA-256: `95ffd7fdee546815c39d96c5aba1639b0ae4084b8009158729491e91717241c4`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:15-26
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import posixpath; preserve alias and import-time effects. Then Resolve source import from collections.abc import Callable, Mapping; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.discovery.walker import RepositoryWalk; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:27-45
In source order: Resolve source import from context_graph_sdk.errors import ModelValidationError; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.extractors.records import ExtractionResult; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.graph.symbols import owner_relationship, same_file_owner, sorted_symbols, symbol_properties; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.identity import SnapshotId; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.models import AnalysisVersion, GraphEdge, GraphNode, GraphSnapshot, LocalRelationshipType, NodeLabel, ProjectMetadata, freeze_properties; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:46-53
In source order: Resolve source import from context_graph_sdk.project.config import ManifestRecord, ProjectConfig, workspace_member_manifest_path; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.resolution.context import ResolutionResult; preserve alias and import-time effects. Then Evaluate once 'project'; assign in source target order to _PROJECT_LOCAL_ID.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:56-95
interface _SnapshotAccumulator {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:57-60
  // Source signature: __init__(self, project: ProjectMetadata) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self, project) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:58-60
    In source order: Evaluate once project; assign in source target order to self.project. Then For self.nodes, assign {}; source annotation dict[str, GraphNode]. Then For self.edges, assign {}; source annotation dict[str, GraphEdge].
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:62-65
  // Source signature: add_node(self, local_id: str, label: NodeLabel, properties: Mapping[str, object]) -> GraphNode
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn add_node(self, local_id, label, properties) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:65-65
    End this invocation with self.add_typed_node(local_id, (label.value,), properties).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:67-79
  // Source signature: add_typed_node(self, local_id: str, labels: tuple[str, ...], properties: Mapping[str, object]) -> GraphNode
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn add_typed_node(self, local_id, labels, properties) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:70-71
    In source order: Evaluate once GraphNode(self.project.project_id, local_id, labels, freeze_properties(properties)); assign in source target order to node. Then Evaluate once self.nodes.get(node.id); assign in source target order to existing.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:72-74
    if (the source predicate existing is None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:73-73
      In source order: Evaluate once node; assign in source target order to self.nodes[node.id].
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:74-74
      End this invocation with node.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:75-78
    if (the source predicate existing != node is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:76-78
      Raise ModelValidationError(source_template_77_16).
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:79-79
    End this invocation with existing.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:81-95
  // Source signature: add_edge(self, source: GraphNode, relationship: LocalRelationshipType, target: GraphNode, properties: Mapping[str, object] | None=None) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn add_edge(self, source, relationship, target, properties) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:88-95
    In source order: Evaluate once GraphEdge(self.project.project_id, source.id, relationship.value, target.id, properties=freeze_properties(properties)); assign in source target order to edge. Then Evaluate self.edges.setdefault(edge.id, edge); retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:98-248
// Source signature: build_structural_snapshot(project: ProjectMetadata, snapshot_id: SnapshotId, analysis_version: AnalysisVersion, walk: RepositoryWalk, config: ProjectConfig, documentation: Mapping[str, str] | None=None, extraction: ExtractionResult | None=None, resolution: ResolutionResult | None=None) -> GraphSnapshot
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn build_structural_snapshot(project, snapshot_id, analysis_version, walk, config, documentation, extraction, resolution) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:108-111
  In source order: Evaluate once documentation or {}; assign in source target order to documentation. Then Evaluate once _SnapshotAccumulator(project); assign in source target order to accumulator. Then For project_properties, assign {'name': project.display_name}; source annotation dict[str, object].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:112-113
  if (the source predicate project.source_path is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:113-113
    In source order: Evaluate once project.source_path; assign in source target order to project_properties['sourcePath'].
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:114-115
  if (the source predicate project.source_url is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:115-115
    In source order: Evaluate once project.source_url; assign in source target order to project_properties['sourceUrl'].
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:116-117
  if (the source predicate project.revision is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:117-117
    In source order: Evaluate once project.revision; assign in source target order to project_properties['revision'].
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:118-120
  In source order: Evaluate once accumulator.add_node(_PROJECT_LOCAL_ID, NodeLabel.PROJECT, project_properties); assign in source target order to project_node. Then For folders, assign {}; source annotation dict[str, GraphNode].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:122-129
  // Source signature: ensure_folder(relative: str) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn ensure_folder(relative) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:123-124
    if (the source predicate not relative or relative == '.' or relative in folders is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:124-124
      End this invocation with None.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:125-129
    In source order: Evaluate once accumulator.add_node(source_template_126_12, NodeLabel.FOLDER, {'name': posixpath.basename(relative), 'filePath': relative}); assign in source target order to folders[relative].
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:131-133
  for each directory in walk.directories {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:132-133
    In source order: Evaluate ensure_folder(directory); retain side effects and discard the expression result. Then Evaluate _ensure_ancestors(directory, ensure_folder); retain side effects and discard the expression result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:135-135
  In source order: For files, assign {}; source annotation dict[str, GraphNode].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:136-149
  for each walked in walk.files {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:137-144
    In source order: Evaluate _ensure_ancestors(walked.relative_path, ensure_folder); retain side effects and discard the expression result. Then For properties, assign {'name': posixpath.basename(walked.relative_path), 'filePath': walked.relative_path, 'language': walked.language, 'size': walked.size}; source annotation dict[str, object]. Then Evaluate once documentation.get(walked.relative_path); assign in source target order to content.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:145-146
    if (the source predicate content is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:146-146
      In source order: Evaluate once content; assign in source target order to properties['content'].
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:147-149
    In source order: Evaluate once accumulator.add_node(source_template_148_12, NodeLabel.FILE, properties); assign in source target order to files[walked.relative_path].
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:151-157
  for each mapping in (files, folders) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:152-157
    for each (relative, node) in mapping.items() {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:153-153
      In source order: Evaluate once posixpath.dirname(relative); assign in source target order to parent.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:154-157
      if (the source predicate parent and parent in folders is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:155-155
        In source order: Evaluate accumulator.add_edge(folders[parent], LocalRelationshipType.CONTAINS, node); retain side effects and discard the expression result.
      }
      else {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:156-157
        if (the source predicate not parent is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:157-157
          In source order: Evaluate accumulator.add_edge(project_node, LocalRelationshipType.CONTAINS, node); retain side effects and discard the expression result.
        }
      }
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:159-172
  for each dependency in config.dependencies {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:160-161
    In source order: Evaluate once files.get(dependency.source); assign in source target order to manifest_file. Then Evaluate once {'name': dependency.name, 'source': dependency.source}; assign in source target order to properties.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:162-163
    if (the source predicate dependency.version is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:163-163
      In source order: Evaluate once dependency.version; assign in source target order to properties['version'].
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:164-165
    if (the source predicate dependency.dev is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:165-165
      In source order: Evaluate once True; assign in source target order to properties['devDep'].
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:166-167
    if (the source predicate dependency.scope is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:167-167
      In source order: Evaluate once dependency.scope; assign in source target order to properties['scope'].
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:168-170
    In source order: Evaluate once accumulator.add_node(source_template_169_12, NodeLabel.DEPENDENCY, properties); assign in source target order to node.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:171-172
    if (the source predicate manifest_file is not None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:172-172
      In source order: Evaluate accumulator.add_edge(manifest_file, LocalRelationshipType.DEPENDS_ON, node); retain side effects and discard the expression result.
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:174-174
  In source order: For modules_by_manifest, assign {}; source annotation dict[str, GraphNode].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:175-191
  for each manifest in config.manifests {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:176-176
    In source order: Evaluate once files.get(manifest.source); assign in source target order to manifest_file.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:177-178
    if (the source predicate manifest_file is None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:178-178
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:179-191
    In source order: Evaluate once accumulator.add_node(source_template_180_12, NodeLabel.MODULE, {'name': manifest.name, 'version': manifest.version, 'filePath': manifest.source, 'language': manifest.language, 'source': manifest.source}); assign in source target order to module. Then Evaluate accumulator.add_edge(manifest_file, LocalRelationshipType.DEFINES, module); retain side effects and discard the expression result. Then Evaluate once module; assign in source target order to modules_by_manifest[manifest.source].
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:193-207
  for each manifest in config.manifests {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:194-195
    In source order: Evaluate once modules_by_manifest.get(manifest.source); assign in source target order to module. Then Evaluate once files.get(manifest.source); assign in source target order to manifest_file.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:196-197
    if (the source predicate module is None or manifest_file is None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:197-197
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:198-207
    for each workspace in manifest.workspaces {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:199-201
      In source order: Evaluate once _resolve_workspace_member(accumulator, manifest, workspace, modules_by_manifest); assign in source target order to member.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:202-204
      if (the source predicate member is None is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:203-204
        In source order: Evaluate once _synthetic_workspace_module(accumulator, manifest, workspace); assign in source target order to member. Then Evaluate accumulator.add_edge(manifest_file, LocalRelationshipType.DEFINES, member); retain side effects and discard the expression result.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:207-207
      In source order: Evaluate accumulator.add_edge(module, LocalRelationshipType.MEMBER_OF, member); retain side effects and discard the expression result.
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:209-225
  for each process in config.build_processes {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:210-210
    In source order: Evaluate once files.get(process.source); assign in source target order to source_file.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:211-212
    if (the source predicate source_file is None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:212-212
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:214-225
    In source order: Evaluate once accumulator.add_node(source_template_215_12, NodeLabel.PROCESS, {'name': process.name, 'entryPoint': process.entry_point, 'filePath': process.source, 'language': process.language, 'source': process.source}); assign in source target order to node. Then Evaluate accumulator.add_edge(source_file, LocalRelationshipType.DEFINES, node); retain side effects and discard the expression result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:227-228
  if (the source predicate extraction is not None is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:228-228
    In source order: Evaluate _add_symbols(accumulator, files, extraction, resolution); retain side effects and discard the expression result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:230-240
  if (the source predicate resolution is not None is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:231-231
    In source order: Evaluate once {node.local_id: node for node in accumulator.nodes.values()}; assign in source target order to nodes_by_local_id.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:232-240
    for each edge in resolution.edges {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:233-234
      In source order: Evaluate once nodes_by_local_id.get(edge.source_local_id); assign in source target order to source. Then Evaluate once nodes_by_local_id.get(edge.target_local_id); assign in source target order to target.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:238-239
      if (the source predicate source is None or target is None is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:239-239
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:240-240
      In source order: Evaluate accumulator.add_edge(source, edge.relationship, target, dict(edge.properties)); retain side effects and discard the expression result.
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:242-248
  End this invocation with GraphSnapshot(project, snapshot_id, analysis_version, tuple(accumulator.nodes.values()), tuple(accumulator.edges.values())).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:251-282
// Source signature: _add_symbols(accumulator: _SnapshotAccumulator, files: Mapping[str, GraphNode], extraction: ExtractionResult, resolution: ResolutionResult | None=None) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _add_symbols(accumulator, files, extraction, resolution) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:257-260
  In source order: Evaluate once sorted_symbols(extraction); assign in source target order to symbols. Then Evaluate once resolution.property_updates if resolution is not None else {}; assign in source target order to updates. Then For nodes_by_name, assign {}; source annotation dict[str, list[GraphNode]]. Then For node_by_symbol_id, assign {}; source annotation dict[str, GraphNode].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:261-272
  for each symbol in symbols {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:262-267
    In source order: Evaluate once symbol_properties(symbol); assign in source target order to properties. Then Evaluate properties.update(updates.get(symbol.id, {})); retain side effects and discard the expression result. Then Evaluate once ['Symbol', symbol.label]; assign in source target order to properties['symbolLabels']. Then Evaluate once accumulator.add_typed_node(symbol.id, (symbol.label,), properties); assign in source target order to node. Then Evaluate once node; assign in source target order to node_by_symbol_id[symbol.id].
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:268-269
    In source order: Evaluate nodes_by_name.setdefault(symbol.name, []).append(node); retain side effects and discard the expression result. Then Evaluate once files.get(symbol.file_path); assign in source target order to file_node.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:270-272
    if (the source predicate file_node is not None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:271-272
      In source order: Evaluate accumulator.add_edge(file_node, LocalRelationshipType.CONTAINS, node); retain side effects and discard the expression result. Then Evaluate accumulator.add_edge(file_node, LocalRelationshipType.DEFINES, node); retain side effects and discard the expression result.
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:273-282
  for each symbol in symbols {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:274-275
    if (the source predicate not symbol.owner_name is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:275-275
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:276-276
    In source order: Evaluate once same_file_owner(symbol, nodes_by_name); assign in source target order to owner_node.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:277-278
    if (the source predicate owner_node is None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:278-278
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:279-279
    In source order: Evaluate once node_by_symbol_id[symbol.id]; assign in source target order to member.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:280-281
    if (the source predicate owner_node.id == member.id is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:281-281
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:282-282
    In source order: Evaluate accumulator.add_edge(owner_node, owner_relationship(symbol), member); retain side effects and discard the expression result.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:285-288
// Source signature: _ensure_ancestors(relative: str, ensure_folder: Callable[[str], None]) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _ensure_ancestors(relative, ensure_folder) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:286-286
  In source order: Evaluate once relative.split('/'); assign in source target order to parts.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:287-288
  for each index in range(1, len(parts)) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:288-288
    In source order: Evaluate ensure_folder('/'.join(parts[:index])); retain side effects and discard the expression result.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:291-300
// Source signature: _resolve_workspace_member(accumulator: _SnapshotAccumulator, manifest: ManifestRecord, workspace: str, modules_by_manifest: Mapping[str, GraphNode]) -> GraphNode | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _resolve_workspace_member(accumulator, manifest, workspace, modules_by_manifest) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:297-297
  In source order: Evaluate once workspace_member_manifest_path(manifest, workspace); assign in source target order to member_manifest.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:298-299
  if (the source predicate member_manifest is None is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:299-299
    End this invocation with None.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:300-300
  End this invocation with modules_by_manifest.get(member_manifest).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:303-315
// Source signature: _synthetic_workspace_module(accumulator: _SnapshotAccumulator, manifest: ManifestRecord, workspace: str) -> GraphNode
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _synthetic_workspace_module(accumulator, manifest, workspace) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/builder.py:306-315
  End this invocation with accumulator.add_node(source_template_307_8, NodeLabel.MODULE, {'name': workspace, 'filePath': manifest.source, 'language': manifest.language, 'source': manifest.source}).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from context_graph_sdk.discovery.walker import RepositoryWalk` at source line 26: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py.sudo.md`.
- `from context_graph_sdk.errors import ModelValidationError` at source line 27: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/errors.py.sudo.md`.
- `from context_graph_sdk.extractors.records import ExtractionResult` at source line 28: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py.sudo.md`.
- `from context_graph_sdk.graph.symbols import owner_relationship, same_file_owner, sorted_symbols, symbol_properties` at source line 29: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/graph/symbols.py.sudo.md`.
- `from context_graph_sdk.identity import SnapshotId` at source line 35: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/identity.py.sudo.md`.
- `from context_graph_sdk.models import AnalysisVersion, GraphEdge, GraphNode, GraphSnapshot, LocalRelationshipType, NodeLabel, ProjectMetadata, freeze_properties` at source line 36: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/models.py.sudo.md`.
- `from context_graph_sdk.project.config import ManifestRecord, ProjectConfig, workspace_member_manifest_path` at source line 46: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/project/config.py.sudo.md`.
- `from context_graph_sdk.resolution.context import ResolutionResult` at source line 51: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py.sudo.md`.
