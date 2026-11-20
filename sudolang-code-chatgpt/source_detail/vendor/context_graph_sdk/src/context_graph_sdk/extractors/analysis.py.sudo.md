# vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py.evidence.json`. SHA-256: `29cb619ebc3231ab01bf34c83d9709f922f0351bf1b40e8a6e92a6d97828434e`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:15-22
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import re; preserve alias and import-time effects. Then Resolve source import from collections.abc import Callable; preserve alias and import-time effects. Then Resolve source import from tree_sitter import Node; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:24-86
In source order: Evaluate once frozenset({'class_definition', 'class_declaration', 'class', 'class_specifier', 'struct_definition', 'struct_declaration', 'struct_item', 'struct_specifier', 'trait_definition', 'trait_item', 'impl_item', 'interface_declaration', 'object_declaration', 'enum_declaration', 'mixin_declaration', 'protocol_declaration', 'extension_declaration', 'companion_object', 'record_declaration', 'type_alias', 'contract_declaration', 'library_declaration'}); assign in source target order to CLASS_NODE_TYPES. Then Evaluate once frozenset({'comment', 'line_comment', 'block_comment', 'multiline_comment', 'documentation_comment', 'documentation_block_comment'}); assign in source target order to COMMENT_NODE_TYPES. Then Evaluate once frozenset({'decorator', 'decorated_definition', 'attribute', 'annotation'}); assign in source target order to DECORATOR_NODE_TYPES. Then Evaluate once frozenset({'decorator', 'decorated_definition', 'attribute', 'attribute_item', 'annotation', 'marker_annotation', 'modifiers'}); assign in source target order to ANNOTATION_CONTAINER_TYPES. Then Evaluate once frozenset({'type_identifier', 'identifier', 'constant', 'scoped_identifier', 'field_identifier', 'property_identifier', 'name'}); assign in source target order to ANNOTATION_NAME_TYPES.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:88-110
In source order: Evaluate once frozenset({'extends', 'implements', 'with', 'class', 'struct', 'interface', 'trait', 'mixin', 'super', 'public', 'private', 'protected', 'open', 'abstract', 'final', 'override', 'virtual'}); assign in source target order to _KEYWORDS. Then Evaluate once re.compile('<[^>]+>'); assign in source target order to _XML_TAG.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:113-119
// Source signature: node_text(node: Node | None, source: bytes) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn node_text(node, source) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:114-115
  if (the source predicate node is None is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:115-115
    End this invocation with ''.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:116-116
  In source order: Evaluate once (node.start_byte, node.end_byte); assign in source target order to (start, end).
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:117-118
  if (the source predicate start >= len(source) is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:118-118
    End this invocation with ''.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:119-119
  End this invocation with source[start:min(end, len(source))].decode('utf-8', errors='replace').
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:122-132
// Source signature: walk(root: Node, visit: Callable[[Node, int], str | None]) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn walk(root, visit) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:123-124
  In source order: Retain source documentation literal source_literal_123_4; it is not a model call. Then For stack, assign [(root, 0)]; source annotation list[tuple[Node, int]].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:125-132
  while (the source predicate stack is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:126-127
    In source order: Evaluate once stack.pop(); assign in source target order to (node, depth). Then Evaluate once visit(node, depth); assign in source target order to action.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:128-129
    if (the source predicate action == 'stop' is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:129-129
      End this invocation with None.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:130-131
    if (the source predicate action == 'skip' is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:131-131
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:132-132
    In source order: Evaluate stack.extend(((child, depth + 1) for child in reversed(node.children))); retain side effects and discard the expression result.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:135-143
// Source signature: has_ancestor_type(node: Node, ancestor_type: str, max_depth: int=20) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn has_ancestor_type(node, ancestor_type, max_depth) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:136-136
  In source order: Evaluate once node.parent; assign in source target order to current.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:137-142
  for each _ in range(max_depth) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:138-139
    if (the source predicate current is None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:139-139
      End this invocation with False.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:140-141
    if (the source predicate current.type == ancestor_type is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:141-141
      End this invocation with True.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:142-142
    In source order: Evaluate once current.parent; assign in source target order to current.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:143-143
  End this invocation with False.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:146-160
// Source signature: find_declaration_ancestor(node: Node) -> Node
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn find_declaration_ancestor(node) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:147-147
  In source order: For current, assign node; source annotation Node | None.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:148-159
  for each _ in range(10) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:149-150
    if (the source predicate current is None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:150-150
      Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:151-151
    In source order: Evaluate once current.type.lower(); assign in source target order to node_type.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:152-158
    if (the source predicate 'declaration' in node_type or 'definition' in node_type or '_item' in node_type or node_type.endswith('_statement') is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:158-158
      End this invocation with current.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:159-159
    In source order: Evaluate once current.parent; assign in source target order to current.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:160-160
  End this invocation with node.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:163-171
// Source signature: has_visibility_modifier(node: Node, source: bytes, *keywords: str) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn has_visibility_modifier(node, source, keywords) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:164-164
  In source order: Evaluate once find_declaration_ancestor(node); assign in source target order to declaration.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:165-170
  for each child in declaration.children {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:166-166
    In source order: Evaluate once child.type.lower(); assign in source target order to child_type.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:167-170
    if (the source predicate 'modifier' in child_type or 'visibility' in child_type is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:168-168
      In source order: Evaluate once node_text(child, source).lower(); assign in source target order to text.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:169-170
      if (the source predicate text and any((keyword in text for keyword in keywords)) is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:170-170
        End this invocation with True.
      }
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:171-171
  End this invocation with False.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:174-179
// Source signature: has_sibling_modifier(node: Node, source: bytes, keyword: str) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn has_sibling_modifier(node, source, keyword) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:175-175
  In source order: Evaluate once find_declaration_ancestor(node); assign in source target order to declaration.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:176-178
  for each child in declaration.children {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:177-178
    if (the source predicate child.type in ('modifiers', 'modifier') and keyword in node_text(child, source) is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:178-178
      End this invocation with True.
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:179-179
  End this invocation with False.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:182-184
// Source signature: has_sibling_node_type(node: Node, node_type: str) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn has_sibling_node_type(node, node_type) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:183-183
  In source order: Evaluate once find_declaration_ancestor(node); assign in source target order to declaration.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:184-184
  End this invocation with any((child.type == node_type for child in declaration.children)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:187-192
// Source signature: has_sibling_modifier_text(node: Node, source: bytes, node_type: str, text: str) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn has_sibling_modifier_text(node, source, node_type, text) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:188-188
  In source order: Evaluate once find_declaration_ancestor(node); assign in source target order to declaration.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:189-192
  End this invocation with any((child.type == node_type and node_text(child, source) == text for child in declaration.children)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:195-196
// Source signature: _access_modifier_is_bare(node: Node) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _access_modifier_is_bare(node) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:196-196
  End this invocation with all((child.type.lower() != 'access_qualifier' for child in node.children)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:199-220
// Source signature: has_scala_bare_visibility(node: Node, source: bytes) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn has_scala_bare_visibility(node, source) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:200-201
  In source order: Retain source documentation literal source_literal_200_4; it is not a model call. Then Evaluate once find_declaration_ancestor(node); assign in source target order to declaration.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:202-219
  for each child in declaration.children {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:203-203
    In source order: Evaluate once child.type.lower(); assign in source target order to child_type.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:204-207
    if (the source predicate child_type == 'access_modifier' is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:205-206
      if (the source predicate _access_modifier_is_bare(child) is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:206-206
        End this invocation with True.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:207-207
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:208-209
    if (the source predicate 'modifier' not in child_type and 'visibility' not in child_type is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:209-209
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:210-217
    for each modifier in child.children {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:211-211
      In source order: Evaluate once modifier.type.lower(); assign in source target order to modifier_type.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:212-215
      if (the source predicate modifier_type == 'access_modifier' is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:213-214
        if (the source predicate _access_modifier_is_bare(modifier) is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:214-214
          End this invocation with True.
        }
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:215-215
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:216-217
      if (the source predicate node_text(modifier, source).lower() in ('private', 'protected') is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:217-217
        End this invocation with True.
      }
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:218-219
    if (the source predicate node_text(child, source).strip().lower() in ('private', 'protected') is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:219-219
      End this invocation with True.
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:220-220
  End this invocation with False.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:223-235
// Source signature: first_identifier_text(node: Node, source: bytes) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn first_identifier_text(node, source) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:224-234
  for each child in node.children {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:225-234
    if (the source predicate child.type.lower() in ('identifier', 'simple_identifier', 'field_identifier', 'variable_name', 'name') is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:232-232
      In source order: Evaluate once node_text(child, source); assign in source target order to text.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:233-234
      if (the source predicate text is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:234-234
        End this invocation with text.
      }
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:235-235
  End this invocation with ''.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:238-249
// Source signature: extract_class_name(node: Node, source: bytes) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn extract_class_name(node, source) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:239-239
  In source order: Evaluate once node.child_by_field_name('name'); assign in source target order to name_node.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:240-241
  if (the source predicate name_node is not None is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:241-241
    End this invocation with node_text(name_node, source).
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:242-245
  if (the source predicate node.type.lower() == 'impl_item' is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:243-243
    In source order: Evaluate once node.child_by_field_name('type'); assign in source target order to type_node.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:244-245
    if (the source predicate type_node is not None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:245-245
      End this invocation with node_text(type_node, source).
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:246-248
  for each child in node.children {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:247-248
    if (the source predicate child.type.lower() in ('type_identifier', 'identifier', 'constant') is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:248-248
      End this invocation with node_text(child, source).
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:249-249
  End this invocation with ''.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:252-260
// Source signature: find_enclosing_class_name(node: Node, source: bytes) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn find_enclosing_class_name(node, source) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:253-253
  In source order: Evaluate once node.parent; assign in source target order to current.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:254-259
  for each _ in range(20) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:255-256
    if (the source predicate current is None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:256-256
      End this invocation with ''.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:257-258
    if (the source predicate current.type.lower() in CLASS_NODE_TYPES is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:258-258
      End this invocation with extract_class_name(current, source).
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:259-259
    In source order: Evaluate once current.parent; assign in source target order to current.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:260-260
  End this invocation with ''.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:263-279
// Source signature: extract_receiver_type(def_node: Node, source: bytes) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn extract_receiver_type(def_node, source) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:264-264
  In source order: Evaluate once def_node.child_by_field_name('receiver'); assign in source target order to receiver.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:265-266
  if (the source predicate receiver is None is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:266-266
    End this invocation with ''.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:267-267
  In source order: Evaluate once ''; assign in source target order to result.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:269-276
  // Source signature: visit(node: Node, _depth: int) -> str | None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn visit(node, _depth) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:270-270
    In source order: Bind names in enclosing nonlocal scope: result.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:271-272
    if (the source predicate result is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:272-272
      End this invocation with 'stop'.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:273-275
    if (the source predicate node.type.lower() == 'type_identifier' is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:274-274
      In source order: Evaluate once node_text(node, source); assign in source target order to result.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:275-275
      End this invocation with 'stop'.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:276-276
    End this invocation with None.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:278-278
  In source order: Evaluate walk(receiver, visit); retain side effects and discard the expression result.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:279-279
  End this invocation with result.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:282-283
In source order: Evaluate once ('body', 'block', 'function_body', 'compound_statement'); assign in source target order to _BODY_FIELDS. Then Evaluate once frozenset({'block', 'body', 'statement_block', 'compound_statement', 'function_body'}); assign in source target order to _BODY_TYPES.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:286-310
// Source signature: extract_signature(def_node: Node, source: bytes) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn extract_signature(def_node, source) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:287-288
  In source order: Evaluate once def_node.start_byte; assign in source target order to start. Then For body, assign None; source annotation Node | None.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:289-292
  for each field in _BODY_FIELDS {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:290-290
    In source order: Evaluate once def_node.child_by_field_name(field); assign in source target order to body.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:291-292
    if (the source predicate body is not None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:292-292
      Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:293-297
  if (the source predicate body is None is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:294-297
    for each child in def_node.children {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:295-297
      if (the source predicate child.type.lower() in _BODY_TYPES is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:296-296
        In source order: Evaluate once child; assign in source target order to body.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:297-297
        Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
      }
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:298-305
  if (the source predicate body is not None is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:299-299
    In source order: Evaluate once body.start_byte; assign in source target order to end.
  }
  else {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:301-303
    In source order: Evaluate once def_node.end_byte; assign in source target order to end. Then Evaluate once source[start:min(end, len(source))].decode('utf-8', errors='replace'); assign in source target order to text. Then Evaluate once text.find(source_literal_303_28); assign in source target order to newline.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:304-305
    if (the source predicate newline >= 0 is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:305-305
      In source order: Evaluate once start + len(text[:newline].encode()); assign in source target order to end.
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:306-307
  if (the source predicate start >= end or end > len(source) is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:307-307
    End this invocation with ''.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:308-309
  In source order: Evaluate once source[start:end].decode('utf-8', errors='replace').strip(); assign in source target order to signature. Then Evaluate once signature.rstrip(' \t{:'); assign in source target order to signature.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:310-310
  End this invocation with signature[:500].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:313-336
// Source signature: extract_method_signature(def_node: Node, source: bytes) -> tuple[int, str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn extract_method_signature(def_node, source) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:314-317
  In source order: Evaluate once 0; assign in source target order to parameter_count. Then Evaluate once def_node.child_by_field_name('parameters') or def_node.child_by_field_name('formal_parameters'); assign in source target order to params.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:318-327
  if (the source predicate params is None is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:319-327
    for each child in def_node.children {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:320-320
      In source order: Evaluate once child.type.lower(); assign in source target order to child_type.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:321-327
      if (the source predicate 'parameter' in child_type and 'list' in child_type or child_type in ('formal_parameters', 'parameter_list', 'function_parameters') is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:326-326
        In source order: Evaluate once child; assign in source target order to params.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:327-327
        Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
      }
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:328-329
  if (the source predicate params is not None is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:329-329
    In source order: Evaluate once sum((1 for child in params.children if child.is_named)); assign in source target order to parameter_count.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:330-335
  In source order: Evaluate once def_node.child_by_field_name('return_type') or def_node.child_by_field_name('result') or def_node.child_by_field_name('type'); assign in source target order to return_node. Then Evaluate once node_text(return_node, source).strip()[:80] if return_node else ''; assign in source target order to return_type.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:336-336
  End this invocation with (parameter_count, return_type).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:339-361
// Source signature: extract_doc_comment(def_node: Node, source: bytes, language: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn extract_doc_comment(def_node, source, language) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:340-343
  if (the source predicate language == 'python' is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:341-341
    In source order: Evaluate once _python_docstring(def_node, source); assign in source target order to docstring.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:342-343
    if (the source predicate docstring is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:343-343
      End this invocation with docstring.
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:344-345
  In source order: For lines, assign []; source annotation list[str]. Then Evaluate once def_node.prev_sibling; assign in source target order to sibling.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:346-357
  while (the source predicate sibling is not None is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:347-347
    In source order: Evaluate once sibling.type.lower(); assign in source target order to node_type.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:348-350
    if (the source predicate node_type in DECORATOR_NODE_TYPES is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:349-349
      In source order: Evaluate once sibling.prev_sibling; assign in source target order to sibling.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:350-350
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:351-352
    if (the source predicate node_type not in COMMENT_NODE_TYPES is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:352-352
      Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:353-353
    In source order: Evaluate once node_text(sibling, source); assign in source target order to text.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:354-355
    if (the source predicate text.strip().startswith('//!') is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:355-355
      Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:356-357
    In source order: Evaluate lines.append(text); retain side effects and discard the expression result. Then Evaluate once sibling.prev_sibling; assign in source target order to sibling.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:358-359
  if (the source predicate not lines is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:359-359
    End this invocation with ''.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:360-360
  In source order: Evaluate lines.reverse(); retain side effects and discard the expression result.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:361-361
  End this invocation with clean_doc_comment(source_literal_361_29.join(lines)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:364-381
// Source signature: _python_docstring(def_node: Node, source: bytes) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _python_docstring(def_node, source) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:365-365
  In source order: Evaluate once def_node.child_by_field_name('body'); assign in source target order to body.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:366-367
  if (the source predicate body is None or body.named_child_count == 0 is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:367-367
    End this invocation with ''.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:368-368
  In source order: Evaluate once body.named_child(0); assign in source target order to first.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:369-370
  if (the source predicate first is None is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:370-370
    End this invocation with ''.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:371-371
  In source order: Evaluate once first.type.lower(); assign in source target order to first_type.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:372-378
  if (the source predicate first_type == 'expression_statement' and first.named_child_count > 0 is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:373-373
    In source order: Evaluate once first.named_child(0); assign in source target order to string_node.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:374-378
    if (the source predicate string_node is not None and string_node.type.lower() in ('string', 'concatenated_string') is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:378-378
      End this invocation with clean_docstring(node_text(string_node, source)).
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:379-380
  if (the source predicate first_type in ('string', 'concatenated_string') is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:380-380
    End this invocation with clean_docstring(node_text(first, source)).
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:381-381
  End this invocation with ''.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:384-395
// Source signature: clean_doc_comment(raw: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn clean_doc_comment(raw) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:385-385
  In source order: For cleaned, assign []; source annotation list[str].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:386-393
  for each line in raw.split(source_literal_386_26) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:387-391
    In source order: Evaluate once line.strip(); assign in source target order to line. Then Evaluate once line.removeprefix('/*').removesuffix('*/'); assign in source target order to line. Then Evaluate once line.removeprefix('///').removeprefix('//!').removeprefix('//'); assign in source target order to line. Then Evaluate once line.removeprefix('#').removeprefix('*'); assign in source target order to line. Then Evaluate once line.strip(); assign in source target order to line.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:392-393
    if (the source predicate line is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:393-393
      In source order: Evaluate cleaned.append(line); retain side effects and discard the expression result.
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:394-394
  In source order: Evaluate once _XML_TAG.sub('', ' '.join(cleaned)); assign in source target order to result.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:395-395
  End this invocation with result[:1000].strip().
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:398-404
// Source signature: clean_docstring(raw: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn clean_docstring(raw) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:399-399
  In source order: Evaluate once raw.strip(); assign in source target order to text.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:400-401
  for each quote in ('"""', "'''") {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:401-401
    In source order: Evaluate once text.removeprefix(quote).removesuffix(quote); assign in source target order to text.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:402-403
  In source order: Evaluate once text.strip('"\''); assign in source target order to text. Then Evaluate once [line.strip() for line in text.split(source_literal_403_49) if line.strip()]; assign in source target order to lines.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:404-404
  End this invocation with ' '.join(lines)[:1000].strip().
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:407-408
// Source signature: is_keyword(text: str) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn is_keyword(text) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:408-408
  End this invocation with text.lower() in _KEYWORDS.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:411-435
// Source signature: extract_annotations(def_node: Node, source: bytes) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn extract_annotations(def_node, source) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:412-414
  In source order: Retain source documentation literal source_literal_412_4; it is not a model call. Then For names, assign []; source annotation list[str]. Then For seen, assign set(); source annotation set[str].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:416-419
  // Source signature: add(name: str) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn add(name) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:417-419
    if (the source predicate name and name not in seen is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:418-419
      In source order: Evaluate seen.add(name); retain side effects and discard the expression result. Then Evaluate names.append(name); retain side effects and discard the expression result.
    }
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:421-422
  for each name in _collect_direct_annotation_names(def_node, source) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:422-422
    In source order: Evaluate add(name); retain side effects and discard the expression result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:423-423
  In source order: Evaluate once def_node.prev_sibling; assign in source target order to sibling.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:424-433
  while (the source predicate sibling is not None is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:425-425
    In source order: Evaluate once sibling.type.lower(); assign in source target order to node_type.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:426-428
    if (the source predicate node_type in COMMENT_NODE_TYPES is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:427-427
      In source order: Evaluate once sibling.prev_sibling; assign in source target order to sibling.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:428-428
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:429-430
    if (the source predicate node_type not in ANNOTATION_CONTAINER_TYPES is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:430-430
      Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:431-432
    for each name in _collect_annotation_names(sibling, source) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:432-432
      In source order: Evaluate add(name); retain side effects and discard the expression result.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:433-433
    In source order: Evaluate once sibling.prev_sibling; assign in source target order to sibling.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:434-434
  In source order: Evaluate names.reverse(); retain side effects and discard the expression result.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:435-435
  End this invocation with ','.join(names).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:438-454
// Source signature: _collect_direct_annotation_names(node: Node, source: bytes) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _collect_direct_annotation_names(node, source) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:439-440
  In source order: For names, assign []; source annotation list[str]. Then For seen, assign set(); source annotation set[str].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:442-451
  // Source signature: collect_from(current: Node) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn collect_from(current) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:443-443
    In source order: Evaluate once current.type.lower(); assign in source target order to current_type.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:444-448
    if (the source predicate current_type in ANNOTATION_CONTAINER_TYPES is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:445-448
      for each name in _collect_annotation_names(current, source) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:446-448
        if (the source predicate name and name not in seen is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:447-448
          In source order: Evaluate seen.add(name); retain side effects and discard the expression result. Then Evaluate names.append(name); retain side effects and discard the expression result.
        }
      }
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:449-451
    for each child in current.children {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:450-451
      if (the source predicate child.is_named and child.type.lower() in ANNOTATION_CONTAINER_TYPES is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:451-451
        In source order: Evaluate collect_from(child); retain side effects and discard the expression result.
      }
    }
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:453-453
  In source order: Evaluate collect_from(node); retain side effects and discard the expression result.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:454-454
  End this invocation with names.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:457-461
// Source signature: _collect_annotation_names(node: Node, source: bytes) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _collect_annotation_names(node, source) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:460-460
  In source order: Evaluate once _annotation_carrier_name(node, source); assign in source target order to carrier.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:461-461
  End this invocation with [carrier] if carrier else [].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:464-487
// Source signature: _annotation_carrier_name(node: Node, source: bytes) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _annotation_carrier_name(node, source) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:465-465
  In source order: Evaluate once node.type.lower(); assign in source target order to node_type.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:466-471
  if (the source predicate node_type == 'decorator' is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:467-471
    for each child in node.children {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:468-471
      if (the source predicate child.is_named is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:469-469
        In source order: Evaluate once _decorator_target_name(child, source); assign in source target order to name.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:470-471
        if (the source predicate name is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:471-471
          End this invocation with name.
        }
      }
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:472-480
  if (the source predicate node_type in ('annotation', 'marker_annotation') is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:473-473
    In source order: Evaluate once node.child_by_field_name('name'); assign in source target order to name_node.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:474-475
    if (the source predicate name_node is not None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:475-475
      End this invocation with _annotation_name(name_node, source).
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:476-480
    for each child in node.children {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:477-480
      if (the source predicate child.is_named is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:478-478
        In source order: Evaluate once _annotation_name(child, source); assign in source target order to name.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:479-480
        if (the source predicate name is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:480-480
          End this invocation with name.
        }
      }
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:481-486
  if (the source predicate node_type in ('attribute_item', 'attribute') is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:482-486
    for each child in node.children {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:483-486
      if (the source predicate child.is_named is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:484-484
        In source order: Evaluate once _annotation_carrier_name(child, source) or _annotation_name(child, source); assign in source target order to name.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:485-486
        if (the source predicate name is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:486-486
          End this invocation with name.
        }
      }
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:487-487
  End this invocation with ''.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:490-510
// Source signature: _decorator_target_name(node: Node, source: bytes) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _decorator_target_name(node, source) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:491-491
  In source order: Evaluate once node.type.lower(); assign in source target order to node_type.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:492-493
  if (the source predicate node_type in ANNOTATION_NAME_TYPES is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:493-493
    End this invocation with _annotation_name(node, source).
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:494-497
  if (the source predicate node_type in ('call', 'call_expression') is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:495-495
    In source order: Evaluate once node.child_by_field_name('function'); assign in source target order to function.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:496-497
    if (the source predicate function is not None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:497-497
      End this invocation with _decorator_target_name(function, source).
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:498-504
  if (the source predicate node_type in ('attribute', 'member_expression', 'field_expression') is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:499-504
    for each field in ('attribute', 'field', 'property') {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:500-500
      In source order: Evaluate once node.child_by_field_name(field); assign in source target order to field_node.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:501-504
      if (the source predicate field_node is not None is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:502-502
        In source order: Evaluate once _annotation_name(field_node, source); assign in source target order to name.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:503-504
        if (the source predicate name is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:504-504
          End this invocation with name.
        }
      }
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:505-509
  for each child in node.children {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:506-509
    if (the source predicate child.is_named is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:507-507
      In source order: Evaluate once _decorator_target_name(child, source); assign in source target order to name.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:508-509
      if (the source predicate name is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:509-509
        End this invocation with name.
      }
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:510-510
  End this invocation with ''.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:513-530
// Source signature: _annotation_name(node: Node, source: bytes) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _annotation_name(node, source) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:514-515
  if (the source predicate node.type.lower() not in ANNOTATION_NAME_TYPES is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:515-515
    End this invocation with ''.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:516-516
  In source order: Evaluate once node_text(node, source).strip(); assign in source target order to text.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:517-518
  if (the source predicate not text is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:518-518
    End this invocation with ''.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:519-520
  In source order: Evaluate once text.lstrip('@#[]'); assign in source target order to text. Then Evaluate once max(text.rfind('.'), text.rfind(':'), text.rfind('\\'), text.rfind('/')); assign in source target order to separator.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:521-522
  if (the source predicate 0 <= separator < len(text) - 1 is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:522-522
    In source order: Evaluate once text[separator + 1:]; assign in source target order to text.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:523-526
  for each opener in '([{' {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:524-524
    In source order: Evaluate once text.find(opener); assign in source target order to index.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:525-526
    if (the source predicate index >= 0 is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:526-526
      In source order: Evaluate once text[:index]; assign in source target order to text.
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:527-527
  In source order: Evaluate once text.strip('`\'"]').strip(); assign in source target order to text.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:528-529
  if (the source predicate not text or is_keyword(text) is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:529-529
    End this invocation with ''.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py:530-530
  End this invocation with text.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

No statically resolved in-checkout import; external calls remain explicit dependency boundaries.
