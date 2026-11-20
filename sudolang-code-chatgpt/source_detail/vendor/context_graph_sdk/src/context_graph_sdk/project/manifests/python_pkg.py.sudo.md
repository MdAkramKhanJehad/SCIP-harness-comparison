# vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py.evidence.json`. SHA-256: `b9893973d94bbf6c8d831929502aba5112d30233aad81963598369edc51ee443`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:15-29
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import posixpath; preserve alias and import-time effects. Then Resolve source import import re; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.project.config import DEV_SCOPE, DependencyRecord, ManifestReader, ManifestRecord, ProjectConfig, workspace_display_name; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:31-45
In source order: Resolve source import from ._data import as_mapping, as_str, mapping_at, parse_toml, string_list; preserve alias and import-time effects. Then Evaluate once re.compile('(^|\\s+)#.*$'); assign in source target order to _INLINE_COMMENT. Then Evaluate once re.compile('^[a-zA-Z0-9]([a-zA-Z0-9._-]*[a-zA-Z0-9])?$'); assign in source target order to _VALID_PACKAGE. Then Evaluate once ('===', '==', '>=', '<=', '~=', '!=', '>', '<'); assign in source target order to _VERSION_SEPARATORS. Then Evaluate once ('requirements.txt', 'requirements-prod.txt', 'requirements-dev.txt', 'requirements-test.txt', 'requirements_dev.txt', 'requirements_test.txt'); assign in source target order to _REQUIREMENTS_VARIANTS.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:46-46
In source order: Evaluate once 64; assign in source target order to _MAX_REQUIREMENT_INCLUDES.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:49-62
// Source signature: _split_name_version(specifier: str) -> tuple[str, str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _split_name_version(specifier) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:50-51
  if (the source predicate ';' in specifier is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:51-51
    In source order: Evaluate once specifier[:specifier.index(';')]; assign in source target order to specifier.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:52-53
  In source order: Evaluate once specifier.strip(); assign in source target order to specifier. Then Evaluate once specifier.find('['); assign in source target order to open_bracket.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:54-57
  if (the source predicate open_bracket >= 0 is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:55-55
    In source order: Evaluate once specifier.find(']'); assign in source target order to close_bracket.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:56-57
    if (the source predicate close_bracket > open_bracket is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:57-57
      In source order: Evaluate once specifier[:open_bracket] + specifier[close_bracket + 1:]; assign in source target order to specifier.
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:58-61
  for each separator in _VERSION_SEPARATORS {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:59-59
    In source order: Evaluate once specifier.find(separator); assign in source target order to index.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:60-61
    if (the source predicate index >= 0 is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:61-61
      End this invocation with (specifier[:index].strip(), specifier[index:].strip()).
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:62-62
  End this invocation with (specifier.strip(), '').
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:65-68
// Source signature: load_requirements_dependencies(reader: ManifestReader, config: ProjectConfig) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn load_requirements_dependencies(reader, config) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:66-66
  In source order: For seen, assign set(); source annotation set[str].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:67-68
  for each relative in reader.by_base_name(*_REQUIREMENTS_VARIANTS) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:68-68
    In source order: Evaluate _parse_requirements_file(reader, relative, config, seen); retain side effects and discard the expression result.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:71-103
// Source signature: _parse_requirements_file(reader: ManifestReader, relative: str, config: ProjectConfig, seen: set[str]) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _parse_requirements_file(reader, relative, config, seen) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:74-74
  In source order: Evaluate once posixpath.normpath(relative); assign in source target order to normalized.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:75-76
  if (the source predicate normalized in seen or len(seen) >= _MAX_REQUIREMENT_INCLUDES is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:76-76
    End this invocation with None.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:77-78
  In source order: Evaluate seen.add(normalized); retain side effects and discard the expression result. Then Evaluate once reader.read_text(normalized); assign in source target order to text.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:79-80
  if (the source predicate text is None is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:80-80
    End this invocation with None.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:81-82
  In source order: Evaluate once text.split(source_literal_81_23); assign in source target order to lines. Then Evaluate once 0; assign in source target order to index.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:83-103
  while (the source predicate index < len(lines) is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:84-85
    In source order: Evaluate once lines[index]; assign in source target order to line. Then Apply source augmented assignment index += 1 with source evaluation/in-place semantics.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:86-88
    while (the source predicate line.rstrip(' \t').endswith('\\') and index < len(lines) is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:87-88
      In source order: Evaluate once line.rstrip(' \t')[:-1] + lines[index]; assign in source target order to line. Then Apply source augmented assignment index += 1 with source evaluation/in-place semantics.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:89-89
    In source order: Evaluate once _INLINE_COMMENT.sub('', line).strip(); assign in source target order to line.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:90-91
    if (the source predicate not line or line.startswith('#') is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:91-91
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:92-95
    if (the source predicate line.startswith(('-r ', '-c ')) is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:93-94
      In source order: Evaluate once posixpath.join(posixpath.dirname(normalized), line[3:].strip()); assign in source target order to include. Then Evaluate _parse_requirements_file(reader, include, config, seen); retain side effects and discard the expression result.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:95-95
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:96-97
    if (the source predicate line.startswith('-') is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:97-97
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:98-99
    if (the source predicate ' --' in line is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:99-99
      In source order: Evaluate once line[:line.index(' --')]; assign in source target order to line.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:100-100
    In source order: Evaluate once _split_name_version(line); assign in source target order to (name, version).
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:101-103
    if (the source predicate name and _VALID_PACKAGE.match(name) is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:103-103
      In source order: Evaluate config.add_dependency(DependencyRecord(name, version, 'requirements.txt')); retain side effects and discard the expression result.
    }
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:106-117
// Source signature: _poetry_version(value: object) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _poetry_version(value) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:107-108
  if (the source predicate isinstance(value, str) is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:108-108
    End this invocation with value.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:109-109
  In source order: Evaluate once as_mapping(value); assign in source target order to mapping.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:110-116
  if (the source predicate mapping is not None is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:111-111
    In source order: Evaluate once as_str(mapping.get('version')); assign in source target order to version.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:112-113
    if (the source predicate version is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:113-113
      End this invocation with version.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:114-114
    In source order: Evaluate once as_str(mapping.get('git')); assign in source target order to git.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:115-116
    if (the source predicate git is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:116-116
      End this invocation with 'git:' + git.
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:117-117
  End this invocation with ''.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:120-126
// Source signature: _add_specifiers(config: ProjectConfig, entries: object, relative: str, *, dev: bool) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _add_specifiers(config, entries, relative, dev) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:121-126
  for each entry in string_list(entries) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:122-122
    In source order: Evaluate once _split_name_version(entry); assign in source target order to (name, version).
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:123-126
    if (the source predicate name is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:124-126
      In source order: Evaluate config.add_dependency(DependencyRecord(name, version, relative, dev, DEV_SCOPE if dev else '')); retain side effects and discard the expression result.
    }
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:129-161
// Source signature: load_pyproject_dependencies(reader: ManifestReader, config: ProjectConfig) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn load_pyproject_dependencies(reader, config) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:130-161
  for each relative in reader.by_base_name('pyproject.toml') {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:131-132
    In source order: Evaluate once reader.read_text(relative); assign in source target order to text. Then Evaluate once parse_toml(text) if text is not None else None; assign in source target order to parsed.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:133-134
    if (the source predicate parsed is None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:134-134
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:135-137
    In source order: Evaluate once mapping_at(parsed, 'project'); assign in source target order to project. Then Evaluate once project.get('dependencies'); assign in source target order to dependencies. Then Evaluate once as_mapping(project.get('optional-dependencies')) or {}; assign in source target order to optional.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:138-143
    if (the source predicate string_list(dependencies) or optional is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:139-139
      In source order: Evaluate _add_specifiers(config, dependencies, relative, dev=False); retain side effects and discard the expression result.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:140-142
      for each (group, entries) in optional.items() {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:141-142
        In source order: Evaluate once 'dev' in group or 'test' in group; assign in source target order to dev. Then Evaluate _add_specifiers(config, entries, relative, dev=dev); retain side effects and discard the expression result.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:143-143
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:144-145
    In source order: Evaluate once mapping_at(parsed, 'tool', 'poetry'); assign in source target order to poetry. Then Evaluate once as_mapping(poetry.get('dependencies')) or {}; assign in source target order to main_dependencies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:146-149
    for each (name, value) in main_dependencies.items() {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:147-148
      if (the source predicate name.lower() == 'python' is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:148-148
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:149-149
      In source order: Evaluate config.add_dependency(DependencyRecord(name, _poetry_version(value), relative)); retain side effects and discard the expression result.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:150-150
    In source order: Evaluate once as_mapping(poetry.get('group')) or {}; assign in source target order to groups.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:151-161
    for each (group_name, group) in groups.items() {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:152-153
      In source order: Evaluate once mapping_at(group, 'dependencies'); assign in source target order to entries. Then Evaluate once 'dev' in group_name or 'test' in group_name; assign in source target order to dev.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:154-161
      for each (name, value) in entries.items() {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:155-156
        if (the source predicate name.lower() == 'python' is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:156-156
          Continue the immediately enclosing source loop at its next iteration.
        }
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:157-161
        In source order: Evaluate config.add_dependency(DependencyRecord(name, _poetry_version(value), relative, dev, DEV_SCOPE if dev else '')); retain side effects and discard the expression result.
      }
    }
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:164-184
// Source signature: load_pyproject_manifests(reader: ManifestReader, config: ProjectConfig) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn load_pyproject_manifests(reader, config) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:165-184
  for each relative in reader.by_base_name('pyproject.toml') {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:166-167
    In source order: Evaluate once reader.read_text(relative); assign in source target order to text. Then Evaluate once parse_toml(text) if text is not None else None; assign in source target order to parsed.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:168-169
    if (the source predicate parsed is None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:169-169
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:170-173
    In source order: Evaluate once mapping_at(parsed, 'project'); assign in source target order to project. Then Evaluate once mapping_at(parsed, 'tool', 'poetry'); assign in source target order to poetry. Then Evaluate once as_str(project.get('name')); assign in source target order to name. Then Evaluate once as_str(project.get('version')); assign in source target order to version.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:174-176
    if (the source predicate not name is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:175-176
      In source order: Evaluate once as_str(poetry.get('name')); assign in source target order to name. Then Evaluate once as_str(poetry.get('version')); assign in source target order to version.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:177-177
    In source order: For members, assign []; source annotation list[str].
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:178-181
    for each tool_name in ('uv', 'pdm') {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:179-181
      In source order: Evaluate members.extend(string_list(mapping_at(parsed, 'tool', tool_name, 'workspace').get('members'))); retain side effects and discard the expression result.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:182-183
    if (the source predicate not name and members is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:183-183
      In source order: Evaluate once workspace_display_name(reader.root, relative); assign in source target order to name.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py:184-184
    In source order: Evaluate config.add_manifest(ManifestRecord(name, relative, 'python', version, tuple(members))); retain side effects and discard the expression result.
  }
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from context_graph_sdk.project.config import DEV_SCOPE, DependencyRecord, ManifestReader, ManifestRecord, ProjectConfig, workspace_display_name` at source line 22: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/project/config.py.sudo.md`.
- `from ._data import as_mapping, as_str, mapping_at, parse_toml, string_list` at source line 31: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/_data.py.sudo.md`.
