# vvaharness/remediation_agent/select/topspec.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/remediation_agent/select/topspec.py.evidence.json`. SHA-256: `257a32432d1d7b45e9d1fe077ccf7d7c7e0c64cc6fee8835b8c10190478e8402`.

```sudo
// Source: vvaharness/remediation_agent/select/topspec.py:15-22
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from collections.abc import Sequence; preserve alias and import-time effects. Then Evaluate once 'all'; assign in source target order to ALL_FINDINGS. Then Evaluate once frozenset({'all', '*'}); assign in source target order to _ALL_TOKENS.
// Source: vvaharness/remediation_agent/select/topspec.py:25-38
// Source signature: _coerce_top_value(raw: str, *, source: str) -> int | str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _coerce_top_value(raw, source) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/select/topspec.py:26-27
  In source order: Retain source documentation literal source_literal_26_4; it is not a model call. Then Evaluate once (raw or '').strip().lower(); assign in source target order to token.
  // Source: vvaharness/remediation_agent/select/topspec.py:28-29
  if (the source predicate token in _ALL_TOKENS is truthy) {
    // Source: vvaharness/remediation_agent/select/topspec.py:29-29
    End this invocation with ALL_FINDINGS.
  }
  // Source: vvaharness/remediation_agent/select/topspec.py:30-34
  Perform the following protected operations {
    // Source: vvaharness/remediation_agent/select/topspec.py:31-31
    In source order: Evaluate once int(token); assign in source target order to n.
  }
  // Source: vvaharness/remediation_agent/select/topspec.py:32-34
  On the first matching source exception (TypeError, ValueError), in handler order {
    // Source: vvaharness/remediation_agent/select/topspec.py:33-34
    Raise ValueError(source_template_34_12).
  }
  // Source: vvaharness/remediation_agent/select/topspec.py:35-37
  if (the source predicate n <= 0 is truthy) {
    // Source: vvaharness/remediation_agent/select/topspec.py:36-37
    Raise ValueError(source_template_37_12).
  }
  // Source: vvaharness/remediation_agent/select/topspec.py:38-38
  End this invocation with n.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/select/topspec.py:41-56
// Source signature: parse_top_arg(args: Sequence[str]) -> int | str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn parse_top_arg(args) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/select/topspec.py:42-43
  In source order: Retain source documentation literal source_literal_42_4; it is not a model call. Then For raw, assign None; source annotation str | None.
  // Source: vvaharness/remediation_agent/select/topspec.py:44-53
  for each (i, a) in enumerate(args) {
    // Source: vvaharness/remediation_agent/select/topspec.py:45-50
    if (the source predicate a == '--top' is truthy) {
      // Source: vvaharness/remediation_agent/select/topspec.py:46-48
      if (the source predicate i + 1 >= len(args) is truthy) {
        // Source: vvaharness/remediation_agent/select/topspec.py:47-48
        Raise ValueError('--top requires a value, e.g. --top 5 or --top all').
      }
      // Source: vvaharness/remediation_agent/select/topspec.py:49-49
      In source order: Evaluate once args[i + 1]; assign in source target order to raw.
      // Source: vvaharness/remediation_agent/select/topspec.py:50-50
      Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
    }
    // Source: vvaharness/remediation_agent/select/topspec.py:51-53
    if (the source predicate a.startswith('--top=') is truthy) {
      // Source: vvaharness/remediation_agent/select/topspec.py:52-52
      In source order: Evaluate once a.split('=', 1)[1]; assign in source target order to raw.
      // Source: vvaharness/remediation_agent/select/topspec.py:53-53
      Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
    }
  }
  // Source: vvaharness/remediation_agent/select/topspec.py:54-55
  if (the source predicate raw is None is truthy) {
    // Source: vvaharness/remediation_agent/select/topspec.py:55-55
    End this invocation with None.
  }
  // Source: vvaharness/remediation_agent/select/topspec.py:56-56
  End this invocation with _coerce_top_value(raw, source='--top').
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/select/topspec.py:59-73
// Source signature: cfg_top_n_findings(cfg) -> int | str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn cfg_top_n_findings(cfg) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/select/topspec.py:60-62
  In source order: Retain source documentation literal source_literal_60_4; it is not a model call. Then Evaluate once getattr(cfg, 'step_remediate', None); assign in source target order to sr.
  // Source: vvaharness/remediation_agent/select/topspec.py:63-64
  if (the source predicate sr is None is truthy) {
    // Source: vvaharness/remediation_agent/select/topspec.py:64-64
    End this invocation with None.
  }
  // Source: vvaharness/remediation_agent/select/topspec.py:65-65
  In source order: Evaluate once getattr(sr, 'top_n_findings', None); assign in source target order to raw.
  // Source: vvaharness/remediation_agent/select/topspec.py:66-68
  if (the source predicate raw is None is truthy) {
    // Source: vvaharness/remediation_agent/select/topspec.py:68-68
    End this invocation with ALL_FINDINGS.
  }
  // Source: vvaharness/remediation_agent/select/topspec.py:69-73
  Perform the following protected operations {
    // Source: vvaharness/remediation_agent/select/topspec.py:70-70
    End this invocation with _coerce_top_value(str(raw), source='top_n_findings').
  }
  // Source: vvaharness/remediation_agent/select/topspec.py:71-73
  On the first matching source exception ValueError, in handler order {
    // Source: vvaharness/remediation_agent/select/topspec.py:73-73
    End this invocation with ALL_FINDINGS.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/select/topspec.py:76-83
// Source signature: resolve_top(cli_top: int | str | None, cfg) -> int | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn resolve_top(cli_top, cfg) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/select/topspec.py:77-79
  In source order: Retain source documentation literal source_literal_77_4; it is not a model call. Then Evaluate once cli_top if cli_top is not None else cfg_top_n_findings(cfg); assign in source target order to chosen.
  // Source: vvaharness/remediation_agent/select/topspec.py:80-81
  if (the source predicate isinstance(chosen, int) is truthy) {
    // Source: vvaharness/remediation_agent/select/topspec.py:81-81
    End this invocation with chosen.
  }
  // Source: vvaharness/remediation_agent/select/topspec.py:83-83
  End this invocation with None.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

No statically resolved in-checkout import; external calls remain explicit dependency boundaries.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../prompt_representation/vvaharness/remediation_agent/select/topspec.py.sudo.md). Exact strings in the evidence asset support this conversion.
