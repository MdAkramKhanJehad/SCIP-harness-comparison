# vvaharness/validation/session/launch_prompt.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/validation/session/launch_prompt.py.evidence.json`. SHA-256: `149c920ab40eac26185d0aebd23cf0c2c1dd2ed6964dd3d004a001a60062be52`.

```sudo
// Source: vvaharness/validation/session/launch_prompt.py:15-22
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from typing import TYPE_CHECKING; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.constants.artifacts import DIFF_FILENAME, MISSING_FIELD_PLACEHOLDER; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.hints import hints_for; preserve alias and import-time effects.
// Source: vvaharness/validation/session/launch_prompt.py:23-23
In source order: Resolve source import from vvaharness.validation.models import Manifest; preserve alias and import-time effects.
// Source: vvaharness/validation/session/launch_prompt.py:25-26
if (the source predicate TYPE_CHECKING is truthy) {
  // Source: vvaharness/validation/session/launch_prompt.py:26-26
  In source order: Resolve source import from vvaharness.models import Finding; preserve alias and import-time effects.
}
// Source: vvaharness/validation/session/launch_prompt.py:28-37
In source order: Evaluate once ['build_launch_prompt']; assign in source target order to __all__. Then For _NARRATIVE_FIELDS, assign (('Description Detail', 'description'), ('Impact', 'impact'), ('Exploit Scenario', 'exploit_scenario'), ('Preconditions', 'preconditions'), ('Recommendation', 'recommendation')); source annotation tuple[tuple[str, str], ...].
// Source: vvaharness/validation/session/launch_prompt.py:40-45
// Source signature: _score_line(label: str, score: object, vector: object) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _score_line(label, score, vector) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/session/launch_prompt.py:41-42
  In source order: Retain source documentation literal source_literal_41_4; it is not a model call. Then Evaluate once source_template_42_11; assign in source target order to line.
  // Source: vvaharness/validation/session/launch_prompt.py:43-44
  if (the source predicate vector is truthy) {
    // Source: vvaharness/validation/session/launch_prompt.py:44-44
    In source order: Apply source augmented assignment line += source_template_44_16 with source evaluation/in-place semantics.
  }
  // Source: vvaharness/validation/session/launch_prompt.py:45-45
  End this invocation with line.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/session/launch_prompt.py:48-52
// Source signature: _render(value: object) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _render(value) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/session/launch_prompt.py:49-49
  In source order: Retain source documentation literal source_literal_49_4; it is not a model call.
  // Source: vvaharness/validation/session/launch_prompt.py:50-51
  if (the source predicate isinstance(value, (list, tuple)) is truthy) {
    // Source: vvaharness/validation/session/launch_prompt.py:51-51
    End this invocation with '; '.join((str(item) for item in value)).
  }
  // Source: vvaharness/validation/session/launch_prompt.py:52-52
  End this invocation with str(value).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/session/launch_prompt.py:55-61
// Source signature: _narrative_lines(finding: Finding) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _narrative_lines(finding) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/session/launch_prompt.py:56-56
  In source order: Retain source documentation literal source_literal_56_4; it is not a model call.
  // Source: vvaharness/validation/session/launch_prompt.py:57-61
  End this invocation with [source_template_58_8 for label, attr in _NARRATIVE_FIELDS if (value := getattr(finding, attr, ''))].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/session/launch_prompt.py:64-66
// Source signature: _category(finding: Finding) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _category(finding) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/session/launch_prompt.py:65-65
  In source order: Retain source documentation literal source_literal_65_4; it is not a model call.
  // Source: vvaharness/validation/session/launch_prompt.py:66-66
  End this invocation with finding.cwe or finding.vuln_class.value.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/session/launch_prompt.py:69-78
// Source signature: _bypass_hint_lines(finding: Finding) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _bypass_hint_lines(finding) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/session/launch_prompt.py:70-72
  In source order: Retain source documentation literal source_literal_70_4; it is not a model call. Then Evaluate once _category(finding); assign in source target order to category. Then Evaluate once hints_for(category); assign in source target order to hints.
  // Source: vvaharness/validation/session/launch_prompt.py:73-74
  if (the source predicate not hints is truthy) {
    // Source: vvaharness/validation/session/launch_prompt.py:74-74
    End this invocation with [].
  }
  // Source: vvaharness/validation/session/launch_prompt.py:75-78
  End this invocation with [source_template_76_8, *[source_template_77_10 for hint in hints]].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/session/launch_prompt.py:81-96
// Source signature: _append_finding_details(lines: list[str], finding: Finding, affected: list[str]) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _append_finding_details(lines, finding, affected) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/session/launch_prompt.py:82-88
  In source order: Retain source documentation literal source_literal_82_4; it is not a model call. Then Apply source augmented assignment lines += ['', '## Finding Details', ''] with source evaluation/in-place semantics. Then Evaluate lines.append(source_template_84_17); retain side effects and discard the expression result. Then Evaluate lines.append(source_template_85_17); retain side effects and discard the expression result. Then Evaluate lines.append(source_template_87_8); retain side effects and discard the expression result.
  // Source: vvaharness/validation/session/launch_prompt.py:89-90
  if (the source predicate finding.cvss_score is not None is truthy) {
    // Source: vvaharness/validation/session/launch_prompt.py:90-90
    In source order: Evaluate lines.append(_score_line('CVSS', finding.cvss_score, finding.cvss_vector)); retain side effects and discard the expression result.
  }
  // Source: vvaharness/validation/session/launch_prompt.py:91-92
  if (the source predicate finding.file is truthy) {
    // Source: vvaharness/validation/session/launch_prompt.py:92-92
    In source order: Evaluate lines.append(source_template_92_21); retain side effects and discard the expression result.
  }
  // Source: vvaharness/validation/session/launch_prompt.py:93-94
  if (the source predicate affected is truthy) {
    // Source: vvaharness/validation/session/launch_prompt.py:94-94
    In source order: Evaluate lines.append(source_template_94_21); retain side effects and discard the expression result.
  }
  // Source: vvaharness/validation/session/launch_prompt.py:95-96
  In source order: Apply source augmented assignment lines += _narrative_lines(finding) with source evaluation/in-place semantics. Then Apply source augmented assignment lines += _bypass_hint_lines(finding) with source evaluation/in-place semantics.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/session/launch_prompt.py:99-127
// Source signature: build_launch_prompt(manifest: Manifest) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn build_launch_prompt(manifest) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/session/launch_prompt.py:100-114
  In source order: Retain source documentation literal source_literal_100_4; it is not a model call. Then Evaluate once [source_template_102_8, source_template_103_8, '', '## Patch under validation', '', source_template_107_8]; assign in source target order to lines.
  // Source: vvaharness/validation/session/launch_prompt.py:115-116
  if (the source predicate manifest.finding is truthy) {
    // Source: vvaharness/validation/session/launch_prompt.py:116-116
    In source order: Evaluate _append_finding_details(lines, manifest.finding, manifest.affected_files); retain side effects and discard the expression result.
  }
  // Source: vvaharness/validation/session/launch_prompt.py:117-119
  In source order: Evaluate lines.append(''); retain side effects and discard the expression result. Then Evaluate lines.append('## Session Config'); retain side effects and discard the expression result. Then Evaluate lines.append(source_template_119_17); retain side effects and discard the expression result.
  // Source: vvaharness/validation/session/launch_prompt.py:120-126
  if (the source predicate manifest.post_results is truthy) {
    // Source: vvaharness/validation/session/launch_prompt.py:121-126
    In source order: Evaluate lines.append(''); retain side effects and discard the expression result. Then Evaluate lines.append('### Post Markers'); retain side effects and discard the expression result. Then Evaluate lines.append(source_template_124_12); retain side effects and discard the expression result.
  }
  // Source: vvaharness/validation/session/launch_prompt.py:127-127
  End this invocation with source_literal_127_11.join(lines).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.validation.constants.artifacts import DIFF_FILENAME, MISSING_FIELD_PLACEHOLDER` at source line 21: `source_detail/vvaharness/validation/constants/artifacts.py.sudo.md`.
- `from vvaharness.validation.hints import hints_for` at source line 22: `source_detail/vvaharness/validation/hints/__init__.py.sudo.md`.
- `from vvaharness.validation.models import Manifest` at source line 23: `source_detail/vvaharness/validation/models/__init__.py.sudo.md`.
- `from vvaharness.models import Finding` at source line 26: `source_detail/vvaharness/models/__init__.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../prompt_representation/vvaharness/validation/session/launch_prompt.py.sudo.md). Exact strings in the evidence asset support this conversion.
