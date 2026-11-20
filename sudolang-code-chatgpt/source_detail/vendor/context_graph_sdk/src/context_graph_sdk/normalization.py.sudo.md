# vendor/context_graph_sdk/src/context_graph_sdk/normalization.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vendor/context_graph_sdk/src/context_graph_sdk/normalization.py.evidence.json`. SHA-256: `5b163e34c0989a8a8a4d2a8e7b3ef1558e659daec118ce71b62355da6a4b0991`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/normalization.py:15-22
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import hashlib; preserve alias and import-time effects. Then Resolve source import import json; preserve alias and import-time effects. Then Resolve source import from .models import FrozenMap, GraphEdge, GraphNode, GraphSnapshot, PropertyValue; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/normalization.py:24-26
In source order: Evaluate once str | int | float | bool | None | list['NormalizedValue'] | dict[str, 'NormalizedValue']; assign in source target order to NormalizedValue.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/normalization.py:29-34
// Source signature: normalize_value(value: PropertyValue) -> NormalizedValue
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn normalize_value(value) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/normalization.py:30-31
  if (the source predicate isinstance(value, FrozenMap) is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/normalization.py:31-31
    End this invocation with {key: normalize_value(child) for key, child in value.entries}.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/normalization.py:32-33
  if (the source predicate isinstance(value, tuple) is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/normalization.py:33-33
    End this invocation with [normalize_value(child) for child in value].
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/normalization.py:34-34
  End this invocation with value.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/normalization.py:37-44
// Source signature: normalize_node(node: GraphNode) -> dict[str, NormalizedValue]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn normalize_node(node) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/normalization.py:38-44
  End this invocation with {'id': node.id, 'labels': list(node.labels), 'localId': node.local_id, 'properties': normalize_value(node.properties), 'projectId': node.project_id.value}.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/normalization.py:47-56
// Source signature: normalize_edge(edge: GraphEdge) -> dict[str, NormalizedValue]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn normalize_edge(edge) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/normalization.py:48-56
  End this invocation with {'discriminator': edge.discriminator, 'id': edge.id, 'properties': normalize_value(edge.properties), 'projectId': edge.project_id.value, 'source': edge.source_id, 'target': edge.target_id, 'type': edge.relationship_type}.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/normalization.py:59-65
// Source signature: normalize_snapshot(snapshot: GraphSnapshot) -> dict[str, NormalizedValue]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn normalize_snapshot(snapshot) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/normalization.py:60-60
  In source order: Retain source documentation literal source_literal_60_4; it is not a model call.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/normalization.py:61-65
  End this invocation with {'projectId': snapshot.project.project_id.value, 'nodes': [normalize_node(node) for node in snapshot.nodes], 'edges': [normalize_edge(edge) for edge in snapshot.edges]}.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/normalization.py:68-69
// Source signature: canonical_json(value: NormalizedValue) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn canonical_json(value) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/normalization.py:69-69
  End this invocation with json.dumps(value, ensure_ascii=True, separators=(',', ':'), sort_keys=True).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/normalization.py:72-73
// Source signature: graph_fingerprint(snapshot: GraphSnapshot) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn graph_fingerprint(snapshot) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/normalization.py:73-73
  End this invocation with hashlib.sha256(canonical_json(normalize_snapshot(snapshot)).encode()).hexdigest().
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from .models import FrozenMap, GraphEdge, GraphNode, GraphSnapshot, PropertyValue` at source line 22: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/models.py.sudo.md`.
