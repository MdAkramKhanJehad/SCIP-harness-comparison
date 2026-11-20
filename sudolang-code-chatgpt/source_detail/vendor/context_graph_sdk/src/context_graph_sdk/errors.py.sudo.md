# vendor/context_graph_sdk/src/context_graph_sdk/errors.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vendor/context_graph_sdk/src/context_graph_sdk/errors.py.evidence.json`. SHA-256: `7052924c47a2d4da2895a967c9491700418e2e49ae681d04601e51d932e41164`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/errors.py:15-17
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/errors.py:20-21
interface ContextGraphError {
  Describe the source Python type, preserving its base/metaclass expression order: Exception.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/errors.py:21-21
  In source order: Retain source documentation literal source_literal_21_4; it is not a model call.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/errors.py:24-25
interface ModelValidationError {
  Describe the source Python type, preserving its base/metaclass expression order: ContextGraphError, ValueError.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/errors.py:25-25
  In source order: Retain source documentation literal source_literal_25_4; it is not a model call.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/errors.py:28-29
interface ResolutionLimitError {
  Describe the source Python type, preserving its base/metaclass expression order: ContextGraphError.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/errors.py:29-29
  In source order: Retain source documentation literal source_literal_29_4; it is not a model call.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/errors.py:32-33
interface LifecycleError {
  Describe the source Python type, preserving its base/metaclass expression order: ContextGraphError.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/errors.py:33-33
  In source order: Retain source documentation literal source_literal_33_4; it is not a model call.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/errors.py:36-37
interface WorkspaceClosedError {
  Describe the source Python type, preserving its base/metaclass expression order: LifecycleError.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/errors.py:37-37
  In source order: Retain source documentation literal source_literal_37_4; it is not a model call.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/errors.py:40-41
interface WorkspaceLockedError {
  Describe the source Python type, preserving its base/metaclass expression order: LifecycleError.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/errors.py:41-41
  In source order: Retain source documentation literal source_literal_41_4; it is not a model call.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/errors.py:44-45
interface SnapshotLifecycleError {
  Describe the source Python type, preserving its base/metaclass expression order: LifecycleError.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/errors.py:45-45
  In source order: Retain source documentation literal source_literal_45_4; it is not a model call.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/errors.py:48-49
interface DiscoveryError {
  Describe the source Python type, preserving its base/metaclass expression order: ContextGraphError.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/errors.py:49-49
  In source order: Retain source documentation literal source_literal_49_4; it is not a model call.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/errors.py:52-53
interface QueryError {
  Describe the source Python type, preserving its base/metaclass expression order: ContextGraphError.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/errors.py:53-53
  In source order: Retain source documentation literal source_literal_53_4; it is not a model call.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/errors.py:56-57
interface QueryValidationError {
  Describe the source Python type, preserving its base/metaclass expression order: QueryError.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/errors.py:57-57
  In source order: Retain source documentation literal source_literal_57_4; it is not a model call.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/errors.py:60-61
interface QueryTimeoutError {
  Describe the source Python type, preserving its base/metaclass expression order: QueryError.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/errors.py:61-61
  In source order: Retain source documentation literal source_literal_61_4; it is not a model call.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/errors.py:64-65
interface QueryCancelledError {
  Describe the source Python type, preserving its base/metaclass expression order: QueryError.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/errors.py:65-65
  In source order: Retain source documentation literal source_literal_65_4; it is not a model call.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/errors.py:68-69
interface QueryResourceLimitError {
  Describe the source Python type, preserving its base/metaclass expression order: QueryError.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/errors.py:69-69
  In source order: Retain source documentation literal source_literal_69_4; it is not a model call.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/errors.py:72-73
interface QueryWorkerError {
  Describe the source Python type, preserving its base/metaclass expression order: QueryError.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/errors.py:73-73
  In source order: Retain source documentation literal source_literal_73_4; it is not a model call.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/errors.py:76-77
interface QueryProtocolError {
  Describe the source Python type, preserving its base/metaclass expression order: QueryError.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/errors.py:77-77
  In source order: Retain source documentation literal source_literal_77_4; it is not a model call.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/errors.py:80-81
interface StructuredQueryError {
  Describe the source Python type, preserving its base/metaclass expression order: QueryError.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/errors.py:81-81
  In source order: Retain source documentation literal source_literal_81_4; it is not a model call.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/errors.py:84-87
interface SymbolNotFoundError {
  Describe the source Python type, preserving its base/metaclass expression order: StructuredQueryError.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/errors.py:85-87
  // Source signature: __init__(self, selector: str) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self, selector) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/errors.py:86-87
    In source order: Evaluate once selector; assign in source target order to self.selector. Then Evaluate super().__init__(source_template_87_25); retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/errors.py:90-94
interface SymbolAmbiguousError {
  Describe the source Python type, preserving its base/metaclass expression order: StructuredQueryError.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/errors.py:91-94
  // Source signature: __init__(self, selector: str, candidate_ids: tuple[str, ...]) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self, selector, candidate_ids) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/errors.py:92-94
    In source order: Evaluate once selector; assign in source target order to self.selector. Then Evaluate once candidate_ids; assign in source target order to self.candidate_ids. Then Evaluate super().__init__(source_template_94_25); retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/errors.py:97-98
interface StructuredQueryLimitError {
  Describe the source Python type, preserving its base/metaclass expression order: StructuredQueryError.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/errors.py:98-98
  In source order: Retain source documentation literal source_literal_98_4; it is not a model call.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/errors.py:101-116
interface PluginError {
  Describe the source Python type, preserving its base/metaclass expression order: ContextGraphError.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/errors.py:102-102
  In source order: Retain source documentation literal source_literal_102_4; it is not a model call.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/errors.py:104-116
  // Source signature: __init__(self, plugin_name: str, phase: str, message: str, *, context: str | None=None) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self, plugin_name, phase, message, context) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/errors.py:112-116
    In source order: Evaluate once plugin_name; assign in source target order to self.plugin_name. Then Evaluate once phase; assign in source target order to self.phase. Then Evaluate once context; assign in source target order to self.context. Then Evaluate once source_template_115_17 if context else ''; assign in source target order to suffix. Then Evaluate super().__init__(source_template_116_25); retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
}
```

## Local import links

No statically resolved in-checkout import; external calls remain explicit dependency boundaries.
