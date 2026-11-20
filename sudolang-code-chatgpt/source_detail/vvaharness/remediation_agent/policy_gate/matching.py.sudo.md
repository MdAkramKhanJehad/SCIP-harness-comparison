# vvaharness/remediation_agent/policy_gate/matching.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/remediation_agent/policy_gate/matching.py.evidence.json`. SHA-256: `7bab22e5ee76ca692029f73c924c6fa4f25ec0dff534c8b5a88d9c63447832de`.

```sudo
// Source: vvaharness/remediation_agent/policy_gate/matching.py:15-18
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import fnmatch; preserve alias and import-time effects.
// Source: vvaharness/remediation_agent/policy_gate/matching.py:21-27
// Source signature: _glob_match(path: str, pat: str) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _glob_match(path, pat) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/policy_gate/matching.py:22-22
  In source order: Retain source documentation literal source_literal_22_4; it is not a model call.
  // Source: vvaharness/remediation_agent/policy_gate/matching.py:23-24
  if (the source predicate fnmatch.fnmatch(path, pat) is truthy) {
    // Source: vvaharness/remediation_agent/policy_gate/matching.py:24-24
    End this invocation with True.
  }
  // Source: vvaharness/remediation_agent/policy_gate/matching.py:25-26
  if (the source predicate pat.startswith('**/') and fnmatch.fnmatch(path, pat[3:]) is truthy) {
    // Source: vvaharness/remediation_agent/policy_gate/matching.py:26-26
    End this invocation with True.
  }
  // Source: vvaharness/remediation_agent/policy_gate/matching.py:27-27
  End this invocation with False.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/policy_gate/matching.py:30-38
// Source signature: _first_match(files: list[str] | None, patterns: list[str]) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _first_match(files, patterns) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/policy_gate/matching.py:31-37
  for each f in files or [] {
    // Source: vvaharness/remediation_agent/policy_gate/matching.py:32-32
    In source order: Evaluate once (f or '').replace('\\', '/'); assign in source target order to nf.
    // Source: vvaharness/remediation_agent/policy_gate/matching.py:33-34
    if (the source predicate not nf is truthy) {
      // Source: vvaharness/remediation_agent/policy_gate/matching.py:34-34
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/remediation_agent/policy_gate/matching.py:35-37
    for each pat in patterns {
      // Source: vvaharness/remediation_agent/policy_gate/matching.py:36-37
      if (the source predicate _glob_match(nf, pat) is truthy) {
        // Source: vvaharness/remediation_agent/policy_gate/matching.py:37-37
        End this invocation with pat.
      }
    }
  }
  // Source: vvaharness/remediation_agent/policy_gate/matching.py:38-38
  End this invocation with None.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

No statically resolved in-checkout import; external calls remain explicit dependency boundaries.
