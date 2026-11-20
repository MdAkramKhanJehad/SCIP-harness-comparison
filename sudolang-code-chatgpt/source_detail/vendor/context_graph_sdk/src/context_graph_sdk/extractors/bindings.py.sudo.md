# vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py.evidence.json`. SHA-256: `f8f90fec2d62d6a5a834e30dd9aaf4ceccb6d0acabfbc34a3647e852e4ccc8e0`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:15-32
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import re; preserve alias and import-time effects. Then Resolve source import from tree_sitter import Node; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.extractors.analysis import CLASS_NODE_TYPES, first_identifier_text, node_text, walk; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:33-70
In source order: Resolve source import from context_graph_sdk.extractors.records import TypeBinding; preserve alias and import-time effects. Then Evaluate once ('type', 'type_annotation', 'return_type', 'result'); assign in source target order to _TYPE_FIELDS. Then Evaluate once ('name', 'declarator', 'pattern', 'variable', 'left'); assign in source target order to _NAME_FIELDS. Then Evaluate once frozenset({'var_spec', 'short_var_declaration', 'const_spec', 'let_declaration', 'let_statement', 'val_declaration', 'val_statement', 'variable_declarator', 'variable_declaration', 'local_variable_declaration', 'property_declaration', 'pattern_binding', 'simple_pattern_binding', 'constant_declaration', 'assignment', 'const_declaration'}); assign in source target order to _VAR_DECL_TYPES. Then Evaluate once frozenset({'type_identifier', 'predefined_type', 'simple_type', 'primitive_type', 'builtin_type', 'generic_type', 'nullable_type', 'user_type'}); assign in source target order to _TYPE_CHILD_TYPES.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:72-109
In source order: Evaluate once frozenset({'extends', 'implements', 'with', 'where', 'when', 'throw', 'throws', 'catch', 'try', 'finally', 'switch', 'case', 'match', 'select', 'abstract', 'virtual', 'override', 'async', 'await', 'yield', 'package', 'module', 'namespace', 'do', 'in', 'is', 'not', 'and', 'or'}); assign in source target order to _NEVER_TYPE_KEYWORDS. Then Evaluate once re.compile('@returns?\\s+\\{([^}]+)\\}'); assign in source target order to _JSDOC_RETURN. Then Evaluate once re.compile('@param\\s+\\{([^}]+)\\}\\s+(\\w+)'); assign in source target order to _JSDOC_PARAM. Then Evaluate once re.compile('@type\\s+\\{([^}]+)\\}'); assign in source target order to _JSDOC_TYPE. Then Evaluate once re.compile('#\\s*type:\\s*(\\S+)'); assign in source target order to _PY_TYPE_COMMENT.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:111-124
In source order: Evaluate once frozenset({'comment', 'line_comment', 'block_comment'}); assign in source target order to _COMMENT_TYPES. Then Evaluate once frozenset({'assignment_expression', 'assignment_statement', 'assignment', 'short_var_declaration', 'variable_declarator', 'let_declaration', 'val_declaration', 'local_variable_declaration'}); assign in source target order to _ASSIGNMENT_TYPES.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:127-139
// Source signature: _is_var_decl_like(lower: str) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _is_var_decl_like(lower) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:128-129
  if (the source predicate lower in _VAR_DECL_TYPES is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:129-129
    End this invocation with True.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:130-131
  if (the source predicate 'var_' in lower or '_var' in lower is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:131-131
    End this invocation with True.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:132-139
  End this invocation with 'declaration' in lower and 'function' not in lower and ('class' not in lower) and ('method' not in lower) and ('import' not in lower) and ('type_' not in lower).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:142-145
// Source signature: _is_param_like(lower: str) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _is_param_like(lower) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:143-144
  if (the source predicate lower in ('parameter', 'formal_parameter', 'param') is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:144-144
    End this invocation with True.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:145-145
  End this invocation with lower.endswith('_parameter') or lower.startswith('parameter_').
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:148-149
// Source signature: is_type_keyword(text: str) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn is_type_keyword(text) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:149-149
  End this invocation with text.lower() in _NEVER_TYPE_KEYWORDS.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:152-153
// Source signature: is_type_name(text: str) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn is_type_name(text) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:153-153
  End this invocation with bool(text) and text[0].isupper() and (not is_type_keyword(text)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:156-172
// Source signature: clean_type_name(text: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn clean_type_name(text) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:157-157
  In source order: Evaluate once text.strip().removeprefix(':').strip(); assign in source target order to text.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:158-161
  for each opener in '<[' {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:159-159
    In source order: Evaluate once text.find(opener); assign in source target order to index.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:160-161
    if (the source predicate index > 0 is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:161-161
      In source order: Evaluate once text[:index]; assign in source target order to text.
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:162-163
  In source order: Evaluate once text.removesuffix('?').removeprefix('*').removeprefix('&'); assign in source target order to text. Then Evaluate once text.rfind('::'); assign in source target order to scope.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:164-165
  if (the source predicate scope >= 0 is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:165-165
    In source order: Evaluate once text[scope + 2:]; assign in source target order to text.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:166-166
  In source order: Evaluate once text.rfind('.'); assign in source target order to dot.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:167-168
  if (the source predicate dot >= 0 is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:168-168
    In source order: Evaluate once text[dot + 1:]; assign in source target order to text.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:169-169
  In source order: Evaluate once text.rfind('\\'); assign in source target order to backslash.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:170-171
  if (the source predicate backslash >= 0 is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:171-171
    In source order: Evaluate once text[backslash + 1:]; assign in source target order to text.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:172-172
  End this invocation with text.strip().
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:175-189
// Source signature: _find_type_in_children(node: Node, source: bytes) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _find_type_in_children(node, source) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:176-188
  for each child in node.children {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:177-178
    if (the source predicate not child.is_named is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:178-178
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:179-179
    In source order: Evaluate once child.type.lower(); assign in source target order to child_type.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:180-183
    if (the source predicate child_type in _TYPE_CHILD_TYPES is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:181-181
      In source order: Evaluate once clean_type_name(node_text(child, source)); assign in source target order to text.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:182-183
      if (the source predicate text is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:183-183
        End this invocation with text.
      }
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:184-188
    if (the source predicate 'type_annotation' in child_type or child_type == 'annotation' is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:185-186
      In source order: Evaluate once clean_type_name(node_text(child, source)); assign in source target order to text. Then Evaluate once text.removeprefix(':').strip(); assign in source target order to text.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:187-188
      if (the source predicate text is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:188-188
        End this invocation with text.
      }
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:189-189
  End this invocation with ''.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:192-215
// Source signature: find_type_annotation(node: Node, source: bytes) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn find_type_annotation(node, source) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:193-198
  for each field in _TYPE_FIELDS {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:194-194
    In source order: Evaluate once node.child_by_field_name(field); assign in source target order to child.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:195-198
    if (the source predicate child is not None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:196-196
      In source order: Evaluate once clean_type_name(node_text(child, source)); assign in source target order to text.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:197-198
      if (the source predicate text and (not is_type_keyword(text)) is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:198-198
        End this invocation with text.
      }
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:199-199
  In source order: Evaluate once _find_type_in_children(node, source); assign in source target order to text.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:200-201
  if (the source predicate text is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:201-201
    End this invocation with text.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:202-214
  for each child in node.children {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:203-204
    if (the source predicate not child.is_named is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:204-204
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:205-205
    In source order: Evaluate once child.type.lower(); assign in source target order to child_type.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:206-214
    if (the source predicate 'declaration' in child_type or 'binding' in child_type or 'pattern' in child_type or (child_type == 'type') is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:212-212
      In source order: Evaluate once _find_type_in_children(child, source); assign in source target order to text.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:213-214
      if (the source predicate text is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:214-214
        End this invocation with text.
      }
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:215-215
  End this invocation with ''.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:218-244
// Source signature: find_decl_name(node: Node, source: bytes) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn find_decl_name(node, source) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:219-232
  for each field in _NAME_FIELDS {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:220-220
    In source order: Evaluate once node.child_by_field_name(field); assign in source target order to child.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:221-222
    if (the source predicate child is None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:222-222
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:223-223
    In source order: Evaluate once child.type.lower(); assign in source target order to child_type.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:224-225
    if (the source predicate 'identifier' in child_type or child_type == 'name' is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:225-225
      End this invocation with node_text(child, source).
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:226-230
    if (the source predicate 'declarator' in child_type is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:227-227
      In source order: Evaluate once child.child_by_field_name('name'); assign in source target order to name_child.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:228-229
      if (the source predicate name_child is not None is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:229-229
        End this invocation with node_text(name_child, source).
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:230-230
      End this invocation with first_identifier_text(child, source).
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:231-232
    if (the source predicate 'expression_list' in child_type or 'pattern' in child_type is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:232-232
      End this invocation with first_identifier_text(child, source).
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:233-233
  In source order: Evaluate once first_identifier_text(node, source); assign in source target order to text.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:234-235
  if (the source predicate text is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:235-235
    End this invocation with text.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:236-243
  for each child in node.children {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:237-238
    if (the source predicate not child.is_named is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:238-238
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:239-239
    In source order: Evaluate once child.type.lower(); assign in source target order to child_type.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:240-243
    if (the source predicate 'declaration' in child_type or 'binding' in child_type or 'pattern' in child_type is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:241-241
      In source order: Evaluate once first_identifier_text(child, source); assign in source target order to text.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:242-243
      if (the source predicate text is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:243-243
        End this invocation with text.
      }
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:244-244
  End this invocation with ''.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:247-263
// Source signature: _find_owner_name(node: Node, source: bytes) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _find_owner_name(node, source) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:248-248
  In source order: Evaluate once node.parent; assign in source target order to current.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:249-262
  for each _ in range(20) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:250-251
    if (the source predicate current is None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:251-251
      End this invocation with ''.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:252-252
    In source order: Evaluate once current.type.lower(); assign in source target order to current_type.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:253-261
    if (the source predicate 'function' in current_type or 'method' in current_type or current_type in CLASS_NODE_TYPES is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:258-258
      In source order: Evaluate once current.child_by_field_name('name'); assign in source target order to name_node.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:259-260
      if (the source predicate name_node is not None is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:260-260
        End this invocation with node_text(name_node, source).
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:261-261
      End this invocation with first_identifier_text(current, source).
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:262-262
    In source order: Evaluate once current.parent; assign in source target order to current.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:263-263
  End this invocation with ''.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:266-276
// Source signature: _find_assignment_target(node: Node, source: bytes) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _find_assignment_target(node, source) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:267-275
  for each field in ('left', 'name', 'pattern', 'declarator') {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:268-268
    In source order: Evaluate once node.child_by_field_name(field); assign in source target order to child.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:269-270
    if (the source predicate child is None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:270-270
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:271-271
    In source order: Evaluate once child.type.lower(); assign in source target order to child_type.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:272-273
    if (the source predicate 'identifier' in child_type is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:273-273
      End this invocation with node_text(child, source).
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:274-275
    if (the source predicate 'declarator' in child_type or 'pattern' in child_type or 'expression_list' in child_type is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:275-275
      End this invocation with first_identifier_text(child, source).
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:276-276
  End this invocation with first_identifier_text(node, source).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:279-284
// Source signature: _unwrap_single_child(node: Node) -> Node
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _unwrap_single_child(node) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:280-283
  if (the source predicate node.type.lower() in ('expression_list', 'parenthesized_expression') is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:281-281
    In source order: Evaluate once [child for child in node.children if child.is_named]; assign in source target order to named.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:282-283
    if (the source predicate len(named) == 1 is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:283-283
      End this invocation with named[0].
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:284-284
  End this invocation with node.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:287-298
// Source signature: _find_assignment_value(node: Node) -> Node | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _find_assignment_value(node) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:288-291
  for each field in ('right', 'value', 'initializer') {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:289-289
    In source order: Evaluate once node.child_by_field_name(field); assign in source target order to child.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:290-291
    if (the source predicate child is not None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:291-291
      End this invocation with _unwrap_single_child(child).
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:292-297
  for each child in node.children {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:293-297
    if (the source predicate child.is_named and 'declarator' in child.type.lower() is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:294-297
      for each field in ('value', 'initializer', 'right') {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:295-295
        In source order: Evaluate once child.child_by_field_name(field); assign in source target order to value.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:296-297
        if (the source predicate value is not None is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:297-297
          End this invocation with _unwrap_single_child(value).
        }
      }
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:298-298
  End this invocation with None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:301-333
// Source signature: _constructor_type(node: Node, source: bytes) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _constructor_type(node, source) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:302-302
  In source order: Evaluate once node.type.lower(); assign in source target order to node_type.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:303-314
  if (the source predicate node_type in ('new_expression', 'object_creation_expression') is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:304-309
    for each field in ('type', 'constructor', 'class') {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:305-305
      In source order: Evaluate once node.child_by_field_name(field); assign in source target order to child.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:306-309
      if (the source predicate child is not None is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:307-307
        In source order: Evaluate once node_text(child, source); assign in source target order to text.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:308-309
        if (the source predicate text and is_type_name(text) is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:309-309
          End this invocation with clean_type_name(text).
        }
      }
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:310-314
    for each child in node.children {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:311-314
      if (the source predicate child.type.lower() in ('type_identifier', 'identifier') is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:312-312
        In source order: Evaluate once node_text(child, source); assign in source target order to text.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:313-314
        if (the source predicate text and is_type_name(text) is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:314-314
          End this invocation with clean_type_name(text).
        }
      }
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:315-328
  if (the source predicate 'call' in node_type is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:316-325
    for each field in ('function', 'callee', 'method') {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:317-317
      In source order: Evaluate once node.child_by_field_name(field); assign in source target order to child.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:318-319
      if (the source predicate child is None is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:319-319
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:320-321
      In source order: Evaluate once node_text(child, source); assign in source target order to text. Then Evaluate once text.find('::'); assign in source target order to scope.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:322-323
      if (the source predicate scope >= 0 is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:323-323
        In source order: Evaluate once text[:scope]; assign in source target order to text.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:324-325
      if (the source predicate text and is_type_name(text) is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:325-325
        End this invocation with clean_type_name(text).
      }
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:326-326
    In source order: Evaluate once first_identifier_text(node, source); assign in source target order to text.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:327-328
    if (the source predicate text and is_type_name(text) is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:328-328
      End this invocation with clean_type_name(text).
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:329-332
  if (the source predicate node_type == 'composite_literal' is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:330-330
    In source order: Evaluate once node.child_by_field_name('type'); assign in source target order to type_node.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:331-332
    if (the source predicate type_node is not None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:332-332
      End this invocation with clean_type_name(node_text(type_node, source)).
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:333-333
  End this invocation with ''.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:336-360
// Source signature: _comment_bindings(node: Node, source: bytes, relative_path: str) -> list[TypeBinding]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _comment_bindings(node, source, relative_path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:337-337
  In source order: Evaluate once node_text(node, source); assign in source target order to text.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:338-339
  if (the source predicate not text is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:339-339
    End this invocation with [].
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:340-341
  In source order: Evaluate once node.start_point.row; assign in source target order to line. Then For bindings, assign []; source annotation list[TypeBinding].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:342-345
  for each match in _JSDOC_RETURN.finditer(text) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:343-345
    In source order: Evaluate bindings.append(TypeBinding(relative_path, '@return', clean_type_name(match.group(1)), line, 'comment')); retain side effects and discard the expression result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:346-351
  for each match in _JSDOC_PARAM.finditer(text) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:347-351
    In source order: Evaluate bindings.append(TypeBinding(relative_path, match.group(2), clean_type_name(match.group(1)), line, 'comment')); retain side effects and discard the expression result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:352-355
  for each match in _JSDOC_TYPE.finditer(text) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:353-355
    In source order: Evaluate bindings.append(TypeBinding(relative_path, '@type', clean_type_name(match.group(1)), line, 'comment')); retain side effects and discard the expression result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:356-359
  for each match in _PY_TYPE_COMMENT.finditer(text) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:357-359
    In source order: Evaluate bindings.append(TypeBinding(relative_path, '@type', clean_type_name(match.group(1)), line, 'comment')); retain side effects and discard the expression result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:360-360
  End this invocation with bindings.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:363-427
// Source signature: extract_type_bindings(root: Node, source: bytes, relative_path: str) -> list[TypeBinding]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn extract_type_bindings(root, source, relative_path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:364-365
  In source order: For bindings, assign []; source annotation list[TypeBinding]. Then For seen, assign set(); source annotation set[tuple[str, str, int, str]].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:367-371
  // Source signature: add(binding: TypeBinding) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn add(binding) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:368-368
    In source order: Evaluate once (binding.variable_name, binding.type_name, binding.line, binding.kind); assign in source target order to key.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:369-371
    if (the source predicate key not in seen is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:370-371
      In source order: Evaluate seen.add(key); retain side effects and discard the expression result. Then Evaluate bindings.append(binding); retain side effects and discard the expression result.
    }
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:373-424
  // Source signature: visit(node: Node, _depth: int) -> str | None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn visit(node, _depth) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:374-374
    In source order: Evaluate once node.type.lower(); assign in source target order to lower.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:375-389
    if (the source predicate _is_var_decl_like(lower) is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:376-376
      In source order: Evaluate once find_type_annotation(node, source); assign in source target order to type_name.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:377-389
      if (the source predicate type_name is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:378-378
        In source order: Evaluate once find_decl_name(node, source); assign in source target order to variable.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:379-389
        if (the source predicate variable is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:380-389
          In source order: Evaluate add(TypeBinding(relative_path, variable, type_name, node.start_point.row, 'declaration', _find_owner_name(node, source))); retain side effects and discard the expression result.
        }
      }
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:390-404
    if (the source predicate _is_param_like(lower) is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:391-391
      In source order: Evaluate once find_type_annotation(node, source); assign in source target order to type_name.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:392-404
      if (the source predicate type_name is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:393-393
        In source order: Evaluate once find_decl_name(node, source); assign in source target order to parameter.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:394-404
        if (the source predicate parameter and parameter not in ('self', 'this', 'cls') is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:395-404
          In source order: Evaluate add(TypeBinding(relative_path, parameter, type_name, node.start_point.row, 'parameter', _find_owner_name(node, source))); retain side effects and discard the expression result.
        }
      }
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:405-420
    if (the source predicate lower in _ASSIGNMENT_TYPES and (not find_type_annotation(node, source)) is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:406-407
      In source order: Evaluate once _find_assignment_target(node, source); assign in source target order to variable. Then Evaluate once _find_assignment_value(node) if variable else None; assign in source target order to value.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:408-420
      if (the source predicate variable and value is not None is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:409-409
        In source order: Evaluate once _constructor_type(value, source); assign in source target order to type_name.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:410-420
        if (the source predicate type_name is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:411-420
          In source order: Evaluate add(TypeBinding(relative_path, variable, type_name, node.start_point.row, 'constructor', _find_owner_name(node, source))); retain side effects and discard the expression result.
        }
      }
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:421-423
    if (the source predicate lower in _COMMENT_TYPES is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:422-423
      for each binding in _comment_bindings(node, source, relative_path) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:423-423
        In source order: Evaluate add(binding); retain side effects and discard the expression result.
      }
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:424-424
    End this invocation with None.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:426-426
  In source order: Evaluate walk(root, visit); retain side effects and discard the expression result.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:427-427
  End this invocation with _propagate_chains(bindings, root, source, relative_path).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:430-470
// Source signature: _propagate_chains(bindings: list[TypeBinding], root: Node, source: bytes, relative_path: str) -> list[TypeBinding]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _propagate_chains(bindings, root, source, relative_path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:433-433
  In source order: For type_map, assign {}; source annotation dict[tuple[str, str], str].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:434-435
  for each binding in bindings {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:435-435
    In source order: Evaluate type_map.setdefault((binding.owner_name, binding.variable_name), binding.type_name); retain side effects and discard the expression result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:437-437
  In source order: For assigns, assign []; source annotation list[tuple[str, str, str, int]].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:439-454
  // Source signature: visit(node: Node, _depth: int) -> str | None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn visit(node, _depth) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:440-441
    if (the source predicate node.type.lower() not in _ASSIGNMENT_TYPES is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:441-441
      End this invocation with None.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:442-442
    In source order: Evaluate once _find_assignment_target(node, source); assign in source target order to target.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:443-444
    if (the source predicate not target is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:444-444
      End this invocation with None.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:445-445
    In source order: Evaluate once _find_assignment_value(node); assign in source target order to value.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:446-447
    if (the source predicate value is None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:447-447
      End this invocation with None.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:448-453
    if (the source predicate 'identifier' in value.type.lower() and value.child_count == 0 is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:449-449
      In source order: Evaluate once node_text(value, source); assign in source target order to source_name.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:450-453
      if (the source predicate source_name and source_name != target is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:451-453
        In source order: Evaluate assigns.append((target, source_name, _find_owner_name(node, source), node.start_point.row)); retain side effects and discard the expression result.
      }
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:454-454
    End this invocation with None.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:456-456
  In source order: Evaluate walk(root, visit); retain side effects and discard the expression result.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:458-469
  for each _ in range(10) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:459-459
    In source order: Evaluate once False; assign in source target order to changed.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:460-467
    for each (target, source_name, owner, line) in assigns {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:461-461
      In source order: Evaluate once type_map.get((owner, source_name)); assign in source target order to source_type.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:462-467
      if (the source predicate source_type is not None and (owner, target) not in type_map is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:463-467
        In source order: Evaluate once source_type; assign in source target order to type_map[owner, target]. Then Evaluate bindings.append(TypeBinding(relative_path, target, source_type, line, 'chain', owner)); retain side effects and discard the expression result. Then Evaluate once True; assign in source target order to changed.
      }
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:468-469
    if (the source predicate not changed is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:469-469
      Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py:470-470
  End this invocation with bindings.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from context_graph_sdk.extractors.analysis import CLASS_NODE_TYPES, first_identifier_text, node_text, walk` at source line 27: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py.sudo.md`.
- `from context_graph_sdk.extractors.records import TypeBinding` at source line 33: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py.sudo.md`.
