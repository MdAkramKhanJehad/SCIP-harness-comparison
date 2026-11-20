# vendor/context_graph_sdk/src/context_graph_sdk/analysis/__init__.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vendor/context_graph_sdk/src/context_graph_sdk/analysis/__init__.py.evidence.json`. SHA-256: `508fd01b67d753765d242c974cab2127e8766340b8c1d4565770a71fc132b155`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/__init__.py:15-37
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from context_graph_sdk.analysis.leiden import Adjacency, LeidenOptions, LeidenResult, Objective, leiden; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.analysis.processes import ProcessOptions; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.analysis.runner import DerivedAnalysis, derive_analysis, derive_snapshot; preserve alias and import-time effects. Then Evaluate once ['Adjacency', 'DerivedAnalysis', 'LeidenOptions', 'LeidenResult', 'Objective', 'ProcessOptions', 'derive_analysis', 'derive_snapshot', 'leiden']; assign in source target order to __all__.
```

## Local import links

- `from context_graph_sdk.analysis.leiden import Adjacency, LeidenOptions, LeidenResult, Objective, leiden` at source line 17: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py.sudo.md`.
- `from context_graph_sdk.analysis.processes import ProcessOptions` at source line 24: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py.sudo.md`.
- `from context_graph_sdk.analysis.runner import DerivedAnalysis, derive_analysis, derive_snapshot` at source line 25: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/analysis/runner.py.sudo.md`.
