# vvaharness/backends/harness/permissions.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/backends/harness/permissions.py.evidence.json`. SHA-256: `a0d9a801a1ab4ffb09cfa2786f2f90ef847ad667bdac8c396bd41ccc6c391acc`.

```sudo
// Source: vvaharness/backends/harness/permissions.py:15-29
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from dataclasses import dataclass, field; preserve alias and import-time effects. Then Resolve source import from typing import TYPE_CHECKING; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.models import MCP_TOOL_PREFIX, READ_ONLY_TOOLS, UNCONDITIONALLY_DENIED_TOOLS, PermissionDecision; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/permissions.py:30-30
In source order: Resolve source import from vvaharness.backends.harness.permission_rules import evaluate_write; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/permissions.py:32-34
if (the source predicate TYPE_CHECKING is truthy) {
  // Source: vvaharness/backends/harness/permissions.py:33-34
  In source order: Resolve source import from collections.abc import Mapping; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects.
}
// Source: vvaharness/backends/harness/permissions.py:38-71
// Source: vvaharness/backends/harness/permissions.py:37-37
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass.
// Source: vvaharness/backends/harness/permissions.py:38-71
interface PermissionsPolicy {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/harness/permissions.py:39-44
  In source order: Retain source documentation literal source_literal_39_4; it is not a model call. Then For target_dir, declare without assigning a value; source annotation Path. Then For allowed_output_files, assign field(default_factory=frozenset); source annotation frozenset[str].
  // Source: vvaharness/backends/harness/permissions.py:46-56
  // Source signature: _evaluate_simple(self, tool_name: str) -> PermissionDecision
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _evaluate_simple(self, tool_name) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/permissions.py:47-47
    In source order: Retain source documentation literal source_literal_47_8; it is not a model call.
    // Source: vvaharness/backends/harness/permissions.py:48-51
    if (the source predicate tool_name in UNCONDITIONALLY_DENIED_TOOLS is truthy) {
      // Source: vvaharness/backends/harness/permissions.py:49-51
      End this invocation with PermissionDecision(False, 'read-only validation session: Edit/NotebookEdit blocked', True).
    }
    // Source: vvaharness/backends/harness/permissions.py:52-53
    if (the source predicate tool_name in READ_ONLY_TOOLS or tool_name.startswith(MCP_TOOL_PREFIX) is truthy) {
      // Source: vvaharness/backends/harness/permissions.py:53-53
      End this invocation with PermissionDecision(True).
    }
    // Source: vvaharness/backends/harness/permissions.py:54-56
    End this invocation with PermissionDecision(False, source_template_55_19, True).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/permissions.py:58-71
  // Source signature: evaluate(self, tool_name: str, input_data: Mapping[str, object]) -> PermissionDecision
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn evaluate(self, tool_name, input_data) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/permissions.py:61-62
    In source order: Retain source documentation literal source_literal_61_8; it is not a model call. Then Evaluate once self.target_dir.resolve(); assign in source target order to resolved.
    // Source: vvaharness/backends/harness/permissions.py:63-64
    if (the source predicate tool_name == 'Write' is truthy) {
      // Source: vvaharness/backends/harness/permissions.py:64-64
      End this invocation with evaluate_write(input_data, resolved, self.allowed_output_files).
    }
    // Source: vvaharness/backends/harness/permissions.py:65-70
    if (the source predicate tool_name == 'Bash' is truthy) {
      // Source: vvaharness/backends/harness/permissions.py:66-70
      End this invocation with PermissionDecision(False, 'Bash is disabled in validation sessions — no shell execution permitted', True).
    }
    // Source: vvaharness/backends/harness/permissions.py:71-71
    End this invocation with self._evaluate_simple(tool_name).
    If execution reaches this end, finish with the source implicit None result.
  }
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vvaharness/backends/harness/permissions.py:74-74
In source order: Evaluate once ['PermissionsPolicy']; assign in source target order to __all__.
```

## Local import links

- `from vvaharness.backends.harness.models import MCP_TOOL_PREFIX, READ_ONLY_TOOLS, UNCONDITIONALLY_DENIED_TOOLS, PermissionDecision` at source line 24: `source_detail/vvaharness/backends/harness/models.py.sudo.md`.
- `from vvaharness.backends.harness.permission_rules import evaluate_write` at source line 30: `source_detail/vvaharness/backends/harness/permission_rules.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../prompt_representation/vvaharness/backends/harness/permissions.py.sudo.md). Exact strings in the evidence asset support this conversion.
