# vvaharness/backends/harness/provider_routing.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/backends/harness/provider_routing.py.evidence.json`. SHA-256: `86778550716f1e8ecafa84b5103b694b5e911afcb93e3fbc01f3e01ea85337b0`.

```sudo
// Source: vvaharness/backends/harness/provider_routing.py:15-30
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from typing import Final; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.models import Provider; preserve alias and import-time effects. Then Evaluate once ['TRANSPORT_CHAT_COMPLETIONS', 'TRANSPORT_RESPONSES', 'credential_env_overrides', 'routes_to_anthropic']; assign in source target order to __all__.
// Source: vvaharness/backends/harness/provider_routing.py:33-34
In source order: For TRANSPORT_RESPONSES, assign 'responses'; source annotation Final. Then For TRANSPORT_CHAT_COMPLETIONS, assign 'chat_completions'; source annotation Final.
// Source: vvaharness/backends/harness/provider_routing.py:37-42
// Source signature: routes_to_anthropic(model_id: str, provider: str | None) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn routes_to_anthropic(model_id, provider) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/provider_routing.py:38-38
  In source order: Retain source documentation literal source_literal_38_4; it is not a model call.
  // Source: vvaharness/backends/harness/provider_routing.py:40-41
  if (the source predicate provider is truthy) {
    // Source: vvaharness/backends/harness/provider_routing.py:41-41
    End this invocation with provider == Provider.ANTHROPIC.
  }
  // Source: vvaharness/backends/harness/provider_routing.py:42-42
  End this invocation with 'claude' in model_id.lower().
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/provider_routing.py:45-60
// Source signature: credential_env_overrides(model_id: str, provider: str | None, *, sdk_cfg: object, openai_cfg: object) -> dict[str, str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn credential_env_overrides(model_id, provider, sdk_cfg, openai_cfg) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/provider_routing.py:48-52
  In source order: Retain source documentation literal source_literal_48_4; it is not a model call. Then Evaluate once routes_to_anthropic(model_id, provider); assign in source target order to is_anthropic. Then Evaluate once sdk_cfg if is_anthropic else openai_cfg; assign in source target order to block. Then Evaluate once 'ANTHROPIC' if is_anthropic else 'OPENAI'; assign in source target order to prefix. Then For overrides, assign {}; source annotation dict[str, str].
  // Source: vvaharness/backends/harness/provider_routing.py:53-54
  In source order: Evaluate once getattr(block, 'api_key', None); assign in source target order to api_key. Then Evaluate once getattr(block, 'base_url', None); assign in source target order to base_url.
  // Source: vvaharness/backends/harness/provider_routing.py:55-57
  if (the source predicate api_key is truthy) {
    // Source: vvaharness/backends/harness/provider_routing.py:57-57
    In source order: Evaluate once api_key.strip(); assign in source target order to overrides[f'{prefix}_API_KEY'].
  }
  // Source: vvaharness/backends/harness/provider_routing.py:58-59
  if (the source predicate base_url is truthy) {
    // Source: vvaharness/backends/harness/provider_routing.py:59-59
    In source order: Evaluate once base_url.strip(); assign in source target order to overrides[f'{prefix}_BASE_URL'].
  }
  // Source: vvaharness/backends/harness/provider_routing.py:60-60
  End this invocation with overrides.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.backends.harness.models import Provider` at source line 23: `source_detail/vvaharness/backends/harness/models.py.sudo.md`.
