# vvaharness/remediation_agent/policy_gate/__init__.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/remediation_agent/policy_gate/__init__.py.evidence.json`. SHA-256: `6ee6901fca8deba191433099be114bf7dac46b3baeb3ba22897e7471215f5290`.

```sudo
// Source: vvaharness/remediation_agent/policy_gate/__init__.py:15-30
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.policy_gate.action import Action, Decision; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.policy_gate.diffscan import cap_verdict, inspect_diff; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.policy_gate.gate import DEFAULT_POLICY_PATH, RULES_DIR, RemediationGate; preserve alias and import-time effects.
// Source: vvaharness/remediation_agent/policy_gate/__init__.py:31-44
In source order: Resolve source import from vvaharness.remediation_agent.policy_gate.matching import _first_match, _glob_match; preserve alias and import-time effects. Then Evaluate once ['DEFAULT_POLICY_PATH', 'RULES_DIR', 'Action', 'Decision', 'RemediationGate', 'cap_verdict', 'inspect_diff']; assign in source target order to __all__.
```

## Local import links

- `from vvaharness.remediation_agent.policy_gate.action import Action, Decision` at source line 18: `source_detail/vvaharness/remediation_agent/policy_gate/action.py.sudo.md`.
- `from vvaharness.remediation_agent.policy_gate.diffscan import cap_verdict, inspect_diff` at source line 22: `source_detail/vvaharness/remediation_agent/policy_gate/diffscan.py.sudo.md`.
- `from vvaharness.remediation_agent.policy_gate.gate import DEFAULT_POLICY_PATH, RULES_DIR, RemediationGate` at source line 26: `source_detail/vvaharness/remediation_agent/policy_gate/gate.py.sudo.md`.
- `from vvaharness.remediation_agent.policy_gate.matching import _first_match, _glob_match` at source line 31: `source_detail/vvaharness/remediation_agent/policy_gate/matching.py.sudo.md`.
