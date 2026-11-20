# vendor/context_graph_sdk/src/context_graph_sdk/plugins/context.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vendor/context_graph_sdk/src/context_graph_sdk/plugins/context.py.evidence.json`. SHA-256: `0f00289407bf15e13493dad0706d9e37d1bd17c224eafd481860b3be840d455a`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/context.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import threading; preserve alias and import-time effects. Then Resolve source import from dataclasses import dataclass; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/context.py:23-28
In source order: Resolve source import from context_graph_sdk.errors import ModelValidationError; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.models import FrozenMap; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.pipeline import PluginDiagnostic, PluginLogLevel; preserve alias and import-time effects. Then Evaluate once 1000; assign in source target order to MAX_PLUGIN_REPORTS. Then Evaluate once 10 * 1024 * 1024; assign in source target order to MAX_SOURCE_READ_BYTES.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/context.py:31-40
interface CancellationToken {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/context.py:32-33
  // Source signature: __init__(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/context.py:33-33
    In source order: Evaluate once threading.Event(); assign in source target order to self._event.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/context.py:36-37
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/context.py:35-35
  Before creating this callable, evaluate and retain decorators top-to-bottom: property.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/context.py:36-37
  // Source signature: is_cancelled(self) -> bool
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn is_cancelled(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/context.py:37-37
    End this invocation with self._event.is_set().
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/context.py:39-40
  // Source signature: cancel(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn cancel(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/context.py:40-40
    In source order: Evaluate self._event.set(); retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/context.py:43-54
interface RepositorySourceReader {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/context.py:44-45
  // Source signature: __init__(self, root: Path) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self, root) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/context.py:45-45
    In source order: Evaluate once root.resolve(); assign in source target order to self._root.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/context.py:47-54
  // Source signature: read_text(self, relative_path: str, max_bytes: int) -> str
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn read_text(self, relative_path, max_bytes) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/context.py:48-49
    if (the source predicate not 0 < max_bytes <= MAX_SOURCE_READ_BYTES is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/context.py:49-49
      Raise ModelValidationError('source read byte limit is outside the approved bound').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/context.py:50-50
    In source order: Evaluate once (self._root / relative_path).resolve(); assign in source target order to candidate.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/context.py:51-52
    if (the source predicate candidate == self._root or self._root not in candidate.parents is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/context.py:52-52
      Raise ModelValidationError('plugin source path escapes the repository').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/context.py:53-54
    Enter source context managers left-to-right: candidate.open('rb') bound to source {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/context.py:54-54
      End this invocation with source.read(max_bytes).decode('utf-8', errors='replace').
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/context.py:58-61
// Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/context.py:57-57
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/context.py:58-61
interface PluginLogRecord {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/context.py:59-61
  In source order: For level, declare without assigning a value; source annotation PluginLogLevel. Then For message, declare without assigning a value; source annotation str. Then For details, declare without assigning a value; source annotation FrozenMap.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/context.py:64-90
interface BufferedPluginReporter {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/context.py:66-68
  // Source signature: __init__(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/context.py:67-68
    In source order: For self._logs, assign []; source annotation list[PluginLogRecord]. Then For self._diagnostics, assign []; source annotation list[PluginDiagnostic].
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/context.py:71-72
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/context.py:70-70
  Before creating this callable, evaluate and retain decorators top-to-bottom: property.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/context.py:71-72
  // Source signature: logs(self) -> tuple[PluginLogRecord, ...]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn logs(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/context.py:72-72
    End this invocation with tuple(self._logs).
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/context.py:75-76
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/context.py:74-74
  Before creating this callable, evaluate and retain decorators top-to-bottom: property.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/context.py:75-76
  // Source signature: diagnostics(self) -> tuple[PluginDiagnostic, ...]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn diagnostics(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/context.py:76-76
    End this invocation with tuple(self._diagnostics).
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/context.py:78-82
  // Source signature: log(self, level: PluginLogLevel, message: str, details: FrozenMap) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn log(self, level, message, details) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/context.py:79-80
    if (the source predicate not message is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/context.py:80-80
      Raise ModelValidationError('plugin log message is required').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/context.py:81-82
    In source order: Evaluate self._reserve(); retain side effects and discard the expression result. Then Evaluate self._logs.append(PluginLogRecord(level, message, details)); retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/context.py:84-86
  // Source signature: diagnostic(self, diagnostic: PluginDiagnostic) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn diagnostic(self, diagnostic) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/context.py:85-86
    In source order: Evaluate self._reserve(); retain side effects and discard the expression result. Then Evaluate self._diagnostics.append(diagnostic); retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/context.py:88-90
  // Source signature: _reserve(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _reserve(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/context.py:89-90
    if (the source predicate len(self._logs) + len(self._diagnostics) >= MAX_PLUGIN_REPORTS is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/context.py:90-90
      Raise ModelValidationError('plugin report count exceeds bound').
    }
    If execution reaches this end, finish with the source implicit None result.
  }
}
```

## Local import links

- `from context_graph_sdk.errors import ModelValidationError` at source line 23: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/errors.py.sudo.md`.
- `from context_graph_sdk.models import FrozenMap` at source line 24: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/models.py.sudo.md`.
- `from context_graph_sdk.pipeline import PluginDiagnostic, PluginLogLevel` at source line 25: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/pipeline/__init__.py.sudo.md`.
