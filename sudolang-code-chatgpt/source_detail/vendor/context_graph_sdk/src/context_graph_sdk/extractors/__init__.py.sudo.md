# vendor/context_graph_sdk/src/context_graph_sdk/extractors/__init__.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vendor/context_graph_sdk/src/context_graph_sdk/extractors/__init__.py.evidence.json`. SHA-256: `1d4e4b745a88b662610c15eb44a20fa8889e5d1282768780f6533a7ef0a4962e`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/__init__.py:15-22
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from collections.abc import Callable; preserve alias and import-time effects. Then Resolve source import from typing import cast; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.extractors.records import ExtractionResult, FileDiagnostic, FileExtraction; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/__init__.py:23-31
In source order: Resolve source import from context_graph_sdk.extractors.runtime import DEFAULT_FILE_TIMEOUT_SECONDS, DEFAULT_MAX_WORKERS, SUPPORTED_LANGUAGES, WorkItem, analysis_components, is_supported_language, run_bounded; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/__init__.py:34-70
// Source signature: extract_repository(root: str, files: list[tuple[str, str]], *, max_workers: int | None=None, file_timeout_seconds: float | None=None, on_progress: Callable[[int, int], None] | None=None) -> ExtractionResult
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn extract_repository(root, files, max_workers, file_timeout_seconds, on_progress) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/__init__.py:42-66
  In source order: Retain source documentation literal source_literal_42_4; it is not a model call. Then Evaluate once sorted((WorkItem(relative_path, language) for relative_path, language in files if is_supported_language(language)), key=lambda item: item.relative_path); assign in source target order to items. Then Evaluate once run_bounded(root, items, max_workers=max_workers if max_workers is not None else DEFAULT_MAX_WORKERS, file_timeout_seconds=file_timeout_seconds if file_timeout_seconds is not None else DEFAULT_FILE_TIMEOUT_SECONDS, on_progress=on_progress); assign in source target order to (raw_successes, failures). Then Evaluate once [(item, cast(FileExtraction, extraction)) for item, extraction in raw_successes]; assign in source target order to successes.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/__init__.py:67-70
  End this invocation with ExtractionResult(tuple(((item.relative_path, extraction) for item, extraction in successes)), tuple((FileDiagnostic(item.relative_path, reason) for item, reason in failures))).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/__init__.py:73-79
In source order: Evaluate once ['SUPPORTED_LANGUAGES', 'ExtractionResult', 'analysis_components', 'extract_repository', 'is_supported_language']; assign in source target order to __all__.
```

## Local import links

- `from context_graph_sdk.extractors.records import ExtractionResult, FileDiagnostic, FileExtraction` at source line 22: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py.sudo.md`.
- `from context_graph_sdk.extractors.runtime import DEFAULT_FILE_TIMEOUT_SECONDS, DEFAULT_MAX_WORKERS, SUPPORTED_LANGUAGES, WorkItem, analysis_components, is_supported_language, run_bounded` at source line 23: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py.sudo.md`.
