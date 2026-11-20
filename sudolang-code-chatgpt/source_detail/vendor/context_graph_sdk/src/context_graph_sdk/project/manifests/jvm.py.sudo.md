# vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py.evidence.json`. SHA-256: `b07d8a48bda62f1f9ec846be2f121ee14b9423f4af3304a3aa80a7be5a9e7a9f`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:15-29
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import re; preserve alias and import-time effects. Then Resolve source import import xml.etree.ElementTree as ElementTree; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.project.config import TEST_SCOPE, DependencyRecord, ManifestReader, ManifestRecord, ProjectConfig, workspace_display_name; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:31-31
In source order: Evaluate once re.compile('\\$\\{([^}]+)\\}'); assign in source target order to _MAVEN_PROPERTY.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:34-35
// Source signature: _local_name(tag: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _local_name(tag) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:35-35
  End this invocation with tag.rsplit('}', 1)[-1].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:38-42
// Source signature: _child_text(element: ElementTree.Element, name: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _child_text(element, name) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:39-41
  for each child in element {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:40-41
    if (the source predicate _local_name(child.tag) == name is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:41-41
      End this invocation with (child.text or '').strip().
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:42-42
  End this invocation with ''.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:45-46
// Source signature: _children(element: ElementTree.Element, name: str) -> list[ElementTree.Element]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _children(element, name) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:46-46
  End this invocation with [child for child in element if _local_name(child.tag) == name].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:49-54
// Source signature: _parse_pom(text: str) -> ElementTree.Element | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _parse_pom(text) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:50-53
  Perform the following protected operations {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:51-51
    In source order: Evaluate once ElementTree.fromstring(text); assign in source target order to root.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:52-53
  On the first matching source exception ElementTree.ParseError, in handler order {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:53-53
    End this invocation with None.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:54-54
  End this invocation with root if _local_name(root.tag) == 'project' else None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:57-58
// Source signature: _expand(value: str, properties: dict[str, str]) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _expand(value, properties) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:58-58
  End this invocation with _MAVEN_PROPERTY.sub(lambda match: properties.get(match.group(1), match.group(0)), value).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:61-76
// Source signature: _pom_properties(root: ElementTree.Element) -> tuple[dict[str, str], str, str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _pom_properties(root) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:62-66
  In source order: Evaluate once next(iter(_children(root, 'parent')), None); assign in source target order to parent. Then Evaluate once _child_text(parent, 'groupId') if parent is not None else ''; assign in source target order to parent_group. Then Evaluate once _child_text(parent, 'version') if parent is not None else ''; assign in source target order to parent_version. Then Evaluate once _child_text(root, 'groupId') or parent_group; assign in source target order to group_id. Then Evaluate once _child_text(root, 'version') or parent_version; assign in source target order to version.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:67-67
  In source order: For properties, assign {}; source annotation dict[str, str].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:68-70
  for each props in _children(root, 'properties') {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:69-70
    for each prop in props {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:70-70
      In source order: Evaluate once (prop.text or '').strip(); assign in source target order to properties[_local_name(prop.tag)].
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:71-71
  In source order: Evaluate once _child_text(root, 'artifactId'); assign in source target order to artifact_id.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:72-75
  for each (key, value) in (('groupId', group_id), ('artifactId', artifact_id), ('version', version)) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:73-75
    if (the source predicate value is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:74-75
      In source order: Evaluate once value; assign in source target order to properties[f'project.{key}']. Then Evaluate once value; assign in source target order to properties[f'pom.{key}'].
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:76-76
  End this invocation with (properties, group_id, version).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:79-102
// Source signature: _add_pom_dependency(element: ElementTree.Element, properties: dict[str, str], relative: str, config: ProjectConfig, *, management: bool) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _add_pom_dependency(element, properties, relative, config, management) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:87-90
  In source order: Evaluate once _expand(_child_text(element, 'groupId'), properties); assign in source target order to group_id. Then Evaluate once _expand(_child_text(element, 'artifactId'), properties); assign in source target order to artifact_id. Then Evaluate once _expand(_child_text(element, 'version'), properties); assign in source target order to version. Then Evaluate once _child_text(element, 'scope'); assign in source target order to scope.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:91-92
  if (the source predicate '${' in group_id or '${' in artifact_id is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:92-92
    End this invocation with None.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:93-94
  if (the source predicate management and scope == 'import' is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:94-94
    End this invocation with None.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:95-96
  if (the source predicate not management and scope in ('provided', 'system') is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:96-96
    End this invocation with None.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:97-102
  In source order: Evaluate once scope == TEST_SCOPE; assign in source target order to dev. Then Evaluate config.add_dependency(DependencyRecord(source_template_100_12, version, relative, dev, TEST_SCOPE if dev else '')); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:105-118
// Source signature: load_pom_dependencies(reader: ManifestReader, config: ProjectConfig) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn load_pom_dependencies(reader, config) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:106-118
  for each relative in reader.by_base_name('pom.xml') {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:107-108
    In source order: Evaluate once reader.read_text(relative); assign in source target order to text. Then Evaluate once _parse_pom(text) if text is not None else None; assign in source target order to root.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:109-110
    if (the source predicate root is None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:110-110
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:111-111
    In source order: Evaluate once _pom_properties(root); assign in source target order to (properties, _, _).
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:112-114
    for each dependencies in _children(root, 'dependencies') {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:113-114
      for each dependency in _children(dependencies, 'dependency') {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:114-114
        In source order: Evaluate _add_pom_dependency(dependency, properties, relative, config, management=False); retain side effects and discard the expression result.
      }
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:115-118
    for each management in _children(root, 'dependencyManagement') {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:116-118
      for each dependencies in _children(management, 'dependencies') {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:117-118
        for each dependency in _children(dependencies, 'dependency') {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:118-118
          In source order: Evaluate _add_pom_dependency(dependency, properties, relative, config, management=True); retain side effects and discard the expression result.
        }
      }
    }
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:121-138
// Source signature: load_pom_manifests(reader: ManifestReader, config: ProjectConfig) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn load_pom_manifests(reader, config) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:122-138
  for each relative in reader.by_base_name('pom.xml') {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:123-124
    In source order: Evaluate once reader.read_text(relative); assign in source target order to text. Then Evaluate once _parse_pom(text) if text is not None else None; assign in source target order to root.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:125-126
    if (the source predicate root is None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:126-126
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:127-138
    In source order: Evaluate once _pom_properties(root); assign in source target order to (_, _, version). Then Evaluate once [module_text for modules in _children(root, 'modules') for module in _children(modules, 'module') if (module_text := (module.text or '').strip())]; assign in source target order to modules. Then Evaluate config.add_manifest(ManifestRecord(_child_text(root, 'artifactId'), relative, 'java', version, tuple(modules))); retain side effects and discard the expression result.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:141-141
In source order: Evaluate once re.compile('include(?:Flat)?\\s*\\(([^)]*)\\)|include\\s+([^\\n]+)'); assign in source target order to _GRADLE_INCLUDE.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:144-185
// Source signature: strip_gradle_comments(content: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn strip_gradle_comments(content) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:145-149
  In source order: For output, assign []; source annotation list[str]. Then Evaluate once False; assign in source target order to in_single. Then Evaluate once False; assign in source target order to in_double. Then Evaluate once False; assign in source target order to in_block. Then Evaluate once False; assign in source target order to escaped.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:150-150
  In source order: Evaluate once 0; assign in source target order to index.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:151-184
  while (the source predicate index < len(content) is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:152-152
    In source order: Evaluate once content[index]; assign in source target order to char.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:153-158
    if (the source predicate in_block is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:154-156
      if (the source predicate char == '*' and content[index + 1:index + 2] == '/' is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:155-156
        In source order: Evaluate once False; assign in source target order to in_block. Then Apply source augmented assignment index += 1 with source evaluation/in-place semantics.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:157-157
      In source order: Apply source augmented assignment index += 1 with source evaluation/in-place semantics.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:158-158
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:159-163
    if (the source predicate escaped is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:160-162
      In source order: Evaluate output.append(char); retain side effects and discard the expression result. Then Evaluate once False; assign in source target order to escaped. Then Apply source augmented assignment index += 1 with source evaluation/in-place semantics.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:163-163
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:164-168
    if (the source predicate char == '\\' is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:165-167
      In source order: Evaluate output.append(char); retain side effects and discard the expression result. Then Evaluate once True; assign in source target order to escaped. Then Apply source augmented assignment index += 1 with source evaluation/in-place semantics.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:168-168
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:169-178
    if (the source predicate not in_single and (not in_double) and (char == '/') is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:170-170
      In source order: Evaluate once content[index + 1:index + 2]; assign in source target order to following.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:171-174
      if (the source predicate following == '/' is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:172-173
        while (the source predicate index < len(content) and content[index] != source_literal_172_65 is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:173-173
          In source order: Apply source augmented assignment index += 1 with source evaluation/in-place semantics.
        }
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:174-174
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:175-178
      if (the source predicate following == '*' is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:176-177
        In source order: Evaluate once True; assign in source target order to in_block. Then Apply source augmented assignment index += 2 with source evaluation/in-place semantics.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:178-178
        Continue the immediately enclosing source loop at its next iteration.
      }
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:179-182
    if (the source predicate char == "'" and (not in_double) is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:180-180
      In source order: Evaluate once not in_single; assign in source target order to in_single.
    }
    else {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:181-182
      if (the source predicate char == '"' and (not in_single) is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:182-182
        In source order: Evaluate once not in_double; assign in source target order to in_double.
      }
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:183-184
    In source order: Evaluate output.append(char); retain side effects and discard the expression result. Then Apply source augmented assignment index += 1 with source evaluation/in-place semantics.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:185-185
  End this invocation with ''.join(output).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:188-211
// Source signature: load_gradle_settings_manifests(reader: ManifestReader, config: ProjectConfig) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn load_gradle_settings_manifests(reader, config) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:189-211
  for each relative in reader.by_base_name('settings.gradle', 'settings.gradle.kts') {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:190-190
    In source order: Evaluate once reader.read_text(relative); assign in source target order to text.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:191-192
    if (the source predicate text is None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:192-192
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:193-195
    In source order: Evaluate once strip_gradle_comments(text); assign in source target order to content. Then For members, assign []; source annotation list[str]. Then For seen, assign set(); source annotation set[str].
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:196-202
    for each match in _GRADLE_INCLUDE.finditer(content) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:197-197
      In source order: Evaluate once match.group(1) or match.group(2) or ''; assign in source target order to arguments.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:198-202
      for each raw in arguments.split(',') {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:199-199
        In source order: Evaluate once raw.strip().strip('"\'').removeprefix(':').replace(':', '/'); assign in source target order to item.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:200-202
        if (the source predicate item and item not in seen is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:201-202
          In source order: Evaluate seen.add(item); retain side effects and discard the expression result. Then Evaluate members.append(item); retain side effects and discard the expression result.
        }
      }
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:203-211
    In source order: Evaluate config.add_manifest(ManifestRecord(workspace_display_name(reader.root, relative), relative, 'java', '', tuple(members))); retain side effects and discard the expression result.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:214-214
In source order: Evaluate once re.compile('^\\s*(\\w+)\\s*\\(?\\s*([\'\\"])([^\'\\"]+)\\2', re.MULTILINE); assign in source target order to _GRADLE_DEPENDENCY_STATEMENT.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:217-223
// Source signature: _gradle_scope(configuration: str) -> tuple[bool, str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _gradle_scope(configuration) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:218-218
  In source order: Evaluate once configuration.lower(); assign in source target order to name.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:219-220
  if (the source predicate 'test' in name is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:220-220
    End this invocation with (True, TEST_SCOPE).
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:221-222
  if (the source predicate 'build' in name or name == 'classpath' or 'processor' in name or (name == 'kapt') is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:222-222
    End this invocation with (True, 'build').
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:223-223
  End this invocation with (False, '').
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:226-238
// Source signature: _dependencies_blocks(content: str) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _dependencies_blocks(content) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:227-227
  In source order: For blocks, assign []; source annotation list[str].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:228-237
  for each match in re.finditer('\\bdependencies\\s*\\{', content) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:229-229
    In source order: Evaluate once 0; assign in source target order to depth.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:230-237
    for each index in range(match.end() - 1, len(content)) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:231-237
      if (the source predicate content[index] == '{' is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:232-232
        In source order: Apply source augmented assignment depth += 1 with source evaluation/in-place semantics.
      }
      else {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:233-237
        if (the source predicate content[index] == '}' is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:234-234
          In source order: Apply source augmented assignment depth -= 1 with source evaluation/in-place semantics.
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:235-237
          if (the source predicate depth == 0 is truthy) {
            // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:236-236
            In source order: Evaluate blocks.append(content[match.end():index]); retain side effects and discard the expression result.
            // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:237-237
            Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
          }
        }
      }
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:238-238
  End this invocation with blocks.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:241-258
// Source signature: load_gradle_build_dependencies(reader: ManifestReader, config: ProjectConfig) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn load_gradle_build_dependencies(reader, config) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:242-258
  for each relative in reader.by_base_name('build.gradle', 'build.gradle.kts') {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:243-243
    In source order: Evaluate once reader.read_text(relative); assign in source target order to text.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:244-245
    if (the source predicate text is None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:245-245
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:246-246
    In source order: Evaluate once strip_gradle_comments(text); assign in source target order to content.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:247-258
    for each block in _dependencies_blocks(content) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:248-258
      for each match in _GRADLE_DEPENDENCY_STATEMENT.finditer(block) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:249-249
        In source order: Evaluate once match.group(3); assign in source target order to coordinates.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:250-251
        if (the source predicate '$' in coordinates is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:251-251
          Continue the immediately enclosing source loop at its next iteration.
        }
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:252-252
        In source order: Evaluate once coordinates.split(':'); assign in source target order to parts.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:253-254
        if (the source predicate len(parts) != 3 is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:254-254
          Continue the immediately enclosing source loop at its next iteration.
        }
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:255-258
        In source order: Evaluate once _gradle_scope(match.group(1)); assign in source target order to (dev, scope). Then Evaluate config.add_dependency(DependencyRecord(source_template_257_37, parts[2], relative, dev, scope)); retain side effects and discard the expression result.
      }
    }
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:261-285
// Source signature: load_gradle_lockfile_dependencies(reader: ManifestReader, config: ProjectConfig) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn load_gradle_lockfile_dependencies(reader, config) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:262-285
  for each relative in reader.by_base_name('gradle.lockfile', 'buildscript-gradle.lockfile') {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:263-263
    In source order: Evaluate once reader.read_text(relative); assign in source target order to text.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:264-265
    if (the source predicate text is None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:265-265
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:266-285
    for each raw in text.split(source_literal_266_30) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:267-267
      In source order: Evaluate once raw.strip(); assign in source target order to line.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:268-269
      if (the source predicate not line or line.startswith('#') is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:269-269
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:270-270
      In source order: Evaluate once line.split(':', 2); assign in source target order to parts.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:271-272
      if (the source predicate len(parts) != 3 is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:272-272
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py:273-285
      In source order: Evaluate once parts[2].partition('='); assign in source target order to (version, _, class_paths). Then Evaluate once bool(class_paths) and all((path.startswith('test') for path in class_paths.split(','))); assign in source target order to dev. Then Evaluate config.add_dependency(DependencyRecord(source_template_279_20, version, relative, dev, TEST_SCOPE if dev else '')); retain side effects and discard the expression result.
    }
  }
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from context_graph_sdk.project.config import TEST_SCOPE, DependencyRecord, ManifestReader, ManifestRecord, ProjectConfig, workspace_display_name` at source line 22: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/project/config.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../../../../prompt_representation/vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py.sudo.md). Exact strings in the evidence asset support this conversion.
