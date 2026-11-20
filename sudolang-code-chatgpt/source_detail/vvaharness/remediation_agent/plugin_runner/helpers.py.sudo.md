# vvaharness/remediation_agent/plugin_runner/helpers.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/remediation_agent/plugin_runner/helpers.py.evidence.json`. SHA-256: `6d25039172d59c67abc4e5dc7d7d948c7f1461c6a615750e53e87786c0915fa2`.

```sudo
// Source: vvaharness/remediation_agent/plugin_runner/helpers.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from typing import Any; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.models import RemediationVerdict; preserve alias and import-time effects.
// Source: vvaharness/remediation_agent/plugin_runner/helpers.py:22-27
In source order: Resolve source import from vvaharness.remediation_agent.prompts import build_user; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.target import RemediationTarget; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.json_extract import extract_json; preserve alias and import-time effects. Then Evaluate once ['Read', 'Glob', 'Grep']; assign in source target order to _DEFAULT_TOOLS.
// Source: vvaharness/remediation_agent/plugin_runner/helpers.py:30-33
// Source signature: _tools(cfg) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _tools(cfg) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/plugin_runner/helpers.py:31-32
  In source order: Evaluate once getattr(cfg, 'step_remediate', None); assign in source target order to sr. Then Evaluate once getattr(sr, 'allowed_tools', None); assign in source target order to tools.
  // Source: vvaharness/remediation_agent/plugin_runner/helpers.py:33-33
  End this invocation with list(tools) if tools else list(_DEFAULT_TOOLS).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/plugin_runner/helpers.py:36-45
// Source signature: _build_user(target: RemediationTarget, repo: Path, mode: str, *, pre=None, ctx=None) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _build_user(target, repo, mode, pre, ctx) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/plugin_runner/helpers.py:38-38
  In source order: Retain source documentation literal source_literal_38_4; it is not a model call.
  // Source: vvaharness/remediation_agent/plugin_runner/helpers.py:39-44
  if (the source predicate pre is not None and ctx is not None and (pre.strategy is not None) is truthy) {
    // Source: vvaharness/remediation_agent/plugin_runner/helpers.py:40-44
    End this invocation with build_user(target, str(repo), mode=mode, strategy_block=pre.strategy.as_prompt_block(), deny_paths=ctx.gate.deny_paths, forbid_paths=ctx.gate.forbid_patch_paths).
  }
  // Source: vvaharness/remediation_agent/plugin_runner/helpers.py:45-45
  End this invocation with build_user(target, str(repo), mode=mode).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/plugin_runner/helpers.py:48-63
// Source signature: _coerce_verdict(raw: Any, target: RemediationTarget) -> RemediationVerdict
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _coerce_verdict(raw, target) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/plugin_runner/helpers.py:49-49
  In source order: Retain source documentation literal source_literal_49_4; it is not a model call.
  // Source: vvaharness/remediation_agent/plugin_runner/helpers.py:50-52
  if (the source predicate isinstance(raw, RemediationVerdict) is truthy) {
    // Source: vvaharness/remediation_agent/plugin_runner/helpers.py:51-51
    In source order: Evaluate once target.index; assign in source target order to raw.finding_index.
    // Source: vvaharness/remediation_agent/plugin_runner/helpers.py:52-52
    End this invocation with raw.
  }
  // Source: vvaharness/remediation_agent/plugin_runner/helpers.py:53-54
  if (the source predicate isinstance(raw, dict) is truthy) {
    // Source: vvaharness/remediation_agent/plugin_runner/helpers.py:54-54
    End this invocation with RemediationVerdict.coerce(raw, finding_index=target.index).
  }
  // Source: vvaharness/remediation_agent/plugin_runner/helpers.py:55-62
  Perform the following protected operations {
    // Source: vvaharness/remediation_agent/plugin_runner/helpers.py:56-56
    In source order: Evaluate once extract_json(raw); assign in source target order to data.
  }
  // Source: vvaharness/remediation_agent/plugin_runner/helpers.py:57-62
  On the first matching source exception Exception as e, in handler order {
    // Source: vvaharness/remediation_agent/plugin_runner/helpers.py:58-62
    End this invocation with RemediationVerdict(finding_index=target.index, verdict='Needs Review', summary=source_template_61_20).
  }
  // Source: vvaharness/remediation_agent/plugin_runner/helpers.py:63-63
  End this invocation with RemediationVerdict.coerce(data, finding_index=target.index).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.remediation_agent.models import RemediationVerdict` at source line 21: `source_detail/vvaharness/remediation_agent/models/__init__.py.sudo.md`.
- `from vvaharness.remediation_agent.prompts import build_user` at source line 22: `source_detail/vvaharness/remediation_agent/prompts.py.sudo.md`.
- `from vvaharness.remediation_agent.target import RemediationTarget` at source line 23: `source_detail/vvaharness/remediation_agent/target.py.sudo.md`.
- `from vvaharness.util.json_extract import extract_json` at source line 24: `source_detail/vvaharness/util/json_extract.py.sudo.md`.
