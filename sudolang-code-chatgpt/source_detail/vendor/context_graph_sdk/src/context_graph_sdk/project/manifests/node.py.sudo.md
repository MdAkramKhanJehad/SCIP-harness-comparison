# vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/node.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/node.py.evidence.json`. SHA-256: `27dcf93a8dd6ead499c210756d3be6ba9be7987981c5ab40a7efc367ed0afa43`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/node.py:15-34
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.project.config import DependencyRecord, ManifestReader, ManifestRecord, ProjectConfig, workspace_display_name; preserve alias and import-time effects. Then Resolve source import from ._data import as_mapping, as_str, parse_json_object, string_items, string_list; preserve alias and import-time effects. Then Evaluate once (('dependencies', False, ''), ('devDependencies', True, 'dev'), ('peerDependencies', True, 'peer'), ('optionalDependencies', True, 'optional')); assign in source target order to _SCOPED_SECTIONS.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/node.py:37-44
// Source signature: _is_non_npm_package(package: dict[str, object]) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _is_non_npm_package(package) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/node.py:38-39
  In source order: Retain source documentation literal source_literal_38_4; it is not a model call. Then Evaluate once as_mapping(package.get('engines')) or {}; assign in source target order to engines.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/node.py:40-41
  if (the source predicate 'vscode' in engines is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/node.py:41-41
    End this invocation with True.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/node.py:42-43
  if (the source predicate package.get('contributes') is not None is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/node.py:43-43
    End this invocation with True.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/node.py:44-44
  End this invocation with bool(package.get('unity')).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/node.py:47-55
// Source signature: load_package_json_dependencies(reader: ManifestReader, config: ProjectConfig) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn load_package_json_dependencies(reader, config) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/node.py:48-55
  for each relative in reader.by_base_name('package.json') {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/node.py:49-50
    In source order: Evaluate once reader.read_text(relative); assign in source target order to text. Then Evaluate once parse_json_object(text) if text is not None else None; assign in source target order to package.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/node.py:51-52
    if (the source predicate package is None or _is_non_npm_package(package) is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/node.py:52-52
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/node.py:53-55
    for each (section, dev, scope) in _SCOPED_SECTIONS {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/node.py:54-55
      for each (name, version) in string_items(package.get(section)) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/node.py:55-55
        In source order: Evaluate config.add_dependency(DependencyRecord(name, version, relative, dev, scope)); retain side effects and discard the expression result.
      }
    }
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/node.py:58-62
// Source signature: _workspace_entries(value: object) -> tuple[str, ...]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _workspace_entries(value) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/node.py:59-59
  In source order: Evaluate once as_mapping(value); assign in source target order to mapping.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/node.py:60-61
  if (the source predicate mapping is not None is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/node.py:61-61
    In source order: Evaluate once mapping.get('packages'); assign in source target order to value.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/node.py:62-62
  End this invocation with string_list(value).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/node.py:65-83
// Source signature: load_package_json_manifests(reader: ManifestReader, config: ProjectConfig) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn load_package_json_manifests(reader, config) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/node.py:66-83
  for each relative in reader.by_base_name('package.json') {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/node.py:67-68
    In source order: Evaluate once reader.read_text(relative); assign in source target order to text. Then Evaluate once parse_json_object(text) if text is not None else None; assign in source target order to package.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/node.py:69-70
    if (the source predicate package is None or _is_non_npm_package(package) is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/node.py:70-70
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/node.py:71-72
    In source order: Evaluate once _workspace_entries(package.get('workspaces')); assign in source target order to workspaces. Then Evaluate once as_str(package.get('name')); assign in source target order to manifest_name.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/node.py:73-74
    if (the source predicate not manifest_name and workspaces is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/node.py:74-74
      In source order: Evaluate once workspace_display_name(reader.root, relative); assign in source target order to manifest_name.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/node.py:75-83
    In source order: Evaluate config.add_manifest(ManifestRecord(manifest_name, relative, 'javascript', as_str(package.get('version')), workspaces)); retain side effects and discard the expression result.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/node.py:86-102
// Source signature: parse_simple_yaml_string_list(text: str, key: str) -> tuple[str, ...]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn parse_simple_yaml_string_list(text, key) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/node.py:87-88
  In source order: For values, assign []; source annotation list[str]. Then Evaluate once False; assign in source target order to in_list.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/node.py:89-101
  for each raw in text.split(source_literal_89_26) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/node.py:90-91
    In source order: Evaluate once _strip_inline_comment(raw.rstrip('\r')); assign in source target order to line. Then Evaluate once line.strip(); assign in source target order to stripped.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/node.py:92-93
    if (the source predicate not stripped or stripped.startswith('#') is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/node.py:93-93
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/node.py:94-96
    if (the source predicate not line.startswith(' ') and stripped.endswith(':') is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/node.py:95-95
      In source order: Evaluate once stripped[:-1] == key; assign in source target order to in_list.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/node.py:96-96
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/node.py:97-98
    if (the source predicate not in_list or not stripped.startswith('-') is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/node.py:98-98
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/node.py:99-99
    In source order: Evaluate once stripped[1:].strip().strip('"\''); assign in source target order to value.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/node.py:100-101
    if (the source predicate value is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/node.py:101-101
      In source order: Evaluate values.append(value); retain side effects and discard the expression result.
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/node.py:102-102
  End this invocation with tuple(values).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/node.py:105-122
// Source signature: _strip_inline_comment(line: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _strip_inline_comment(line) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/node.py:106-108
  In source order: Evaluate once False; assign in source target order to in_single. Then Evaluate once False; assign in source target order to in_double. Then Evaluate once False; assign in source target order to escaped.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/node.py:109-121
  for each (index, char) in enumerate(line) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/node.py:110-112
    if (the source predicate escaped is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/node.py:111-111
      In source order: Evaluate once False; assign in source target order to escaped.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/node.py:112-112
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/node.py:113-115
    if (the source predicate char == '\\' is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/node.py:114-114
      In source order: Evaluate once True; assign in source target order to escaped.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/node.py:115-115
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/node.py:116-121
    if (the source predicate char == "'" and (not in_double) is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/node.py:117-117
      In source order: Evaluate once not in_single; assign in source target order to in_single.
    }
    else {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/node.py:118-121
      if (the source predicate char == '"' and (not in_single) is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/node.py:119-119
        In source order: Evaluate once not in_double; assign in source target order to in_double.
      }
      else {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/node.py:120-121
        if (the source predicate char == '#' and (not in_single) and (not in_double) is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/node.py:121-121
          End this invocation with line[:index].rstrip(' \t').
        }
      }
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/node.py:122-122
  End this invocation with line.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/node.py:125-138
// Source signature: load_pnpm_workspace_manifests(reader: ManifestReader, config: ProjectConfig) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn load_pnpm_workspace_manifests(reader, config) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/node.py:126-138
  for each relative in reader.by_base_name('pnpm-workspace.yaml') {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/node.py:127-127
    In source order: Evaluate once reader.read_text(relative); assign in source target order to text.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/node.py:128-129
    if (the source predicate text is None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/node.py:129-129
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/node.py:130-138
    In source order: Evaluate config.add_manifest(ManifestRecord(workspace_display_name(reader.root, relative), relative, 'javascript', '', parse_simple_yaml_string_list(text, 'packages'))); retain side effects and discard the expression result.
  }
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from context_graph_sdk.project.config import DependencyRecord, ManifestReader, ManifestRecord, ProjectConfig, workspace_display_name` at source line 19: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/project/config.py.sudo.md`.
- `from ._data import as_mapping, as_str, parse_json_object, string_items, string_list` at source line 27: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/_data.py.sudo.md`.
