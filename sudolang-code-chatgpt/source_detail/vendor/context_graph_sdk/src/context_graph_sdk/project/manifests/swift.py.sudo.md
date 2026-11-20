# vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/swift.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/swift.py.evidence.json`. SHA-256: `0913d85418d63c2f23af3988eb5a08f5bb47e31d1a937b2612509cb27373eb95`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/swift.py:15-29
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import re; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.project.config import DependencyRecord, ManifestReader, ManifestRecord, ProjectConfig, workspace_display_name; preserve alias and import-time effects. Then Evaluate once re.compile('name:\\s*"([^"]+)"'); assign in source target order to _PACKAGE_NAME.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/swift.py:30-36
In source order: Evaluate once re.compile(source_literal_31_4); assign in source target order to _PACKAGE_DEPENDENCY.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/swift.py:39-41
// Source signature: _package_name_from_url(url: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _package_name_from_url(url) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/swift.py:40-40
  In source order: Evaluate once url.removesuffix('.git').rsplit('/', 1)[-1]; assign in source target order to name.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/swift.py:41-41
  End this invocation with name or url.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/swift.py:44-55
// Source signature: load_swift_package_dependencies(reader: ManifestReader, config: ProjectConfig) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn load_swift_package_dependencies(reader, config) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/swift.py:45-55
  for each relative in reader.by_base_name('Package.swift') {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/swift.py:46-47
    if (the source predicate relative != 'Package.swift' is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/swift.py:47-47
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/swift.py:48-48
    In source order: Evaluate once reader.read_text(relative); assign in source target order to text.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/swift.py:49-50
    if (the source predicate text is None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/swift.py:50-50
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/swift.py:51-55
    for each match in _PACKAGE_DEPENDENCY.finditer(text) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/swift.py:52-55
      In source order: Evaluate once next((group for group in match.groups()[1:] if group), ''); assign in source target order to version. Then Evaluate config.add_dependency(DependencyRecord(_package_name_from_url(match.group(1)), version, relative)); retain side effects and discard the expression result.
    }
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/swift.py:58-65
// Source signature: load_swift_package_manifests(reader: ManifestReader, config: ProjectConfig) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn load_swift_package_manifests(reader, config) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/swift.py:59-65
  for each relative in reader.by_base_name('Package.swift') {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/swift.py:60-60
    In source order: Evaluate once reader.read_text(relative); assign in source target order to text.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/swift.py:61-62
    if (the source predicate text is None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/swift.py:62-62
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/swift.py:63-65
    In source order: Evaluate once _PACKAGE_NAME.search(text); assign in source target order to name_match. Then Evaluate once name_match.group(1) if name_match else workspace_display_name(reader.root, relative); assign in source target order to name. Then Evaluate config.add_manifest(ManifestRecord(name, relative, 'swift')); retain side effects and discard the expression result.
  }
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from context_graph_sdk.project.config import DependencyRecord, ManifestReader, ManifestRecord, ProjectConfig, workspace_display_name` at source line 21: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/project/config.py.sudo.md`.
