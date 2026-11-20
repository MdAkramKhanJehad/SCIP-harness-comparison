# vvaharness/validation/cli/_parser.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/validation/cli/_parser.py.evidence.json`. SHA-256: `b939d998c523d69dff9eba37a53cfde8f66ba753395263f2f0c195c328346f37`.

```sudo
// Source: vvaharness/validation/cli/_parser.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import argparse; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from typing import cast; preserve alias and import-time effects.
// Source: vvaharness/validation/cli/_parser.py:23-28
In source order: Resolve source import from vvaharness.config import Config as HarnessConfig; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.config.overrides import ValidateOverrides; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.constants.artifacts import VALIDATABLE_STATES; preserve alias and import-time effects. Then Evaluate once ' / '.join(sorted((state.value for state in VALIDATABLE_STATES))); assign in source target order to _VALIDATABLE_HELP.
// Source: vvaharness/validation/cli/_parser.py:31-87
// Source signature: _build_parser() -> argparse.ArgumentParser
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _build_parser() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/cli/_parser.py:32-44
  In source order: Retain source documentation literal source_literal_32_4; it is not a model call. Then Evaluate once argparse.ArgumentParser(prog='vvaharness validate', description='s11 — agentic validation agent (invoke as `validate` or `s11`).'); assign in source target order to parser. Then Evaluate parser.add_argument('--repo', type=Path, required=True, help='Target repository root'); retain side effects and discard the expression result. Then Evaluate parser.add_argument('--config', default=None, help='Config profile path (else default)'); retain side effects and discard the expression result. Then Evaluate parser.add_argument('--finding', dest='findings', action='append', help='Finding id to validate (repeatable)'); retain side effects and discard the expression result.
  // Source: vvaharness/validation/cli/_parser.py:45-86
  In source order: Evaluate parser.add_argument('--all', action='store_true', help=source_template_49_12); retain side effects and discard the expression result. Then Evaluate parser.add_argument('--max-findings', dest='max_findings', type=int, default=None, help=source_template_59_12); retain side effects and discard the expression result. Then Evaluate parser.add_argument('--workspace', type=Path, default=None, help=source_literal_68_12); retain side effects and discard the expression result. Then Evaluate parser.add_argument('--resume', action='store_true', help='Skip findings already validated in a prior run (cached verdict reprinted)'); retain side effects and discard the expression result. Then Evaluate parser.add_argument('--scan-report', type=Path, default=None, dest='scan_report', help='Combined report (.md) to enrich; else the newest in security-remediation/'); retain side effects and discard the expression result.
  // Source: vvaharness/validation/cli/_parser.py:87-87
  End this invocation with parser.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/cli/_parser.py:91-94
In source order: For _TUNABLE_ATTRS, assign ('effort', 'max_turns', 'max_budget_usd', 'max_findings', 'timeout', 'max_model_calls', 'orchestrator_max_model_calls'); source annotation tuple[str, ...].
// Source: vvaharness/validation/cli/_parser.py:97-107
// Source signature: _tunable_overrides(cfg: HarnessConfig) -> ValidateOverrides
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _tunable_overrides(cfg) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/cli/_parser.py:98-99
  In source order: Retain source documentation literal source_literal_98_4; it is not a model call. Then Evaluate once getattr(cfg, 'step_validate', None); assign in source target order to block.
  // Source: vvaharness/validation/cli/_parser.py:100-101
  if (the source predicate block is None is truthy) {
    // Source: vvaharness/validation/cli/_parser.py:101-101
    End this invocation with ValidateOverrides().
  }
  // Source: vvaharness/validation/cli/_parser.py:102-102
  In source order: For overrides, assign {}; source annotation dict[str, object].
  // Source: vvaharness/validation/cli/_parser.py:103-106
  for each attr in _TUNABLE_ATTRS {
    // Source: vvaharness/validation/cli/_parser.py:104-104
    In source order: Evaluate once getattr(block, attr, None); assign in source target order to value.
    // Source: vvaharness/validation/cli/_parser.py:105-106
    if (the source predicate value is not None is truthy) {
      // Source: vvaharness/validation/cli/_parser.py:106-106
      In source order: Evaluate once value; assign in source target order to overrides[attr].
    }
  }
  // Source: vvaharness/validation/cli/_parser.py:107-107
  End this invocation with cast('ValidateOverrides', overrides).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.config import Config as HarnessConfig` at source line 23: `source_detail/vvaharness/config/__init__.py.sudo.md`.
- `from vvaharness.validation.config.overrides import ValidateOverrides` at source line 24: `source_detail/vvaharness/validation/config/overrides.py.sudo.md`.
- `from vvaharness.validation.constants.artifacts import VALIDATABLE_STATES` at source line 25: `source_detail/vvaharness/validation/constants/artifacts.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../prompt_representation/vvaharness/validation/cli/_parser.py.sudo.md). Exact strings in the evidence asset support this conversion.
