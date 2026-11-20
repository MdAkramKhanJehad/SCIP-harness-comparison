# vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py.evidence.json`. SHA-256: `d9f4b909ca2d02aac567e557beca9738c96812ca9a99995039e6eb16e83eb9de`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:15-26
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import posixpath; preserve alias and import-time effects. Then Resolve source import from collections.abc import Mapping, Sequence; preserve alias and import-time effects. Then Resolve source import from dataclasses import dataclass, field; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:28-33
In source order: Resolve source import from context_graph_sdk.errors import ResolutionLimitError; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.extractors.records import ExtractionResult, Symbol; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.models import LocalRelationshipType; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.project.config import ProjectConfig, ResolutionSettings; preserve alias and import-time effects. Then Evaluate once 500000; assign in source target order to MAX_RESOLUTION_EDGES.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:34-34
In source order: Evaluate once 200; assign in source target order to MAX_CANDIDATES_PER_NAME.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:38-42
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:37-37
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:38-42
interface ResolvedEdge {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:39-42
  In source order: For source_local_id, declare without assigning a value; source annotation str. Then For relationship, declare without assigning a value; source annotation LocalRelationshipType. Then For target_local_id, declare without assigning a value; source annotation str. Then For properties, assign (); source annotation tuple[tuple[str, object], ...].
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:46-86
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:45-45
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:46-86
interface ResolutionResult {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:47-53
  In source order: Retain source documentation literal source_literal_47_4; it is not a model call. Then For edges, assign field(default_factory=list[ResolvedEdge]); source annotation list[ResolvedEdge]. Then For property_updates, assign field(default_factory=dict[str, dict[str, object]]); source annotation dict[str, dict[str, object]]. Then For _seen, assign field(default_factory=set[tuple[str, str, str]], repr=False); source annotation set[tuple[str, str, str]].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:55-83
  // Source signature: add_edge(self, source_local_id: str, relationship: LocalRelationshipType, target_local_id: str, properties: Mapping[str, object] | None=None) -> bool
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn add_edge(self, source_local_id, relationship, target_local_id, properties) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:62-63
    In source order: Retain source documentation literal source_literal_62_8; it is not a model call.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:64-65
    if (the source predicate not source_local_id or not target_local_id or source_local_id == target_local_id is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:65-65
      End this invocation with False.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:66-66
    In source order: Evaluate once (source_local_id, relationship.value, target_local_id); assign in source target order to key.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:67-68
    if (the source predicate key in self._seen is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:68-68
      End this invocation with False.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:69-73
    if (the source predicate len(self.edges) >= MAX_RESOLUTION_EDGES is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:70-72
      Raise ResolutionLimitError(source_template_71_16).
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:73-73
      End this invocation with False.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:74-82
    In source order: Evaluate self._seen.add(key); retain side effects and discard the expression result. Then Evaluate self.edges.append(ResolvedEdge(source_local_id, relationship, target_local_id, tuple(sorted((properties or {}).items())))); retain side effects and discard the expression result.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:83-83
    End this invocation with True.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:85-86
  // Source signature: update_property(self, symbol_id: str, key: str, value: object) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn update_property(self, symbol_id, key, value) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:86-86
    In source order: Evaluate self.property_updates.setdefault(symbol_id, {}).setdefault(key, value); retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:89-90
// Source signature: file_local_id(relative_path: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn file_local_id(relative_path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:90-90
  End this invocation with source_template_90_11.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:93-94
// Source signature: folder_local_id(relative_path: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn folder_local_id(relative_path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:94-94
  End this invocation with source_template_94_11.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:98-101
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:97-97
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:98-101
interface _SymbolRange {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:99-101
  In source order: For local_id, declare without assigning a value; source annotation str. Then For start, declare without assigning a value; source annotation int. Then For end, declare without assigning a value; source annotation int.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:104-193
interface ResolutionContext {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:105-105
  In source order: Retain source documentation literal source_literal_105_4; it is not a model call.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:107-153
  // Source signature: __init__(self, files: Sequence[tuple[str, str]], folder_paths: Sequence[str], extraction: ExtractionResult, config: ProjectConfig) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self, files, folder_paths, extraction, config) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:114-120
    In source order: Retain source documentation literal source_literal_114_8; it is not a model call. Then For self.settings, assign config.resolution; source annotation ResolutionSettings. Then For self.file_language, assign {path: language for path, language in sorted(files)}; source annotation dict[str, str]. Then For self.file_paths, assign tuple(sorted(self.file_language)); source annotation tuple[str, ...]. Then For self.folders, assign frozenset(folder_paths); source annotation frozenset[str].
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:121-122
    In source order: For self.files, assign frozenset(self.file_paths); source annotation frozenset[str]. Then For self.files_by_dir, assign {}; source annotation dict[str, list[str]].
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:123-126
    for each path in self.file_paths {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:124-126
      In source order: Evaluate self.files_by_dir.setdefault(posixpath.dirname(path), []).append(posixpath.basename(path)); retain side effects and discard the expression result.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:127-127
    In source order: For self.files_by_base, assign {}; source annotation dict[str, list[str]].
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:128-129
    for each path in self.file_paths {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:129-129
      In source order: Evaluate self.files_by_base.setdefault(posixpath.basename(path), []).append(path); retain side effects and discard the expression result.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:131-139
    In source order: Evaluate once extraction; assign in source target order to self.extraction. Then For self.symbols, assign tuple(sorted((s for _, fr in extraction.files for s in fr.symbols), key=lambda s: (s.file_path, s.start_line, s.id))); source annotation tuple[Symbol, ...]. Then For self.symbols_by_id, assign {s.id: s for s in self.symbols}; source annotation dict[str, Symbol]. Then For self.symbols_by_name, assign {}; source annotation dict[str, list[Symbol]].
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:140-143
    for each symbol in self.symbols {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:141-141
      In source order: Evaluate once self.symbols_by_name.setdefault(symbol.name, []); assign in source target order to bucket.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:142-143
      if (the source predicate len(bucket) < MAX_CANDIDATES_PER_NAME is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:143-143
        In source order: Evaluate bucket.append(symbol); retain side effects and discard the expression result.
      }
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:144-145
    for each bucket in self.symbols_by_name.values() {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:145-145
      In source order: Evaluate bucket.sort(key=lambda s: s.id); retain side effects and discard the expression result.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:146-146
    In source order: For self._ranges, assign {}; source annotation dict[str, list[_SymbolRange]].
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:147-150
    for each symbol in self.symbols {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:148-150
      In source order: Evaluate self._ranges.setdefault(symbol.file_path, []).append(_SymbolRange(symbol.id, symbol.start_line, symbol.end_line)); retain side effects and discard the expression result.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:152-153
    In source order: Evaluate once _build_import_alias_map(extraction); assign in source target order to self.import_aliases. Then Evaluate once _build_receiver_type_map(extraction); assign in source target order to self.receiver_types.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:155-156
  // Source signature: has_file(self, path: str) -> bool
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn has_file(self, path) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:156-156
    End this invocation with path in self.files.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:158-165
  // Source signature: lookup_with_extensions(self, base_path: str, extensions: tuple[str, ...]) -> str | None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn lookup_with_extensions(self, base_path, extensions) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:159-160
    if (the source predicate base_path in self.files is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:160-160
      End this invocation with base_path.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:161-164
    for each extension in extensions {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:162-162
      In source order: Evaluate once base_path + extension; assign in source target order to candidate.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:163-164
      if (the source predicate candidate in self.files is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:164-164
        End this invocation with candidate.
      }
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:165-165
    End this invocation with None.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:167-172
  // Source signature: lookup_suffix(self, suffix: str) -> str | None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn lookup_suffix(self, suffix) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:168-168
    In source order: Evaluate once posixpath.basename(suffix); assign in source target order to base.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:169-171
    for each path in self.files_by_base.get(base, []) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:170-171
      if (the source predicate path.endswith(suffix) is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:171-171
        End this invocation with path.
      }
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:172-172
    End this invocation with None.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:174-175
  // Source signature: files_in_dir(self, directory: str) -> list[str]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn files_in_dir(self, directory) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:175-175
    End this invocation with self.files_by_dir.get(directory.rstrip('/'), []).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:177-187
  // Source signature: enclosing_symbol(self, relative_path: str, line: int) -> str
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn enclosing_symbol(self, relative_path, line) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:178-180
    In source order: Retain source documentation literal source_literal_178_8; it is not a model call. Then Evaluate once ''; assign in source target order to best_id. Then Evaluate once 1 << 31; assign in source target order to best_span.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:181-186
    for each candidate in self._ranges.get(relative_path, []) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:182-186
      if (the source predicate candidate.start <= line <= candidate.end is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:183-183
        In source order: Evaluate once candidate.end - candidate.start; assign in source target order to span.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:184-186
        if (the source predicate span < best_span or (span == best_span and candidate.local_id < best_id) is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:185-186
          In source order: Evaluate once span; assign in source target order to best_span. Then Evaluate once candidate.local_id; assign in source target order to best_id.
        }
      }
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:187-187
    End this invocation with best_id or file_local_id(relative_path).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:189-193
  // Source signature: receiver_type(self, relative_path: str, receiver_name: str) -> str
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn receiver_type(self, relative_path, receiver_name) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:191-192
    if (the source predicate receiver_name in ('self', 'this', 'cls') is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:192-192
      End this invocation with ''.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:193-193
    End this invocation with self.receiver_types.get(relative_path, {}).get(receiver_name, '').
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:196-208
// Source signature: _build_import_alias_map(extraction: ExtractionResult) -> dict[str, dict[str, str]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _build_import_alias_map(extraction) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:197-197
  In source order: For result, assign {}; source annotation dict[str, dict[str, str]].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:198-207
  for each (path, file_result) in extraction.files {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:199-207
    for each imported in file_result.imports {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:200-207
      for each binding in imported.bindings {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:201-207
        if (the source predicate binding.alias and binding.original and (binding.alias != binding.original) and (binding.original != '*') is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:207-207
          In source order: Evaluate result.setdefault(path, {}).setdefault(binding.alias, binding.original); retain side effects and discard the expression result.
        }
      }
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:208-208
  End this invocation with result.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:211-220
// Source signature: _build_receiver_type_map(extraction: ExtractionResult) -> dict[str, dict[str, str]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _build_receiver_type_map(extraction) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:212-212
  In source order: For result, assign {}; source annotation dict[str, dict[str, str]].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:213-219
  for each (path, file_result) in extraction.files {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:214-219
    for each binding in file_result.type_bindings {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:215-216
      if (the source predicate not binding.variable_name or not binding.type_name is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:216-216
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:217-218
      if (the source predicate binding.variable_name.startswith('@') is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:218-218
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:219-219
      In source order: Evaluate result.setdefault(path, {}).setdefault(binding.variable_name, binding.type_name); retain side effects and discard the expression result.
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py:220-220
  End this invocation with result.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from context_graph_sdk.errors import ResolutionLimitError` at source line 28: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/errors.py.sudo.md`.
- `from context_graph_sdk.extractors.records import ExtractionResult, Symbol` at source line 29: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py.sudo.md`.
- `from context_graph_sdk.models import LocalRelationshipType` at source line 30: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/models.py.sudo.md`.
- `from context_graph_sdk.project.config import ProjectConfig, ResolutionSettings` at source line 31: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/project/config.py.sudo.md`.
