# vvaharness/remediation_agent/prompts.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/remediation_agent/prompts.py.evidence.json`. SHA-256: `9d609cc3c0eea845d78fcea488c0b36e53e97d340f408a43da7cb89639576cbf`.

```sudo
// Source: vvaharness/remediation_agent/prompts.py:15-20
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.models import RemediationVerdict; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.render import render_finding_md; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.target import RemediationTarget; preserve alias and import-time effects.
// Source: vvaharness/remediation_agent/prompts.py:23-74
// Source signature: build_system() -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn build_system() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/prompts.py:24-24
  In source order: Retain source documentation literal source_literal_24_4; it is not a model call.
  // Source: vvaharness/remediation_agent/prompts.py:25-74
  End this invocation with source_template_25_11.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/prompts.py:79-103
In source order: Evaluate once build_system(); assign in source target order to SYSTEM. Then Evaluate once source_literal_82_15; assign in source target order to FIXER_SYSTEM.
// Source: vvaharness/remediation_agent/prompts.py:106-165
// Source signature: build_orchestrator_system() -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn build_orchestrator_system() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/prompts.py:107-107
  In source order: Retain source documentation literal source_literal_107_4; it is not a model call.
  // Source: vvaharness/remediation_agent/prompts.py:109-165
  End this invocation with source_literal_109_11.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/prompts.py:168-168
In source order: Evaluate once build_orchestrator_system(); assign in source target order to ORCHESTRATOR_SYSTEM.
// Source: vvaharness/remediation_agent/prompts.py:171-184
// Source signature: _policy_block(*, deny_paths: list[str] | None, forbid_paths: list[str] | None) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _policy_block(deny_paths, forbid_paths) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/prompts.py:173-173
  In source order: Retain source documentation literal source_literal_173_4; it is not a model call.
  // Source: vvaharness/remediation_agent/prompts.py:174-175
  if (the source predicate not (deny_paths or forbid_paths) is truthy) {
    // Source: vvaharness/remediation_agent/prompts.py:175-175
    End this invocation with ''.
  }
  // Source: vvaharness/remediation_agent/prompts.py:176-177
  In source order: Evaluate once ['', '## Remediation policy (authoritative)']; assign in source target order to lines. Then Evaluate once sorted(set((deny_paths or []) + (forbid_paths or []))); assign in source target order to paths.
  // Source: vvaharness/remediation_agent/prompts.py:178-183
  if (the source predicate paths is truthy) {
    // Source: vvaharness/remediation_agent/prompts.py:179-183
    In source order: Evaluate once ', '.join(paths[:24]) + (' …' if len(paths) > 24 else ''); assign in source target order to shown. Then Evaluate lines.append(source_template_181_12); retain side effects and discard the expression result.
  }
  // Source: vvaharness/remediation_agent/prompts.py:184-184
  End this invocation with source_literal_184_11.join(lines) + source_literal_184_30.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/prompts.py:187-207
// Source signature: build_user(target: RemediationTarget, repo: str, mode: str='fix', *, strategy_block: str | None=None, deny_paths: list[str] | None=None, forbid_paths: list[str] | None=None) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn build_user(target, repo, mode, strategy_block, deny_paths, forbid_paths) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/prompts.py:191-196
  In source order: Retain source documentation literal source_literal_191_4; it is not a model call. Then Evaluate once render_finding_md(target.finding, target.index) or target.label; assign in source target order to body. Then Evaluate once 'apply the minimal safe fix' if mode == 'fix' else 'describe the minimal safe fix (do NOT edit files)'; assign in source target order to action. Then Evaluate once source_template_195_12 if strategy_block else ''; assign in source target order to strat. Then Evaluate once _policy_block(deny_paths=deny_paths, forbid_paths=forbid_paths); assign in source target order to policy.
  // Source: vvaharness/remediation_agent/prompts.py:197-207
  End this invocation with source_template_197_11.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.remediation_agent.models import RemediationVerdict` at source line 18: `source_detail/vvaharness/remediation_agent/models/__init__.py.sudo.md`.
- `from vvaharness.remediation_agent.render import render_finding_md` at source line 19: `source_detail/vvaharness/remediation_agent/render.py.sudo.md`.
- `from vvaharness.remediation_agent.target import RemediationTarget` at source line 20: `source_detail/vvaharness/remediation_agent/target.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../prompt_representation/vvaharness/remediation_agent/prompts.py.sudo.md). Exact strings in the evidence asset support this conversion.
