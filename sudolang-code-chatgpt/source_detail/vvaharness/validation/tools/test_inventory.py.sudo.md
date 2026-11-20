# vvaharness/validation/tools/test_inventory.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/validation/tools/test_inventory.py.evidence.json`. SHA-256: `d79aec19d8edd7a70f7c2fcd85fe6bc37128cc8eab41a4018c8a8de6f6a9e84e`.

```sudo
// Source: vvaharness/validation/tools/test_inventory.py:15-28
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import re; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.constants.test_inventory import JS_TEST_SUFFIXES, NEGATIVE_TEST_MARKERS, PY_TEST_EXACT_NAMES, PY_TEST_NAME_PREFIX, PY_TEST_NAME_SUFFIX; preserve alias and import-time effects.
// Source: vvaharness/validation/tools/test_inventory.py:29-34
In source order: Resolve source import from vvaharness.validation.tools._scope import iter_in_scope_files; preserve alias and import-time effects. Then Evaluate once tuple(((marker, re.compile(source_template_32_24, re.IGNORECASE)) for marker in NEGATIVE_TEST_MARKERS)); assign in source target order to _MARKER_PATTERNS.
// Source: vvaharness/validation/tools/test_inventory.py:37-44
// Source signature: _is_test_file(name: str) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _is_test_file(name) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/tools/test_inventory.py:38-39
  if (the source predicate name in PY_TEST_EXACT_NAMES is truthy) {
    // Source: vvaharness/validation/tools/test_inventory.py:39-39
    End this invocation with True.
  }
  // Source: vvaharness/validation/tools/test_inventory.py:40-43
  if (the source predicate name.endswith('.py') and (name.startswith(PY_TEST_NAME_PREFIX) or name.endswith(PY_TEST_NAME_SUFFIX)) is truthy) {
    // Source: vvaharness/validation/tools/test_inventory.py:43-43
    End this invocation with True.
  }
  // Source: vvaharness/validation/tools/test_inventory.py:44-44
  End this invocation with any((name.endswith(suffix) for suffix in JS_TEST_SUFFIXES)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/tools/test_inventory.py:47-48
// Source signature: _negative_markers(text: str) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _negative_markers(text) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/tools/test_inventory.py:48-48
  End this invocation with sorted({marker for marker, pattern in _MARKER_PATTERNS if pattern.search(text)}).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/tools/test_inventory.py:51-75
// Source signature: test_inventory(workspace: Path) -> dict
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn test_inventory(workspace) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/tools/test_inventory.py:52-53
  In source order: Retain source documentation literal source_literal_52_4; it is not a model call. Then For test_files, assign []; source annotation list[dict].
  // Source: vvaharness/validation/tools/test_inventory.py:54-69
  for each file_path in iter_in_scope_files(workspace, include_tests=True) {
    // Source: vvaharness/validation/tools/test_inventory.py:55-56
    if (the source predicate not _is_test_file(file_path.name) is truthy) {
      // Source: vvaharness/validation/tools/test_inventory.py:56-56
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/validation/tools/test_inventory.py:57-60
    Perform the following protected operations {
      // Source: vvaharness/validation/tools/test_inventory.py:58-58
      In source order: Evaluate once file_path.read_text(errors='replace'); assign in source target order to text.
    }
    // Source: vvaharness/validation/tools/test_inventory.py:59-60
    On the first matching source exception OSError, in handler order {
      // Source: vvaharness/validation/tools/test_inventory.py:60-60
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/validation/tools/test_inventory.py:61-69
    In source order: Evaluate once _negative_markers(text); assign in source target order to markers. Then Evaluate test_files.append({'file': str(file_path.relative_to(workspace)), 'lines': len(text.splitlines()), 'negative_test_markers': markers, 'has_negative_tests': bool(markers)}); retain side effects and discard the expression result.
  }
  // Source: vvaharness/validation/tools/test_inventory.py:70-70
  In source order: Evaluate test_files.sort(key=lambda item: item['file']); retain side effects and discard the expression result.
  // Source: vvaharness/validation/tools/test_inventory.py:71-75
  End this invocation with {'test_files': test_files, 'total_test_files': len(test_files), 'files_with_negative_tests': sum((1 for item in test_files if item['has_negative_tests']))}.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.validation.constants.test_inventory import JS_TEST_SUFFIXES, NEGATIVE_TEST_MARKERS, PY_TEST_EXACT_NAMES, PY_TEST_NAME_PREFIX, PY_TEST_NAME_SUFFIX` at source line 22: `source_detail/vvaharness/validation/constants/test_inventory.py.sudo.md`.
- `from vvaharness.validation.tools._scope import iter_in_scope_files` at source line 29: `source_detail/vvaharness/validation/tools/_scope.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../prompt_representation/vvaharness/validation/tools/test_inventory.py.sudo.md). Exact strings in the evidence asset support this conversion.
