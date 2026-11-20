# vvaharness/backends/llm/sdk.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/backends/llm/sdk.py.evidence.json`. SHA-256: `3e6961017efb73bf12539c923b3d322c2f75eab61e81eba0f7d57941d1064c91`.

```sudo
// Source: vvaharness/backends/llm/sdk.py:15-25
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import json; preserve alias and import-time effects. Then Resolve source import import os; preserve alias and import-time effects. Then Resolve source import import re; preserve alias and import-time effects.
// Source: vvaharness/backends/llm/sdk.py:26-30
In source order: Resolve source import import ssl; preserve alias and import-time effects. Then Resolve source import import threading; preserve alias and import-time effects. Then Resolve source import import time; preserve alias and import-time effects. Then Resolve source import from typing import TYPE_CHECKING, Any, Final, cast; preserve alias and import-time effects. Then Resolve source import from urllib.parse import urlsplit; preserve alias and import-time effects.
// Source: vvaharness/backends/llm/sdk.py:33-37
In source order: Resolve source import import anthropic; preserve alias and import-time effects. Then Resolve source import import httpx2; preserve alias and import-time effects. Then Resolve source import from pydantic import BaseModel; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import logs; preserve alias and import-time effects.
// Source: vvaharness/backends/llm/sdk.py:39-40
if (the source predicate TYPE_CHECKING is truthy) {
  // Source: vvaharness/backends/llm/sdk.py:40-40
  In source order: Resolve source import from collections.abc import Callable; preserve alias and import-time effects.
}
// Source: vvaharness/backends/llm/sdk.py:42-49
In source order: Resolve source import from vvaharness.backends.harness.deepagents.limits import MODEL_MAX_OUTPUT_TOKENS; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.models import AuthenticationError, TruncatedResponseError; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm import cache as _cache; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm import tools as _localtools; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm.cli import _truncation_error; preserve alias and import-time effects.
// Source: vvaharness/backends/llm/sdk.py:50-93
In source order: Resolve source import from vvaharness.backends.llm.models import AGENTIC_MAX_TOKENS, ANTHROPIC_STOP_REFUSAL, DEFAULT_READ_TOOLS, DEFAULT_REQUEST_TIMEOUT_SECONDS, PARAM_REJECTION_STATUS, RATE_LIMIT_TRANSIENT_RX, RESPONSE_MODEL_TOOL_NAME, RETRYABLE_STATUS, SERVER_ERROR_TRANSIENT_RX, STRUCTURED_PROSE_REASK, STRUCTURED_REASK_MAX, TRUNCATED_REPLIES_COUNTER, TRUNCATED_RETRY_ATTEMPTED_COUNTER, TRUNCATED_RETRY_RECOVERED_COUNTER, ClockKind, SdkConfig, call_timeout_error, cause_chain, effort_scaled_seconds, finish_truncated, is_gateway_wrapped_param_rejection, jittered_delay, model_refusal, note_budget_use, proxy_error, rejection_text, response_model_tool, truncation_retry_max, turn_options, wait_overrun, with_submit_instruction; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm.tls import anthropic_auth_kwargs, coerce_verify, load_client_chain, resolve_client_chain, scoped_no_proxy_env, warn_verify_disabled; preserve alias and import-time effects. Then Resolve source import from vvaharness.report.redact import redact; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import console; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import errlog as _errlog; preserve alias and import-time effects.
// Source: vvaharness/backends/llm/sdk.py:94-104
In source order: Resolve source import from vvaharness.util.counters import COUNTERS; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.events import Event; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.response_quality import StructuredOutputRejected, check_response_quality, is_timeout_failure, output_tokens_for_gate, structured_failure_detail; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.scan_progress import is_stage_only; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.tokens import TOKENS, TokenUsage, estimate_tokens; preserve alias and import-time effects.
// Source: vvaharness/backends/llm/sdk.py:105-119
In source order: Resolve source import from vvaharness.util.warn_once import warn_once; preserve alias and import-time effects. Then Evaluate once logs.get_logger(__name__); assign in source target order to log. Then Evaluate once re.compile(source_literal_110_4, re.IGNORECASE); assign in source target order to _AUTH_STATUS_RX. Then Evaluate once 3; assign in source target order to _AUTH_MAX_RETRIES_SDK. Then Evaluate once (2, 4, 8); assign in source target order to _AUTH_BACKOFF_SDK.
// Source: vvaharness/backends/llm/sdk.py:123-143
In source order: Evaluate once None; assign in source target order to _client. Then Evaluate once threading.Lock(); assign in source target order to _client_lock. Then For _client_default_betas, assign ''; source annotation str. Then For _cfg, assign {'api_key': None, 'base_url': None, 'verify_ssl': True, 'ca_cert': None, 'client_cert': None, 'no_proxy': None, 'allow_api_key_fallback': False, 'cache_min_block_tokens': None, 'cache_route': 'auto', 'cache_markers': 'on'}; source annotation SdkConfig.
// Source: vvaharness/backends/llm/sdk.py:146-186
// Source signature: configure(*, api_key: str | None=None, base_url: str | None=None, verify_ssl: bool | str | None=None, ca_cert: str | None=None, client_cert: str | tuple | None=None, no_proxy: str | None=None, allow_api_key_fallback: bool | None=None, cache_min_block_tokens: int | None=None, cache_markers: str | None=None, cache_route: str | None=None) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn configure(api_key, base_url, verify_ssl, ca_cert, client_cert, no_proxy, allow_api_key_fallback, cache_min_block_tokens, cache_markers, cache_route) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/sdk.py:155-156
  In source order: Retain source documentation literal source_literal_155_4; it is not a model call. Then Bind names in module scope: _client.
  // Source: vvaharness/backends/llm/sdk.py:157-186
  Enter source context managers left-to-right: _client_lock {
    // Source: vvaharness/backends/llm/sdk.py:158-159
    if (the source predicate api_key is truthy) {
      // Source: vvaharness/backends/llm/sdk.py:159-159
      In source order: Evaluate once api_key; assign in source target order to _cfg['api_key'].
    }
    // Source: vvaharness/backends/llm/sdk.py:160-161
    if (the source predicate base_url is truthy) {
      // Source: vvaharness/backends/llm/sdk.py:161-161
      In source order: Evaluate once base_url; assign in source target order to _cfg['base_url'].
    }
    // Source: vvaharness/backends/llm/sdk.py:162-163
    if (the source predicate allow_api_key_fallback is not None is truthy) {
      // Source: vvaharness/backends/llm/sdk.py:163-163
      In source order: Evaluate once bool(allow_api_key_fallback); assign in source target order to _cfg['allow_api_key_fallback'].
    }
    // Source: vvaharness/backends/llm/sdk.py:164-165
    if (the source predicate verify_ssl is not None is truthy) {
      // Source: vvaharness/backends/llm/sdk.py:165-165
      In source order: Evaluate once coerce_verify(verify_ssl); assign in source target order to _cfg['verify_ssl'].
    }
    // Source: vvaharness/backends/llm/sdk.py:166-167
    if (the source predicate ca_cert is truthy) {
      // Source: vvaharness/backends/llm/sdk.py:167-167
      In source order: Evaluate once ca_cert; assign in source target order to _cfg['ca_cert'].
    }
    // Source: vvaharness/backends/llm/sdk.py:168-169
    if (the source predicate client_cert is truthy) {
      // Source: vvaharness/backends/llm/sdk.py:169-169
      In source order: Evaluate once client_cert; assign in source target order to _cfg['client_cert'].
    }
    // Source: vvaharness/backends/llm/sdk.py:170-171
    if (the source predicate no_proxy is truthy) {
      // Source: vvaharness/backends/llm/sdk.py:171-171
      In source order: Evaluate once no_proxy; assign in source target order to _cfg['no_proxy'].
    }
    // Source: vvaharness/backends/llm/sdk.py:172-173
    if (the source predicate cache_min_block_tokens is not None is truthy) {
      // Source: vvaharness/backends/llm/sdk.py:173-173
      In source order: Evaluate once int(cache_min_block_tokens); assign in source target order to _cfg['cache_min_block_tokens'].
    }
    // Source: vvaharness/backends/llm/sdk.py:174-175
    if (the source predicate cache_markers is not None is truthy) {
      // Source: vvaharness/backends/llm/sdk.py:175-175
      In source order: Evaluate once cache_markers; assign in source target order to _cfg['cache_markers'].
    }
    // Source: vvaharness/backends/llm/sdk.py:176-185
    if (the source predicate cache_route is not None is truthy) {
      // Source: vvaharness/backends/llm/sdk.py:180-180
      In source order: Evaluate once 'none' if cache_route is False else str(cache_route).strip().lower(); assign in source target order to v.
      // Source: vvaharness/backends/llm/sdk.py:181-184
      if (the source predicate v not in ('auto', 'none', _ROUTE_ANTHROPIC, _ROUTE_VERTEX, _ROUTE_BEDROCK) is truthy) {
        // Source: vvaharness/backends/llm/sdk.py:183-184
        In source order: Evaluate log.warning(Event.CACHE_ROUTE_UNKNOWN, cache_route=cache_route); retain side effects and discard the expression result. Then Evaluate once 'auto'; assign in source target order to v.
      }
      // Source: vvaharness/backends/llm/sdk.py:185-185
      In source order: Evaluate once v; assign in source target order to _cfg['cache_route'].
    }
    // Source: vvaharness/backends/llm/sdk.py:186-186
    In source order: Evaluate once None; assign in source target order to _client.
  }
  Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/sdk.py:189-201
// Source signature: _mtls_verify(verify: bool | str) -> bool | str | ssl.SSLContext
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _mtls_verify(verify) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/sdk.py:190-195
  In source order: Retain source documentation literal source_literal_190_4; it is not a model call. Then Evaluate once resolve_client_chain(_cfg['client_cert'], label='sdk'); assign in source target order to client_cert.
  // Source: vvaharness/backends/llm/sdk.py:196-197
  if (the source predicate not client_cert is truthy) {
    // Source: vvaharness/backends/llm/sdk.py:197-197
    End this invocation with verify.
  }
  // Source: vvaharness/backends/llm/sdk.py:198-198
  In source order: Evaluate once httpx2.create_ssl_context(verify=verify, trust_env=True); assign in source target order to context.
  // Source: vvaharness/backends/llm/sdk.py:199-200
  if (the source predicate not load_client_chain(context, client_cert, label='sdk') is truthy) {
    // Source: vvaharness/backends/llm/sdk.py:200-200
    End this invocation with verify.
  }
  // Source: vvaharness/backends/llm/sdk.py:201-201
  End this invocation with context.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/sdk.py:204-269
// Source signature: _get_client()
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _get_client() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/sdk.py:205-205
  In source order: Bind names in module scope: _client, _client_default_betas.
  // Source: vvaharness/backends/llm/sdk.py:206-207
  if (the source predicate _client is not None is truthy) {
    // Source: vvaharness/backends/llm/sdk.py:207-207
    End this invocation with _client.
  }
  // Source: vvaharness/backends/llm/sdk.py:208-268
  Enter source context managers left-to-right: _client_lock {
    // Source: vvaharness/backends/llm/sdk.py:209-268
    if (the source predicate _client is None is truthy) {
      // Source: vvaharness/backends/llm/sdk.py:215-217
      In source order: Evaluate once {'max_retries': 2}; assign in source target order to kw. Then Evaluate once _cfg['api_key'] or os.environ.get('ANTHROPIC_SDK_API_KEY'); assign in source target order to key.
      // Source: vvaharness/backends/llm/sdk.py:218-225
      if (the source predicate not key and _cfg.get('allow_api_key_fallback') is truthy) {
        // Source: vvaharness/backends/llm/sdk.py:220-221
        In source order: Evaluate once os.environ.get('ANTHROPIC_API_KEY') or os.environ.get('ANTHROPIC_AUTH_TOKEN'); assign in source target order to key.
        // Source: vvaharness/backends/llm/sdk.py:222-225
        if (the source predicate key is truthy) {
          // Source: vvaharness/backends/llm/sdk.py:223-225
          In source order: Evaluate console.write('    [sdk] no ANTHROPIC_SDK_API_KEY — falling back to ANTHROPIC_API_KEY/ANTHROPIC_AUTH_TOKEN (sdk is the only backend)'); retain side effects and discard the expression result.
        }
      }
      // Source: vvaharness/backends/llm/sdk.py:226-238
      if (the source predicate not key is truthy) {
        // Source: vvaharness/backends/llm/sdk.py:231-238
        Raise AuthenticationError(source_literal_232_20, backend='sdk').
      }
      // Source: vvaharness/backends/llm/sdk.py:239-246
      In source order: Evaluate once anthropic_auth_kwargs(key); assign in source target order to auth_kw. Then Evaluate once str((auth_kw.get('default_headers') or {}).get('anthropic-beta') or ''); assign in source target order to _client_default_betas. Then Evaluate kw.update(auth_kw); retain side effects and discard the expression result.
      // Source: vvaharness/backends/llm/sdk.py:247-248
      if (the source predicate _cfg['base_url'] is truthy) {
        // Source: vvaharness/backends/llm/sdk.py:248-248
        In source order: Evaluate once _cfg['base_url']; assign in source target order to kw['base_url'].
      }
      // Source: vvaharness/backends/llm/sdk.py:250-250
      In source order: Evaluate once _cfg['ca_cert']; assign in source target order to ca.
      // Source: vvaharness/backends/llm/sdk.py:251-253
      if (the source predicate ca and (not os.path.exists(ca)) is truthy) {
        // Source: vvaharness/backends/llm/sdk.py:252-253
        In source order: Evaluate log.warning(Event.TLS_CA_FALLBACK, path=ca, verify_ssl=_cfg['verify_ssl']); retain side effects and discard the expression result. Then Evaluate once None; assign in source target order to ca.
      }
      // Source: vvaharness/backends/llm/sdk.py:254-254
      In source order: Evaluate once ca or _cfg['verify_ssl']; assign in source target order to verify.
      // Source: vvaharness/backends/llm/sdk.py:255-261
      if (the source predicate verify is False is truthy) {
        // Source: vvaharness/backends/llm/sdk.py:259-261
        In source order: Evaluate warn_verify_disabled(_cfg['base_url'], label='sdk', default_endpoint='<default Anthropic endpoint>', ca_hint='sdk.ca_cert'); retain side effects and discard the expression result.
      }
      // Source: vvaharness/backends/llm/sdk.py:264-264
      In source order: Evaluate once _mtls_verify(verify); assign in source target order to verify.
      // Source: vvaharness/backends/llm/sdk.py:265-266
      if (the source predicate verify is not True is truthy) {
        // Source: vvaharness/backends/llm/sdk.py:266-266
        In source order: Evaluate once anthropic.DefaultHttpxClient(verify=verify); assign in source target order to kw['http_client'].
      }
      // Source: vvaharness/backends/llm/sdk.py:267-268
      Enter source context managers left-to-right: scoped_no_proxy_env(_cfg.get('no_proxy')) {
        // Source: vvaharness/backends/llm/sdk.py:268-268
        In source order: Evaluate once anthropic.Anthropic(**kw); assign in source target order to _client.
      }
      Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    }
  }
  Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
  // Source: vvaharness/backends/llm/sdk.py:269-269
  End this invocation with _client.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/sdk.py:276-283
In source order: Evaluate once 'anthropic'; assign in source target order to _ROUTE_ANTHROPIC. Then Evaluate once 'vertex'; assign in source target order to _ROUTE_VERTEX. Then Evaluate once 'bedrock'; assign in source target order to _ROUTE_BEDROCK. Then Evaluate once 'unknown'; assign in source target order to _ROUTE_UNKNOWN. Then Evaluate once (_ROUTE_ANTHROPIC, _ROUTE_VERTEX); assign in source target order to _CACHE_CONTROL_ROUTES.
// Source: vvaharness/backends/llm/sdk.py:288-298
In source order: Evaluate once re.compile('(?:^|\\.)bedrock[a-z0-9-]*(?:\\.[a-z0-9-]+)*\\.amazonaws\\.com$', re.IGNORECASE); assign in source target order to _BEDROCK_HOST_RX. Then Evaluate once re.compile('(?:^|[.-])aiplatform\\.googleapis\\.com$', re.IGNORECASE); assign in source target order to _VERTEX_HOST_RX. Then Evaluate once re.compile('(?:^|\\.)anthropic\\.com$', re.IGNORECASE); assign in source target order to _ANTHROPIC_HOST_RX. Then For _CACHE_ROUTE_NOTED, assign set(); source annotation set[str].
// Source: vvaharness/backends/llm/sdk.py:301-348
// Source signature: _cache_route(client, *, config=None, emit_note: bool=True) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _cache_route(client, config, emit_note) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/sdk.py:302-308
  In source order: Retain source documentation literal source_literal_302_4; it is not a model call. Then Evaluate once _cfg if config is None else config; assign in source target order to settings. Then Evaluate once settings.get('cache_route', 'auto'); assign in source target order to forced.
  // Source: vvaharness/backends/llm/sdk.py:309-310
  if (the source predicate forced is False is truthy) {
    // Source: vvaharness/backends/llm/sdk.py:310-310
    In source order: Evaluate once 'none'; assign in source target order to forced.
  }
  // Source: vvaharness/backends/llm/sdk.py:311-311
  In source order: Evaluate once str(forced or 'auto').strip().lower(); assign in source target order to forced.
  // Source: vvaharness/backends/llm/sdk.py:312-313
  if (the source predicate forced == 'none' is truthy) {
    // Source: vvaharness/backends/llm/sdk.py:313-313
    End this invocation with _ROUTE_UNKNOWN.
  }
  // Source: vvaharness/backends/llm/sdk.py:314-315
  if (the source predicate forced in (_ROUTE_ANTHROPIC, _ROUTE_VERTEX, _ROUTE_BEDROCK) is truthy) {
    // Source: vvaharness/backends/llm/sdk.py:315-315
    End this invocation with forced.
  }
  // Source: vvaharness/backends/llm/sdk.py:316-318
  In source order: Evaluate once getattr(client, 'base_url', None) or settings.get('base_url') or ''; assign in source target order to base_url. Then Evaluate once urlsplit(str(base_url)).hostname or str(base_url); assign in source target order to host. Then Evaluate once (host or '').lower(); assign in source target order to host.
  // Source: vvaharness/backends/llm/sdk.py:319-320
  if (the source predicate not host is truthy) {
    // Source: vvaharness/backends/llm/sdk.py:320-320
    End this invocation with _ROUTE_ANTHROPIC.
  }
  // Source: vvaharness/backends/llm/sdk.py:321-322
  if (the source predicate _BEDROCK_HOST_RX.search(host) is truthy) {
    // Source: vvaharness/backends/llm/sdk.py:322-322
    End this invocation with _ROUTE_BEDROCK.
  }
  // Source: vvaharness/backends/llm/sdk.py:323-324
  if (the source predicate _VERTEX_HOST_RX.search(host) is truthy) {
    // Source: vvaharness/backends/llm/sdk.py:324-324
    End this invocation with _ROUTE_VERTEX.
  }
  // Source: vvaharness/backends/llm/sdk.py:325-326
  if (the source predicate _ANTHROPIC_HOST_RX.search(host) is truthy) {
    // Source: vvaharness/backends/llm/sdk.py:326-326
    End this invocation with _ROUTE_ANTHROPIC.
  }
  // Source: vvaharness/backends/llm/sdk.py:337-338
  if (the source predicate not emit_note is truthy) {
    // Source: vvaharness/backends/llm/sdk.py:338-338
    End this invocation with _ROUTE_UNKNOWN.
  }
  // Source: vvaharness/backends/llm/sdk.py:339-347
  In source order: Evaluate warn_once(_CACHE_ROUTE_NOTED, _ROUTE_UNKNOWN, source_literal_341_8); retain side effects and discard the expression result.
  // Source: vvaharness/backends/llm/sdk.py:348-348
  End this invocation with _ROUTE_UNKNOWN.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/sdk.py:351-353
// Source signature: _cache_markers_enabled() -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _cache_markers_enabled() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/sdk.py:352-352
  In source order: Retain source documentation literal source_literal_352_4; it is not a model call.
  // Source: vvaharness/backends/llm/sdk.py:353-353
  End this invocation with _cache.markers_enabled(_cfg).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/sdk.py:361-368
In source order: For _CACHE_MIN_TOKENS_TABLE, assign ((re.compile('opus-5|fable-5', re.IGNORECASE), 512), (re.compile('opus-4[-.]?[56]|haiku-4[-.]?5', re.IGNORECASE), 4096), (re.compile('opus-4[-.]?7|haiku-3[-.]?5', re.IGNORECASE), 2048), (re.compile('opus-4|sonnet-[45]', re.IGNORECASE), 1024)); source annotation tuple[tuple[re.Pattern, int], ...]. Then Evaluate once 4096; assign in source target order to _CACHE_MIN_TOKENS_FALLBACK.
// Source: vvaharness/backends/llm/sdk.py:371-381
// Source signature: _cache_min_tokens_for(model: str) -> int
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _cache_min_tokens_for(model) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/sdk.py:372-373
  In source order: Retain source documentation literal source_literal_372_4; it is not a model call. Then Evaluate once _cfg.get('cache_min_block_tokens'); assign in source target order to override.
  // Source: vvaharness/backends/llm/sdk.py:374-377
  if (the source predicate override is not None is truthy) {
    // Source: vvaharness/backends/llm/sdk.py:377-377
    End this invocation with max(0, int(override)).
  }
  // Source: vvaharness/backends/llm/sdk.py:378-380
  for each (rx, floor) in _CACHE_MIN_TOKENS_TABLE {
    // Source: vvaharness/backends/llm/sdk.py:379-380
    if (the source predicate rx.search(model or '') is truthy) {
      // Source: vvaharness/backends/llm/sdk.py:380-380
      End this invocation with floor.
    }
  }
  // Source: vvaharness/backends/llm/sdk.py:381-381
  End this invocation with _CACHE_MIN_TOKENS_FALLBACK.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/sdk.py:385-385
In source order: Evaluate once _cache.CACHE_EST_MARGIN; assign in source target order to _CACHE_EST_MARGIN.
// Source: vvaharness/backends/llm/sdk.py:388-393
// Source signature: _cache_prefix_meets_minimum(text: str, model: str, *, preceding: str='') -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _cache_prefix_meets_minimum(text, model, preceding) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/sdk.py:390-392
  In source order: Retain source documentation literal source_literal_390_4; it is not a model call. Then Evaluate once _cache_min_tokens_for(model); assign in source target order to floor. Then Evaluate once estimate_tokens(preceding) + estimate_tokens(text); assign in source target order to est.
  // Source: vvaharness/backends/llm/sdk.py:393-393
  End this invocation with est * _CACHE_EST_MARGIN >= floor.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/sdk.py:396-435
// Source signature: _build_cache_prefix_content(client, cache_prefix: str | None, user_prompt: str | list[dict], *, model: str, preceding: str='') -> str | list[dict]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _build_cache_prefix_content(client, cache_prefix, user_prompt, model, preceding) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/sdk.py:400-400
  In source order: Retain source documentation literal source_literal_400_4; it is not a model call.
  // Source: vvaharness/backends/llm/sdk.py:404-405
  if (the source predicate not cache_prefix is truthy) {
    // Source: vvaharness/backends/llm/sdk.py:405-405
    End this invocation with user_prompt.
  }
  // Source: vvaharness/backends/llm/sdk.py:407-407
  In source order: Evaluate once None; assign in source target order to route.
  // Source: vvaharness/backends/llm/sdk.py:408-413
  if (the source predicate _cache_markers_enabled() is truthy) {
    // Source: vvaharness/backends/llm/sdk.py:409-409
    In source order: Evaluate once _cache_route(client); assign in source target order to candidate.
    // Source: vvaharness/backends/llm/sdk.py:410-413
    if (the source predicate candidate in _CACHE_CONTROL_ROUTES and _cache_prefix_meets_minimum(cache_prefix, model, preceding=preceding) is truthy) {
      // Source: vvaharness/backends/llm/sdk.py:413-413
      In source order: Evaluate once candidate; assign in source target order to route.
    }
  }
  // Source: vvaharness/backends/llm/sdk.py:417-421
  if (the source predicate isinstance(user_prompt, list) is truthy) {
    // Source: vvaharness/backends/llm/sdk.py:418-418
    In source order: For prefix_block, assign {'type': 'text', 'text': cache_prefix}; source annotation dict.
    // Source: vvaharness/backends/llm/sdk.py:419-420
    if (the source predicate route is not None and user_prompt is truthy) {
      // Source: vvaharness/backends/llm/sdk.py:420-420
      In source order: Evaluate once {'type': 'ephemeral'}; assign in source target order to prefix_block['cache_control'].
    }
    // Source: vvaharness/backends/llm/sdk.py:421-421
    End this invocation with [prefix_block, *user_prompt].
  }
  // Source: vvaharness/backends/llm/sdk.py:425-430
  if (the source predicate route is not None and user_prompt is truthy) {
    // Source: vvaharness/backends/llm/sdk.py:426-430
    End this invocation with [{'type': 'text', 'text': cache_prefix, 'cache_control': {'type': 'ephemeral'}}, {'type': 'text', 'text': user_prompt}].
  }
  // Source: vvaharness/backends/llm/sdk.py:435-435
  End this invocation with cache_prefix + user_prompt.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/sdk.py:438-455
// Source signature: _build_system_content(client, system_prompt: str, model: str, *, tools_text: str='') -> str | list[dict]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _build_system_content(client, system_prompt, model, tools_text) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/sdk.py:440-440
  In source order: Retain source documentation literal source_literal_440_4; it is not a model call.
  // Source: vvaharness/backends/llm/sdk.py:446-454
  if (the source predicate _cache_markers_enabled() and _cache_route(client) in _CACHE_CONTROL_ROUTES and _cache_prefix_meets_minimum(system_prompt, model, preceding=tools_text) is truthy) {
    // Source: vvaharness/backends/llm/sdk.py:450-454
    End this invocation with [{'type': 'text', 'text': system_prompt, 'cache_control': {'type': 'ephemeral'}}].
  }
  // Source: vvaharness/backends/llm/sdk.py:455-455
  End this invocation with system_prompt.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/sdk.py:458-458
In source order: Evaluate once _cache.ANTHROPIC_PARSED_CACHE_KEYS; assign in source target order to _PARSED_USAGE_CACHE_KEYS.
// Source: vvaharness/backends/llm/sdk.py:461-463
// Source signature: _note_unparsed_cache_keys(usage: dict | None) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _note_unparsed_cache_keys(usage) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/sdk.py:462-463
  In source order: Retain source documentation literal source_literal_462_4; it is not a model call. Then Evaluate _cache.note_unparsed_cache_keys(usage, via='sdk'); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/sdk.py:466-471
// Source signature: _bank_usage(msg: anthropic.types.Message) -> TokenUsage | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _bank_usage(msg) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/sdk.py:467-470
  In source order: Retain source documentation literal source_literal_467_4; it is not a model call. Then Evaluate once cast('TokenUsage', msg.usage.model_dump()) if msg.usage else None; assign in source target order to usage. Then Evaluate _note_unparsed_cache_keys(usage); retain side effects and discard the expression result. Then Evaluate TOKENS.add(usage); retain side effects and discard the expression result.
  // Source: vvaharness/backends/llm/sdk.py:471-471
  End this invocation with usage.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/sdk.py:477-486
In source order: For _ATTEMPTS_CEILING, assign 6; source annotation Final. Then For _NO_TEMP_MODELS, assign set(); source annotation set[str]. Then For _NO_THINK_MODELS, assign set(); source annotation set[str]. Then For _NO_TOOL_CHOICE_MODELS, assign set(); source annotation set[str]. Then For _WARNED_DROPS, assign set(); source annotation set[str].
// Source: vvaharness/backends/llm/sdk.py:487-490
In source order: Evaluate once re.compile('opus-4[-.]?([7-9]|\\d{2,})|opus-[5-9]|sonnet-[5-9]|haiku-[5-9]', re.IGNORECASE); assign in source target order to _NO_TEMP_RX.
// Source: vvaharness/backends/llm/sdk.py:493-506
// Source signature: _warn_max_budget_unenforced(fn: str, max_budget_usd: float | None) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _warn_max_budget_unenforced(fn, max_budget_usd) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/sdk.py:494-494
  In source order: Retain source documentation literal source_literal_494_4; it is not a model call.
  // Source: vvaharness/backends/llm/sdk.py:499-500
  if (the source predicate max_budget_usd is None is truthy) {
    // Source: vvaharness/backends/llm/sdk.py:500-500
    End this invocation with None.
  }
  // Source: vvaharness/backends/llm/sdk.py:501-506
  In source order: Evaluate warn_once(_WARNED_DROPS, source_template_502_23, source_template_503_8); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/sdk.py:509-512
// Source signature: _supports_temperature(model: str) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _supports_temperature(model) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/sdk.py:510-511
  if (the source predicate model in _NO_TEMP_MODELS is truthy) {
    // Source: vvaharness/backends/llm/sdk.py:511-511
    End this invocation with False.
  }
  // Source: vvaharness/backends/llm/sdk.py:512-512
  End this invocation with not _NO_TEMP_RX.search(model).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/sdk.py:515-527
// Source signature: _beta_headers(betas: list[str] | None) -> dict[str, str] | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _beta_headers(betas) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/sdk.py:516-516
  In source order: Retain source documentation literal source_literal_516_4; it is not a model call.
  // Source: vvaharness/backends/llm/sdk.py:521-522
  if (the source predicate not betas is truthy) {
    // Source: vvaharness/backends/llm/sdk.py:522-522
    End this invocation with None.
  }
  // Source: vvaharness/backends/llm/sdk.py:523-523
  In source order: Evaluate once [b for b in _client_default_betas.split(',') if b.strip()]; assign in source target order to joined.
  // Source: vvaharness/backends/llm/sdk.py:524-526
  for each b in betas {
    // Source: vvaharness/backends/llm/sdk.py:525-526
    if (the source predicate str(b) not in joined is truthy) {
      // Source: vvaharness/backends/llm/sdk.py:526-526
      In source order: Evaluate joined.append(str(b)); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/backends/llm/sdk.py:527-527
  End this invocation with {'anthropic-beta': ','.join(joined)}.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/sdk.py:530-549
// Source signature: _is_transient_sdk(error: anthropic.APIStatusError) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _is_transient_sdk(error) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/sdk.py:531-531
  In source order: Retain source documentation literal source_literal_531_4; it is not a model call.
  // Source: vvaharness/backends/llm/sdk.py:536-537
  if (the source predicate error.status_code in RETRYABLE_STATUS is truthy) {
    // Source: vvaharness/backends/llm/sdk.py:537-537
    End this invocation with True.
  }
  // Source: vvaharness/backends/llm/sdk.py:543-544
  if (the source predicate error.status_code in (401, 403) is truthy) {
    // Source: vvaharness/backends/llm/sdk.py:544-544
    End this invocation with False.
  }
  // Source: vvaharness/backends/llm/sdk.py:547-547
  In source order: Evaluate once rejection_text(error); assign in source target order to body.
  // Source: vvaharness/backends/llm/sdk.py:548-549
  End this invocation with bool(RATE_LIMIT_TRANSIENT_RX.search(body) or SERVER_ERROR_TRANSIENT_RX.search(body)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/sdk.py:556-557
In source order: Evaluate once RESPONSE_MODEL_TOOL_NAME; assign in source target order to _RESPONSE_MODEL_TOOL_NAME. Then Evaluate once response_model_tool; assign in source target order to _response_model_tool.
// Source: vvaharness/backends/llm/sdk.py:560-581
// Source signature: _extract_response_model(response_model: type[BaseModel], msg, *, model: str) -> BaseModel
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _extract_response_model(response_model, msg, model) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/sdk.py:561-566
  In source order: Retain source documentation literal source_literal_561_4; it is not a model call. Then Evaluate once getattr(msg, 'stop_reason', None); assign in source target order to finish.
  // Source: vvaharness/backends/llm/sdk.py:567-577
  for each b in msg.content {
    // Source: vvaharness/backends/llm/sdk.py:568-569
    if (the source predicate getattr(b, 'type', None) != 'tool_use' is truthy) {
      // Source: vvaharness/backends/llm/sdk.py:569-569
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/backends/llm/sdk.py:570-577
    if (the source predicate b.name == _RESPONSE_MODEL_TOOL_NAME is truthy) {
      // Source: vvaharness/backends/llm/sdk.py:571-577
      Perform the following protected operations {
        // Source: vvaharness/backends/llm/sdk.py:572-572
        End this invocation with response_model.model_validate(b.input).
      }
      // Source: vvaharness/backends/llm/sdk.py:573-577
      On the first matching source exception Exception as e, in handler order {
        // Source: vvaharness/backends/llm/sdk.py:574-577
        Raise StructuredOutputRejected(source_template_575_20, finish=finish) with explicit source cause e.
      }
    }
  }
  // Source: vvaharness/backends/llm/sdk.py:578-581
  Raise StructuredOutputRejected(source_template_579_8, finish=finish).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/sdk.py:584-588
// Source signature: _refusal_category(msg: anthropic.types.Message) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _refusal_category(msg) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/sdk.py:585-587
  In source order: Retain source documentation literal source_literal_585_4; it is not a model call. Then Evaluate once getattr(getattr(msg, 'stop_details', None), 'category', None); assign in source target order to category.
  // Source: vvaharness/backends/llm/sdk.py:588-588
  End this invocation with category if isinstance(category, str) else None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/sdk.py:591-594
// Source signature: _raise_if_refused(msg: anthropic.types.Message, *, tag: str | None) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _raise_if_refused(msg, tag) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/sdk.py:592-592
  In source order: Retain source documentation literal source_literal_592_4; it is not a model call.
  // Source: vvaharness/backends/llm/sdk.py:593-594
  if (the source predicate getattr(msg, 'stop_reason', None) == ANTHROPIC_STOP_REFUSAL is truthy) {
    // Source: vvaharness/backends/llm/sdk.py:594-594
    Raise model_refusal(route='sdk', stage=tag or '', category=_refusal_category(msg)).
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/sdk.py:597-608
// Source signature: _effort_thinking_kwargs(model: str, effort: str | None) -> dict
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _effort_thinking_kwargs(model, effort) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/sdk.py:598-598
  In source order: Retain source documentation literal source_literal_598_4; it is not a model call.
  // Source: vvaharness/backends/llm/sdk.py:603-604
  if (the source predicate effort is None or model in _NO_THINK_MODELS is truthy) {
    // Source: vvaharness/backends/llm/sdk.py:604-604
    End this invocation with {}.
  }
  // Source: vvaharness/backends/llm/sdk.py:605-607
  In source order: Resolve source import from vvaharness.backends.harness.deepagents.options.model_building import _anthropic_thinking_kwargs; preserve alias and import-time effects.
  // Source: vvaharness/backends/llm/sdk.py:608-608
  End this invocation with _anthropic_thinking_kwargs(effort).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/sdk.py:611-617
// Source signature: _forcing_blocked(model: str, thinking: dict | None) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _forcing_blocked(model, thinking) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/sdk.py:612-612
  In source order: Retain source documentation literal source_literal_612_4; it is not a model call.
  // Source: vvaharness/backends/llm/sdk.py:617-617
  End this invocation with model in _NO_TOOL_CHOICE_MODELS or (thinking or {}).get('type') == 'enabled'.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/sdk.py:620-631
// Source signature: _warn_tool_choice_dropped_for_thinking(model: str, effort: str | None) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _warn_tool_choice_dropped_for_thinking(model, effort) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/sdk.py:621-631
  In source order: Retain source documentation literal source_literal_621_4; it is not a model call. Then Evaluate warn_once(_WARNED_DROPS, source_template_623_23, source_template_624_8); retain side effects and discard the expression result. Then Evaluate COUNTERS.bump('sdk_tool_choice_dropped_for_thinking'); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/sdk.py:634-660
// Source signature: _unforce_rejected_tool_choice(kw: dict, e: anthropic.APIStatusError, low: str, *, client, model: str, system_prompt: str | None, response_model: type[BaseModel] | None, tools_text: str='') -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _unforce_rejected_tool_choice(kw, e, low, client, model, system_prompt, response_model, tools_text) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/sdk.py:638-638
  In source order: Retain source documentation literal source_literal_638_4; it is not a model call.
  // Source: vvaharness/backends/llm/sdk.py:643-646
  if (the source predicate not ('tool_choice' in kw and 'tool_choice' in low and (e.status_code in PARAM_REJECTION_STATUS or is_gateway_wrapped_param_rejection(e))) is truthy) {
    // Source: vvaharness/backends/llm/sdk.py:646-646
    End this invocation with False.
  }
  // Source: vvaharness/backends/llm/sdk.py:647-654
  In source order: Evaluate _NO_TOOL_CHOICE_MODELS.add(model); retain side effects and discard the expression result. Then Evaluate warn_once(_WARNED_DROPS, source_template_649_23, source_template_650_8); retain side effects and discard the expression result. Then Evaluate kw.pop('tool_choice', None); retain side effects and discard the expression result.
  // Source: vvaharness/backends/llm/sdk.py:655-659
  if (the source predicate response_model is not None is truthy) {
    // Source: vvaharness/backends/llm/sdk.py:657-659
    In source order: Evaluate once _build_system_content(client, with_submit_instruction(system_prompt, response_model), model, tools_text=tools_text); assign in source target order to kw['system'].
  }
  // Source: vvaharness/backends/llm/sdk.py:660-660
  End this invocation with True.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/sdk.py:663-675
// Source signature: _reforce_tool_choice(kw: dict, tool_choice: dict, *, client, model: str, system_prompt: str | None, response_model: type[BaseModel] | None, tools_text: str='') -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _reforce_tool_choice(kw, tool_choice, client, model, system_prompt, response_model, tools_text) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/sdk.py:667-667
  In source order: Retain source documentation literal source_literal_667_4; it is not a model call.
  // Source: vvaharness/backends/llm/sdk.py:669-670
  if (the source predicate response_model is None or model in _NO_TOOL_CHOICE_MODELS is truthy) {
    // Source: vvaharness/backends/llm/sdk.py:670-670
    End this invocation with None.
  }
  // Source: vvaharness/backends/llm/sdk.py:671-671
  In source order: Evaluate once tool_choice; assign in source target order to kw['tool_choice'].
  // Source: vvaharness/backends/llm/sdk.py:672-675
  if (the source predicate system_prompt is truthy) {
    // Source: vvaharness/backends/llm/sdk.py:673-673
    In source order: Evaluate once _build_system_content(client, system_prompt, model, tools_text=tools_text); assign in source target order to kw['system'].
  }
  else {
    // Source: vvaharness/backends/llm/sdk.py:675-675
    In source order: Evaluate kw.pop('system', None); retain side effects and discard the expression result.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/sdk.py:678-988
// Source signature: prompt(user_prompt: str | list[dict], *, model: str, cache_prefix: str | None=None, system_prompt: str | None=None, max_tokens: int | None=None, temperature: float | None=None, thinking_budget: int | None=None, betas: list[str] | None=None, json_schema: dict | None=None, output_format: str='text', cwd: str | None=None, max_budget_usd: float | None=None, timeout: int | None=None, tag: str | None=None, response_model: type[BaseModel] | None=None, effort: str | None=None) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn prompt(user_prompt, model, cache_prefix, system_prompt, max_tokens, temperature, thinking_budget, betas, json_schema, output_format, cwd, max_budget_usd, timeout, tag, response_model, effort) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/sdk.py:699-706
  In source order: Evaluate _warn_max_budget_unenforced('prompt', max_budget_usd); retain side effects and discard the expression result. Then Evaluate once _get_client(); assign in source target order to client. Then Evaluate once max_tokens or 16000; assign in source target order to max_tok. Then Evaluate once _effort_thinking_kwargs(model, effort); assign in source target order to effort_kw. Then Evaluate once response_model is not None and (not _forcing_blocked(model, effort_kw.get('thinking'))); assign in source target order to forced.
  // Source: vvaharness/backends/llm/sdk.py:708-708
  In source order: Evaluate once system_prompt; assign in source target order to system_text.
  // Source: vvaharness/backends/llm/sdk.py:709-712
  if (the source predicate response_model is not None and (not forced) is truthy) {
    // Source: vvaharness/backends/llm/sdk.py:712-712
    In source order: Evaluate once with_submit_instruction(system_prompt, response_model); assign in source target order to system_text.
  }
  // Source: vvaharness/backends/llm/sdk.py:717-728
  In source order: Evaluate once _build_cache_prefix_content(client, cache_prefix, user_prompt, model=model, preceding=system_text or ''); assign in source target order to user_content. Then For kw, assign {'model': model, 'max_tokens': max_tok, 'messages': [{'role': 'user', 'content': user_content}]}; source annotation dict.
  // Source: vvaharness/backends/llm/sdk.py:729-734
  if (the source predicate response_model is not None is truthy) {
    // Source: vvaharness/backends/llm/sdk.py:730-730
    In source order: Evaluate once [_response_model_tool(response_model)]; assign in source target order to kw['tools'].
    // Source: vvaharness/backends/llm/sdk.py:731-734
    if (the source predicate forced is truthy) {
      // Source: vvaharness/backends/llm/sdk.py:732-732
      In source order: Evaluate once {'type': 'tool', 'name': _RESPONSE_MODEL_TOOL_NAME}; assign in source target order to kw['tool_choice'].
    }
    else {
      // Source: vvaharness/backends/llm/sdk.py:733-734
      if (the source predicate model not in _NO_TOOL_CHOICE_MODELS is truthy) {
        // Source: vvaharness/backends/llm/sdk.py:734-734
        In source order: Evaluate _warn_tool_choice_dropped_for_thinking(model, effort); retain side effects and discard the expression result.
      }
    }
  }
  // Source: vvaharness/backends/llm/sdk.py:737-737
  In source order: Evaluate once _beta_headers(betas); assign in source target order to beta_headers.
  // Source: vvaharness/backends/llm/sdk.py:738-739
  if (the source predicate beta_headers is truthy) {
    // Source: vvaharness/backends/llm/sdk.py:739-739
    In source order: Evaluate once beta_headers; assign in source target order to kw['extra_headers'].
  }
  // Source: vvaharness/backends/llm/sdk.py:740-748
  if (the source predicate thinking_budget and model not in _NO_THINK_MODELS is truthy) {
    // Source: vvaharness/backends/llm/sdk.py:744-746
    if (the source predicate max_tok <= thinking_budget is truthy) {
      // Source: vvaharness/backends/llm/sdk.py:745-746
      In source order: Evaluate once thinking_budget + 8000; assign in source target order to max_tok. Then Evaluate once max_tok; assign in source target order to kw['max_tokens'].
    }
    // Source: vvaharness/backends/llm/sdk.py:747-748
    In source order: Evaluate once {'type': 'adaptive'}; assign in source target order to kw['thinking']. Then Evaluate once None; assign in source target order to temperature.
  }
  // Source: vvaharness/backends/llm/sdk.py:749-752
  if (the source predicate effort_kw is truthy) {
    // Source: vvaharness/backends/llm/sdk.py:751-752
    In source order: Evaluate kw.update(effort_kw); retain side effects and discard the expression result. Then Evaluate once None; assign in source target order to temperature.
  }
  // Source: vvaharness/backends/llm/sdk.py:753-759
  if (the source predicate temperature is not None is truthy) {
    // Source: vvaharness/backends/llm/sdk.py:754-759
    if (the source predicate _supports_temperature(model) is truthy) {
      // Source: vvaharness/backends/llm/sdk.py:755-755
      In source order: Evaluate once temperature; assign in source target order to kw.setdefault('extra_body', {})['temperature'].
    }
    else {
      // Source: vvaharness/backends/llm/sdk.py:756-759
      if (the source predicate model not in _NO_TEMP_MODELS is truthy) {
        // Source: vvaharness/backends/llm/sdk.py:757-759
        In source order: Evaluate _NO_TEMP_MODELS.add(model); retain side effects and discard the expression result. Then Evaluate console.write(source_template_758_26); retain side effects and discard the expression result.
      }
    }
  }
  // Source: vvaharness/backends/llm/sdk.py:760-763
  if (the source predicate system_text is truthy) {
    // Source: vvaharness/backends/llm/sdk.py:763-763
    In source order: Evaluate once _build_system_content(client, system_text, model); assign in source target order to kw['system'].
  }
  // Source: vvaharness/backends/llm/sdk.py:767-783
  In source order: Evaluate once effort_scaled_seconds(timeout or DEFAULT_REQUEST_TIMEOUT_SECONDS, effort, kind=ClockKind.REQUEST); assign in source target order to request_timeout. Then Evaluate once sum((len(b.get('text', '')) for b in user_prompt if isinstance(b, dict))) if isinstance(user_prompt, list) else len(user_prompt); assign in source target order to _up_chars. Then Evaluate console.write(source_template_774_18); retain side effects and discard the expression result. Then Evaluate once time.monotonic(); assign in source target order to session_t0. Then Evaluate once request_timeout; assign in source target order to session_budget.
  // Source: vvaharness/backends/llm/sdk.py:785-790
  In source order: Evaluate once (3, 60); assign in source target order to (attempts, retry_wait). Then Evaluate once 0; assign in source target order to auth_attempt. Then Evaluate once None; assign in source target order to msg. Then Evaluate once False; assign in source target order to trunc_retried. Then Evaluate once 0; assign in source target order to trunc_retry_at.
  // Source: vvaharness/backends/llm/sdk.py:792-792
  In source order: Evaluate once 0; assign in source target order to attempt.
  // Source: vvaharness/backends/llm/sdk.py:793-958
  while (the source predicate attempt < attempts is truthy) {
    // Source: vvaharness/backends/llm/sdk.py:794-794
    In source order: Apply source augmented assignment attempt += 1 with source evaluation/in-place semantics.
    // Source: vvaharness/backends/llm/sdk.py:795-958
    Perform the following protected operations {
      // Source: vvaharness/backends/llm/sdk.py:797-799
      In source order: Evaluate once time.monotonic(); assign in source target order to _t0. Then Evaluate once turn_options(session_t0, session_budget, request_timeout); assign in source target order to send. Then Evaluate once client.with_options(**send); assign in source target order to stream_client.
      // Source: vvaharness/backends/llm/sdk.py:800-803
      Enter source context managers left-to-right: stream_client.messages.stream(**kw) bound to stream {
        // Source: vvaharness/backends/llm/sdk.py:801-803
        In source order: Evaluate once _drain_within_deadline(stream, deadline=_t0 + send['timeout'], stage=tag, effort=effort, budget_s=request_timeout); assign in source target order to msg.
      }
      Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
      // Source: vvaharness/backends/llm/sdk.py:804-804
      In source order: Evaluate note_budget_use(time.monotonic() - _t0, request_timeout, effort); retain side effects and discard the expression result.
      // Source: vvaharness/backends/llm/sdk.py:805-834
      if (the source predicate finish_truncated(msg.stop_reason) is truthy) {
        // Source: vvaharness/backends/llm/sdk.py:809-813
        In source order: Evaluate once _bank_usage(msg); assign in source target order to clipped_usage. Then Evaluate once clipped_usage.get('output_tokens') if clipped_usage else None; assign in source target order to produced. Then Evaluate once kw['max_tokens']; assign in source target order to requested_now. Then Evaluate once None if trunc_retried else truncation_retry_max(requested_now, cap=MODEL_MAX_OUTPUT_TOKENS); assign in source target order to retry_at.
        // Source: vvaharness/backends/llm/sdk.py:814-832
        if (the source predicate retry_at is not None is truthy) {
          // Source: vvaharness/backends/llm/sdk.py:816-817
          if (the source predicate attempt == attempts and attempts < _ATTEMPTS_CEILING is truthy) {
            // Source: vvaharness/backends/llm/sdk.py:817-817
            In source order: Apply source augmented assignment attempts += 1 with source evaluation/in-place semantics.
          }
          // Source: vvaharness/backends/llm/sdk.py:818-832
          if (the source predicate attempt < attempts is truthy) {
            // Source: vvaharness/backends/llm/sdk.py:819-830
            In source order: Evaluate once (True, retry_at); assign in source target order to (trunc_retried, trunc_retry_at). Then Evaluate COUNTERS.bump(TRUNCATED_RETRY_ATTEMPTED_COUNTER); retain side effects and discard the expression result. Then Evaluate log.warning(Event.TRUNCATED_RETRY, route='sdk', stop_reason=msg.stop_reason, budget=requested_now, retry_at=retry_at); retain side effects and discard the expression result. Then Evaluate _errlog.log(tag or 'sdk', tag or 'truncation', source_template_825_28, error_code=TruncatedResponseError.error_code, recovered=True, produced=produced); retain side effects and discard the expression result. Then Evaluate once retry_at; assign in source target order to kw['max_tokens'].
            // Source: vvaharness/backends/llm/sdk.py:831-831
            In source order: Evaluate once None; assign in source target order to msg.
            // Source: vvaharness/backends/llm/sdk.py:832-832
            Continue the immediately enclosing source loop at its next iteration.
          }
        }
        // Source: vvaharness/backends/llm/sdk.py:833-834
        Raise _truncation_error(requested=max_tok, retried=trunc_retry_at, tag=tag, retry_at=retry_at, produced=produced).
      }
      // Source: vvaharness/backends/llm/sdk.py:835-836
      if (the source predicate trunc_retried is truthy) {
        // Source: vvaharness/backends/llm/sdk.py:836-836
        In source order: Evaluate COUNTERS.bump(TRUNCATED_RETRY_RECOVERED_COUNTER); retain side effects and discard the expression result.
      }
      // Source: vvaharness/backends/llm/sdk.py:837-837
      Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
    }
    // Source: vvaharness/backends/llm/sdk.py:838-934
    On the first matching source exception anthropic.APIStatusError as e, in handler order {
      // Source: vvaharness/backends/llm/sdk.py:839-840
      In source order: Evaluate once str(getattr(e, 'message', e)); assign in source target order to body. Then Evaluate once rejection_text(e).lower(); assign in source target order to low.
      // Source: vvaharness/backends/llm/sdk.py:841-849
      if (the source predicate 'temperature' in kw.get('extra_body', {}) and 'temperature' in low and (e.status_code in PARAM_REJECTION_STATUS) is truthy) {
        // Source: vvaharness/backends/llm/sdk.py:843-846
        In source order: Evaluate _NO_TEMP_MODELS.add(model); retain side effects and discard the expression result. Then Evaluate console.write(source_template_844_30); retain side effects and discard the expression result. Then Evaluate kw.get('extra_body', {}).pop('temperature', None); retain side effects and discard the expression result.
        // Source: vvaharness/backends/llm/sdk.py:847-848
        if (the source predicate attempt == attempts and attempts < _ATTEMPTS_CEILING is truthy) {
          // Source: vvaharness/backends/llm/sdk.py:848-848
          In source order: Apply source augmented assignment attempts += 1 with source evaluation/in-place semantics.
        }
        // Source: vvaharness/backends/llm/sdk.py:849-849
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/backends/llm/sdk.py:854-859
      if (the source predicate _unforce_rejected_tool_choice(kw, e, low, client=client, model=model, system_prompt=system_prompt, response_model=response_model) is truthy) {
        // Source: vvaharness/backends/llm/sdk.py:857-858
        if (the source predicate attempt == attempts and attempts < _ATTEMPTS_CEILING is truthy) {
          // Source: vvaharness/backends/llm/sdk.py:858-858
          In source order: Apply source augmented assignment attempts += 1 with source evaluation/in-place semantics.
        }
        // Source: vvaharness/backends/llm/sdk.py:859-859
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/backends/llm/sdk.py:860-888
      if (the source predicate 'thinking' in kw and 'thinking' in low and (e.status_code in PARAM_REJECTION_STATUS) is truthy) {
        // Source: vvaharness/backends/llm/sdk.py:869-871
        In source order: Evaluate once 'not supported' in low or 'unexpected' in low or 'adaptive' in low or ('unrecognized' in low) or ('unknown' in low); assign in source target order to unsupported.
        // Source: vvaharness/backends/llm/sdk.py:872-873
        if (the source predicate unsupported is truthy) {
          // Source: vvaharness/backends/llm/sdk.py:873-873
          In source order: Evaluate _NO_THINK_MODELS.add(model); retain side effects and discard the expression result.
        }
        // Source: vvaharness/backends/llm/sdk.py:874-877
        In source order: Evaluate console.write(source_template_874_30); retain side effects and discard the expression result. Then Evaluate kw.pop('thinking', None); retain side effects and discard the expression result.
        // Source: vvaharness/backends/llm/sdk.py:878-885
        if (the source predicate effort_kw is truthy) {
          // Source: vvaharness/backends/llm/sdk.py:881-885
          In source order: Evaluate kw.pop('output_config', None); retain side effects and discard the expression result. Then Evaluate _reforce_tool_choice(kw, {'type': 'tool', 'name': _RESPONSE_MODEL_TOOL_NAME}, client=client, model=model, system_prompt=system_prompt, response_model=response_model); retain side effects and discard the expression result.
        }
        // Source: vvaharness/backends/llm/sdk.py:886-887
        if (the source predicate attempt == attempts and attempts < _ATTEMPTS_CEILING is truthy) {
          // Source: vvaharness/backends/llm/sdk.py:887-887
          In source order: Apply source augmented assignment attempts += 1 with source evaluation/in-place semantics.
        }
        // Source: vvaharness/backends/llm/sdk.py:888-888
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/backends/llm/sdk.py:897-919
      if (the source predicate _auth_failure_sdk(e) is truthy) {
        // Source: vvaharness/backends/llm/sdk.py:902-914
        if (the source predicate auth_attempt < _AUTH_MAX_RETRIES_SDK and attempt < attempts is truthy) {
          // Source: vvaharness/backends/llm/sdk.py:903-904
          In source order: Evaluate once _AUTH_BACKOFF_SDK[min(auth_attempt, len(_AUTH_BACKOFF_SDK) - 1)]; assign in source target order to wait.
          // Source: vvaharness/backends/llm/sdk.py:905-907
          if (the source predicate (overrun := wait_overrun(wait, session_t0, session_budget, stage=tag or '', route='sdk', effort=effort)) is truthy) {
            // Source: vvaharness/backends/llm/sdk.py:907-907
            Raise overrun with explicit source cause e.
          }
          // Source: vvaharness/backends/llm/sdk.py:908-913
          In source order: Evaluate console.write(source_template_908_34); retain side effects and discard the expression result. Then Evaluate time.sleep(wait); retain side effects and discard the expression result. Then Apply source augmented assignment auth_attempt += 1 with source evaluation/in-place semantics.
          // Source: vvaharness/backends/llm/sdk.py:914-914
          Continue the immediately enclosing source loop at its next iteration.
        }
        // Source: vvaharness/backends/llm/sdk.py:917-919
        Raise AuthenticationError(redact(body)[:400], status_code=e.status_code, backend='sdk') with explicit source cause e.
      }
      // Source: vvaharness/backends/llm/sdk.py:920-929
      if (the source predicate _is_transient_sdk(e) and attempt < attempts is truthy) {
        // Source: vvaharness/backends/llm/sdk.py:921-921
        In source order: Evaluate once jittered_delay(retry_wait); assign in source target order to wait.
        // Source: vvaharness/backends/llm/sdk.py:922-924
        if (the source predicate (overrun := wait_overrun(wait, session_t0, session_budget, stage=tag or '', route='sdk', effort=effort)) is truthy) {
          // Source: vvaharness/backends/llm/sdk.py:924-924
          Raise overrun with explicit source cause e.
        }
        // Source: vvaharness/backends/llm/sdk.py:925-928
        In source order: Evaluate console.write(source_template_925_30); retain side effects and discard the expression result. Then Evaluate time.sleep(wait); retain side effects and discard the expression result.
        // Source: vvaharness/backends/llm/sdk.py:929-929
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/backends/llm/sdk.py:931-934
      Raise RuntimeError(source_template_932_16) with explicit source cause e.
    }
    // Source: vvaharness/backends/llm/sdk.py:935-958
    On the first matching source exception (anthropic.APIConnectionError, httpx2.TransportError) as e, in handler order {
      // Source: vvaharness/backends/llm/sdk.py:936-939
      if (the source predicate is_timeout_failure(e) is truthy) {
        // Source: vvaharness/backends/llm/sdk.py:937-939
        Raise call_timeout_error(stage=tag or '', route='sdk', budget_s=request_timeout, effort=effort, cause_text=source_template_939_31) with explicit source cause e.
      }
      // Source: vvaharness/backends/llm/sdk.py:940-941
      if (the source predicate (proxy := proxy_error(e, backend='sdk')) is truthy) {
        // Source: vvaharness/backends/llm/sdk.py:941-941
        Raise proxy with explicit source cause e.
      }
      // Source: vvaharness/backends/llm/sdk.py:942-950
      if (the source predicate attempt < attempts is truthy) {
        // Source: vvaharness/backends/llm/sdk.py:943-943
        In source order: Evaluate once jittered_delay(retry_wait); assign in source target order to wait.
        // Source: vvaharness/backends/llm/sdk.py:944-946
        if (the source predicate (overrun := wait_overrun(wait, session_t0, session_budget, stage=tag or '', route='sdk', effort=effort)) is truthy) {
          // Source: vvaharness/backends/llm/sdk.py:946-946
          Raise overrun with explicit source cause e.
        }
        // Source: vvaharness/backends/llm/sdk.py:947-949
        In source order: Evaluate console.write(source_template_947_30); retain side effects and discard the expression result. Then Evaluate time.sleep(wait); retain side effects and discard the expression result.
        // Source: vvaharness/backends/llm/sdk.py:950-950
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/backends/llm/sdk.py:951-958
      Raise RuntimeError(source_template_952_16) with explicit source cause e.
    }
  }
  // Source: vvaharness/backends/llm/sdk.py:960-965
  if (the source predicate msg is None is truthy) {
    // Source: vvaharness/backends/llm/sdk.py:961-965
    Raise RuntimeError(source_template_962_12).
  }
  // Source: vvaharness/backends/llm/sdk.py:967-967
  In source order: Evaluate once _bank_usage(msg); assign in source target order to usage.
  // Source: vvaharness/backends/llm/sdk.py:968-976
  if (the source predicate usage is truthy) {
    // Source: vvaharness/backends/llm/sdk.py:969-975
    In source order: Evaluate once usage.get('input_tokens', 0) + (usage.get('cache_creation_input_tokens') or 0) + (usage.get('cache_read_input_tokens') or 0); assign in source target order to _in. Then Evaluate once usage.get('cache_read_input_tokens') or 0; assign in source target order to cr. Then Evaluate once usage.get('cache_creation_input_tokens') or 0; assign in source target order to cw. Then Evaluate once usage.get('output_tokens', 0); assign in source target order to out. Then Evaluate once source_template_975_21 if cr or cw else ''; assign in source target order to cache_info.
    // Source: vvaharness/backends/llm/sdk.py:976-976
    In source order: Evaluate console.write(source_template_976_22); retain side effects and discard the expression result.
  }
  // Source: vvaharness/backends/llm/sdk.py:978-978
  In source order: Evaluate _raise_if_refused(msg, tag=tag); retain side effects and discard the expression result.
  // Source: vvaharness/backends/llm/sdk.py:980-983
  if (the source predicate response_model is not None is truthy) {
    // Source: vvaharness/backends/llm/sdk.py:981-981
    In source order: Evaluate once _extract_response_model(response_model, msg, model=model).model_dump_json(); assign in source target order to text.
  }
  else {
    // Source: vvaharness/backends/llm/sdk.py:983-983
    In source order: Evaluate once ''.join((b.text for b in msg.content if b.type == 'text')); assign in source target order to text.
  }
  // Source: vvaharness/backends/llm/sdk.py:985-987
  In source order: Evaluate once output_tokens_for_gate(usage); assign in source target order to out_tokens. Then Evaluate check_response_quality(text.strip(), stage=tag or '', output_tokens=out_tokens); retain side effects and discard the expression result.
  // Source: vvaharness/backends/llm/sdk.py:988-988
  End this invocation with text.strip().
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/sdk.py:993-994
In source order: Evaluate once AGENTIC_MAX_TOKENS; assign in source target order to _AGENTIC_MAX_TOK. Then Evaluate once 40; assign in source target order to _AGENTIC_MAX_TURNS.
// Source: vvaharness/backends/llm/sdk.py:997-1016
// Source signature: _assistant_blocks(content) -> list[dict]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _assistant_blocks(content) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/sdk.py:998-999
  In source order: Retain source documentation literal source_literal_998_4; it is not a model call. Then For out, assign []; source annotation list[dict].
  // Source: vvaharness/backends/llm/sdk.py:1000-1015
  for each b in content {
    // Source: vvaharness/backends/llm/sdk.py:1001-1001
    In source order: Evaluate once getattr(b, 'type', None); assign in source target order to bt.
    // Source: vvaharness/backends/llm/sdk.py:1002-1015
    if (the source predicate bt == 'text' is truthy) {
      // Source: vvaharness/backends/llm/sdk.py:1004-1005
      if (the source predicate b.text.strip() is truthy) {
        // Source: vvaharness/backends/llm/sdk.py:1005-1005
        In source order: Evaluate out.append({'type': 'text', 'text': b.text}); retain side effects and discard the expression result.
      }
    }
    else {
      // Source: vvaharness/backends/llm/sdk.py:1006-1015
      if (the source predicate bt == 'tool_use' is truthy) {
        // Source: vvaharness/backends/llm/sdk.py:1007-1008
        In source order: Evaluate out.append({'type': 'tool_use', 'id': b.id, 'name': b.name, 'input': b.input}); retain side effects and discard the expression result.
      }
      else {
        // Source: vvaharness/backends/llm/sdk.py:1010-1015
        Perform the following protected operations {
          // Source: vvaharness/backends/llm/sdk.py:1011-1013
          In source order: Evaluate once b.model_dump(); assign in source target order to d. Then Evaluate d.pop('cache_control', None); retain side effects and discard the expression result. Then Evaluate out.append(d); retain side effects and discard the expression result.
        }
        // Source: vvaharness/backends/llm/sdk.py:1014-1015
        On the first matching source exception Exception, in handler order {
          // Source: vvaharness/backends/llm/sdk.py:1015-1015
          In source order: Perform no operation at this source statement.
        }
      }
    }
  }
  // Source: vvaharness/backends/llm/sdk.py:1016-1016
  End this invocation with out.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/sdk.py:1019-1038
// Source signature: _with_cache_marker(client, msgs: list[dict]) -> list[dict]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _with_cache_marker(client, msgs) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/sdk.py:1020-1022
  In source order: Retain source documentation literal source_literal_1020_4; it is not a model call. Then For out, assign []; source annotation list[dict]. Then For last_block, assign None; source annotation dict | None.
  // Source: vvaharness/backends/llm/sdk.py:1023-1034
  for each m in msgs {
    // Source: vvaharness/backends/llm/sdk.py:1024-1024
    In source order: Evaluate once m.get('content'); assign in source target order to c.
    // Source: vvaharness/backends/llm/sdk.py:1025-1034
    if (the source predicate isinstance(c, list) is truthy) {
      // Source: vvaharness/backends/llm/sdk.py:1026-1026
      In source order: For cc, assign []; source annotation list.
      // Source: vvaharness/backends/llm/sdk.py:1027-1031
      for each b in c {
        // Source: vvaharness/backends/llm/sdk.py:1028-1030
        if (the source predicate isinstance(b, dict) is truthy) {
          // Source: vvaharness/backends/llm/sdk.py:1029-1030
          In source order: Evaluate once {k: v for k, v in b.items() if k != 'cache_control'}; assign in source target order to b. Then Evaluate once b; assign in source target order to last_block.
        }
        // Source: vvaharness/backends/llm/sdk.py:1031-1031
        In source order: Evaluate cc.append(b); retain side effects and discard the expression result.
      }
      // Source: vvaharness/backends/llm/sdk.py:1032-1032
      In source order: Evaluate out.append({**m, 'content': cc}); retain side effects and discard the expression result.
    }
    else {
      // Source: vvaharness/backends/llm/sdk.py:1034-1034
      In source order: Evaluate out.append(m); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/backends/llm/sdk.py:1035-1037
  if (the source predicate last_block is not None and _cache_markers_enabled() and (_cache_route(client) in _CACHE_CONTROL_ROUTES) is truthy) {
    // Source: vvaharness/backends/llm/sdk.py:1037-1037
    In source order: Evaluate once {'type': 'ephemeral'}; assign in source target order to last_block['cache_control'].
  }
  // Source: vvaharness/backends/llm/sdk.py:1038-1038
  End this invocation with out.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/sdk.py:1041-1045
// Source signature: _auth_failure_sdk(error: anthropic.APIStatusError) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _auth_failure_sdk(error) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/sdk.py:1042-1042
  In source order: Retain source documentation literal source_literal_1042_4; it is not a model call.
  // Source: vvaharness/backends/llm/sdk.py:1043-1045
  End this invocation with bool(error.status_code == 401 or (_AUTH_STATUS_RX.search(rejection_text(error)) and error.status_code not in RETRYABLE_STATUS)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/sdk.py:1048-1065
// Source signature: _drain_within_deadline(stream: Any, *, deadline: float, stage: str | None, effort: str | None, budget_s: float | None) -> Any
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _drain_within_deadline(stream, deadline, stage, effort, budget_s) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/sdk.py:1050-1057
  In source order: Retain source documentation literal source_literal_1050_4; it is not a model call.
  // Source: vvaharness/backends/llm/sdk.py:1058-1064
  if (the source predicate hasattr(stream, '__iter__') is truthy) {
    // Source: vvaharness/backends/llm/sdk.py:1059-1064
    for each _event in stream {
      // Source: vvaharness/backends/llm/sdk.py:1060-1064
      if (the source predicate time.monotonic() >= deadline is truthy) {
        // Source: vvaharness/backends/llm/sdk.py:1061-1061
        In source order: Evaluate stream.close(); retain side effects and discard the expression result.
        // Source: vvaharness/backends/llm/sdk.py:1062-1064
        Raise call_timeout_error(stage=stage or '', route='sdk', budget_s=budget_s, effort=effort, cause_text=source_template_1064_31).
      }
    }
  }
  // Source: vvaharness/backends/llm/sdk.py:1065-1065
  End this invocation with stream.get_final_message().
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/sdk.py:1068-1172
// Source signature: _check_agentic_stop(msg, *, client, messages: list[dict], call_kw: dict, model: str, tag: str | None, requested: int, response_model: type[BaseModel] | None=None, dispatchable: bool=False, effort: str | None=None, request_timeout: float | None=None, session_t0: float | None=None, session_budget: float | None=None)
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _check_agentic_stop(msg, client, messages, call_kw, model, tag, requested, response_model, dispatchable, effort, request_timeout, session_t0, session_budget) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/sdk.py:1076-1076
  In source order: Retain source documentation literal source_literal_1076_4; it is not a model call.
  // Source: vvaharness/backends/llm/sdk.py:1077-1078
  if (the source predicate not finish_truncated(getattr(msg, 'stop_reason', None)) is truthy) {
    // Source: vvaharness/backends/llm/sdk.py:1078-1078
    End this invocation with (msg, None).
  }
  // Source: vvaharness/backends/llm/sdk.py:1079-1079
  In source order: Evaluate once truncation_retry_max(requested, cap=MODEL_MAX_OUTPUT_TOKENS); assign in source target order to retry_at.
  // Source: vvaharness/backends/llm/sdk.py:1080-1166
  if (the source predicate retry_at is not None is truthy) {
    // Source: vvaharness/backends/llm/sdk.py:1081-1089
    In source order: Evaluate COUNTERS.bump(TRUNCATED_RETRY_ATTEMPTED_COUNTER); retain side effects and discard the expression result. Then Evaluate log.warning(Event.TRUNCATED_RETRY, route='sdk', stop_reason=msg.stop_reason, budget=requested, retry_at=retry_at); retain side effects and discard the expression result. Then Evaluate _errlog.log(tag or 'sdk', tag or 'truncation', source_template_1086_12, error_code=TruncatedResponseError.error_code, recovered=True); retain side effects and discard the expression result. Then Evaluate once {**call_kw, 'max_tokens': retry_at}; assign in source target order to retry_kw.
    // Source: vvaharness/backends/llm/sdk.py:1090-1136
    Perform the following protected operations {
      // Source: vvaharness/backends/llm/sdk.py:1091-1093
      In source order: Evaluate once time.monotonic(); assign in source target order to _t0. Then Evaluate once turn_options(session_t0 or _t0, session_budget, request_timeout); assign in source target order to send. Then Evaluate once client.with_options(**send); assign in source target order to retry_client.
      // Source: vvaharness/backends/llm/sdk.py:1094-1098
      Enter source context managers left-to-right: retry_client.messages.stream(messages=_with_cache_marker(client, messages), **retry_kw) bound to stream {
        // Source: vvaharness/backends/llm/sdk.py:1096-1098
        In source order: Evaluate once _drain_within_deadline(stream, deadline=_t0 + send['timeout'], stage=tag, effort=effort, budget_s=request_timeout); assign in source target order to retried.
      }
      Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
      // Source: vvaharness/backends/llm/sdk.py:1099-1099
      In source order: Evaluate note_budget_use(time.monotonic() - _t0, request_timeout, effort); retain side effects and discard the expression result.
    }
    // Source: vvaharness/backends/llm/sdk.py:1100-1124
    On the first matching source exception anthropic.APIStatusError as e, in handler order {
      // Source: vvaharness/backends/llm/sdk.py:1104-1107
      if (the source predicate _auth_failure_sdk(e) is truthy) {
        // Source: vvaharness/backends/llm/sdk.py:1105-1107
        Raise AuthenticationError(redact(str(getattr(e, 'message', e)))[:400], status_code=e.status_code, backend='sdk') with explicit source cause e.
      }
      // Source: vvaharness/backends/llm/sdk.py:1108-1108
      In source order: Evaluate once rejection_text(e).lower(); assign in source target order to low.
      // Source: vvaharness/backends/llm/sdk.py:1109-1119
      if (the source predicate e.status_code in PARAM_REJECTION_STATUS and _CTX_OVERFLOW_RX.search(low) is truthy) {
        // Source: vvaharness/backends/llm/sdk.py:1114-1114
        In source order: Evaluate COUNTERS.bump(TRUNCATED_REPLIES_COUNTER); retain side effects and discard the expression result.
        // Source: vvaharness/backends/llm/sdk.py:1115-1119
        Raise TruncatedResponseError(source_literal_1116_20, stage=tag or '', requested=requested, retried=0) with explicit source cause e.
      }
      // Source: vvaharness/backends/llm/sdk.py:1120-1124
      Raise RuntimeError(redact(source_template_1121_16)) with explicit source cause e.
    }
    // Source: vvaharness/backends/llm/sdk.py:1125-1136
    On the first matching source exception (anthropic.APIConnectionError, httpx2.TransportError) as e, in handler order {
      // Source: vvaharness/backends/llm/sdk.py:1126-1130
      if (the source predicate is_timeout_failure(e) is truthy) {
        // Source: vvaharness/backends/llm/sdk.py:1127-1130
        Raise call_timeout_error(stage=tag or '', route='sdk', budget_s=request_timeout, effort=effort, cause_text=source_template_1129_31) with explicit source cause e.
      }
      // Source: vvaharness/backends/llm/sdk.py:1131-1132
      if (the source predicate (proxy := proxy_error(e, backend='sdk')) is truthy) {
        // Source: vvaharness/backends/llm/sdk.py:1132-1132
        Raise proxy with explicit source cause e.
      }
      // Source: vvaharness/backends/llm/sdk.py:1133-1136
      Raise RuntimeError(redact(source_template_1134_16)) with explicit source cause e.
    }
    // Source: vvaharness/backends/llm/sdk.py:1137-1140
    if (the source predicate retried.usage is truthy) {
      // Source: vvaharness/backends/llm/sdk.py:1138-1140
      In source order: Evaluate once cast('TokenUsage', retried.usage.model_dump()); assign in source target order to retried_usage. Then Evaluate _note_unparsed_cache_keys(retried_usage); retain side effects and discard the expression result. Then Evaluate TOKENS.add(retried_usage); retain side effects and discard the expression result.
    }
    // Source: vvaharness/backends/llm/sdk.py:1141-1146
    if (the source predicate finish_truncated(getattr(retried, 'stop_reason', None)) is truthy) {
      // Source: vvaharness/backends/llm/sdk.py:1142-1142
      In source order: Evaluate COUNTERS.bump(TRUNCATED_REPLIES_COUNTER); retain side effects and discard the expression result.
      // Source: vvaharness/backends/llm/sdk.py:1143-1146
      Raise TruncatedResponseError('agentic reply still hit the output-token budget after the doubled retry', stage=tag or '', requested=requested, retried=retry_at).
    }
    // Source: vvaharness/backends/llm/sdk.py:1148-1149
    In source order: Evaluate once getattr(retried, 'stop_reason', None) == 'tool_use' and (not dispatchable); assign in source target order to undispatched_call.
    // Source: vvaharness/backends/llm/sdk.py:1150-1158
    if (the source predicate undispatched_call and response_model is None is truthy) {
      // Source: vvaharness/backends/llm/sdk.py:1154-1158
      Raise TruncatedResponseError(source_literal_1155_16, stage=tag or '', requested=requested, retried=retry_at).
    }
    // Source: vvaharness/backends/llm/sdk.py:1159-1159
    In source order: Evaluate COUNTERS.bump(TRUNCATED_RETRY_RECOVERED_COUNTER); retain side effects and discard the expression result.
    // Source: vvaharness/backends/llm/sdk.py:1160-1165
    if (the source predicate undispatched_call and response_model is not None is truthy) {
      // Source: vvaharness/backends/llm/sdk.py:1164-1165
      End this invocation with (retried, _extract_response_model(response_model, retried, model=model).model_dump_json()).
    }
    // Source: vvaharness/backends/llm/sdk.py:1166-1166
    End this invocation with (retried, None).
  }
  // Source: vvaharness/backends/llm/sdk.py:1167-1167
  In source order: Evaluate COUNTERS.bump(TRUNCATED_REPLIES_COUNTER); retain side effects and discard the expression result.
  // Source: vvaharness/backends/llm/sdk.py:1168-1172
  Raise TruncatedResponseError(source_template_1169_8, stage=tag or '', requested=requested, retried=0).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/sdk.py:1176-1178
In source order: Evaluate once '[evicted to fit context]'; assign in source target order to _EVICTED_MARK. Then Evaluate once re.compile('context.?length|context length|exceed.*(?:token|limit)|too long', re.I); assign in source target order to _CTX_OVERFLOW_RX.
// Source: vvaharness/backends/llm/sdk.py:1181-1199
// Source signature: _shrink_history(messages: list[dict]) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _shrink_history(messages) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/sdk.py:1182-1182
  In source order: Retain source documentation literal source_literal_1182_4; it is not a model call.
  // Source: vvaharness/backends/llm/sdk.py:1187-1198
  for each m in messages {
    // Source: vvaharness/backends/llm/sdk.py:1188-1188
    In source order: Evaluate once m.get('content'); assign in source target order to blocks.
    // Source: vvaharness/backends/llm/sdk.py:1189-1190
    if (the source predicate not isinstance(blocks, list) is truthy) {
      // Source: vvaharness/backends/llm/sdk.py:1190-1190
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/backends/llm/sdk.py:1191-1198
    for each b in blocks {
      // Source: vvaharness/backends/llm/sdk.py:1192-1193
      if (the source predicate not isinstance(b, dict) or b.get('type') != 'tool_result' is truthy) {
        // Source: vvaharness/backends/llm/sdk.py:1193-1193
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/backends/llm/sdk.py:1194-1194
      In source order: Evaluate once b.get('content'); assign in source target order to c.
      // Source: vvaharness/backends/llm/sdk.py:1195-1198
      if (the source predicate isinstance(c, str) and len(c) > 1200 and (not c.endswith(_EVICTED_MARK)) is truthy) {
        // Source: vvaharness/backends/llm/sdk.py:1197-1197
        In source order: Evaluate once c[:800] + source_literal_1197_41 + _EVICTED_MARK; assign in source target order to b['content'].
        // Source: vvaharness/backends/llm/sdk.py:1198-1198
        End this invocation with True.
      }
    }
  }
  // Source: vvaharness/backends/llm/sdk.py:1199-1199
  End this invocation with False.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/sdk.py:1202-1684
// Source signature: agentic(user_prompt: str, *, model: str, system_prompt: str | None=None, allowed_tools: list[str] | None=None, cwd: str, max_budget_usd: float | None=None, permission_mode: str='auto', max_turns: int | None=None, timeout: int | None=None, tag: str | None=None, extra_tools: list[dict] | None=None, extra_dispatch=None, response_model: type[BaseModel] | None=None, max_output_tokens: int | None=None, submit_guard: Callable[[], str | None] | None=None, exhausted_tools: Callable[[], frozenset[str]] | None=None, effort: str | None=None) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn agentic(user_prompt, model, system_prompt, allowed_tools, cwd, max_budget_usd, permission_mode, max_turns, timeout, tag, extra_tools, extra_dispatch, response_model, max_output_tokens, submit_guard, exhausted_tools, effort) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/sdk.py:1243-1249
  In source order: Evaluate once int(max_turns) if max_turns else _AGENTIC_MAX_TURNS; assign in source target order to turns_cap. Then Evaluate once int(max_output_tokens) if max_output_tokens else _AGENTIC_MAX_TOK; assign in source target order to out_cap. Then Evaluate once list(DEFAULT_READ_TOOLS) if allowed_tools is None else list(allowed_tools); assign in source target order to allowed.
  // Source: vvaharness/backends/llm/sdk.py:1250-1253
  if (the source predicate 'Bash' in allowed is truthy) {
    // Source: vvaharness/backends/llm/sdk.py:1251-1253
    Raise ValueError('sdk.agentic: `Bash` is forbidden on `via: sdk`; remove it from allowed_tools or switch that role to `via: cli`.').
  }
  // Source: vvaharness/backends/llm/sdk.py:1254-1254
  In source order: Evaluate once _localtools.supported(allowed); assign in source target order to (ok, missing).
  // Source: vvaharness/backends/llm/sdk.py:1255-1277
  if (the source predicate missing is truthy) {
    // Source: vvaharness/backends/llm/sdk.py:1259-1264
    if (the source predicate extra_tools is truthy) {
      // Source: vvaharness/backends/llm/sdk.py:1262-1264
      Raise ValueError(source_template_1263_16).
    }
    // Source: vvaharness/backends/llm/sdk.py:1267-1271
    In source order: Resolve source import from vvaharness.backends.llm import agent_sdk as _agent_sdk; preserve alias and import-time effects. Then Evaluate console.write(source_template_1270_22); retain side effects and discard the expression result.
    // Source: vvaharness/backends/llm/sdk.py:1272-1277
    End this invocation with _agent_sdk.agentic(user_prompt, model=model, system_prompt=system_prompt, allowed_tools=allowed, cwd=cwd, max_budget_usd=max_budget_usd, permission_mode=permission_mode, max_turns=max_turns, tag=tag, timeout=timeout, effort=effort).
  }
  // Source: vvaharness/backends/llm/sdk.py:1281-1289
  In source order: Evaluate _warn_max_budget_unenforced('agentic', max_budget_usd); retain side effects and discard the expression result. Then Evaluate once _get_client(); assign in source target order to client. Then Evaluate once effort_scaled_seconds(DEFAULT_REQUEST_TIMEOUT_SECONDS, effort, kind=ClockKind.REQUEST); assign in source target order to request_timeout. Then Evaluate once effort_scaled_seconds(timeout, effort, kind=ClockKind.SESSION) if timeout else None; assign in source target order to session_budget. Then Evaluate once time.monotonic(); assign in source target order to session_t0.
  // Source: vvaharness/backends/llm/sdk.py:1290-1291
  In source order: Evaluate once [*_localtools.anthropic_schemas_for(ok), *(extra_tools or [])]; assign in source target order to tools. Then Evaluate once ok + [t.get('name') for t in extra_tools or []]; assign in source target order to advertised.
  // Source: vvaharness/backends/llm/sdk.py:1292-1294
  if (the source predicate response_model is not None is truthy) {
    // Source: vvaharness/backends/llm/sdk.py:1293-1294
    In source order: Evaluate once [*tools, _response_model_tool(response_model)]; assign in source target order to tools. Then Evaluate once [*advertised, _RESPONSE_MODEL_TOOL_NAME]; assign in source target order to advertised.
  }
  // Source: vvaharness/backends/llm/sdk.py:1296-1301
  In source order: For base_kw, assign {'model': model, 'max_tokens': out_cap, 'tools': tools}; source annotation dict. Then Evaluate once _effort_thinking_kwargs(model, effort); assign in source target order to thinking_kwargs. Then Evaluate base_kw.update(thinking_kwargs); retain side effects and discard the expression result. Then Evaluate once system_prompt; assign in source target order to system_text.
  // Source: vvaharness/backends/llm/sdk.py:1302-1310
  if (the source predicate response_model is not None is truthy) {
    // Source: vvaharness/backends/llm/sdk.py:1303-1310
    if (the source predicate not _forcing_blocked(model, thinking_kwargs.get('thinking')) is truthy) {
      // Source: vvaharness/backends/llm/sdk.py:1305-1305
      In source order: Evaluate once {'type': 'any'}; assign in source target order to base_kw['tool_choice'].
    }
    else {
      // Source: vvaharness/backends/llm/sdk.py:1308-1309
      if (the source predicate model not in _NO_TOOL_CHOICE_MODELS is truthy) {
        // Source: vvaharness/backends/llm/sdk.py:1309-1309
        In source order: Evaluate _warn_tool_choice_dropped_for_thinking(model, effort); retain side effects and discard the expression result.
      }
      // Source: vvaharness/backends/llm/sdk.py:1310-1310
      In source order: Evaluate once with_submit_instruction(system_prompt, response_model); assign in source target order to system_text.
    }
  }
  // Source: vvaharness/backends/llm/sdk.py:1311-1311
  In source order: Evaluate once json.dumps(tools, default=str); assign in source target order to tools_text.
  // Source: vvaharness/backends/llm/sdk.py:1312-1316
  if (the source predicate system_text is truthy) {
    // Source: vvaharness/backends/llm/sdk.py:1315-1316
    In source order: Evaluate once _build_system_content(client, system_text, model, tools_text=tools_text); assign in source target order to base_kw['system'].
  }
  // Source: vvaharness/backends/llm/sdk.py:1319-1331
  In source order: For messages, assign [{'role': 'user', 'content': [{'type': 'text', 'text': user_prompt}]}]; source annotation list[dict]. Then Evaluate once source_template_1322_14 if tag else ''; assign in source target order to tag_sfx. Then Evaluate console.write(source_template_1323_18); retain side effects and discard the expression result. Then Evaluate once 0; assign in source target order to tool_calls_total. Then Evaluate once 0; assign in source target order to submit_rejects.
  // Source: vvaharness/backends/llm/sdk.py:1333-1336
  In source order: Evaluate once False; assign in source target order to schema_nudged. Then For withdrawn, assign frozenset(); source annotation frozenset[str].
  // Source: vvaharness/backends/llm/sdk.py:1337-1564
  for each turn in range(1, turns_cap + 1) {
    // Source: vvaharness/backends/llm/sdk.py:1338-1342
    if (the source predicate session_budget and time.monotonic() - session_t0 >= session_budget is truthy) {
      // Source: vvaharness/backends/llm/sdk.py:1340-1342
      Raise call_timeout_error(stage=tag or '', route='sdk', budget_s=session_budget, effort=effort, cause_text=source_template_1342_27).
    }
    // Source: vvaharness/backends/llm/sdk.py:1343-1350
    if (the source predicate exhausted_tools is not None is truthy) {
      // Source: vvaharness/backends/llm/sdk.py:1344-1344
      In source order: Evaluate once exhausted_tools() - withdrawn; assign in source target order to newly_exhausted.
      // Source: vvaharness/backends/llm/sdk.py:1345-1350
      if (the source predicate newly_exhausted is truthy) {
        // Source: vvaharness/backends/llm/sdk.py:1346-1350
        In source order: Apply source augmented assignment withdrawn |= newly_exhausted with source evaluation/in-place semantics. Then Evaluate once [t for t in base_kw['tools'] if t.get('name') not in withdrawn]; assign in source target order to base_kw['tools']. Then Evaluate console.write(source_template_1349_30); retain side effects and discard the expression result.
      }
    }
    // Source: vvaharness/backends/llm/sdk.py:1351-1353
    In source order: Evaluate once None; assign in source target order to msg. Then Evaluate once 0; assign in source target order to transients. Then Evaluate once 0; assign in source target order to shrinks.
    // Source: vvaharness/backends/llm/sdk.py:1354-1445
    while (the source predicate msg is None is truthy) {
      // Source: vvaharness/backends/llm/sdk.py:1355-1445
      Perform the following protected operations {
        // Source: vvaharness/backends/llm/sdk.py:1356-1358
        In source order: Evaluate once time.monotonic(); assign in source target order to _t0. Then Evaluate once turn_options(session_t0, session_budget, request_timeout); assign in source target order to send. Then Evaluate once client.with_options(**send); assign in source target order to turn_client.
        // Source: vvaharness/backends/llm/sdk.py:1359-1363
        Enter source context managers left-to-right: turn_client.messages.stream(messages=_with_cache_marker(client, messages), **base_kw) bound to stream {
          // Source: vvaharness/backends/llm/sdk.py:1361-1363
          In source order: Evaluate once _drain_within_deadline(stream, deadline=_t0 + send['timeout'], stage=tag, effort=effort, budget_s=request_timeout); assign in source target order to msg.
        }
        Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
        // Source: vvaharness/backends/llm/sdk.py:1364-1364
        In source order: Evaluate note_budget_use(time.monotonic() - _t0, request_timeout, effort); retain side effects and discard the expression result.
      }
      // Source: vvaharness/backends/llm/sdk.py:1365-1422
      On the first matching source exception anthropic.APIStatusError as e, in handler order {
        // Source: vvaharness/backends/llm/sdk.py:1370-1373
        if (the source predicate _auth_failure_sdk(e) is truthy) {
          // Source: vvaharness/backends/llm/sdk.py:1371-1373
          Raise AuthenticationError(redact(str(getattr(e, 'message', e)))[:400], status_code=e.status_code, backend='sdk') with explicit source cause e.
        }
        // Source: vvaharness/backends/llm/sdk.py:1374-1374
        In source order: Evaluate once rejection_text(e).lower(); assign in source target order to low.
        // Source: vvaharness/backends/llm/sdk.py:1377-1382
        if (the source predicate e.status_code in PARAM_REJECTION_STATUS and _CTX_OVERFLOW_RX.search(low) and (shrinks < 16) and _shrink_history(messages) is truthy) {
          // Source: vvaharness/backends/llm/sdk.py:1379-1381
          In source order: Apply source augmented assignment shrinks += 1 with source evaluation/in-place semantics. Then Evaluate console.write(source_template_1380_34); retain side effects and discard the expression result.
          // Source: vvaharness/backends/llm/sdk.py:1382-1382
          Continue the immediately enclosing source loop at its next iteration.
        }
        // Source: vvaharness/backends/llm/sdk.py:1384-1388
        if (the source predicate _unforce_rejected_tool_choice(base_kw, e, low, client=client, model=model, system_prompt=system_prompt, response_model=response_model, tools_text=tools_text) is truthy) {
          // Source: vvaharness/backends/llm/sdk.py:1388-1388
          Continue the immediately enclosing source loop at its next iteration.
        }
        // Source: vvaharness/backends/llm/sdk.py:1392-1407
        if (the source predicate e.status_code in PARAM_REJECTION_STATUS and 'thinking' in base_kw and ('thinking' in low) is truthy) {
          // Source: vvaharness/backends/llm/sdk.py:1394-1396
          In source order: Evaluate once 'not supported' in low or 'unexpected' in low or 'adaptive' in low or ('unrecognized' in low) or ('unknown' in low); assign in source target order to unsupported.
          // Source: vvaharness/backends/llm/sdk.py:1397-1398
          if (the source predicate unsupported is truthy) {
            // Source: vvaharness/backends/llm/sdk.py:1398-1398
            In source order: Evaluate _NO_THINK_MODELS.add(model); retain side effects and discard the expression result.
          }
          // Source: vvaharness/backends/llm/sdk.py:1399-1406
          In source order: Evaluate base_kw.pop('thinking', None); retain side effects and discard the expression result. Then Evaluate base_kw.pop('output_config', None); retain side effects and discard the expression result. Then Evaluate _reforce_tool_choice(base_kw, {'type': 'any'}, client=client, model=model, system_prompt=system_prompt, response_model=response_model, tools_text=tools_text); retain side effects and discard the expression result. Then Evaluate console.write(source_template_1404_34); retain side effects and discard the expression result.
          // Source: vvaharness/backends/llm/sdk.py:1407-1407
          Continue the immediately enclosing source loop at its next iteration.
        }
        // Source: vvaharness/backends/llm/sdk.py:1408-1418
        if (the source predicate _is_transient_sdk(e) and transients < 4 is truthy) {
          // Source: vvaharness/backends/llm/sdk.py:1409-1410
          In source order: Apply source augmented assignment transients += 1 with source evaluation/in-place semantics. Then Evaluate once jittered_delay(min(60, 20 * transients)); assign in source target order to wait.
          // Source: vvaharness/backends/llm/sdk.py:1411-1413
          if (the source predicate (overrun := wait_overrun(wait, session_t0, session_budget, stage=tag or '', route='sdk', effort=effort)) is truthy) {
            // Source: vvaharness/backends/llm/sdk.py:1413-1413
            Raise overrun with explicit source cause e.
          }
          // Source: vvaharness/backends/llm/sdk.py:1414-1417
          In source order: Evaluate console.write(source_template_1414_34); retain side effects and discard the expression result. Then Evaluate time.sleep(wait); retain side effects and discard the expression result.
          // Source: vvaharness/backends/llm/sdk.py:1418-1418
          Continue the immediately enclosing source loop at its next iteration.
        }
        // Source: vvaharness/backends/llm/sdk.py:1419-1422
        Raise RuntimeError(redact(source_template_1420_20)) with explicit source cause e.
      }
      // Source: vvaharness/backends/llm/sdk.py:1423-1445
      On the first matching source exception (anthropic.APIConnectionError, httpx2.TransportError) as e, in handler order {
        // Source: vvaharness/backends/llm/sdk.py:1424-1428
        if (the source predicate is_timeout_failure(e) is truthy) {
          // Source: vvaharness/backends/llm/sdk.py:1425-1428
          Raise call_timeout_error(stage=tag or '', route='sdk', budget_s=request_timeout, effort=effort, cause_text=source_template_1427_35) with explicit source cause e.
        }
        // Source: vvaharness/backends/llm/sdk.py:1429-1430
        if (the source predicate (proxy := proxy_error(e, backend='sdk')) is truthy) {
          // Source: vvaharness/backends/llm/sdk.py:1430-1430
          Raise proxy with explicit source cause e.
        }
        // Source: vvaharness/backends/llm/sdk.py:1431-1440
        if (the source predicate transients < 4 is truthy) {
          // Source: vvaharness/backends/llm/sdk.py:1432-1433
          In source order: Apply source augmented assignment transients += 1 with source evaluation/in-place semantics. Then Evaluate once jittered_delay(min(60, 20 * transients)); assign in source target order to wait.
          // Source: vvaharness/backends/llm/sdk.py:1434-1436
          if (the source predicate (overrun := wait_overrun(wait, session_t0, session_budget, stage=tag or '', route='sdk', effort=effort)) is truthy) {
            // Source: vvaharness/backends/llm/sdk.py:1436-1436
            Raise overrun with explicit source cause e.
          }
          // Source: vvaharness/backends/llm/sdk.py:1437-1439
          In source order: Evaluate console.write(source_template_1437_34); retain side effects and discard the expression result. Then Evaluate time.sleep(wait); retain side effects and discard the expression result.
          // Source: vvaharness/backends/llm/sdk.py:1440-1440
          Continue the immediately enclosing source loop at its next iteration.
        }
        // Source: vvaharness/backends/llm/sdk.py:1441-1445
        Raise RuntimeError(redact(source_template_1442_20)) with explicit source cause e.
      }
    }
    // Source: vvaharness/backends/llm/sdk.py:1447-1450
    if (the source predicate msg.usage is truthy) {
      // Source: vvaharness/backends/llm/sdk.py:1448-1450
      In source order: Evaluate once cast('TokenUsage', msg.usage.model_dump()); assign in source target order to turn_usage. Then Evaluate _note_unparsed_cache_keys(turn_usage); retain side effects and discard the expression result. Then Evaluate TOKENS.add(turn_usage); retain side effects and discard the expression result.
    }
    // Source: vvaharness/backends/llm/sdk.py:1452-1460
    if (the source predicate finish_truncated(msg.stop_reason) is truthy) {
      // Source: vvaharness/backends/llm/sdk.py:1453-1458
      In source order: Evaluate once _check_agentic_stop(msg, client=client, messages=messages, call_kw=base_kw, model=model, tag=tag, requested=out_cap, response_model=response_model, dispatchable=True, effort=effort, request_timeout=request_timeout, session_t0=session_t0, session_budget=session_budget); assign in source target order to (msg, override).
      // Source: vvaharness/backends/llm/sdk.py:1459-1460
      if (the source predicate override is not None is truthy) {
        // Source: vvaharness/backends/llm/sdk.py:1460-1460
        End this invocation with override.
      }
    }
    // Source: vvaharness/backends/llm/sdk.py:1466-1466
    In source order: Evaluate _raise_if_refused(msg, tag=tag); retain side effects and discard the expression result.
    // Source: vvaharness/backends/llm/sdk.py:1467-1487
    if (the source predicate msg.stop_reason != 'tool_use' is truthy) {
      // Source: vvaharness/backends/llm/sdk.py:1468-1469
      In source order: Evaluate once ''.join((b.text for b in msg.content if getattr(b, 'type', None) == 'text')).strip(); assign in source target order to text.
      // Source: vvaharness/backends/llm/sdk.py:1472-1484
      if (the source predicate response_model is not None and (not schema_nudged) and (turn < turns_cap) is truthy) {
        // Source: vvaharness/backends/llm/sdk.py:1473-1477
        In source order: Evaluate once True; assign in source target order to schema_nudged. Then Evaluate COUNTERS.bump('llm_structured_prose_reask'); retain side effects and discard the expression result. Then Evaluate log.warning(Event.STRUCTURED_PROSE_REASK, route='sdk', model=model, tool=_RESPONSE_MODEL_TOOL_NAME, tag=tag or None); retain side effects and discard the expression result. Then Evaluate once _assistant_blocks(msg.content); assign in source target order to blocks.
        // Source: vvaharness/backends/llm/sdk.py:1480-1481
        if (the source predicate any((b.get('type') in ('text', 'tool_use') for b in blocks)) is truthy) {
          // Source: vvaharness/backends/llm/sdk.py:1481-1481
          In source order: Evaluate messages.append({'role': 'assistant', 'content': blocks}); retain side effects and discard the expression result.
        }
        // Source: vvaharness/backends/llm/sdk.py:1482-1483
        In source order: Evaluate messages.append({'role': 'user', 'content': [{'type': 'text', 'text': STRUCTURED_PROSE_REASK}]}); retain side effects and discard the expression result.
        // Source: vvaharness/backends/llm/sdk.py:1484-1484
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/backends/llm/sdk.py:1485-1486
      In source order: Evaluate console.write(source_template_1485_26); retain side effects and discard the expression result.
      // Source: vvaharness/backends/llm/sdk.py:1487-1487
      End this invocation with text.
    }
    // Source: vvaharness/backends/llm/sdk.py:1489-1491
    In source order: Evaluate messages.append({'role': 'assistant', 'content': _assistant_blocks(msg.content)}); retain side effects and discard the expression result. Then For results, assign []; source annotation list[dict].
    // Source: vvaharness/backends/llm/sdk.py:1492-1562
    for each b in msg.content {
      // Source: vvaharness/backends/llm/sdk.py:1493-1494
      if (the source predicate getattr(b, 'type', None) != 'tool_use' is truthy) {
        // Source: vvaharness/backends/llm/sdk.py:1494-1494
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/backends/llm/sdk.py:1495-1538
      if (the source predicate response_model is not None and b.name == _RESPONSE_MODEL_TOOL_NAME is truthy) {
        // Source: vvaharness/backends/llm/sdk.py:1496-1524
        Perform the following protected operations {
          // Source: vvaharness/backends/llm/sdk.py:1497-1497
          In source order: Evaluate once response_model.model_validate(b.input); assign in source target order to validated.
        }
        // Source: vvaharness/backends/llm/sdk.py:1498-1524
        On the first matching source exception Exception as exc, in handler order {
          // Source: vvaharness/backends/llm/sdk.py:1502-1503
          In source order: Apply source augmented assignment submit_rejects += 1 with source evaluation/in-place semantics. Then Evaluate COUNTERS.bump('llm_structured_submit_rejected'); retain side effects and discard the expression result.
          // Source: vvaharness/backends/llm/sdk.py:1504-1515
          if (the source predicate submit_rejects >= STRUCTURED_REASK_MAX is truthy) {
            // Source: vvaharness/backends/llm/sdk.py:1505-1514
            In source order: Evaluate log.warning(Event.STRUCTURED_SUBMIT_REJECTED, route='sdk', tool=_RESPONSE_MODEL_TOOL_NAME, error=type(exc).__name__, rejects=submit_rejects); retain side effects and discard the expression result. Then Evaluate once structured_failure_detail(exc); assign in source target order to (detail, _). Then Evaluate _errlog.log(tag or 'sdk', tag or 'structured', source_template_1512_28, detail=detail, reason='llm_structured_reask_gave_up', recovered=True); retain side effects and discard the expression result.
            // Source: vvaharness/backends/llm/sdk.py:1515-1515
            End this invocation with json.dumps(dict(b.input or {})).
          }
          // Source: vvaharness/backends/llm/sdk.py:1516-1523
          In source order: Evaluate console.write(source_template_1516_34); retain side effects and discard the expression result. Then Evaluate results.append({'type': 'tool_result', 'tool_use_id': b.id, 'content': source_template_1521_36}); retain side effects and discard the expression result.
          // Source: vvaharness/backends/llm/sdk.py:1524-1524
          Continue the immediately enclosing source loop at its next iteration.
        }
        // Source: vvaharness/backends/llm/sdk.py:1525-1535
        if (the source predicate submit_guard is not None is truthy) {
          // Source: vvaharness/backends/llm/sdk.py:1526-1526
          In source order: Evaluate once submit_guard(); assign in source target order to hold_text.
          // Source: vvaharness/backends/llm/sdk.py:1527-1535
          if (the source predicate hold_text is not None is truthy) {
            // Source: vvaharness/backends/llm/sdk.py:1528-1534
            In source order: Evaluate console.write(source_template_1528_38); retain side effects and discard the expression result. Then Evaluate results.append({'type': 'tool_result', 'tool_use_id': b.id, 'content': hold_text}); retain side effects and discard the expression result.
            // Source: vvaharness/backends/llm/sdk.py:1535-1535
            Continue the immediately enclosing source loop at its next iteration.
          }
        }
        // Source: vvaharness/backends/llm/sdk.py:1536-1537
        In source order: Evaluate console.write(source_template_1536_30); retain side effects and discard the expression result.
        // Source: vvaharness/backends/llm/sdk.py:1538-1538
        End this invocation with validated.model_dump_json().
      }
      // Source: vvaharness/backends/llm/sdk.py:1539-1546
      In source order: Apply source augmented assignment tool_calls_total += 1 with source evaluation/in-place semantics. Then Evaluate once dict(b.input or {}); assign in source target order to args. Then Evaluate once extra_dispatch(b.name, args) if extra_dispatch is not None else None; assign in source target order to out.
      // Source: vvaharness/backends/llm/sdk.py:1547-1549
      if (the source predicate out is None and b.name not in ok is truthy) {
        // Source: vvaharness/backends/llm/sdk.py:1549-1549
        In source order: Evaluate once _localtools.UNGRANTED_TOOL_ERROR.format(name=b.name); assign in source target order to out.
      }
      // Source: vvaharness/backends/llm/sdk.py:1550-1559
      if (the source predicate out is None is truthy) {
        // Source: vvaharness/backends/llm/sdk.py:1554-1555
        In source order: Evaluate once _localtools.cap_tool_result(_localtools.execute(b.name, args, cwd=cwd)); assign in source target order to out.
        // Source: vvaharness/backends/llm/sdk.py:1556-1559
        if (the source predicate not is_stage_only() is truthy) {
          // Source: vvaharness/backends/llm/sdk.py:1557-1559
          In source order: Evaluate console.write(source_template_1558_24); retain side effects and discard the expression result.
        }
      }
      // Source: vvaharness/backends/llm/sdk.py:1560-1562
      In source order: Evaluate results.append({'type': 'tool_result', 'tool_use_id': b.id, 'content': out}); retain side effects and discard the expression result.
    }
    // Source: vvaharness/backends/llm/sdk.py:1564-1564
    In source order: Evaluate messages.append({'role': 'user', 'content': results}); retain side effects and discard the expression result.
  }
  // Source: vvaharness/backends/llm/sdk.py:1568-1569
  In source order: Evaluate log.warning(Event.LLM_TURN_CAP_EXHAUSTED, turns_cap=turns_cap, model=model, tag=tag_sfx); retain side effects and discard the expression result. Then Evaluate COUNTERS.bump('llm_turn_cap_exhausted'); retain side effects and discard the expression result.
  // Source: vvaharness/backends/llm/sdk.py:1571-1586
  if (the source predicate response_model is not None is truthy) {
    // Source: vvaharness/backends/llm/sdk.py:1572-1578
    In source order: Evaluate messages.append({'role': 'user', 'content': [{'type': 'text', 'text': source_template_1575_33}]}); retain side effects and discard the expression result.
  }
  else {
    // Source: vvaharness/backends/llm/sdk.py:1580-1586
    In source order: Evaluate messages.append({'role': 'user', 'content': [{'type': 'text', 'text': 'Tool budget exhausted. Reply now with your final answer based on what you have read so far; do not call any tool.'}]}); retain side effects and discard the expression result.
  }
  // Source: vvaharness/backends/llm/sdk.py:1587-1587
  In source order: Evaluate once {k: v for k, v in base_kw.items() if k != 'tools'}; assign in source target order to final_kw.
  // Source: vvaharness/backends/llm/sdk.py:1593-1598
  if (the source predicate response_model is None is truthy) {
    // Source: vvaharness/backends/llm/sdk.py:1594-1594
    In source order: Evaluate once {'type': 'none'}; assign in source target order to final_kw['tool_choice'].
  }
  else {
    // Source: vvaharness/backends/llm/sdk.py:1595-1598
    if (the source predicate _forcing_blocked(model, final_kw.get('thinking')) is truthy) {
      // Source: vvaharness/backends/llm/sdk.py:1596-1596
      In source order: Evaluate final_kw.pop('tool_choice', None); retain side effects and discard the expression result.
    }
    else {
      // Source: vvaharness/backends/llm/sdk.py:1598-1598
      In source order: Evaluate once {'type': 'tool', 'name': _RESPONSE_MODEL_TOOL_NAME}; assign in source target order to final_kw['tool_choice'].
    }
  }
  // Source: vvaharness/backends/llm/sdk.py:1599-1603
  In source order: Evaluate once tools; assign in source target order to final_kw['tools']. Then Evaluate once 0; assign in source target order to final_transients.
  // Source: vvaharness/backends/llm/sdk.py:1604-1667
  while (the source predicate True is truthy) {
    // Source: vvaharness/backends/llm/sdk.py:1605-1667
    Perform the following protected operations {
      // Source: vvaharness/backends/llm/sdk.py:1606-1608
      In source order: Evaluate once time.monotonic(); assign in source target order to _t0. Then Evaluate once turn_options(session_t0, session_budget, request_timeout); assign in source target order to send. Then Evaluate once client.with_options(**send); assign in source target order to final_client.
      // Source: vvaharness/backends/llm/sdk.py:1609-1613
      Enter source context managers left-to-right: final_client.messages.stream(messages=_with_cache_marker(client, messages), **final_kw) bound to stream {
        // Source: vvaharness/backends/llm/sdk.py:1611-1613
        In source order: Evaluate once _drain_within_deadline(stream, deadline=_t0 + send['timeout'], stage=tag, effort=effort, budget_s=request_timeout); assign in source target order to msg.
      }
      Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
      // Source: vvaharness/backends/llm/sdk.py:1614-1614
      In source order: Evaluate note_budget_use(time.monotonic() - _t0, request_timeout, effort); retain side effects and discard the expression result.
      // Source: vvaharness/backends/llm/sdk.py:1615-1615
      Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
    }
    // Source: vvaharness/backends/llm/sdk.py:1616-1644
    On the first matching source exception anthropic.APIStatusError as e, in handler order {
      // Source: vvaharness/backends/llm/sdk.py:1617-1620
      if (the source predicate _auth_failure_sdk(e) is truthy) {
        // Source: vvaharness/backends/llm/sdk.py:1618-1620
        Raise AuthenticationError(redact(str(getattr(e, 'message', e)))[:400], status_code=e.status_code, backend='sdk') with explicit source cause e.
      }
      // Source: vvaharness/backends/llm/sdk.py:1622-1628
      if (the source predicate _unforce_rejected_tool_choice(final_kw, e, rejection_text(e).lower(), client=client, model=model, system_prompt=system_prompt, response_model=response_model, tools_text=json.dumps(final_kw['tools'], default=str)) is truthy) {
        // Source: vvaharness/backends/llm/sdk.py:1628-1628
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/backends/llm/sdk.py:1629-1639
      if (the source predicate _is_transient_sdk(e) and final_transients < 4 is truthy) {
        // Source: vvaharness/backends/llm/sdk.py:1630-1631
        In source order: Apply source augmented assignment final_transients += 1 with source evaluation/in-place semantics. Then Evaluate once jittered_delay(min(60, 20 * final_transients)); assign in source target order to wait.
        // Source: vvaharness/backends/llm/sdk.py:1632-1634
        if (the source predicate (overrun := wait_overrun(wait, session_t0, session_budget, stage=tag or '', route='sdk', effort=effort)) is truthy) {
          // Source: vvaharness/backends/llm/sdk.py:1634-1634
          Raise overrun with explicit source cause e.
        }
        // Source: vvaharness/backends/llm/sdk.py:1635-1638
        In source order: Evaluate console.write(source_template_1635_30); retain side effects and discard the expression result. Then Evaluate time.sleep(wait); retain side effects and discard the expression result.
        // Source: vvaharness/backends/llm/sdk.py:1639-1639
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/backends/llm/sdk.py:1640-1644
      Raise RuntimeError(redact(source_template_1641_16)) with explicit source cause e.
    }
    // Source: vvaharness/backends/llm/sdk.py:1645-1667
    On the first matching source exception (anthropic.APIConnectionError, httpx2.TransportError) as e, in handler order {
      // Source: vvaharness/backends/llm/sdk.py:1646-1650
      if (the source predicate is_timeout_failure(e) is truthy) {
        // Source: vvaharness/backends/llm/sdk.py:1647-1650
        Raise call_timeout_error(stage=tag or '', route='sdk', budget_s=request_timeout, effort=effort, cause_text=source_template_1649_31) with explicit source cause e.
      }
      // Source: vvaharness/backends/llm/sdk.py:1651-1652
      if (the source predicate (proxy := proxy_error(e, backend='sdk')) is truthy) {
        // Source: vvaharness/backends/llm/sdk.py:1652-1652
        Raise proxy with explicit source cause e.
      }
      // Source: vvaharness/backends/llm/sdk.py:1653-1662
      if (the source predicate final_transients < 4 is truthy) {
        // Source: vvaharness/backends/llm/sdk.py:1654-1655
        In source order: Apply source augmented assignment final_transients += 1 with source evaluation/in-place semantics. Then Evaluate once jittered_delay(min(60, 20 * final_transients)); assign in source target order to wait.
        // Source: vvaharness/backends/llm/sdk.py:1656-1658
        if (the source predicate (overrun := wait_overrun(wait, session_t0, session_budget, stage=tag or '', route='sdk', effort=effort)) is truthy) {
          // Source: vvaharness/backends/llm/sdk.py:1658-1658
          Raise overrun with explicit source cause e.
        }
        // Source: vvaharness/backends/llm/sdk.py:1659-1661
        In source order: Evaluate console.write(source_template_1659_30); retain side effects and discard the expression result. Then Evaluate time.sleep(wait); retain side effects and discard the expression result.
        // Source: vvaharness/backends/llm/sdk.py:1662-1662
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/backends/llm/sdk.py:1663-1667
      Raise RuntimeError(redact(source_template_1664_16)) with explicit source cause e.
    }
  }
  // Source: vvaharness/backends/llm/sdk.py:1668-1671
  if (the source predicate msg.usage is truthy) {
    // Source: vvaharness/backends/llm/sdk.py:1669-1671
    In source order: Evaluate once cast('TokenUsage', msg.usage.model_dump()); assign in source target order to final_usage. Then Evaluate _note_unparsed_cache_keys(final_usage); retain side effects and discard the expression result. Then Evaluate TOKENS.add(final_usage); retain side effects and discard the expression result.
  }
  // Source: vvaharness/backends/llm/sdk.py:1672-1676
  In source order: Evaluate once _check_agentic_stop(msg, client=client, messages=messages, call_kw=final_kw, model=model, tag=tag, requested=out_cap, response_model=response_model, effort=effort, request_timeout=request_timeout, session_t0=session_t0, session_budget=session_budget); assign in source target order to (msg, override).
  // Source: vvaharness/backends/llm/sdk.py:1677-1678
  if (the source predicate override is not None is truthy) {
    // Source: vvaharness/backends/llm/sdk.py:1678-1678
    End this invocation with override.
  }
  // Source: vvaharness/backends/llm/sdk.py:1680-1680
  In source order: Evaluate _raise_if_refused(msg, tag=tag); retain side effects and discard the expression result.
  // Source: vvaharness/backends/llm/sdk.py:1681-1682
  if (the source predicate response_model is not None is truthy) {
    // Source: vvaharness/backends/llm/sdk.py:1682-1682
    End this invocation with _extract_response_model(response_model, msg, model=model).model_dump_json().
  }
  // Source: vvaharness/backends/llm/sdk.py:1683-1684
  End this invocation with ''.join((b.text for b in msg.content if getattr(b, 'type', None) == 'text')).strip().
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.util import logs` at source line 37: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import logs` at source line 37: `source_detail/vvaharness/util/logs.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.limits import MODEL_MAX_OUTPUT_TOKENS` at source line 42: `source_detail/vvaharness/backends/harness/deepagents/limits.py.sudo.md`.
- `from vvaharness.backends.harness.models import AuthenticationError, TruncatedResponseError` at source line 43: `source_detail/vvaharness/backends/harness/models.py.sudo.md`.
- `from vvaharness.backends.llm import cache as _cache` at source line 47: `source_detail/vvaharness/backends/llm/__init__.py.sudo.md`.
- `from vvaharness.backends.llm import cache as _cache` at source line 47: `source_detail/vvaharness/backends/llm/cache.py.sudo.md`.
- `from vvaharness.backends.llm import tools as _localtools` at source line 48: `source_detail/vvaharness/backends/llm/__init__.py.sudo.md`.
- `from vvaharness.backends.llm import tools as _localtools` at source line 48: `source_detail/vvaharness/backends/llm/tools.py.sudo.md`.
- `from vvaharness.backends.llm.cli import _truncation_error` at source line 49: `source_detail/vvaharness/backends/llm/cli/__init__.py.sudo.md`.
- `from vvaharness.backends.llm.models import AGENTIC_MAX_TOKENS, ANTHROPIC_STOP_REFUSAL, DEFAULT_READ_TOOLS, DEFAULT_REQUEST_TIMEOUT_SECONDS, PARAM_REJECTION_STATUS, RATE_LIMIT_TRANSIENT_RX, RESPONSE_MODEL_TOOL_NAME, RETRYABLE_STATUS, SERVER_ERROR_TRANSIENT_RX, STRUCTURED_PROSE_REASK, STRUCTURED_REASK_MAX, TRUNCATED_REPLIES_COUNTER, TRUNCATED_RETRY_ATTEMPTED_COUNTER, TRUNCATED_RETRY_RECOVERED_COUNTER, ClockKind, SdkConfig, call_timeout_error, cause_chain, effort_scaled_seconds, finish_truncated, is_gateway_wrapped_param_rejection, jittered_delay, model_refusal, note_budget_use, proxy_error, rejection_text, response_model_tool, truncation_retry_max, turn_options, wait_overrun, with_submit_instruction` at source line 50: `source_detail/vvaharness/backends/llm/models.py.sudo.md`.
- `from vvaharness.backends.llm.tls import anthropic_auth_kwargs, coerce_verify, load_client_chain, resolve_client_chain, scoped_no_proxy_env, warn_verify_disabled` at source line 83: `source_detail/vvaharness/backends/llm/tls.py.sudo.md`.
- `from vvaharness.report.redact import redact` at source line 91: `source_detail/vvaharness/report/redact.py.sudo.md`.
- `from vvaharness.util import console` at source line 92: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import console` at source line 92: `source_detail/vvaharness/util/console.py.sudo.md`.
- `from vvaharness.util import errlog as _errlog` at source line 93: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import errlog as _errlog` at source line 93: `source_detail/vvaharness/util/errlog.py.sudo.md`.
- `from vvaharness.util.counters import COUNTERS` at source line 94: `source_detail/vvaharness/util/counters.py.sudo.md`.
- `from vvaharness.util.events import Event` at source line 95: `source_detail/vvaharness/util/events.py.sudo.md`.
- `from vvaharness.util.response_quality import StructuredOutputRejected, check_response_quality, is_timeout_failure, output_tokens_for_gate, structured_failure_detail` at source line 96: `source_detail/vvaharness/util/response_quality.py.sudo.md`.
- `from vvaharness.util.scan_progress import is_stage_only` at source line 103: `source_detail/vvaharness/util/scan_progress.py.sudo.md`.
- `from vvaharness.util.tokens import TOKENS, TokenUsage, estimate_tokens` at source line 104: `source_detail/vvaharness/util/tokens.py.sudo.md`.
- `from vvaharness.util.warn_once import warn_once` at source line 105: `source_detail/vvaharness/util/warn_once.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.options.model_building import _anthropic_thinking_kwargs` at source line 605: `source_detail/vvaharness/backends/harness/deepagents/options/model_building.py.sudo.md`.
- `from vvaharness.backends.llm import agent_sdk as _agent_sdk` at source line 1267: `source_detail/vvaharness/backends/llm/__init__.py.sudo.md`.
- `from vvaharness.backends.llm import agent_sdk as _agent_sdk` at source line 1267: `source_detail/vvaharness/backends/llm/agent_sdk.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../prompt_representation/vvaharness/backends/llm/sdk.py.sudo.md). Exact strings in the evidence asset support this conversion.
