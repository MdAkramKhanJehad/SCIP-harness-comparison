# vendor/context_graph_sdk/src/context_graph_sdk/workspace/__init__.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vendor/context_graph_sdk/src/context_graph_sdk/workspace/__init__.py.evidence.json`. SHA-256: `64e40f4a8b7a03e7b2c966649d25e84a958848595a81071c98213bc18234f7d8`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/workspace/__init__.py:15-26
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from .catalog import WorkspaceCatalog; preserve alias and import-time effects. Then Resolve source import from .contracts import SnapshotLease, SnapshotLeaseManager; preserve alias and import-time effects. Then Resolve source import from .handles import SnapshotLeaseRegistry; preserve alias and import-time effects. Then Evaluate once ['SnapshotLease', 'SnapshotLeaseManager', 'SnapshotLeaseRegistry', 'WorkspaceCatalog']; assign in source target order to __all__.
```

## Local import links

- `from .catalog import WorkspaceCatalog` at source line 17: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/workspace/catalog.py.sudo.md`.
- `from .contracts import SnapshotLease, SnapshotLeaseManager` at source line 18: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/workspace/contracts.py.sudo.md`.
- `from .handles import SnapshotLeaseRegistry` at source line 19: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/workspace/handles.py.sudo.md`.
