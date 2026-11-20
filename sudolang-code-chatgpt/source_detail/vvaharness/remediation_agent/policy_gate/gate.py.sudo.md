# vvaharness/remediation_agent/policy_gate/gate.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/remediation_agent/policy_gate/gate.py.evidence.json`. SHA-256: `bd2bbafeb1bc127c6595b80bf7c5d2201ea3067093198a4d8e7f1f56ab6cd132`.

```sudo
// Source: vvaharness/remediation_agent/policy_gate/gate.py:15-25
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import os; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.policy_gate.action import _FAIL_CLOSED, Action, Decision; preserve alias and import-time effects.
// Source: vvaharness/remediation_agent/policy_gate/gate.py:26-31
In source order: Resolve source import from vvaharness.remediation_agent.policy_gate.loader import _norm_cwe, parse_policy; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.policy_gate.matching import _first_match, _glob_match; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.rule_paths import locate_rule; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import logs; preserve alias and import-time effects. Then Evaluate once logs.get_logger(__name__); assign in source target order to log.
// Source: vvaharness/remediation_agent/policy_gate/gate.py:33-35
// Source signature: _default_policy_path() -> Path
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _default_policy_path() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/policy_gate/gate.py:34-34
  In source order: Retain source documentation literal source_literal_34_4; it is not a model call.
  // Source: vvaharness/remediation_agent/policy_gate/gate.py:35-35
  End this invocation with locate_rule('remediation_policy.yaml', __file__).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/policy_gate/gate.py:38-41
In source order: Evaluate once _default_policy_path(); assign in source target order to DEFAULT_POLICY_PATH. Then Evaluate once DEFAULT_POLICY_PATH.parent; assign in source target order to RULES_DIR. Then Evaluate once ('1', 'true', 'yes', 'on'); assign in source target order to _TRUE.
// Source: vvaharness/remediation_agent/policy_gate/gate.py:44-117
interface RemediationGate {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/remediation_agent/policy_gate/gate.py:46-49
  // Source signature: __init__(self, policy_path: Path | str | None=None)
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self, policy_path) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/remediation_agent/policy_gate/gate.py:47-49
    In source order: Evaluate once parse_policy(Path(policy_path) if policy_path else DEFAULT_POLICY_PATH); assign in source target order to data. Then Evaluate once data; assign in source target order to self._data. Then Evaluate once data is not None; assign in source target order to self._loaded.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/remediation_agent/policy_gate/gate.py:52-53
  // Source: vvaharness/remediation_agent/policy_gate/gate.py:51-51
  Before creating this callable, evaluate and retain decorators top-to-bottom: property.
  // Source: vvaharness/remediation_agent/policy_gate/gate.py:52-53
  // Source signature: deny_paths(self) -> list[str]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn deny_paths(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/remediation_agent/policy_gate/gate.py:53-53
    End this invocation with list(self._data.deny_paths) if self._data else [].
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vvaharness/remediation_agent/policy_gate/gate.py:56-57
  // Source: vvaharness/remediation_agent/policy_gate/gate.py:55-55
  Before creating this callable, evaluate and retain decorators top-to-bottom: property.
  // Source: vvaharness/remediation_agent/policy_gate/gate.py:56-57
  // Source signature: forbid_patch_paths(self) -> list[str]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn forbid_patch_paths(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/remediation_agent/policy_gate/gate.py:57-57
    End this invocation with list(self._data.forbid_patch_paths) if self._data else [].
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vvaharness/remediation_agent/policy_gate/gate.py:60-96
  // Source signature: decide(self, cwe_id: str | None, file_path: str) -> Decision
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn decide(self, cwe_id, file_path) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/remediation_agent/policy_gate/gate.py:61-63
    In source order: Retain source documentation literal source_literal_61_8; it is not a model call. Then Evaluate once self._data; assign in source target order to d.
    // Source: vvaharness/remediation_agent/policy_gate/gate.py:64-65
    if (the source predicate not self._loaded or d is None is truthy) {
      // Source: vvaharness/remediation_agent/policy_gate/gate.py:65-65
      End this invocation with _FAIL_CLOSED.
    }
    // Source: vvaharness/remediation_agent/policy_gate/gate.py:68-69
    if (the source predicate d.kill_env and os.environ.get(d.kill_env, '').strip().lower() in _TRUE is truthy) {
      // Source: vvaharness/remediation_agent/policy_gate/gate.py:69-69
      End this invocation with Decision(Action.GUIDANCE_ONLY, 'kill_switch_env').
    }
    // Source: vvaharness/remediation_agent/policy_gate/gate.py:70-71
    if (the source predicate d.kill_file and d.kill_file.exists() is truthy) {
      // Source: vvaharness/remediation_agent/policy_gate/gate.py:71-71
      End this invocation with Decision(Action.GUIDANCE_ONLY, 'kill_switch_file').
    }
    // Source: vvaharness/remediation_agent/policy_gate/gate.py:73-73
    In source order: Evaluate once _norm_cwe(cwe_id); assign in source target order to cwe.
    // Source: vvaharness/remediation_agent/policy_gate/gate.py:74-75
    if (the source predicate not cwe is truthy) {
      // Source: vvaharness/remediation_agent/policy_gate/gate.py:75-75
      End this invocation with Decision(Action.GUIDANCE_ONLY, 'unmapped_cwe').
    }
    // Source: vvaharness/remediation_agent/policy_gate/gate.py:78-80
    if (the source predicate cwe in d.deny is truthy) {
      // Source: vvaharness/remediation_agent/policy_gate/gate.py:79-80
      End this invocation with Decision(Action.GUIDANCE_ONLY, d.deny[cwe], matched_rule=source_template_80_41).
    }
    // Source: vvaharness/remediation_agent/policy_gate/gate.py:83-83
    In source order: Evaluate once (file_path or '').replace('\\', '/'); assign in source target order to norm_path.
    // Source: vvaharness/remediation_agent/policy_gate/gate.py:84-88
    for each pat in d.deny_paths {
      // Source: vvaharness/remediation_agent/policy_gate/gate.py:85-88
      if (the source predicate _glob_match(norm_path, pat) is truthy) {
        // Source: vvaharness/remediation_agent/policy_gate/gate.py:86-88
        End this invocation with Decision(Action.GUIDANCE_ONLY, source_template_87_32, matched_rule=source_template_88_45).
      }
    }
    // Source: vvaharness/remediation_agent/policy_gate/gate.py:91-93
    if (the source predicate cwe in d.allow is truthy) {
      // Source: vvaharness/remediation_agent/policy_gate/gate.py:92-93
      End this invocation with Decision(Action.PATCH, 'allow_list', matched_rule=source_template_93_41).
    }
    // Source: vvaharness/remediation_agent/policy_gate/gate.py:96-96
    End this invocation with Decision(d.default, 'default_action').
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/remediation_agent/policy_gate/gate.py:99-101
  // Source signature: patch_touches_forbidden(self, changed_files: list[str]) -> str | None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn patch_touches_forbidden(self, changed_files) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/remediation_agent/policy_gate/gate.py:100-100
    In source order: Retain source documentation literal source_literal_100_8; it is not a model call.
    // Source: vvaharness/remediation_agent/policy_gate/gate.py:101-101
    End this invocation with _first_match(changed_files, self.forbid_patch_paths).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/remediation_agent/policy_gate/gate.py:103-105
  // Source signature: changed_paths_hit_deny(self, changed_files: list[str]) -> str | None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn changed_paths_hit_deny(self, changed_files) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/remediation_agent/policy_gate/gate.py:104-104
    In source order: Retain source documentation literal source_literal_104_8; it is not a model call.
    // Source: vvaharness/remediation_agent/policy_gate/gate.py:105-105
    End this invocation with _first_match(changed_files, self.deny_paths).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/remediation_agent/policy_gate/gate.py:107-117
  // Source signature: forbidden_files(self, changed_files: list[str]) -> list[str]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn forbidden_files(self, changed_files) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/remediation_agent/policy_gate/gate.py:108-109
    In source order: Retain source documentation literal source_literal_108_8; it is not a model call. Then For bad, assign []; source annotation list[str].
    // Source: vvaharness/remediation_agent/policy_gate/gate.py:110-116
    for each f in changed_files or [] {
      // Source: vvaharness/remediation_agent/policy_gate/gate.py:111-111
      In source order: Evaluate once (f or '').replace('\\', '/'); assign in source target order to nf.
      // Source: vvaharness/remediation_agent/policy_gate/gate.py:112-113
      if (the source predicate not nf is truthy) {
        // Source: vvaharness/remediation_agent/policy_gate/gate.py:113-113
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/remediation_agent/policy_gate/gate.py:114-116
      if (the source predicate _first_match([nf], self.forbid_patch_paths) or _first_match([nf], self.deny_paths) is truthy) {
        // Source: vvaharness/remediation_agent/policy_gate/gate.py:116-116
        In source order: Evaluate bad.append(f); retain side effects and discard the expression result.
      }
    }
    // Source: vvaharness/remediation_agent/policy_gate/gate.py:117-117
    End this invocation with bad.
    If execution reaches this end, finish with the source implicit None result.
  }
}
```

## Local import links

- `from vvaharness.remediation_agent.policy_gate.action import _FAIL_CLOSED, Action, Decision` at source line 21: `source_detail/vvaharness/remediation_agent/policy_gate/action.py.sudo.md`.
- `from vvaharness.remediation_agent.policy_gate.loader import _norm_cwe, parse_policy` at source line 26: `source_detail/vvaharness/remediation_agent/policy_gate/loader.py.sudo.md`.
- `from vvaharness.remediation_agent.policy_gate.matching import _first_match, _glob_match` at source line 27: `source_detail/vvaharness/remediation_agent/policy_gate/matching.py.sudo.md`.
- `from vvaharness.remediation_agent.rule_paths import locate_rule` at source line 28: `source_detail/vvaharness/remediation_agent/rule_paths.py.sudo.md`.
- `from vvaharness.util import logs` at source line 29: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import logs` at source line 29: `source_detail/vvaharness/util/logs.py.sudo.md`.
