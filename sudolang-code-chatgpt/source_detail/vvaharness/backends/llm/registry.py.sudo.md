# vvaharness/backends/llm/registry.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/backends/llm/registry.py.evidence.json`. SHA-256: `29954674cd1cf9ef0cf9c8a06afba3ab03218949c6098b48ac84b7b7358ec393`.

```sudo
// Source: vvaharness/backends/llm/registry.py:15-22
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from collections.abc import Mapping; preserve alias and import-time effects. Then Resolve source import from importlib import import_module; preserve alias and import-time effects. Then Resolve source import from typing import Any, Final; preserve alias and import-time effects.
// Source: vvaharness/backends/llm/registry.py:24-33
In source order: Resolve source import from vvaharness.backends.llm.cli import parse_json_response; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm.models import LlmBackend, ModelExtras, ModulePath, ResolvedModel; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import logs; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.events import Event; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.response_quality import check_response_quality; preserve alias and import-time effects.
// Source: vvaharness/backends/llm/registry.py:34-52
In source order: Resolve source import from vvaharness.util.scan_progress import get_active_tracker; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.tokens import TOKENS; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.warn_once import warn_once; preserve alias and import-time effects. Then Evaluate once logs.get_logger(__name__); assign in source target order to log. Then Evaluate once frozenset({'remediate', 'validate', 'preprocess', 'autoexclude', 'threatmodel', 'decompose', 'deepdive', 'verify', 'dedup', 'chain', 'graph_annotate', 'exploit_verification.classify', 'exploit_verification.mapper', 'exploit_verification.judge', 'exploit_verification.attacker'}); assign in source target order to DEEPAGENTS_ROLES.
// Source: vvaharness/backends/llm/registry.py:55-55
In source order: Evaluate once frozenset({'remediate', 'validate'}); assign in source target order to POST_SCAN_ROLES.
// Source: vvaharness/backends/llm/registry.py:58-61
// Source signature: provider_of(model_cfg: object) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn provider_of(model_cfg) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/registry.py:59-60
  In source order: Retain source documentation literal source_literal_59_4; it is not a model call. Then Evaluate once getattr(model_cfg, 'provider', None); assign in source target order to provider.
  // Source: vvaharness/backends/llm/registry.py:61-61
  End this invocation with provider if isinstance(provider, str) else None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/registry.py:64-67
// Source signature: use_responses_api_of(model_cfg: object) -> bool | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn use_responses_api_of(model_cfg) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/registry.py:65-66
  In source order: Retain source documentation literal source_literal_65_4; it is not a model call. Then Evaluate once getattr(model_cfg, 'use_responses_api', None); assign in source target order to value.
  // Source: vvaharness/backends/llm/registry.py:67-67
  End this invocation with value if isinstance(value, bool) else None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/registry.py:70-74
// Source signature: output_cap_of(model_cfg: object) -> int | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn output_cap_of(model_cfg) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/registry.py:71-73
  In source order: Retain source documentation literal source_literal_71_4; it is not a model call. Then Evaluate once getattr(model_cfg, 'max_tokens', None); assign in source target order to value.
  // Source: vvaharness/backends/llm/registry.py:74-74
  End this invocation with int(value) if isinstance(value, (int, float)) and value > 0 else None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/registry.py:77-87
// Source signature: clamp_output_tokens(requested: int, model_cfg: object, *, tag: str | None=None) -> int
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn clamp_output_tokens(requested, model_cfg, tag) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/registry.py:78-80
  In source order: Retain source documentation literal source_literal_78_4; it is not a model call. Then Evaluate once output_cap_of(model_cfg); assign in source target order to cap.
  // Source: vvaharness/backends/llm/registry.py:81-82
  if (the source predicate cap is None or requested <= cap is truthy) {
    // Source: vvaharness/backends/llm/registry.py:82-82
    End this invocation with requested.
  }
  // Source: vvaharness/backends/llm/registry.py:83-86
  In source order: Evaluate once getattr(model_cfg, 'id', None) or str(model_cfg); assign in source target order to model_id. Then Evaluate once tag.split()[0] if tag else ''; assign in source target order to stage. Then Evaluate log.warning(Event.OUTPUT_TOKENS_CLAMPED, stage=stage or 'llm', model=model_id, requested=requested, cap=cap); retain side effects and discard the expression result.
  // Source: vvaharness/backends/llm/registry.py:87-87
  End this invocation with cap.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/registry.py:91-94
In source order: For KNOWN_MODEL_NODE_KEYS, assign frozenset({'id', 'via', 'provider', 'temperature', 'thinking_budget', 'betas', 'use_responses_api', 'max_tokens'}); source annotation Final[frozenset[str]].
// Source: vvaharness/backends/llm/registry.py:97-102
// Source signature: unrecognized_model_keys(model_cfg: object) -> tuple[str, ...]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn unrecognized_model_keys(model_cfg) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/registry.py:98-99
  In source order: Retain source documentation literal source_literal_98_4; it is not a model call. Then Evaluate once getattr(model_cfg, '_data', None); assign in source target order to data.
  // Source: vvaharness/backends/llm/registry.py:100-101
  if (the source predicate not isinstance(data, dict) is truthy) {
    // Source: vvaharness/backends/llm/registry.py:101-101
    End this invocation with ().
  }
  // Source: vvaharness/backends/llm/registry.py:102-102
  End this invocation with tuple(sorted((str(k) for k in data if str(k) not in KNOWN_MODEL_NODE_KEYS))).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/registry.py:105-126
// Source signature: resolve(model_cfg: Any) -> ResolvedModel
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn resolve(model_cfg) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/registry.py:106-106
  In source order: Retain source documentation literal source_literal_106_4; it is not a model call.
  // Source: vvaharness/backends/llm/registry.py:107-108
  if (the source predicate isinstance(model_cfg, str) is truthy) {
    // Source: vvaharness/backends/llm/registry.py:108-108
    End this invocation with ResolvedModel(model_cfg, DEFAULT_LLM_VIA, ModelExtras()).
  }
  // Source: vvaharness/backends/llm/registry.py:110-110
  In source order: Evaluate once getattr(model_cfg, 'id', None); assign in source target order to model_id.
  // Source: vvaharness/backends/llm/registry.py:111-114
  if (the source predicate model_id is None is truthy) {
    // Source: vvaharness/backends/llm/registry.py:112-114
    Raise ValueError(source_template_113_12).
  }
  // Source: vvaharness/backends/llm/registry.py:115-117
  In source order: Evaluate once getattr(model_cfg, 'via', None) or DEFAULT_LLM_VIA; assign in source target order to via. Then Evaluate once ModelExtras(); assign in source target order to extras. Then Evaluate once getattr(model_cfg, 'temperature', None); assign in source target order to temperature.
  // Source: vvaharness/backends/llm/registry.py:118-119
  if (the source predicate temperature is not None is truthy) {
    // Source: vvaharness/backends/llm/registry.py:119-119
    In source order: Evaluate once float(temperature); assign in source target order to extras['temperature'].
  }
  // Source: vvaharness/backends/llm/registry.py:120-120
  In source order: Evaluate once getattr(model_cfg, 'thinking_budget', None); assign in source target order to thinking_budget.
  // Source: vvaharness/backends/llm/registry.py:121-122
  if (the source predicate thinking_budget is truthy) {
    // Source: vvaharness/backends/llm/registry.py:122-122
    In source order: Evaluate once int(thinking_budget); assign in source target order to extras['thinking_budget'].
  }
  // Source: vvaharness/backends/llm/registry.py:123-123
  In source order: Evaluate once getattr(model_cfg, 'betas', None); assign in source target order to betas.
  // Source: vvaharness/backends/llm/registry.py:124-125
  if (the source predicate betas is truthy) {
    // Source: vvaharness/backends/llm/registry.py:125-125
    In source order: Evaluate once list(betas); assign in source target order to extras['betas'].
  }
  // Source: vvaharness/backends/llm/registry.py:126-126
  End this invocation with ResolvedModel(model_id, via, extras).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/registry.py:130-137
In source order: For _BACKENDS, assign {'cli': ModulePath('vvaharness.backends.llm.cli'), 'sdk': ModulePath('vvaharness.backends.llm.sdk'), 'openai': ModulePath('vvaharness.backends.llm.openai')}; source annotation Final[Mapping[str, ModulePath]]. Then For DEFAULT_LLM_VIA, assign 'cli'; source annotation Final.
// Source: vvaharness/backends/llm/registry.py:140-142
// Source signature: available() -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn available() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/registry.py:141-141
  In source order: Retain source documentation literal source_literal_141_4; it is not a model call.
  // Source: vvaharness/backends/llm/registry.py:142-142
  End this invocation with sorted(_BACKENDS).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/registry.py:145-147
// Source signature: targets() -> Mapping[str, ModulePath]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn targets() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/registry.py:146-146
  In source order: Retain source documentation literal source_literal_146_4; it is not a model call.
  // Source: vvaharness/backends/llm/registry.py:147-147
  End this invocation with _BACKENDS.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/registry.py:150-159
// Source signature: get_backend(via: str, model_id: str) -> LlmBackend
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn get_backend(via, model_id) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/registry.py:151-152
  In source order: Retain source documentation literal source_literal_151_4; it is not a model call. Then Evaluate once _BACKENDS.get(via); assign in source target order to path.
  // Source: vvaharness/backends/llm/registry.py:153-154
  if (the source predicate path is None is truthy) {
    // Source: vvaharness/backends/llm/registry.py:154-154
    Raise ValueError(source_template_154_25).
  }
  // Source: vvaharness/backends/llm/registry.py:155-155
  In source order: Evaluate once import_module(path); assign in source target order to module.
  // Source: vvaharness/backends/llm/registry.py:156-158
  if (the source predicate not isinstance(module, LlmBackend) is truthy) {
    // Source: vvaharness/backends/llm/registry.py:157-157
    In source order: Evaluate once source_template_157_14; assign in source target order to msg.
    // Source: vvaharness/backends/llm/registry.py:158-158
    Raise TypeError(msg).
  }
  // Source: vvaharness/backends/llm/registry.py:159-159
  End this invocation with module.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/registry.py:162-169
// Source signature: _flatten_blocks(user_prompt: str | list[dict]) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _flatten_blocks(user_prompt) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/registry.py:163-163
  In source order: Retain source documentation literal source_literal_163_4; it is not a model call.
  // Source: vvaharness/backends/llm/registry.py:164-165
  if (the source predicate isinstance(user_prompt, str) is truthy) {
    // Source: vvaharness/backends/llm/registry.py:165-165
    End this invocation with user_prompt.
  }
  // Source: vvaharness/backends/llm/registry.py:166-169
  End this invocation with source_literal_166_11.join((str(b.get('text', '')) for b in user_prompt if isinstance(b, dict) and b.get('type') == 'text')).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/registry.py:173-176
In source order: For _WARNED_CLI_DROPPED, assign set(); source annotation set[str]. Then For _CLI_UNSUPPORTED_KEYS, assign ('temperature', 'thinking_budget', 'betas'); source annotation Final.
// Source: vvaharness/backends/llm/registry.py:179-191
// Source signature: warn_cli_dropped_knobs(model_id: str, extras: ModelExtras) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn warn_cli_dropped_knobs(model_id, extras) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/registry.py:180-182
  In source order: Retain source documentation literal source_literal_180_4; it is not a model call. Then Evaluate once [k for k in _CLI_UNSUPPORTED_KEYS if k in extras]; assign in source target order to dropped.
  // Source: vvaharness/backends/llm/registry.py:183-184
  if (the source predicate not dropped is truthy) {
    // Source: vvaharness/backends/llm/registry.py:184-184
    End this invocation with None.
  }
  // Source: vvaharness/backends/llm/registry.py:185-191
  In source order: Evaluate warn_once(_WARNED_CLI_DROPPED, source_template_186_29, source_template_187_8); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/registry.py:194-205
// Source signature: _fold_for_cli(user_prompt: str | list[dict], kw: dict[str, Any]) -> str | list[dict]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _fold_for_cli(user_prompt, kw) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/registry.py:195-200
  In source order: Retain source documentation literal source_literal_195_4; it is not a model call. Then Evaluate kw.pop('temperature', None); retain side effects and discard the expression result. Then Evaluate kw.pop('thinking_budget', None); retain side effects and discard the expression result. Then Evaluate kw.pop('betas', None); retain side effects and discard the expression result. Then Evaluate once kw.pop('cache_prefix', None); assign in source target order to cache_prefix.
  // Source: vvaharness/backends/llm/registry.py:201-202
  if (the source predicate not cache_prefix is truthy) {
    // Source: vvaharness/backends/llm/registry.py:202-202
    End this invocation with user_prompt.
  }
  // Source: vvaharness/backends/llm/registry.py:203-204
  if (the source predicate isinstance(user_prompt, list) is truthy) {
    // Source: vvaharness/backends/llm/registry.py:204-204
    End this invocation with [{'type': 'text', 'text': cache_prefix}, *user_prompt].
  }
  // Source: vvaharness/backends/llm/registry.py:205-205
  End this invocation with cache_prefix + user_prompt.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/registry.py:208-236
// Source signature: prompt(user_prompt: str | list[dict], *, model: Any, **kw: Any) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn prompt(user_prompt, model, kw) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/registry.py:209-211
  In source order: Retain source documentation literal source_literal_209_4; it is not a model call. Then Evaluate once resolve(model); assign in source target order to (model_id, via, extras). Then Evaluate once get_backend(via, model_id); assign in source target order to backend.
  // Source: vvaharness/backends/llm/registry.py:212-213
  if (the source predicate kw.get('max_tokens') is not None is truthy) {
    // Source: vvaharness/backends/llm/registry.py:213-213
    In source order: Evaluate once clamp_output_tokens(int(kw['max_tokens']), model, tag=kw.get('tag')); assign in source target order to kw['max_tokens'].
  }
  // Source: vvaharness/backends/llm/registry.py:214-216
  if (the source predicate via == 'openai' is truthy) {
    // Source: vvaharness/backends/llm/registry.py:216-216
    In source order: Evaluate once output_cap_of(model); assign in source target order to kw['output_cap'].
  }
  // Source: vvaharness/backends/llm/registry.py:217-217
  In source order: Evaluate once get_active_tracker(); assign in source target order to tracker.
  // Source: vvaharness/backends/llm/registry.py:218-229
  if (the source predicate tracker is not None is truthy) {
    // Source: vvaharness/backends/llm/registry.py:220-229
    In source order: Evaluate once kw.get('cache_prefix') or ''; assign in source target order to _prefix. Then Evaluate once _flatten_blocks(user_prompt); assign in source target order to _body. Then Evaluate tracker.llm_payload(phase=TOKENS.current_phase(), backend=via, model_id=model_id, tag=str(kw.get('tag', '') or ''), user_prompt=_prefix + _body if _prefix else _body, system_prompt=str(kw.get('system_prompt', '') or '')); retain side effects and discard the expression result.
  }
  // Source: vvaharness/backends/llm/registry.py:230-235
  if (the source predicate via == DEFAULT_LLM_VIA is truthy) {
    // Source: vvaharness/backends/llm/registry.py:231-232
    In source order: Evaluate warn_cli_dropped_knobs(model_id, extras); retain side effects and discard the expression result. Then Evaluate once _fold_for_cli(user_prompt, kw); assign in source target order to user_prompt.
  }
  else {
    // Source: vvaharness/backends/llm/registry.py:234-235
    for each (k, v) in extras.items() {
      // Source: vvaharness/backends/llm/registry.py:235-235
      In source order: Evaluate kw.setdefault(k, v); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/backends/llm/registry.py:236-236
  End this invocation with backend.prompt(user_prompt, model=model_id, **kw).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/registry.py:239-265
// Source signature: agentic(user_prompt: str, *, model: Any, **kw) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn agentic(user_prompt, model, kw) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/registry.py:240-243
  In source order: Retain source documentation literal source_literal_240_4; it is not a model call. Then Evaluate once resolve(model); assign in source target order to (model_id, via, extras). Then Evaluate once get_backend(via, model_id); assign in source target order to backend.
  // Source: vvaharness/backends/llm/registry.py:244-245
  if (the source predicate via == DEFAULT_LLM_VIA is truthy) {
    // Source: vvaharness/backends/llm/registry.py:245-245
    In source order: Evaluate warn_cli_dropped_knobs(model_id, extras); retain side effects and discard the expression result.
  }
  // Source: vvaharness/backends/llm/registry.py:246-250
  if (the source predicate kw.get('max_output_tokens') is not None is truthy) {
    // Source: vvaharness/backends/llm/registry.py:249-250
    In source order: Evaluate once clamp_output_tokens(int(kw['max_output_tokens']), model, tag=kw.get('tag')); assign in source target order to kw['max_output_tokens'].
  }
  // Source: vvaharness/backends/llm/registry.py:251-253
  if (the source predicate via == 'openai' is truthy) {
    // Source: vvaharness/backends/llm/registry.py:252-253
    In source order: Evaluate once output_cap_of(model); assign in source target order to kw['output_cap']. Then Evaluate once use_responses_api_of(model); assign in source target order to kw['use_responses_api'].
  }
  // Source: vvaharness/backends/llm/registry.py:254-254
  In source order: Evaluate once kw.pop('cache_prefix', None); assign in source target order to cache_prefix.
  // Source: vvaharness/backends/llm/registry.py:255-256
  if (the source predicate cache_prefix is truthy) {
    // Source: vvaharness/backends/llm/registry.py:256-256
    In source order: Evaluate once cache_prefix + user_prompt; assign in source target order to user_prompt.
  }
  // Source: vvaharness/backends/llm/registry.py:260-261
  if (the source predicate via != DEFAULT_LLM_VIA is truthy) {
    // Source: vvaharness/backends/llm/registry.py:261-261
    In source order: Evaluate kw.pop('stream_cb', None); retain side effects and discard the expression result.
  }
  // Source: vvaharness/backends/llm/registry.py:262-264
  In source order: Evaluate once backend.agentic(user_prompt, model=model_id, **kw); assign in source target order to text. Then Evaluate check_response_quality(text, stage=str(kw.get('tag', '') or '')); retain side effects and discard the expression result.
  // Source: vvaharness/backends/llm/registry.py:265-265
  End this invocation with text.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.backends.llm.cli import parse_json_response` at source line 24: `source_detail/vvaharness/backends/llm/cli/__init__.py.sudo.md`.
- `from vvaharness.backends.llm.models import LlmBackend, ModelExtras, ModulePath, ResolvedModel` at source line 25: `source_detail/vvaharness/backends/llm/models.py.sudo.md`.
- `from vvaharness.util import logs` at source line 31: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import logs` at source line 31: `source_detail/vvaharness/util/logs.py.sudo.md`.
- `from vvaharness.util.events import Event` at source line 32: `source_detail/vvaharness/util/events.py.sudo.md`.
- `from vvaharness.util.response_quality import check_response_quality` at source line 33: `source_detail/vvaharness/util/response_quality.py.sudo.md`.
- `from vvaharness.util.scan_progress import get_active_tracker` at source line 34: `source_detail/vvaharness/util/scan_progress.py.sudo.md`.
- `from vvaharness.util.tokens import TOKENS` at source line 35: `source_detail/vvaharness/util/tokens.py.sudo.md`.
- `from vvaharness.util.warn_once import warn_once` at source line 36: `source_detail/vvaharness/util/warn_once.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../prompt_representation/vvaharness/backends/llm/registry.py.sudo.md). Exact strings in the evidence asset support this conversion.
