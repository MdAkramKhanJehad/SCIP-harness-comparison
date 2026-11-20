# vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/golang.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/golang.py.evidence.json`. SHA-256: `416d07b3868719bc10915514542fe0cf664ee33b4764172a8f441659c8987f6e`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/golang.py:15-29
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import re; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.project.config import DependencyRecord, ManifestReader, ManifestRecord, ProjectConfig, workspace_display_name; preserve alias and import-time effects. Then Evaluate once re.compile('//.*$'); assign in source target order to _COMMENT.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/golang.py:32-55
// Source signature: _directive_lines(text: str, keyword: str) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _directive_lines(text, keyword) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/golang.py:33-35
  In source order: Retain source documentation literal source_literal_33_4; it is not a model call. Then For lines, assign []; source annotation list[str]. Then Evaluate once False; assign in source target order to in_block.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/golang.py:36-54
  for each raw in text.split(source_literal_36_26) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/golang.py:37-37
    In source order: Evaluate once _COMMENT.sub('', raw).strip(); assign in source target order to line.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/golang.py:38-39
    if (the source predicate not line is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/golang.py:39-39
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/golang.py:40-45
    if (the source predicate in_block is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/golang.py:41-43
      if (the source predicate line == ')' is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/golang.py:42-42
        In source order: Evaluate once False; assign in source target order to in_block.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/golang.py:43-43
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/golang.py:44-44
      In source order: Evaluate lines.append(line); retain side effects and discard the expression result.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/golang.py:45-45
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/golang.py:46-48
    if (the source predicate line == source_template_46_19 is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/golang.py:47-47
      In source order: Evaluate once True; assign in source target order to in_block.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/golang.py:48-48
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/golang.py:49-54
    if (the source predicate line.startswith(keyword + ' ') is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/golang.py:50-50
      In source order: Evaluate once line[len(keyword) + 1:].strip(); assign in source target order to argument.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/golang.py:51-54
      if (the source predicate argument == '(' is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/golang.py:52-52
        In source order: Evaluate once True; assign in source target order to in_block.
      }
      else {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/golang.py:53-54
        if (the source predicate argument is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/golang.py:54-54
          In source order: Evaluate lines.append(argument); retain side effects and discard the expression result.
        }
      }
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/golang.py:55-55
  End this invocation with lines.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/golang.py:58-63
// Source signature: _module_path(text: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _module_path(text) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/golang.py:59-62
  for each line in text.split(source_literal_59_27) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/golang.py:60-60
    In source order: Evaluate once _COMMENT.sub('', line).strip(); assign in source target order to stripped.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/golang.py:61-62
    if (the source predicate stripped.startswith('module ') is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/golang.py:62-62
      End this invocation with stripped[len('module '):].strip().
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/golang.py:63-63
  End this invocation with ''.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/golang.py:66-94
// Source signature: load_go_dependencies(reader: ManifestReader, config: ProjectConfig) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn load_go_dependencies(reader, config) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/golang.py:67-94
  for each relative in reader.by_base_name('go.mod') {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/golang.py:68-68
    In source order: Evaluate once reader.read_text(relative); assign in source target order to text.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/golang.py:69-70
    if (the source predicate text is None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/golang.py:70-70
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/golang.py:71-71
    In source order: For replacements, assign {}; source annotation dict[str, tuple[str, str]].
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/golang.py:72-83
    for each line in _directive_lines(text, 'replace') {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/golang.py:73-74
      if (the source predicate '=>' not in line is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/golang.py:74-74
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/golang.py:75-77
      In source order: Evaluate once (part.strip() for part in line.split('=>', 1)); assign in source target order to (old_part, new_part). Then Evaluate once old_part.split(); assign in source target order to old_fields. Then Evaluate once new_part.split(); assign in source target order to new_fields.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/golang.py:78-79
      if (the source predicate not old_fields or not new_fields is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/golang.py:79-79
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/golang.py:80-83
      In source order: Evaluate once new_fields[0]; assign in source target order to new_path. Then Evaluate once new_fields[1] if len(new_fields) > 1 else ''; assign in source target order to new_version. Then Evaluate once source_template_82_18 if len(old_fields) > 1 else old_fields[0]; assign in source target order to key. Then Evaluate once (new_path, new_version); assign in source target order to replacements[key].
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/golang.py:84-94
    for each line in _directive_lines(text, 'require') {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/golang.py:85-85
      In source order: Evaluate once line.split(); assign in source target order to fields.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/golang.py:86-87
      if (the source predicate len(fields) < 2 is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/golang.py:87-87
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/golang.py:88-89
      In source order: Evaluate once (fields[0], fields[1]); assign in source target order to (name, version). Then Evaluate once replacements.get(source_template_89_43) or replacements.get(name); assign in source target order to replacement.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/golang.py:90-93
      if (the source predicate replacement is not None is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/golang.py:91-91
        In source order: Evaluate once replacement[0]; assign in source target order to name.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/golang.py:92-93
        if (the source predicate replacement[1] is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/golang.py:93-93
          In source order: Evaluate once replacement[1]; assign in source target order to version.
        }
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/golang.py:94-94
      In source order: Evaluate config.add_dependency(DependencyRecord(name, version, relative)); retain side effects and discard the expression result.
    }
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/golang.py:97-116
// Source signature: load_go_manifests(reader: ManifestReader, config: ProjectConfig) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn load_go_manifests(reader, config) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/golang.py:98-109
  for each relative in reader.by_base_name('go.work') {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/golang.py:99-99
    In source order: Evaluate once reader.read_text(relative); assign in source target order to text.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/golang.py:100-101
    if (the source predicate text is None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/golang.py:101-101
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/golang.py:102-109
    In source order: Evaluate once tuple((line.split()[0].replace('\\', '/') for line in _directive_lines(text, 'use') if line)); assign in source target order to members. Then Evaluate config.add_manifest(ManifestRecord(workspace_display_name(reader.root, relative), relative, 'go', '', members)); retain side effects and discard the expression result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/golang.py:110-116
  for each relative in reader.by_base_name('go.mod') {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/golang.py:111-111
    In source order: Evaluate once reader.read_text(relative); assign in source target order to text.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/golang.py:112-113
    if (the source predicate text is None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/golang.py:113-113
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/golang.py:114-114
    In source order: Evaluate once _module_path(text); assign in source target order to module_path.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/golang.py:115-116
    if (the source predicate module_path is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/golang.py:116-116
      In source order: Evaluate config.add_manifest(ManifestRecord(module_path, relative, 'go')); retain side effects and discard the expression result.
    }
  }
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from context_graph_sdk.project.config import DependencyRecord, ManifestReader, ManifestRecord, ProjectConfig, workspace_display_name` at source line 21: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/project/config.py.sudo.md`.
