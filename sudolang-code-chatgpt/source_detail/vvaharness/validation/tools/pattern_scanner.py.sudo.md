# vvaharness/validation/tools/pattern_scanner.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/validation/tools/pattern_scanner.py.evidence.json`. SHA-256: `a124b8e4b95a5c04e583c49c10cf23d7543610a1a106b250abb2d367c72456ca`.

```sudo
// Source: vvaharness/validation/tools/pattern_scanner.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import os; preserve alias and import-time effects. Then Resolve source import import re; preserve alias and import-time effects. Then Resolve source import from dataclasses import dataclass, field; preserve alias and import-time effects.
// Source: vvaharness/validation/tools/pattern_scanner.py:22-33
In source order: Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.constants.pattern_sets import BUILTIN_RULE, DEFAULT_PATTERN_SETS, NUL_BYTE, SKIP_IN_SCAN; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.tools._scope import iter_in_scope_files; preserve alias and import-time effects. Then Evaluate once 512 * 1024; assign in source target order to _MAX_FILE_BYTES. Then Evaluate once 32 * 1024 * 1024; assign in source target order to _MAX_TOTAL_BYTES.
// Source: vvaharness/validation/tools/pattern_scanner.py:34-36
In source order: Evaluate once 10000; assign in source target order to _MAX_FILES. Then Evaluate once 50; assign in source target order to _MAX_MATCHES_PER_FILE. Then Evaluate once 200; assign in source target order to _MAX_MATCHES.
// Source: vvaharness/validation/tools/pattern_scanner.py:39-44
// Source: vvaharness/validation/tools/pattern_scanner.py:38-38
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vvaharness/validation/tools/pattern_scanner.py:39-44
interface _ReadResult {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/validation/tools/pattern_scanner.py:40-44
  In source order: For data, assign b''; source annotation bytes. Then For unreadable, assign False; source annotation bool. Then For too_large, assign False; source annotation bool. Then For binary, assign False; source annotation bool. Then For has_more, assign False; source annotation bool.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vvaharness/validation/tools/pattern_scanner.py:48-51
// Source: vvaharness/validation/tools/pattern_scanner.py:47-47
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vvaharness/validation/tools/pattern_scanner.py:48-51
interface _ScanPattern {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/validation/tools/pattern_scanner.py:49-51
  In source order: For name, declare without assigning a value; source annotation str. Then For description, declare without assigning a value; source annotation str. Then For regex, declare without assigning a value; source annotation re.Pattern[str].
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vvaharness/validation/tools/pattern_scanner.py:55-67
// Source: vvaharness/validation/tools/pattern_scanner.py:54-54
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass.
// Source: vvaharness/validation/tools/pattern_scanner.py:55-67
interface _ScanState {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/validation/tools/pattern_scanner.py:56-60
  In source order: For matches, assign field(default_factory=list); source annotation list[dict]. Then For matches_seen, assign 0; source annotation int. Then For files_considered, assign 0; source annotation int. Then For files_scanned, assign 0; source annotation int. Then For files_too_large, assign 0; source annotation int.
  // Source: vvaharness/validation/tools/pattern_scanner.py:61-65
  In source order: For files_unreadable, assign 0; source annotation int. Then For binary_files, assign 0; source annotation int. Then For bytes_scanned, assign 0; source annotation int. Then For file_count_truncated, assign False; source annotation bool. Then For byte_limit_truncated, assign False; source annotation bool.
  // Source: vvaharness/validation/tools/pattern_scanner.py:66-67
  In source order: For per_file_truncated, assign False; source annotation bool. Then For overall_truncated, assign False; source annotation bool.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vvaharness/validation/tools/pattern_scanner.py:70-83
// Source signature: _read_bounded(path: Path, max_bytes: int) -> _ReadResult
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _read_bounded(path, max_bytes) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/tools/pattern_scanner.py:71-76
  Perform the following protected operations {
    // Source: vvaharness/validation/tools/pattern_scanner.py:72-74
    Enter source context managers left-to-right: path.open('rb') bound to handle {
      // Source: vvaharness/validation/tools/pattern_scanner.py:73-74
      In source order: Evaluate once os.fstat(handle.fileno()).st_size; assign in source target order to size. Then Evaluate once handle.read(max_bytes); assign in source target order to raw_bytes.
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
  }
  // Source: vvaharness/validation/tools/pattern_scanner.py:75-76
  On the first matching source exception OSError, in handler order {
    // Source: vvaharness/validation/tools/pattern_scanner.py:76-76
    End this invocation with _ReadResult(unreadable=True).
  }
  // Source: vvaharness/validation/tools/pattern_scanner.py:77-77
  In source order: Evaluate once max(size, len(raw_bytes)); assign in source target order to observed_size.
  // Source: vvaharness/validation/tools/pattern_scanner.py:78-83
  End this invocation with _ReadResult(data=raw_bytes, too_large=observed_size > _MAX_FILE_BYTES, binary=NUL_BYTE in raw_bytes, has_more=observed_size > max_bytes).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/tools/pattern_scanner.py:86-110
// Source signature: _scan_text(state: _ScanState, *, text: str, relative_path: str, pattern: _ScanPattern) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _scan_text(state, text, relative_path, pattern) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/tools/pattern_scanner.py:93-93
  In source order: Evaluate once 0; assign in source target order to file_matches.
  // Source: vvaharness/validation/tools/pattern_scanner.py:94-110
  for each match in pattern.regex.finditer(text) {
    // Source: vvaharness/validation/tools/pattern_scanner.py:95-96
    In source order: Apply source augmented assignment state.matches_seen += 1 with source evaluation/in-place semantics. Then Apply source augmented assignment file_matches += 1 with source evaluation/in-place semantics.
    // Source: vvaharness/validation/tools/pattern_scanner.py:97-99
    if (the source predicate file_matches > _MAX_MATCHES_PER_FILE is truthy) {
      // Source: vvaharness/validation/tools/pattern_scanner.py:98-98
      In source order: Evaluate once True; assign in source target order to state.per_file_truncated.
      // Source: vvaharness/validation/tools/pattern_scanner.py:99-99
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/validation/tools/pattern_scanner.py:100-102
    if (the source predicate len(state.matches) >= _MAX_MATCHES is truthy) {
      // Source: vvaharness/validation/tools/pattern_scanner.py:101-101
      In source order: Evaluate once True; assign in source target order to state.overall_truncated.
      // Source: vvaharness/validation/tools/pattern_scanner.py:102-102
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/validation/tools/pattern_scanner.py:103-110
    In source order: Evaluate state.matches.append({'kind': 'match', 'file': relative_path, 'line': text.count(source_literal_106_31, 0, match.start()) + 1, 'pattern_set': pattern.name, 'rule': BUILTIN_RULE, 'description': pattern.description}); retain side effects and discard the expression result.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/tools/pattern_scanner.py:113-149
// Source signature: _result(state: _ScanState, pattern_set: str) -> list[dict]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _result(state, pattern_set) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/tools/pattern_scanner.py:114-148
  In source order: Evaluate state.matches.sort(key=lambda match: (match['file'], match['line'])); retain side effects and discard the expression result. Then Evaluate once [reason for limited, reason in ((state.files_too_large, 'file_size_limit'), (state.files_unreadable, 'unreadable_files'), (state.binary_files, 'binary_files'), (state.file_count_truncated, 'overall_file_limit'), (state.byte_limit_truncated, 'overall_byte_limit'), (state.per_file_truncated, 'per_file_match_limit'), (state.overall_truncated, 'overall_match_limit')) if limited]; assign in source target order to reasons. Then Evaluate state.matches.append({'kind': 'summary', 'pattern_set': pattern_set, 'matches_seen': state.matches_seen, 'matches_returned': len(state.matches), 'files_considered': state.files_considered, 'files_scanned': state.files_scanned, 'files_too_large': state.files_too_large, 'files_unreadable': state.files_unreadable, 'binary_files': state.binary_files, 'bytes_scanned': state.bytes_scanned, 'truncated': bool(reasons), 'truncation_reasons': reasons, 'limits': {'max_file_bytes': _MAX_FILE_BYTES, 'max_total_bytes': _MAX_TOTAL_BYTES, 'max_files': _MAX_FILES, 'max_matches_per_file': _MAX_MATCHES_PER_FILE, 'max_matches': _MAX_MATCHES}}); retain side effects and discard the expression result.
  // Source: vvaharness/validation/tools/pattern_scanner.py:149-149
  End this invocation with state.matches.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/tools/pattern_scanner.py:152-173
// Source signature: _consume_file(state: _ScanState, file_path: Path, workspace: Path, pattern: _ScanPattern) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _consume_file(state, file_path, workspace, pattern) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/tools/pattern_scanner.py:155-159
  In source order: Apply source augmented assignment state.files_considered += 1 with source evaluation/in-place semantics. Then Evaluate once _MAX_TOTAL_BYTES - state.bytes_scanned; assign in source target order to remaining_bytes. Then Evaluate once min(_MAX_FILE_BYTES, remaining_bytes); assign in source target order to read_limit. Then Evaluate once _read_bounded(file_path, read_limit); assign in source target order to result. Then Apply source augmented assignment state.bytes_scanned += len(result.data) with source evaluation/in-place semantics.
  // Source: vvaharness/validation/tools/pattern_scanner.py:160-164
  In source order: Apply source augmented assignment state.files_unreadable += int(result.unreadable) with source evaluation/in-place semantics. Then Apply source augmented assignment state.files_too_large += int(result.too_large) with source evaluation/in-place semantics. Then Apply source augmented assignment state.binary_files += int(result.binary) with source evaluation/in-place semantics. Then Evaluate once read_limit == remaining_bytes and result.has_more; assign in source target order to budget_exhausted. Then Apply source augmented assignment state.byte_limit_truncated |= budget_exhausted with source evaluation/in-place semantics.
  // Source: vvaharness/validation/tools/pattern_scanner.py:165-173
  if (the source predicate not (result.unreadable or result.too_large or result.binary or budget_exhausted) is truthy) {
    // Source: vvaharness/validation/tools/pattern_scanner.py:167-173
    In source order: Apply source augmented assignment state.files_scanned += 1 with source evaluation/in-place semantics. Then Evaluate _scan_text(state, text=result.data.decode('utf-8', errors='replace'), relative_path=str(file_path.relative_to(workspace)), pattern=pattern); retain side effects and discard the expression result.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/tools/pattern_scanner.py:176-187
// Source signature: _scan_workspace(state: _ScanState, workspace: Path, pattern: _ScanPattern) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _scan_workspace(state, workspace, pattern) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/tools/pattern_scanner.py:179-187
  for each file_path in iter_in_scope_files(workspace, include_tests=False) {
    // Source: vvaharness/validation/tools/pattern_scanner.py:180-181
    if (the source predicate file_path.name in SKIP_IN_SCAN is truthy) {
      // Source: vvaharness/validation/tools/pattern_scanner.py:181-181
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/validation/tools/pattern_scanner.py:182-184
    if (the source predicate state.files_considered >= _MAX_FILES is truthy) {
      // Source: vvaharness/validation/tools/pattern_scanner.py:183-183
      In source order: Evaluate once True; assign in source target order to state.file_count_truncated.
      // Source: vvaharness/validation/tools/pattern_scanner.py:184-184
      Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
    }
    // Source: vvaharness/validation/tools/pattern_scanner.py:185-185
    In source order: Evaluate _consume_file(state, file_path, workspace, pattern); retain side effects and discard the expression result.
    // Source: vvaharness/validation/tools/pattern_scanner.py:186-187
    if (the source predicate state.byte_limit_truncated is truthy) {
      // Source: vvaharness/validation/tools/pattern_scanner.py:187-187
      Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
    }
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/tools/pattern_scanner.py:190-203
// Source signature: pattern_scan(workspace: Path, pattern_set: str) -> list[dict]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn pattern_scan(workspace, pattern_set) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/tools/pattern_scanner.py:191-191
  In source order: Retain source documentation literal source_literal_191_4; it is not a model call.
  // Source: vvaharness/validation/tools/pattern_scanner.py:192-197
  if (the source predicate pattern_set not in DEFAULT_PATTERN_SETS is truthy) {
    // Source: vvaharness/validation/tools/pattern_scanner.py:193-197
    End this invocation with [{'kind': 'error', 'error': source_template_195_22}].
  }
  // Source: vvaharness/validation/tools/pattern_scanner.py:199-202
  In source order: Evaluate once DEFAULT_PATTERN_SETS[pattern_set]; assign in source target order to (description, regex). Then Evaluate once _ScanPattern(pattern_set, description, regex); assign in source target order to pattern. Then Evaluate once _ScanState(); assign in source target order to state. Then Evaluate _scan_workspace(state, workspace, pattern); retain side effects and discard the expression result.
  // Source: vvaharness/validation/tools/pattern_scanner.py:203-203
  End this invocation with _result(state, pattern_set).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.validation.constants.pattern_sets import BUILTIN_RULE, DEFAULT_PATTERN_SETS, NUL_BYTE, SKIP_IN_SCAN` at source line 24: `source_detail/vvaharness/validation/constants/pattern_sets.py.sudo.md`.
- `from vvaharness.validation.tools._scope import iter_in_scope_files` at source line 30: `source_detail/vvaharness/validation/tools/_scope.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../prompt_representation/vvaharness/validation/tools/pattern_scanner.py.sudo.md). Exact strings in the evidence asset support this conversion.
