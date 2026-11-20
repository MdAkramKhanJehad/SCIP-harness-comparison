# vendor/context_graph_sdk/src/context_graph_sdk/extractors/descriptors.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vendor/context_graph_sdk/src/context_graph_sdk/extractors/descriptors.py.evidence.json`. SHA-256: `16819b56fd1a302ba16ca426849d2820c19fb5b28db13bed5730fa4344dc39b0`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/descriptors.py:15-26
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from collections.abc import Callable; preserve alias and import-time effects. Then Resolve source import from dataclasses import dataclass; preserve alias and import-time effects. Then Resolve source import from tree_sitter import Node; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/descriptors.py:28-46
In source order: Resolve source import from context_graph_sdk.extractors.analysis import has_ancestor_type, has_scala_bare_visibility, has_sibling_modifier, has_sibling_modifier_text, has_sibling_node_type, has_visibility_modifier; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.extractors.languages.jvm import extract_infix_calls, extract_primary_constructor_params, reclassify_interface_declarations; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.extractors.languages.ruby import route_ruby_calls; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.extractors.languages.solidity import include_solidity_call, solidity_annotation_supplement; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.extractors.languages.systems import cpp_annotation_supplement; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/descriptors.py:47-50
In source order: Resolve source import from context_graph_sdk.extractors.records import MutableFileResult; preserve alias and import-time effects. Then Evaluate once Callable[[Node, bytes, str, str, MutableFileResult], None]; assign in source target order to PostPass.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/descriptors.py:54-59
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/descriptors.py:53-53
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/descriptors.py:54-59
interface LanguageDescriptor {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/descriptors.py:55-59
  In source order: For is_exported, declare without assigning a value; source annotation Callable[[Node, str, bytes], bool]. Then For interface_method_specs, assign False; source annotation bool. Then For include_call, assign None; source annotation Callable[[str, Node, bytes], bool] | None. Then For annotation_supplement, assign None; source annotation Callable[[Node, bytes], tuple[str, ...]] | None. Then For post_passes, assign (); source annotation tuple[PostPass, ...].
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/descriptors.py:62-63
// Source signature: _exported_go(_node: Node, name: str, _source: bytes) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _exported_go(_node, name, _source) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/descriptors.py:63-63
  End this invocation with bool(name) and name[0].isupper() and name[0].isascii().
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/descriptors.py:66-67
// Source signature: _exported_python(_node: Node, name: str, _source: bytes) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _exported_python(_node, name, _source) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/descriptors.py:67-67
  End this invocation with not name.startswith('_').
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/descriptors.py:70-71
// Source signature: _exported_ecmascript(node: Node, _name: str, _source: bytes) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _exported_ecmascript(node, _name, _source) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/descriptors.py:71-71
  End this invocation with has_ancestor_type(node, 'export_statement').
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/descriptors.py:74-75
// Source signature: _exported_public_modifier(node: Node, _name: str, source: bytes) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _exported_public_modifier(node, _name, source) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/descriptors.py:75-75
  End this invocation with has_sibling_modifier(node, source, 'public').
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/descriptors.py:78-79
// Source signature: _exported_kotlin(node: Node, _name: str, source: bytes) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _exported_kotlin(node, _name, source) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/descriptors.py:79-79
  End this invocation with not has_visibility_modifier(node, source, 'private', 'internal', 'protected').
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/descriptors.py:82-83
// Source signature: _exported_rust(node: Node, _name: str, _source: bytes) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _exported_rust(node, _name, _source) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/descriptors.py:83-83
  End this invocation with has_sibling_node_type(node, 'visibility_modifier').
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/descriptors.py:86-87
// Source signature: _exported_c_family(node: Node, _name: str, source: bytes) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _exported_c_family(node, _name, source) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/descriptors.py:87-87
  End this invocation with not has_sibling_modifier_text(node, source, 'storage_class_specifier', 'static').
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/descriptors.py:90-91
// Source signature: _exported_always(_node: Node, _name: str, _source: bytes) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _exported_always(_node, _name, _source) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/descriptors.py:91-91
  End this invocation with True.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/descriptors.py:94-95
// Source signature: _exported_php(node: Node, _name: str, source: bytes) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _exported_php(node, _name, source) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/descriptors.py:95-95
  End this invocation with not has_visibility_modifier(node, source, 'private', 'protected').
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/descriptors.py:98-99
// Source signature: _exported_swift(node: Node, _name: str, source: bytes) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _exported_swift(node, _name, source) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/descriptors.py:99-99
  End this invocation with has_visibility_modifier(node, source, 'public', 'open').
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/descriptors.py:102-103
// Source signature: _exported_scala(node: Node, _name: str, source: bytes) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _exported_scala(node, _name, source) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/descriptors.py:103-103
  End this invocation with not has_scala_bare_visibility(node, source).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/descriptors.py:106-107
// Source signature: _exported_dart(_node: Node, name: str, _source: bytes) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _exported_dart(_node, name, _source) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/descriptors.py:107-107
  End this invocation with not name.startswith('_').
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/descriptors.py:110-111
// Source signature: _exported_solidity(node: Node, _name: str, source: bytes) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _exported_solidity(node, _name, source) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/descriptors.py:111-111
  End this invocation with not has_visibility_modifier(node, source, 'private', 'internal').
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/descriptors.py:114-147
In source order: For _JVM_POST_PASSES, assign (reclassify_interface_declarations, extract_infix_calls, extract_primary_constructor_params); source annotation tuple[PostPass, ...]. Then For LANGUAGE_DESCRIPTORS, assign {'go': LanguageDescriptor(_exported_go, interface_method_specs=True), 'python': LanguageDescriptor(_exported_python), 'javascript': LanguageDescriptor(_exported_ecmascript), 'typescript': LanguageDescriptor(_exported_ecmascript), 'tsx': LanguageDescriptor(_exported_ecmascript), 'java': LanguageDescriptor(_exported_public_modifier), 'kotlin': LanguageDescriptor(_exported_kotlin, post_passes=_JVM_POST_PASSES), 'csharp': LanguageDescriptor(_exported_public_modifier, post_passes=(extract_primary_constructor_params,)), 'scala': LanguageDescriptor(_exported_scala, post_passes=(extract_infix_calls, extract_primary_constructor_params)), 'c': LanguageDescriptor(_exported_c_family), 'cpp': LanguageDescriptor(_exported_c_family, annotation_supplement=cpp_annotation_supplement), 'rust': LanguageDescriptor(_exported_rust), 'ruby': LanguageDescriptor(_exported_always, post_passes=(route_ruby_calls,)), 'php': LanguageDescriptor(_exported_php), 'swift': LanguageDescriptor(_exported_swift, interface_method_specs=True), 'dart': LanguageDescriptor(_exported_dart), 'solidity': LanguageDescriptor(_exported_solidity, include_call=include_solidity_call, annotation_supplement=solidity_annotation_supplement)}; source annotation dict[str, LanguageDescriptor].
```

## Local import links

- `from context_graph_sdk.extractors.analysis import has_ancestor_type, has_scala_bare_visibility, has_sibling_modifier, has_sibling_modifier_text, has_sibling_node_type, has_visibility_modifier` at source line 28: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py.sudo.md`.
- `from context_graph_sdk.extractors.languages.jvm import extract_infix_calls, extract_primary_constructor_params, reclassify_interface_declarations` at source line 36: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/jvm.py.sudo.md`.
- `from context_graph_sdk.extractors.languages.ruby import route_ruby_calls` at source line 41: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py.sudo.md`.
- `from context_graph_sdk.extractors.languages.solidity import include_solidity_call, solidity_annotation_supplement` at source line 42: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/solidity.py.sudo.md`.
- `from context_graph_sdk.extractors.languages.systems import cpp_annotation_supplement` at source line 46: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/systems.py.sudo.md`.
- `from context_graph_sdk.extractors.records import MutableFileResult` at source line 47: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py.sudo.md`.
