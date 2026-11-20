# vvaharness/remediation_agent/policy/__init__.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/remediation_agent/policy/__init__.py.evidence.json`. SHA-256: `b569ddf3dc03957ad684d21987978d6134c03709d44cefd503ee163f52f04301`.

```sudo
// Source: vvaharness/remediation_agent/policy/__init__.py:15-33
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.policy.context import PolicyContext, _resolve_input, _sr, build_context, policy_enabled; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.policy.decide import PreResult, guidance_verdict, pre_decision; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.policy.patch_content import scan_added_lines, undeclared_edited_files; preserve alias and import-time effects.
// Source: vvaharness/remediation_agent/policy/__init__.py:34-66
In source order: Resolve source import from vvaharness.remediation_agent.policy.postgate import PostResult, enforce_post, worktree_forbidden_matches; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.policy.revert import revert_files; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.policy.symlink_jail import describe_escapes, escaping_symlinks; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.policy.workflow_refs import introduced_unsafe_workflow_refs, workflow_snapshot_paths; preserve alias and import-time effects. Then Evaluate once ['PolicyContext', 'PostResult', 'PreResult', 'build_context', 'describe_escapes', 'enforce_post', 'escaping_symlinks', 'guidance_verdict', 'introduced_unsafe_workflow_refs', 'policy_enabled', 'pre_decision', 'revert_files', 'scan_added_lines', 'undeclared_edited_files', 'workflow_snapshot_paths', 'worktree_forbidden_matches']; assign in source target order to __all__.
```

## Local import links

- `from vvaharness.remediation_agent.policy.context import PolicyContext, _resolve_input, _sr, build_context, policy_enabled` at source line 18: `source_detail/vvaharness/remediation_agent/policy/context.py.sudo.md`.
- `from vvaharness.remediation_agent.policy.decide import PreResult, guidance_verdict, pre_decision` at source line 25: `source_detail/vvaharness/remediation_agent/policy/decide.py.sudo.md`.
- `from vvaharness.remediation_agent.policy.patch_content import scan_added_lines, undeclared_edited_files` at source line 30: `source_detail/vvaharness/remediation_agent/policy/patch_content.py.sudo.md`.
- `from vvaharness.remediation_agent.policy.postgate import PostResult, enforce_post, worktree_forbidden_matches` at source line 34: `source_detail/vvaharness/remediation_agent/policy/postgate.py.sudo.md`.
- `from vvaharness.remediation_agent.policy.revert import revert_files` at source line 39: `source_detail/vvaharness/remediation_agent/policy/revert.py.sudo.md`.
- `from vvaharness.remediation_agent.policy.symlink_jail import describe_escapes, escaping_symlinks` at source line 40: `source_detail/vvaharness/remediation_agent/policy/symlink_jail.py.sudo.md`.
- `from vvaharness.remediation_agent.policy.workflow_refs import introduced_unsafe_workflow_refs, workflow_snapshot_paths` at source line 44: `source_detail/vvaharness/remediation_agent/policy/workflow_refs.py.sudo.md`.
