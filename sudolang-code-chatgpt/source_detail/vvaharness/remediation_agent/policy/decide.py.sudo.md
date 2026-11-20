# vvaharness/remediation_agent/policy/decide.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/remediation_agent/policy/decide.py.evidence.json`. SHA-256: `836e8422cdcf7700ba89f0b1410872421495e904f0dcafe841fab2218fcf6343`.

```sudo
// Source: vvaharness/remediation_agent/policy/decide.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from dataclasses import dataclass; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.frameworks import language_for; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.models import RemediationVerdict; preserve alias and import-time effects.
// Source: vvaharness/remediation_agent/policy/decide.py:22-25
In source order: Resolve source import from vvaharness.remediation_agent.playbook import Strategy; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.policy.context import PolicyContext; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.policy_gate import Decision; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.target import RemediationTarget; preserve alias and import-time effects.
// Source: vvaharness/remediation_agent/policy/decide.py:29-37
// Source: vvaharness/remediation_agent/policy/decide.py:28-28
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass.
// Source: vvaharness/remediation_agent/policy/decide.py:29-37
interface PreResult {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/remediation_agent/policy/decide.py:30-33
  In source order: Retain source documentation literal source_literal_30_4; it is not a model call. Then For decision, declare without assigning a value; source annotation Decision. Then For cwe, declare without assigning a value; source annotation str | None. Then For strategy, declare without assigning a value; source annotation Strategy | None.
  // Source: vvaharness/remediation_agent/policy/decide.py:36-37
  // Source: vvaharness/remediation_agent/policy/decide.py:35-35
  Before creating this callable, evaluate and retain decorators top-to-bottom: property.
  // Source: vvaharness/remediation_agent/policy/decide.py:36-37
  // Source signature: allowed(self) -> bool
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn allowed(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/remediation_agent/policy/decide.py:37-37
    End this invocation with self.decision.may_generate_patch.
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vvaharness/remediation_agent/policy/decide.py:40-50
// Source signature: pre_decision(ctx: PolicyContext, target: RemediationTarget) -> PreResult
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn pre_decision(ctx, target) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/policy/decide.py:41-45
  In source order: Retain source documentation literal source_literal_41_4; it is not a model call. Then Evaluate once target.finding.cwe; assign in source target order to cwe. Then Evaluate once target.finding.file; assign in source target order to file_path. Then Evaluate once ctx.gate.decide(cwe, file_path); assign in source target order to decision. Then Evaluate once None; assign in source target order to strategy.
  // Source: vvaharness/remediation_agent/policy/decide.py:46-49
  if (the source predicate decision.may_generate_patch is truthy) {
    // Source: vvaharness/remediation_agent/policy/decide.py:47-49
    In source order: Evaluate once language_for(file_path); assign in source target order to lang. Then Evaluate once ctx.playbook.resolve(cwe, lang, ctx.frameworks); assign in source target order to strategy.
  }
  // Source: vvaharness/remediation_agent/policy/decide.py:50-50
  End this invocation with PreResult(decision=decision, cwe=cwe, strategy=strategy).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/policy/decide.py:53-64
// Source signature: guidance_verdict(ctx: PolicyContext, target: RemediationTarget, pre: PreResult) -> RemediationVerdict
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn guidance_verdict(ctx, target, pre) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/policy/decide.py:55-56
  In source order: Retain source documentation literal source_literal_55_4; it is not a model call. Then Evaluate once pre.decision.reason; assign in source target order to reason.
  // Source: vvaharness/remediation_agent/policy/decide.py:57-64
  End this invocation with RemediationVerdict(finding_index=target.index, verdict='Denied', root_cause='', changes=[], recommendations=[], summary=source_template_63_16).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.remediation_agent.frameworks import language_for` at source line 20: `source_detail/vvaharness/remediation_agent/frameworks.py.sudo.md`.
- `from vvaharness.remediation_agent.models import RemediationVerdict` at source line 21: `source_detail/vvaharness/remediation_agent/models/__init__.py.sudo.md`.
- `from vvaharness.remediation_agent.playbook import Strategy` at source line 22: `source_detail/vvaharness/remediation_agent/playbook.py.sudo.md`.
- `from vvaharness.remediation_agent.policy.context import PolicyContext` at source line 23: `source_detail/vvaharness/remediation_agent/policy/context.py.sudo.md`.
- `from vvaharness.remediation_agent.policy_gate import Decision` at source line 24: `source_detail/vvaharness/remediation_agent/policy_gate/__init__.py.sudo.md`.
- `from vvaharness.remediation_agent.target import RemediationTarget` at source line 25: `source_detail/vvaharness/remediation_agent/target.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../prompt_representation/vvaharness/remediation_agent/policy/decide.py.sudo.md). Exact strings in the evidence asset support this conversion.
