# vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/php.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/php.py.evidence.json`. SHA-256: `4cc2b5192e39c879361fd031bff3c90b08914ce59e435166b1942fb16c38d2ce`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/php.py:15-26
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.project.config import DEV_SCOPE, DependencyRecord, ManifestReader, ProjectConfig; preserve alias and import-time effects. Then Resolve source import from ._data import parse_json_object, string_items; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/php.py:29-30
// Source signature: _is_platform_requirement(name: str) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _is_platform_requirement(name) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/php.py:30-30
  End this invocation with name == 'php' or name.startswith(('ext-', 'lib-')).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/php.py:33-47
// Source signature: load_composer_dependencies(reader: ManifestReader, config: ProjectConfig) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn load_composer_dependencies(reader, config) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/php.py:34-47
  for each relative in reader.by_base_name('composer.json') {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/php.py:35-36
    if (the source predicate relative != 'composer.json' is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/php.py:36-36
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/php.py:37-38
    In source order: Evaluate once reader.read_text(relative); assign in source target order to text. Then Evaluate once parse_json_object(text) if text is not None else None; assign in source target order to parsed.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/php.py:39-40
    if (the source predicate parsed is None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/php.py:40-40
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/php.py:41-47
    for each (section, dev) in (('require', False), ('require-dev', True)) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/php.py:42-47
      for each (name, version) in string_items(parsed.get(section)) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/php.py:43-44
        if (the source predicate _is_platform_requirement(name) is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/php.py:44-44
          Continue the immediately enclosing source loop at its next iteration.
        }
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/php.py:45-47
        In source order: Evaluate config.add_dependency(DependencyRecord(name, version, relative, dev, DEV_SCOPE if dev else '')); retain side effects and discard the expression result.
      }
    }
  }
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from context_graph_sdk.project.config import DEV_SCOPE, DependencyRecord, ManifestReader, ProjectConfig` at source line 19: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/project/config.py.sudo.md`.
- `from ._data import parse_json_object, string_items` at source line 26: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/_data.py.sudo.md`.
