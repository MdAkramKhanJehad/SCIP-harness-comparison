# vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/dotnet.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/dotnet.py.evidence.json`. SHA-256: `922ea17594425af2f2095f8dbec31fcb4d35bec86323c238fc89bf3e0535dd00`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/dotnet.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import posixpath; preserve alias and import-time effects. Then Resolve source import import re; preserve alias and import-time effects. Then Resolve source import import xml.etree.ElementTree as ElementTree; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/dotnet.py:23-30
In source order: Resolve source import from context_graph_sdk.project.config import DependencyRecord, ManifestReader, ManifestRecord, ProjectConfig; preserve alias and import-time effects. Then Evaluate once re.compile('Project\\("[^"]+"\\)\\s*=\\s*"[^"]+"\\s*,\\s*"([^"]+\\.csproj)"'); assign in source target order to _SOLUTION_PROJECT.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/dotnet.py:33-34
// Source signature: _is_msbuild_variable(value: str) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _is_msbuild_variable(value) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/dotnet.py:34-34
  End this invocation with value.startswith('$(') and value.endswith(')').
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/dotnet.py:37-55
// Source signature: load_csproj_dependencies(reader: ManifestReader, config: ProjectConfig) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn load_csproj_dependencies(reader, config) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/dotnet.py:38-55
  for each relative in reader.by_extension('.csproj') {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/dotnet.py:39-39
    In source order: Evaluate once reader.read_text(relative); assign in source target order to text.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/dotnet.py:40-41
    if (the source predicate text is None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/dotnet.py:41-41
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/dotnet.py:42-45
    Perform the following protected operations {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/dotnet.py:43-43
      In source order: Evaluate once ElementTree.fromstring(text); assign in source target order to root.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/dotnet.py:44-45
    On the first matching source exception ElementTree.ParseError, in handler order {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/dotnet.py:45-45
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/dotnet.py:46-55
    for each reference in root.iter('PackageReference') {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/dotnet.py:47-48
      In source order: Evaluate once (reference.get('Include') or reference.get('Update') or '').strip(); assign in source target order to name. Then Evaluate once (reference.get('Version') or '').strip(); assign in source target order to version.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/dotnet.py:49-52
      if (the source predicate not version is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/dotnet.py:50-50
        In source order: Evaluate once reference.find('Version'); assign in source target order to version_element.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/dotnet.py:51-52
        if (the source predicate version_element is not None is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/dotnet.py:52-52
          In source order: Evaluate once (version_element.text or '').strip(); assign in source target order to version.
        }
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/dotnet.py:53-54
      if (the source predicate not name or _is_msbuild_variable(name) or _is_msbuild_variable(version) is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/dotnet.py:54-54
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/dotnet.py:55-55
      In source order: Evaluate config.add_dependency(DependencyRecord(name, version, relative)); retain side effects and discard the expression result.
    }
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/dotnet.py:58-74
// Source signature: load_solution_manifests(reader: ManifestReader, config: ProjectConfig) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn load_solution_manifests(reader, config) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/dotnet.py:59-74
  for each relative in reader.by_extension('.sln') {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/dotnet.py:60-60
    In source order: Evaluate once reader.read_text(relative); assign in source target order to text.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/dotnet.py:61-62
    if (the source predicate text is None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/dotnet.py:62-62
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/dotnet.py:63-74
    In source order: Evaluate once tuple((match.group(1).replace('\\', '/') for match in _SOLUTION_PROJECT.finditer(text))); assign in source target order to members. Then Evaluate config.add_manifest(ManifestRecord(posixpath.splitext(posixpath.basename(relative))[0], relative, 'csharp', '', members)); retain side effects and discard the expression result.
  }
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from context_graph_sdk.project.config import DependencyRecord, ManifestReader, ManifestRecord, ProjectConfig` at source line 23: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/project/config.py.sudo.md`.
