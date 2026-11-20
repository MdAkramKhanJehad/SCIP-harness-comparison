# vendor/context_graph_sdk/src/context_graph_sdk/resolution/__init__.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vendor/context_graph_sdk/src/context_graph_sdk/resolution/__init__.py.evidence.json`. SHA-256: `896a34b41327768ccdb43abae6b582968e8cb24acd347f33f36c12cc2e33107d`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/__init__.py:15-27
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from context_graph_sdk.resolution.context import ResolutionContext, ResolutionResult, ResolvedEdge; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.resolution.mro import c3_linearize; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.resolution.runner import resolve_project; preserve alias and import-time effects. Then Evaluate once ['ResolutionContext', 'ResolutionResult', 'ResolvedEdge', 'c3_linearize', 'resolve_project']; assign in source target order to __all__.
```

## Local import links

- `from context_graph_sdk.resolution.context import ResolutionContext, ResolutionResult, ResolvedEdge` at source line 17: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py.sudo.md`.
- `from context_graph_sdk.resolution.mro import c3_linearize` at source line 18: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py.sudo.md`.
- `from context_graph_sdk.resolution.runner import resolve_project` at source line 19: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/resolution/runner.py.sudo.md`.
