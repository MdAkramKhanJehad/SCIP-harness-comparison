# vvaharness/backends/harness/deepagents/options/model_building.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/backends/harness/deepagents/options/model_building.py.evidence.json`. SHA-256: `630ea52d3fcfc05776cb487d7480a9cb1fb772f0b66f8b24663a0b18971a9b39`.

```sudo
// Source: vvaharness/backends/harness/deepagents/options/model_building.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import asyncio; preserve alias and import-time effects. Then Resolve source import import itertools; preserve alias and import-time effects. Then Resolve source import import os; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/deepagents/options/model_building.py:22-26
In source order: Resolve source import import re; preserve alias and import-time effects. Then Resolve source import import ssl; preserve alias and import-time effects. Then Resolve source import import threading; preserve alias and import-time effects. Then Resolve source import import weakref; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/deepagents/options/model_building.py:27-32
In source order: Resolve source import from typing import Any, Final; preserve alias and import-time effects. Then Resolve source import import anthropic; preserve alias and import-time effects. Then Resolve source import import httpx2; preserve alias and import-time effects. Then Resolve source import import langchain_anthropic; preserve alias and import-time effects. Then Resolve source import import openai; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/deepagents/options/model_building.py:33-53
In source order: Resolve source import from langchain_anthropic import ChatAnthropic; preserve alias and import-time effects. Then Resolve source import from langchain_core.language_models import BaseChatModel; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.deepagents import tool_choice_rejection; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.deepagents.limits import MODEL_MAX_OUTPUT_TOKENS, MODEL_MAX_RETRIES, MODEL_TIMEOUT_SECONDS; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.deepagents.models import SSL_CERT_DIR_VAR, SSL_CERT_FILE_VAR, TLS_CLIENT_CERT_VAR, TLS_CLIENT_KEY_VAR, TLS_VERIFY_VAR, ModelKey, anthropic_base, anthropic_key, openai_base, openai_key; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/deepagents/options/model_building.py:54-69
In source order: Resolve source import from vvaharness.backends.harness.deepagents.options.forcing import ForcingChatAnthropic; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.deepagents.options.tool_call_state import ToolCallStateChatOpenAI; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.models import EffortLevel; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.provider_routing import TRANSPORT_CHAT_COMPLETIONS, TRANSPORT_RESPONSES, routes_to_anthropic; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm.models import EFFORT_REJECTIONS, REASONING_OFF, TRANSPORT_MEMORY, ClockKind, effort_after_rejections, effort_scaled_seconds; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/deepagents/options/model_building.py:72-85
In source order: Resolve source import from vvaharness.backends.llm.tls import anthropic_auth_kwargs, chain_paths, coerce_verify, is_anthropic_oauth_token, load_client_chain, resolve_client_chain, scoped_no_proxy_env, warn_verify_disabled; preserve alias and import-time effects. Then Resolve source import from vvaharness.orchestrator.config_paths import _resolve_against; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import logs; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.events import Event; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.warn_once import warn_once; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/deepagents/options/model_building.py:87-93
In source order: Evaluate once logs.get_logger(__name__); assign in source target order to log. Then Evaluate once 'vvaharness-config:'; assign in source target order to _TLS_VERIFY_STAMP. Then Evaluate once 'VVAHARNESS_NO_PROXY'; assign in source target order to NO_PROXY_VAR.
// Source: vvaharness/backends/harness/deepagents/options/model_building.py:96-121
// Source signature: _ca_bundle(env: dict[str, str], *, allow_ambient: bool) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _ca_bundle(env, allow_ambient) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:97-97
  In source order: Retain source documentation literal source_literal_97_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:99-109
  if (the source predicate allow_ambient is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/model_building.py:100-107
    In source order: Evaluate once env.get(SSL_CERT_FILE_VAR) or env.get('REQUESTS_CA_BUNDLE') or env.get('NODE_EXTRA_CA_CERTS') or os.environ.get(SSL_CERT_FILE_VAR) or os.environ.get('REQUESTS_CA_BUNDLE') or os.environ.get('NODE_EXTRA_CA_CERTS'); assign in source target order to ca_file.
  }
  else {
    // Source: vvaharness/backends/harness/deepagents/options/model_building.py:109-109
    In source order: Evaluate once env.get(SSL_CERT_FILE_VAR); assign in source target order to ca_file.
  }
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:110-113
  if (the source predicate ca_file and (not Path(ca_file).is_file()) is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/model_building.py:111-113
    Raise FileNotFoundError(source_template_112_12).
  }
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:114-116
  In source order: Evaluate once env.get(SSL_CERT_DIR_VAR) or (os.environ.get(SSL_CERT_DIR_VAR) if allow_ambient else None); assign in source target order to ca_dir.
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:117-120
  if (the source predicate ca_dir and (not Path(ca_dir).is_dir()) is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/model_building.py:118-120
    Raise FileNotFoundError(source_template_119_12).
  }
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:121-121
  End this invocation with ca_file or ca_dir.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/options/model_building.py:124-133
// Source signature: _config_verify(env: dict[str, str]) -> str | bool | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _config_verify(env) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:125-127
  In source order: Retain source documentation literal source_literal_125_4; it is not a model call. Then Evaluate once env.get(TLS_VERIFY_VAR); assign in source target order to raw.
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:128-129
  if (the source predicate raw is None is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/model_building.py:129-129
    End this invocation with None.
  }
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:130-132
  if (the source predicate not raw.startswith(_TLS_VERIFY_STAMP) is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/model_building.py:131-131
    In source order: Evaluate log.warning(Event.AMBIENT_ENV_IGNORED, var=TLS_VERIFY_VAR, value=raw, knob='verify_ssl'); retain side effects and discard the expression result.
    // Source: vvaharness/backends/harness/deepagents/options/model_building.py:132-132
    End this invocation with None.
  }
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:133-133
  End this invocation with coerce_verify(raw.removeprefix(_TLS_VERIFY_STAMP)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/options/model_building.py:136-145
// Source signature: _config_no_proxy(env: dict[str, str]) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _config_no_proxy(env) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:137-139
  In source order: Retain source documentation literal source_literal_137_4; it is not a model call. Then Evaluate once env.get(NO_PROXY_VAR); assign in source target order to raw.
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:140-141
  if (the source predicate raw is None is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/model_building.py:141-141
    End this invocation with None.
  }
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:142-144
  if (the source predicate not raw.startswith(_TLS_VERIFY_STAMP) is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/model_building.py:143-143
    In source order: Evaluate log.warning(Event.AMBIENT_ENV_IGNORED, var=NO_PROXY_VAR, value=raw, knob='no_proxy'); retain side effects and discard the expression result.
    // Source: vvaharness/backends/harness/deepagents/options/model_building.py:144-144
    End this invocation with None.
  }
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:145-145
  End this invocation with raw.removeprefix(_TLS_VERIFY_STAMP) or None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/options/model_building.py:148-158
// Source signature: _resolve_verify(env: dict[str, str], *, allow_ambient: bool) -> str | bool | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _resolve_verify(env, allow_ambient) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:149-150
  In source order: Retain source documentation literal source_literal_149_4; it is not a model call. Then Evaluate once _ca_bundle(env, allow_ambient=allow_ambient) or _config_verify(env); assign in source target order to verify.
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:151-156
  if (the source predicate verify is False is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/model_building.py:152-155
    In source order: Evaluate warn_verify_disabled(openai_base(env) if allow_ambient else anthropic_base(env), label='deepagents'); retain side effects and discard the expression result.
    // Source: vvaharness/backends/harness/deepagents/options/model_building.py:156-156
    End this invocation with False.
  }
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:158-158
  End this invocation with verify if isinstance(verify, str) else None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/options/model_building.py:161-169
// Source signature: _client_cert(env: dict[str, str]) -> str | tuple[str, ...] | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _client_cert(env) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:162-163
  In source order: Retain source documentation literal source_literal_162_4; it is not a model call. Then Evaluate once env.get(TLS_CLIENT_CERT_VAR) or os.environ.get(TLS_CLIENT_CERT_VAR); assign in source target order to cert.
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:164-165
  if (the source predicate not cert is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/model_building.py:165-165
    End this invocation with None.
  }
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:166-166
  In source order: Evaluate once env.get(TLS_CLIENT_KEY_VAR) or os.environ.get(TLS_CLIENT_KEY_VAR); assign in source target order to key.
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:167-169
  End this invocation with resolve_client_chain((cert, key) if key else cert, label='deepagents', noun='client_cert/key').
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/options/model_building.py:172-177
// Source signature: _resolve_cert_path(path: str, cfg_dir: Path | None) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _resolve_cert_path(path, cfg_dir) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:173-173
  In source order: Retain source documentation literal source_literal_173_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:175-176
  if (the source predicate cfg_dir is None is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/model_building.py:176-176
    End this invocation with path.
  }
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:177-177
  End this invocation with _resolve_against(cfg_dir, path).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/options/model_building.py:180-209
// Source signature: tls_carriers_for(model_id: str, provider: str | None, *, sdk_cfg: object | None, openai_cfg: object | None, cfg_dir: Path | str | None=None) -> dict[str, str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn tls_carriers_for(model_id, provider, sdk_cfg, openai_cfg, cfg_dir) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:188-190
  In source order: Retain source documentation literal source_literal_188_4; it is not a model call. Then Evaluate once sdk_cfg if routes_to_anthropic(model_id, provider) else openai_cfg; assign in source target order to block.
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:191-192
  if (the source predicate block is None is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/model_building.py:192-192
    End this invocation with {}.
  }
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:193-195
  In source order: Evaluate once Path(cfg_dir) if cfg_dir else None; assign in source target order to directory. Then For carriers, assign {}; source annotation dict[str, str]. Then Evaluate once getattr(block, 'ca_cert', None); assign in source target order to ca.
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:196-197
  if (the source predicate ca is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/model_building.py:197-197
    In source order: Evaluate once _resolve_cert_path(ca, directory); assign in source target order to carriers[SSL_CERT_FILE_VAR].
  }
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:198-199
  In source order: Evaluate once getattr(block, 'client_cert', None); assign in source target order to cert. Then Evaluate once chain_paths(cert) if cert else (); assign in source target order to pair.
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:200-201
  for each (var, path) in zip((TLS_CLIENT_CERT_VAR, TLS_CLIENT_KEY_VAR), pair, strict=False) {
    // Source: vvaharness/backends/harness/deepagents/options/model_building.py:201-201
    In source order: Evaluate once _resolve_cert_path(path, directory); assign in source target order to carriers[var].
  }
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:202-202
  In source order: Evaluate once coerce_verify(getattr(block, 'verify_ssl', None)); assign in source target order to verify.
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:203-205
  if (the source predicate verify is not None and verify is not True is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/model_building.py:204-205
    In source order: Evaluate once 'false' if verify is False else _resolve_cert_path(verify, directory); assign in source target order to value. Then Evaluate once _TLS_VERIFY_STAMP + value; assign in source target order to carriers[TLS_VERIFY_VAR].
  }
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:206-206
  In source order: Evaluate once getattr(block, 'no_proxy', None); assign in source target order to no_proxy.
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:207-208
  if (the source predicate no_proxy is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/model_building.py:208-208
    In source order: Evaluate once _TLS_VERIFY_STAMP + no_proxy; assign in source target order to carriers[NO_PROXY_VAR].
  }
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:209-209
  End this invocation with carriers.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/options/model_building.py:212-228
// Source signature: _ssl_context(env: dict[str, str], *, allow_ambient_ca: bool=True) -> ssl.SSLContext | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _ssl_context(env, allow_ambient_ca) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:215-218
  In source order: Retain source documentation literal source_literal_215_4; it is not a model call. Then Evaluate once _resolve_verify(env, allow_ambient=allow_ambient_ca); assign in source target order to verify. Then Evaluate once _client_cert(env); assign in source target order to cert.
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:219-220
  if (the source predicate verify is None and cert is None is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/model_building.py:220-220
    End this invocation with None.
  }
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:221-223
  In source order: Evaluate once httpx2.create_ssl_context(verify=True if verify is None else verify, trust_env=True); assign in source target order to context.
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:224-227
  if (the source predicate cert is not None and (not load_client_chain(context, cert, label='deepagents')) and (verify is None) is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/model_building.py:227-227
    End this invocation with None.
  }
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:228-228
  End this invocation with context.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/options/model_building.py:231-272
// Source signature: _inject_anthropic_clients(chat: ChatAnthropic, ssl_context: ssl.SSLContext | None, token: str, *, timeout: float=MODEL_TIMEOUT_SECONDS) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _inject_anthropic_clients(chat, ssl_context, token, timeout) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:233-235
  In source order: Retain source documentation literal source_literal_233_4; it is not a model call. Then Evaluate once None; assign in source target order to sync_http.
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:236-272
  Perform the following protected operations {
    // Source: vvaharness/backends/harness/deepagents/options/model_building.py:237-237
    In source order: Evaluate once dict(chat._client_params); assign in source target order to params.
    // Source: vvaharness/backends/harness/deepagents/options/model_building.py:238-243
    if (the source predicate is_anthropic_oauth_token(token) is truthy) {
      // Source: vvaharness/backends/harness/deepagents/options/model_building.py:243-243
      In source order: Evaluate params.pop('api_key', None); retain side effects and discard the expression result.
    }
    // Source: vvaharness/backends/harness/deepagents/options/model_building.py:244-244
    In source order: For http_kwargs, assign {'timeout': timeout}; source annotation dict[str, object].
    // Source: vvaharness/backends/harness/deepagents/options/model_building.py:245-246
    if (the source predicate ssl_context is not None is truthy) {
      // Source: vvaharness/backends/harness/deepagents/options/model_building.py:246-246
      In source order: Evaluate once ssl_context; assign in source target order to http_kwargs['verify'].
    }
    // Source: vvaharness/backends/harness/deepagents/options/model_building.py:247-257
    In source order: Evaluate once anthropic.DefaultHttpxClient(**http_kwargs); assign in source target order to sync_http. Then Evaluate once anthropic.Client(**{**params, **anthropic_auth_kwargs(token), 'http_client': sync_http}); assign in source target order to chat.__dict__['_client']. Then Evaluate once anthropic.AsyncClient(**{**params, **anthropic_auth_kwargs(token), 'http_client': anthropic.DefaultAsyncHttpxClient(**http_kwargs)}); assign in source target order to chat.__dict__['_async_client'].
  }
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:258-272
  On the first matching source exception Exception as exc, in handler order {
    // Source: vvaharness/backends/harness/deepagents/options/model_building.py:260-261
    In source order: Evaluate chat.__dict__.pop('_client', None); retain side effects and discard the expression result. Then Evaluate chat.__dict__.pop('_async_client', None); retain side effects and discard the expression result.
    // Source: vvaharness/backends/harness/deepagents/options/model_building.py:262-263
    if (the source predicate sync_http is not None is truthy) {
      // Source: vvaharness/backends/harness/deepagents/options/model_building.py:263-263
      In source order: Evaluate sync_http.close(); retain side effects and discard the expression result.
    }
    // Source: vvaharness/backends/harness/deepagents/options/model_building.py:264-264
    In source order: Evaluate once getattr(langchain_anthropic, '__version__', 'unknown'); assign in source target order to version.
    // Source: vvaharness/backends/harness/deepagents/options/model_building.py:265-272
    Raise RuntimeError(source_template_266_12) with explicit source cause exc.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/options/model_building.py:275-281
In source order: For _OPENAI_EFFORT_MAP, assign {EffortLevel.LOW: 'low', EffortLevel.MEDIUM: 'medium', EffortLevel.HIGH: 'high', EffortLevel.XHIGH: 'xhigh', EffortLevel.MAX: 'max'}; source annotation dict[EffortLevel, str].
// Source: vvaharness/backends/harness/deepagents/options/model_building.py:284-287
// Source signature: _to_openai_reasoning_effort(effort: str | None) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _to_openai_reasoning_effort(effort) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:285-286
  In source order: Retain source documentation literal source_literal_285_4; it is not a model call. Then Evaluate once EffortLevel.parse(effort); assign in source target order to parsed.
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:287-287
  End this invocation with _OPENAI_EFFORT_MAP.get(parsed) if parsed is not None else None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/options/model_building.py:291-306
In source order: For _NO_REASONING_EFFORT, assign EFFORT_REJECTIONS.tiers; source annotation set[tuple[str, str]]. Then For _CHAT_COMPLETIONS_ONLY_MODELS, assign TRANSPORT_MEMORY.chat_only; source annotation set[str]. Then For _FORCED_TOOL_CHOICE_UNSUPPORTED_MODELS, assign tool_choice_rejection.UNSUPPORTED_MODELS; source annotation set[str]. Then For _RESPONSES_BROKEN_MODELS, assign frozenset({'kimi-k2.6', 'kimi-k2.7-code', 'glm-5.2'}); source annotation frozenset[str].
// Source: vvaharness/backends/harness/deepagents/options/model_building.py:309-311
// Source signature: _needs_chat_completions(model_id: str) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _needs_chat_completions(model_id) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:310-310
  In source order: Retain source documentation literal source_literal_310_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:311-311
  End this invocation with model_id.rsplit(_GATEWAY_NAMESPACE, 1)[-1].lower() in _RESPONSES_BROKEN_MODELS.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/options/model_building.py:314-316
In source order: For RESPONSES_INCLUDE_ENCRYPTED_REASONING, assign ('reasoning.encrypted_content',); source annotation Final[tuple[str, ...]].
// Source: vvaharness/backends/harness/deepagents/options/model_building.py:319-331
// Source signature: _effort_kwargs(model_id: str, effort: str | None, transport: str=TRANSPORT_CHAT_COMPLETIONS) -> dict[str, Any]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _effort_kwargs(model_id, effort, transport) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:322-327
  In source order: Retain source documentation literal source_literal_322_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:328-329
  if (the source predicate model_id in EFFORT_REJECTIONS.field is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/model_building.py:329-329
    End this invocation with {}.
  }
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:330-330
  In source order: Evaluate once effort_after_rejections(model_id, _to_openai_reasoning_effort(effort), transport); assign in source target order to mapped.
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:331-331
  End this invocation with {} if mapped is None else {'reasoning_effort': mapped}.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/options/model_building.py:336-340
In source order: For _REASONING_OFF_MODELS, assign frozenset({'kimi-k2.6', 'kimi-k2.7-code', 'glm-5.2'}); source annotation frozenset[str].
// Source: vvaharness/backends/harness/deepagents/options/model_building.py:343-350
// Source signature: _reasoning_off_kwargs(model_id: str) -> dict[str, Any]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _reasoning_off_kwargs(model_id) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:344-344
  In source order: Retain source documentation literal source_literal_344_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:345-346
  if (the source predicate model_id not in _REASONING_OFF_MODELS or model_id in EFFORT_REJECTIONS.field is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/model_building.py:346-346
    End this invocation with {}.
  }
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:348-349
  if (the source predicate (model_id, REASONING_OFF) in _NO_REASONING_EFFORT is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/model_building.py:349-349
    End this invocation with {}.
  }
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:350-350
  End this invocation with {'reasoning_effort': REASONING_OFF}.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/options/model_building.py:353-375
In source order: For _ANTHROPIC_EFFORT_MAP, assign {EffortLevel.LOW: 'low', EffortLevel.MEDIUM: 'medium', EffortLevel.HIGH: 'high', EffortLevel.XHIGH: 'xhigh', EffortLevel.MAX: 'max'}; source annotation dict[EffortLevel, str]. Then Evaluate once source_literal_365_4; assign in source target order to REASON_IN_PROMPT. Then For _NO_REASON_IN_PROMPT_RX, assign re.compile('claude-(?:sonnet-5-5|opus-5|fable-5)(?!\\d)', re.IGNORECASE); source annotation Final[re.Pattern[str]].
// Source: vvaharness/backends/harness/deepagents/options/model_building.py:378-382
// Source signature: reasons_in_prompt(model_id: str, provider: str | None) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn reasons_in_prompt(model_id, provider) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:379-379
  In source order: Retain source documentation literal source_literal_379_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:380-381
  if (the source predicate not routes_to_anthropic(model_id, provider) is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/model_building.py:381-381
    End this invocation with True.
  }
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:382-382
  End this invocation with _NO_REASON_IN_PROMPT_RX.search(model_id) is None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/options/model_building.py:385-395
// Source signature: _anthropic_thinking_kwargs(effort: str | None, *, in_prompt: bool=False) -> dict[str, Any]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _anthropic_thinking_kwargs(effort, in_prompt) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:386-388
  In source order: Retain source documentation literal source_literal_386_4; it is not a model call. Then Evaluate once EffortLevel.parse(effort); assign in source target order to parsed. Then Evaluate once _ANTHROPIC_EFFORT_MAP.get(parsed) if parsed is not None else None; assign in source target order to mapped.
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:389-390
  if (the source predicate mapped is None is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/model_building.py:390-390
    End this invocation with {'thinking': {'type': 'disabled'}} if in_prompt else {}.
  }
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:393-394
  if (the source predicate in_prompt is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/model_building.py:394-394
    End this invocation with {'thinking': {'type': 'disabled'}, 'output_config': {'effort': mapped}}.
  }
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:395-395
  End this invocation with {'thinking': {'type': 'adaptive'}, 'output_config': {'effort': mapped}}.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/options/model_building.py:398-408
// Source signature: resolve_use_responses_api(model_id: str, provider: str | None, override: bool | None) -> bool | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn resolve_use_responses_api(model_id, provider, override) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:401-401
  In source order: Retain source documentation literal source_literal_401_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:402-403
  if (the source predicate routes_to_anthropic(model_id, provider) is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/model_building.py:403-403
    End this invocation with None.
  }
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:404-405
  if (the source predicate override is not None is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/model_building.py:405-405
    End this invocation with override.
  }
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:406-407
  if (the source predicate _needs_chat_completions(model_id) is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/model_building.py:407-407
    End this invocation with False.
  }
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:408-408
  End this invocation with model_id not in _CHAT_COMPLETIONS_ONLY_MODELS.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/options/model_building.py:412-415
In source order: For _INFERRED_VENDOR_WARNED, assign set(); source annotation set[str]. Then Evaluate once '/'; assign in source target order to _GATEWAY_NAMESPACE.
// Source: vvaharness/backends/harness/deepagents/options/model_building.py:418-430
// Source signature: _warn_if_vendor_inferred(model_id: str, provider: str | None) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _warn_if_vendor_inferred(model_id, provider) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:419-419
  In source order: Retain source documentation literal source_literal_419_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:421-422
  if (the source predicate provider or _GATEWAY_NAMESPACE not in model_id is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/model_building.py:422-422
    End this invocation with None.
  }
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:423-430
  In source order: Evaluate once 'anthropic' if routes_to_anthropic(model_id, provider) else 'openai'; assign in source target order to vendor. Then Evaluate warn_once(_INFERRED_VENDOR_WARNED, model_id, source_template_426_8); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/options/model_building.py:433-441
// Source signature: _transport_kwargs(resolved: bool) -> dict[str, Any]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _transport_kwargs(resolved) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:434-434
  In source order: Retain source documentation literal source_literal_434_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:435-436
  if (the source predicate not resolved is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/model_building.py:436-436
    End this invocation with {'use_responses_api': False}.
  }
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:437-441
  End this invocation with {'use_responses_api': True, 'store': False, 'include': list(RESPONSES_INCLUDE_ENCRYPTED_REASONING)}.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/options/model_building.py:444-456
// Source signature: _openai_effort_kwargs(model_id: str, effort: str | None, *, think_in_prompt: bool, resolved_transport: bool) -> dict[str, Any]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _openai_effort_kwargs(model_id, effort, think_in_prompt, resolved_transport) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:447-447
  In source order: Retain source documentation literal source_literal_447_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:451-452
  if (the source predicate model_id in EFFORT_REJECTIONS.tools_off and (not resolved_transport) is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/model_building.py:452-452
    End this invocation with {'reasoning_effort': REASONING_OFF}.
  }
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:454-454
  In source order: Evaluate once TRANSPORT_RESPONSES if resolved_transport else TRANSPORT_CHAT_COMPLETIONS; assign in source target order to transport.
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:455-456
  End this invocation with _reasoning_off_kwargs(model_id) if think_in_prompt else _effort_kwargs(model_id, effort, transport).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/options/model_building.py:459-521
// Source signature: build_model(model_id: str, env: dict[str, str], provider: str | None=None, effort: str | None=None, use_responses_api: bool | None=None, think_in_prompt: bool=False) -> BaseChatModel
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn build_model(model_id, env, provider, effort, use_responses_api, think_in_prompt) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:467-472
  In source order: Retain source documentation literal source_literal_467_4; it is not a model call. Then Evaluate _warn_if_vendor_inferred(model_id, provider); retain side effects and discard the expression result. Then Evaluate once think_in_prompt and reasons_in_prompt(model_id, provider); assign in source target order to think_in_prompt. Then Evaluate once routes_to_anthropic(model_id, provider); assign in source target order to anthropic_route. Then Evaluate once _ssl_context(env, allow_ambient_ca=not anthropic_route); assign in source target order to ssl_context.
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:473-477
  In source order: Evaluate once _config_no_proxy(env); assign in source target order to no_proxy. Then Evaluate once effort_scaled_seconds(MODEL_TIMEOUT_SECONDS, effort, kind=ClockKind.REQUEST); assign in source target order to request_timeout.
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:478-493
  if (the source predicate anthropic_route is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/model_building.py:479-489
    In source order: Evaluate once anthropic_key(env); assign in source target order to token. Then Evaluate once ForcingChatAnthropic(model_name=model_id, api_key=token, base_url=anthropic_base(env), timeout=request_timeout, max_retries=MODEL_MAX_RETRIES, max_tokens_to_sample=MODEL_MAX_OUTPUT_TOKENS, **_anthropic_thinking_kwargs(effort, in_prompt=think_in_prompt)); assign in source target order to chat.
    // Source: vvaharness/backends/harness/deepagents/options/model_building.py:490-492
    if (the source predicate ssl_context is not None or is_anthropic_oauth_token(token) is truthy) {
      // Source: vvaharness/backends/harness/deepagents/options/model_building.py:491-492
      Enter source context managers left-to-right: scoped_no_proxy_env(no_proxy) {
        // Source: vvaharness/backends/harness/deepagents/options/model_building.py:492-492
        In source order: Evaluate _inject_anthropic_clients(chat, ssl_context, token or '', timeout=request_timeout); retain side effects and discard the expression result.
      }
      Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    }
    // Source: vvaharness/backends/harness/deepagents/options/model_building.py:493-493
    End this invocation with chat.
  }
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:496-496
  In source order: For client_kwargs, assign {'timeout': request_timeout}; source annotation dict[str, Any].
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:497-498
  if (the source predicate ssl_context is not None is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/model_building.py:498-498
    In source order: Evaluate once ssl_context; assign in source target order to client_kwargs['verify'].
  }
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:499-501
  Enter source context managers left-to-right: scoped_no_proxy_env(no_proxy) {
    // Source: vvaharness/backends/harness/deepagents/options/model_building.py:500-501
    In source order: Evaluate once openai.DefaultHttpxClient(**client_kwargs); assign in source target order to http_client. Then Evaluate once openai.DefaultAsyncHttpxClient(**client_kwargs); assign in source target order to http_async_client.
  }
  Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:503-503
  In source order: For socket_options_kwargs, assign {}; source annotation dict[str, Any].
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:504-505
  if (the source predicate 'http_socket_options' in ToolCallStateChatOpenAI.model_fields is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/model_building.py:505-505
    In source order: Evaluate once (); assign in source target order to socket_options_kwargs['http_socket_options'].
  }
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:506-509
  In source order: Evaluate once bool(resolve_use_responses_api(model_id, provider, use_responses_api)); assign in source target order to resolved_transport. Then Evaluate once _openai_effort_kwargs(model_id, effort, think_in_prompt=think_in_prompt, resolved_transport=resolved_transport); assign in source target order to effort_kwargs. Then Evaluate once _transport_kwargs(resolved_transport); assign in source target order to transport_kwargs.
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:510-521
  End this invocation with ToolCallStateChatOpenAI(model=model_id, api_key=openai_key(env), base_url=openai_base(env), timeout=request_timeout, max_retries=MODEL_MAX_RETRIES, http_client=http_client, http_async_client=http_async_client, **socket_options_kwargs, **effort_kwargs, **transport_kwargs).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/options/model_building.py:525-544
In source order: For _TLS_ENV_VARS, assign (TLS_CLIENT_CERT_VAR, TLS_CLIENT_KEY_VAR, TLS_VERIFY_VAR, NO_PROXY_VAR, SSL_CERT_FILE_VAR, SSL_CERT_DIR_VAR, 'REQUESTS_CA_BUNDLE', 'NODE_EXTRA_CA_CERTS'); source annotation tuple[str, ...]. Then For _model_cache, assign {}; source annotation dict[tuple[Any, ...], BaseChatModel]. Then Evaluate once threading.Lock(); assign in source target order to _model_cache_lock. Then For _loop_tokens, assign weakref.WeakKeyDictionary(); source annotation 'weakref.WeakKeyDictionary[Any, int]'. Then Evaluate once itertools.count(); assign in source target order to _loop_token_counter.
// Source: vvaharness/backends/harness/deepagents/options/model_building.py:545-545
In source order: Evaluate once threading.Lock(); assign in source target order to _loop_token_lock.
// Source: vvaharness/backends/harness/deepagents/options/model_building.py:548-550
// Source signature: _tls_fingerprint(env: dict[str, str]) -> tuple[str, ...]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _tls_fingerprint(env) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:549-549
  In source order: Retain source documentation literal source_literal_549_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:550-550
  End this invocation with tuple((env.get(v) or os.environ.get(v) or '' for v in _TLS_ENV_VARS)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/options/model_building.py:553-589
// Source signature: _loop_token() -> int | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _loop_token() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:554-576
  In source order: Retain source documentation literal source_literal_554_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:577-580
  Perform the following protected operations {
    // Source: vvaharness/backends/harness/deepagents/options/model_building.py:578-578
    In source order: Evaluate once asyncio.get_running_loop(); assign in source target order to loop.
  }
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:579-580
  On the first matching source exception RuntimeError, in handler order {
    // Source: vvaharness/backends/harness/deepagents/options/model_building.py:580-580
    End this invocation with None.
  }
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:581-581
  In source order: Evaluate once _loop_tokens.get(loop); assign in source target order to token.
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:582-583
  if (the source predicate token is not None is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/model_building.py:583-583
    End this invocation with token.
  }
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:584-589
  Enter source context managers left-to-right: _loop_token_lock {
    // Source: vvaharness/backends/harness/deepagents/options/model_building.py:585-585
    In source order: Evaluate once _loop_tokens.get(loop); assign in source target order to token.
    // Source: vvaharness/backends/harness/deepagents/options/model_building.py:586-588
    if (the source predicate token is None is truthy) {
      // Source: vvaharness/backends/harness/deepagents/options/model_building.py:587-588
      In source order: Evaluate once next(_loop_token_counter); assign in source target order to token. Then Evaluate once token; assign in source target order to _loop_tokens[loop].
    }
    // Source: vvaharness/backends/harness/deepagents/options/model_building.py:589-589
    End this invocation with token.
  }
  Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/options/model_building.py:592-627
// Source signature: build_model_cached(model_id: str, env: dict[str, str], provider: str | None=None, effort: str | None=None, use_responses_api: bool | None=None, think_in_prompt: bool=False) -> BaseChatModel
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn build_model_cached(model_id, env, provider, effort, use_responses_api, think_in_prompt) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:600-616
  In source order: Retain source documentation literal source_literal_600_4; it is not a model call. Then Evaluate once resolve_use_responses_api(model_id, provider, use_responses_api); assign in source target order to resolved_transport. Then Evaluate once _openai_effort_kwargs(model_id, effort, think_in_prompt=think_in_prompt, resolved_transport=bool(resolved_transport)).get('reasoning_effort'); assign in source target order to cache_effort. Then Evaluate once (ModelKey.of(model_id, env, provider, cache_effort, resolved_transport), _tls_fingerprint(env), think_in_prompt, _loop_token()); assign in source target order to key. Then Evaluate once _model_cache.get(key); assign in source target order to cached.
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:617-618
  if (the source predicate cached is not None is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/model_building.py:618-618
    End this invocation with cached.
  }
  // Source: vvaharness/backends/harness/deepagents/options/model_building.py:620-627
  Enter source context managers left-to-right: _model_cache_lock {
    // Source: vvaharness/backends/harness/deepagents/options/model_building.py:621-621
    In source order: Evaluate once _model_cache.get(key); assign in source target order to cached.
    // Source: vvaharness/backends/harness/deepagents/options/model_building.py:622-623
    if (the source predicate cached is not None is truthy) {
      // Source: vvaharness/backends/harness/deepagents/options/model_building.py:623-623
      End this invocation with cached.
    }
    // Source: vvaharness/backends/harness/deepagents/options/model_building.py:624-626
    In source order: Evaluate once build_model(model_id, env, provider, effort, resolved_transport, think_in_prompt=think_in_prompt); assign in source target order to model. Then Evaluate once model; assign in source target order to _model_cache[key].
    // Source: vvaharness/backends/harness/deepagents/options/model_building.py:627-627
    End this invocation with model.
  }
  Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.backends.harness.deepagents import tool_choice_rejection` at source line 36: `source_detail/vvaharness/backends/harness/deepagents/__init__.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents import tool_choice_rejection` at source line 36: `source_detail/vvaharness/backends/harness/deepagents/tool_choice_rejection.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.limits import MODEL_MAX_OUTPUT_TOKENS, MODEL_MAX_RETRIES, MODEL_TIMEOUT_SECONDS` at source line 37: `source_detail/vvaharness/backends/harness/deepagents/limits.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.models import SSL_CERT_DIR_VAR, SSL_CERT_FILE_VAR, TLS_CLIENT_CERT_VAR, TLS_CLIENT_KEY_VAR, TLS_VERIFY_VAR, ModelKey, anthropic_base, anthropic_key, openai_base, openai_key` at source line 42: `source_detail/vvaharness/backends/harness/deepagents/models.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.options.forcing import ForcingChatAnthropic` at source line 54: `source_detail/vvaharness/backends/harness/deepagents/options/forcing.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.options.tool_call_state import ToolCallStateChatOpenAI` at source line 55: `source_detail/vvaharness/backends/harness/deepagents/options/tool_call_state.py.sudo.md`.
