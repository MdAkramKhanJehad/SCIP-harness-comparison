# vvaharness/remediation_agent/policy_gate/loader.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/remediation_agent/policy_gate/loader.py.evidence.json`. SHA-256: `359d09277f27d7306100ae3f4e83795b007e38fc7fd3c8a4a3885b118e5be875`.

```sudo
// Source: vvaharness/remediation_agent/policy_gate/loader.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from dataclasses import dataclass, field; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import import yaml; preserve alias and import-time effects.
// Source: vvaharness/remediation_agent/policy_gate/loader.py:23-26
In source order: Resolve source import from vvaharness.remediation_agent.policy_gate.action import Action; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import logs; preserve alias and import-time effects. Then Evaluate once logs.get_logger(__name__); assign in source target order to log.
// Source: vvaharness/remediation_agent/policy_gate/loader.py:29-35
// Source signature: _norm_cwe(raw) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _norm_cwe(raw) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/policy_gate/loader.py:30-30
  In source order: Retain source documentation literal source_literal_30_4; it is not a model call.
  // Source: vvaharness/remediation_agent/policy_gate/loader.py:31-32
  if (the source predicate raw is None is truthy) {
    // Source: vvaharness/remediation_agent/policy_gate/loader.py:32-32
    End this invocation with None.
  }
  // Source: vvaharness/remediation_agent/policy_gate/loader.py:33-34
  In source order: Evaluate once str(raw).strip().upper(); assign in source target order to s. Then Evaluate once s.removeprefix('CWE-'); assign in source target order to s.
  // Source: vvaharness/remediation_agent/policy_gate/loader.py:35-35
  End this invocation with source_template_35_11 if s.isdigit() else None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/policy_gate/loader.py:39-47
// Source: vvaharness/remediation_agent/policy_gate/loader.py:38-38
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass.
// Source: vvaharness/remediation_agent/policy_gate/loader.py:39-47
interface PolicyData {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/remediation_agent/policy_gate/loader.py:40-44
  In source order: Retain source documentation literal source_literal_40_4; it is not a model call. Then For deny, assign field(default_factory=dict); source annotation dict[str, str]. Then For allow, assign field(default_factory=set); source annotation set[str]. Then For deny_paths, assign field(default_factory=list); source annotation list[str]. Then For forbid_patch_paths, assign field(default_factory=list); source annotation list[str].
  // Source: vvaharness/remediation_agent/policy_gate/loader.py:45-47
  In source order: For kill_env, assign None; source annotation str | None. Then For kill_file, assign None; source annotation Path | None. Then For default, assign Action.GUIDANCE_ONLY; source annotation Action.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vvaharness/remediation_agent/policy_gate/loader.py:50-91
// Source signature: parse_policy(path: Path) -> PolicyData | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn parse_policy(path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/policy_gate/loader.py:51-51
  In source order: Retain source documentation literal source_literal_51_4; it is not a model call.
  // Source: vvaharness/remediation_agent/policy_gate/loader.py:52-56
  Perform the following protected operations {
    // Source: vvaharness/remediation_agent/policy_gate/loader.py:53-53
    In source order: Evaluate once yaml.safe_load(path.read_text(encoding='utf-8')) or {}; assign in source target order to doc.
  }
  // Source: vvaharness/remediation_agent/policy_gate/loader.py:54-56
  On the first matching source exception Exception as exc, in handler order {
    // Source: vvaharness/remediation_agent/policy_gate/loader.py:55-55
    In source order: Evaluate log.error('remediation policy load failed (%s) — fail-closed', exc); retain side effects and discard the expression result.
    // Source: vvaharness/remediation_agent/policy_gate/loader.py:56-56
    End this invocation with None.
  }
  // Source: vvaharness/remediation_agent/policy_gate/loader.py:58-61
  In source order: Evaluate once PolicyData(); assign in source target order to data. Then Evaluate once str(doc.get('default_action', 'deny')).lower(); assign in source target order to default. Then Evaluate once Action.PATCH if default == 'allow' else Action.GUIDANCE_ONLY; assign in source target order to data.default.
  // Source: vvaharness/remediation_agent/policy_gate/loader.py:63-72
  for each entry in doc.get('deny', []) or [] {
    // Source: vvaharness/remediation_agent/policy_gate/loader.py:64-64
    In source order: Evaluate once _norm_cwe(entry.get('id')); assign in source target order to cwe.
    // Source: vvaharness/remediation_agent/policy_gate/loader.py:65-66
    if (the source predicate not cwe is truthy) {
      // Source: vvaharness/remediation_agent/policy_gate/loader.py:66-66
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/remediation_agent/policy_gate/loader.py:67-68
    In source order: Evaluate once entry.get('reason', 'policy_denied'); assign in source target order to reason. Then Evaluate once reason; assign in source target order to data.deny[cwe].
    // Source: vvaharness/remediation_agent/policy_gate/loader.py:69-72
    for each child in entry.get('descendants', []) or [] {
      // Source: vvaharness/remediation_agent/policy_gate/loader.py:70-70
      In source order: Evaluate once _norm_cwe(child); assign in source target order to c.
      // Source: vvaharness/remediation_agent/policy_gate/loader.py:71-72
      if (the source predicate c is truthy) {
        // Source: vvaharness/remediation_agent/policy_gate/loader.py:72-72
        In source order: Evaluate data.deny.setdefault(c, source_template_72_40); retain side effects and discard the expression result.
      }
    }
  }
  // Source: vvaharness/remediation_agent/policy_gate/loader.py:74-77
  for each entry in doc.get('allow', []) or [] {
    // Source: vvaharness/remediation_agent/policy_gate/loader.py:75-75
    In source order: Evaluate once _norm_cwe(entry.get('id')); assign in source target order to cwe.
    // Source: vvaharness/remediation_agent/policy_gate/loader.py:76-77
    if (the source predicate cwe is truthy) {
      // Source: vvaharness/remediation_agent/policy_gate/loader.py:77-77
      In source order: Evaluate data.allow.add(cwe); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/remediation_agent/policy_gate/loader.py:79-83
  In source order: Evaluate once [str(p) for p in doc.get('deny_paths') or []]; assign in source target order to data.deny_paths. Then Evaluate once [str(p) for p in doc.get('forbid_patch_paths') or []]; assign in source target order to data.forbid_patch_paths. Then Evaluate once doc.get('kill_switch') or {}; assign in source target order to ks. Then Evaluate once ks.get('env_var') or None; assign in source target order to data.kill_env. Then Evaluate once ks.get('file'); assign in source target order to kf.
  // Source: vvaharness/remediation_agent/policy_gate/loader.py:84-90
  In source order: Evaluate once Path(kf) if kf else None; assign in source target order to data.kill_file. Then Evaluate log.info('remediation policy loaded: deny=%d allow=%d deny_paths=%d forbid_patch_paths=%d default=%s', len(data.deny), len(data.allow), len(data.deny_paths), len(data.forbid_patch_paths), data.default); retain side effects and discard the expression result.
  // Source: vvaharness/remediation_agent/policy_gate/loader.py:91-91
  End this invocation with data.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.remediation_agent.policy_gate.action import Action` at source line 23: `source_detail/vvaharness/remediation_agent/policy_gate/action.py.sudo.md`.
- `from vvaharness.util import logs` at source line 24: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import logs` at source line 24: `source_detail/vvaharness/util/logs.py.sudo.md`.
