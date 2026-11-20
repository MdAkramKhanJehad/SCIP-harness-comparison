# vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/jvm.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/jvm.py.evidence.json`. SHA-256: `8bba6220b55c285dad6ff149d83e37aba527d874b343acc81fb47724093ba584`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/jvm.py:15-23
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from dataclasses import replace; preserve alias and import-time effects. Then Resolve source import from tree_sitter import Node; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.extractors.analysis import node_text, walk; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/jvm.py:24-32
In source order: Resolve source import from context_graph_sdk.extractors.records import Call, MutableFileResult, Symbol, is_valid_symbol_name, symbol_id; preserve alias and import-time effects. Then Evaluate once ('type_identifier', 'identifier', 'simple_identifier'); assign in source target order to _NAME_FALLBACK_TYPES.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/jvm.py:35-42
// Source signature: _class_like_name(node: Node, source: bytes) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _class_like_name(node, source) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/jvm.py:36-36
  In source order: Evaluate once node.child_by_field_name('name'); assign in source target order to name_node.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/jvm.py:37-38
  if (the source predicate name_node is not None is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/jvm.py:38-38
    End this invocation with node_text(name_node, source).
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/jvm.py:39-41
  for each child in node.children {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/jvm.py:40-41
    if (the source predicate child.type.lower() in _NAME_FALLBACK_TYPES is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/jvm.py:41-41
      End this invocation with node_text(child, source).
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/jvm.py:42-42
  End this invocation with ''.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/jvm.py:45-72
// Source signature: reclassify_interface_declarations(root: Node, source: bytes, relative_path: str, _language: str, result: MutableFileResult) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn reclassify_interface_declarations(root, source, relative_path, _language, result) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/jvm.py:48-50
  In source order: Retain source documentation literal source_literal_48_4; it is not a model call. Then For interface_names, assign set(); source annotation set[str].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/jvm.py:52-63
  // Source signature: visit(node: Node, _depth: int) -> str | None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn visit(node, _depth) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/jvm.py:53-54
    if (the source predicate 'class_declaration' not in node.type.lower() is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/jvm.py:54-54
      End this invocation with None.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/jvm.py:55-58
    In source order: Evaluate once any((not child.is_named and node_text(child, source) == 'interface' for child in node.children)); assign in source target order to keyword.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/jvm.py:59-62
    if (the source predicate keyword is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/jvm.py:60-60
      In source order: Evaluate once _class_like_name(node, source); assign in source target order to name.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/jvm.py:61-62
      if (the source predicate name is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/jvm.py:62-62
        In source order: Evaluate interface_names.add(name); retain side effects and discard the expression result.
      }
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/jvm.py:63-63
    End this invocation with None.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/jvm.py:65-65
  In source order: Evaluate walk(root, visit); retain side effects and discard the expression result.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/jvm.py:66-72
  for each (index, symbol) in enumerate(result.symbols) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/jvm.py:67-72
    if (the source predicate symbol.label == 'Class' and symbol.name in interface_names is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/jvm.py:68-72
      In source order: Evaluate once replace(symbol, label='Interface', id=symbol_id('Interface', relative_path, symbol.name, '')); assign in source target order to result.symbols[index].
    }
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/jvm.py:75-96
// Source signature: extract_infix_calls(root: Node, source: bytes, relative_path: str, _language: str, result: MutableFileResult) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn extract_infix_calls(root, source, relative_path, _language, result) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/jvm.py:78-78
  In source order: Retain source documentation literal source_literal_78_4; it is not a model call.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/jvm.py:80-94
  // Source signature: visit(node: Node, _depth: int) -> str | None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn visit(node, _depth) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/jvm.py:81-82
    if (the source predicate node.type.lower() not in ('infix_expression', 'infix_call') is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/jvm.py:82-82
      End this invocation with None.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/jvm.py:83-84
    if (the source predicate node.child_count < 3 is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/jvm.py:84-84
      End this invocation with None.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/jvm.py:85-93
    for each index in range(1, node.child_count - 1) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/jvm.py:86-86
      In source order: Evaluate once node.child(index); assign in source target order to child.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/jvm.py:87-93
      if (the source predicate child is not None and 'identifier' in child.type.lower() is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/jvm.py:88-88
        In source order: Evaluate once node_text(child, source); assign in source target order to callee.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/jvm.py:91-92
        if (the source predicate callee and is_valid_symbol_name(callee) and (not _is_operator_noise(callee)) is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/jvm.py:92-92
          In source order: Evaluate result.calls.append(Call(relative_path, callee, '', node.start_point.row)); retain side effects and discard the expression result.
        }
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/jvm.py:93-93
        Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
      }
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/jvm.py:94-94
    End this invocation with None.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/jvm.py:96-96
  In source order: Evaluate walk(root, visit); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/jvm.py:99-102
// Source signature: _is_operator_noise(callee: str) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _is_operator_noise(callee) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/jvm.py:102-102
  End this invocation with all((char in '-.:@$' for char in callee)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/jvm.py:105-158
// Source signature: extract_primary_constructor_params(root: Node, source: bytes, relative_path: str, language: str, result: MutableFileResult) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn extract_primary_constructor_params(root, source, relative_path, language, result) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/jvm.py:108-116
  In source order: Retain source documentation literal source_literal_108_4; it is not a model call. Then Evaluate once {symbol.name for symbol in result.symbols if symbol.label in ('Class', 'Struct', 'Record')}; assign in source target order to class_names. Then Evaluate once {symbol.owner_name for symbol in result.symbols if symbol.label == 'Constructor'}; assign in source target order to owners_with_constructor. Then For additions, assign []; source annotation list[Symbol].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/jvm.py:118-155
  // Source signature: visit(node: Node, _depth: int) -> str | None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn visit(node, _depth) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/jvm.py:119-119
    In source order: Evaluate once node.type.lower(); assign in source target order to node_type.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/jvm.py:120-121
    if (the source predicate 'class' not in node_type and 'record' not in node_type is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/jvm.py:121-121
      End this invocation with None.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/jvm.py:122-122
    In source order: Evaluate once _class_like_name(node, source); assign in source target order to class_name.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/jvm.py:123-124
    if (the source predicate not class_name or class_name not in class_names is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/jvm.py:124-124
      End this invocation with None.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/jvm.py:125-125
    In source order: For parameter_list, assign None; source annotation Node | None.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/jvm.py:126-129
    for each child in node.children {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/jvm.py:127-129
      if (the source predicate child.is_named and child.type.lower() in ('parameter_list', 'primary_constructor') is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/jvm.py:128-128
        In source order: Evaluate once child; assign in source target order to parameter_list.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/jvm.py:129-129
        Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
      }
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/jvm.py:130-131
    if (the source predicate parameter_list is None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/jvm.py:131-131
      End this invocation with None.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/jvm.py:132-136
    In source order: Evaluate once sum((1 for child in parameter_list.children if child.is_named and 'parameter' in child.type.lower())); assign in source target order to parameter_count.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/jvm.py:137-138
    if (the source predicate parameter_count == 0 or class_name in owners_with_constructor is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/jvm.py:138-138
      End this invocation with None.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/jvm.py:139-154
    In source order: Evaluate owners_with_constructor.add(class_name); retain side effects and discard the expression result. Then Evaluate additions.append(Symbol(id=symbol_id('Constructor', relative_path, class_name, class_name), name=class_name, label='Constructor', file_path=relative_path, start_line=parameter_list.start_point.row, end_line=parameter_list.end_point.row, is_exported=True, language=language, content=node_text(parameter_list, source), owner_name=class_name, parameter_count=parameter_count)); retain side effects and discard the expression result.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/jvm.py:155-155
    End this invocation with None.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/jvm.py:157-158
  In source order: Evaluate walk(root, visit); retain side effects and discard the expression result. Then Evaluate result.symbols.extend(additions); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from context_graph_sdk.extractors.analysis import node_text, walk` at source line 23: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py.sudo.md`.
- `from context_graph_sdk.extractors.records import Call, MutableFileResult, Symbol, is_valid_symbol_name, symbol_id` at source line 24: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py.sudo.md`.
