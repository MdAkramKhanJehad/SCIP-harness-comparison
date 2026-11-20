# vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/resolution_config.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/resolution_config.py.evidence.json`. SHA-256: `a93894e56a88588c8151605ce054cb8612a6cbe5a47a0f3082f5686f4585032f`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/resolution_config.py:15-22
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import posixpath; preserve alias and import-time effects. Then Resolve source import import re; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.project.config import ManifestReader, ProjectConfig, ResolutionSettings; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/resolution_config.py:24-28
In source order: Resolve source import from ._data import as_mapping, as_str, mapping_at, parse_json_object, string_list; preserve alias and import-time effects. Then Evaluate once re.compile('<RootNamespace>([^<]+)</RootNamespace>'); assign in source target order to _ROOT_NAMESPACE. Then Evaluate once re.compile('\\.(?:target|executableTarget|testTarget)\\s*\\(\\s*name:\\s*"([^"]+)"'); assign in source target order to _SWIFT_TARGET. Then Evaluate once re.compile('path:\\s*"([^"]+)"'); assign in source target order to _SWIFT_PATH.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/resolution_config.py:31-39
// Source signature: _go_module_path(reader: ManifestReader) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _go_module_path(reader) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/resolution_config.py:32-32
  In source order: Evaluate once reader.read_text('go.mod') if 'go.mod' in reader.files else None; assign in source target order to text.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/resolution_config.py:33-34
  if (the source predicate text is None is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/resolution_config.py:34-34
    End this invocation with ''.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/resolution_config.py:35-38
  for each line in text.split(source_literal_35_27) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/resolution_config.py:36-36
    In source order: Evaluate once line.split('//', 1)[0].strip(); assign in source target order to stripped.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/resolution_config.py:37-38
    if (the source predicate stripped.startswith('module ') is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/resolution_config.py:38-38
      End this invocation with stripped[len('module '):].strip().
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/resolution_config.py:39-39
  End this invocation with ''.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/resolution_config.py:42-52
// Source signature: _string_list_map(value: object) -> tuple[tuple[str, tuple[str, ...]], ...]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _string_list_map(value) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/resolution_config.py:43-44
  In source order: Evaluate once as_mapping(value) or {}; assign in source target order to mapping. Then For entries, assign []; source annotation list[tuple[str, tuple[str, ...]]].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/resolution_config.py:45-51
  for each (key, item) in sorted(mapping.items()) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/resolution_config.py:46-51
    if (the source predicate isinstance(item, str) is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/resolution_config.py:47-47
      In source order: Evaluate entries.append((key, (item,))); retain side effects and discard the expression result.
    }
    else {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/resolution_config.py:49-49
      In source order: Evaluate once string_list(item); assign in source target order to values.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/resolution_config.py:50-51
      if (the source predicate values is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/resolution_config.py:51-51
        In source order: Evaluate entries.append((key, values)); retain side effects and discard the expression result.
      }
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/resolution_config.py:52-52
  End this invocation with tuple(entries).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/resolution_config.py:55-62
// Source signature: _ts_config(reader: ManifestReader) -> tuple[str, tuple[tuple[str, tuple[str, ...]], ...]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _ts_config(reader) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/resolution_config.py:56-61
  for each name in ('tsconfig.json', 'jsconfig.json') {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/resolution_config.py:57-58
    if (the source predicate name not in reader.files is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/resolution_config.py:58-58
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/resolution_config.py:59-59
    In source order: Evaluate once _load_ts_config(reader, name, set(), 0); assign in source target order to loaded.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/resolution_config.py:60-61
    if (the source predicate loaded is not None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/resolution_config.py:61-61
      End this invocation with loaded.
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/resolution_config.py:62-62
  End this invocation with ('', ()).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/resolution_config.py:65-87
// Source signature: _load_ts_config(reader: ManifestReader, relative_path: str, seen: set[str], depth: int) -> tuple[str, tuple[tuple[str, tuple[str, ...]], ...]] | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _load_ts_config(reader, relative_path, seen, depth) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/resolution_config.py:68-69
  if (the source predicate depth >= 32 or relative_path in seen is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/resolution_config.py:69-69
    End this invocation with None.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/resolution_config.py:70-72
  In source order: Evaluate seen.add(relative_path); retain side effects and discard the expression result. Then Evaluate once reader.read_text(relative_path); assign in source target order to text. Then Evaluate once parse_json_object(text) if text is not None else None; assign in source target order to parsed.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/resolution_config.py:73-74
  if (the source predicate parsed is None is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/resolution_config.py:74-74
    End this invocation with None.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/resolution_config.py:75-78
  In source order: Evaluate once mapping_at(parsed, 'compilerOptions'); assign in source target order to options. Then Evaluate once as_str(options.get('baseUrl')); assign in source target order to base_url. Then Evaluate once _string_list_map(options.get('paths')); assign in source target order to paths. Then Evaluate once as_str(parsed.get('extends')); assign in source target order to extends.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/resolution_config.py:79-86
  if (the source predicate extends and (not base_url or not paths) is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/resolution_config.py:80-81
    if (the source predicate not extends.endswith('.json') is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/resolution_config.py:81-81
      In source order: Apply source augmented assignment extends += '.json' with source evaluation/in-place semantics.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/resolution_config.py:82-83
    In source order: Evaluate once posixpath.normpath(posixpath.join(posixpath.dirname(relative_path), extends)); assign in source target order to parent. Then Evaluate once _load_ts_config(reader, parent, seen, depth + 1); assign in source target order to inherited.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/resolution_config.py:84-86
    if (the source predicate inherited is not None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/resolution_config.py:85-86
      In source order: Evaluate once base_url or inherited[0]; assign in source target order to base_url. Then Evaluate once paths or inherited[1]; assign in source target order to paths.
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/resolution_config.py:87-87
  End this invocation with (base_url, paths).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/resolution_config.py:90-97
// Source signature: _composer_psr4(reader: ManifestReader) -> tuple[tuple[str, tuple[str, ...]], ...]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _composer_psr4(reader) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/resolution_config.py:91-92
  if (the source predicate 'composer.json' not in reader.files is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/resolution_config.py:92-92
    End this invocation with ().
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/resolution_config.py:93-94
  In source order: Evaluate once reader.read_text('composer.json'); assign in source target order to text. Then Evaluate once parse_json_object(text) if text is not None else None; assign in source target order to parsed.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/resolution_config.py:95-96
  if (the source predicate parsed is None is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/resolution_config.py:96-96
    End this invocation with ().
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/resolution_config.py:97-97
  End this invocation with _string_list_map(mapping_at(parsed, 'autoload').get('psr-4')).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/resolution_config.py:100-110
// Source signature: _csharp_root_namespace(reader: ManifestReader) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _csharp_root_namespace(reader) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/resolution_config.py:101-109
  for each relative in reader.by_extension('.csproj') {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/resolution_config.py:102-103
    if (the source predicate '/' in relative is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/resolution_config.py:103-103
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/resolution_config.py:104-104
    In source order: Evaluate once reader.read_text(relative); assign in source target order to text.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/resolution_config.py:105-106
    if (the source predicate text is None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/resolution_config.py:106-106
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/resolution_config.py:107-107
    In source order: Evaluate once _ROOT_NAMESPACE.search(text); assign in source target order to match.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/resolution_config.py:108-109
    if (the source predicate match is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/resolution_config.py:109-109
      End this invocation with match.group(1).
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/resolution_config.py:110-110
  End this invocation with ''.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/resolution_config.py:113-125
// Source signature: _swift_targets(reader: ManifestReader) -> tuple[tuple[str, str], ...]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _swift_targets(reader) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/resolution_config.py:114-115
  if (the source predicate 'Package.swift' not in reader.files is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/resolution_config.py:115-115
    End this invocation with ().
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/resolution_config.py:116-116
  In source order: Evaluate once reader.read_text('Package.swift'); assign in source target order to text.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/resolution_config.py:117-118
  if (the source predicate text is None is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/resolution_config.py:118-118
    End this invocation with ().
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/resolution_config.py:119-119
  In source order: For targets, assign []; source annotation list[tuple[str, str]].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/resolution_config.py:120-124
  for each match in _SWIFT_TARGET.finditer(text) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/resolution_config.py:121-124
    In source order: Evaluate once match.group(1); assign in source target order to name. Then Evaluate once text[match.end():match.end() + 200]; assign in source target order to window. Then Evaluate once _SWIFT_PATH.search(window); assign in source target order to path_match. Then Evaluate targets.append((name, path_match.group(1) if path_match else source_template_124_69)); retain side effects and discard the expression result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/resolution_config.py:125-125
  End this invocation with tuple(targets).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/resolution_config.py:128-137
// Source signature: load_resolution_settings(reader: ManifestReader, config: ProjectConfig) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn load_resolution_settings(reader, config) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/resolution_config.py:129-137
  In source order: Evaluate once _ts_config(reader); assign in source target order to (base_url, paths). Then Evaluate once ResolutionSettings(go_module_path=_go_module_path(reader), ts_config_base_url=base_url, ts_config_paths=paths, composer_psr4=_composer_psr4(reader), csharp_root_namespace=_csharp_root_namespace(reader), swift_targets=_swift_targets(reader)); assign in source target order to config.resolution.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from context_graph_sdk.project.config import ManifestReader, ProjectConfig, ResolutionSettings` at source line 22: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/project/config.py.sudo.md`.
- `from ._data import as_mapping, as_str, mapping_at, parse_json_object, string_list` at source line 24: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/_data.py.sudo.md`.
