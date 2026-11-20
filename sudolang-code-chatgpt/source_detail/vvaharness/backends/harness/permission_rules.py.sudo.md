# vvaharness/backends/harness/permission_rules.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/backends/harness/permission_rules.py.evidence.json`. SHA-256: `14a60a0ee62e819ad5c9443b08550afc8b0cb24b40a88397eec6b45eeab14134`.

```sudo
// Source: vvaharness/backends/harness/permission_rules.py:15-23
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import os; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from typing import TYPE_CHECKING; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/permission_rules.py:25-26
In source order: Resolve source import from vvaharness.backends.harness.models import PermissionDecision; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import console; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/permission_rules.py:28-29
if (the source predicate TYPE_CHECKING is truthy) {
  // Source: vvaharness/backends/harness/permission_rules.py:29-29
  In source order: Resolve source import from collections.abc import Mapping; preserve alias and import-time effects.
}
// Source: vvaharness/backends/harness/permission_rules.py:32-45
// Source signature: _resolve_write_path(input_data: Mapping[str, object], resolved_target: Path) -> Path | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _resolve_write_path(input_data, resolved_target) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/permission_rules.py:35-36
  In source order: Retain source documentation literal source_literal_35_4; it is not a model call. Then Evaluate once input_data.get('file_path', ''); assign in source target order to raw_path.
  // Source: vvaharness/backends/harness/permission_rules.py:37-38
  if (the source predicate not isinstance(raw_path, str) or not raw_path is truthy) {
    // Source: vvaharness/backends/harness/permission_rules.py:38-38
    End this invocation with None.
  }
  // Source: vvaharness/backends/harness/permission_rules.py:39-39
  In source order: Evaluate once Path(raw_path); assign in source target order to candidate.
  // Source: vvaharness/backends/harness/permission_rules.py:40-41
  if (the source predicate not candidate.is_absolute() is truthy) {
    // Source: vvaharness/backends/harness/permission_rules.py:41-41
    In source order: Evaluate once resolved_target / candidate; assign in source target order to candidate.
  }
  // Source: vvaharness/backends/harness/permission_rules.py:42-45
  Perform the following protected operations {
    // Source: vvaharness/backends/harness/permission_rules.py:43-43
    End this invocation with candidate.resolve().
  }
  // Source: vvaharness/backends/harness/permission_rules.py:44-45
  On the first matching source exception (ValueError, OSError), in handler order {
    // Source: vvaharness/backends/harness/permission_rules.py:45-45
    End this invocation with None.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/permission_rules.py:48-50
// Source signature: _under_target(resolved: Path, resolved_target: Path) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _under_target(resolved, resolved_target) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/permission_rules.py:49-49
  In source order: Retain source documentation literal source_literal_49_4; it is not a model call.
  // Source: vvaharness/backends/harness/permission_rules.py:50-50
  End this invocation with os.path.normcase(str(resolved.parent)) == os.path.normcase(str(resolved_target)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/permission_rules.py:53-69
// Source signature: evaluate_write(input_data: Mapping[str, object], resolved_target: Path, allowed_output_files: frozenset[str]) -> PermissionDecision
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn evaluate_write(input_data, resolved_target, allowed_output_files) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/permission_rules.py:58-59
  In source order: Retain source documentation literal source_literal_58_4; it is not a model call. Then Evaluate once _resolve_write_path(input_data, resolved_target); assign in source target order to resolved.
  // Source: vvaharness/backends/harness/permission_rules.py:60-64
  if (the source predicate os.environ.get('VVAHARNESS_DEBUG') is truthy) {
    // Source: vvaharness/backends/harness/permission_rules.py:61-64
    In source order: Evaluate console.write(source_template_62_12); retain side effects and discard the expression result.
  }
  // Source: vvaharness/backends/harness/permission_rules.py:65-66
  if (the source predicate resolved is None is truthy) {
    // Source: vvaharness/backends/harness/permission_rules.py:66-66
    End this invocation with PermissionDecision(False, 'Write path missing or unresolvable', True).
  }
  // Source: vvaharness/backends/harness/permission_rules.py:67-68
  if (the source predicate not _under_target(resolved, resolved_target) or resolved.name not in allowed_output_files is truthy) {
    // Source: vvaharness/backends/harness/permission_rules.py:68-68
    End this invocation with PermissionDecision(False, source_template_68_41, True).
  }
  // Source: vvaharness/backends/harness/permission_rules.py:69-69
  End this invocation with PermissionDecision(True).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/permission_rules.py:72-72
In source order: Evaluate once ['evaluate_write']; assign in source target order to __all__.
```

## Local import links

- `from vvaharness.backends.harness.models import PermissionDecision` at source line 25: `source_detail/vvaharness/backends/harness/models.py.sudo.md`.
- `from vvaharness.util import console` at source line 26: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import console` at source line 26: `source_detail/vvaharness/util/console.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../prompt_representation/vvaharness/backends/harness/permission_rules.py.sudo.md). Exact strings in the evidence asset support this conversion.
