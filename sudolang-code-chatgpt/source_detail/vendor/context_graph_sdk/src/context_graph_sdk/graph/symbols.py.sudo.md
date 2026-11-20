# vendor/context_graph_sdk/src/context_graph_sdk/graph/symbols.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vendor/context_graph_sdk/src/context_graph_sdk/graph/symbols.py.evidence.json`. SHA-256: `bfd4863324567b181aa20b688d73dfa02db816292b9fc14db3ea17f36e7fcd11`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/symbols.py:15-22
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import re; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.extractors.records import CALLABLE_LABELS, ExtractionResult, Symbol; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.models import GraphNode, LocalRelationshipType; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/symbols.py:24-44
In source order: Evaluate once re.compile(source_literal_25_4); assign in source target order to _TEST_DIR. Then Evaluate once frozenset({'testing.go', 'test_helpers.go', 'test_helper.go', 'testutil.go', 'testutils.go', 'conftest.py', 'test_helpers.rb', 'test_helper.rb', 'spec_helper.rb', 'rails_helper.rb'}); assign in source target order to _TEST_HELPER_NAMES.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/symbols.py:47-64
// Source signature: is_test_file(file_path: str) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn is_test_file(file_path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/symbols.py:48-48
  In source order: Evaluate once file_path.replace('\\', '/').lower(); assign in source target order to lower.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/symbols.py:49-50
  if (the source predicate _TEST_DIR.search(lower) is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/symbols.py:50-50
    End this invocation with True.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/symbols.py:51-52
  if (the source predicate '.test.' in lower or '.spec.' in lower or '.cy.' in lower is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/symbols.py:52-52
    End this invocation with True.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/symbols.py:53-54
  if (the source predicate lower.endswith('_test.go') is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/symbols.py:54-54
    End this invocation with True.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/symbols.py:55-55
  In source order: Evaluate once lower.rsplit('/', 1)[-1]; assign in source target order to base.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/symbols.py:56-57
  if (the source predicate base in _TEST_HELPER_NAMES is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/symbols.py:57-57
    End this invocation with True.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/symbols.py:58-61
  if (the source predicate base.endswith('.go') and base.startswith('test') and (base != 'testing.go') is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/symbols.py:59-59
    In source order: Evaluate once base[:-3]; assign in source target order to stem.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/symbols.py:60-61
    if (the source predicate len(stem) == 4 or (len(stem) > 4 and (stem[4].isupper() or stem[4] == '_')) is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/symbols.py:61-61
      End this invocation with True.
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/symbols.py:62-63
  if (the source predicate base.endswith('.py') and (base.startswith('test_') or base.endswith('_test.py')) is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/symbols.py:63-63
    End this invocation with True.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/symbols.py:64-64
  End this invocation with base.endswith('_spec.rb').
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/symbols.py:67-97
// Source signature: symbol_properties(symbol: Symbol) -> dict[str, object]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn symbol_properties(symbol) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/symbols.py:68-69
  In source order: Evaluate once is_test_file(symbol.file_path); assign in source target order to is_test. Then Evaluate once symbol.is_exported; assign in source target order to is_exported.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/symbols.py:72-73
  if (the source predicate is_exported and symbol.label in ('Function', 'Method') and is_test is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/symbols.py:73-73
    In source order: Evaluate once False; assign in source target order to is_exported.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/symbols.py:74-82
  In source order: For properties, assign {'name': symbol.name, 'filePath': symbol.file_path, 'startLine': symbol.start_line, 'endLine': symbol.end_line, 'isExported': is_exported, 'language': symbol.language, 'isTest': is_test}; source annotation dict[str, object].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/symbols.py:83-84
  if (the source predicate symbol.kind is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/symbols.py:84-84
    In source order: Evaluate once symbol.kind; assign in source target order to properties['kind'].
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/symbols.py:85-86
  if (the source predicate symbol.content is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/symbols.py:86-86
    In source order: Evaluate once symbol.content; assign in source target order to properties['content'].
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/symbols.py:87-88
  if (the source predicate symbol.doc_comment is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/symbols.py:88-88
    In source order: Evaluate once symbol.doc_comment; assign in source target order to properties['description'].
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/symbols.py:89-90
  if (the source predicate symbol.annotations is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/symbols.py:90-90
    In source order: Evaluate once symbol.annotations; assign in source target order to properties['annotations'].
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/symbols.py:91-92
  if (the source predicate symbol.signature is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/symbols.py:92-92
    In source order: Evaluate once symbol.signature; assign in source target order to properties['signature'].
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/symbols.py:93-94
  if (the source predicate symbol.parameter_count > 0 is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/symbols.py:94-94
    In source order: Evaluate once symbol.parameter_count; assign in source target order to properties['parameterCount'].
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/symbols.py:95-96
  if (the source predicate symbol.return_type is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/symbols.py:96-96
    In source order: Evaluate once symbol.return_type; assign in source target order to properties['returnType'].
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/symbols.py:97-97
  End this invocation with properties.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/symbols.py:100-105
// Source signature: owner_relationship(symbol: Symbol) -> LocalRelationshipType
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn owner_relationship(symbol) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/symbols.py:101-102
  if (the source predicate symbol.label in ('Property', 'Const') is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/symbols.py:102-102
    End this invocation with LocalRelationshipType.HAS_PROPERTY.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/symbols.py:103-104
  if (the source predicate symbol.label in CALLABLE_LABELS is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/symbols.py:104-104
    End this invocation with LocalRelationshipType.HAS_METHOD.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/symbols.py:105-105
  End this invocation with LocalRelationshipType.CONTAINS.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/symbols.py:108-113
// Source signature: same_file_owner(symbol: Symbol, nodes_by_name: dict[str, list[GraphNode]]) -> GraphNode | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn same_file_owner(symbol, nodes_by_name) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/symbols.py:109-109
  In source order: Retain source documentation literal source_literal_109_4; it is not a model call.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/symbols.py:110-112
  for each candidate in nodes_by_name.get(symbol.owner_name, []) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/symbols.py:111-112
    if (the source predicate candidate.properties.to_dict().get('filePath') == symbol.file_path is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/symbols.py:112-112
      End this invocation with candidate.
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/symbols.py:113-113
  End this invocation with None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/symbols.py:116-120
// Source signature: sorted_symbols(extraction: ExtractionResult) -> list[Symbol]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn sorted_symbols(extraction) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/graph/symbols.py:117-120
  End this invocation with sorted((symbol for _, file_result in extraction.files for symbol in file_result.symbols), key=lambda symbol: (symbol.file_path, symbol.start_line, symbol.id)).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from context_graph_sdk.extractors.records import CALLABLE_LABELS, ExtractionResult, Symbol` at source line 21: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py.sudo.md`.
- `from context_graph_sdk.models import GraphNode, LocalRelationshipType` at source line 22: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/models.py.sudo.md`.
