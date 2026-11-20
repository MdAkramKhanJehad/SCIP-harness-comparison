# vvaharness/remediation_agent/policy/context.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/remediation_agent/policy/context.py.evidence.json`. SHA-256: `6688a85f881e1e090b71df7cf3a91c08fb469ed288cc9154b9c68cb528fb90a8`.

```sudo
// Source: vvaharness/remediation_agent/policy/context.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from dataclasses import dataclass; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from vvaharness.config import is_network_path; preserve alias and import-time effects.
// Source: vvaharness/remediation_agent/policy/context.py:22-26
In source order: Resolve source import from vvaharness.orchestrator.config_paths import _resolve_against; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.frameworks import detect_frameworks; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.playbook import Playbook; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.policy_gate import RemediationGate; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import logs; preserve alias and import-time effects.
// Source: vvaharness/remediation_agent/policy/context.py:28-28
In source order: Evaluate once logs.get_logger(__name__); assign in source target order to log.
// Source: vvaharness/remediation_agent/policy/context.py:31-33
// Source signature: _sr(cfg, key: str, default)
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _sr(cfg, key, default) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/policy/context.py:32-32
  In source order: Evaluate once getattr(cfg, 'step_remediate', None); assign in source target order to sr.
  // Source: vvaharness/remediation_agent/policy/context.py:33-33
  End this invocation with getattr(sr, key, default) if sr else default.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/policy/context.py:36-38
// Source signature: policy_enabled(cfg) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn policy_enabled(cfg) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/policy/context.py:37-37
  In source order: Retain source documentation literal source_literal_37_4; it is not a model call.
  // Source: vvaharness/remediation_agent/policy/context.py:38-38
  End this invocation with bool(_sr(cfg, 'enforce_policy', True)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/policy/context.py:42-47
// Source: vvaharness/remediation_agent/policy/context.py:41-41
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass.
// Source: vvaharness/remediation_agent/policy/context.py:42-47
interface PolicyContext {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/remediation_agent/policy/context.py:43-47
  In source order: Retain source documentation literal source_literal_43_4; it is not a model call. Then For gate, declare without assigning a value; source annotation RemediationGate. Then For playbook, declare without assigning a value; source annotation Playbook. Then For frameworks, declare without assigning a value; source annotation set[str]. Then For enabled, assign True; source annotation bool.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vvaharness/remediation_agent/policy/context.py:51-67
// Source signature: _resolve_input(cfg, raw: str | None) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _resolve_input(cfg, raw) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/policy/context.py:52-52
  In source order: Retain source documentation literal source_literal_52_4; it is not a model call.
  // Source: vvaharness/remediation_agent/policy/context.py:54-55
  if (the source predicate not raw is truthy) {
    // Source: vvaharness/remediation_agent/policy/context.py:55-55
    End this invocation with None.
  }
  // Source: vvaharness/remediation_agent/policy/context.py:57-60
  if (the source predicate is_network_path(raw) is truthy) {
    // Source: vvaharness/remediation_agent/policy/context.py:58-60
    Raise ValueError(source_template_59_12).
  }
  // Source: vvaharness/remediation_agent/policy/context.py:61-62
  In source order: Evaluate once getattr(cfg, '_data', {}).get('_config_dir') if cfg else None; assign in source target order to cfg_dir. Then Evaluate once _resolve_against(Path(cfg_dir), raw) if cfg_dir else raw; assign in source target order to resolved.
  // Source: vvaharness/remediation_agent/policy/context.py:63-66
  if (the source predicate resolved and (not Path(resolved).exists()) is truthy) {
    // Source: vvaharness/remediation_agent/policy/context.py:64-65
    In source order: Evaluate log.warning('configured remediation input %r not found at %s — falling back to bundled default', raw, resolved); retain side effects and discard the expression result.
    // Source: vvaharness/remediation_agent/policy/context.py:66-66
    End this invocation with None.
  }
  // Source: vvaharness/remediation_agent/policy/context.py:67-67
  End this invocation with resolved.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/policy/context.py:70-81
// Source signature: build_context(cfg, repo_root: str | Path) -> PolicyContext
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn build_context(cfg, repo_root) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/policy/context.py:71-75
  In source order: Retain source documentation literal source_literal_71_4; it is not a model call. Then Evaluate once _resolve_input(cfg, _sr(cfg, 'policy_file', None)); assign in source target order to policy_file. Then Evaluate once _resolve_input(cfg, _sr(cfg, 'playbook_file', None)); assign in source target order to playbook_file. Then Evaluate once RemediationGate(policy_file); assign in source target order to gate. Then Evaluate once Playbook(playbook_file); assign in source target order to pb.
  // Source: vvaharness/remediation_agent/policy/context.py:76-79
  Perform the following protected operations {
    // Source: vvaharness/remediation_agent/policy/context.py:77-77
    In source order: Evaluate once detect_frameworks(repo_root); assign in source target order to fw.
  }
  // Source: vvaharness/remediation_agent/policy/context.py:78-79
  On the first matching source exception Exception, in handler order {
    // Source: vvaharness/remediation_agent/policy/context.py:79-79
    In source order: Evaluate once set(); assign in source target order to fw.
  }
  // Source: vvaharness/remediation_agent/policy/context.py:80-81
  End this invocation with PolicyContext(gate=gate, playbook=pb, frameworks=fw, enabled=policy_enabled(cfg)).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.config import is_network_path` at source line 21: `source_detail/vvaharness/config/__init__.py.sudo.md`.
- `from vvaharness.orchestrator.config_paths import _resolve_against` at source line 22: `source_detail/vvaharness/orchestrator/config_paths.py.sudo.md`.
- `from vvaharness.remediation_agent.frameworks import detect_frameworks` at source line 23: `source_detail/vvaharness/remediation_agent/frameworks.py.sudo.md`.
- `from vvaharness.remediation_agent.playbook import Playbook` at source line 24: `source_detail/vvaharness/remediation_agent/playbook.py.sudo.md`.
- `from vvaharness.remediation_agent.policy_gate import RemediationGate` at source line 25: `source_detail/vvaharness/remediation_agent/policy_gate/__init__.py.sudo.md`.
- `from vvaharness.util import logs` at source line 26: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import logs` at source line 26: `source_detail/vvaharness/util/logs.py.sudo.md`.
