# vendor/context_graph_sdk/src/context_graph_sdk/progress.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vendor/context_graph_sdk/src/context_graph_sdk/progress.py.evidence.json`. SHA-256: `460e2f0ba23199fc7ffd6c3661ce2e37cad1ae9b2d2d19d71a70a9e0e50b6336`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/progress.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from collections.abc import Callable; preserve alias and import-time effects. Then Resolve source import from dataclasses import dataclass; preserve alias and import-time effects. Then Resolve source import from enum import StrEnum; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/progress.py:22-24
In source order: Resolve source import from typing import TypeAlias; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.errors import ModelValidationError; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/progress.py:27-35
interface AnalysisPhase {
  Describe the source Python type, preserving its base/metaclass expression order: StrEnum.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/progress.py:28-32
  In source order: Evaluate once 'discovery'; assign in source target order to DISCOVERY. Then Evaluate once 'configuration'; assign in source target order to CONFIGURATION. Then Evaluate once 'extraction'; assign in source target order to EXTRACTION. Then Evaluate once 'resolution'; assign in source target order to RESOLUTION. Then Evaluate once 'graph_build'; assign in source target order to GRAPH_BUILD.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/progress.py:33-35
  In source order: Evaluate once 'derivation'; assign in source target order to DERIVATION. Then Evaluate once 'correlation'; assign in source target order to CORRELATION. Then Evaluate once 'publication'; assign in source target order to PUBLICATION.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/progress.py:39-60
// Source: vendor/context_graph_sdk/src/context_graph_sdk/progress.py:38-38
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/progress.py:39-60
interface AnalysisProgress {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/progress.py:40-44
  In source order: For phase, declare without assigning a value; source annotation AnalysisPhase. Then For message, declare without assigning a value; source annotation str. Then For step, declare without assigning a value; source annotation int. Then For step_count, declare without assigning a value; source annotation int. Then For completed, assign None; source annotation int | None.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/progress.py:45-46
  In source order: For total, assign None; source annotation int | None. Then For finished, assign False; source annotation bool.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/progress.py:48-60
  // Source signature: __post_init__(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __post_init__(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/progress.py:49-50
    if (the source predicate not self.message is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/progress.py:50-50
      Raise ModelValidationError('analysis progress message is required').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/progress.py:51-52
    if (the source predicate not 1 <= self.step <= self.step_count is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/progress.py:52-52
      Raise ModelValidationError('analysis progress step is outside the pipeline').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/progress.py:53-54
    if (the source predicate (self.completed is None) != (self.total is None) is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/progress.py:54-54
      Raise ModelValidationError('analysis progress item counts must be paired').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/progress.py:55-60
    if (the source predicate self.completed is not None and self.total is not None and (self.total < 0 or not 0 <= self.completed <= self.total) is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/progress.py:60-60
      Raise ModelValidationError('analysis progress item counts are invalid').
    }
    If execution reaches this end, finish with the source implicit None result.
  }
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/progress.py:63-63
In source order: For AnalysisProgressCallback, assign Callable[[AnalysisProgress], None]; source annotation TypeAlias.
```

## Local import links

- `from context_graph_sdk.errors import ModelValidationError` at source line 24: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/errors.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../../prompt_representation/vendor/context_graph_sdk/src/context_graph_sdk/progress.py.sudo.md). Exact strings in the evidence asset support this conversion.
