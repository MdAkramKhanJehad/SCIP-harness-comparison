# vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py.evidence.json`. SHA-256: `3a18f7f0bc6eff0f53e0c5affeada9a097de262fb7501f0ee2ad2b8c208c589d`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:15-27
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import os; preserve alias and import-time effects. Then Resolve source import from collections.abc import Sequence; preserve alias and import-time effects. Then Resolve source import from dataclasses import dataclass; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:28-35
In source order: Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.errors import DiscoveryError; preserve alias and import-time effects. Then Resolve source import from .ignore import DEFAULT_IGNORE_PATTERNS, GitIgnoreMatcher, parse_ignore_lines; preserve alias and import-time effects. Then Resolve source import from .languages import detect_language, is_documentation_file; preserve alias and import-time effects. Then Evaluate once 10 * 1024 * 1024; assign in source target order to DEFAULT_MAX_FILE_BYTES.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:36-37
In source order: Evaluate once 50000; assign in source target order to DOCUMENTATION_CONTENT_BYTES. Then Evaluate once 500000; assign in source target order to DEFAULT_MAX_ENTRIES.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:41-45
// Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:40-40
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:41-45
interface WalkedFile {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:42-45
  In source order: For relative_path, declare without assigning a value; source annotation str. Then For size, declare without assigning a value; source annotation int. Then For language, declare without assigning a value; source annotation str. Then For is_documentation, declare without assigning a value; source annotation bool.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:49-53
// Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:48-48
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:49-53
interface RepositoryWalk {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:50-53
  In source order: For root, declare without assigning a value; source annotation str. Then For directories, declare without assigning a value; source annotation tuple[str, ...]. Then For files, declare without assigning a value; source annotation tuple[WalkedFile, ...]. Then For skipped, declare without assigning a value; source annotation tuple[str, ...].
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:56-64
// Source signature: _load_ignore_matcher(root: Path, extra_patterns: Sequence[str]) -> GitIgnoreMatcher
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _load_ignore_matcher(root, extra_patterns) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:57-57
  In source order: Evaluate once list(DEFAULT_IGNORE_PATTERNS); assign in source target order to lines.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:58-62
  for each name in ('.gitignore', '.contextgraphignore') {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:59-62
    Perform the following protected operations {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:60-60
      In source order: Evaluate lines.extend(parse_ignore_lines((root / name).read_text(encoding='utf-8'))); retain side effects and discard the expression result.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:61-62
    On the first matching source exception (OSError, UnicodeDecodeError), in handler order {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:62-62
      Continue the immediately enclosing source loop at its next iteration.
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:63-63
  In source order: Evaluate lines.extend(extra_patterns); retain side effects and discard the expression result.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:64-64
  End this invocation with GitIgnoreMatcher(tuple(lines)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:67-143
// Source signature: walk_repository(root: str | Path, *, extra_ignore_patterns: Sequence[str]=(), max_file_bytes: int=DEFAULT_MAX_FILE_BYTES, max_entries: int=DEFAULT_MAX_ENTRIES) -> RepositoryWalk
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn walk_repository(root, extra_ignore_patterns, max_file_bytes, max_entries) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:74-75
  if (the source predicate max_file_bytes <= 0 or max_entries <= 0 is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:75-75
    Raise DiscoveryError('walker bounds must be positive').
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:76-76
  In source order: Evaluate once Path(root); assign in source target order to input_root.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:79-80
  if (the source predicate input_root.is_symlink() is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:80-80
    Raise DiscoveryError(source_template_80_29).
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:81-81
  In source order: Evaluate once input_root.resolve(); assign in source target order to resolved_root.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:82-83
  if (the source predicate not resolved_root.is_dir() is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:83-83
    Raise DiscoveryError(source_template_83_29).
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:84-89
  In source order: Evaluate once _load_ignore_matcher(resolved_root, extra_ignore_patterns); assign in source target order to matcher. Then For directories, assign []; source annotation list[str]. Then For files, assign []; source annotation list[WalkedFile]. Then For skipped, assign []; source annotation list[str]. Then Evaluate once 0; assign in source target order to entry_count.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:91-91
  In source order: For pending, assign [(resolved_root, '')]; source annotation list[tuple[Path, str]].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:92-137
  while (the source predicate pending is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:93-93
    In source order: Evaluate once pending.pop(); assign in source target order to (directory, relative_prefix).
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:94-100
    Perform the following protected operations {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:95-96
      Enter source context managers left-to-right: os.scandir(directory) bound to scanner {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:96-96
        In source order: Evaluate once sorted(scanner, key=lambda entry: entry.name); assign in source target order to entries.
      }
      Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:97-100
    On the first matching source exception OSError, in handler order {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:98-99
      if (the source predicate relative_prefix is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:99-99
        In source order: Evaluate skipped.append(relative_prefix); retain side effects and discard the expression result.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:100-100
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:101-137
    for each entry in entries {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:102-103
      In source order: Evaluate once source_template_102_23 if relative_prefix else entry.name; assign in source target order to relative. Then Apply source augmented assignment entry_count += 1 with source evaluation/in-place semantics.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:104-105
      if (the source predicate entry_count > max_entries is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:105-105
        Raise DiscoveryError(source_template_105_37).
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:106-107
      if (the source predicate entry.name.startswith('.') is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:107-107
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:108-110
      if (the source predicate entry.is_symlink() is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:109-109
        In source order: Evaluate skipped.append(relative); retain side effects and discard the expression result.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:110-110
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:111-115
      Perform the following protected operations {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:112-112
        In source order: Evaluate once entry.is_dir(follow_symlinks=False); assign in source target order to is_dir.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:113-115
      On the first matching source exception OSError, in handler order {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:114-114
        In source order: Evaluate skipped.append(relative); retain side effects and discard the expression result.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:115-115
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:116-117
      if (the source predicate matcher.matches(relative, is_dir=is_dir) is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:117-117
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:118-121
      if (the source predicate is_dir is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:119-120
        In source order: Evaluate directories.append(relative); retain side effects and discard the expression result. Then Evaluate pending.append((Path(entry.path), relative)); retain side effects and discard the expression result.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:121-121
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:122-126
      Perform the following protected operations {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:123-123
        In source order: Evaluate once entry.stat(follow_symlinks=False).st_size; assign in source target order to size.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:124-126
      On the first matching source exception OSError, in handler order {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:125-125
        In source order: Evaluate skipped.append(relative); retain side effects and discard the expression result.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:126-126
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:127-129
      if (the source predicate size > max_file_bytes is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:128-128
        In source order: Evaluate skipped.append(relative); retain side effects and discard the expression result.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:129-129
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:130-137
      In source order: Evaluate files.append(WalkedFile(relative, size, detect_language(entry.name), is_documentation_file(relative))); retain side effects and discard the expression result.
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:138-143
  End this invocation with RepositoryWalk(str(resolved_root), tuple(sorted(directories)), tuple(sorted(files, key=lambda item: item.relative_path)), tuple(sorted(skipped))).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:146-174
// Source signature: read_documentation_text(root: str | Path, relative_path: str, *, max_bytes: int=DOCUMENTATION_CONTENT_BYTES) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn read_documentation_text(root, relative_path, max_bytes) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:152-158
  In source order: Retain source documentation literal source_literal_152_4; it is not a model call. Then Evaluate once _resolve_inside_root(Path(root).resolve(), relative_path); assign in source target order to path.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:159-163
  Perform the following protected operations {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:160-161
    Enter source context managers left-to-right: path.open('rb') bound to handle {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:161-161
      In source order: Evaluate once handle.read(max_bytes + 4); assign in source target order to data.
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:162-163
  On the first matching source exception OSError, in handler order {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:163-163
    End this invocation with ''.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:164-164
  In source order: Evaluate once data[:max_bytes]; assign in source target order to truncated.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:165-173
  if (the source predicate len(data) > max_bytes is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:166-173
    for each trim in range(4) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:167-167
      In source order: Evaluate once truncated[:max_bytes - trim] if trim else truncated; assign in source target order to candidate.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:168-173
      Perform the following protected operations {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:169-169
        End this invocation with candidate.decode('utf-8').
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:170-173
      On the first matching source exception UnicodeDecodeError as error, in handler order {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:171-172
        if (the source predicate error.reason == 'unexpected end of data' and error.start >= len(candidate) - 3 is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:172-172
          Continue the immediately enclosing source loop at its next iteration.
        }
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:173-173
        Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
      }
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:174-174
  End this invocation with truncated.decode('utf-8', errors='replace').
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:177-184
// Source signature: _resolve_inside_root(root: Path, relative_path: str) -> Path
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _resolve_inside_root(root, relative_path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:178-178
  In source order: Evaluate once Path(relative_path); assign in source target order to candidate.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:179-180
  if (the source predicate candidate.is_absolute() or '..' in candidate.parts is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:180-180
    Raise DiscoveryError(source_template_180_29).
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:181-181
  In source order: Evaluate once (root / candidate).resolve(); assign in source target order to resolved.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:182-183
  if (the source predicate not resolved.is_relative_to(root) is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:183-183
    Raise DiscoveryError(source_template_183_29).
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py:184-184
  End this invocation with resolved.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from context_graph_sdk.errors import DiscoveryError` at source line 30: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/errors.py.sudo.md`.
- `from .ignore import DEFAULT_IGNORE_PATTERNS, GitIgnoreMatcher, parse_ignore_lines` at source line 32: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/discovery/ignore.py.sudo.md`.
- `from .languages import detect_language, is_documentation_file` at source line 33: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/discovery/languages.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../../../prompt_representation/vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py.sudo.md). Exact strings in the evidence asset support this conversion.