- `from vvaharness.backends.harness.models import EffortLevel` at source line 56: `source_detail/vvaharness/backends/harness/models.py.sudo.md`.
- `from vvaharness.backends.harness.provider_routing import TRANSPORT_CHAT_COMPLETIONS, TRANSPORT_RESPONSES, routes_to_anthropic` at source line 57: `source_detail/vvaharness/backends/harness/provider_routing.py.sudo.md`.
- `from vvaharness.backends.llm.models import EFFORT_REJECTIONS, REASONING_OFF, TRANSPORT_MEMORY, ClockKind, effort_after_rejections, effort_scaled_seconds` at source line 62: `source_detail/vvaharness/backends/llm/models.py.sudo.md`.
- `from vvaharness.backends.llm.tls import anthropic_auth_kwargs, chain_paths, coerce_verify, is_anthropic_oauth_token, load_client_chain, resolve_client_chain, scoped_no_proxy_env, warn_verify_disabled` at source line 72: `source_detail/vvaharness/backends/llm/tls.py.sudo.md`.
- `from vvaharness.orchestrator.config_paths import _resolve_against` at source line 82: `source_detail/vvaharness/orchestrator/config_paths.py.sudo.md`.
- `from vvaharness.util import logs` at source line 83: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import logs` at source line 83: `source_detail/vvaharness/util/logs.py.sudo.md`.
- `from vvaharness.util.events import Event` at source line 84: `source_detail/vvaharness/util/events.py.sudo.md`.
- `from vvaharness.util.warn_once import warn_once` at source line 85: `source_detail/vvaharness/util/warn_once.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../../../prompt_representation/vvaharness/backends/harness/deepagents/options/model_building.py.sudo.md). Exact strings in the evidence asset support this conversion.
