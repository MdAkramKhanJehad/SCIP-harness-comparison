# vvaharness/validation/cli/_model.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/validation/cli/_model.py.evidence.json`. SHA-256: `b7ca09e020d6f0869a7cd8217c48b4f1b70b9e4d69311b4ad8176cecbe912210`.

```sudo
// Source: vvaharness/validation/cli/_model.py:15-22
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from typing import NamedTuple; preserve alias and import-time effects. Then Resolve source import from vvaharness import config as harness_config; preserve alias and import-time effects.
// Source: vvaharness/validation/cli/_model.py:23-27
In source order: Resolve source import from vvaharness.backends.harness.provider_routing import routes_to_anthropic; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm import registry as llm; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm.deepagents import markers_on; preserve alias and import-time effects. Then Resolve source import from vvaharness.config import Config as HarnessConfig; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import console; preserve alias and import-time effects.
// Source: vvaharness/validation/cli/_model.py:28-39
In source order: Resolve source import from vvaharness.validation.cli._parser import _tunable_overrides; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.config.overrides import ValidateOverrides; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.config.validate_role import normalize_validate_backend, validate_model_spec; preserve alias and import-time effects. Then For _PERSONA_FIELDS, assign {'security_architect': 'security_architect_model', 'penetration_tester': 'penetration_tester_model', 'cross_repo_analyzer': 'cross_repo_analyzer_model'}; source annotation dict[str, str].
// Source: vvaharness/validation/cli/_model.py:42-46
interface LoadedValidateSpec {
  Describe the source Python type, preserving its base/metaclass expression order: NamedTuple.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/validation/cli/_model.py:43-46
  In source order: Retain source documentation literal source_literal_43_4; it is not a model call. Then For config, declare without assigning a value; source annotation HarnessConfig. Then For spec, declare without assigning a value; source annotation object.
}
// Source: vvaharness/validation/cli/_model.py:49-53
interface PersonaModelResolution {
  Describe the source Python type, preserving its base/metaclass expression order: NamedTuple.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/validation/cli/_model.py:50-53
  In source order: Retain source documentation literal source_literal_50_4; it is not a model call. Then For model_id, declare without assigning a value; source annotation str. Then For via, declare without assigning a value; source annotation str.
}
// Source: vvaharness/validation/cli/_model.py:56-60
interface ModelEnvResult {
  Describe the source Python type, preserving its base/metaclass expression order: NamedTuple.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/validation/cli/_model.py:57-60
  In source order: Retain source documentation literal source_literal_57_4; it is not a model call. Then For exit_code, declare without assigning a value; source annotation int. Then For overrides, declare without assigning a value; source annotation ValidateOverrides.
}
// Source: vvaharness/validation/cli/_model.py:63-89
// Source signature: _check_persona_vendors(overrides: ValidateOverrides) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _check_persona_vendors(overrides) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/cli/_model.py:64-69
  In source order: Retain source documentation literal source_literal_64_4; it is not a model call. Then Evaluate once overrides.get('provider'); assign in source target order to provider. Then Evaluate once routes_to_anthropic(str(overrides.get('model') or ''), provider if isinstance(provider, str) and provider else None); assign in source target order to panel_anthropic.
  // Source: vvaharness/validation/cli/_model.py:70-88
  for each (short_name, field) in _PERSONA_FIELDS.items() {
    // Source: vvaharness/validation/cli/_model.py:71-71
    In source order: Evaluate once overrides.get(field); assign in source target order to model.
    // Source: vvaharness/validation/cli/_model.py:72-73
    if (the source predicate not isinstance(model, str) or not model is truthy) {
      // Source: vvaharness/validation/cli/_model.py:73-73
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/validation/cli/_model.py:75-76
    if (the source predicate routes_to_anthropic(model, None) == panel_anthropic is truthy) {
      // Source: vvaharness/validation/cli/_model.py:76-76
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/validation/cli/_model.py:77-80
    In source order: Evaluate once ('Anthropic', 'an Anthropic') if panel_anthropic else ('an OpenAI-compatible endpoint', 'an OpenAI-compatible'); assign in source target order to (panel, wanted).
    // Source: vvaharness/validation/cli/_model.py:81-88
    End this invocation with source_template_82_12.
  }
  // Source: vvaharness/validation/cli/_model.py:89-89
  End this invocation with None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/cli/_model.py:92-106
// Source signature: _load_validated_spec(config_path: str) -> LoadedValidateSpec | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _load_validated_spec(config_path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/cli/_model.py:93-93
  In source order: Retain source documentation literal source_literal_93_4; it is not a model call.
  // Source: vvaharness/validation/cli/_model.py:94-96
  if (the source predicate not Path(config_path).exists() is truthy) {
    // Source: vvaharness/validation/cli/_model.py:95-95
    In source order: Evaluate console.write(source_template_95_22); retain side effects and discard the expression result.
    // Source: vvaharness/validation/cli/_model.py:96-96
    End this invocation with None.
  }
  // Source: vvaharness/validation/cli/_model.py:97-101
  Perform the following protected operations {
    // Source: vvaharness/validation/cli/_model.py:98-98
    In source order: Evaluate once harness_config.load(config_path); assign in source target order to cfg.
  }
  // Source: vvaharness/validation/cli/_model.py:99-101
  On the first matching source exception harness_config.ConfigPolicyError as e, in handler order {
    // Source: vvaharness/validation/cli/_model.py:100-100
    In source order: Evaluate console.write(source_template_100_22); retain side effects and discard the expression result.
    // Source: vvaharness/validation/cli/_model.py:101-101
    End this invocation with None.
  }
  // Source: vvaharness/validation/cli/_model.py:102-102
  In source order: Evaluate once validate_model_spec(cfg); assign in source target order to spec.
  // Source: vvaharness/validation/cli/_model.py:103-105
  if (the source predicate spec is None is truthy) {
    // Source: vvaharness/validation/cli/_model.py:104-104
    In source order: Evaluate console.write('validate: config defines no models.validate role'); retain side effects and discard the expression result.
    // Source: vvaharness/validation/cli/_model.py:105-105
    End this invocation with None.
  }
  // Source: vvaharness/validation/cli/_model.py:106-106
  End this invocation with LoadedValidateSpec(cfg, spec).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/cli/_model.py:109-111
// Source signature: _declares_route(spec: object) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _declares_route(spec) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/cli/_model.py:110-110
  In source order: Retain source documentation literal source_literal_110_4; it is not a model call.
  // Source: vvaharness/validation/cli/_model.py:111-111
  End this invocation with bool(getattr(spec, 'via', None) or getattr(spec, 'provider', None)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/cli/_model.py:114-123
// Source signature: _warn_ignored_persona_routes(declared: list[str], via: str, provider: str | None) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _warn_ignored_persona_routes(declared, via, provider) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/cli/_model.py:115-115
  In source order: Retain source documentation literal source_literal_115_4; it is not a model call.
  // Source: vvaharness/validation/cli/_model.py:116-117
  if (the source predicate not declared is truthy) {
    // Source: vvaharness/validation/cli/_model.py:117-117
    End this invocation with None.
  }
  // Source: vvaharness/validation/cli/_model.py:118-123
  In source order: Evaluate once source_template_118_12 if provider else via; assign in source target order to route. Then Evaluate console.write(source_template_120_8); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/cli/_model.py:126-134
// Source signature: _persona_spec_resolved(spec: object) -> PersonaModelResolution | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _persona_spec_resolved(spec) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/cli/_model.py:127-127
  In source order: Retain source documentation literal source_literal_127_4; it is not a model call.
  // Source: vvaharness/validation/cli/_model.py:128-129
  if (the source predicate spec is None is truthy) {
    // Source: vvaharness/validation/cli/_model.py:129-129
    End this invocation with None.
  }
  // Source: vvaharness/validation/cli/_model.py:130-133
  Perform the following protected operations {
    // Source: vvaharness/validation/cli/_model.py:131-131
    In source order: Evaluate once llm.resolve(spec); assign in source target order to (model_id, via, _).
  }
  // Source: vvaharness/validation/cli/_model.py:132-133
  On the first matching source exception (ValueError, AttributeError, KeyError, TypeError), in handler order {
    // Source: vvaharness/validation/cli/_model.py:133-133
    End this invocation with None.
  }
  // Source: vvaharness/validation/cli/_model.py:134-134
  End this invocation with PersonaModelResolution(model_id, via or '') if model_id else None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/cli/_model.py:137-174
// Source signature: _apply_model_env(config_path: str) -> ModelEnvResult
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _apply_model_env(config_path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/cli/_model.py:138-139
  In source order: Retain source documentation literal source_literal_138_4; it is not a model call. Then Evaluate once _load_validated_spec(config_path); assign in source target order to loaded.
  // Source: vvaharness/validation/cli/_model.py:140-141
  if (the source predicate loaded is None is truthy) {
    // Source: vvaharness/validation/cli/_model.py:141-141
    End this invocation with ModelEnvResult(2, ValidateOverrides()).
  }
  // Source: vvaharness/validation/cli/_model.py:142-147
  In source order: Evaluate once loaded; assign in source target order to (cfg, spec). Then Evaluate once llm.resolve(spec); assign in source target order to (model_id, via, _). Then Evaluate once normalize_validate_backend(via or '', getattr(spec, 'provider', None)); assign in source target order to (via, provider). Then For overrides, assign _tunable_overrides(cfg); source annotation ValidateOverrides. Then Evaluate once model_id; assign in source target order to overrides['model'].
  // Source: vvaharness/validation/cli/_model.py:148-154
  In source order: Evaluate once via; assign in source target order to overrides['via']. Then Evaluate once provider; assign in source target order to overrides['provider']. Then Evaluate once llm.use_responses_api_of(spec); assign in source target order to overrides['use_responses_api']. Then Evaluate once getattr(cfg, 'models', None); assign in source target order to models. Then Evaluate once getattr(models, 'validate', None) if models is not None else None; assign in source target order to validate.
  // Source: vvaharness/validation/cli/_model.py:155-163
  if (the source predicate validate is not None is truthy) {
    // Source: vvaharness/validation/cli/_model.py:156-159
    for each (short_name, field) in _PERSONA_FIELDS.items() {
      // Source: vvaharness/validation/cli/_model.py:157-157
      In source order: Evaluate once _persona_spec_resolved(getattr(validate, short_name, None)); assign in source target order to resolved.
      // Source: vvaharness/validation/cli/_model.py:158-159
      if (the source predicate resolved is not None is truthy) {
        // Source: vvaharness/validation/cli/_model.py:159-159
        In source order: Evaluate once resolved.model_id; assign in source target order to overrides[field].
      }
    }
    // Source: vvaharness/validation/cli/_model.py:161-163
    In source order: Evaluate once [name for name in _PERSONA_FIELDS if _declares_route(getattr(validate, name, None))]; assign in source target order to declared. Then Evaluate _warn_ignored_persona_routes(declared, via, provider); retain side effects and discard the expression result.
  }
  // Source: vvaharness/validation/cli/_model.py:166-167
  In source order: Evaluate once getattr(cfg, 'step_validate', None); assign in source target order to block. Then Evaluate once getattr(block, 'allowed_tools', None) if block is not None else None; assign in source target order to tools.
  // Source: vvaharness/validation/cli/_model.py:168-169
  if (the source predicate isinstance(tools, list) and tools is truthy) {
    // Source: vvaharness/validation/cli/_model.py:169-169
    In source order: Evaluate once ','.join((str(t) for t in tools)); assign in source target order to overrides['validate_tools'].
  }
  // Source: vvaharness/validation/cli/_model.py:172-172
  In source order: Evaluate once markers_on(getattr(cfg, 'sdk', None)); assign in source target order to overrides['cache_markers'].
  // Source: vvaharness/validation/cli/_model.py:174-174
  End this invocation with ModelEnvResult(0, overrides).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness import config as harness_config` at source line 22: `source_detail/vvaharness/__init__.py.sudo.md`.
