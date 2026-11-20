# vendor/context_graph_sdk/src/context_graph_sdk/symbols.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vendor/context_graph_sdk/src/context_graph_sdk/symbols.py.evidence.json`. SHA-256: `bfc890dd55c273c11b74ce36d885b46bb907dba7e554030089ef4de631e04f3d`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/symbols.py:15-52
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Evaluate once 'Symbol'; assign in source target order to SYMBOL_LABEL. Then Evaluate once frozenset({'Annotation', 'Class', 'CodeElement', 'Const', 'Constructor', 'Delegate', 'Enum', 'Function', 'Impl', 'Interface', 'Macro', 'Method', 'Module', 'Namespace', 'Property', 'Record', 'Static', 'Struct', 'Template', 'Trait', 'TypeAlias', 'Typedef', 'Union', 'Variable'}); assign in source target order to SYMBOL_CATEGORY_LABELS. Then Evaluate once frozenset({SYMBOL_LABEL, *SYMBOL_CATEGORY_LABELS}); assign in source target order to SYMBOL_LABELS.
```

## Local import links

No statically resolved in-checkout import; external calls remain explicit dependency boundaries.
