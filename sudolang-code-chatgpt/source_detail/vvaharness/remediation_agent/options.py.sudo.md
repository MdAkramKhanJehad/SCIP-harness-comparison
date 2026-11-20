# vvaharness/remediation_agent/options.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/remediation_agent/options.py.evidence.json`. SHA-256: `b9dc0ce17f814c765403d4df7eefa2ec29213a65cbfe72e87686faef8bdb3e2e`.

```sudo
// Source: vvaharness/remediation_agent/options.py:15-22
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from dataclasses import dataclass; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.select import parse_top_arg; preserve alias and import-time effects. Then Evaluate once ('fix', 'report-only'); assign in source target order to VALID_MODES.
// Source: vvaharness/remediation_agent/options.py:26-32
// Source: vvaharness/remediation_agent/options.py:25-25
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vvaharness/remediation_agent/options.py:26-32
interface RemediateOptions {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/remediation_agent/options.py:27-31
  In source order: Retain source documentation literal source_literal_27_4; it is not a model call. Then For resume, assign False; source annotation bool. Then For interactive, assign False; source annotation bool. Then For verbose, assign False; source annotation bool. Then For mode, assign 'fix'; source annotation str.
  // Source: vvaharness/remediation_agent/options.py:32-32
  In source order: For top, assign None; source annotation int | str | None.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vvaharness/remediation_agent/options.py:35-46
// Source signature: parse_options(args: list[str]) -> RemediateOptions
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn parse_options(args) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/options.py:36-37
  In source order: Retain source documentation literal source_literal_36_4; it is not a model call. Then Evaluate once _mode_from(args); assign in source target order to mode.
  // Source: vvaharness/remediation_agent/options.py:38-39
  if (the source predicate mode not in VALID_MODES is truthy) {
    // Source: vvaharness/remediation_agent/options.py:39-39
    Raise ValueError(source_template_39_25).
  }
  // Source: vvaharness/remediation_agent/options.py:40-46
  End this invocation with RemediateOptions(resume='--resume' in args, interactive='--interactive' in args or '-i' in args, verbose='--verbose' in args or '-v' in args, mode=mode, top=parse_top_arg(args)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/options.py:49-56
// Source signature: _mode_from(args: list[str]) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _mode_from(args) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/options.py:50-50
  In source order: Retain source documentation literal source_literal_50_4; it is not a model call.
  // Source: vvaharness/remediation_agent/options.py:51-55
  for each (i, a) in enumerate(args) {
    // Source: vvaharness/remediation_agent/options.py:52-53
    if (the source predicate a == '--mode' and i + 1 < len(args) is truthy) {
      // Source: vvaharness/remediation_agent/options.py:53-53
      End this invocation with args[i + 1].
    }
    // Source: vvaharness/remediation_agent/options.py:54-55
    if (the source predicate a.startswith('--mode=') is truthy) {
      // Source: vvaharness/remediation_agent/options.py:55-55
      End this invocation with a.split('=', 1)[1].
    }
  }
  // Source: vvaharness/remediation_agent/options.py:56-56
  End this invocation with 'fix'.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.remediation_agent.select import parse_top_arg` at source line 20: `source_detail/vvaharness/remediation_agent/select/__init__.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../prompt_representation/vvaharness/remediation_agent/options.py.sudo.md). Exact strings in the evidence asset support this conversion.