- `from vvaharness import config as harness_config` at source line 22: `source_detail/vvaharness/config/__init__.py.sudo.md`.
- `from vvaharness.backends.harness.provider_routing import routes_to_anthropic` at source line 23: `source_detail/vvaharness/backends/harness/provider_routing.py.sudo.md`.
- `from vvaharness.backends.llm import registry as llm` at source line 24: `source_detail/vvaharness/backends/llm/__init__.py.sudo.md`.
- `from vvaharness.backends.llm import registry as llm` at source line 24: `source_detail/vvaharness/backends/llm/registry.py.sudo.md`.
- `from vvaharness.backends.llm.deepagents import markers_on` at source line 25: `source_detail/vvaharness/backends/llm/deepagents.py.sudo.md`.
- `from vvaharness.config import Config as HarnessConfig` at source line 26: `source_detail/vvaharness/config/__init__.py.sudo.md`.
- `from vvaharness.util import console` at source line 27: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import console` at source line 27: `source_detail/vvaharness/util/console.py.sudo.md`.
- `from vvaharness.validation.cli._parser import _tunable_overrides` at source line 28: `source_detail/vvaharness/validation/cli/_parser.py.sudo.md`.
- `from vvaharness.validation.config.overrides import ValidateOverrides` at source line 29: `source_detail/vvaharness/validation/config/overrides.py.sudo.md`.
- `from vvaharness.validation.config.validate_role import normalize_validate_backend, validate_model_spec` at source line 30: `source_detail/vvaharness/validation/config/validate_role.py.sudo.md`.
