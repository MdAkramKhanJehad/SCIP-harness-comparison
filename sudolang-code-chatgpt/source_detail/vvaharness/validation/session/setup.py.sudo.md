# vvaharness/validation/session/setup.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/validation/session/setup.py.evidence.json`. SHA-256: `b74d95dad63d356e2775a8b500ff99af74c7090ff09021c2d62dfbd0098d375e`.

```sudo
// Source: vvaharness/validation/session/setup.py:15-25
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness import PermissionsPolicy; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.constants.policy import DEFAULT_ALLOWED_OUTPUT_FILES, VALIDATION_POLICY; preserve alias and import-time effects.
// Source: vvaharness/validation/session/setup.py:26-31
In source order: Resolve source import from vvaharness.validation.constants.tools import DEFAULT_FACT_TOOLS; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.models.output import ValidationOutput; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.tools.deep_tools import build_validation_tools; preserve alias and import-time effects. Then Evaluate once 'validation'; assign in source target order to VALIDATION_GRAPH_NAME.
// Source: vvaharness/validation/session/setup.py:34-39
// Source signature: validation_skill_root(workspace: Path) -> Path
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn validation_skill_root(workspace) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/session/setup.py:35-37
  In source order: Retain source documentation literal source_literal_35_4; it is not a model call. Then Resolve source import from vvaharness.validation.constants.artifacts import CLAUDE_DIRNAME; preserve alias and import-time effects.
  // Source: vvaharness/validation/session/setup.py:39-39
  End this invocation with workspace / CLAUDE_DIRNAME / 'skills'.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/session/setup.py:42-47
// Source signature: validation_write_gate(workspace: Path) -> PermissionsPolicy
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn validation_write_gate(workspace) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/session/setup.py:43-43
  In source order: Retain source documentation literal source_literal_43_4; it is not a model call.
  // Source: vvaharness/validation/session/setup.py:44-47
  End this invocation with PermissionsPolicy(target_dir=workspace, allowed_output_files=DEFAULT_ALLOWED_OUTPUT_FILES).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/session/setup.py:50-58
In source order: Evaluate once ['DEFAULT_FACT_TOOLS', 'VALIDATION_GRAPH_NAME', 'VALIDATION_POLICY', 'ValidationOutput', 'build_validation_tools', 'validation_skill_root', 'validation_write_gate']; assign in source target order to __all__.
```

## Local import links

- `from vvaharness.backends.harness import PermissionsPolicy` at source line 21: `source_detail/vvaharness/backends/harness/__init__.py.sudo.md`.
- `from vvaharness.validation.constants.policy import DEFAULT_ALLOWED_OUTPUT_FILES, VALIDATION_POLICY` at source line 22: `source_detail/vvaharness/validation/constants/policy.py.sudo.md`.
- `from vvaharness.validation.constants.tools import DEFAULT_FACT_TOOLS` at source line 26: `source_detail/vvaharness/validation/constants/tools.py.sudo.md`.
- `from vvaharness.validation.models.output import ValidationOutput` at source line 27: `source_detail/vvaharness/validation/models/output.py.sudo.md`.
- `from vvaharness.validation.tools.deep_tools import build_validation_tools` at source line 28: `source_detail/vvaharness/validation/tools/deep_tools.py.sudo.md`.
- `from vvaharness.validation.constants.artifacts import CLAUDE_DIRNAME` at source line 37: `source_detail/vvaharness/validation/constants/artifacts.py.sudo.md`.
