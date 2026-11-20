# vvaharness/remediation_agent/provenance.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/remediation_agent/provenance.py.evidence.json`. SHA-256: `b508fbaabd70a379be429d5accdc4c8fa42cae65e8e58cb31826abe6b792e538`.

```sudo
// Source: vvaharness/remediation_agent/provenance.py:15-32
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from vvaharness.orchestrator import store; preserve alias and import-time effects. Then Resolve source import from vvaharness.orchestrator.checkpoints import REMEDIATE_PREFIX, load_ckpt; preserve alias and import-time effects.
// Source: vvaharness/remediation_agent/provenance.py:34-34
In source order: Evaluate once ['owned_cases']; assign in source target order to __all__.
// Source: vvaharness/remediation_agent/provenance.py:37-57
// Source signature: owned_cases(run_id: str) -> set[tuple[str, Path]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn owned_cases(run_id) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/provenance.py:38-44
  In source order: Retain source documentation literal source_literal_38_4; it is not a model call. Then For owned, assign set(); source annotation set[tuple[str, Path]].
  // Source: vvaharness/remediation_agent/provenance.py:45-56
  for each step in store.steps_with_prefix(run_id, REMEDIATE_PREFIX) {
    // Source: vvaharness/remediation_agent/provenance.py:46-46
    In source order: Evaluate once load_ckpt(Path(), run_id, step); assign in source target order to record.
    // Source: vvaharness/remediation_agent/provenance.py:47-48
    if (the source predicate not isinstance(record, dict) is truthy) {
      // Source: vvaharness/remediation_agent/provenance.py:48-48
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/remediation_agent/provenance.py:49-50
    In source order: Evaluate once record.get('finding_id'); assign in source target order to finding_id. Then Evaluate once record.get('artifact_dir'); assign in source target order to artifact_dir.
    // Source: vvaharness/remediation_agent/provenance.py:51-52
    if (the source predicate not finding_id or not artifact_dir is truthy) {
      // Source: vvaharness/remediation_agent/provenance.py:52-52
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/remediation_agent/provenance.py:53-56
    Perform the following protected operations {
      // Source: vvaharness/remediation_agent/provenance.py:54-54
      In source order: Evaluate owned.add((finding_id, Path(artifact_dir).resolve())); retain side effects and discard the expression result.
    }
    // Source: vvaharness/remediation_agent/provenance.py:55-56
    On the first matching source exception OSError, in handler order {
      // Source: vvaharness/remediation_agent/provenance.py:56-56
      Continue the immediately enclosing source loop at its next iteration.
    }
  }
  // Source: vvaharness/remediation_agent/provenance.py:57-57
  End this invocation with owned.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.orchestrator import store` at source line 31: `source_detail/vvaharness/orchestrator/__init__.py.sudo.md`.
- `from vvaharness.orchestrator import store` at source line 31: `source_detail/vvaharness/orchestrator/store/__init__.py.sudo.md`.
- `from vvaharness.orchestrator.checkpoints import REMEDIATE_PREFIX, load_ckpt` at source line 32: `source_detail/vvaharness/orchestrator/checkpoints.py.sudo.md`.
