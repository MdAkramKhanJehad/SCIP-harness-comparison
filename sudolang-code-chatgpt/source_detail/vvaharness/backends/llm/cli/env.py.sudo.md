# vvaharness/backends/llm/cli/env.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/backends/llm/cli/env.py.evidence.json`. SHA-256: `dba3e0a6881ea2c913f95272a54fcb7a155c52c5dcf33e53ee45286ad3638a5f`.

```sudo
// Source: vvaharness/backends/llm/cli/env.py:15-23
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import os; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.models import EffortLevel; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm.cli import discovery as _discovery; preserve alias and import-time effects.
// Source: vvaharness/backends/llm/cli/env.py:24-31
In source order: Resolve source import from vvaharness.backends.llm.models import CliConfig; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm.tls import coerce_verify; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import logs; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.events import Event; preserve alias and import-time effects. Then Evaluate once logs.get_logger(__name__); assign in source target order to log.
// Source: vvaharness/backends/llm/cli/env.py:35-38
In source order: For _cfg, assign {'verify_ssl': True, 'ca_cert': None, 'client_cert': None, 'no_proxy': None, 'effort': 'high', 'restricted': True}; source annotation CliConfig. Then For _tls_extra, assign {}; source annotation dict.
// Source: vvaharness/backends/llm/cli/env.py:41-66
// Source signature: _build_tls_env() -> dict
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _build_tls_env() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli/env.py:42-47
  In source order: Retain source documentation literal source_literal_42_4; it is not a model call. Then For out, assign {}; source annotation dict. Then Evaluate once _cfg['ca_cert']; assign in source target order to ca. Then Evaluate once _cfg['verify_ssl']; assign in source target order to verify. Then Evaluate once ca or (verify if isinstance(verify, str) else None); assign in source target order to bundle.
  // Source: vvaharness/backends/llm/cli/env.py:48-52
  if (the source predicate bundle is truthy) {
    // Source: vvaharness/backends/llm/cli/env.py:49-52
    if (the source predicate os.path.exists(bundle) is truthy) {
      // Source: vvaharness/backends/llm/cli/env.py:50-50
      In source order: Evaluate once bundle; assign in source target order to out['NODE_EXTRA_CA_CERTS'].
    }
    else {
      // Source: vvaharness/backends/llm/cli/env.py:52-52
      In source order: Evaluate log.warning(Event.TLS_CA_NOT_FOUND, path=bundle); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/backends/llm/cli/env.py:53-56
  if (the source predicate verify is False is truthy) {
    // Source: vvaharness/backends/llm/cli/env.py:54-56
    In source order: Evaluate once '0'; assign in source target order to out['NODE_TLS_REJECT_UNAUTHORIZED']. Then Evaluate log.warning('TLS verification disabled (verify_ssl=false) for the claude subprocess'); retain side effects and discard the expression result.
  }
  // Source: vvaharness/backends/llm/cli/env.py:57-57
  In source order: Evaluate once _cfg['no_proxy']; assign in source target order to np.
  // Source: vvaharness/backends/llm/cli/env.py:58-60
  if (the source predicate np is truthy) {
    // Source: vvaharness/backends/llm/cli/env.py:59-60
    In source order: Evaluate once np; assign in source target order to out['NO_PROXY']. Then Evaluate once np; assign in source target order to out['no_proxy'].
  }
  // Source: vvaharness/backends/llm/cli/env.py:61-65
  if (the source predicate _cfg['client_cert'] is truthy) {
    // Source: vvaharness/backends/llm/cli/env.py:62-65
    In source order: Evaluate log.warning(source_literal_62_20); retain side effects and discard the expression result.
  }
  // Source: vvaharness/backends/llm/cli/env.py:66-66
  End this invocation with out.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cli/env.py:69-90
// Source signature: configure(*, verify_ssl: bool | str | None=None, ca_cert: str | None=None, client_cert: str | tuple | None=None, no_proxy: str | None=None, effort: str | None=None, restricted: bool | None=None) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn configure(verify_ssl, ca_cert, client_cert, no_proxy, effort, restricted) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli/env.py:75-75
  In source order: Retain source documentation literal source_literal_75_4; it is not a model call.
  // Source: vvaharness/backends/llm/cli/env.py:76-77
  if (the source predicate verify_ssl is not None is truthy) {
    // Source: vvaharness/backends/llm/cli/env.py:77-77
    In source order: Evaluate once coerce_verify(verify_ssl); assign in source target order to _cfg['verify_ssl'].
  }
  // Source: vvaharness/backends/llm/cli/env.py:78-79
  if (the source predicate ca_cert is truthy) {
    // Source: vvaharness/backends/llm/cli/env.py:79-79
    In source order: Evaluate once ca_cert; assign in source target order to _cfg['ca_cert'].
  }
  // Source: vvaharness/backends/llm/cli/env.py:80-81
  if (the source predicate client_cert is truthy) {
    // Source: vvaharness/backends/llm/cli/env.py:81-81
    In source order: Evaluate once client_cert; assign in source target order to _cfg['client_cert'].
  }
  // Source: vvaharness/backends/llm/cli/env.py:82-83
  if (the source predicate no_proxy is truthy) {
    // Source: vvaharness/backends/llm/cli/env.py:83-83
    In source order: Evaluate once no_proxy; assign in source target order to _cfg['no_proxy'].
  }
  // Source: vvaharness/backends/llm/cli/env.py:84-85
  if (the source predicate effort is truthy) {
    // Source: vvaharness/backends/llm/cli/env.py:85-85
    In source order: Evaluate once effort; assign in source target order to _cfg['effort'].
  }
  // Source: vvaharness/backends/llm/cli/env.py:87-88
  if (the source predicate restricted is not None is truthy) {
    // Source: vvaharness/backends/llm/cli/env.py:88-88
    In source order: Evaluate once bool(restricted); assign in source target order to _cfg['restricted'].
  }
  // Source: vvaharness/backends/llm/cli/env.py:89-90
  In source order: Evaluate _tls_extra.clear(); retain side effects and discard the expression result. Then Evaluate _tls_extra.update(_build_tls_env()); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cli/env.py:93-96
// Source signature: _effective_effort(effort: str | None) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _effective_effort(effort) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli/env.py:94-95
  In source order: Retain source documentation literal source_literal_94_4; it is not a model call. Then Evaluate once EffortLevel.parse(effort) if effort is not None else None; assign in source target order to parsed.
  // Source: vvaharness/backends/llm/cli/env.py:96-96
  End this invocation with parsed.value if parsed is not None else _cfg.get('effort').
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cli/env.py:99-104
// Source signature: _effort_argv(effort: str | None) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _effort_argv(effort) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli/env.py:100-101
  In source order: Retain source documentation literal source_literal_100_4; it is not a model call. Then Evaluate once _effective_effort(effort); assign in source target order to tier.
  // Source: vvaharness/backends/llm/cli/env.py:102-103
  if (the source predicate tier and _discovery._cli_capabilities()['effort'] is truthy) {
    // Source: vvaharness/backends/llm/cli/env.py:103-103
    End this invocation with ['--effort', tier].
  }
  // Source: vvaharness/backends/llm/cli/env.py:104-104
  End this invocation with [].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cli/env.py:109-112
In source order: Evaluate once {'CLAUDE_CODE_DISABLE_REFUSAL_RETRY': '1', 'CLAUDE_CODE_DISABLE_REFUSAL_FALLBACK': '1'}; assign in source target order to _NO_REFUSAL_RESEND_ENV.
// Source: vvaharness/backends/llm/cli/env.py:115-121
// Source signature: _session_pins(effort: str | None) -> dict[str, str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _session_pins(effort) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli/env.py:116-119
  In source order: Retain source documentation literal source_literal_116_4; it is not a model call. Then Evaluate once _effort_argv(effort); assign in source target order to effort_argv.
  // Source: vvaharness/backends/llm/cli/env.py:120-121
  End this invocation with {'CLAUDE_CODE_EFFORT_LEVEL': effort_argv[1] if effort_argv else '', **_NO_REFUSAL_RESEND_ENV}.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cli/env.py:124-129
// Source signature: _call_env(*, max_tokens: int | None, effort: str | None) -> dict[str, str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _call_env(max_tokens, effort) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli/env.py:125-126
  In source order: Retain source documentation literal source_literal_125_4; it is not a model call. Then Evaluate once _session_pins(effort); assign in source target order to env.
  // Source: vvaharness/backends/llm/cli/env.py:127-128
  if (the source predicate max_tokens is truthy) {
    // Source: vvaharness/backends/llm/cli/env.py:128-128
    In source order: Evaluate once str(max_tokens); assign in source target order to env['CLAUDE_CODE_MAX_OUTPUT_TOKENS'].
  }
  // Source: vvaharness/backends/llm/cli/env.py:129-129
  End this invocation with env.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.backends.harness.models import EffortLevel` at source line 20: `source_detail/vvaharness/backends/harness/models.py.sudo.md`.
- `from vvaharness.backends.llm.cli import discovery as _discovery` at source line 23: `source_detail/vvaharness/backends/llm/cli/__init__.py.sudo.md`.
- `from vvaharness.backends.llm.cli import discovery as _discovery` at source line 23: `source_detail/vvaharness/backends/llm/cli/discovery.py.sudo.md`.
- `from vvaharness.backends.llm.models import CliConfig` at source line 24: `source_detail/vvaharness/backends/llm/models.py.sudo.md`.
- `from vvaharness.backends.llm.tls import coerce_verify` at source line 27: `source_detail/vvaharness/backends/llm/tls.py.sudo.md`.
- `from vvaharness.util import logs` at source line 28: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import logs` at source line 28: `source_detail/vvaharness/util/logs.py.sudo.md`.
- `from vvaharness.util.events import Event` at source line 29: `source_detail/vvaharness/util/events.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../../prompt_representation/vvaharness/backends/llm/cli/env.py.sudo.md). Exact strings in the evidence asset support this conversion.
