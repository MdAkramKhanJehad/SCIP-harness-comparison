# vendor/context_graph_sdk/src/context_graph_sdk/resolution/heritage.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vendor/context_graph_sdk/src/context_graph_sdk/resolution/heritage.py.evidence.json`. SHA-256: `8690939c33022fee5544802126a96cf8b914ef36a2efb79adafed8da4707f84a`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/heritage.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.extractors.records import Symbol; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.models import LocalRelationshipType; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.resolution.context import ResolutionContext, ResolutionResult; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/heritage.py:24-24
In source order: Evaluate once ('Class', 'Interface', 'Struct', 'Trait'); assign in source target order to CLASS_LIKE_LABELS.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/heritage.py:27-40
// Source signature: _resolve_parent(context: ResolutionContext, name: str, child_file: str) -> Symbol | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _resolve_parent(context, name, child_file) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/heritage.py:28-29
  In source order: Retain source documentation literal source_literal_28_4; it is not a model call. Then Evaluate once context.symbols_by_name.get(name, []); assign in source target order to candidates.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/heritage.py:30-31
  if (the source predicate not candidates is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/heritage.py:31-31
    End this invocation with None.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/heritage.py:32-39
  for each label in CLASS_LIKE_LABELS {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/heritage.py:33-33
    In source order: Evaluate once [candidate for candidate in candidates if candidate.label == label]; assign in source target order to labelled.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/heritage.py:34-35
    if (the source predicate not labelled is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/heritage.py:35-35
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/heritage.py:36-38
    for each candidate in labelled {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/heritage.py:37-38
      if (the source predicate candidate.file_path == child_file is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/heritage.py:38-38
        End this invocation with candidate.
      }
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/heritage.py:39-39
    End this invocation with labelled[0].
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/heritage.py:40-40
  End this invocation with candidates[0].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/heritage.py:43-70
// Source signature: resolve_heritage(context: ResolutionContext, result: ResolutionResult) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn resolve_heritage(context, result) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/heritage.py:44-70
  for each (path, file_result) in context.extraction.files {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/heritage.py:45-70
    for each heritage in file_result.heritage {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/heritage.py:47-51
      In source order: Evaluate once [candidate for candidate in context.symbols_by_name.get(heritage.class_name, []) if candidate.file_path == path]; assign in source target order to children.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/heritage.py:52-53
      if (the source predicate not children is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/heritage.py:53-53
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/heritage.py:54-55
      In source order: Evaluate once children[0]; assign in source target order to child. Then Evaluate once _resolve_parent(context, heritage.parent_name, path); assign in source target order to parent.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/heritage.py:56-57
      if (the source predicate parent is None is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/heritage.py:57-57
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/heritage.py:58-69
      if (the source predicate heritage.kind == 'extends' is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/heritage.py:61-65
        In source order: Evaluate once LocalRelationshipType.IMPLEMENTS if parent.label in ('Interface', 'Trait') else LocalRelationshipType.INHERITS; assign in source target order to relationship.
      }
      else {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/heritage.py:66-69
        if (the source predicate heritage.kind in ('implements', 'trait') is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/heritage.py:67-67
          In source order: Evaluate once LocalRelationshipType.IMPLEMENTS; assign in source target order to relationship.
        }
        else {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/heritage.py:69-69
          Continue the immediately enclosing source loop at its next iteration.
        }
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/heritage.py:70-70
      In source order: Evaluate result.add_edge(child.id, relationship, parent.id); retain side effects and discard the expression result.
    }
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/heritage.py:73-81
// Source signature: _methods_by_owner(context: ResolutionContext) -> dict[str, dict[str, list[Symbol]]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _methods_by_owner(context) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/heritage.py:74-75
  In source order: Retain source documentation literal source_literal_74_4; it is not a model call. Then For by_owner, assign {}; source annotation dict[str, dict[str, list[Symbol]]].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/heritage.py:76-80
  for each symbol in context.symbols {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/heritage.py:77-78
    if (the source predicate symbol.label != 'Method' or not symbol.owner_name is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/heritage.py:78-78
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/heritage.py:79-80
    In source order: Evaluate once source_template_79_20; assign in source target order to owner_key. Then Evaluate by_owner.setdefault(owner_key, {}).setdefault(symbol.name, []).append(symbol); retain side effects and discard the expression result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/heritage.py:81-81
  End this invocation with by_owner.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/heritage.py:84-120
// Source signature: resolve_structural_interfaces(context: ResolutionContext, result: ResolutionResult) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn resolve_structural_interfaces(context, result) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/heritage.py:85-85
  In source order: Evaluate once _methods_by_owner(context); assign in source target order to methods.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/heritage.py:87-88
  // Source signature: method_names(owner: Symbol) -> set[str]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn method_names(owner) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/heritage.py:88-88
    End this invocation with set(methods.get(source_template_88_31, {})).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/heritage.py:90-94
  In source order: Evaluate once [(symbol, method_names(symbol)) for symbol in context.symbols if symbol.label == 'Interface' and method_names(symbol)]; assign in source target order to interfaces.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/heritage.py:95-96
  if (the source predicate not interfaces is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/heritage.py:96-96
    End this invocation with None.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/heritage.py:97-109
  In source order: For existing_implements, assign {(edge.source_local_id, edge.target_local_id) for edge in result.edges if edge.relationship is LocalRelationshipType.IMPLEMENTS}; source annotation set[tuple[str, str]]. Then Evaluate once [(symbol, method_names(symbol)) for symbol in context.symbols if symbol.label in ('Struct', 'Class') and method_names(symbol)]; assign in source target order to classes. Then For owners_by_method, assign {}; source annotation dict[str, list[int]].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/heritage.py:110-112
  for each (index, (_, names)) in enumerate(classes) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/heritage.py:111-112
    for each name in names {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/heritage.py:112-112
      In source order: Evaluate owners_by_method.setdefault(name, []).append(index); retain side effects and discard the expression result.
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/heritage.py:113-120
  for each (interface, required) in interfaces {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/heritage.py:114-114
    In source order: Evaluate once min(required, key=lambda name: (len(owners_by_method.get(name, [])), name)); assign in source target order to rarest.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/heritage.py:115-120
    for each index in owners_by_method.get(rarest, []) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/heritage.py:116-116
      In source order: Evaluate once classes[index]; assign in source target order to (symbol, own).
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/heritage.py:117-118
      if (the source predicate (symbol.id, interface.id) in existing_implements is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/heritage.py:118-118
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/heritage.py:119-120
      if (the source predicate required <= own is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/heritage.py:120-120
        In source order: Evaluate result.add_edge(symbol.id, LocalRelationshipType.IMPLEMENTS, interface.id); retain side effects and discard the expression result.
      }
    }
  }
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from context_graph_sdk.extractors.records import Symbol` at source line 19: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py.sudo.md`.
- `from context_graph_sdk.models import LocalRelationshipType` at source line 20: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/models.py.sudo.md`.
- `from context_graph_sdk.resolution.context import ResolutionContext, ResolutionResult` at source line 21: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py.sudo.md`.
