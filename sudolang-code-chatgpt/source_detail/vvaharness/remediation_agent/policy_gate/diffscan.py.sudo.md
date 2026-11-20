# vvaharness/remediation_agent/policy_gate/diffscan.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/remediation_agent/policy_gate/diffscan.py.evidence.json`. SHA-256: `9193330a392d7ff033f002ac63f0f64de9e80478b3ef03403952e18247ed7d50`.

```sudo
// Source: vvaharness/remediation_agent/policy_gate/diffscan.py:15-23
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import re; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.policy_gate.action import Action; preserve alias and import-time effects. Then Evaluate once re.compile('^diff --git a/(.+?) b/(.+?)\\s*$'); assign in source target order to _DIFF_GIT_RE.
// Source: vvaharness/remediation_agent/policy_gate/diffscan.py:24-25
In source order: Evaluate once re.compile('^\\+\\+\\+ (?:b/)?(.+?)\\s*$'); assign in source target order to _PLUS_RE. Then Evaluate once re.compile('^--- (?:a/)?(.+?)\\s*$'); assign in source target order to _MINUS_RE.
// Source: vvaharness/remediation_agent/policy_gate/diffscan.py:28-55
// Source signature: inspect_diff(diff_text: str | None) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn inspect_diff(diff_text) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/policy_gate/diffscan.py:29-29
  In source order: Retain source documentation literal source_literal_29_4; it is not a model call.
  // Source: vvaharness/remediation_agent/policy_gate/diffscan.py:30-31
  if (the source predicate not diff_text is truthy) {
    // Source: vvaharness/remediation_agent/policy_gate/diffscan.py:31-31
    End this invocation with [].
  }
  // Source: vvaharness/remediation_agent/policy_gate/diffscan.py:32-33
  In source order: For out, assign []; source annotation list[str]. Then For seen, assign set(); source annotation set[str].
  // Source: vvaharness/remediation_agent/policy_gate/diffscan.py:35-41
  // Source signature: _add(p: str) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _add(p) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/remediation_agent/policy_gate/diffscan.py:36-36
    In source order: Evaluate once (p or '').strip(); assign in source target order to p.
    // Source: vvaharness/remediation_agent/policy_gate/diffscan.py:37-38
    if (the source predicate not p or p == '/dev/null' is truthy) {
      // Source: vvaharness/remediation_agent/policy_gate/diffscan.py:38-38
      End this invocation with None.
    }
    // Source: vvaharness/remediation_agent/policy_gate/diffscan.py:39-41
    if (the source predicate p not in seen is truthy) {
      // Source: vvaharness/remediation_agent/policy_gate/diffscan.py:40-41
      In source order: Evaluate seen.add(p); retain side effects and discard the expression result. Then Evaluate out.append(p); retain side effects and discard the expression result.
    }
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/remediation_agent/policy_gate/diffscan.py:43-54
  for each line in diff_text.splitlines() {
    // Source: vvaharness/remediation_agent/policy_gate/diffscan.py:44-44
    In source order: Evaluate once _DIFF_GIT_RE.match(line); assign in source target order to m.
    // Source: vvaharness/remediation_agent/policy_gate/diffscan.py:45-47
    if (the source predicate m is truthy) {
      // Source: vvaharness/remediation_agent/policy_gate/diffscan.py:46-46
      In source order: Evaluate _add(m.group(2) or m.group(1)); retain side effects and discard the expression result.
      // Source: vvaharness/remediation_agent/policy_gate/diffscan.py:47-47
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/remediation_agent/policy_gate/diffscan.py:48-48
    In source order: Evaluate once _PLUS_RE.match(line); assign in source target order to m.
    // Source: vvaharness/remediation_agent/policy_gate/diffscan.py:49-51
    if (the source predicate m is truthy) {
      // Source: vvaharness/remediation_agent/policy_gate/diffscan.py:50-50
      In source order: Evaluate _add(m.group(1)); retain side effects and discard the expression result.
      // Source: vvaharness/remediation_agent/policy_gate/diffscan.py:51-51
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/remediation_agent/policy_gate/diffscan.py:52-52
    In source order: Evaluate once _MINUS_RE.match(line); assign in source target order to m.
    // Source: vvaharness/remediation_agent/policy_gate/diffscan.py:53-54
    if (the source predicate m is truthy) {
      // Source: vvaharness/remediation_agent/policy_gate/diffscan.py:54-54
      In source order: Evaluate _add(m.group(1)); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/remediation_agent/policy_gate/diffscan.py:55-55
  End this invocation with out.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/policy_gate/diffscan.py:58-62
// Source signature: cap_verdict(action: Action, all_gates_passed: bool) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn cap_verdict(action, all_gates_passed) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/policy_gate/diffscan.py:59-59
  In source order: Retain source documentation literal source_literal_59_4; it is not a model call.
  // Source: vvaharness/remediation_agent/policy_gate/diffscan.py:60-61
  if (the source predicate action == Action.GUIDANCE_ONLY is truthy) {
    // Source: vvaharness/remediation_agent/policy_gate/diffscan.py:61-61
    End this invocation with 'REJECT'.
  }
  // Source: vvaharness/remediation_agent/policy_gate/diffscan.py:62-62
  End this invocation with 'ACCEPT' if all_gates_passed else 'REJECT'.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.remediation_agent.policy_gate.action import Action` at source line 20: `source_detail/vvaharness/remediation_agent/policy_gate/action.py.sudo.md`.
