# vvaharness/validation/tools/fact_specs.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/validation/tools/fact_specs.py.evidence.json`. SHA-256: `53ca8a1b848d2666d92b82a790076009bea00ab038e3037e916a1be65f77d17e`.

```sudo
// Source: vvaharness/validation/tools/fact_specs.py:15-28
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from typing import TYPE_CHECKING; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.models import FactToolSpec; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.tools.diff_facts import build_diff_impact_map, changed_lines, diff_touched; preserve alias and import-time effects.
// Source: vvaharness/validation/tools/fact_specs.py:29-30
In source order: Resolve source import from vvaharness.validation.tools.pattern_scanner import pattern_scan; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.tools.test_inventory import test_inventory; preserve alias and import-time effects.
// Source: vvaharness/validation/tools/fact_specs.py:32-33
if (the source predicate TYPE_CHECKING is truthy) {
  // Source: vvaharness/validation/tools/fact_specs.py:33-33
  In source order: Resolve source import from pathlib import Path; preserve alias and import-time effects.
}
// Source: vvaharness/validation/tools/fact_specs.py:35-49
In source order: Evaluate once {'type': 'object', 'properties': {'file_path': {'type': 'string', 'description': 'Repo-relative path.'}}, 'required': ['file_path']}; assign in source target order to _FILE_PATH_SCHEMA. Then For _NO_ARGS_SCHEMA, assign {'type': 'object', 'properties': {}, 'required': []}; source annotation dict. Then Evaluate once {'type': 'object', 'properties': {'pattern_set': {'type': 'string', 'description': 'Builtin set: "secret_exposure" or "insecure_value".'}}, 'required': ['pattern_set']}; assign in source target order to _PATTERN_SET_SCHEMA.
// Source: vvaharness/validation/tools/fact_specs.py:52-91
// Source signature: build_validation_fact_specs(workspace: Path) -> tuple[FactToolSpec, ...]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn build_validation_fact_specs(workspace) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/tools/fact_specs.py:53-53
  In source order: Retain source documentation literal source_literal_53_4; it is not a model call.
  // Source: vvaharness/validation/tools/fact_specs.py:54-91
  End this invocation with (FactToolSpec(name='DiffTouched', description='Return whether *file_path* is in diff.patch and its changed line ranges.', input_schema=_FILE_PATH_SCHEMA, fn=lambda file_path: diff_touched(workspace, file_path)), FactToolSpec(name='ChangedLines', description='Return added line ranges for *file_path* from diff.patch.', input_schema=_FILE_PATH_SCHEMA, fn=lambda file_path: changed_lines(workspace, file_path)), FactToolSpec(name='DiffImpactMap', description='Return files changed by diff.patch and whether a trust boundary was touched.', input_schema=_NO_ARGS_SCHEMA, fn=lambda: _impact(workspace)), FactToolSpec(name='PatternScan', description=source_literal_77_25, input_schema=_PATTERN_SET_SCHEMA, fn=lambda pattern_set: pattern_scan(workspace, pattern_set)), FactToolSpec(name='TestInventory', description='Inventory test files and detect negative/adversarial test markers.', input_schema=_NO_ARGS_SCHEMA, fn=lambda: test_inventory(workspace))).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/tools/fact_specs.py:94-100
// Source signature: _impact(workspace: Path) -> dict
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _impact(workspace) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/tools/fact_specs.py:95-96
  In source order: Retain source documentation literal source_literal_95_4; it is not a model call. Then Evaluate once build_diff_impact_map(workspace); assign in source target order to impact.
  // Source: vvaharness/validation/tools/fact_specs.py:97-100
  End this invocation with {'files_changed': impact.files_changed, 'trust_boundary_touched': impact.trust_boundary_touched}.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/tools/fact_specs.py:103-103
In source order: Evaluate once ['build_validation_fact_specs']; assign in source target order to __all__.
```

## Local import links

- `from vvaharness.backends.harness.models import FactToolSpec` at source line 23: `source_detail/vvaharness/backends/harness/models.py.sudo.md`.
- `from vvaharness.validation.tools.diff_facts import build_diff_impact_map, changed_lines, diff_touched` at source line 24: `source_detail/vvaharness/validation/tools/diff_facts.py.sudo.md`.
- `from vvaharness.validation.tools.pattern_scanner import pattern_scan` at source line 29: `source_detail/vvaharness/validation/tools/pattern_scanner.py.sudo.md`.
- `from vvaharness.validation.tools.test_inventory import test_inventory` at source line 30: `source_detail/vvaharness/validation/tools/test_inventory.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../prompt_representation/vvaharness/validation/tools/fact_specs.py.sudo.md). Exact strings in the evidence asset support this conversion.
