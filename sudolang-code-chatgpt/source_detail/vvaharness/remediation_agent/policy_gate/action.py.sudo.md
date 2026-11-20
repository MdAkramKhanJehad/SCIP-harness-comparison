# vvaharness/remediation_agent/policy_gate/action.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/remediation_agent/policy_gate/action.py.evidence.json`. SHA-256: `677373f8e77ce7d5566d30ea648a3f8a768046f52ba6b2bc1106a70584966129`.

```sudo
// Source: vvaharness/remediation_agent/policy_gate/action.py:15-19
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from dataclasses import dataclass; preserve alias and import-time effects. Then Resolve source import from enum import Enum; preserve alias and import-time effects.
// Source: vvaharness/remediation_agent/policy_gate/action.py:22-25
interface Action {
  Describe the source Python type, preserving its base/metaclass expression order: str, Enum.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/remediation_agent/policy_gate/action.py:24-25
  In source order: Evaluate once 'patch'; assign in source target order to PATCH. Then Evaluate once 'guidance_only'; assign in source target order to GUIDANCE_ONLY.
}
// Source: vvaharness/remediation_agent/policy_gate/action.py:29-36
// Source: vvaharness/remediation_agent/policy_gate/action.py:28-28
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vvaharness/remediation_agent/policy_gate/action.py:29-36
interface Decision {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/remediation_agent/policy_gate/action.py:30-32
  In source order: For action, declare without assigning a value; source annotation Action. Then For reason, declare without assigning a value; source annotation str. Then For matched_rule, assign None; source annotation str | None.
  // Source: vvaharness/remediation_agent/policy_gate/action.py:35-36
  // Source: vvaharness/remediation_agent/policy_gate/action.py:34-34
  Before creating this callable, evaluate and retain decorators top-to-bottom: property.
  // Source: vvaharness/remediation_agent/policy_gate/action.py:35-36
  // Source signature: may_generate_patch(self) -> bool
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn may_generate_patch(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/remediation_agent/policy_gate/action.py:36-36
    End this invocation with self.action is Action.PATCH.
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vvaharness/remediation_agent/policy_gate/action.py:39-39
In source order: Evaluate once Decision(Action.GUIDANCE_ONLY, 'policy_unavailable_fail_closed'); assign in source target order to _FAIL_CLOSED.
```

## Local import links

No statically resolved in-checkout import; external calls remain explicit dependency boundaries.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../prompt_representation/vvaharness/remediation_agent/policy_gate/action.py.sudo.md). Exact strings in the evidence asset support this conversion.
