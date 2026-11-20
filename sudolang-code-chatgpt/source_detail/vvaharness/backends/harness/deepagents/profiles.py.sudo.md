# vvaharness/backends/harness/deepagents/profiles.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/backends/harness/deepagents/profiles.py.evidence.json`. SHA-256: `972361ecab2354e641639def33efbe4bd57331b3ee8792615b1f3e0bd62c92ce`.

```sudo
// Source: vvaharness/backends/harness/deepagents/profiles.py:15-29
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import threading; preserve alias and import-time effects. Then Resolve source import from deepagents.profiles import HarnessProfile, register_harness_profile; preserve alias and import-time effects. Then Evaluate once ['PER_MODEL_PROFILE_KEYS', 'PROFILED_PROVIDERS', 'STAGE_PROFILE_KEYS', 'register_vvah_harness_profiles', 'stage_profile_suffix']; assign in source target order to __all__.
// Source: vvaharness/backends/harness/deepagents/profiles.py:33-56
In source order: Evaluate once source_literal_33_25; assign in source target order to _READ_BEFORE_ANSWERING. Then Evaluate once source_literal_38_23; assign in source target order to _PARALLEL_TOOL_CALLS. Then Evaluate once source_literal_43_22; assign in source target order to _REFLECT_IN_WRITING. Then Evaluate once source_literal_48_27; assign in source target order to _REFLECT_WITHOUT_WRITING. Then Evaluate once source_literal_53_30; assign in source target order to _ENUMERATE_DO_NOT_SUMMARISE.
// Source: vvaharness/backends/harness/deepagents/profiles.py:58-81
In source order: Evaluate once source_literal_58_18; assign in source target order to _BEAT_THE_CLOCK. Then Evaluate once source_literal_65_18; assign in source target order to _DO_NOT_NARRATE. Then Evaluate once source_literal_70_23.join((_READ_BEFORE_ANSWERING, _PARALLEL_TOOL_CALLS, _REFLECT_IN_WRITING, _ENUMERATE_DO_NOT_SUMMARISE)); assign in source target order to _INVESTIGATION_FLOOR. Then For PROFILED_PROVIDERS, assign ('openai',); source annotation tuple[str, ...]. Then For _PER_MODEL_SUFFIX, assign {}; source annotation dict[str, str].
// Source: vvaharness/backends/harness/deepagents/profiles.py:83-90
In source order: For PER_MODEL_PROFILE_KEYS, assign tuple(_PER_MODEL_SUFFIX); source annotation tuple[str, ...]. Then For _STAGE_SUFFIX, assign {}; source annotation dict[str, dict[str, str]]. Then For STAGE_PROFILE_KEYS, assign tuple(_STAGE_SUFFIX); source annotation tuple[str, ...]. Then Evaluate once False; assign in source target order to _REGISTERED. Then Evaluate once threading.Lock(); assign in source target order to _LOCK.
// Source: vvaharness/backends/harness/deepagents/profiles.py:93-96
// Source signature: stage_profile_suffix(stage: str | None, registry_key: str) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn stage_profile_suffix(stage, registry_key) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/profiles.py:94-95
  In source order: Retain source documentation literal source_literal_94_4; it is not a model call. Then Evaluate once _STAGE_SUFFIX.get(stage or ''); assign in source target order to by_model.
  // Source: vvaharness/backends/harness/deepagents/profiles.py:96-96
  End this invocation with by_model.get(registry_key) if by_model else None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/profiles.py:99-101
// Source signature: _stage_keyed_models() -> frozenset[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _stage_keyed_models() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/profiles.py:100-100
  In source order: Retain source documentation literal source_literal_100_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/profiles.py:101-101
  End this invocation with frozenset((key for by_model in _STAGE_SUFFIX.values() for key in by_model)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/profiles.py:104-117
// Source signature: register_vvah_harness_profiles() -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn register_vvah_harness_profiles() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/profiles.py:105-106
  In source order: Retain source documentation literal source_literal_105_4; it is not a model call. Then Bind names in module scope: _REGISTERED.
  // Source: vvaharness/backends/harness/deepagents/profiles.py:107-117
  Enter source context managers left-to-right: _LOCK {
    // Source: vvaharness/backends/harness/deepagents/profiles.py:108-109
    if (the source predicate _REGISTERED is truthy) {
      // Source: vvaharness/backends/harness/deepagents/profiles.py:109-109
      End this invocation with None.
    }
    // Source: vvaharness/backends/harness/deepagents/profiles.py:110-110
    In source order: Evaluate once HarnessProfile(system_prompt_suffix=_INVESTIGATION_FLOOR); assign in source target order to profile.
    // Source: vvaharness/backends/harness/deepagents/profiles.py:111-112
    for each key in PROFILED_PROVIDERS {
      // Source: vvaharness/backends/harness/deepagents/profiles.py:112-112
      In source order: Evaluate register_harness_profile(key, profile); retain side effects and discard the expression result.
    }
    // Source: vvaharness/backends/harness/deepagents/profiles.py:113-114
    for each key in sorted(_stage_keyed_models() - set(_PER_MODEL_SUFFIX)) {
      // Source: vvaharness/backends/harness/deepagents/profiles.py:114-114
      In source order: Evaluate register_harness_profile(key, profile); retain side effects and discard the expression result.
    }
    // Source: vvaharness/backends/harness/deepagents/profiles.py:115-116
    for each (key, suffix) in _PER_MODEL_SUFFIX.items() {
      // Source: vvaharness/backends/harness/deepagents/profiles.py:116-116
      In source order: Evaluate register_harness_profile(key, HarnessProfile(system_prompt_suffix=suffix)); retain side effects and discard the expression result.
    }
    // Source: vvaharness/backends/harness/deepagents/profiles.py:117-117
    In source order: Evaluate once True; assign in source target order to _REGISTERED.
  }
  Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

No statically resolved in-checkout import; external calls remain explicit dependency boundaries.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../../prompt_representation/vvaharness/backends/harness/deepagents/profiles.py.sudo.md). Exact strings in the evidence asset support this conversion.
