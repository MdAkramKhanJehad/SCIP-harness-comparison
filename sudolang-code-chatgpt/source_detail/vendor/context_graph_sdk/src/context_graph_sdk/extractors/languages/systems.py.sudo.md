# vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/systems.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/systems.py.evidence.json`. SHA-256: `40524933940baca89cf369fa49e531ab682e6cc01acc60d5e72be7642b1714d8`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/systems.py:15-23
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import re; preserve alias and import-time effects. Then Resolve source import from tree_sitter import Node; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.extractors.analysis import node_text; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/systems.py:25-26
In source order: Evaluate once re.compile('[^A-Za-z_]+'); assign in source target order to _TOKEN_SPLIT. Then Evaluate once ('virtual', 'override', 'final'); assign in source target order to _MODIFIER_KEYWORDS.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/systems.py:29-34
// Source signature: cpp_annotation_supplement(def_node: Node, source: bytes) -> tuple[str, ...]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn cpp_annotation_supplement(def_node, source) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/systems.py:30-30
  In source order: Evaluate once node_text(def_node, source); assign in source target order to text.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/systems.py:31-32
  if (the source predicate not text is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/systems.py:32-32
    End this invocation with ().
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/systems.py:33-33
  In source order: Evaluate once set(_TOKEN_SPLIT.split(text)); assign in source target order to tokens.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/systems.py:34-34
  End this invocation with tuple((keyword for keyword in _MODIFIER_KEYWORDS if keyword in tokens)).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from context_graph_sdk.extractors.analysis import node_text` at source line 23: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py.sudo.md`.
