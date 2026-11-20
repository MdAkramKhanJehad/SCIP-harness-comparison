# vvaharness/sdk/handoff.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/sdk/handoff.py.evidence.json`. SHA-256: `62f2d5951e1fa2e3c2a8a492e73188e520c2b16ad3a7bc9a3830f9b8637a5831`.

```sudo
// Source: vvaharness/sdk/handoff.py:15-20
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from collections.abc import Sequence; preserve alias and import-time effects. Then Resolve source import from dataclasses import dataclass; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects.
// Source: vvaharness/sdk/handoff.py:22-32
In source order: Resolve source import from vvaharness.models import Finding, TaskManifest, ThreatModel; preserve alias and import-time effects. Then Resolve source import from vvaharness.orchestrator import store as _store; preserve alias and import-time effects. Then Resolve source import from vvaharness.orchestrator.checkpoints import run_id_for, save_ckpt; preserve alias and import-time effects. Then Evaluate once 2000; assign in source target order to MAX_INJECTED_FINDINGS. Then For DISCOVERY_STAGES, assign ('s2', 's3'); source annotation tuple[str, ...].
// Source: vvaharness/sdk/handoff.py:35-36
interface HandoffError {
  Describe the source Python type, preserving its base/metaclass expression order: ValueError.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/sdk/handoff.py:36-36
  In source order: Retain source documentation literal source_literal_36_4; it is not a model call.
}
// Source: vvaharness/sdk/handoff.py:40-51
// Source: vvaharness/sdk/handoff.py:39-39
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vvaharness/sdk/handoff.py:40-51
interface Handoff {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/sdk/handoff.py:41-46
  In source order: Retain source documentation literal source_literal_41_4; it is not a model call. Then For run_id, declare without assigning a value; source annotation str. Then For stage, declare without assigning a value; source annotation str. Then For finding_count, declare without assigning a value; source annotation int. Then For skipped, assign (); source annotation tuple[str, ...].
  // Source: vvaharness/sdk/handoff.py:49-51
  // Source: vvaharness/sdk/handoff.py:48-48
  Before creating this callable, evaluate and retain decorators top-to-bottom: property.
  // Source: vvaharness/sdk/handoff.py:49-51
  // Source signature: resume_argv(self) -> tuple[str, ...]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn resume_argv(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/sdk/handoff.py:50-50
    In source order: Retain source documentation literal source_literal_50_8; it is not a model call.
    // Source: vvaharness/sdk/handoff.py:51-51
    End this invocation with ('--resume',).
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vvaharness/sdk/handoff.py:54-75
// Source signature: inject_findings(repo: Path | str, findings: Sequence[Finding], *, skip_discovery: bool=True) -> Handoff
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn inject_findings(repo, findings, skip_discovery) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/sdk/handoff.py:56-56
  In source order: Retain source documentation literal source_literal_56_4; it is not a model call.
  // Source: vvaharness/sdk/handoff.py:57-58
  if (the source predicate not findings is truthy) {
    // Source: vvaharness/sdk/handoff.py:58-58
    Raise HandoffError('no findings to inject').
  }
  // Source: vvaharness/sdk/handoff.py:59-61
  if (the source predicate len(findings) > MAX_INJECTED_FINDINGS is truthy) {
    // Source: vvaharness/sdk/handoff.py:60-61
    Raise HandoffError(source_template_61_12).
  }
  // Source: vvaharness/sdk/handoff.py:62-62
  In source order: Evaluate once [f for f in findings if not isinstance(f, Finding)]; assign in source target order to bad.
  // Source: vvaharness/sdk/handoff.py:63-64
  if (the source predicate bad is truthy) {
    // Source: vvaharness/sdk/handoff.py:64-64
    Raise HandoffError(source_template_64_27).
  }
  // Source: vvaharness/sdk/handoff.py:65-65
  In source order: Evaluate once Path(repo).expanduser().resolve(); assign in source target order to repo_path.
  // Source: vvaharness/sdk/handoff.py:66-67
  if (the source predicate not repo_path.is_dir() is truthy) {
    // Source: vvaharness/sdk/handoff.py:67-67
    Raise HandoffError(source_template_67_27).
  }
  // Source: vvaharness/sdk/handoff.py:68-74
  In source order: Evaluate once run_id_for(repo_path); assign in source target order to run_id. Then Evaluate once _store.state_root() / 'checkpoints' / run_id; assign in source target order to ckpt_dir. Then Evaluate _store.register_run(run_id, repo_root=str(repo_path), repo_name=repo_path.name, app_id=None); retain side effects and discard the expression result. Then Evaluate save_ckpt(ckpt_dir, run_id, 's4', {'findings': list(findings), 'outcomes': _outcomes(findings), 'input_kind': 'external'}); retain side effects and discard the expression result. Then Evaluate once _seed_discovery(ckpt_dir, run_id) if skip_discovery else (); assign in source target order to skipped.
  // Source: vvaharness/sdk/handoff.py:75-75
  End this invocation with Handoff(run_id=run_id, stage='s4', finding_count=len(findings), skipped=skipped).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/sdk/handoff.py:78-82
// Source signature: _seed_discovery(ckpt_dir: Path, run_id: str) -> tuple[str, ...]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _seed_discovery(ckpt_dir, run_id) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/sdk/handoff.py:79-81
  In source order: Retain source documentation literal source_literal_79_4; it is not a model call. Then Evaluate save_ckpt(ckpt_dir, run_id, 's2', ThreatModel()); retain side effects and discard the expression result. Then Evaluate save_ckpt(ckpt_dir, run_id, 's3', TaskManifest(units=[])); retain side effects and discard the expression result.
  // Source: vvaharness/sdk/handoff.py:82-82
  End this invocation with DISCOVERY_STAGES.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/sdk/handoff.py:85-88
// Source signature: _outcomes(findings: Sequence[Finding]) -> dict[str, str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _outcomes(findings) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/sdk/handoff.py:86-87
  In source order: Retain source documentation literal source_literal_86_4; it is not a model call. Then Evaluate once {str(getattr(f, 'origin', None) or 'external') for f in findings}; assign in source target order to origins.
  // Source: vvaharness/sdk/handoff.py:88-88
  End this invocation with dict.fromkeys(sorted(origins), 'injected').
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/sdk/handoff.py:91-92
In source order: Evaluate once ['DISCOVERY_STAGES', 'MAX_INJECTED_FINDINGS', 'Handoff', 'HandoffError', 'inject_findings']; assign in source target order to __all__.
```

## Local import links

- `from vvaharness.models import Finding, TaskManifest, ThreatModel` at source line 22: `source_detail/vvaharness/models/__init__.py.sudo.md`.
- `from vvaharness.orchestrator import store as _store` at source line 23: `source_detail/vvaharness/orchestrator/__init__.py.sudo.md`.
- `from vvaharness.orchestrator import store as _store` at source line 23: `source_detail/vvaharness/orchestrator/store/__init__.py.sudo.md`.
- `from vvaharness.orchestrator.checkpoints import run_id_for, save_ckpt` at source line 24: `source_detail/vvaharness/orchestrator/checkpoints.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../prompt_representation/vvaharness/sdk/handoff.py.sudo.md). Exact strings in the evidence asset support this conversion.
