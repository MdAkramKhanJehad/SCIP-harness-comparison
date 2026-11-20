# vendor/context_graph_sdk/src/context_graph_sdk/ingestion.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vendor/context_graph_sdk/src/context_graph_sdk/ingestion.py.evidence.json`. SHA-256: `b140b34d0289b9fa5be4f070fb3a0dbbf2826c2bbd34c8febd3cf603140e611d`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/ingestion.py:15-22
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from collections.abc import Callable; preserve alias and import-time effects. Then Resolve source import from dataclasses import dataclass; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.discovery.walker import RepositoryWalk; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/ingestion.py:23-30
In source order: Resolve source import from context_graph_sdk.extractors import ExtractionResult, extract_repository; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.plugins import LanguageExtractor, PluginMetadata, PluginPhase, ProjectExtractor; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.project import ProjectConfig, load_project_config; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/ingestion.py:34-36
// Source: vendor/context_graph_sdk/src/context_graph_sdk/ingestion.py:33-33
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/ingestion.py:34-36
interface IngestionResult {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/ingestion.py:35-36
  In source order: For config, declare without assigning a value; source annotation ProjectConfig. Then For extraction, declare without assigning a value; source annotation ExtractionResult.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/ingestion.py:39-56
interface BuiltinLanguageExtractor {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/ingestion.py:40-40
  In source order: Evaluate once PluginMetadata(PluginPhase.EXTRACTION, 10, 'builtin-languages', '1'); assign in source target order to metadata.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/ingestion.py:42-43
  // Source signature: __init__(self, on_progress: Callable[[int, int], None] | None=None) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self, on_progress) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/ingestion.py:43-43
    In source order: Evaluate once on_progress; assign in source target order to self._on_progress.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/ingestion.py:46-49
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/ingestion.py:45-45
  Before creating this callable, evaluate and retain decorators top-to-bottom: property.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/ingestion.py:46-49
  // Source signature: languages(self) -> tuple[str, ...]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn languages(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/ingestion.py:47-47
    In source order: Resolve source import from context_graph_sdk.extractors.runtime import SUPPORTED_LANGUAGES; preserve alias and import-time effects.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/ingestion.py:49-49
    End this invocation with tuple(sorted(SUPPORTED_LANGUAGES)).
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/ingestion.py:51-56
  // Source signature: extract(self, repository: RepositoryWalk) -> ExtractionResult
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn extract(self, repository) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/ingestion.py:52-56
    End this invocation with extract_repository(repository.root, [(file.relative_path, file.language) for file in repository.files if file.language], on_progress=self._on_progress).
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/ingestion.py:59-65
interface BuiltinProjectExtractor {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/ingestion.py:60-60
  In source order: Evaluate once PluginMetadata(PluginPhase.EXTRACTION, 20, 'builtin-project', '1'); assign in source target order to metadata.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/ingestion.py:62-65
  // Source signature: extract(self, repository: RepositoryWalk) -> ProjectConfig
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn extract(self, repository) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/ingestion.py:63-65
    End this invocation with load_project_config(repository.root, [file.relative_path for file in repository.files]).
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/ingestion.py:68-82
interface BuiltinExtractionRegistry {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/ingestion.py:69-69
  In source order: Retain source documentation literal source_literal_69_4; it is not a model call.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/ingestion.py:71-79
  // Source signature: __init__(self, language_extractor: LanguageExtractor | None=None, project_extractor: ProjectExtractor | None=None) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self, language_extractor, project_extractor) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/ingestion.py:76-79
    In source order: Evaluate once language_extractor or BuiltinLanguageExtractor(); assign in source target order to language. Then Evaluate once project_extractor or BuiltinProjectExtractor(); assign in source target order to project. Then For self.language, assign language; source annotation LanguageExtractor. Then For self.project, assign project; source annotation ProjectExtractor.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/ingestion.py:81-82
  // Source signature: run(self, walk: RepositoryWalk) -> IngestionResult
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn run(self, walk) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/ingestion.py:82-82
    End this invocation with IngestionResult(self.project.extract(walk), self.language.extract(walk)).
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/ingestion.py:85-95
// Source signature: run_builtin_ingestion(walk: RepositoryWalk, *, on_language_start: Callable[[], None] | None=None, on_file_progress: Callable[[int, int], None] | None=None) -> IngestionResult
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn run_builtin_ingestion(walk, on_language_start, on_file_progress) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/ingestion.py:91-92
  In source order: Evaluate once BuiltinExtractionRegistry(BuiltinLanguageExtractor(on_file_progress)); assign in source target order to registry. Then Evaluate once registry.project.extract(walk); assign in source target order to config.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/ingestion.py:93-94
  if (the source predicate on_language_start is not None is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/ingestion.py:94-94
    In source order: Evaluate on_language_start(); retain side effects and discard the expression result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/ingestion.py:95-95
  End this invocation with IngestionResult(config, registry.language.extract(walk)).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from context_graph_sdk.discovery.walker import RepositoryWalk` at source line 22: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py.sudo.md`.
- `from context_graph_sdk.extractors import ExtractionResult, extract_repository` at source line 23: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/extractors/__init__.py.sudo.md`.
- `from context_graph_sdk.plugins import LanguageExtractor, PluginMetadata, PluginPhase, ProjectExtractor` at source line 24: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/plugins/__init__.py.sudo.md`.
- `from context_graph_sdk.project import ProjectConfig, load_project_config` at source line 30: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/project/__init__.py.sudo.md`.
- `from context_graph_sdk.extractors.runtime import SUPPORTED_LANGUAGES` at source line 47: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py.sudo.md`.
