# vendor/context_graph_sdk/src/context_graph_sdk/pipeline/context.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vendor/context_graph_sdk/src/context_graph_sdk/pipeline/context.py.evidence.json`. SHA-256: `f5ab4bec54a5699cce3b55ac05d540936bc5f6b8c68118dd6eb71fe2f064e4c5`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/pipeline/context.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from dataclasses import dataclass; preserve alias and import-time effects. Then Resolve source import from enum import StrEnum; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/pipeline/context.py:22-31
In source order: Resolve source import from typing import Protocol, runtime_checkable; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.errors import ModelValidationError; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.models import FrozenMap, GraphSnapshot, ProjectMetadata, ProjectSnapshot, SnapshotLocator; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/pipeline/context.py:35-36
// Source: vendor/context_graph_sdk/src/context_graph_sdk/pipeline/context.py:34-34
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: runtime_checkable.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/pipeline/context.py:35-36
interface SourceReader {
  Describe the source Python type, preserving its base/metaclass expression order: Protocol.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/pipeline/context.py:36-36
  // Source signature: read_text(self, relative_path: str, max_bytes: int) -> str
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn read_text(self, relative_path, max_bytes) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/pipeline/context.py:36-36
    In source order: Evaluate ...; retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/pipeline/context.py:40-42
// Source: vendor/context_graph_sdk/src/context_graph_sdk/pipeline/context.py:39-39
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: runtime_checkable.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/pipeline/context.py:40-42
interface CancellationState {
  Describe the source Python type, preserving its base/metaclass expression order: Protocol.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/pipeline/context.py:42-42
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/pipeline/context.py:41-41
  Before creating this callable, evaluate and retain decorators top-to-bottom: property.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/pipeline/context.py:42-42
  // Source signature: is_cancelled(self) -> bool
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn is_cancelled(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/pipeline/context.py:42-42
    In source order: Evaluate ...; retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/pipeline/context.py:46-55
// Source: vendor/context_graph_sdk/src/context_graph_sdk/pipeline/context.py:45-45
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: runtime_checkable.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/pipeline/context.py:46-55
interface AcceptedGraphReader {
  Describe the source Python type, preserving its base/metaclass expression order: Protocol.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/pipeline/context.py:47-47
  In source order: Retain source documentation literal source_literal_47_4; it is not a model call.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/pipeline/context.py:49-55
  // Source signature: query(self, locator: SnapshotLocator, cypher: str, parameters: FrozenMap, row_limit: int) -> tuple[FrozenMap, ...]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn query(self, locator, cypher, parameters, row_limit) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/pipeline/context.py:55-55
    In source order: Evaluate ...; retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/pipeline/context.py:58-62
interface PluginLogLevel {
  Describe the source Python type, preserving its base/metaclass expression order: StrEnum.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/pipeline/context.py:59-62
  In source order: Evaluate once 'debug'; assign in source target order to DEBUG. Then Evaluate once 'info'; assign in source target order to INFO. Then Evaluate once 'warning'; assign in source target order to WARNING. Then Evaluate once 'error'; assign in source target order to ERROR.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/pipeline/context.py:66-76
// Source: vendor/context_graph_sdk/src/context_graph_sdk/pipeline/context.py:65-65
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/pipeline/context.py:66-76
interface PluginDiagnostic {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/pipeline/context.py:67-70
  In source order: For code, declare without assigning a value; source annotation str. Then For message, declare without assigning a value; source annotation str. Then For path, assign None; source annotation str | None. Then For line, assign None; source annotation int | None.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/pipeline/context.py:72-76
  // Source signature: __post_init__(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __post_init__(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/pipeline/context.py:73-74
    if (the source predicate not self.code or not self.message is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/pipeline/context.py:74-74
      Raise ModelValidationError('diagnostic code and message are required').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/pipeline/context.py:75-76
    if (the source predicate self.line is not None and self.line <= 0 is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/pipeline/context.py:76-76
      Raise ModelValidationError('diagnostic line must be positive').
    }
    If execution reaches this end, finish with the source implicit None result.
  }
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/pipeline/context.py:80-83
// Source: vendor/context_graph_sdk/src/context_graph_sdk/pipeline/context.py:79-79
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: runtime_checkable.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/pipeline/context.py:80-83
interface PluginReporter {
  Describe the source Python type, preserving its base/metaclass expression order: Protocol.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/pipeline/context.py:81-81
  // Source signature: log(self, level: PluginLogLevel, message: str, details: FrozenMap) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn log(self, level, message, details) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/pipeline/context.py:81-81
    In source order: Evaluate ...; retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/pipeline/context.py:83-83
  // Source signature: diagnostic(self, diagnostic: PluginDiagnostic) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn diagnostic(self, diagnostic) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/pipeline/context.py:83-83
    In source order: Evaluate ...; retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/pipeline/context.py:87-94
// Source: vendor/context_graph_sdk/src/context_graph_sdk/pipeline/context.py:86-86
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/pipeline/context.py:87-94
interface PluginContext {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/pipeline/context.py:88-92
  In source order: For project, declare without assigning a value; source annotation ProjectMetadata. Then For graph, declare without assigning a value; source annotation GraphSnapshot. Then For source_reader, declare without assigning a value; source annotation SourceReader. Then For reporter, declare without assigning a value; source annotation PluginReporter. Then For cancellation, declare without assigning a value; source annotation CancellationState.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/pipeline/context.py:93-94
  In source order: For configuration, declare without assigning a value; source annotation FrozenMap. Then For deadline_monotonic, declare without assigning a value; source annotation float.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/pipeline/context.py:98-105
// Source: vendor/context_graph_sdk/src/context_graph_sdk/pipeline/context.py:97-97
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/pipeline/context.py:98-105
interface CorrelationContext {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/pipeline/context.py:99-103
  In source order: For candidate, declare without assigning a value; source annotation GraphSnapshot. Then For accepted, declare without assigning a value; source annotation tuple[ProjectSnapshot, ...]. Then For graph_reader, declare without assigning a value; source annotation AcceptedGraphReader. Then For reporter, declare without assigning a value; source annotation PluginReporter. Then For configuration, declare without assigning a value; source annotation FrozenMap.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/pipeline/context.py:104-105
  In source order: For cancellation, declare without assigning a value; source annotation CancellationState. Then For deadline_monotonic, declare without assigning a value; source annotation float.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/pipeline/context.py:109-119
// Source: vendor/context_graph_sdk/src/context_graph_sdk/pipeline/context.py:108-108
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/pipeline/context.py:109-119
interface IndexContext {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/pipeline/context.py:110-114
  In source order: For snapshot, declare without assigning a value; source annotation ProjectSnapshot. Then For locator, declare without assigning a value; source annotation SnapshotLocator. Then For artifact_path, declare without assigning a value; source annotation Path. Then For graph_fingerprint, declare without assigning a value; source annotation str. Then For graph_reader, declare without assigning a value; source annotation AcceptedGraphReader.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/pipeline/context.py:115-119
  In source order: For source_reader, declare without assigning a value; source annotation SourceReader. Then For reporter, declare without assigning a value; source annotation PluginReporter. Then For configuration, declare without assigning a value; source annotation FrozenMap. Then For cancellation, declare without assigning a value; source annotation CancellationState. Then For deadline_monotonic, declare without assigning a value; source annotation float.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
```

## Local import links

- `from context_graph_sdk.errors import ModelValidationError` at source line 24: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/errors.py.sudo.md`.
- `from context_graph_sdk.models import FrozenMap, GraphSnapshot, ProjectMetadata, ProjectSnapshot, SnapshotLocator` at source line 25: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/models.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../../../prompt_representation/vendor/context_graph_sdk/src/context_graph_sdk/pipeline/context.py.sudo.md). Exact strings in the evidence asset support this conversion.
