# vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/rust.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/rust.py.evidence.json`. SHA-256: `3e901de21f5c953f6068e6430902a37b532b08f606236058c00af5dfd18ec6e7`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/rust.py:15-33
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.project.config import DependencyRecord, ManifestReader, ManifestRecord, ProjectConfig, workspace_display_name; preserve alias and import-time effects. Then Resolve source import from ._data import as_mapping, as_str, mapping_at, parse_toml, string_list; preserve alias and import-time effects. Then Evaluate once (('dependencies', False, ''), ('dev-dependencies', True, 'dev'), ('build-dependencies', True, 'build')); assign in source target order to _SECTIONS.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/rust.py:36-42
// Source signature: _dependency_version(value: object) -> tuple[str, str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _dependency_version(value) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/rust.py:37-38
  if (the source predicate isinstance(value, str) is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/rust.py:38-38
    End this invocation with (value, '').
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/rust.py:39-39
  In source order: Evaluate once as_mapping(value); assign in source target order to mapping.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/rust.py:40-41
  if (the source predicate mapping is not None is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/rust.py:41-41
    End this invocation with (as_str(mapping.get('version')), as_str(mapping.get('git'))).
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/rust.py:42-42
  End this invocation with ('', '').
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/rust.py:45-57
// Source signature: load_cargo_dependencies(reader: ManifestReader, config: ProjectConfig) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn load_cargo_dependencies(reader, config) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/rust.py:46-57
  for each relative in reader.by_base_name('Cargo.toml') {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/rust.py:47-48
    In source order: Evaluate once reader.read_text(relative); assign in source target order to text. Then Evaluate once parse_toml(text) if text is not None else None; assign in source target order to parsed.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/rust.py:49-50
    if (the source predicate parsed is None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/rust.py:50-50
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/rust.py:51-57
    for each (section, dev, scope) in _SECTIONS {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/rust.py:52-52
      In source order: Evaluate once as_mapping(parsed.get(section)) or {}; assign in source target order to entries.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/rust.py:53-57
      for each (name, value) in entries.items() {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/rust.py:54-54
        In source order: Evaluate once _dependency_version(value); assign in source target order to (version, git).
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/rust.py:55-56
        if (the source predicate not version and (not git) is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/rust.py:56-56
          Continue the immediately enclosing source loop at its next iteration.
        }
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/rust.py:57-57
        In source order: Evaluate config.add_dependency(DependencyRecord(name, version, relative, dev, scope)); retain side effects and discard the expression result.
      }
    }
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/rust.py:60-79
// Source signature: load_cargo_manifests(reader: ManifestReader, config: ProjectConfig) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn load_cargo_manifests(reader, config) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/rust.py:61-79
  for each relative in reader.by_base_name('Cargo.toml') {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/rust.py:62-63
    In source order: Evaluate once reader.read_text(relative); assign in source target order to text. Then Evaluate once parse_toml(text) if text is not None else None; assign in source target order to parsed.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/rust.py:64-65
    if (the source predicate parsed is None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/rust.py:65-65
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/rust.py:66-68
    In source order: Evaluate once mapping_at(parsed, 'package'); assign in source target order to package. Then Evaluate once string_list(mapping_at(parsed, 'workspace').get('members')); assign in source target order to members. Then Evaluate once as_str(package.get('name')); assign in source target order to manifest_name.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/rust.py:69-70
    if (the source predicate not manifest_name and members is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/rust.py:70-70
      In source order: Evaluate once workspace_display_name(reader.root, relative); assign in source target order to manifest_name.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/rust.py:71-79
    In source order: Evaluate config.add_manifest(ManifestRecord(manifest_name, relative, 'rust', as_str(package.get('version')), members)); retain side effects and discard the expression result.
  }
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from context_graph_sdk.project.config import DependencyRecord, ManifestReader, ManifestRecord, ProjectConfig, workspace_display_name` at source line 19: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/project/config.py.sudo.md`.
- `from ._data import as_mapping, as_str, mapping_at, parse_toml, string_list` at source line 27: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/_data.py.sudo.md`.
