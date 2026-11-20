# vendor/context_graph_sdk/src/context_graph_sdk/resolution/runner.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vendor/context_graph_sdk/src/context_graph_sdk/resolution/runner.py.evidence.json`. SHA-256: `a001e69008a772c7d47cede1c25d940bf968dc62e9264adac807b76f91583ef9`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/runner.py:15-22
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from collections.abc import Sequence; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.extractors.records import ExtractionResult; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.project.config import ProjectConfig; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/runner.py:23-27
In source order: Resolve source import from context_graph_sdk.resolution.bindings import resolve_assignments, resolve_type_bindings; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.resolution.calls import resolve_calls_spawns_delegates; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.resolution.context import ResolutionContext, ResolutionResult; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.resolution.heritage import resolve_heritage, resolve_structural_interfaces; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.resolution.imports import resolve_imports; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/runner.py:28-28
In source order: Resolve source import from context_graph_sdk.resolution.mro import compute_mro; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/runner.py:31-51
// Source signature: resolve_project(files: Sequence[tuple[str, str]], folder_paths: Sequence[str], extraction: ExtractionResult, config: ProjectConfig) -> ResolutionResult
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn resolve_project(files, folder_paths, extraction, config) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/runner.py:37-45
  In source order: Retain source documentation literal source_literal_37_4; it is not a model call. Then Evaluate once ResolutionContext(files, folder_paths, extraction, config); assign in source target order to context. Then Evaluate once ResolutionResult(); assign in source target order to result. Then Evaluate resolve_imports(context, result); retain side effects and discard the expression result. Then Evaluate resolve_calls_spawns_delegates(context, result); retain side effects and discard the expression result.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/runner.py:46-50
  In source order: Evaluate resolve_heritage(context, result); retain side effects and discard the expression result. Then Evaluate resolve_structural_interfaces(context, result); retain side effects and discard the expression result. Then Evaluate resolve_assignments(context, result); retain side effects and discard the expression result. Then Evaluate resolve_type_bindings(context, result); retain side effects and discard the expression result. Then Evaluate compute_mro(context, result); retain side effects and discard the expression result.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/runner.py:51-51
  End this invocation with result.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from context_graph_sdk.extractors.records import ExtractionResult` at source line 21: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py.sudo.md`.
- `from context_graph_sdk.project.config import ProjectConfig` at source line 22: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/project/config.py.sudo.md`.
- `from context_graph_sdk.resolution.bindings import resolve_assignments, resolve_type_bindings` at source line 23: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/resolution/bindings.py.sudo.md`.
- `from context_graph_sdk.resolution.calls import resolve_calls_spawns_delegates` at source line 24: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py.sudo.md`.
- `from context_graph_sdk.resolution.context import ResolutionContext, ResolutionResult` at source line 25: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py.sudo.md`.
- `from context_graph_sdk.resolution.heritage import resolve_heritage, resolve_structural_interfaces` at source line 26: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/resolution/heritage.py.sudo.md`.
- `from context_graph_sdk.resolution.imports import resolve_imports` at source line 27: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py.sudo.md`.
- `from context_graph_sdk.resolution.mro import compute_mro` at source line 28: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py.sudo.md`.
