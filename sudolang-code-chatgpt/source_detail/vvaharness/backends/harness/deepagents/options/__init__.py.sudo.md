# vvaharness/backends/harness/deepagents/options/__init__.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/backends/harness/deepagents/options/__init__.py.evidence.json`. SHA-256: `946b8906fe723b345e10a8f7bcbdb4e7bed195df71acd587c03906be8e1322c2`.

```sudo
// Source: vvaharness/backends/harness/deepagents/options/__init__.py:15-22
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from deepagents import register_provider_profile; preserve alias and import-time effects. Then Resolve source import from deepagents.profiles.provider.provider_profiles import ProviderProfile; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.deepagents.limits import MODEL_TIMEOUT_SECONDS; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/deepagents/options/__init__.py:23-49
In source order: Resolve source import from vvaharness.backends.harness.deepagents.options.model_building import RESPONSES_INCLUDE_ENCRYPTED_REASONING, build_model, build_model_cached; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.deepagents.options.oneshot import build_oneshot_options; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.deepagents.options.streaming import build_streaming_agent, release_session, resumable; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.deepagents.options.subagents import get_subagent_specs; preserve alias and import-time effects. Then Evaluate register_provider_profile('openai', ProviderProfile(init_kwargs={'use_responses_api': True, 'store': False, 'include': list(RESPONSES_INCLUDE_ENCRYPTED_REASONING), 'timeout': MODEL_TIMEOUT_SECONDS})); retain side effects and discard the expression result.
// Source: vvaharness/backends/harness/deepagents/options/__init__.py:51-59
In source order: Evaluate once ['build_model', 'build_model_cached', 'build_oneshot_options', 'build_streaming_agent', 'release_session', 'resumable', 'get_subagent_specs']; assign in source target order to __all__.
```

## Local import links

- `from vvaharness.backends.harness.deepagents.limits import MODEL_TIMEOUT_SECONDS` at source line 22: `source_detail/vvaharness/backends/harness/deepagents/limits.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.options.model_building import RESPONSES_INCLUDE_ENCRYPTED_REASONING, build_model, build_model_cached` at source line 23: `source_detail/vvaharness/backends/harness/deepagents/options/model_building.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.options.oneshot import build_oneshot_options` at source line 28: `source_detail/vvaharness/backends/harness/deepagents/options/oneshot.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.options.streaming import build_streaming_agent, release_session, resumable` at source line 29: `source_detail/vvaharness/backends/harness/deepagents/options/streaming.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.options.subagents import get_subagent_specs` at source line 34: `source_detail/vvaharness/backends/harness/deepagents/options/subagents.py.sudo.md`.
