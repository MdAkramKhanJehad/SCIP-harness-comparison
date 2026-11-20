# vendor/context_graph_sdk/src/context_graph_sdk/resolution/bindings.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vendor/context_graph_sdk/src/context_graph_sdk/resolution/bindings.py.evidence.json`. SHA-256: `0a480198fb25d61e971dd9f2bcebdbfdf15e9273c931b3a373aebfd77dc255bb`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/bindings.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.extractors.records import Symbol; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.models import LocalRelationshipType; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.resolution.context import ResolutionContext, ResolutionResult; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/bindings.py:23-23
In source order: Evaluate once ('Class', 'Struct', 'Interface', 'Trait', 'Enum', 'Record'); assign in source target order to _TYPE_TARGET_LABELS.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/bindings.py:26-44
// Source signature: _assignment_target(context: ResolutionContext, candidates: list[Symbol], writer_id: str) -> Symbol | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _assignment_target(context, candidates, writer_id) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/bindings.py:29-30
  if (the source predicate not candidates is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/bindings.py:30-30
    End this invocation with None.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/bindings.py:31-31
  In source order: Evaluate once context.symbols_by_id.get(writer_id); assign in source target order to writer.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/bindings.py:32-33
  if (the source predicate writer is None or len(candidates) == 1 is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/bindings.py:33-33
    End this invocation with candidates[0].
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/bindings.py:34-40
  if (the source predicate writer.owner_name is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/bindings.py:35-40
    for each candidate in candidates {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/bindings.py:36-40
      if (the source predicate candidate.label in ('Property', 'Const') and (candidate.owner_name == writer.owner_name and candidate.file_path == writer.file_path) is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/bindings.py:40-40
        End this invocation with candidate.
      }
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/bindings.py:41-43
  for each candidate in candidates {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/bindings.py:42-43
    if (the source predicate candidate.file_path == writer.file_path is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/bindings.py:43-43
      End this invocation with candidate.
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/bindings.py:44-44
  End this invocation with candidates[0].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/bindings.py:47-62
// Source signature: resolve_assignments(context: ResolutionContext, result: ResolutionResult) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn resolve_assignments(context, result) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/bindings.py:48-62
  for each (path, file_result) in context.extraction.files {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/bindings.py:49-62
    for each assignment in file_result.assignments {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/bindings.py:50-50
      In source order: Evaluate once context.symbols_by_name.get(assignment.property_name, []); assign in source target order to candidates.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/bindings.py:51-52
      if (the source predicate not candidates is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/bindings.py:52-52
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/bindings.py:53-54
      In source order: Evaluate once context.enclosing_symbol(path, assignment.line); assign in source target order to writer_id. Then Evaluate once _assignment_target(context, candidates, writer_id); assign in source target order to target.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/bindings.py:55-56
      if (the source predicate target is None is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/bindings.py:56-56
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/bindings.py:57-62
      In source order: Evaluate result.add_edge(writer_id, LocalRelationshipType.ACCESSES, target.id, {'accessKind': 'write'}); retain side effects and discard the expression result.
    }
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/bindings.py:65-70
// Source signature: _owners_in_file(context: ResolutionContext, owner_name: str, path: str) -> list[Symbol]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _owners_in_file(context, owner_name, path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/bindings.py:66-70
  End this invocation with [candidate for candidate in context.symbols_by_name.get(owner_name, []) if candidate.file_path == path].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/bindings.py:73-106
// Source signature: resolve_type_bindings(context: ResolutionContext, result: ResolutionResult) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn resolve_type_bindings(context, result) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/bindings.py:76-76
  In source order: For parameter_types, assign {}; source annotation dict[tuple[str, str], list[tuple[str, str]]].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/bindings.py:77-101
  for each (path, file_result) in context.extraction.files {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/bindings.py:78-101
    for each binding in file_result.type_bindings {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/bindings.py:79-79
      In source order: Evaluate once context.enclosing_symbol(path, binding.line); assign in source target order to source_id.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/bindings.py:80-89
      if (the source predicate binding.type_name and binding.variable_name not in ('@return', '@type') is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/bindings.py:81-89
        for each candidate in context.symbols_by_name.get(binding.type_name, []) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/bindings.py:82-89
          if (the source predicate candidate.label in _TYPE_TARGET_LABELS is truthy) {
            // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/bindings.py:83-88
            In source order: Evaluate result.add_edge(source_id, LocalRelationshipType.USES, candidate.id, {'reason': source_template_87_39}); retain side effects and discard the expression result.
            // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/bindings.py:89-89
            Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
          }
        }
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/bindings.py:90-93
      if (the source predicate binding.kind == 'parameter' and binding.owner_name is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/bindings.py:91-93
        In source order: Evaluate parameter_types.setdefault((path, binding.owner_name), []).append((binding.variable_name, binding.type_name)); retain side effects and discard the expression result.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/bindings.py:94-101
      if (the source predicate binding.kind == 'comment' and binding.variable_name == '@return' and binding.owner_name is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/bindings.py:99-101
        for each owner in _owners_in_file(context, binding.owner_name, path) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/bindings.py:100-101
          if (the source predicate not owner.return_type is truthy) {
            // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/bindings.py:101-101
            In source order: Evaluate result.update_property(owner.id, 'returnType', binding.type_name); retain side effects and discard the expression result.
          }
        }
      }
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/bindings.py:103-106
  for each ((path, owner_name), entries) in sorted(parameter_types.items()) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/bindings.py:104-104
    In source order: Evaluate once ', '.join((source_template_104_29 for name, type_name in entries)); assign in source target order to rendered.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/bindings.py:105-106
    for each owner in _owners_in_file(context, owner_name, path) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/bindings.py:106-106
      In source order: Evaluate result.update_property(owner.id, 'parameterTypes', rendered); retain side effects and discard the expression result.
    }
  }
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from context_graph_sdk.extractors.records import Symbol` at source line 19: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py.sudo.md`.
- `from context_graph_sdk.models import LocalRelationshipType` at source line 20: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/models.py.sudo.md`.
- `from context_graph_sdk.resolution.context import ResolutionContext, ResolutionResult` at source line 21: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py.sudo.md`.
