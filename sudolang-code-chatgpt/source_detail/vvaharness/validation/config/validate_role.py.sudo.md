# vvaharness/validation/config/validate_role.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/validation/config/validate_role.py.evidence.json`. SHA-256: `9e6362f7d176ff7869e282cef4c652bf760df4c8c3e81845ec6613e3247ee4db`.

```sudo
// Source: vvaharness/validation/config/validate_role.py:15-22
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from typing import NamedTuple; preserve alias and import-time effects. Then Resolve source import from vvaharness.config import Config as HarnessConfig; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.warn_once import warn_once; preserve alias and import-time effects.
// Source: vvaharness/validation/config/validate_role.py:23-32
In source order: Resolve source import from vvaharness.validation.constants.artifacts import BACKEND_DEEPAGENTS, BACKEND_OPENAI, PROVIDER_OPENAI; preserve alias and import-time effects. Then Evaluate once ['BackendRoute', 'normalize_validate_backend', 'validate_model_spec']; assign in source target order to __all__. Then For _WARNED_VIA_REWRITE, assign set(); source annotation set[str].
// Source: vvaharness/validation/config/validate_role.py:35-39
interface BackendRoute {
  Describe the source Python type, preserving its base/metaclass expression order: NamedTuple.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/validation/config/validate_role.py:36-39
  In source order: Retain source documentation literal source_literal_36_4; it is not a model call. Then For via, declare without assigning a value; source annotation str. Then For provider, declare without assigning a value; source annotation str | None.
}
// Source: vvaharness/validation/config/validate_role.py:42-50
// Source signature: validate_model_spec(cfg: HarnessConfig) -> object | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn validate_model_spec(cfg) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/config/validate_role.py:43-44
  In source order: Retain source documentation literal source_literal_43_4; it is not a model call. Then Evaluate once getattr(cfg, 'models', None); assign in source target order to models.
  // Source: vvaharness/validation/config/validate_role.py:45-46
  if (the source predicate models is None is truthy) {
    // Source: vvaharness/validation/config/validate_role.py:46-46
    End this invocation with None.
  }
  // Source: vvaharness/validation/config/validate_role.py:47-47
  In source order: Evaluate once getattr(models, 'validate', None); assign in source target order to validate.
  // Source: vvaharness/validation/config/validate_role.py:48-49
  if (the source predicate validate is None is truthy) {
    // Source: vvaharness/validation/config/validate_role.py:49-49
    End this invocation with None.
  }
  // Source: vvaharness/validation/config/validate_role.py:50-50
  End this invocation with getattr(validate, 'orchestrator', None).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/config/validate_role.py:53-63
// Source signature: normalize_validate_backend(via: str, provider: str | None) -> BackendRoute
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn normalize_validate_backend(via, provider) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/config/validate_role.py:54-54
  In source order: Retain source documentation literal source_literal_54_4; it is not a model call.
  // Source: vvaharness/validation/config/validate_role.py:55-56
  if (the source predicate via != BACKEND_OPENAI is truthy) {
    // Source: vvaharness/validation/config/validate_role.py:56-56
    End this invocation with BackendRoute(via, provider).
  }
  // Source: vvaharness/validation/config/validate_role.py:57-62
  In source order: Evaluate warn_once(_WARNED_VIA_REWRITE, 'validate-via-openai-rewritten', source_literal_59_8); retain side effects and discard the expression result.
  // Source: vvaharness/validation/config/validate_role.py:63-63
  End this invocation with BackendRoute(BACKEND_DEEPAGENTS, provider or PROVIDER_OPENAI).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.config import Config as HarnessConfig` at source line 21: `source_detail/vvaharness/config/__init__.py.sudo.md`.
- `from vvaharness.util.warn_once import warn_once` at source line 22: `source_detail/vvaharness/util/warn_once.py.sudo.md`.
- `from vvaharness.validation.constants.artifacts import BACKEND_DEEPAGENTS, BACKEND_OPENAI, PROVIDER_OPENAI` at source line 23: `source_detail/vvaharness/validation/constants/artifacts.py.sudo.md`.
