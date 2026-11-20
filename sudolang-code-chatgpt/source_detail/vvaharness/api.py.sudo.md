# vvaharness/api.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/api.py.evidence.json`. SHA-256: `6f5a61aad11d55e7ca0c673949a3766790806392a7a2cd7d8e5c26124c090ccf`.

```sudo
// Source: vvaharness/api.py:15-41
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from vvaharness.models import Finding, MergeReadiness, Remediation, ScoringPolicy, Verdict, merge_readiness_for, state_of; preserve alias and import-time effects. Then Evaluate once ['Finding', 'MergeReadiness', 'Remediation', 'ScoringPolicy', 'Verdict', 'merge_readiness_for', 'remediate', 'state_of', 'validate']; assign in source target order to __all__.
// Source: vvaharness/api.py:44-74
// Source signature: remediate(finding: Finding, *, repo: Path, mode: str='fix', config: Path | None=None, verbose: bool=False) -> Remediation
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn remediate(finding, repo, mode, config, verbose) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/api.py:46-50
  In source order: Retain source documentation literal source_literal_46_4; it is not a model call. Then Resolve source import from vvaharness import __version__; preserve alias and import-time effects. Then Resolve source import from vvaharness.orchestrator.artifacts import artifact_dir; preserve alias and import-time effects. Then Resolve source import from vvaharness.orchestrator.checkpoints import REMEDIATE_PREFIX, save_ckpt, step_key_for; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.discovery import prepare_layout; preserve alias and import-time effects.
  // Source: vvaharness/api.py:51-61
  In source order: Resolve source import from vvaharness.remediation_agent.plugin_runner import ENGINE_ID, apply_plugin, checkpoint_record, engine_model; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.target import RemediationTarget; preserve alias and import-time effects. Then Evaluate once Path(repo); assign in source target order to repo. Then Evaluate once _config(config); assign in source target order to cfg. Then Evaluate once prepare_layout(repo); assign in source target order to layout.
  // Source: vvaharness/api.py:62-71
  In source order: Evaluate once RemediationTarget(finding=finding, index=1); assign in source target order to target. Then Evaluate once artifact_dir(layout.rem_dir, target.slug); assign in source target order to out_dir. Then Evaluate once apply_plugin(target, out_dir, cfg=cfg, repo=repo, mode=mode, verbose=verbose); assign in source target order to remediation. Then Evaluate once engine_model(cfg); assign in source target order to (model, backend). Then Evaluate once step_key_for(REMEDIATE_PREFIX, engine_id=ENGINE_ID, engine_version=__version__, case_id=target.case_id, model=model, backend=backend); assign in source target order to step.
  // Source: vvaharness/api.py:72-73
  In source order: Evaluate once {**checkpoint_record(target, out_dir, remediation), 'finding_id': target.case_id}; assign in source target order to record. Then Evaluate save_ckpt(layout.ckpt_dir, layout.run_id, step, record); retain side effects and discard the expression result.
  // Source: vvaharness/api.py:74-74
  End this invocation with remediation.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/api.py:77-83
// Source signature: validate(finding: Finding, remediation: Remediation, *, repo: Path, config: Path | None=None) -> Verdict
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn validate(finding, remediation, repo, config) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/api.py:79-80
  In source order: Retain source documentation literal source_literal_79_4; it is not a model call. Then Resolve source import from vvaharness.validation.case_api import validate_case; preserve alias and import-time effects.
  // Source: vvaharness/api.py:82-83
  End this invocation with validate_case(finding, remediation, repo=Path(repo), config=_validation_config(config)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/api.py:86-92
// Source signature: _validation_config(config: Path | None) -> object
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _validation_config(config) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/api.py:87-87
  In source order: Retain source documentation literal source_literal_87_4; it is not a model call.
  // Source: vvaharness/api.py:88-89
  if (the source predicate config is None is truthy) {
    // Source: vvaharness/api.py:89-89
    End this invocation with None.
  }
  // Source: vvaharness/api.py:90-90
  In source order: Resolve source import from vvaharness.validation.config import load_config; preserve alias and import-time effects.
  // Source: vvaharness/api.py:92-92
  End this invocation with load_config(project_root=Path(config).parent).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/api.py:95-100
// Source signature: _config(config: Path | None) -> object
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _config(config) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/api.py:96-98
  In source order: Retain source documentation literal source_literal_96_4; it is not a model call. Then Resolve source import from vvaharness import config as config_mod; preserve alias and import-time effects. Then Resolve source import from vvaharness.orchestrator import _default_config; preserve alias and import-time effects.
  // Source: vvaharness/api.py:100-100
  End this invocation with config_mod.load(str(config if config is not None else _default_config())).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.models import Finding, MergeReadiness, Remediation, ScoringPolicy, Verdict, merge_readiness_for, state_of` at source line 21: `source_detail/vvaharness/models/__init__.py.sudo.md`.
- `from vvaharness import __version__` at source line 47: `source_detail/vvaharness/__init__.py.sudo.md`.
- `from vvaharness.orchestrator.artifacts import artifact_dir` at source line 48: `source_detail/vvaharness/orchestrator/artifacts.py.sudo.md`.
- `from vvaharness.orchestrator.checkpoints import REMEDIATE_PREFIX, save_ckpt, step_key_for` at source line 49: `source_detail/vvaharness/orchestrator/checkpoints.py.sudo.md`.
- `from vvaharness.remediation_agent.discovery import prepare_layout` at source line 50: `source_detail/vvaharness/remediation_agent/discovery.py.sudo.md`.
- `from vvaharness.remediation_agent.plugin_runner import ENGINE_ID, apply_plugin, checkpoint_record, engine_model` at source line 51: `source_detail/vvaharness/remediation_agent/plugin_runner/__init__.py.sudo.md`.
- `from vvaharness.remediation_agent.target import RemediationTarget` at source line 57: `source_detail/vvaharness/remediation_agent/target.py.sudo.md`.
- `from vvaharness.validation.case_api import validate_case` at source line 80: `source_detail/vvaharness/validation/case_api.py.sudo.md`.
- `from vvaharness.validation.config import load_config` at source line 90: `source_detail/vvaharness/validation/config/__init__.py.sudo.md`.
- `from vvaharness import config as config_mod` at source line 97: `source_detail/vvaharness/__init__.py.sudo.md`.
- `from vvaharness import config as config_mod` at source line 97: `source_detail/vvaharness/config/__init__.py.sudo.md`.
- `from vvaharness.orchestrator import _default_config` at source line 98: `source_detail/vvaharness/orchestrator/__init__.py.sudo.md`.
