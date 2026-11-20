# vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/sbt.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/sbt.py.evidence.json`. SHA-256: `afe33b7d6a377bd1935b83a9c33e22e3649cdf173bef968b0a247e2c8ced3002`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/sbt.py:15-33
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import re; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.project.config import TEST_SCOPE, DependencyRecord, ManifestReader, ProjectConfig; preserve alias and import-time effects. Then Evaluate once re.compile('"([^"]*)"'); assign in source target order to _QUOTED.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/sbt.py:36-48
// Source signature: _seq_arguments(content: str) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _seq_arguments(content) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/sbt.py:37-37
  In source order: For arguments, assign []; source annotation list[str].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/sbt.py:38-47
  for each match in re.finditer('\\bSeq\\s*\\(', content) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/sbt.py:39-39
    In source order: Evaluate once 0; assign in source target order to depth.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/sbt.py:40-47
    for each index in range(match.end() - 1, len(content)) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/sbt.py:41-47
      if (the source predicate content[index] == '(' is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/sbt.py:42-42
        In source order: Apply source augmented assignment depth += 1 with source evaluation/in-place semantics.
      }
      else {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/sbt.py:43-47
        if (the source predicate content[index] == ')' is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/sbt.py:44-44
          In source order: Apply source augmented assignment depth -= 1 with source evaluation/in-place semantics.
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/sbt.py:45-47
          if (the source predicate depth == 0 is truthy) {
            // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/sbt.py:46-46
            In source order: Evaluate arguments.append(content[match.end():index]); retain side effects and discard the expression result.
            // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/sbt.py:47-47
            Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
          }
        }
      }
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/sbt.py:48-48
  End this invocation with arguments.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/sbt.py:51-71
// Source signature: _split_top_level(argument_list: str) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _split_top_level(argument_list) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/sbt.py:52-55
  In source order: For elements, assign []; source annotation list[str]. Then Evaluate once 0; assign in source target order to depth. Then For current, assign []; source annotation list[str]. Then Evaluate once False; assign in source target order to in_string.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/sbt.py:56-68
  for each char in argument_list {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/sbt.py:57-58
    if (the source predicate char == '"' is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/sbt.py:58-58
      In source order: Evaluate once not in_string; assign in source target order to in_string.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/sbt.py:59-67
    if (the source predicate not in_string is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/sbt.py:60-67
      if (the source predicate char in '([{' is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/sbt.py:61-61
        In source order: Apply source augmented assignment depth += 1 with source evaluation/in-place semantics.
      }
      else {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/sbt.py:62-67
        if (the source predicate char in ')]}' is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/sbt.py:63-63
          In source order: Apply source augmented assignment depth -= 1 with source evaluation/in-place semantics.
        }
        else {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/sbt.py:64-67
          if (the source predicate char == ',' and depth == 0 is truthy) {
            // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/sbt.py:65-66
            In source order: Evaluate elements.append(''.join(current)); retain side effects and discard the expression result. Then Evaluate once []; assign in source target order to current.
            // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/sbt.py:67-67
            Continue the immediately enclosing source loop at its next iteration.
          }
        }
      }
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/sbt.py:68-68
    In source order: Evaluate current.append(char); retain side effects and discard the expression result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/sbt.py:69-70
  if (the source predicate current is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/sbt.py:70-70
    In source order: Evaluate elements.append(''.join(current)); retain side effects and discard the expression result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/sbt.py:71-71
  End this invocation with elements.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/sbt.py:74-95
// Source signature: load_sbt_dependencies(reader: ManifestReader, config: ProjectConfig) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn load_sbt_dependencies(reader, config) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/sbt.py:75-95
  for each relative in reader.by_base_name('build.sbt') {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/sbt.py:76-76
    In source order: Evaluate once reader.read_text(relative); assign in source target order to text.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/sbt.py:77-78
    if (the source predicate text is None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/sbt.py:78-78
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/sbt.py:79-95
    for each argument_list in _seq_arguments(text) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/sbt.py:80-95
      for each element in _split_top_level(argument_list) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/sbt.py:81-82
        if (the source predicate '%' not in element is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/sbt.py:82-82
          Continue the immediately enclosing source loop at its next iteration.
        }
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/sbt.py:83-83
        In source order: Evaluate once _QUOTED.findall(element); assign in source target order to values.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/sbt.py:84-85
        if (the source predicate len(values) < 3 is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/sbt.py:85-85
          Continue the immediately enclosing source loop at its next iteration.
        }
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/sbt.py:86-95
        In source order: Evaluate once len(values) >= 4 and values[3].lower() == TEST_SCOPE; assign in source target order to dev. Then Evaluate config.add_dependency(DependencyRecord(source_template_89_24, values[2], relative, dev, TEST_SCOPE if dev else '')); retain side effects and discard the expression result.
      }
    }
  }
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from context_graph_sdk.project.config import TEST_SCOPE, DependencyRecord, ManifestReader, ProjectConfig` at source line 26: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/project/config.py.sudo.md`.
