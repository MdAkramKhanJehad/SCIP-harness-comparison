# vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py.evidence.json`. SHA-256: `294326271a8f1a0844df5f3f4bdf5d407fa61ebbb7e9570936374ea2d3385f97`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:15-28
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import importlib; preserve alias and import-time effects. Then Resolve source import import importlib.metadata; preserve alias and import-time effects. Then Resolve source import import importlib.resources; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:29-33
In source order: Resolve source import import io; preserve alias and import-time effects. Then Resolve source import import os; preserve alias and import-time effects. Then Resolve source import import pickle; preserve alias and import-time effects. Then Resolve source import import queue; preserve alias and import-time effects. Then Resolve source import import subprocess; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:34-38
In source order: Resolve source import import time; preserve alias and import-time effects. Then Resolve source import import warnings; preserve alias and import-time effects. Then Resolve source import from collections.abc import Callable, Sequence; preserve alias and import-time effects. Then Resolve source import from contextlib import suppress; preserve alias and import-time effects. Then Resolve source import from dataclasses import dataclass; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:39-45
In source order: Resolve source import from functools import cache; preserve alias and import-time effects. Then Resolve source import from typing import cast; preserve alias and import-time effects. Then Resolve source import from tree_sitter import Language, Node, Parser, Query, QueryCursor, Tree; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk._process import StdioChannel, spawn_stdio_worker; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.errors import ModelValidationError; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:46-51
In source order: Resolve source import from context_graph_sdk.extractors import records; preserve alias and import-time effects. Then Evaluate once 30.0; assign in source target order to DEFAULT_FILE_TIMEOUT_SECONDS. Then Evaluate once 8; assign in source target order to DEFAULT_MAX_WORKERS. Then Evaluate once 32; assign in source target order to MAX_EXTRACTION_PROCESSES. Then Evaluate once 200000; assign in source target order to MAX_QUERY_MATCHES_PER_FILE.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:52-71
In source order: Evaluate once 10 * 1024 * 1024; assign in source target order to MAX_SOURCE_BYTES. Then Evaluate once 64 * 1024; assign in source target order to MAX_EXTRACTION_REQUEST_BYTES. Then Evaluate once 64 * 1024 * 1024; assign in source target order to MAX_EXTRACTION_RESULT_BYTES. Then Evaluate once 24 * 60 * 60.0; assign in source target order to MAX_AGGREGATE_TIMEOUT_SECONDS. Then Evaluate once {cls.__name__: cls for cls in (records.Assignment, records.Call, records.Delegate, records.FileExtraction, records.Heritage, records.Import, records.ImportBinding, records.Spawn, records.Symbol, records.TypeBinding)}; assign in source target order to _ALLOWED_EXTRACTION_TYPES.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:74-80
interface _ExtractionUnpickler {
  Describe the source Python type, preserving its base/metaclass expression order: pickle.Unpickler.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:75-75
  In source order: Retain source documentation literal source_literal_75_4; it is not a model call.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:77-80
  // Source signature: find_class(self, module: str, name: str) -> object
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn find_class(self, module, name) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:78-79
    if (the source predicate module == records.__name__ and name in _ALLOWED_EXTRACTION_TYPES is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:79-79
      End this invocation with _ALLOWED_EXTRACTION_TYPES[name].
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:80-80
    Raise pickle.UnpicklingError(source_template_80_37).
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:83-89
// Source signature: _load_worker_message(payload: bytes) -> object
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _load_worker_message(payload) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:84-89
  Perform the following protected operations {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:85-85
    End this invocation with _ExtractionUnpickler(io.BytesIO(payload)).load().
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:86-87
  On the first matching source exception pickle.PickleError, in handler order {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:87-87
    Raise the currently handled exception.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:88-89
  On the first matching source exception Exception as error, in handler order {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:89-89
    Raise pickle.UnpicklingError('invalid extraction result payload') with explicit source cause error.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:93-99
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:92-92
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:93-99
interface LanguageRuntimeSpec {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:94-98
  In source order: For name, declare without assigning a value; source annotation str. Then For distribution, declare without assigning a value; source annotation str. Then For module, declare without assigning a value; source annotation str. Then For entry, declare without assigning a value; source annotation str. Then For query_asset, declare without assigning a value; source annotation str.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:99-99
  In source order: For entry_arguments, assign (); source annotation tuple[str, ...].
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:103-163
In source order: For SUPPORTED_LANGUAGES, assign {spec.name: spec for spec in (LanguageRuntimeSpec('go', 'tree-sitter-go', 'tree_sitter_go', 'language', 'go.scm'), LanguageRuntimeSpec('python', 'tree-sitter-python', 'tree_sitter_python', 'language', 'python.scm'), LanguageRuntimeSpec('javascript', 'tree-sitter-javascript', 'tree_sitter_javascript', 'language', 'javascript.scm'), LanguageRuntimeSpec('typescript', 'tree-sitter-typescript', 'tree_sitter_typescript', 'language_typescript', 'typescript.scm'), LanguageRuntimeSpec('tsx', 'tree-sitter-typescript', 'tree_sitter_typescript', 'language_tsx', 'typescript.scm'), LanguageRuntimeSpec('java', 'tree-sitter-java', 'tree_sitter_java', 'language', 'java.scm'), LanguageRuntimeSpec('kotlin', 'tree-sitter-language-pack', 'tree_sitter_language_pack', 'get_language', 'kotlin.scm', ('kotlin',)), LanguageRuntimeSpec('csharp', 'tree-sitter-c-sharp', 'tree_sitter_c_sharp', 'language', 'csharp.scm'), LanguageRuntimeSpec('scala', 'tree-sitter-scala', 'tree_sitter_scala', 'language', 'scala.scm'), LanguageRuntimeSpec('c', 'tree-sitter-c', 'tree_sitter_c', 'language', 'c.scm'), LanguageRuntimeSpec('cpp', 'tree-sitter-cpp', 'tree_sitter_cpp', 'language', 'cpp.scm'), LanguageRuntimeSpec('rust', 'tree-sitter-rust', 'tree_sitter_rust', 'language', 'rust.scm'), LanguageRuntimeSpec('ruby', 'tree-sitter-ruby', 'tree_sitter_ruby', 'language', 'ruby.scm'), LanguageRuntimeSpec('php', 'tree-sitter-php', 'tree_sitter_php', 'language_php', 'php.scm'), LanguageRuntimeSpec('swift', 'tree-sitter-swift', 'tree_sitter_swift', 'language', 'swift.scm'), LanguageRuntimeSpec('dart', 'tree-sitter-dart', 'tree_sitter_dart', 'language', 'dart.scm'), LanguageRuntimeSpec('solidity', 'tree-sitter-solidity', 'tree_sitter_solidity', 'language', 'solidity.scm'))}; source annotation dict[str, LanguageRuntimeSpec].
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:166-167
// Source signature: is_supported_language(name: str) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn is_supported_language(name) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:167-167
  End this invocation with name in SUPPORTED_LANGUAGES.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:171-183
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:170-170
Before creating this callable, evaluate and retain decorators top-to-bottom: cache.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:171-183
// Source signature: load_language(name: str) -> Language
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn load_language(name) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:172-174
  In source order: Evaluate once SUPPORTED_LANGUAGES[name]; assign in source target order to spec. Then Evaluate once importlib.import_module(spec.module); assign in source target order to module. Then For obtained, assign getattr(module, spec.entry)(*spec.entry_arguments); source annotation object.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:175-177
  if (the source predicate isinstance(obtained, Language) is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:177-177
    End this invocation with obtained.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:178-182
  if (the source predicate isinstance(obtained, int) is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:180-182
    Enter source context managers left-to-right: warnings.catch_warnings() {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:181-181
      In source order: Evaluate warnings.simplefilter('ignore', DeprecationWarning); retain side effects and discard the expression result.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:182-182
      End this invocation with Language(obtained).
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:183-183
  End this invocation with Language(obtained).
  If execution reaches this end, finish with the source implicit None result.
}
At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:187-190
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:186-186
Before creating this callable, evaluate and retain decorators top-to-bottom: cache.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:187-190
// Source signature: query_text(name: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn query_text(name) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:188-189
  In source order: Evaluate once SUPPORTED_LANGUAGES[name].query_asset; assign in source target order to asset. Then Evaluate once importlib.resources.files('context_graph_sdk.extractors') / 'queries' / asset; assign in source target order to resource.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:190-190
  End this invocation with resource.read_text(encoding='utf-8').
  If execution reaches this end, finish with the source implicit None result.
}
At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:194-195
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:193-193
Before creating this callable, evaluate and retain decorators top-to-bottom: cache.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:194-195
// Source signature: load_query(name: str) -> Query
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn load_query(name) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:195-195
  End this invocation with Query(load_language(name), query_text(name)).
  If execution reaches this end, finish with the source implicit None result.
}
At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:198-205
// Source signature: analysis_components() -> tuple[tuple[str, str], ...]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn analysis_components() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:199-202
  In source order: Retain source documentation literal source_literal_199_4; it is not a model call. Then Evaluate once sorted({spec.distribution for spec in SUPPORTED_LANGUAGES.values()} | {'tree-sitter'}); assign in source target order to distributions.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:203-205
  End this invocation with tuple(((distribution, importlib.metadata.version(distribution)) for distribution in distributions)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:208-208
In source order: Evaluate once list[tuple[int, dict[str, list[Node]]]]; assign in source target order to QueryMatches.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:211-222
// Source signature: parse_and_match(name: str, source: bytes) -> tuple[Tree, QueryMatches]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn parse_and_match(name, source) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:212-212
  In source order: Retain source documentation literal source_literal_212_4; it is not a model call.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:213-214
  if (the source predicate len(source) > MAX_SOURCE_BYTES is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:214-214
    Raise ModelValidationError('source exceeds the extraction size bound').
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:215-217
  In source order: Evaluate once Parser(load_language(name)).parse(source); assign in source target order to tree. Then Evaluate once QueryCursor(load_query(name)); assign in source target order to cursor. Then Evaluate once cursor.matches(tree.root_node); assign in source target order to matches.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:218-221
  if (the source predicate len(matches) > MAX_QUERY_MATCHES_PER_FILE is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:219-221
    Raise ModelValidationError(source_template_220_12).
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:222-222
  End this invocation with (tree, matches).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:226-228
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:225-225
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:226-228
interface WorkItem {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:227-228
  In source order: For relative_path, declare without assigning a value; source annotation str. Then For language, declare without assigning a value; source annotation str.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:232-236
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:231-231
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:232-236
interface _ActiveWorker {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:233-236
  In source order: For process, declare without assigning a value; source annotation subprocess.Popen[bytes]. Then For channel, declare without assigning a value; source annotation StdioChannel. Then For index, assign None; source annotation int | None. Then For started_at, assign 0.0; source annotation float.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:239-444
// Source signature: run_bounded(root: str, items: Sequence[WorkItem], *, max_workers: int=DEFAULT_MAX_WORKERS, file_timeout_seconds: float=DEFAULT_FILE_TIMEOUT_SECONDS, aggregate_timeout_seconds: float | None=None, max_result_bytes: int=MAX_EXTRACTION_RESULT_BYTES, worker_module: str='context_graph_sdk.extractors.worker_entry', on_progress: Callable[[int, int], None] | None=None) -> tuple[list[tuple[WorkItem, object]], list[tuple[WorkItem, str]]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn run_bounded(root, items, max_workers, file_timeout_seconds, aggregate_timeout_seconds, max_result_bytes, worker_module, on_progress) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:250-250
  In source order: Retain source documentation literal source_literal_250_4; it is not a model call.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:251-252
  if (the source predicate not 1 <= max_workers <= MAX_EXTRACTION_PROCESSES is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:252-252
    Raise ModelValidationError(source_template_252_35).
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:253-254
  if (the source predicate not 0 < file_timeout_seconds <= 3600 is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:254-254
    Raise ModelValidationError('file_timeout_seconds must be in (0, 3600]').
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:255-258
  if (the source predicate not 1 <= max_result_bytes <= MAX_EXTRACTION_RESULT_BYTES is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:256-258
    Raise ModelValidationError(source_template_257_12).
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:259-260
  if (the source predicate not worker_module is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:260-260
    Raise ModelValidationError('worker_module is required').
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:261-265
  if (the source predicate aggregate_timeout_seconds is None is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:262-265
    In source order: Evaluate once min(MAX_AGGREGATE_TIMEOUT_SECONDS, file_timeout_seconds * max(1, (len(items) + max_workers - 1) // max_workers) + 5.0); assign in source target order to aggregate_timeout_seconds.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:266-269
  if (the source predicate not 0 < aggregate_timeout_seconds <= MAX_AGGREGATE_TIMEOUT_SECONDS is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:267-269
    Raise ModelValidationError(source_template_268_12).
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:270-272
  if (the source predicate not items is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:271-271
    In source order: Evaluate _report_progress(on_progress, 0, 0); retain side effects and discard the expression result.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:272-272
    End this invocation with ([], []).
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:274-278
  In source order: Evaluate once min(max_workers, os.cpu_count() or 1, len(items)); assign in source target order to worker_limit. Then For ready, assign queue.Queue(); source annotation queue.Queue[StdioChannel]. Then For workers, assign {}; source annotation dict[StdioChannel, _ActiveWorker]. Then For outcomes, assign {}; source annotation dict[int, tuple[bool, object]]. Then Evaluate once 0; assign in source target order to next_index.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:279-281
  In source order: Evaluate once time.monotonic() + aggregate_timeout_seconds; assign in source target order to aggregate_deadline. Then Evaluate once max(1, (len(items) + 199) // 200); assign in source target order to progress_interval. Then Evaluate once 0; assign in source target order to last_progress.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:283-288
  // Source signature: report_progress(*, force: bool=False) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn report_progress(force) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:284-285
    In source order: Bind names in enclosing nonlocal scope: last_progress. Then Evaluate once len(outcomes); assign in source target order to completed.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:286-288
    if (the source predicate force or completed == len(items) or completed - last_progress >= progress_interval is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:287-288
      In source order: Evaluate _report_progress(on_progress, completed, len(items)); retain side effects and discard the expression result. Then Evaluate once completed; assign in source target order to last_progress.
    }
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:290-290
  In source order: Evaluate report_progress(force=True); retain side effects and discard the expression result.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:292-311
  // Source signature: stop(worker: _ActiveWorker, *, graceful: bool) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn stop(worker, graceful) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:293-293
    In source order: Evaluate workers.pop(worker.channel, None); retain side effects and discard the expression result.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:294-298
    if (the source predicate graceful and worker.process.poll() is None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:295-296
      Enter source context managers left-to-right: suppress(OSError) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:296-296
        In source order: Evaluate worker.channel.send_bytes(b''); retain side effects and discard the expression result.
      }
      Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:297-298
      Enter source context managers left-to-right: suppress(subprocess.TimeoutExpired) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:298-298
        In source order: Evaluate worker.process.wait(1.0); retain side effects and discard the expression result.
      }
      Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:299-310
    if (the source predicate worker.process.poll() is None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:300-300
      In source order: Evaluate worker.process.terminate(); retain side effects and discard the expression result.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:301-310
      Perform the following protected operations {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:302-302
        In source order: Evaluate worker.process.wait(1.0); retain side effects and discard the expression result.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:303-310
      On the first matching source exception subprocess.TimeoutExpired, in handler order {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:304-304
        In source order: Evaluate worker.process.kill(); retain side effects and discard the expression result.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:305-310
        Perform the following protected operations {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:306-306
          In source order: Evaluate worker.process.wait(1.0); retain side effects and discard the expression result.
        }
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:307-310
        On the first matching source exception subprocess.TimeoutExpired as error, in handler order {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:308-310
          Raise ModelValidationError('extraction worker could not be terminated') with explicit source cause error.
        }
      }
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:311-311
    In source order: Evaluate worker.channel.close(); retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:313-324
  // Source signature: spawn() -> _ActiveWorker
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn spawn() {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:314-323
    In source order: Evaluate once spawn_stdio_worker(worker_module, root, str(MAX_EXTRACTION_REQUEST_BYTES), str(max_result_bytes), maximum_response_bytes=max_result_bytes, on_response=ready.put); assign in source target order to (process, channel). Then Evaluate once _ActiveWorker(process, channel); assign in source target order to worker. Then Evaluate once worker; assign in source target order to workers[channel].
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:324-324
    End this invocation with worker.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:326-335
  // Source signature: dispatch(worker: _ActiveWorker, index: int) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn dispatch(worker, index) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:327-330
    In source order: Evaluate once items[index]; assign in source target order to item. Then Evaluate once pickle.dumps((index, item.relative_path, item.language), protocol=pickle.HIGHEST_PROTOCOL); assign in source target order to payload.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:331-332
    if (the source predicate len(payload) > MAX_EXTRACTION_REQUEST_BYTES is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:332-332
      Raise ModelValidationError('extraction request exceeds IPC bound').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:333-335
    In source order: Evaluate worker.channel.send_bytes(payload); retain side effects and discard the expression result. Then Evaluate once index; assign in source target order to worker.index. Then Evaluate once time.monotonic(); assign in source target order to worker.started_at.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:337-343
  // Source signature: replace_if_needed() -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn replace_if_needed() {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:338-338
    In source order: Bind names in enclosing nonlocal scope: next_index.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:339-340
    if (the source predicate next_index >= len(items) is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:340-340
      End this invocation with None.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:341-343
    In source order: Evaluate once spawn(); assign in source target order to worker. Then Evaluate dispatch(worker, next_index); retain side effects and discard the expression result. Then Apply source augmented assignment next_index += 1 with source evaluation/in-place semantics.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:345-346
  for each _ in range(worker_limit) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:346-346
    In source order: Evaluate replace_if_needed(); retain side effects and discard the expression result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:348-349
  In source order: Evaluate once False; assign in source target order to completed_normally. Then For primary_failure, assign None; source annotation BaseException | None.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:350-434
  Perform the following protected operations {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:351-421
    while (the source predicate len(outcomes) < len(items) is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:352-352
      In source order: Evaluate once time.monotonic(); assign in source target order to now.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:353-364
      if (the source predicate now >= aggregate_deadline is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:354-360
        for each worker in list(workers.values()) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:355-359
          if (the source predicate worker.index is not None is truthy) {
            // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:356-359
            In source order: Evaluate once (False, 'extraction exceeded the aggregate time bound'); assign in source target order to outcomes[worker.index].
          }
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:360-360
          In source order: Evaluate stop(worker, graceful=False); retain side effects and discard the expression result.
        }
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:361-362
        for each index in range(next_index, len(items)) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:362-362
          In source order: Evaluate once (False, 'extraction exceeded the aggregate time bound'); assign in source target order to outcomes[index].
        }
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:363-363
        In source order: Evaluate report_progress(force=True); retain side effects and discard the expression result.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:364-364
        Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:366-366
      In source order: Evaluate once [worker for worker in workers.values() if worker.index is not None]; assign in source target order to busy.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:367-368
      if (the source predicate not busy is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:368-368
        Raise ModelValidationError('extraction worker pool stopped before completion').
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:369-372
      In source order: Evaluate once min(aggregate_deadline, *(worker.started_at + file_timeout_seconds for worker in busy)); assign in source target order to nearest_deadline.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:373-376
      Perform the following protected operations {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:374-374
        In source order: Evaluate once ready.get(timeout=max(0.0, nearest_deadline - now)); assign in source target order to channel.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:375-376
      On the first matching source exception queue.Empty, in handler order {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:376-376
        In source order: Evaluate once None; assign in source target order to channel.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:377-377
      In source order: Evaluate once workers.get(channel) if channel is not None else None; assign in source target order to worker.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:378-412
      if (the source predicate worker is not None and worker.index is not None is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:379-379
        In source order: Evaluate once worker.index; assign in source target order to index.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:380-412
        Perform the following protected operations {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:381-382
          In source order: Evaluate once worker.channel.recv_bytes(max_result_bytes); assign in source target order to payload. Then Evaluate once _load_worker_message(payload); assign in source target order to decoded.
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:383-384
          if (the source predicate not isinstance(decoded, tuple) is truthy) {
            // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:384-384
            Raise ValueError('invalid result shape').
          }
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:385-385
          In source order: Evaluate once cast(tuple[object, ...], decoded); assign in source target order to message.
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:386-387
          if (the source predicate len(message) != 3 or message[0] != index or (not isinstance(message[1], bool)) is truthy) {
            // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:387-387
            Raise ValueError('invalid result shape').
          }
        }
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:388-400
        On the first matching source exception EOFError, in handler order {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:389-390
          Enter source context managers left-to-right: suppress(subprocess.TimeoutExpired) {
            // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:390-390
            In source order: Evaluate worker.process.wait(0.2); retain side effects and discard the expression result.
          }
          Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:391-399
          In source order: Evaluate once worker.process.returncode; assign in source target order to exit_code. Then Evaluate once source_template_393_24 if exit_code is not None else 'extraction worker closed its response stream without exiting'; assign in source target order to reason. Then Evaluate once (False, reason); assign in source target order to outcomes[index]. Then Evaluate report_progress(); retain side effects and discard the expression result. Then Evaluate stop(worker, graceful=False); retain side effects and discard the expression result.
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:400-400
          In source order: Evaluate replace_if_needed(); retain side effects and discard the expression result.
        }
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:401-405
        On the first matching source exception (OSError, ValueError, pickle.PickleError) as error, in handler order {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:402-405
          In source order: Evaluate once (False, source_template_402_46); assign in source target order to outcomes[index]. Then Evaluate report_progress(); retain side effects and discard the expression result. Then Evaluate stop(worker, graceful=False); retain side effects and discard the expression result. Then Evaluate replace_if_needed(); retain side effects and discard the expression result.
        }
        Only when the protected body falls through normally, without exception, return, break or continue {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:407-409
          In source order: Evaluate once (message[1], message[2]); assign in source target order to outcomes[index]. Then Evaluate report_progress(); retain side effects and discard the expression result. Then Evaluate once None; assign in source target order to worker.index.
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:410-412
          if (the source predicate next_index < len(items) is truthy) {
            // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:411-412
            In source order: Evaluate dispatch(worker, next_index); retain side effects and discard the expression result. Then Apply source augmented assignment next_index += 1 with source evaluation/in-place semantics.
          }
        }
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:414-414
      In source order: Evaluate once time.monotonic(); assign in source target order to now.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:415-421
      for each worker in list(workers.values()) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:416-417
        if (the source predicate worker.index is None or now < worker.started_at + file_timeout_seconds is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:417-417
          Continue the immediately enclosing source loop at its next iteration.
        }
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:418-421
        In source order: Evaluate once (False, 'extraction exceeded the per-file time bound'); assign in source target order to outcomes[worker.index]. Then Evaluate report_progress(); retain side effects and discard the expression result. Then Evaluate stop(worker, graceful=False); retain side effects and discard the expression result. Then Evaluate replace_if_needed(); retain side effects and discard the expression result.
      }
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:422-422
    In source order: Evaluate once True; assign in source target order to completed_normally.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:423-425
  On the first matching source exception BaseException as error, in handler order {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:424-424
    In source order: Evaluate once error; assign in source target order to primary_failure.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:425-425
    Raise the currently handled exception.
  }
  On every exit from this protected/handler/normal-completion region {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:427-427
    In source order: For cleanup_failure, assign None; source annotation Exception | None.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:428-432
    for each worker in list(workers.values()) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:429-432
      Perform the following protected operations {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:430-430
        In source order: Evaluate stop(worker, graceful=completed_normally); retain side effects and discard the expression result.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:431-432
      On the first matching source exception Exception as error, in handler order {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:432-432
        In source order: Evaluate once cleanup_failure or error; assign in source target order to cleanup_failure.
      }
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:433-434
    if (the source predicate cleanup_failure is not None and primary_failure is None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:434-434
      Raise cleanup_failure.
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:436-437
  In source order: For successes, assign []; source annotation list[tuple[WorkItem, object]]. Then For failures, assign []; source annotation list[tuple[WorkItem, str]].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:438-443
  for each (index, item) in enumerate(items) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:439-439
    In source order: Evaluate once outcomes[index]; assign in source target order to (ok, value).
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:440-443
    if (the source predicate ok is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:441-441
      In source order: Evaluate successes.append((item, value)); retain side effects and discard the expression result.
    }
    else {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:443-443
      In source order: Evaluate failures.append((item, str(value))); retain side effects and discard the expression result.
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:444-444
  End this invocation with (successes, failures).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:447-454
// Source signature: _report_progress(callback: Callable[[int, int], None] | None, completed: int, total: int) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _report_progress(callback, completed, total) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:450-451
  if (the source predicate callback is None is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:451-451
    End this invocation with None.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:453-454
  Enter source context managers left-to-right: suppress(Exception) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py:454-454
    In source order: Evaluate callback(completed, total); retain side effects and discard the expression result.
  }
  Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from context_graph_sdk._process import StdioChannel, spawn_stdio_worker` at source line 44: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/_process.py.sudo.md`.
- `from context_graph_sdk.errors import ModelValidationError` at source line 45: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/errors.py.sudo.md`.
- `from context_graph_sdk.extractors import records` at source line 46: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/extractors/__init__.py.sudo.md`.
- `from context_graph_sdk.extractors import records` at source line 46: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../../../prompt_representation/vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py.sudo.md). Exact strings in the evidence asset support this conversion.
