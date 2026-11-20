# vvaharness/remediation_agent/plugin_runner/trace.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/remediation_agent/plugin_runner/trace.py.evidence.json`. SHA-256: `191699482afba3088e893c44cc44a761d32b32710a77f043dd57af7aa705f085`.

```sudo
// Source: vvaharness/remediation_agent/plugin_runner/trace.py:15-20
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.target import RemediationTarget; preserve alias and import-time effects. Then Resolve source import from vvaharness.report.redact import redact; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import console; preserve alias and import-time effects.
// Source: vvaharness/remediation_agent/plugin_runner/trace.py:23-29
// Source signature: dump(title: str, body: str) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn dump(title, body) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/plugin_runner/trace.py:24-26
  In source order: Retain source documentation literal source_literal_24_4; it is not a model call. Then Evaluate once '─' * 72; assign in source target order to bar. Then Evaluate console.write(source_template_26_18); retain side effects and discard the expression result.
  // Source: vvaharness/remediation_agent/plugin_runner/trace.py:27-28
  for each line in redact(body or '').splitlines() or [''] {
    // Source: vvaharness/remediation_agent/plugin_runner/trace.py:28-28
    In source order: Evaluate console.write(source_template_28_22); retain side effects and discard the expression result.
  }
  // Source: vvaharness/remediation_agent/plugin_runner/trace.py:29-29
  In source order: Evaluate console.write(source_template_29_18); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/plugin_runner/trace.py:32-53
// Source signature: dump_policy(target: RemediationTarget, pre) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn dump_policy(target, pre) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/plugin_runner/trace.py:33-39
  In source order: Retain source documentation literal source_literal_33_4; it is not a model call. Then Evaluate once pre.decision; assign in source target order to decision. Then Evaluate console.write(source_template_35_18); retain side effects and discard the expression result. Then Evaluate console.write(source_template_37_18); retain side effects and discard the expression result. Then Evaluate console.write(source_template_38_18); retain side effects and discard the expression result.
  // Source: vvaharness/remediation_agent/plugin_runner/trace.py:40-41
  In source order: Evaluate console.write(source_template_40_18); retain side effects and discard the expression result. Then Evaluate once getattr(decision, 'matched_rule', None); assign in source target order to matched.
  // Source: vvaharness/remediation_agent/plugin_runner/trace.py:42-43
  if (the source predicate matched is truthy) {
    // Source: vvaharness/remediation_agent/plugin_runner/trace.py:43-43
    In source order: Evaluate console.write(source_template_43_22); retain side effects and discard the expression result.
  }
  // Source: vvaharness/remediation_agent/plugin_runner/trace.py:44-49
  if (the source predicate pre.strategy is not None is truthy) {
    // Source: vvaharness/remediation_agent/plugin_runner/trace.py:45-47
    In source order: Evaluate console.write(source_template_45_22); retain side effects and discard the expression result.
  }
  else {
    // Source: vvaharness/remediation_agent/plugin_runner/trace.py:49-49
    In source order: Evaluate console.write('  │ playbook strategy: (none resolved — guidance-only)'); retain side effects and discard the expression result.
  }
  // Source: vvaharness/remediation_agent/plugin_runner/trace.py:50-50
  In source order: Evaluate console.write(source_template_50_18); retain side effects and discard the expression result.
  // Source: vvaharness/remediation_agent/plugin_runner/trace.py:51-53
  if (the source predicate pre.strategy is not None is truthy) {
    // Source: vvaharness/remediation_agent/plugin_runner/trace.py:52-53
    In source order: Evaluate dump(source_template_52_13, pre.strategy.as_prompt_block()); retain side effects and discard the expression result.
  }
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.remediation_agent.target import RemediationTarget` at source line 18: `source_detail/vvaharness/remediation_agent/target.py.sudo.md`.
- `from vvaharness.report.redact import redact` at source line 19: `source_detail/vvaharness/report/redact.py.sudo.md`.
- `from vvaharness.util import console` at source line 20: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import console` at source line 20: `source_detail/vvaharness/util/console.py.sudo.md`.
