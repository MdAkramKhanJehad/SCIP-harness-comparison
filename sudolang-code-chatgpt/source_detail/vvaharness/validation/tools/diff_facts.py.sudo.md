# vvaharness/validation/tools/diff_facts.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/validation/tools/diff_facts.py.evidence.json`. SHA-256: `3ea8870f7af073b745bd432a4864cf84cf05e8e780ebbeef5e679087f68ff47d`.

```sudo
// Source: vvaharness/validation/tools/diff_facts.py:15-22
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from dataclasses import dataclass, field; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.constants.artifacts import DIFF_FILENAME; preserve alias and import-time effects.
// Source: vvaharness/validation/tools/diff_facts.py:23-37
In source order: Resolve source import from vvaharness.validation.constants.diff import ADDED_LINE, DEV_NULL_PATH, GIT_HEADER_MIN_TOKENS, GIT_HEADER_PREFIX, GIT_PATH_PREFIXES, HUNK_HEADER_RE, HUNK_NEW_START_GROUP, MARKER_PATH_START, NEW_FILE_MARKER, NO_NEWLINE_NOTE, OLD_FILE_MARKER, REMOVED_LINE, TRUST_BOUNDARY_RE; preserve alias and import-time effects.
// Source: vvaharness/validation/tools/diff_facts.py:40-41
// Source signature: _without_git_prefix(path: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _without_git_prefix(path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/tools/diff_facts.py:41-41
  End this invocation with path[2:] if path[:2] in GIT_PATH_PREFIXES else path.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/tools/diff_facts.py:44-45
// Source signature: _marker_path(marker_line: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _marker_path(marker_line) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/tools/diff_facts.py:45-45
  End this invocation with marker_line[MARKER_PATH_START:].split('\t')[0].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/tools/diff_facts.py:49-53
// Source: vvaharness/validation/tools/diff_facts.py:48-48
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass.
// Source: vvaharness/validation/tools/diff_facts.py:49-53
interface FileChange {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/validation/tools/diff_facts.py:50-53
  In source order: Retain source documentation literal source_literal_50_4; it is not a model call. Then For path, declare without assigning a value; source annotation str. Then For added_ranges, assign field(default_factory=list); source annotation list[tuple[int, int]].
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vvaharness/validation/tools/diff_facts.py:56-118
interface _DiffParser {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/validation/tools/diff_facts.py:57-57
  In source order: Retain source documentation literal source_literal_57_4; it is not a model call.
  // Source: vvaharness/validation/tools/diff_facts.py:59-66
  // Source signature: __init__(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/validation/tools/diff_facts.py:60-64
    In source order: For self.changes, assign []; source annotation list[FileChange]. Then For self.current_path, assign None; source annotation str | None. Then For self.old_path, assign None; source annotation str | None. Then For self.added_ranges, assign []; source annotation list[tuple[int, int]]. Then Evaluate once 0; assign in source target order to self.new_line_number.
    // Source: vvaharness/validation/tools/diff_facts.py:65-66
    In source order: For self.added_run_start, assign None; source annotation int | None. Then Evaluate once 0; assign in source target order to self.added_run_length.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/validation/tools/diff_facts.py:68-71
  // Source signature: _close_added_run(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _close_added_run(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/validation/tools/diff_facts.py:69-70
    if (the source predicate self.added_run_start is not None and self.added_run_length is truthy) {
      // Source: vvaharness/validation/tools/diff_facts.py:70-70
      In source order: Evaluate self.added_ranges.append((self.added_run_start, self.added_run_length)); retain side effects and discard the expression result.
    }
    // Source: vvaharness/validation/tools/diff_facts.py:71-71
    In source order: Evaluate once (None, 0); assign in source target order to (self.added_run_start, self.added_run_length).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/validation/tools/diff_facts.py:73-77
  // Source signature: _close_file(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _close_file(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/validation/tools/diff_facts.py:74-74
    In source order: Evaluate self._close_added_run(); retain side effects and discard the expression result.
    // Source: vvaharness/validation/tools/diff_facts.py:75-76
    if (the source predicate self.current_path is not None is truthy) {
      // Source: vvaharness/validation/tools/diff_facts.py:76-76
      In source order: Evaluate self.changes.append(FileChange(self.current_path, self.added_ranges)); retain side effects and discard the expression result.
    }
    // Source: vvaharness/validation/tools/diff_facts.py:77-77
    In source order: Evaluate once (None, None, []); assign in source target order to (self.current_path, self.old_path, self.added_ranges).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/validation/tools/diff_facts.py:79-92
  // Source signature: _consume_hunk_line(self, line: str) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _consume_hunk_line(self, line) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/validation/tools/diff_facts.py:80-80
    In source order: Evaluate once line[:1]; assign in source target order to prefix.
    // Source: vvaharness/validation/tools/diff_facts.py:81-92
    if (the source predicate prefix == ADDED_LINE is truthy) {
      // Source: vvaharness/validation/tools/diff_facts.py:82-83
      if (the source predicate self.added_run_start is None is truthy) {
        // Source: vvaharness/validation/tools/diff_facts.py:83-83
        In source order: Evaluate once self.new_line_number; assign in source target order to self.added_run_start.
      }
      // Source: vvaharness/validation/tools/diff_facts.py:84-85
      In source order: Apply source augmented assignment self.added_run_length += 1 with source evaluation/in-place semantics. Then Apply source augmented assignment self.new_line_number += 1 with source evaluation/in-place semantics.
    }
    else {
      // Source: vvaharness/validation/tools/diff_facts.py:86-92
      if (the source predicate prefix == REMOVED_LINE is truthy) {
        // Source: vvaharness/validation/tools/diff_facts.py:87-87
        In source order: Evaluate self._close_added_run(); retain side effects and discard the expression result.
      }
      else {
        // Source: vvaharness/validation/tools/diff_facts.py:88-92
        if (the source predicate prefix == NO_NEWLINE_NOTE is truthy) {
          // Source: vvaharness/validation/tools/diff_facts.py:89-89
          End this invocation with None.
        }
        else {
          // Source: vvaharness/validation/tools/diff_facts.py:91-92
          In source order: Evaluate self._close_added_run(); retain side effects and discard the expression result. Then Apply source augmented assignment self.new_line_number += 1 with source evaluation/in-place semantics.
        }
      }
    }
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/validation/tools/diff_facts.py:94-114
  // Source signature: feed(self, line: str) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn feed(self, line) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/validation/tools/diff_facts.py:95-114
    if (the source predicate line.startswith(GIT_HEADER_PREFIX) is truthy) {
      // Source: vvaharness/validation/tools/diff_facts.py:96-97
      In source order: Evaluate self._close_file(); retain side effects and discard the expression result. Then Evaluate once line.split(' '); assign in source target order to tokens.
      // Source: vvaharness/validation/tools/diff_facts.py:99-100
      if (the source predicate len(tokens) >= GIT_HEADER_MIN_TOKENS is truthy) {
        // Source: vvaharness/validation/tools/diff_facts.py:100-100
        In source order: Evaluate once _without_git_prefix(tokens[-1]); assign in source target order to self.current_path.
      }
    }
    else {
      // Source: vvaharness/validation/tools/diff_facts.py:101-114
      if (the source predicate line.startswith(OLD_FILE_MARKER) is truthy) {
        // Source: vvaharness/validation/tools/diff_facts.py:102-103
        In source order: Evaluate self._close_added_run(); retain side effects and discard the expression result. Then Evaluate once _without_git_prefix(_marker_path(line)); assign in source target order to self.old_path.
      }
      else {
        // Source: vvaharness/validation/tools/diff_facts.py:104-114
        if (the source predicate line.startswith(NEW_FILE_MARKER) is truthy) {
          // Source: vvaharness/validation/tools/diff_facts.py:105-109
          In source order: Evaluate self._close_added_run(); retain side effects and discard the expression result. Then Evaluate once _without_git_prefix(_marker_path(line)); assign in source target order to new_path. Then Evaluate once self.old_path if new_path == DEV_NULL_PATH else new_path; assign in source target order to self.current_path. Then Evaluate once 0; assign in source target order to self.new_line_number.
        }
        else {
          // Source: vvaharness/validation/tools/diff_facts.py:110-114
          if (the source predicate (hunk := HUNK_HEADER_RE.match(line)) is truthy) {
            // Source: vvaharness/validation/tools/diff_facts.py:111-112
            In source order: Evaluate self._close_added_run(); retain side effects and discard the expression result. Then Evaluate once int(hunk.group(HUNK_NEW_START_GROUP)); assign in source target order to self.new_line_number.
          }
          else {
            // Source: vvaharness/validation/tools/diff_facts.py:113-114
            if (the source predicate self.new_line_number is truthy) {
              // Source: vvaharness/validation/tools/diff_facts.py:114-114
              In source order: Evaluate self._consume_hunk_line(line); retain side effects and discard the expression result.
            }
          }
        }
      }
    }
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/validation/tools/diff_facts.py:116-118
  // Source signature: finish(self) -> list[FileChange]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn finish(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/validation/tools/diff_facts.py:117-117
    In source order: Evaluate self._close_file(); retain side effects and discard the expression result.
    // Source: vvaharness/validation/tools/diff_facts.py:118-118
    End this invocation with self.changes.
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vvaharness/validation/tools/diff_facts.py:121-129
// Source signature: parse_diff_patch(workspace: Path) -> list[FileChange]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn parse_diff_patch(workspace) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/tools/diff_facts.py:122-123
  In source order: Retain source documentation literal source_literal_122_4; it is not a model call. Then Evaluate once workspace / DIFF_FILENAME; assign in source target order to diff_file.
  // Source: vvaharness/validation/tools/diff_facts.py:124-125
  if (the source predicate not diff_file.exists() is truthy) {
    // Source: vvaharness/validation/tools/diff_facts.py:125-125
    End this invocation with [].
  }
  // Source: vvaharness/validation/tools/diff_facts.py:126-126
  In source order: Evaluate once _DiffParser(); assign in source target order to parser.
  // Source: vvaharness/validation/tools/diff_facts.py:127-128
  for each line in diff_file.read_text(errors='replace').splitlines() {
    // Source: vvaharness/validation/tools/diff_facts.py:128-128
    In source order: Evaluate parser.feed(line); retain side effects and discard the expression result.
  }
  // Source: vvaharness/validation/tools/diff_facts.py:129-129
  End this invocation with parser.finish().
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/tools/diff_facts.py:132-137
// Source signature: diff_touched(workspace: Path, file_path: str) -> dict
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn diff_touched(workspace, file_path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/tools/diff_facts.py:133-133
  In source order: Retain source documentation literal source_literal_133_4; it is not a model call.
  // Source: vvaharness/validation/tools/diff_facts.py:134-136
  for each change in parse_diff_patch(workspace) {
    // Source: vvaharness/validation/tools/diff_facts.py:135-136
    if (the source predicate change.path == file_path is truthy) {
      // Source: vvaharness/validation/tools/diff_facts.py:136-136
      End this invocation with {'touched': True, 'added_ranges': change.added_ranges}.
    }
  }
  // Source: vvaharness/validation/tools/diff_facts.py:137-137
  End this invocation with {'touched': False, 'added_ranges': []}.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/tools/diff_facts.py:140-142
// Source signature: changed_lines(workspace: Path, file_path: str) -> list[tuple[int, int]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn changed_lines(workspace, file_path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/tools/diff_facts.py:141-141
  In source order: Retain source documentation literal source_literal_141_4; it is not a model call.
  // Source: vvaharness/validation/tools/diff_facts.py:142-142
  End this invocation with diff_touched(workspace, file_path)['added_ranges'].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/tools/diff_facts.py:146-150
// Source: vvaharness/validation/tools/diff_facts.py:145-145
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass.
// Source: vvaharness/validation/tools/diff_facts.py:146-150
interface DiffImpactMap {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/validation/tools/diff_facts.py:147-150
  In source order: Retain source documentation literal source_literal_147_4; it is not a model call. Then For files_changed, declare without assigning a value; source annotation list[str]. Then For trust_boundary_touched, declare without assigning a value; source annotation bool.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vvaharness/validation/tools/diff_facts.py:153-159
// Source signature: build_diff_impact_map(workspace: Path) -> DiffImpactMap
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn build_diff_impact_map(workspace) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/tools/diff_facts.py:154-155
  In source order: Retain source documentation literal source_literal_154_4; it is not a model call. Then Evaluate once [change.path for change in parse_diff_patch(workspace)]; assign in source target order to files.
  // Source: vvaharness/validation/tools/diff_facts.py:156-159
  End this invocation with DiffImpactMap(files_changed=sorted(set(files)), trust_boundary_touched=any((TRUST_BOUNDARY_RE.search(path) for path in files))).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.validation.constants.artifacts import DIFF_FILENAME` at source line 22: `source_detail/vvaharness/validation/constants/artifacts.py.sudo.md`.
- `from vvaharness.validation.constants.diff import ADDED_LINE, DEV_NULL_PATH, GIT_HEADER_MIN_TOKENS, GIT_HEADER_PREFIX, GIT_PATH_PREFIXES, HUNK_HEADER_RE, HUNK_NEW_START_GROUP, MARKER_PATH_START, NEW_FILE_MARKER, NO_NEWLINE_NOTE, OLD_FILE_MARKER, REMOVED_LINE, TRUST_BOUNDARY_RE` at source line 23: `source_detail/vvaharness/validation/constants/diff.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../prompt_representation/vvaharness/validation/tools/diff_facts.py.sudo.md). Exact strings in the evidence asset support this conversion.
