# vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py.evidence.json`. SHA-256: `49ef60afaada45f3dd2f2a988b7f8ec16e878b1f6ce4ec83450ef672867119f7`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py:15-33
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from tree_sitter import Node; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.extractors.analysis import node_text, walk; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.extractors.records import Call, Heritage, Import, MutableFileResult, Symbol, symbol_id; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py:35-37
In source order: Evaluate once ('require', 'require_relative'); assign in source target order to _REQUIRES. Then Evaluate once ('include', 'extend', 'prepend'); assign in source target order to _MIXINS. Then Evaluate once ('attr_accessor', 'attr_reader', 'attr_writer'); assign in source target order to _ATTRIBUTES.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py:40-74
interface _CallIndex {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py:41-41
  In source order: Retain source documentation literal source_literal_41_4; it is not a model call.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py:43-51
  // Source signature: __init__(self, root: Node) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self, root) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py:44-44
    In source order: For self.by_line, assign {}; source annotation dict[int, list[Node]].
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py:46-49
    // Source signature: visit(node: Node, _depth: int) -> str | None
    Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
    fn visit(node, _depth) {
      Bind arguments/defaults/annotations exactly as the source signature specifies.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py:47-48
      if (the source predicate node.type == 'call' is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py:48-48
        In source order: Evaluate self.by_line.setdefault(node.start_point.row, []).append(node); retain side effects and discard the expression result.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py:49-49
      End this invocation with None.
      If execution reaches this end, finish with the source implicit None result.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py:51-51
    In source order: Evaluate walk(root, visit); retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py:53-58
  // Source signature: matching(self, source: bytes, line: int, method_name: str) -> Node | None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn matching(self, source, line, method_name) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py:54-57
    for each node in self.by_line.get(line, []) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py:55-55
      In source order: Evaluate once node.child_by_field_name('method'); assign in source target order to method.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py:56-57
      if (the source predicate method is not None and node_text(method, source) == method_name is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py:57-57
        End this invocation with node.
      }
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py:58-58
    End this invocation with None.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py:60-74
  // Source signature: enclosing_class(self, source: bytes, line: int) -> str
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn enclosing_class(self, source, line) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py:62-62
    In source order: Evaluate once self.by_line.get(line, []); assign in source target order to nodes.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py:63-64
    if (the source predicate not nodes is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py:64-64
      End this invocation with ''.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py:65-65
    In source order: Evaluate once nodes[0].parent; assign in source target order to current.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py:66-73
    for each _ in range(20) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py:67-68
      if (the source predicate current is None is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py:68-68
        End this invocation with ''.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py:69-72
      if (the source predicate current.type in ('class', 'module') is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py:70-70
        In source order: Evaluate once current.child_by_field_name('name'); assign in source target order to name_node.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py:71-72
        if (the source predicate name_node is not None is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py:72-72
          End this invocation with node_text(name_node, source).
        }
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py:73-73
      In source order: Evaluate once current.parent; assign in source target order to current.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py:74-74
    End this invocation with ''.
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py:77-114
// Source signature: route_ruby_calls(root: Node, source: bytes, relative_path: str, language: str, result: MutableFileResult) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn route_ruby_calls(root, source, relative_path, language, result) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py:80-81
  In source order: Evaluate once _CallIndex(root); assign in source target order to index. Then For remaining, assign []; source annotation list[Call].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py:82-113
  for each call in result.calls {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py:83-89
    if (the source predicate call.callee_name in _REQUIRES is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py:84-84
      In source order: Evaluate once _call_argument(index, source, call.line, call.callee_name); assign in source target order to import_path.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py:85-88
      if (the source predicate import_path is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py:86-87
        if (the source predicate call.callee_name == 'require_relative' and (not import_path.startswith('.')) is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py:87-87
          In source order: Evaluate once './' + import_path; assign in source target order to import_path.
        }
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py:88-88
        In source order: Evaluate result.imports.append(Import(relative_path, import_path)); retain side effects and discard the expression result.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py:89-89
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py:90-95
    if (the source predicate call.callee_name in _MIXINS is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py:91-92
      In source order: Evaluate once _call_argument(index, source, call.line, call.callee_name); assign in source target order to mixin. Then Evaluate once index.enclosing_class(source, call.line); assign in source target order to owner.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py:93-94
      if (the source predicate mixin and owner is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py:94-94
        In source order: Evaluate result.heritage.append(Heritage(relative_path, owner, mixin, 'trait')); retain side effects and discard the expression result.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py:95-95
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py:96-112
    if (the source predicate call.callee_name in _ATTRIBUTES is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py:97-97
      In source order: Evaluate once index.enclosing_class(source, call.line); assign in source target order to owner.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py:98-111
      for each property_name in _attribute_arguments(index, source, call.line, call.callee_name) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py:99-111
        In source order: Evaluate result.symbols.append(Symbol(id=symbol_id('Property', relative_path, property_name, owner), name=property_name, label='Property', file_path=relative_path, start_line=call.line, end_line=call.line, is_exported=False, language=language, owner_name=owner)); retain side effects and discard the expression result.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py:112-112
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py:113-113
    In source order: Evaluate remaining.append(call); retain side effects and discard the expression result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py:114-114
  In source order: Evaluate once remaining; assign in source target order to result.calls.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py:117-131
// Source signature: _call_argument(index: _CallIndex, source: bytes, line: int, method_name: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _call_argument(index, source, line, method_name) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py:118-118
  In source order: Evaluate once index.matching(source, line, method_name); assign in source target order to call.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py:119-120
  if (the source predicate call is None is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py:120-120
    End this invocation with ''.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py:121-121
  In source order: Evaluate once call.child_by_field_name('arguments'); assign in source target order to arguments.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py:122-123
  if (the source predicate arguments is None is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py:123-123
    End this invocation with ''.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py:124-130
  for each child in arguments.children {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py:125-128
    if (the source predicate child.type == 'string' is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py:126-128
      for each grandchild in child.children {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py:127-128
        if (the source predicate grandchild.type == 'string_content' is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py:128-128
          End this invocation with node_text(grandchild, source).
        }
      }
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py:129-130
    if (the source predicate child.type in ('constant', 'scope_resolution') is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py:130-130
      End this invocation with node_text(child, source).
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py:131-131
  End this invocation with ''.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py:134-149
// Source signature: _attribute_arguments(index: _CallIndex, source: bytes, line: int, method_name: str) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _attribute_arguments(index, source, line, method_name) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py:137-137
  In source order: Evaluate once index.matching(source, line, method_name); assign in source target order to call.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py:138-139
  if (the source predicate call is None is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py:139-139
    End this invocation with [].
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py:140-140
  In source order: Evaluate once call.child_by_field_name('arguments'); assign in source target order to arguments.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py:141-142
  if (the source predicate arguments is None is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py:142-142
    End this invocation with [].
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py:143-143
  In source order: For names, assign []; source annotation list[str].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py:144-148
  for each child in arguments.children {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py:145-148
    if (the source predicate child.type == 'simple_symbol' is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py:146-146
      In source order: Evaluate once node_text(child, source).removeprefix(':'); assign in source target order to text.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py:147-148
      if (the source predicate text is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py:148-148
        In source order: Evaluate names.append(text); retain side effects and discard the expression result.
      }
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/languages/ruby.py:149-149
  End this invocation with names.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from context_graph_sdk.extractors.analysis import node_text, walk` at source line 25: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py.sudo.md`.
- `from context_graph_sdk.extractors.records import Call, Heritage, Import, MutableFileResult, Symbol, symbol_id` at source line 26: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py.sudo.md`.
