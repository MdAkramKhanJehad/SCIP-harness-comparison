# vendor/context_graph_sdk/src/context_graph_sdk/plugins/base.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vendor/context_graph_sdk/src/context_graph_sdk/plugins/base.py.evidence.json`. SHA-256: `e9ade8d5bf5f9025a1e84a12b6e873cce2f92a5e38eb74368f08fcd574a44d7e`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/base.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from dataclasses import dataclass; preserve alias and import-time effects. Then Resolve source import from enum import StrEnum; preserve alias and import-time effects. Then Resolve source import from typing import TYPE_CHECKING, Protocol, runtime_checkable; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/base.py:23-25
In source order: Resolve source import from context_graph_sdk.errors import ModelValidationError; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.models import CorrelationEdge, GraphMutation; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.pipeline.context import CorrelationContext, IndexContext, PluginContext; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/base.py:27-30
if (the source predicate TYPE_CHECKING is truthy) {
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/base.py:28-30
  In source order: Resolve source import from context_graph_sdk.discovery.walker import RepositoryWalk; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.extractors.records import ExtractionResult; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.project.config import ProjectConfig; preserve alias and import-time effects.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/base.py:33-38
interface PluginPhase {
  Describe the source Python type, preserving its base/metaclass expression order: StrEnum.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/base.py:34-38
  In source order: Evaluate once 'extraction'; assign in source target order to EXTRACTION. Then Evaluate once 'pre_derivation'; assign in source target order to PRE_DERIVATION. Then Evaluate once 'post_derivation'; assign in source target order to POST_DERIVATION. Then Evaluate once 'correlation'; assign in source target order to CORRELATION. Then Evaluate once 'index'; assign in source target order to INDEX.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/base.py:41-41
In source order: Evaluate once {phase: index for index, phase in enumerate(PluginPhase)}; assign in source target order to _PHASE_ORDER.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/base.py:45-57
// Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/base.py:44-44
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/base.py:45-57
interface PluginMetadata {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/base.py:46-49
  In source order: For phase, declare without assigning a value; source annotation PluginPhase. Then For priority, declare without assigning a value; source annotation int. Then For name, declare without assigning a value; source annotation str. Then For version, declare without assigning a value; source annotation str.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/base.py:51-53
  // Source signature: __post_init__(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __post_init__(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/base.py:52-53
    if (the source predicate not self.name or not self.version is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/base.py:53-53
      Raise ModelValidationError('plugin name and version are required').
    }
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/base.py:56-57
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/base.py:55-55
  Before creating this callable, evaluate and retain decorators top-to-bottom: property.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/base.py:56-57
  // Source signature: ordering_key(self) -> tuple[int, int, str]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn ordering_key(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/base.py:57-57
    End this invocation with (_PHASE_ORDER[self.phase], self.priority, self.name).
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/base.py:61-70
// Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/base.py:60-60
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: runtime_checkable.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/base.py:61-70
interface LanguageExtractor {
  Describe the source Python type, preserving its base/metaclass expression order: Protocol.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/base.py:62-62
  In source order: Retain source documentation literal source_literal_62_4; it is not a model call.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/base.py:65-65
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/base.py:64-64
  Before creating this callable, evaluate and retain decorators top-to-bottom: property.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/base.py:65-65
  // Source signature: metadata(self) -> PluginMetadata
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn metadata(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/base.py:65-65
    In source order: Evaluate ...; retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/base.py:68-68
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/base.py:67-67
  Before creating this callable, evaluate and retain decorators top-to-bottom: property.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/base.py:68-68
  // Source signature: languages(self) -> tuple[str, ...]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn languages(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/base.py:68-68
    In source order: Evaluate ...; retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/base.py:70-70
  // Source signature: extract(self, repository: RepositoryWalk) -> ExtractionResult
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn extract(self, repository) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/base.py:70-70
    In source order: Evaluate ...; retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/base.py:74-80
// Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/base.py:73-73
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: runtime_checkable.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/base.py:74-80
interface ProjectExtractor {
  Describe the source Python type, preserving its base/metaclass expression order: Protocol.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/base.py:75-75
  In source order: Retain source documentation literal source_literal_75_4; it is not a model call.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/base.py:78-78
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/base.py:77-77
  Before creating this callable, evaluate and retain decorators top-to-bottom: property.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/base.py:78-78
  // Source signature: metadata(self) -> PluginMetadata
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn metadata(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/base.py:78-78
    In source order: Evaluate ...; retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/base.py:80-80
  // Source signature: extract(self, repository: RepositoryWalk) -> ProjectConfig
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn extract(self, repository) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/base.py:80-80
    In source order: Evaluate ...; retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/base.py:84-90
// Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/base.py:83-83
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: runtime_checkable.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/base.py:84-90
interface GraphEnricher {
  Describe the source Python type, preserving its base/metaclass expression order: Protocol.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/base.py:85-85
  In source order: Retain source documentation literal source_literal_85_4; it is not a model call.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/base.py:88-88
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/base.py:87-87
  Before creating this callable, evaluate and retain decorators top-to-bottom: property.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/base.py:88-88
  // Source signature: metadata(self) -> PluginMetadata
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn metadata(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/base.py:88-88
    In source order: Evaluate ...; retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/base.py:90-90
  // Source signature: enrich(self, context: PluginContext) -> GraphMutation
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn enrich(self, context) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/base.py:90-90
    In source order: Evaluate ...; retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/base.py:94-100
// Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/base.py:93-93
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: runtime_checkable.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/base.py:94-100
interface CorrelationProvider {
  Describe the source Python type, preserving its base/metaclass expression order: Protocol.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/base.py:95-95
  In source order: Retain source documentation literal source_literal_95_4; it is not a model call.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/base.py:98-98
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/base.py:97-97
  Before creating this callable, evaluate and retain decorators top-to-bottom: property.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/base.py:98-98
  // Source signature: metadata(self) -> PluginMetadata
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn metadata(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/base.py:98-98
    In source order: Evaluate ...; retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/base.py:100-100
  // Source signature: correlate(self, context: CorrelationContext) -> tuple[CorrelationEdge, ...]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn correlate(self, context) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/base.py:100-100
    In source order: Evaluate ...; retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/base.py:104-108
// Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/base.py:103-103
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: runtime_checkable.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/base.py:104-108
interface IndexProvider {
  Describe the source Python type, preserving its base/metaclass expression order: Protocol.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/base.py:106-106
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/base.py:105-105
  Before creating this callable, evaluate and retain decorators top-to-bottom: property.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/base.py:106-106
  // Source signature: metadata(self) -> PluginMetadata
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn metadata(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/base.py:106-106
    In source order: Evaluate ...; retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/base.py:108-108
  // Source signature: build(self, context: IndexContext) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn build(self, context) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/plugins/base.py:108-108
    In source order: Evaluate ...; retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
```

## Local import links

- `from context_graph_sdk.errors import ModelValidationError` at source line 23: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/errors.py.sudo.md`.
- `from context_graph_sdk.models import CorrelationEdge, GraphMutation` at source line 24: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/models.py.sudo.md`.
- `from context_graph_sdk.pipeline.context import CorrelationContext, IndexContext, PluginContext` at source line 25: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/pipeline/context.py.sudo.md`.
- `from context_graph_sdk.discovery.walker import RepositoryWalk` at source line 28: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py.sudo.md`.
- `from context_graph_sdk.extractors.records import ExtractionResult` at source line 29: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py.sudo.md`.
- `from context_graph_sdk.project.config import ProjectConfig` at source line 30: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/project/config.py.sudo.md`.
