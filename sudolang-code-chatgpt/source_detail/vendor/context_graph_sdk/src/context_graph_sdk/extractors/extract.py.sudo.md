# vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py.evidence.json`. SHA-256: `d3c6af08b1fd913730e20fc0771ea2a094f1261448e7861847152ebbcdd6518f`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:15-38
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from tree_sitter import Node; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.extractors import runtime; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.extractors.analysis import extract_annotations, extract_class_name, extract_doc_comment, extract_method_signature, extract_receiver_type, extract_signature, find_enclosing_class_name, first_identifier_text, node_text, walk; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:39-86
In source order: Resolve source import from context_graph_sdk.extractors.bindings import extract_type_bindings; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.extractors.descriptors import LANGUAGE_DESCRIPTORS, LanguageDescriptor; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.extractors.records import CALLABLE_LABELS, OWNERLESS_LABELS, Assignment, Call, Delegate, FileExtraction, Heritage, Import, ImportBinding, MutableFileResult, Spawn, Symbol, deduplicate_symbols, disambiguate_duplicate_ids, is_valid_symbol_name, symbol_id; preserve alias and import-time effects. Then For _DEFINITION_LABELS, assign (('definition.function', 'Function'), ('definition.class', 'Class'), ('definition.interface', 'Interface'), ('definition.method', 'Method'), ('definition.struct', 'Struct'), ('definition.enum', 'Enum'), ('definition.namespace', 'Namespace'), ('definition.module', 'Module'), ('definition.trait', 'Trait'), ('definition.impl', 'Impl'), ('definition.const', 'Const'), ('definition.static', 'Static'), ('definition.typedef', 'Typedef'), ('definition.macro', 'Macro'), ('definition.union', 'Union'), ('definition.property', 'Property'), ('definition.record', 'Record'), ('definition.delegate', 'Delegate'), ('definition.annotation', 'Annotation'), ('definition.constructor', 'Constructor'), ('definition.template', 'Template'), ('definition.constant', 'Const'), ('definition.variable', 'Variable')); source annotation tuple[tuple[str, str], ...]. Then Evaluate once {'definition.event': 'event', 'definition.error': 'error'}; assign in source target order to _KIND_CAPTURES.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:89-99
// Source signature: _classify(captures: dict[str, list[Node]]) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _classify(captures) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:90-90
  In source order: Evaluate once ''; assign in source target order to fallback.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:91-93
  for each (capture, label) in _DEFINITION_LABELS {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:92-93
    if (the source predicate capture in captures is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:93-93
      End this invocation with label.
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:94-96
  for each capture in _KIND_CAPTURES {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:95-96
    if (the source predicate capture in captures is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:96-96
      End this invocation with 'CodeElement'.
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:97-98
  if (the source predicate 'definition.type' in captures is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:98-98
    In source order: Evaluate once 'TypeAlias'; assign in source target order to fallback.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:99-99
  End this invocation with fallback.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:102-106
// Source signature: _classify_kind(captures: dict[str, list[Node]]) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _classify_kind(captures) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:103-105
  for each (capture, kind) in _KIND_CAPTURES.items() {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:104-105
    if (the source predicate capture in captures is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:105-105
      End this invocation with kind.
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:106-106
  End this invocation with ''.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:109-120
// Source signature: _definition_node(captures: dict[str, list[Node]]) -> Node | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _definition_node(captures) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:110-112
  for each (name, nodes) in captures.items() {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:111-112
    if (the source predicate name.startswith('definition.') and nodes is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:112-112
      End this invocation with nodes[-1].
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:113-116
  for each name in ('heritage', 'name') {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:114-114
    In source order: Evaluate once captures.get(name); assign in source target order to nodes.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:115-116
    if (the source predicate nodes is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:116-116
      End this invocation with nodes[-1].
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:117-119
  for each nodes in captures.values() {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:118-119
    if (the source predicate nodes is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:119-119
      End this invocation with nodes[-1].
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:120-120
  End this invocation with None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:123-127
// Source signature: _trim_quotes(text: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _trim_quotes(text) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:124-124
  In source order: Evaluate once text.strip(); assign in source target order to text.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:125-126
  if (the source predicate len(text) >= 2 and text[0] == text[-1] and (text[0] in '"\'`') is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:126-126
    End this invocation with text[1:-1].
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:127-127
  End this invocation with text.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:130-293
// Source signature: extract_file(relative_path: str, source: bytes, language: str) -> FileExtraction
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn extract_file(relative_path, source, language) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:131-134
  In source order: Retain source documentation literal source_literal_131_4; it is not a model call. Then Evaluate once LANGUAGE_DESCRIPTORS[language]; assign in source target order to descriptor. Then Evaluate once runtime.parse_and_match(language, source); assign in source target order to (tree, matches). Then Evaluate once MutableFileResult(); assign in source target order to result.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:136-280
  for each (_, captures) in matches {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:137-140
    In source order: Evaluate once {name: [node_text(node, source) for node in nodes] for name, nodes in captures.items()}; assign in source target order to texts. Then Evaluate once {name: values[-1] if values else '' for name, values in texts.items()}; assign in source target order to last.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:142-150
    if (the source predicate 'import' in captures is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:143-143
      In source order: Evaluate once texts.get('import.alias', []); assign in source target order to aliases.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:144-149
      for each (index, import_source) in enumerate(texts.get('import.source', [])) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:145-146
        In source order: For bindings, assign (); source annotation tuple[ImportBinding, ...]. Then Evaluate once _trim_quotes(import_source); assign in source target order to cleaned.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:147-148
        if (the source predicate index < len(aliases) and aliases[index] is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:148-148
          In source order: Evaluate once (ImportBinding(cleaned, aliases[index]),); assign in source target order to bindings.
        }
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:149-149
        In source order: Evaluate result.imports.append(Import(relative_path, cleaned, bindings)); retain side effects and discard the expression result.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:150-150
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:152-163
    if (the source predicate 'spawn' in captures is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:153-153
      In source order: Evaluate once last.get('spawn.name', '') or last.get('spawn.target', ''); assign in source target order to target.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:154-162
      if (the source predicate target and is_valid_symbol_name(target) is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:155-162
        In source order: Evaluate result.spawns.append(Spawn(relative_path, target, last.get('spawn.receiver', ''), captures['spawn'][-1].start_point.row)); retain side effects and discard the expression result.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:163-163
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:165-176
    if (the source predicate 'delegate' in captures is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:166-166
      In source order: Evaluate once last.get('delegate.target', ''); assign in source target order to target.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:167-175
      if (the source predicate target and is_valid_symbol_name(target) is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:168-175
        In source order: Evaluate result.delegates.append(Delegate(relative_path, target, last.get('delegate.receiver', ''), captures['delegate'][-1].start_point.row)); retain side effects and discard the expression result.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:176-176
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:178-197
    if (the source predicate 'call' in captures is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:179-181
      In source order: Evaluate once texts.get('call.name', []); assign in source target order to names. Then Evaluate once captures.get('call.name', []); assign in source target order to nodes. Then Evaluate once last.get('call.receiver', ''); assign in source target order to receiver.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:182-196
      for each (index, callee) in enumerate(names) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:183-188
        if (the source predicate not is_valid_symbol_name(callee) is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:184-185
          if (the source predicate index >= len(nodes) is truthy) {
            // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:185-185
            Continue the immediately enclosing source loop at its next iteration.
          }
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:186-186
          In source order: Evaluate once first_identifier_text(nodes[index], source); assign in source target order to callee.
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:187-188
          if (the source predicate not is_valid_symbol_name(callee) is truthy) {
            // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:188-188
            Continue the immediately enclosing source loop at its next iteration.
          }
        }
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:189-194
        if (the source predicate descriptor.include_call is not None and index < len(nodes) and (not descriptor.include_call(callee, nodes[index], source)) is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:194-194
          Continue the immediately enclosing source loop at its next iteration.
        }
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:195-196
        In source order: Evaluate once nodes[index].start_point.row if index < len(nodes) else 0; assign in source target order to line. Then Evaluate result.calls.append(Call(relative_path, callee, receiver, line)); retain side effects and discard the expression result.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:197-197
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:199-212
    if (the source predicate 'assignment' in captures is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:200-200
      In source order: Evaluate once last.get('assignment.property', ''); assign in source target order to property_name.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:201-211
      if (the source predicate property_name is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:202-211
        In source order: Evaluate once captures.get('assignment.property', []); assign in source target order to property_nodes. Then Evaluate once property_nodes[-1].start_point.row if property_nodes else 0; assign in source target order to line. Then Evaluate result.assignments.append(Assignment(relative_path, last.get('assignment.receiver', ''), property_name, line)); retain side effects and discard the expression result.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:212-212
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:214-229
    if (the source predicate 'heritage' in captures or 'heritage.impl' in captures is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:215-215
      In source order: Evaluate once last.get('heritage.class', ''); assign in source target order to class_name.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:216-226
      if (the source predicate class_name is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:217-226
        for each (capture, kind) in (('heritage.extends', 'extends'), ('heritage.implements', 'implements'), ('heritage.trait', 'trait')) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:222-226
          for each parent in texts.get(capture, []) {
            // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:223-226
            if (the source predicate parent is truthy) {
              // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:224-226
              In source order: Evaluate result.heritage.append(Heritage(relative_path, class_name, parent, kind)); retain side effects and discard the expression result.
            }
          }
        }
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:228-229
      if (the source predicate 'name' not in captures is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:229-229
        Continue the immediately enclosing source loop at its next iteration.
      }
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:233-233
    In source order: Evaluate once last.get('name', ''); assign in source target order to name.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:234-235
    if (the source predicate not name or not is_valid_symbol_name(name) is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:235-235
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:236-236
    In source order: Evaluate once _classify(captures); assign in source target order to label.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:237-238
    if (the source predicate not label is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:238-238
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:239-239
    In source order: Evaluate once _definition_node(captures); assign in source target order to def_node.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:240-241
    if (the source predicate def_node is None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:241-241
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:243-243
    In source order: Evaluate once ''; assign in source target order to owner.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:244-247
    if (the source predicate label not in OWNERLESS_LABELS is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:245-245
      In source order: Evaluate once find_enclosing_class_name(def_node, source); assign in source target order to owner.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:246-247
      if (the source predicate not owner is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:247-247
        In source order: Evaluate once extract_receiver_type(def_node, source); assign in source target order to owner.
      }
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:248-252
    if (the source predicate label == 'Function' is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:249-249
      In source order: Evaluate once find_enclosing_class_name(def_node, source); assign in source target order to enclosing.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:250-252
      if (the source predicate enclosing is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:251-252
        In source order: Evaluate once 'Method'; assign in source target order to label. Then Evaluate once enclosing; assign in source target order to owner.
      }
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:254-256
    In source order: Evaluate once 0; assign in source target order to parameter_count. Then Evaluate once ''; assign in source target order to return_type. Then Evaluate once ''; assign in source target order to signature.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:257-259
    if (the source predicate label in CALLABLE_LABELS is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:258-259
      In source order: Evaluate once extract_method_signature(def_node, source); assign in source target order to (parameter_count, return_type). Then Evaluate once extract_signature(def_node, source); assign in source target order to signature.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:261-280
    In source order: Evaluate result.symbols.append(Symbol(id=symbol_id(label, relative_path, name, owner), name=name, label=label, kind=_classify_kind(captures), file_path=relative_path, start_line=def_node.start_point.row, end_line=def_node.end_point.row, is_exported=descriptor.is_exported(def_node, name, source), language=language, content=node_text(def_node, source), owner_name=owner, doc_comment=extract_doc_comment(def_node, source, language), annotations=_annotations_with_supplement(descriptor, def_node, source), signature=signature, parameter_count=parameter_count, return_type=return_type)); retain side effects and discard the expression result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:282-286
  In source order: Evaluate once deduplicate_symbols(result.symbols); assign in source target order to result.symbols. Then Evaluate once tree.root_node; assign in source target order to root. Then Evaluate once enrich_import_bindings(result.imports, root, source); assign in source target order to result.imports. Then Evaluate once enrich_call_receivers(result.calls, root, source); assign in source target order to result.calls.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:287-288
  if (the source predicate descriptor.interface_method_specs is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:288-288
    In source order: Evaluate result.symbols.extend(extract_interface_method_specs(root, source, relative_path, language)); retain side effects and discard the expression result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:289-290
  for each post_pass in descriptor.post_passes {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:290-290
    In source order: Evaluate post_pass(root, source, relative_path, language, result); retain side effects and discard the expression result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:291-292
  In source order: Evaluate once disambiguate_duplicate_ids(result.symbols); assign in source target order to result.symbols. Then Evaluate once list(extract_type_bindings(root, source, relative_path)); assign in source target order to result.type_bindings.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:293-293
  End this invocation with result.freeze().
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:296-306
// Source signature: _annotations_with_supplement(descriptor: LanguageDescriptor, def_node: Node, source: bytes) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _annotations_with_supplement(descriptor, def_node, source) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:299-299
  In source order: Evaluate once extract_annotations(def_node, source); assign in source target order to annotations.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:300-301
  if (the source predicate descriptor.annotation_supplement is None is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:301-301
    End this invocation with annotations.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:302-302
  In source order: Evaluate once annotations.split(',') if annotations else []; assign in source target order to existing.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:303-305
  for each name in descriptor.annotation_supplement(def_node, source) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:304-305
    if (the source predicate name not in existing is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:305-305
      In source order: Evaluate existing.append(name); retain side effects and discard the expression result.
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:306-306
  End this invocation with ','.join(existing).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:309-364
// Source signature: enrich_import_bindings(imports: list[Import], root: Node, source: bytes) -> list[Import]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn enrich_import_bindings(imports, root, source) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:310-310
  In source order: For source_index, assign {}; source annotation dict[str, int].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:311-312
  for each (index, imported) in enumerate(imports) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:312-312
    In source order: Evaluate source_index.setdefault(imported.source, index); retain side effects and discard the expression result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:314-361
  // Source signature: visit(node: Node, _depth: int) -> str | None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn visit(node, _depth) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:315-316
    if (the source predicate 'import' not in node.type.lower() is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:316-316
      End this invocation with None.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:317-317
    In source order: Evaluate once ''; assign in source target order to import_source.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:318-322
    for each field in ('source', 'path', 'module_name') {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:319-319
      In source order: Evaluate once node.child_by_field_name(field); assign in source target order to child.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:320-322
      if (the source predicate child is not None is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:321-321
        In source order: Evaluate once _trim_quotes(node_text(child, source)); assign in source target order to import_source.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:322-322
        Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
      }
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:323-328
    if (the source predicate not import_source is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:324-328
      for each child in node.children {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:325-325
        In source order: Evaluate once child.type.lower(); assign in source target order to child_type.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:326-328
        if (the source predicate child_type == 'string' or 'string_literal' in child_type is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:327-327
          In source order: Evaluate once _trim_quotes(node_text(child, source)); assign in source target order to import_source.
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:328-328
          Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
        }
      }
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:329-330
    if (the source predicate not import_source or import_source not in source_index is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:330-330
      End this invocation with None.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:331-331
    In source order: Evaluate once source_index[import_source]; assign in source target order to index.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:332-333
    if (the source predicate imports[index].bindings is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:333-333
      End this invocation with 'skip'.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:334-334
    In source order: For bindings, assign []; source annotation list[ImportBinding].
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:336-354
    // Source signature: collect(current: Node, _d: int) -> str | None
    Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
    fn collect(current, _d) {
      Bind arguments/defaults/annotations exactly as the source signature specifies.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:337-337
      In source order: Evaluate once current.type.lower(); assign in source target order to current_type.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:338-344
      if (the source predicate current_type == 'import_specifier' is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:339-339
        In source order: Evaluate once _collect_identifiers(current, source); assign in source target order to identifiers.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:340-343
        if (the source predicate len(identifiers) == 1 is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:341-341
          In source order: Evaluate bindings.append(ImportBinding(identifiers[0])); retain side effects and discard the expression result.
        }
        else {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:342-343
          if (the source predicate len(identifiers) >= 2 is truthy) {
            // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:343-343
            In source order: Evaluate bindings.append(ImportBinding(identifiers[0], identifiers[1])); retain side effects and discard the expression result.
          }
        }
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:344-344
        End this invocation with 'skip'.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:345-349
      if (the source predicate current_type == 'namespace_import' is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:346-346
        In source order: Evaluate once _collect_identifiers(current, source); assign in source target order to identifiers.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:347-348
        if (the source predicate identifiers is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:348-348
          In source order: Evaluate bindings.append(ImportBinding('*', identifiers[-1])); retain side effects and discard the expression result.
        }
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:349-349
        End this invocation with 'skip'.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:350-353
      if (the source predicate current_type == 'import_clause' is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:351-353
        for each child in current.children {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:352-353
          if (the source predicate child.type.lower() == 'identifier' is truthy) {
            // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:353-353
            In source order: Evaluate bindings.append(ImportBinding('default', node_text(child, source))); retain side effects and discard the expression result.
          }
        }
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:354-354
      End this invocation with None.
      If execution reaches this end, finish with the source implicit None result.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:356-356
    In source order: Evaluate walk(node, collect); retain side effects and discard the expression result.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:357-360
    if (the source predicate bindings is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:358-360
      In source order: Evaluate once Import(imports[index].file_path, imports[index].source, tuple(bindings)); assign in source target order to imports[index].
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:361-361
    End this invocation with 'skip'.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:363-363
  In source order: Evaluate walk(root, visit); retain side effects and discard the expression result.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:364-364
  End this invocation with imports.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:367-375
// Source signature: _collect_identifiers(node: Node, source: bytes) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _collect_identifiers(node, source) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:368-368
  In source order: For identifiers, assign []; source annotation list[str].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:369-374
  for each child in node.children {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:370-370
    In source order: Evaluate once child.type.lower(); assign in source target order to child_type.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:371-374
    if (the source predicate 'identifier' in child_type or child_type == 'name' is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:372-372
      In source order: Evaluate once node_text(child, source); assign in source target order to text.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:373-374
      if (the source predicate text is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:374-374
        In source order: Evaluate identifiers.append(text); retain side effects and discard the expression result.
      }
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:375-375
  End this invocation with identifiers.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:378-429
// Source signature: enrich_call_receivers(calls: list[Call], root: Node, source: bytes) -> list[Call]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn enrich_call_receivers(calls, root, source) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:379-379
  In source order: Evaluate once {(call.callee_name, call.line): index for index, call in enumerate(calls)}; assign in source target order to call_index.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:381-426
  // Source signature: visit(node: Node, _depth: int) -> str | None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn visit(node, _depth) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:382-382
    In source order: Evaluate once node.type.lower(); assign in source target order to node_type.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:383-384
    if (the source predicate 'call' not in node_type and 'invocation' not in node_type is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:384-384
      End this invocation with None.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:385-385
    In source order: For function_node, assign None; source annotation Node | None.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:386-389
    for each field in ('function', 'method', 'callee', 'name') {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:387-387
      In source order: Evaluate once node.child_by_field_name(field); assign in source target order to function_node.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:388-389
      if (the source predicate function_node is not None is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:389-389
        Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
      }
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:390-391
    if (the source predicate function_node is None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:391-391
      End this invocation with None.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:392-392
    In source order: Evaluate once function_node.type.lower(); assign in source target order to function_type.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:393-397
    if (the source predicate not any((token in function_type for token in ('member', 'field', 'selector', 'navigation', 'attribute', 'access'))) is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:397-397
      End this invocation with None.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:398-399
    In source order: Evaluate once ''; assign in source target order to receiver. Then Evaluate once ''; assign in source target order to method_name.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:400-409
    for each field in ('object', 'operand', 'value', 'expression') {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:401-401
      In source order: Evaluate once function_node.child_by_field_name(field); assign in source target order to child.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:402-409
      if (the source predicate child is not None is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:403-406
        In source order: Evaluate once node_text(child, source); assign in source target order to receiver. Then Evaluate once receiver.rfind('.'); assign in source target order to dot.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:407-408
        if (the source predicate dot >= 0 is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:408-408
          In source order: Evaluate once receiver[dot + 1:]; assign in source target order to receiver.
        }
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:409-409
        Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
      }
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:410-414
    for each field in ('property', 'field', 'name', 'attribute') {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:411-411
      In source order: Evaluate once function_node.child_by_field_name(field); assign in source target order to child.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:412-414
      if (the source predicate child is not None is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:413-413
        In source order: Evaluate once node_text(child, source); assign in source target order to method_name.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:414-414
        Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
      }
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:415-419
    if (the source predicate not receiver or not method_name is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:416-416
      In source order: Evaluate once _collect_identifiers(function_node, source); assign in source target order to identifiers.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:417-419
      if (the source predicate len(identifiers) >= 2 is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:418-419
        In source order: Evaluate once receiver or identifiers[0]; assign in source target order to receiver. Then Evaluate once method_name or identifiers[-1]; assign in source target order to method_name.
      }
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:420-425
    if (the source predicate receiver and method_name is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:421-421
      In source order: Evaluate once call_index.get((method_name, node.start_point.row)); assign in source target order to index.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:422-425
      if (the source predicate index is not None and (not calls[index].receiver_name) is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:423-425
        In source order: Evaluate once Call(calls[index].file_path, method_name, receiver, calls[index].line); assign in source target order to calls[index].
      }
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:426-426
    End this invocation with None.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:428-428
  In source order: Evaluate walk(root, visit); retain side effects and discard the expression result.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:429-429
  End this invocation with calls.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:434-435
In source order: Evaluate once frozenset({'interface_type', 'protocol_body'}); assign in source target order to _INTERFACE_BODY_TYPES. Then Evaluate once frozenset({'method_spec', 'method_elem'}); assign in source target order to _METHOD_SPEC_TYPES.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:438-484
// Source signature: extract_interface_method_specs(root: Node, source: bytes, relative_path: str, language: str) -> list[Symbol]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn extract_interface_method_specs(root, source, relative_path, language) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:441-442
  In source order: Retain source documentation literal source_literal_441_4; it is not a model call. Then For extra, assign []; source annotation list[Symbol].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:444-481
  // Source signature: visit(node: Node, _depth: int) -> str | None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn visit(node, _depth) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:445-446
    if (the source predicate node.type.lower() not in _INTERFACE_BODY_TYPES is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:446-446
      End this invocation with None.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:447-447
    In source order: Evaluate once _interface_owner_name(node, source); assign in source target order to interface_name.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:448-449
    if (the source predicate not interface_name is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:449-449
      End this invocation with None.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:450-480
    for each child in node.children {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:451-452
      if (the source predicate not child.is_named or child.type.lower() not in _METHOD_SPEC_TYPES is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:452-452
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:453-453
      In source order: Evaluate once child.child_by_field_name('name'); assign in source target order to name_node.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:454-458
      if (the source predicate name_node is None is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:455-458
        for each candidate in child.children {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:456-458
          if (the source predicate candidate.type.lower() in ('field_identifier', 'identifier') is truthy) {
            // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:457-457
            In source order: Evaluate once candidate; assign in source target order to name_node.
            // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:458-458
            Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
          }
        }
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:459-460
      if (the source predicate name_node is None is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:460-460
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:461-461
      In source order: Evaluate once node_text(name_node, source); assign in source target order to method_name.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:462-463
      if (the source predicate not method_name is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:463-463
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:464-480
      In source order: Evaluate once extract_method_signature(child, source); assign in source target order to (parameter_count, return_type). Then Evaluate extra.append(Symbol(id=symbol_id('Method', relative_path, method_name, interface_name), name=method_name, label='Method', file_path=relative_path, start_line=child.start_point.row, end_line=child.end_point.row, is_exported=True, language=language, content=node_text(child, source), owner_name=interface_name, parameter_count=parameter_count, return_type=return_type)); retain side effects and discard the expression result.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:481-481
    End this invocation with 'skip'.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:483-483
  In source order: Evaluate walk(root, visit); retain side effects and discard the expression result.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:484-484
  End this invocation with extra.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:487-502
// Source signature: _interface_owner_name(node: Node, source: bytes) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _interface_owner_name(node, source) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:488-488
  In source order: Evaluate once node.parent; assign in source target order to current.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:489-501
  for each _ in range(5) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:490-491
    if (the source predicate current is None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:491-491
      End this invocation with ''.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:492-492
    In source order: Evaluate once current.child_by_field_name('name'); assign in source target order to name_node.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:493-496
    if (the source predicate name_node is not None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:494-494
      In source order: Evaluate once node_text(name_node, source); assign in source target order to name.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:495-496
      if (the source predicate name is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:496-496
        End this invocation with name.
      }
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:497-500
    if (the source predicate current.type.lower() in ('type_spec', 'protocol_declaration') is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:498-498
      In source order: Evaluate once extract_class_name(current, source); assign in source target order to name.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:499-500
      if (the source predicate name is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:500-500
        End this invocation with name.
      }
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:501-501
    In source order: Evaluate once current.parent; assign in source target order to current.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py:502-502
  End this invocation with ''.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from context_graph_sdk.extractors import runtime` at source line 26: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/extractors/__init__.py.sudo.md`.
- `from context_graph_sdk.extractors import runtime` at source line 26: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py.sudo.md`.
- `from context_graph_sdk.extractors.analysis import extract_annotations, extract_class_name, extract_doc_comment, extract_method_signature, extract_receiver_type, extract_signature, find_enclosing_class_name, first_identifier_text, node_text, walk` at source line 27: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/extractors/analysis.py.sudo.md`.
- `from context_graph_sdk.extractors.bindings import extract_type_bindings` at source line 39: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/extractors/bindings.py.sudo.md`.
- `from context_graph_sdk.extractors.descriptors import LANGUAGE_DESCRIPTORS, LanguageDescriptor` at source line 40: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/extractors/descriptors.py.sudo.md`.
- `from context_graph_sdk.extractors.records import CALLABLE_LABELS, OWNERLESS_LABELS, Assignment, Call, Delegate, FileExtraction, Heritage, Import, ImportBinding, MutableFileResult, Spawn, Symbol, deduplicate_symbols, disambiguate_duplicate_ids, is_valid_symbol_name, symbol_id` at source line 41: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../../../prompt_representation/vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py.sudo.md). Exact strings in the evidence asset support this conversion.
