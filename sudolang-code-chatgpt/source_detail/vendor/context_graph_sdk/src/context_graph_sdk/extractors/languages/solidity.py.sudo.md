# vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/solidity.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/solidity.py.evidence.json`. SHA-256: `aea094aac893429220f6259411e626b48b7ca978db48b2e72f1e8092597f511e`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/solidity.py:15-28
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import re; preserve alias and import-time effects. Then Resolve source import from tree_sitter import Node; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.extractors.analysis import extract_signature, first_identifier_text, node_text, walk; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/solidity.py:29-46
In source order: Resolve source import from context_graph_sdk.extractors.records import is_valid_symbol_name; preserve alias and import-time effects. Then Evaluate once re.compile('returns\\s*\\([^)]*\\)'); assign in source target order to _RETURNS. Then Evaluate once re.compile('\\b([A-Za-z_][A-Za-z0-9_]*)\\s*(\\(|$|\\s)'); assign in source target order to _MODIFIER_NAME. Then Evaluate once frozenset({'public', 'external', 'internal', 'private', 'view', 'pure', 'payable', 'virtual', 'override', 'returns'}); assign in source target order to _NON_MODIFIER_TOKENS.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/solidity.py:49-57
// Source signature: _ancestor_exact(node: Node, node_type: str, max_depth: int) -> Node | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _ancestor_exact(node, node_type, max_depth) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/solidity.py:50-50
  In source order: Evaluate once node.parent; assign in source target order to current.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/solidity.py:51-56
  for each _ in range(max_depth) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/solidity.py:52-53
    if (the source predicate current is None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/solidity.py:53-53
      End this invocation with None.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/solidity.py:54-55
    if (the source predicate current.type == node_type is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/solidity.py:55-55
      End this invocation with current.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/solidity.py:56-56
    In source order: Evaluate once current.parent; assign in source target order to current.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/solidity.py:57-57
  End this invocation with None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/solidity.py:60-78
// Source signature: include_solidity_call(callee: str, name_node: Node, source: bytes) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn include_solidity_call(callee, name_node, source) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/solidity.py:61-63
  In source order: Retain source documentation literal source_literal_61_4; it is not a model call. Then Evaluate once _ancestor_exact(name_node, 'modifier_invocation', 6); assign in source target order to modifier_invocation.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/solidity.py:64-65
  if (the source predicate modifier_invocation is None is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/solidity.py:65-65
    End this invocation with True.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/solidity.py:66-66
  In source order: Evaluate once _ancestor_exact(modifier_invocation, 'constructor_definition', 8); assign in source target order to constructor.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/solidity.py:67-68
  if (the source predicate constructor is None is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/solidity.py:68-68
    End this invocation with False.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/solidity.py:69-69
  In source order: Evaluate once _ancestor_exact(constructor, 'contract_declaration', 12); assign in source target order to contract.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/solidity.py:70-71
  if (the source predicate contract is None is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/solidity.py:71-71
    End this invocation with False.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/solidity.py:72-77
  for each child in contract.children {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/solidity.py:73-74
    if (the source predicate child.type != 'inheritance_specifier' is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/solidity.py:74-74
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/solidity.py:75-75
    In source order: Evaluate once child.child_by_field_name('ancestor') or child; assign in source target order to ancestor.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/solidity.py:76-77
    if (the source predicate _last_identifier(ancestor, source) == callee is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/solidity.py:77-77
      End this invocation with True.
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/solidity.py:78-78
  End this invocation with False.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/solidity.py:81-91
// Source signature: _last_identifier(node: Node, source: bytes) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _last_identifier(node, source) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/solidity.py:82-82
  In source order: Evaluate once ''; assign in source target order to result.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/solidity.py:84-88
  // Source signature: visit(current: Node, _depth: int) -> str | None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn visit(current, _depth) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/solidity.py:85-85
    In source order: Bind names in enclosing nonlocal scope: result.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/solidity.py:86-87
    if (the source predicate 'identifier' in current.type.lower() and current.child_count == 0 is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/solidity.py:87-87
      In source order: Evaluate once node_text(current, source); assign in source target order to result.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/solidity.py:88-88
    End this invocation with None.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/solidity.py:90-90
  In source order: Evaluate walk(node, visit); retain side effects and discard the expression result.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/solidity.py:91-91
  End this invocation with result.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/solidity.py:94-112
// Source signature: solidity_annotation_supplement(def_node: Node, source: bytes) -> tuple[str, ...]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn solidity_annotation_supplement(def_node, source) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/solidity.py:95-96
  In source order: Retain source documentation literal source_literal_95_4; it is not a model call. Then For names, assign []; source annotation list[str].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/solidity.py:98-107
  // Source signature: visit(node: Node, depth: int) -> str | None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn visit(node, depth) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/solidity.py:99-99
    In source order: Evaluate once node.type.lower(); assign in source target order to node_type.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/solidity.py:100-101
    if (the source predicate depth > 0 and node_type in ('function_body', 'block') is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/solidity.py:101-101
      End this invocation with 'skip'.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/solidity.py:102-103
    if (the source predicate node_type != 'modifier_invocation' is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/solidity.py:103-103
      End this invocation with None.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/solidity.py:104-104
    In source order: Evaluate once first_identifier_text(node, source); assign in source target order to name.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/solidity.py:105-106
    if (the source predicate name and is_valid_symbol_name(name) is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/solidity.py:106-106
      In source order: Evaluate names.append(name); retain side effects and discard the expression result.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/solidity.py:107-107
    End this invocation with 'skip'.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/solidity.py:109-109
  In source order: Evaluate walk(def_node, visit); retain side effects and discard the expression result.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/solidity.py:110-111
  if (the source predicate not names is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/solidity.py:111-111
    In source order: Evaluate once _modifier_names_from_signature(extract_signature(def_node, source)); assign in source target order to names.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/solidity.py:112-112
  End this invocation with tuple(dict.fromkeys(names)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/solidity.py:115-130
// Source signature: _modifier_names_from_signature(signature: str) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _modifier_names_from_signature(signature) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/solidity.py:116-117
  if (the source predicate not signature is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/solidity.py:117-117
    End this invocation with [].
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/solidity.py:118-118
  In source order: Evaluate once signature.find(')'); assign in source target order to closing.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/solidity.py:119-120
  if (the source predicate closing < 0 or closing + 1 >= len(signature) is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/solidity.py:120-120
    End this invocation with [].
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/solidity.py:121-123
  In source order: Evaluate once _RETURNS.sub(' ', signature[closing + 1:]); assign in source target order to tail. Then For names, assign []; source annotation list[str]. Then For seen, assign set(); source annotation set[str].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/solidity.py:124-129
  for each match in _MODIFIER_NAME.finditer(tail) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/solidity.py:125-125
    In source order: Evaluate once match.group(1); assign in source target order to name.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/solidity.py:126-127
    if (the source predicate name in seen or name in _NON_MODIFIER_TOKENS is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/solidity.py:127-127
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/solidity.py:128-129
    In source order: Evaluate seen.add(name); retain side effects and discard the expression result. Then Evaluate names.append(name); retain side effects and discard the expression result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/solidity.py:130-130
  End this invocation with names.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from context_graph_sdk.extractors.analysis import extract_signature, first_identifier_text, node_text, walk` at source line 23: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py.sudo.md`.
- `from context_graph_sdk.extractors.records import is_valid_symbol_name` at source line 29: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py.sudo.md`.
