# vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/cpp.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/cpp.py.evidence.json`. SHA-256: `806986f6102dccdbebba20ec3778b070aa125cb44ec1cec1217dbc09b0f494f9`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/cpp.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.project.config import DependencyRecord, ManifestReader, ProjectConfig; preserve alias and import-time effects. Then Resolve source import from ._data import as_list, as_mapping, as_str, parse_json_object; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/cpp.py:24-43
// Source signature: load_vcpkg_dependencies(reader: ManifestReader, config: ProjectConfig) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn load_vcpkg_dependencies(reader, config) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/cpp.py:25-43
  for each relative in reader.by_base_name('vcpkg.json') {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/cpp.py:26-27
    if (the source predicate relative != 'vcpkg.json' is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/cpp.py:27-27
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/cpp.py:28-29
    In source order: Evaluate once reader.read_text(relative); assign in source target order to text. Then Evaluate once parse_json_object(text) if text is not None else None; assign in source target order to parsed.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/cpp.py:30-31
    if (the source predicate parsed is None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/cpp.py:31-31
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/cpp.py:32-43
    for each entry in as_list(parsed.get('dependencies')) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/cpp.py:33-35
      if (the source predicate isinstance(entry, str) is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/cpp.py:34-34
        In source order: Evaluate config.add_dependency(DependencyRecord(entry, '', relative)); retain side effects and discard the expression result.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/cpp.py:35-35
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/cpp.py:36-36
      In source order: Evaluate once as_mapping(entry); assign in source target order to mapping.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/cpp.py:37-38
      if (the source predicate mapping is None is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/cpp.py:38-38
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/cpp.py:39-39
      In source order: Evaluate once as_str(mapping.get('name')); assign in source target order to name.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/cpp.py:40-41
      if (the source predicate not name is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/cpp.py:41-41
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/cpp.py:42-43
      In source order: Evaluate once as_str(mapping.get('version>=')) or as_str(mapping.get('version')); assign in source target order to version. Then Evaluate config.add_dependency(DependencyRecord(name, version, relative)); retain side effects and discard the expression result.
    }
  }
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from context_graph_sdk.project.config import DependencyRecord, ManifestReader, ProjectConfig` at source line 19: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/project/config.py.sudo.md`.
- `from ._data import as_list, as_mapping, as_str, parse_json_object` at source line 21: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/_data.py.sudo.md`.
