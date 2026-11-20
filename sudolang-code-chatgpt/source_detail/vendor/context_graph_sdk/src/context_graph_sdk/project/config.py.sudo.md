# vendor/context_graph_sdk/src/context_graph_sdk/project/config.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vendor/context_graph_sdk/src/context_graph_sdk/project/config.py.evidence.json`. SHA-256: `2106285f0d96f91c91018301c17ee75efe62590b507341f1be5e107e1092dc99`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:15-26
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import posixpath; preserve alias and import-time effects. Then Resolve source import from collections.abc import Callable, Iterable, Sequence; preserve alias and import-time effects. Then Resolve source import from dataclasses import dataclass, field; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:27-31
In source order: Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Evaluate once 'dev'; assign in source target order to DEV_SCOPE. Then Evaluate once 'test'; assign in source target order to TEST_SCOPE. Then Evaluate once 10 * 1024 * 1024; assign in source target order to MANIFEST_READ_BYTES.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:35-40
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:34-34
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:35-40
interface DependencyRecord {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:36-40
  In source order: For name, declare without assigning a value; source annotation str. Then For version, assign ''; source annotation str. Then For source, assign ''; source annotation str. Then For dev, assign False; source annotation bool. Then For scope, assign ''; source annotation str.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:44-49
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:43-43
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:44-49
interface ManifestRecord {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:45-49
  In source order: For name, declare without assigning a value; source annotation str. Then For source, declare without assigning a value; source annotation str. Then For language, declare without assigning a value; source annotation str. Then For version, assign ''; source annotation str. Then For workspaces, assign (); source annotation tuple[str, ...].
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:53-57
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:52-52
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:53-57
interface BuildProcessRecord {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:54-57
  In source order: For name, declare without assigning a value; source annotation str. Then For source, declare without assigning a value; source annotation str. Then For language, declare without assigning a value; source annotation str. Then For entry_point, declare without assigning a value; source annotation str.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:61-69
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:60-60
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:61-69
interface ResolutionSettings {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:62-67
  In source order: Retain source documentation literal source_literal_62_4; it is not a model call. Then For go_module_path, assign ''; source annotation str. Then For ts_config_base_url, assign ''; source annotation str. Then For ts_config_paths, assign (); source annotation tuple[tuple[str, tuple[str, ...]], ...]. Then For composer_psr4, assign (); source annotation tuple[tuple[str, tuple[str, ...]], ...].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:68-69
  In source order: For csharp_root_namespace, assign ''; source annotation str. Then For swift_targets, assign (); source annotation tuple[tuple[str, str], ...].
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:73-111
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:72-72
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:73-111
interface ProjectConfig {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:74-78
  In source order: For dependencies, assign field(default_factory=list[DependencyRecord]); source annotation list[DependencyRecord]. Then For manifests, assign field(default_factory=list[ManifestRecord]); source annotation list[ManifestRecord]. Then For build_processes, assign field(default_factory=list[BuildProcessRecord]); source annotation list[BuildProcessRecord]. Then For resolution, assign field(default_factory=ResolutionSettings); source annotation ResolutionSettings. Then For _dependency_keys, assign field(default_factory=set[tuple[str, str]], repr=False); source annotation set[tuple[str, str]].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:80-97
  // Source signature: add_dependency(self, dependency: DependencyRecord) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn add_dependency(self, dependency) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:81-86
    In source order: Retain source documentation literal source_literal_81_8; it is not a model call.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:87-88
    if (the source predicate not dependency.name is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:88-88
      End this invocation with None.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:89-89
    In source order: Evaluate once (dependency.source, dependency.name); assign in source target order to key.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:90-91
    if (the source predicate key in self._dependency_keys is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:91-91
      End this invocation with None.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:92-92
    In source order: Evaluate self._dependency_keys.add(key); retain side effects and discard the expression result.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:93-96
    if (the source predicate dependency.dev and (not dependency.scope) is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:94-96
      In source order: Evaluate once DependencyRecord(dependency.name, dependency.version, dependency.source, True, DEV_SCOPE); assign in source target order to dependency.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:97-97
    In source order: Evaluate self.dependencies.append(dependency); retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:99-101
  // Source signature: add_manifest(self, manifest: ManifestRecord) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn add_manifest(self, manifest) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:100-101
    if (the source predicate manifest.name and manifest.source is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:101-101
      In source order: Evaluate self.manifests.append(manifest); retain side effects and discard the expression result.
    }
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:103-111
  // Source signature: add_build_process(self, process: BuildProcessRecord) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn add_build_process(self, process) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:104-105
    if (the source predicate not process.name or not process.source is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:105-105
      End this invocation with None.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:106-110
    if (the source predicate any((existing.name == process.name and existing.source == process.source for existing in self.build_processes)) is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:110-110
      End this invocation with None.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:111-111
    In source order: Evaluate self.build_processes.append(process); retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:114-166
interface ManifestReader {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:115-115
  In source order: Retain source documentation literal source_literal_115_4; it is not a model call.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:117-128
  // Source signature: __init__(self, root: Path, files: Sequence[str]) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self, root, files) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:118-120
    In source order: Evaluate once root.resolve(); assign in source target order to self.root. Then For normalized_files, assign []; source annotation list[str]. Then For seen, assign set(); source annotation set[str].
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:121-126
    for each relative_path in files {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:122-122
      In source order: Evaluate once _normalize_discovered_path(relative_path); assign in source target order to normalized.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:123-124
      if (the source predicate normalized is None or normalized in seen is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:124-124
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:125-126
      In source order: Evaluate seen.add(normalized); retain side effects and discard the expression result. Then Evaluate normalized_files.append(normalized); retain side effects and discard the expression result.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:127-128
    In source order: Evaluate once tuple(normalized_files); assign in source target order to self.files. Then Evaluate once frozenset(self.files); assign in source target order to self._files.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:130-139
  // Source signature: by_base_name(self, *names: str) -> tuple[str, ...]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn by_base_name(self, names) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:131-132
    In source order: For selected, assign []; source annotation list[str]. Then For seen, assign set(); source annotation set[str].
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:133-138
    for each name in names {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:134-138
      for each relative in self.files {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:135-136
        if (the source predicate posixpath.basename(relative) != name or relative in seen is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:136-136
          Continue the immediately enclosing source loop at its next iteration.
        }
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:137-138
        In source order: Evaluate seen.add(relative); retain side effects and discard the expression result. Then Evaluate selected.append(relative); retain side effects and discard the expression result.
      }
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:139-139
    End this invocation with tuple(selected).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:141-142
  // Source signature: by_extension(self, extension: str) -> tuple[str, ...]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn by_extension(self, extension) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:142-142
    End this invocation with tuple((rel for rel in self.files if posixpath.splitext(rel)[1] == extension)).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:144-166
  // Source signature: read_text(self, relative_path: str) -> str | None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn read_text(self, relative_path) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:145-145
    In source order: Evaluate once _normalize_discovered_path(relative_path); assign in source target order to normalized.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:146-147
    if (the source predicate normalized is None or normalized not in self._files is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:147-147
      End this invocation with None.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:148-148
    In source order: Evaluate once self.root / normalized; assign in source target order to candidate.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:149-166
    Perform the following protected operations {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:152-152
      In source order: Evaluate once self.root; assign in source target order to current.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:153-156
      for each part in Path(normalized).parts {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:154-154
        In source order: Apply source augmented assignment current /= part with source evaluation/in-place semantics.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:155-156
        if (the source predicate current.is_symlink() is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:156-156
          End this invocation with None.
        }
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:157-157
      In source order: Evaluate once candidate.resolve(strict=True); assign in source target order to resolved.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:158-159
      if (the source predicate not resolved.is_relative_to(self.root) or not resolved.is_file() is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:159-159
        End this invocation with None.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:160-161
      Enter source context managers left-to-right: resolved.open('rb') bound to handle {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:161-161
        In source order: Evaluate once handle.read(MANIFEST_READ_BYTES + 1); assign in source target order to data.
      }
      Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:162-163
      if (the source predicate len(data) > MANIFEST_READ_BYTES is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:163-163
        End this invocation with None.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:164-164
      End this invocation with data.decode('utf-8', errors='replace').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:165-166
    On the first matching source exception OSError, in handler order {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:166-166
      End this invocation with None.
    }
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:169-177
// Source signature: _normalize_discovered_path(relative_path: str) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _normalize_discovered_path(relative_path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:170-171
  if (the source predicate not relative_path or '\\' in relative_path or posixpath.isabs(relative_path) is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:171-171
    End this invocation with None.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:172-172
  In source order: Evaluate once posixpath.normpath(relative_path); assign in source target order to normalized.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:173-174
  if (the source predicate normalized in ('', '.', '..') or normalized.startswith('../') is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:174-174
    End this invocation with None.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:175-176
  if (the source predicate normalized != relative_path is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:176-176
    End this invocation with None.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:177-177
  End this invocation with normalized.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:180-182
// Source signature: workspace_display_name(root: Path, source: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn workspace_display_name(root, source) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:181-181
  In source order: Evaluate once root.name; assign in source target order to name.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:182-182
  End this invocation with name if name and name not in ('.', '/') else source.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:185-208
// Source signature: workspace_member_manifest_path(manifest: ManifestRecord, workspace: str) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn workspace_member_manifest_path(manifest, workspace) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:186-187
  In source order: Retain source documentation literal source_literal_186_4; it is not a model call. Then Evaluate once _clean_workspace_member_root(manifest.source, workspace); assign in source target order to member_root.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:188-189
  if (the source predicate member_root is None is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:189-189
    End this invocation with None.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:190-196
  In source order: Evaluate once {'go': 'go.mod', 'java': 'pom.xml', 'javascript': 'package.json', 'python': 'pyproject.toml', 'rust': 'Cargo.toml'}; assign in source target order to member_file_by_language.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:197-204
  if (the source predicate manifest.language == 'csharp' is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:198-199
    if (the source predicate posixpath.splitext(member_root)[1] == '.csproj' is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:199-199
      End this invocation with member_root.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:200-201
    if (the source predicate not member_root is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:201-201
      End this invocation with None.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:202-204
    End this invocation with posixpath.normpath(posixpath.join(member_root, posixpath.basename(member_root) + '.csproj')).
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:205-205
  In source order: Evaluate once member_file_by_language.get(manifest.language); assign in source target order to member_file.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:206-207
  if (the source predicate member_file is None is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:207-207
    End this invocation with None.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:208-208
  End this invocation with posixpath.normpath(posixpath.join(member_root, member_file)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:211-221
// Source signature: _clean_workspace_member_root(manifest_source: str, workspace: str) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _clean_workspace_member_root(manifest_source, workspace) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:212-212
  In source order: Evaluate once workspace.replace('\\', '/').strip(); assign in source target order to workspace.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:213-214
  if (the source predicate not workspace or posixpath.isabs(workspace) or any((c in workspace for c in '*?[')) is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:214-214
    End this invocation with None.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:215-216
  In source order: Evaluate once posixpath.dirname(manifest_source); assign in source target order to manifest_dir. Then Evaluate once posixpath.normpath(posixpath.join(manifest_dir, workspace)); assign in source target order to cleaned.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:217-218
  if (the source predicate cleaned == '.' is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:218-218
    In source order: Evaluate once ''; assign in source target order to cleaned.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:219-220
  if (the source predicate cleaned == '..' or cleaned.startswith('../') is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:220-220
    End this invocation with None.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:221-221
  End this invocation with cleaned.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:224-232
// Source signature: load_project_config(root: str | Path, files: Iterable[str]) -> ProjectConfig
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn load_project_config(root, files) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:225-229
  In source order: Resolve source import from context_graph_sdk.project.manifests import ALL_LOADERS; preserve alias and import-time effects. Then Evaluate once ManifestReader(Path(root).resolve(), tuple(files)); assign in source target order to reader. Then Evaluate once ProjectConfig(); assign in source target order to config. Then For loaders, assign ALL_LOADERS; source annotation tuple[Callable[[ManifestReader, ProjectConfig], None], ...].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:230-231
  for each loader in loaders {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:231-231
    In source order: Evaluate loader(reader, config); retain side effects and discard the expression result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/config.py:232-232
  End this invocation with config.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from context_graph_sdk.project.manifests import ALL_LOADERS` at source line 225: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/__init__.py.sudo.md`.
