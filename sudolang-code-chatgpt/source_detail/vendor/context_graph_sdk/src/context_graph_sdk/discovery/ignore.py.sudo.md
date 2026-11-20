# vendor/context_graph_sdk/src/context_graph_sdk/discovery/ignore.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vendor/context_graph_sdk/src/context_graph_sdk/discovery/ignore.py.evidence.json`. SHA-256: `9e4a4632abcfceea5e77d0b8956103a347d8999f526ec3032c1ebe6689d0f920`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/ignore.py:15-141
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import re; preserve alias and import-time effects. Then Resolve source import from dataclasses import dataclass; preserve alias and import-time effects. Then For DEFAULT_IGNORE_PATTERNS, assign ('.git/', '.svn/', '.hg/', '.bzr/', '.idea/', '.vscode/', '.vs/', 'node_modules/', 'vendor/', 'venv/', '.venv/', '__pycache__/', 'site-packages/', '.mypy_cache/', '.pytest_cache/', 'dist/', 'out/', 'output/', 'bin/', 'obj/', 'target/', '.next/', '.nuxt/', '.vercel/', '.parcel-cache/', '.turbo/', 'coverage/', '__tests__/', '__mocks__/', '.nyc_output/', '*.exe', '*.bin', '*.o', '*.so', '*.dll', '*.dylib', '*.class', '*.jar', '*.zip', '*.tar', '*.gz', '*.rar', '*.png', '*.jpg', '*.jpeg', '*.gif', '*.svg', '*.ico', '*.webp', '*.pdf', '*.wasm', '*.pyc', '*.doc', '*.docx', '*.mp4', '*.mp3', '*.wav', '*.woff', '*.woff2', '*.ttf', '*.db', '*.sqlite', '*.pem', '*.key', '*.crt', '*.csv', '*.parquet', '*.pkl', '*.map', '*.lock', '*.min.js', '*.bundle.js', '*.chunk.js', '*.min.css', '*.generated.ts', '*.generated.js', '*.generated.go', '*.d.ts', '*.pb.go', '*.pb.gw.go', '*_generated.go', '*_gen.go', '*_string.go', '*.zz_generated.go', '*.deepcopy.go', '*_enumer.go', '*.twirp.go', '*_easyjson.go', '*_ffjson.go', '*.mock.go', '*_mock.go', '*.pb.scala', 'package-lock.json', 'yarn.lock', 'pnpm-lock.yaml', 'composer.lock', 'Cargo.lock', 'go.sum', '.gitignore', '.gitattributes', '.npmrc', '.editorconfig', '.prettierrc', '.eslintignore', '.dockerignore', 'LICENSE', 'LICENSE.md', 'CHANGELOG.md', '.env', '.env.local', '.env.production'); source annotation tuple[str, ...].
// Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/ignore.py:144-152
// Source signature: parse_ignore_lines(text: str) -> tuple[str, ...]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn parse_ignore_lines(text) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/ignore.py:145-145
  In source order: For lines, assign []; source annotation list[str].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/ignore.py:146-151
  for each raw in text.split(source_literal_146_26) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/ignore.py:147-148
    In source order: Evaluate once raw.rstrip('\r'); assign in source target order to line. Then Evaluate once line.strip(); assign in source target order to stripped.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/ignore.py:149-150
    if (the source predicate not stripped or stripped.startswith('#') is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/ignore.py:150-150
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/ignore.py:151-151
    In source order: Evaluate lines.append(line); retain side effects and discard the expression result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/ignore.py:152-152
  End this invocation with tuple(lines).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/ignore.py:156-162
// Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/ignore.py:155-155
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/ignore.py:156-162
interface _CompiledPattern {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/ignore.py:157-162
  In source order: For regex, declare without assigning a value; source annotation re.Pattern[str]. Then For beneath_regex, declare without assigning a value; source annotation re.Pattern[str]. Then For negated, declare without assigning a value; source annotation bool. Then For directory_only, declare without assigning a value; source annotation bool.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/ignore.py:165-204
// Source signature: _translate_glob(pattern: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _translate_glob(pattern) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/ignore.py:166-167
  In source order: For parts, assign []; source annotation list[str]. Then Evaluate once 0; assign in source target order to index.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/ignore.py:168-203
  while (the source predicate index < len(pattern) is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/ignore.py:169-169
    In source order: Evaluate once pattern[index]; assign in source target order to char.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/ignore.py:170-188
    if (the source predicate char == '*' is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/ignore.py:171-185
      if (the source predicate pattern[index:index + 2] == '**' is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/ignore.py:172-172
        In source order: Evaluate once index; assign in source target order to run_end.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/ignore.py:173-174
        while (the source predicate run_end < len(pattern) and pattern[run_end] == '*' is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/ignore.py:174-174
          In source order: Apply source augmented assignment run_end += 1 with source evaluation/in-place semantics.
        }
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/ignore.py:175-182
        if (the source predicate index > 0 and pattern[index - 1] == '/' and (pattern[run_end:run_end + 1] == '/') is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/ignore.py:180-181
          In source order: Evaluate parts.append('(?:[^/]+/)*'); retain side effects and discard the expression result. Then Evaluate once run_end + 1; assign in source target order to index.
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/ignore.py:182-182
          Continue the immediately enclosing source loop at its next iteration.
        }
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/ignore.py:183-184
        In source order: Evaluate parts.append('.*'); retain side effects and discard the expression result. Then Evaluate once run_end; assign in source target order to index.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/ignore.py:185-185
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/ignore.py:186-187
      In source order: Evaluate parts.append('[^/]*'); retain side effects and discard the expression result. Then Apply source augmented assignment index += 1 with source evaluation/in-place semantics.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/ignore.py:188-188
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/ignore.py:189-192
    if (the source predicate char == '?' is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/ignore.py:190-191
      In source order: Evaluate parts.append('[^/]'); retain side effects and discard the expression result. Then Apply source augmented assignment index += 1 with source evaluation/in-place semantics.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/ignore.py:192-192
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/ignore.py:193-201
    if (the source predicate char == '[' is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/ignore.py:194-194
      In source order: Evaluate once pattern.find(']', index + 1); assign in source target order to end.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/ignore.py:195-201
      if (the source predicate end > index is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/ignore.py:196-196
        In source order: Evaluate once pattern[index + 1:end]; assign in source target order to inner.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/ignore.py:197-198
        if (the source predicate inner.startswith('!') is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/ignore.py:198-198
          In source order: Evaluate once '^' + inner[1:]; assign in source target order to inner.
        }
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/ignore.py:199-200
        In source order: Evaluate parts.append('[' + inner.replace('\\', '\\\\') + ']'); retain side effects and discard the expression result. Then Evaluate once end + 1; assign in source target order to index.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/ignore.py:201-201
        Continue the immediately enclosing source loop at its next iteration.
      }
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/ignore.py:202-203
    In source order: Evaluate parts.append(re.escape(char)); retain side effects and discard the expression result. Then Apply source augmented assignment index += 1 with source evaluation/in-place semantics.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/ignore.py:204-204
  End this invocation with ''.join(parts).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/ignore.py:207-231
// Source signature: _compile_pattern(line: str) -> _CompiledPattern | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _compile_pattern(line) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/ignore.py:208-209
  In source order: Evaluate once line; assign in source target order to pattern. Then Evaluate once pattern.startswith('!'); assign in source target order to negated.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/ignore.py:210-211
  if (the source predicate negated is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/ignore.py:211-211
    In source order: Evaluate once pattern[1:]; assign in source target order to pattern.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/ignore.py:212-212
  In source order: Evaluate once pattern.rstrip(); assign in source target order to pattern.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/ignore.py:213-214
  if (the source predicate not pattern is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/ignore.py:214-214
    End this invocation with None.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/ignore.py:215-216
  In source order: Evaluate once pattern.endswith('/'); assign in source target order to directory_only. Then Evaluate once pattern.rstrip('/'); assign in source target order to pattern.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/ignore.py:217-218
  if (the source predicate not pattern is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/ignore.py:218-218
    End this invocation with None.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/ignore.py:219-220
  In source order: Evaluate once pattern.startswith('/'); assign in source target order to anchored. Then Evaluate once pattern.lstrip('/'); assign in source target order to pattern.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/ignore.py:221-223
  if (the source predicate pattern.startswith('**/') is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/ignore.py:222-223
    In source order: Evaluate once False; assign in source target order to anchored. Then Evaluate once pattern[3:]; assign in source target order to pattern.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/ignore.py:224-225
  if (the source predicate '/' in pattern is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/ignore.py:225-225
    In source order: Evaluate once True; assign in source target order to anchored.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/ignore.py:226-230
  In source order: Evaluate once _translate_glob(pattern); assign in source target order to body. Then Evaluate once '^' if anchored else '^(?:.*/)?'; assign in source target order to prefix. Then Evaluate once re.compile(prefix + body + '(?:/.*)?$'); assign in source target order to regex. Then Evaluate once re.compile(prefix + body + '/.*$'); assign in source target order to beneath_regex.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/ignore.py:231-231
  End this invocation with _CompiledPattern(regex, beneath_regex, negated, directory_only).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/ignore.py:234-249
interface GitIgnoreMatcher {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/ignore.py:235-235
  In source order: Retain source documentation literal source_literal_235_4; it is not a model call.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/ignore.py:237-239
  // Source signature: __init__(self, lines: tuple[str, ...]) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self, lines) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/ignore.py:238-239
    In source order: Evaluate once (_compile_pattern(line) for line in lines); assign in source target order to compiled. Then Evaluate once tuple((pattern for pattern in compiled if pattern is not None)); assign in source target order to self._patterns.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/ignore.py:241-249
  // Source signature: matches(self, relative_path: str, *, is_dir: bool) -> bool
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn matches(self, relative_path, is_dir) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/ignore.py:242-242
    In source order: Evaluate once False; assign in source target order to ignored.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/ignore.py:243-248
    for each pattern in self._patterns {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/ignore.py:244-246
      In source order: Evaluate once pattern.beneath_regex if pattern.directory_only and (not is_dir) else pattern.regex; assign in source target order to regex.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/ignore.py:247-248
      if (the source predicate regex.match(relative_path) is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/ignore.py:248-248
        In source order: Evaluate once not pattern.negated; assign in source target order to ignored.
      }
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/ignore.py:249-249
    End this invocation with ignored.
    If execution reaches this end, finish with the source implicit None result.
  }
}
```

## Local import links

No statically resolved in-checkout import; external calls remain explicit dependency boundaries.
