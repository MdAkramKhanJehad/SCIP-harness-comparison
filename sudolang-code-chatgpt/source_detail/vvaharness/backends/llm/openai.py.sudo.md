# vvaharness/backends/llm/openai.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/backends/llm/openai.py.evidence.json`. SHA-256: `a057576efd0869513a1cfb23f514f038aa18a2161070aa6ed5b6e2991afb2026`.

```sudo
// Source: vvaharness/backends/llm/openai.py:15-37
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import hashlib; preserve alias and import-time effects. Then Resolve source import import json; preserve alias and import-time effects. Then Resolve source import import os; preserve alias and import-time effects.
// Source: vvaharness/backends/llm/openai.py:38-43
In source order: Resolve source import import re; preserve alias and import-time effects. Then Resolve source import import threading; preserve alias and import-time effects. Then Resolve source import import time; preserve alias and import-time effects. Then Resolve source import from typing import TYPE_CHECKING, Any, Final, NamedTuple; preserve alias and import-time effects. Then Resolve source import import openai; preserve alias and import-time effects.
// Source: vvaharness/backends/llm/openai.py:45-45
In source order: Resolve source import from vvaharness.util import logs; preserve alias and import-time effects.
// Source: vvaharness/backends/llm/openai.py:47-52
if (the source predicate TYPE_CHECKING is truthy) {
  // Source: vvaharness/backends/llm/openai.py:48-52
  In source order: Resolve source import from collections.abc import Callable; preserve alias and import-time effects. Then Resolve source import from pydantic import BaseModel; preserve alias and import-time effects.
}
// Source: vvaharness/backends/llm/openai.py:54-109
In source order: Resolve source import from vvaharness.backends.harness.models import AuthenticationError, TruncatedResponseError, truncated_below_budget; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm import cache as _cache; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm import tools as _localtools; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm.models import AGENTIC_MAX_TOKENS, DEFAULT_READ_TOOLS, DEFAULT_REQUEST_TIMEOUT_SECONDS, EFFORT_REJECTIONS, LLM_TRUNCATED_BELOW_BUDGET_COUNTER, OPENAI_FINISH_LENGTH, RATE_LIMIT_TRANSIENT_RX, REASONING_OFF, RESPONSE_MODEL_TOOL_NAME, RETRYABLE_STATUS, SERVER_ERROR_STATUS, SERVER_ERROR_TRANSIENT_RX, STRUCTURED_PROSE_REASK, STRUCTURED_REASK_MAX, TRANSPORT_CHAT, TRANSPORT_MEMORY, TRANSPORT_RESPONSES, TRUNCATED_REPLIES_COUNTER, TRUNCATED_RETRY_ATTEMPTED_COUNTER, TRUNCATED_RETRY_RECOVERED_COUNTER, ClockKind, OpenAiConfig, _tiers_key, call_timeout_error, classify_effort_rejection, effort_after_rejections, effort_scaled_seconds, is_param_rejection, is_responses_shape_rejection, jittered_delay, model_refusal, model_refusal_from, next_effort_tier, note_budget_use, proxy_error, rejection_text, response_model_tool, step_down, truncation_retry_max, turn_options, wait_overrun; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm.openai_responses import REASONING_ITEMS_KEY, from_response, to_chat_messages, to_responses_request; preserve alias and import-time effects.
// Source: vvaharness/backends/llm/openai.py:110-118
In source order: Resolve source import from vvaharness.backends.llm.tls import coerce_verify, scoped_no_proxy_env, warn_verify_disabled; preserve alias and import-time effects. Then Resolve source import from vvaharness.report.redact import redact; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import console; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import errlog as _errlog; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.counters import COUNTERS; preserve alias and import-time effects.
// Source: vvaharness/backends/llm/openai.py:119-128
In source order: Resolve source import from vvaharness.util.events import Event; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.response_quality import check_response_quality, is_timeout_failure, output_tokens_for_gate, structured_failure_detail; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.scan_progress import get_active_tracker, is_stage_only; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.tokens import TOKENS, TokenUsage, estimate_tokens; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.warn_once import warn_once; preserve alias and import-time effects.
// Source: vvaharness/backends/llm/openai.py:130-152
In source order: Evaluate once logs.get_logger(__name__); assign in source target order to log. Then Evaluate once re.compile(source_literal_139_4, re.IGNORECASE); assign in source target order to _AUTH_STATUS_RX_OAI. Then Evaluate once 3; assign in source target order to _AUTH_MAX_RETRIES_OAI. Then Evaluate once (2, 4, 8); assign in source target order to _AUTH_BACKOFF_OAI. Then Evaluate once re.compile('(sk-[A-Za-z0-9_-]{6})[A-Za-z0-9_-]+'); assign in source target order to _REDACT_RX.
// Source: vvaharness/backends/llm/openai.py:154-156
In source order: Evaluate once re.compile('(?:class="[^"]*\\brsn\\b[^"]*">\\s*|class="[^"]*\\breason\\b[^"]*">\\s*|reason=)([^<&\\n]{1,200})', re.I); assign in source target order to _PROXY_REASON_RX.
// Source: vvaharness/backends/llm/openai.py:159-176
// Source signature: _summarise_status_error(e) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _summarise_status_error(e) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/openai.py:160-162
  In source order: Retain source documentation literal source_literal_160_4; it is not a model call. Then Evaluate once ''; assign in source target order to body. Then Evaluate once getattr(e, 'response', None); assign in source target order to resp.
  // Source: vvaharness/backends/llm/openai.py:163-167
  if (the source predicate resp is not None is truthy) {
    // Source: vvaharness/backends/llm/openai.py:164-167
    Perform the following protected operations {
      // Source: vvaharness/backends/llm/openai.py:165-165
      In source order: Evaluate once resp.text; assign in source target order to body.
    }
    // Source: vvaharness/backends/llm/openai.py:166-167
    On the first matching source exception Exception, in handler order {
      // Source: vvaharness/backends/llm/openai.py:167-167
      In source order: Evaluate once ''; assign in source target order to body.
    }
  }
  // Source: vvaharness/backends/llm/openai.py:168-169
  In source order: Evaluate once body or str(getattr(e, 'message', '') or e); assign in source target order to body. Then Evaluate once body.lower(); assign in source target order to low.
  // Source: vvaharness/backends/llm/openai.py:170-175
  if (the source predicate 'dlp' in low or '<html' in low is truthy) {
    // Source: vvaharness/backends/llm/openai.py:171-172
    In source order: Evaluate once _PROXY_REASON_RX.search(body); assign in source target order to m. Then Evaluate once _scrub_secrets(m.group(1).strip() if m else 'policy block'); assign in source target order to reason.
    // Source: vvaharness/backends/llm/openai.py:173-175
    End this invocation with source_template_173_16.
  }
  // Source: vvaharness/backends/llm/openai.py:176-176
  End this invocation with redact(_scrub_secrets(body))[:300].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/openai.py:180-183
In source order: Evaluate once re.compile('(?im)^(.*?\\b(authorization|api[-_ ]?key|x-api-key|cookie|set-cookie|token|secret|bearer)\\b\\s*[:=]\\s*).+$'); assign in source target order to _SECRET_LINE_RX. Then Evaluate once re.compile('(?i)\\b(bearer\\s+)[A-Za-z0-9._\\-]+'); assign in source target order to _BEARER_RX.
// Source: vvaharness/backends/llm/openai.py:186-192
// Source signature: _scrub_secrets(text: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _scrub_secrets(text) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/openai.py:187-188
  if (the source predicate not text is truthy) {
    // Source: vvaharness/backends/llm/openai.py:188-188
    End this invocation with text.
  }
  // Source: vvaharness/backends/llm/openai.py:189-191
  In source order: Evaluate once _REDACT_RX.sub('\\1***', text); assign in source target order to text. Then Evaluate once _BEARER_RX.sub('\\1***', text); assign in source target order to text. Then Evaluate once _SECRET_LINE_RX.sub('\\1***', text); assign in source target order to text.
  // Source: vvaharness/backends/llm/openai.py:192-192
  End this invocation with text.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/openai.py:195-201
// Source signature: _cause_chain(e: Exception) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _cause_chain(e) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/openai.py:196-196
  In source order: Evaluate once ([], e.__cause__); assign in source target order to (parts, c).
  // Source: vvaharness/backends/llm/openai.py:197-199
  while (the source predicate c is not None is truthy) {
    // Source: vvaharness/backends/llm/openai.py:198-199
    In source order: Evaluate parts.append(source_template_198_21); retain side effects and discard the expression result. Then Evaluate once c.__cause__; assign in source target order to c.
  }
  // Source: vvaharness/backends/llm/openai.py:200-200
  In source order: Evaluate once ' <- '.join(parts) or 'no underlying cause reported'; assign in source target order to detail.
  // Source: vvaharness/backends/llm/openai.py:201-201
  End this invocation with _REDACT_RX.sub('\\1***', detail).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/openai.py:204-231
// Source signature: _payload_shape(messages: list[dict], error_body: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _payload_shape(messages, error_body) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/openai.py:205-208
  In source order: Retain source documentation literal source_literal_205_4; it is not a model call. Then Evaluate once 0; assign in source target order to chars. Then For block_types, assign set(); source annotation set[str]. Then Evaluate once 0; assign in source target order to markers.
  // Source: vvaharness/backends/llm/openai.py:209-222
  for each m in messages {
    // Source: vvaharness/backends/llm/openai.py:210-210
    In source order: Evaluate once m.get('content'); assign in source target order to c.
    // Source: vvaharness/backends/llm/openai.py:211-222
    if (the source predicate isinstance(c, str) is truthy) {
      // Source: vvaharness/backends/llm/openai.py:212-214
      In source order: Evaluate block_types.add('text'); retain side effects and discard the expression result. Then Apply source augmented assignment chars += len(c) with source evaluation/in-place semantics. Then Apply source augmented assignment markers += c.count('data:image/') with source evaluation/in-place semantics.
    }
    else {
      // Source: vvaharness/backends/llm/openai.py:215-222
      if (the source predicate isinstance(c, list) is truthy) {
        // Source: vvaharness/backends/llm/openai.py:216-222
        for each b in c {
          // Source: vvaharness/backends/llm/openai.py:217-222
          if (the source predicate isinstance(b, dict) is truthy) {
            // Source: vvaharness/backends/llm/openai.py:218-219
            In source order: Evaluate block_types.add(str(b.get('type') or '?')); retain side effects and discard the expression result. Then Evaluate once b.get('text'); assign in source target order to t.
            // Source: vvaharness/backends/llm/openai.py:220-222
            if (the source predicate isinstance(t, str) is truthy) {
              // Source: vvaharness/backends/llm/openai.py:221-222
              In source order: Apply source augmented assignment chars += len(t) with source evaluation/in-place semantics. Then Apply source augmented assignment markers += t.count('data:image/') with source evaluation/in-place semantics.
            }
          }
        }
      }
    }
  }
  // Source: vvaharness/backends/llm/openai.py:223-225
  In source order: Evaluate once source_template_223_12; assign in source target order to line.
  // Source: vvaharness/backends/llm/openai.py:226-230
  if (the source predicate 'image' in error_body.lower() and block_types <= {'text'} is truthy) {
    // Source: vvaharness/backends/llm/openai.py:227-230
    In source order: Apply source augmented assignment line += source_literal_227_17 with source evaluation/in-place semantics.
  }
  // Source: vvaharness/backends/llm/openai.py:231-231
  End this invocation with line.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/openai.py:236-242
In source order: Evaluate once None; assign in source target order to _client. Then Evaluate once threading.Lock(); assign in source target order to _client_lock. Then For _cfg, assign {'api_key': None, 'base_url': None, 'verify_ssl': True, 'ca_cert': None, 'organization': None, 'no_proxy': None, 'cache_markers': 'on'}; source annotation OpenAiConfig.
// Source: vvaharness/backends/llm/openai.py:245-277
// Source signature: configure(*, api_key: str | None=None, base_url: str | None=None, verify_ssl: bool | str | None=None, ca_cert: str | None=None, client_cert: str | tuple | list | None=None, organization: str | None=None, no_proxy: str | None=None, cache_markers: str | None=None) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn configure(api_key, base_url, verify_ssl, ca_cert, client_cert, organization, no_proxy, cache_markers) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/openai.py:252-253
  In source order: Retain source documentation literal source_literal_252_4; it is not a model call. Then Bind names in module scope: _client.
  // Source: vvaharness/backends/llm/openai.py:254-277
  Enter source context managers left-to-right: _client_lock {
    // Source: vvaharness/backends/llm/openai.py:255-256
    if (the source predicate api_key is truthy) {
      // Source: vvaharness/backends/llm/openai.py:256-256
      In source order: Evaluate once api_key; assign in source target order to _cfg['api_key'].
    }
    // Source: vvaharness/backends/llm/openai.py:257-258
    if (the source predicate base_url is truthy) {
      // Source: vvaharness/backends/llm/openai.py:258-258
      In source order: Evaluate once base_url; assign in source target order to _cfg['base_url'].
    }
    // Source: vvaharness/backends/llm/openai.py:259-260
    if (the source predicate verify_ssl is not None is truthy) {
      // Source: vvaharness/backends/llm/openai.py:260-260
      In source order: Evaluate once coerce_verify(verify_ssl); assign in source target order to _cfg['verify_ssl'].
    }
    // Source: vvaharness/backends/llm/openai.py:261-262
    if (the source predicate ca_cert is truthy) {
      // Source: vvaharness/backends/llm/openai.py:262-262
      In source order: Evaluate once ca_cert; assign in source target order to _cfg['ca_cert'].
    }
    // Source: vvaharness/backends/llm/openai.py:263-270
    if (the source predicate client_cert is truthy) {
      // Source: vvaharness/backends/llm/openai.py:267-270
      In source order: Evaluate log.warning(source_literal_267_24); retain side effects and discard the expression result.
    }
    // Source: vvaharness/backends/llm/openai.py:271-272
    if (the source predicate organization is truthy) {
      // Source: vvaharness/backends/llm/openai.py:272-272
      In source order: Evaluate once organization; assign in source target order to _cfg['organization'].
    }
    // Source: vvaharness/backends/llm/openai.py:273-274
    if (the source predicate no_proxy is truthy) {
      // Source: vvaharness/backends/llm/openai.py:274-274
      In source order: Evaluate once no_proxy; assign in source target order to _cfg['no_proxy'].
    }
    // Source: vvaharness/backends/llm/openai.py:275-276
    if (the source predicate cache_markers is not None is truthy) {
      // Source: vvaharness/backends/llm/openai.py:276-276
      In source order: Evaluate once cache_markers; assign in source target order to _cfg['cache_markers'].
    }
    // Source: vvaharness/backends/llm/openai.py:277-277
    In source order: Evaluate once None; assign in source target order to _client.
  }
  Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/openai.py:280-318
// Source signature: _get_client()
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _get_client() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/openai.py:281-281
  In source order: Bind names in module scope: _client.
  // Source: vvaharness/backends/llm/openai.py:282-283
  if (the source predicate _client is not None is truthy) {
    // Source: vvaharness/backends/llm/openai.py:283-283
    End this invocation with _client.
  }
  // Source: vvaharness/backends/llm/openai.py:284-317
  Enter source context managers left-to-right: _client_lock {
    // Source: vvaharness/backends/llm/openai.py:285-317
    if (the source predicate _client is None is truthy) {
      // Source: vvaharness/backends/llm/openai.py:291-292
      In source order: For kw, assign {'max_retries': 2}; source annotation dict. Then Evaluate once _cfg['api_key'] or os.environ.get('OPENAI_API_KEY'); assign in source target order to key.
      // Source: vvaharness/backends/llm/openai.py:293-295
      if (the source predicate key is truthy) {
        // Source: vvaharness/backends/llm/openai.py:295-295
        In source order: Evaluate once key.strip(); assign in source target order to kw['api_key'].
      }
      // Source: vvaharness/backends/llm/openai.py:297-299
      In source order: Evaluate once _cfg['base_url'] or os.environ.get('OPENAI_BASE_URL') or 'https://api.openai.com/v1'; assign in source target order to kw['base_url'].
      // Source: vvaharness/backends/llm/openai.py:300-301
      if (the source predicate _cfg['organization'] is truthy) {
        // Source: vvaharness/backends/llm/openai.py:301-301
        In source order: Evaluate once _cfg['organization']; assign in source target order to kw['organization'].
      }
      // Source: vvaharness/backends/llm/openai.py:302-302
      In source order: Evaluate once _cfg['ca_cert']; assign in source target order to ca.
      // Source: vvaharness/backends/llm/openai.py:303-305
      if (the source predicate ca and (not os.path.exists(ca)) is truthy) {
        // Source: vvaharness/backends/llm/openai.py:304-305
        In source order: Evaluate log.warning(Event.TLS_CA_FALLBACK, path=ca, verify_ssl=_cfg['verify_ssl']); retain side effects and discard the expression result. Then Evaluate once None; assign in source target order to ca.
      }
      // Source: vvaharness/backends/llm/openai.py:306-306
      In source order: Evaluate once ca or _cfg['verify_ssl']; assign in source target order to verify.
      // Source: vvaharness/backends/llm/openai.py:307-309
      if (the source predicate verify is False is truthy) {
        // Source: vvaharness/backends/llm/openai.py:308-309
        In source order: Evaluate warn_verify_disabled(kw.get('base_url'), label='openai', ca_hint='openai.ca_cert'); retain side effects and discard the expression result.
      }
      // Source: vvaharness/backends/llm/openai.py:314-317
      Enter source context managers left-to-right: scoped_no_proxy_env(_cfg.get('no_proxy')) {
        // Source: vvaharness/backends/llm/openai.py:315-316
        if (the source predicate verify is not True is truthy) {
          // Source: vvaharness/backends/llm/openai.py:316-316
          In source order: Evaluate once openai.DefaultHttpxClient(verify=verify); assign in source target order to kw['http_client'].
        }
        // Source: vvaharness/backends/llm/openai.py:317-317
        In source order: Evaluate once openai.OpenAI(**kw); assign in source target order to _client.
      }
      Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    }
  }
  Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
  // Source: vvaharness/backends/llm/openai.py:318-318
  End this invocation with _client.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/openai.py:321-323
// Source signature: _cache_markers_enabled() -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _cache_markers_enabled() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/openai.py:322-322
  In source order: Retain source documentation literal source_literal_322_4; it is not a model call.
  // Source: vvaharness/backends/llm/openai.py:323-323
  End this invocation with _cache.markers_enabled(_cfg).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/openai.py:330-338
In source order: Evaluate once 1024; assign in source target order to _CACHE_MIN_PROMPT_TOKENS. Then Evaluate once 8; assign in source target order to _CACHE_KEY_SHARDS. Then Evaluate once _cache.CACHE_EST_MARGIN; assign in source target order to _CACHE_EST_MARGIN.
// Source: vvaharness/backends/llm/openai.py:341-350
// Source signature: _prefix_meets_cache_minimum(text: str | None, *, preceding: str='') -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _prefix_meets_cache_minimum(text, preceding) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/openai.py:343-343
  In source order: Retain source documentation literal source_literal_343_4; it is not a model call.
  // Source: vvaharness/backends/llm/openai.py:347-348
  if (the source predicate not text is truthy) {
    // Source: vvaharness/backends/llm/openai.py:348-348
    End this invocation with False.
  }
  // Source: vvaharness/backends/llm/openai.py:349-349
  In source order: Evaluate once estimate_tokens(preceding or '') + estimate_tokens(text); assign in source target order to est.
  // Source: vvaharness/backends/llm/openai.py:350-350
  End this invocation with est * _CACHE_EST_MARGIN >= _CACHE_MIN_PROMPT_TOKENS.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/openai.py:353-378
// Source signature: _prompt_cache_key(tag: str | None, model: str, cache_prefix: str | None=None, *, preceding: str='') -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _prompt_cache_key(tag, model, cache_prefix, preceding) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/openai.py:356-366
  In source order: Retain source documentation literal source_literal_356_4; it is not a model call. Then Evaluate once (tag or '').split(None, 1); assign in source target order to fields. Then Evaluate once fields[0] if fields else ''; assign in source target order to stage. Then Evaluate once get_active_tracker(); assign in source target order to tracker. Then Evaluate once getattr(tracker, 'repo_name', '') or '' if tracker else ''; assign in source target order to repo_name.
  // Source: vvaharness/backends/llm/openai.py:367-367
  In source order: Evaluate once ''; assign in source target order to bucket.
  // Source: vvaharness/backends/llm/openai.py:368-376
  if (the source predicate cache_prefix is truthy) {
    // Source: vvaharness/backends/llm/openai.py:369-376
    if (the source predicate _prefix_meets_cache_minimum(cache_prefix, preceding=preceding) is truthy) {
      // Source: vvaharness/backends/llm/openai.py:370-371
      In source order: Evaluate once hashlib.sha256(cache_prefix.encode('utf-8')).hexdigest()[:12]; assign in source target order to bucket.
    }
    else {
      // Source: vvaharness/backends/llm/openai.py:373-376
      In source order: Evaluate once fields[1] if len(fields) > 1 else ''; assign in source target order to rest. Then Evaluate once int(hashlib.sha256(rest.encode('utf-8')).hexdigest(), 16) % _CACHE_KEY_SHARDS; assign in source target order to shard. Then Evaluate once source_template_376_21; assign in source target order to bucket.
    }
  }
  // Source: vvaharness/backends/llm/openai.py:377-377
  In source order: Evaluate once source_template_377_10; assign in source target order to raw.
  // Source: vvaharness/backends/llm/openai.py:378-378
  End this invocation with hashlib.sha256(raw.encode('utf-8')).hexdigest()[:32].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/openai.py:384-391
In source order: For _MAX_TOKENS_KEY, assign 'max_tokens'; source annotation Final. Then For _MAX_COMPLETION_TOKENS_KEY, assign 'max_completion_tokens'; source annotation Final. Then For _MAX_OUTPUT_TOKENS_KEY, assign 'max_output_tokens'; source annotation Final. Then For _ATTEMPTS_CEILING, assign 6; source annotation Final. Then For _AGENTIC_TRANSIENT_RETRIES, assign 4; source annotation Final.
// Source: vvaharness/backends/llm/openai.py:393-410
In source order: For _NO_TEMP_MODELS, assign set(); source annotation set[str]. Then For _USE_LEGACY_MAXTOK, assign set(); source annotation set[str]. Then For _LEARNED_OUTPUT_CAP, assign {}; source annotation dict[str, int]. Then For _CAP_VALUE_RX, assign re.compile('\\b(\\d{4,7})\\b'); source annotation Final. Then For _SDK_ERROR_PREFIX_RX, assign re.compile('^error code:\\s*\\d+\\s*-\\s*'); source annotation Final.
// Source: vvaharness/backends/llm/openai.py:413-417
// Source signature: _learned_cap_from_body(body: str, *, requested: int) -> int | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _learned_cap_from_body(body, requested) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/openai.py:414-416
  In source order: Evaluate once _SDK_ERROR_PREFIX_RX.sub('', body.strip()); assign in source target order to body. Then Evaluate once {int(n) for n in _CAP_VALUE_RX.findall(body)}; assign in source target order to candidates. Then Evaluate once {n for n in candidates if 0 < n < requested}; assign in source target order to candidates.
  // Source: vvaharness/backends/llm/openai.py:417-417
  End this invocation with candidates.pop() if len(candidates) == 1 else None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/openai.py:420-427
In source order: For _NO_CACHE_KEY_MODELS, assign set(); source annotation set[str]. Then For _NO_TOOL_CHOICE_MODELS, assign set(); source annotation set[str]. Then For _NO_REASONING_EFFORT_MODELS, assign EFFORT_REJECTIONS.field; source annotation set[str].
// Source: vvaharness/backends/llm/openai.py:430-450
// Source signature: _reasoning_effort_kw(model: str, effort: str | None, transport: str=TRANSPORT_CHAT, *, with_tools: bool=False) -> dict
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _reasoning_effort_kw(model, effort, transport, with_tools) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/openai.py:432-437
  In source order: Retain source documentation literal source_literal_432_4; it is not a model call.
  // Source: vvaharness/backends/llm/openai.py:442-443
  if (the source predicate with_tools and transport == TRANSPORT_CHAT and (model in EFFORT_REJECTIONS.tools_off) is truthy) {
    // Source: vvaharness/backends/llm/openai.py:443-443
    End this invocation with {'reasoning_effort': REASONING_OFF}.
  }
  // Source: vvaharness/backends/llm/openai.py:444-445
  if (the source predicate effort is None or model in _NO_REASONING_EFFORT_MODELS is truthy) {
    // Source: vvaharness/backends/llm/openai.py:445-445
    End this invocation with {}.
  }
  // Source: vvaharness/backends/llm/openai.py:446-449
  In source order: Resolve source import from vvaharness.backends.harness.deepagents.options.model_building import _to_openai_reasoning_effort; preserve alias and import-time effects. Then Evaluate once effort_after_rejections(model, _to_openai_reasoning_effort(effort), transport); assign in source target order to tier.
  // Source: vvaharness/backends/llm/openai.py:450-450
  End this invocation with {} if tier is None else {'reasoning_effort': tier}.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/openai.py:453-455
// Source signature: _next_effort_label(nxt: str | None) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _next_effort_label(nxt) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/openai.py:454-454
  In source order: Retain source documentation literal source_literal_454_4; it is not a model call.
  // Source: vvaharness/backends/llm/openai.py:455-455
  End this invocation with repr(nxt) if nxt is not None else 'no field'.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/openai.py:459-465
In source order: For _NO_JSON_SCHEMA_MODELS, assign set(); source annotation set[str]. Then For _NO_STREAM_OPTIONS_MODELS, assign set(); source annotation set[str]. Then For _OPENAI_FINISH_CONTENT_FILTER, assign 'content_filter'; source annotation Final.
// Source: vvaharness/backends/llm/openai.py:468-473
// Source signature: _raise_if_refusal_rejection(e: openai.APIError, *, tag: str | None) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _raise_if_refusal_rejection(e, tag) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/openai.py:469-471
  In source order: Retain source documentation literal source_literal_469_4; it is not a model call. Then Evaluate once model_refusal_from(e, route='openai', stage=tag or ''); assign in source target order to refusal.
  // Source: vvaharness/backends/llm/openai.py:472-473
  if (the source predicate refusal is not None is truthy) {
    // Source: vvaharness/backends/llm/openai.py:473-473
    Raise refusal with explicit source cause e.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/openai.py:476-476
In source order: For _WARNED_DROPS, assign set(); source annotation set[str].
// Source: vvaharness/backends/llm/openai.py:479-492
// Source signature: _warn_max_budget_unenforced(fn: str, max_budget_usd: float | None) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _warn_max_budget_unenforced(fn, max_budget_usd) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/openai.py:480-480
  In source order: Retain source documentation literal source_literal_480_4; it is not a model call.
  // Source: vvaharness/backends/llm/openai.py:485-486
  if (the source predicate max_budget_usd is None is truthy) {
    // Source: vvaharness/backends/llm/openai.py:486-486
    End this invocation with None.
  }
  // Source: vvaharness/backends/llm/openai.py:487-492
  In source order: Evaluate warn_once(_WARNED_DROPS, source_template_488_23, source_template_489_8); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/openai.py:496-496
In source order: Evaluate once re.compile('[^A-Za-z0-9_-]+'); assign in source target order to _SCHEMA_NAME_RX.
// Source: vvaharness/backends/llm/openai.py:499-517
// Source signature: _strict_ready(node: object) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _strict_ready(node) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/openai.py:500-500
  In source order: Retain source documentation literal source_literal_500_4; it is not a model call.
  // Source: vvaharness/backends/llm/openai.py:507-508
  if (the source predicate isinstance(node, list) is truthy) {
    // Source: vvaharness/backends/llm/openai.py:508-508
    End this invocation with all((_strict_ready(item) for item in node)).
  }
  // Source: vvaharness/backends/llm/openai.py:509-510
  if (the source predicate not isinstance(node, dict) is truthy) {
    // Source: vvaharness/backends/llm/openai.py:510-510
    End this invocation with True.
  }
  // Source: vvaharness/backends/llm/openai.py:511-511
  In source order: Evaluate once node.get('properties'); assign in source target order to props.
  // Source: vvaharness/backends/llm/openai.py:512-516
  if (the source predicate isinstance(props, dict) is truthy) {
    // Source: vvaharness/backends/llm/openai.py:513-514
    if (the source predicate node.get('additionalProperties') is not False is truthy) {
      // Source: vvaharness/backends/llm/openai.py:514-514
      End this invocation with False.
    }
    // Source: vvaharness/backends/llm/openai.py:515-516
    if (the source predicate set(props) != set(node.get('required') or ()) is truthy) {
      // Source: vvaharness/backends/llm/openai.py:516-516
      End this invocation with False.
    }
  }
  // Source: vvaharness/backends/llm/openai.py:517-517
  End this invocation with all((_strict_ready(v) for k, v in node.items() if k != 'required')).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/openai.py:520-541
// Source signature: _response_format_for(json_schema: dict | None, *, model: str, tag: str | None) -> dict
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _response_format_for(json_schema, model, tag) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/openai.py:522-522
  In source order: Retain source documentation literal source_literal_522_4; it is not a model call.
  // Source: vvaharness/backends/llm/openai.py:523-524
  if (the source predicate not json_schema or model in _NO_JSON_SCHEMA_MODELS is truthy) {
    // Source: vvaharness/backends/llm/openai.py:524-524
    End this invocation with {'type': 'json_object'}.
  }
  // Source: vvaharness/backends/llm/openai.py:525-526
  In source order: Evaluate once _SCHEMA_NAME_RX.sub('_', (tag or 'vvaharness').strip()) or 'vvaharness'; assign in source target order to name. Then Evaluate once _strict_ready(json_schema); assign in source target order to strict.
  // Source: vvaharness/backends/llm/openai.py:527-537
  if (the source predicate not strict is truthy) {
    // Source: vvaharness/backends/llm/openai.py:528-537
    In source order: Evaluate warn_once(_WARNED_DROPS, source_template_529_27, source_template_530_12); retain side effects and discard the expression result.
  }
  // Source: vvaharness/backends/llm/openai.py:538-541
  End this invocation with {'type': 'json_schema', 'json_schema': {'name': name[:64], 'schema': json_schema, 'strict': strict}}.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/openai.py:544-561
// Source signature: _is_transient_oai(error: openai.APIStatusError) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _is_transient_oai(error) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/openai.py:545-545
  In source order: Retain source documentation literal source_literal_545_4; it is not a model call.
  // Source: vvaharness/backends/llm/openai.py:546-547
  if (the source predicate error.status_code in RETRYABLE_STATUS is truthy) {
    // Source: vvaharness/backends/llm/openai.py:547-547
    End this invocation with True.
  }
  // Source: vvaharness/backends/llm/openai.py:552-553
  if (the source predicate error.status_code in (401, 403) is truthy) {
    // Source: vvaharness/backends/llm/openai.py:553-553
    End this invocation with False.
  }
  // Source: vvaharness/backends/llm/openai.py:559-559
  In source order: Evaluate once rejection_text(error); assign in source target order to body.
  // Source: vvaharness/backends/llm/openai.py:560-561
  End this invocation with bool(RATE_LIMIT_TRANSIENT_RX.search(body) or SERVER_ERROR_TRANSIENT_RX.search(body)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/openai.py:564-568
// Source signature: _auth_failure_oai(error: openai.APIStatusError) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _auth_failure_oai(error) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/openai.py:565-565
  In source order: Retain source documentation literal source_literal_565_4; it is not a model call.
  // Source: vvaharness/backends/llm/openai.py:566-568
  End this invocation with bool(error.status_code == 401 or (_AUTH_STATUS_RX_OAI.search(rejection_text(error)) and error.status_code not in RETRYABLE_STATUS)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/openai.py:571-585
// Source signature: _stream_within_deadline(stream: Any, *, deadline: float, stage: str | None, effort: str | None, budget_s: float | None) -> Any
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _stream_within_deadline(stream, deadline, stage, effort, budget_s) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/openai.py:573-578
  In source order: Retain source documentation literal source_literal_573_4; it is not a model call.
  // Source: vvaharness/backends/llm/openai.py:579-585
  for each ev in stream {
    // Source: vvaharness/backends/llm/openai.py:580-584
    if (the source predicate time.monotonic() >= deadline is truthy) {
      // Source: vvaharness/backends/llm/openai.py:581-581
      In source order: Evaluate stream.close(); retain side effects and discard the expression result.
      // Source: vvaharness/backends/llm/openai.py:582-584
      Raise call_timeout_error(stage=stage or '', route='openai', budget_s=budget_s, effort=effort, cause_text=source_template_584_27).
    }
    // Source: vvaharness/backends/llm/openai.py:585-585
    In source order: Yield ev; suspend this generator until resumed.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/openai.py:588-1102
// Source signature: prompt(user_prompt: str | list[dict], *, model: str, cache_prefix: str | None=None, system_prompt: str | None=None, max_tokens: int | None=None, temperature: float | None=None, thinking_budget: int | None=None, betas: list[str] | None=None, json_schema: dict | None=None, output_format: str='text', cwd: str | None=None, max_budget_usd: float | None=None, timeout: int | None=None, tag: str | None=None, output_cap: int | None=None, effort: str | None=None) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn prompt(user_prompt, model, cache_prefix, system_prompt, max_tokens, temperature, thinking_budget, betas, json_schema, output_format, cwd, max_budget_usd, timeout, tag, output_cap, effort) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/openai.py:613-615
  In source order: Evaluate _warn_max_budget_unenforced('prompt', max_budget_usd); retain side effects and discard the expression result. Then Evaluate once _get_client(); assign in source target order to client. Then Evaluate once max_tokens or 16000; assign in source target order to max_tok.
  // Source: vvaharness/backends/llm/openai.py:616-617
  if (the source predicate output_cap is not None is truthy) {
    // Source: vvaharness/backends/llm/openai.py:617-617
    In source order: Evaluate once min(max_tok, output_cap); assign in source target order to max_tok.
  }
  // Source: vvaharness/backends/llm/openai.py:618-618
  In source order: Evaluate once _LEARNED_OUTPUT_CAP.get(model); assign in source target order to learned_cap.
  // Source: vvaharness/backends/llm/openai.py:619-620
  if (the source predicate learned_cap is not None is truthy) {
    // Source: vvaharness/backends/llm/openai.py:620-620
    In source order: Evaluate once min(max_tok, learned_cap); assign in source target order to max_tok.
  }
  // Source: vvaharness/backends/llm/openai.py:622-622
  In source order: For messages, assign []; source annotation list[dict].
  // Source: vvaharness/backends/llm/openai.py:623-624
  if (the source predicate system_prompt is truthy) {
    // Source: vvaharness/backends/llm/openai.py:624-624
    In source order: Evaluate messages.append({'role': 'system', 'content': system_prompt}); retain side effects and discard the expression result.
  }
  // Source: vvaharness/backends/llm/openai.py:629-638
  if (the source predicate isinstance(user_prompt, list) is truthy) {
    // Source: vvaharness/backends/llm/openai.py:630-634
    In source order: For user_content, assign [{k: v for k, v in b.items() if k != 'cache_control'} for b in user_prompt if isinstance(b, dict)]; source annotation str | list.
    // Source: vvaharness/backends/llm/openai.py:635-636
    if (the source predicate cache_prefix is truthy) {
      // Source: vvaharness/backends/llm/openai.py:636-636
      In source order: Evaluate once [{'type': 'text', 'text': cache_prefix}, *user_content]; assign in source target order to user_content.
    }
  }
  else {
    // Source: vvaharness/backends/llm/openai.py:638-638
    In source order: Evaluate once cache_prefix + user_prompt if cache_prefix else user_prompt; assign in source target order to user_content.
  }
  // Source: vvaharness/backends/llm/openai.py:639-645
  In source order: Evaluate messages.append({'role': 'user', 'content': user_content}); retain side effects and discard the expression result. Then For kw, assign {'model': model, 'messages': messages, 'stream': True}; source annotation dict.
  // Source: vvaharness/backends/llm/openai.py:646-647
  if (the source predicate model not in _NO_STREAM_OPTIONS_MODELS is truthy) {
    // Source: vvaharness/backends/llm/openai.py:647-647
    In source order: Evaluate once {'include_usage': True}; assign in source target order to kw['stream_options'].
  }
  // Source: vvaharness/backends/llm/openai.py:648-653
  if (the source predicate _cache_markers_enabled() and model not in _NO_CACHE_KEY_MODELS is truthy) {
    // Source: vvaharness/backends/llm/openai.py:651-653
    In source order: Evaluate once _prompt_cache_key(tag, model, cache_prefix=cache_prefix, preceding=system_prompt or ''); assign in source target order to kw['prompt_cache_key'].
  }
  // Source: vvaharness/backends/llm/openai.py:655-658
  if (the source predicate model in _USE_LEGACY_MAXTOK is truthy) {
    // Source: vvaharness/backends/llm/openai.py:656-656
    In source order: Evaluate once max_tok; assign in source target order to kw['max_tokens'].
  }
  else {
    // Source: vvaharness/backends/llm/openai.py:658-658
    In source order: Evaluate once max_tok; assign in source target order to kw['max_completion_tokens'].
  }
  // Source: vvaharness/backends/llm/openai.py:659-660
  if (the source predicate temperature is not None and model not in _NO_TEMP_MODELS is truthy) {
    // Source: vvaharness/backends/llm/openai.py:660-660
    In source order: Evaluate once temperature; assign in source target order to kw['temperature'].
  }
  // Source: vvaharness/backends/llm/openai.py:661-664
  if (the source predicate json_schema or output_format == 'json' is truthy) {
    // Source: vvaharness/backends/llm/openai.py:664-664
    In source order: Evaluate once _response_format_for(json_schema, model=model, tag=tag); assign in source target order to kw['response_format'].
  }
  // Source: vvaharness/backends/llm/openai.py:665-683
  In source order: Evaluate kw.update(_reasoning_effort_kw(model, effort)); retain side effects and discard the expression result. Then Evaluate once effort_scaled_seconds(timeout or DEFAULT_REQUEST_TIMEOUT_SECONDS, effort, kind=ClockKind.REQUEST); assign in source target order to request_timeout. Then Evaluate once sum((len(b.get('text', '')) for b in user_prompt if isinstance(b, dict))) if isinstance(user_prompt, list) else len(user_prompt); assign in source target order to _up_chars. Then Evaluate console.write(source_template_676_18); retain side effects and discard the expression result. Then Evaluate once time.monotonic(); assign in source target order to session_t0.
  // Source: vvaharness/backends/llm/openai.py:684-689
  In source order: Evaluate once request_timeout; assign in source target order to session_budget. Then Evaluate once (3, 60); assign in source target order to (attempts, retry_wait). Then Evaluate once None; assign in source target order to text. Then Evaluate once None; assign in source target order to usage. Then Evaluate once 0; assign in source target order to auth_attempt.
  // Source: vvaharness/backends/llm/openai.py:691-700
  In source order: Evaluate once False; assign in source target order to trunc_retried. Then Evaluate once 0; assign in source target order to trunc_retry_at. Then Evaluate once 0; assign in source target order to attempt. Then Evaluate once False; assign in source target order to streamed_any. Then Evaluate once None; assign in source target order to server_error_probe.
  // Source: vvaharness/backends/llm/openai.py:701-701
  In source order: Evaluate once None; assign in source target order to server_error_exc.
  // Source: vvaharness/backends/llm/openai.py:702-1071
  while (the source predicate attempt < attempts is truthy) {
    // Source: vvaharness/backends/llm/openai.py:703-703
    In source order: Apply source augmented assignment attempt += 1 with source evaluation/in-place semantics.
    // Source: vvaharness/backends/llm/openai.py:704-1071
    Perform the following protected operations {
      // Source: vvaharness/backends/llm/openai.py:707-712
      In source order: Evaluate once False; assign in source target order to streamed_any. Then Evaluate once time.monotonic(); assign in source target order to _t0. Then Evaluate once turn_options(session_t0, session_budget, request_timeout); assign in source target order to send. Then Evaluate once client.with_options(**send); assign in source target order to req_client. Then Evaluate once req_client.chat.completions.create(**kw); assign in source target order to stream.
      // Source: vvaharness/backends/llm/openai.py:713-716
      In source order: For parts, assign []; source annotation list[str]. Then Evaluate once None; assign in source target order to usage. Then For finish, assign None; source annotation str | None. Then For refusal, assign None; source annotation str | None.
      // Source: vvaharness/backends/llm/openai.py:717-734
      for each ev in _stream_within_deadline(stream, deadline=_t0 + send['timeout'], stage=tag, effort=effort, budget_s=request_timeout) {
        // Source: vvaharness/backends/llm/openai.py:720-720
        In source order: Evaluate once True; assign in source target order to streamed_any.
        // Source: vvaharness/backends/llm/openai.py:721-732
        if (the source predicate ev.choices is truthy) {
          // Source: vvaharness/backends/llm/openai.py:722-723
          In source order: Evaluate once ev.choices[0]; assign in source target order to choice. Then Evaluate once choice.delta; assign in source target order to delta.
          // Source: vvaharness/backends/llm/openai.py:724-725
          if (the source predicate delta and delta.content is truthy) {
            // Source: vvaharness/backends/llm/openai.py:725-725
            In source order: Evaluate parts.append(delta.content); retain side effects and discard the expression result.
          }
          // Source: vvaharness/backends/llm/openai.py:729-730
          if (the source predicate delta is not None and getattr(delta, 'refusal', None) is truthy) {
            // Source: vvaharness/backends/llm/openai.py:730-730
            In source order: Evaluate once (refusal or '') + str(delta.refusal); assign in source target order to refusal.
          }
          // Source: vvaharness/backends/llm/openai.py:732-732
          In source order: Evaluate once getattr(choice, 'finish_reason', None) or finish; assign in source target order to finish.
        }
        // Source: vvaharness/backends/llm/openai.py:733-734
        if (the source predicate getattr(ev, 'usage', None) is truthy) {
          // Source: vvaharness/backends/llm/openai.py:734-734
          In source order: Evaluate once ev.usage; assign in source target order to usage.
        }
      }
      // Source: vvaharness/backends/llm/openai.py:735-735
      In source order: Evaluate note_budget_use(time.monotonic() - _t0, request_timeout, effort); retain side effects and discard the expression result.
      // Source: vvaharness/backends/llm/openai.py:736-741
      if (the source predicate finish == _OPENAI_FINISH_CONTENT_FILTER is truthy) {
        // Source: vvaharness/backends/llm/openai.py:739-739
        In source order: Evaluate _bank_attempt_usage(usage); retain side effects and discard the expression result.
        // Source: vvaharness/backends/llm/openai.py:740-741
        Raise model_refusal(route='openai', stage=tag or '', category=_OPENAI_FINISH_CONTENT_FILTER, detail=refusal or '').
      }
      // Source: vvaharness/backends/llm/openai.py:742-745
      if (the source predicate refusal and (not ''.join(parts).strip()) is truthy) {
        // Source: vvaharness/backends/llm/openai.py:743-743
        In source order: Evaluate _bank_attempt_usage(usage); retain side effects and discard the expression result.
        // Source: vvaharness/backends/llm/openai.py:744-745
        Raise model_refusal(route='openai', stage=tag or '', category=None, detail=refusal).
      }
      // Source: vvaharness/backends/llm/openai.py:746-798
      if (the source predicate finish == OPENAI_FINISH_LENGTH is truthy) {
        // Source: vvaharness/backends/llm/openai.py:748-752
        In source order: Evaluate once _MAX_TOKENS_KEY if _MAX_TOKENS_KEY in kw else _MAX_COMPLETION_TOKENS_KEY; assign in source target order to budget_key. Then Evaluate once kw[budget_key]; assign in source target order to requested_now. Then Evaluate once None if trunc_retried else truncation_retry_max(requested_now, cap=output_cap); assign in source target order to retry_at.
        // Source: vvaharness/backends/llm/openai.py:753-778
        if (the source predicate retry_at is not None is truthy) {
          // Source: vvaharness/backends/llm/openai.py:755-756
          if (the source predicate attempt == attempts and attempts < _ATTEMPTS_CEILING is truthy) {
            // Source: vvaharness/backends/llm/openai.py:756-756
            In source order: Apply source augmented assignment attempts += 1 with source evaluation/in-place semantics.
          }
          // Source: vvaharness/backends/llm/openai.py:757-778
          if (the source predicate attempt < attempts is truthy) {
            // Source: vvaharness/backends/llm/openai.py:758-776
            In source order: Evaluate once (True, retry_at); assign in source target order to (trunc_retried, trunc_retry_at). Then Evaluate COUNTERS.bump(TRUNCATED_RETRY_ATTEMPTED_COUNTER); retain side effects and discard the expression result. Then Evaluate log.warning(Event.TRUNCATED_RETRY, route='openai', finish_reason=OPENAI_FINISH_LENGTH, budget_key=budget_key, budget=requested_now, retry_at=retry_at); retain side effects and discard the expression result. Then Evaluate once _bank_attempt_usage(usage); assign in source target order to discarded. Then Evaluate _errlog.log(tag or 'openai', tag or 'truncation', source_template_769_28, error_code=TruncatedResponseError.error_code, recovered=True, produced=discarded.get('output_tokens') if discarded else None); retain side effects and discard the expression result.
            // Source: vvaharness/backends/llm/openai.py:777-777
            In source order: Evaluate once retry_at; assign in source target order to kw[budget_key].
            // Source: vvaharness/backends/llm/openai.py:778-778
            Continue the immediately enclosing source loop at its next iteration.
          }
        }
        // Source: vvaharness/backends/llm/openai.py:782-785
        In source order: Evaluate once _bank_attempt_usage(usage); assign in source target order to norm. Then Evaluate once norm.get('output_tokens') if norm else None; assign in source target order to produced. Then Evaluate once norm.get('reasoning_tokens') if norm else None; assign in source target order to reasoning_tokens. Then Evaluate COUNTERS.bump(TRUNCATED_REPLIES_COUNTER); retain side effects and discard the expression result.
        // Source: vvaharness/backends/llm/openai.py:786-787
        if (the source predicate truncated_below_budget(produced, max_tok) is truthy) {
          // Source: vvaharness/backends/llm/openai.py:787-787
          In source order: Evaluate COUNTERS.bump(LLM_TRUNCATED_BELOW_BUDGET_COUNTER); retain side effects and discard the expression result.
        }
        // Source: vvaharness/backends/llm/openai.py:788-798
        Raise TruncatedResponseError('reply still hit the output-token budget after the doubled retry' if trunc_retried else 'reply hit the output-token budget with no retry budget left', stage=tag or '', requested=max_tok, retried=trunc_retry_at, produced=produced, reasoning_tokens=reasoning_tokens).
      }
      // Source: vvaharness/backends/llm/openai.py:799-800
      if (the source predicate trunc_retried is truthy) {
        // Source: vvaharness/backends/llm/openai.py:800-800
        In source order: Evaluate COUNTERS.bump(TRUNCATED_RETRY_RECOVERED_COUNTER); retain side effects and discard the expression result.
      }
      // Source: vvaharness/backends/llm/openai.py:801-811
      if (the source predicate server_error_probe is not None is truthy) {
        // Source: vvaharness/backends/llm/openai.py:802-802
        In source order: Evaluate once server_error_probe; assign in source target order to (probed_model, probed_sent).
        // Source: vvaharness/backends/llm/openai.py:803-804
        if (the source predicate (learned := EFFORT_REJECTIONS.recovered_twice(server_error_probe)) is truthy) {
          // Source: vvaharness/backends/llm/openai.py:804-804
          In source order: Evaluate EFFORT_REJECTIONS.tiers.add(server_error_probe); retain side effects and discard the expression result.
        }
        // Source: vvaharness/backends/llm/openai.py:805-811
        In source order: Evaluate COUNTERS.bump('llm_effort_tier_stepped_down_on_server_error'); retain side effects and discard the expression result. Then Evaluate warn_once(_WARNED_DROPS, source_template_807_35, source_template_808_20); retain side effects and discard the expression result.
      }
      // Source: vvaharness/backends/llm/openai.py:812-812
      In source order: Evaluate once ''.join(parts); assign in source target order to text.
      // Source: vvaharness/backends/llm/openai.py:813-813
      Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
    }
    // Source: vvaharness/backends/llm/openai.py:815-969
    On the first matching source exception (openai.BadRequestError, openai.UnprocessableEntityError) as e, in handler order {
      // Source: vvaharness/backends/llm/openai.py:816-819
      In source order: Evaluate _raise_if_refusal_rejection(e, tag=tag); retain side effects and discard the expression result. Then Evaluate once rejection_text(e).lower(); assign in source target order to body. Then Evaluate once _MAX_TOKENS_KEY if _MAX_TOKENS_KEY in kw else _MAX_COMPLETION_TOKENS_KEY; assign in source target order to budget_key_now.
      // Source: vvaharness/backends/llm/openai.py:820-836
      if (the source predicate model not in _LEARNED_OUTPUT_CAP and (_MAX_TOKENS_KEY in body or _MAX_COMPLETION_TOKENS_KEY in body) is truthy) {
        // Source: vvaharness/backends/llm/openai.py:822-822
        In source order: Evaluate once _learned_cap_from_body(body, requested=kw[budget_key_now]); assign in source target order to learned.
        // Source: vvaharness/backends/llm/openai.py:823-836
        if (the source predicate learned is not None is truthy) {
          // Source: vvaharness/backends/llm/openai.py:824-833
          In source order: Evaluate once learned; assign in source target order to _LEARNED_OUTPUT_CAP[model]. Then Evaluate warn_once(_WARNED_DROPS, source_template_826_39, source_template_827_24); retain side effects and discard the expression result. Then Evaluate once learned; assign in source target order to kw[budget_key_now].
          // Source: vvaharness/backends/llm/openai.py:834-835
          if (the source predicate attempt == attempts and attempts < _ATTEMPTS_CEILING is truthy) {
            // Source: vvaharness/backends/llm/openai.py:835-835
            In source order: Apply source augmented assignment attempts += 1 with source evaluation/in-place semantics.
          }
          // Source: vvaharness/backends/llm/openai.py:836-836
          Continue the immediately enclosing source loop at its next iteration.
        }
      }
      // Source: vvaharness/backends/llm/openai.py:837-858
      if (the source predicate trunc_retried and (_MAX_TOKENS_KEY in body or _MAX_COMPLETION_TOKENS_KEY in body) is truthy) {
        // Source: vvaharness/backends/llm/openai.py:844-846
        In source order: Evaluate once _normalised_attempt_usage(usage); assign in source target order to stale. Then Evaluate once stale.get('output_tokens') if stale else None; assign in source target order to produced. Then Evaluate COUNTERS.bump(TRUNCATED_REPLIES_COUNTER); retain side effects and discard the expression result.
        // Source: vvaharness/backends/llm/openai.py:847-848
        if (the source predicate truncated_below_budget(produced, max_tok) is truthy) {
          // Source: vvaharness/backends/llm/openai.py:848-848
          In source order: Evaluate COUNTERS.bump(LLM_TRUNCATED_BELOW_BUDGET_COUNTER); retain side effects and discard the expression result.
        }
        // Source: vvaharness/backends/llm/openai.py:849-858
        Raise TruncatedResponseError(source_template_850_20, stage=tag or '', requested=max_tok, retried=trunc_retry_at, produced=produced, reasoning_tokens=stale.get('reasoning_tokens') if stale else None) with explicit source cause e.
      }
      // Source: vvaharness/backends/llm/openai.py:860-860
      In source order: Evaluate once False; assign in source target order to dropped.
      // Source: vvaharness/backends/llm/openai.py:861-943
      if (the source predicate 'temperature' in body and 'temperature' in kw is truthy) {
        // Source: vvaharness/backends/llm/openai.py:862-866
        In source order: Evaluate _NO_TEMP_MODELS.add(model); retain side effects and discard the expression result. Then Evaluate console.write(source_template_863_30); retain side effects and discard the expression result. Then Evaluate kw.pop('temperature', None); retain side effects and discard the expression result. Then Evaluate once True; assign in source target order to dropped.
      }
      else {
        // Source: vvaharness/backends/llm/openai.py:867-943
        if (the source predicate 'max_completion_tokens' in kw and 'max_completion_tokens' in body is truthy) {
          // Source: vvaharness/backends/llm/openai.py:868-872
          In source order: Evaluate _USE_LEGACY_MAXTOK.add(model); retain side effects and discard the expression result. Then Evaluate once kw.pop('max_completion_tokens'); assign in source target order to kw['max_tokens']. Then Evaluate console.write(source_template_870_30); retain side effects and discard the expression result. Then Evaluate once True; assign in source target order to dropped.
        }
        else {
          // Source: vvaharness/backends/llm/openai.py:873-943
          if (the source predicate 'max_tokens' in kw and 'max_completion_tokens' in body is truthy) {
            // Source: vvaharness/backends/llm/openai.py:874-877
            In source order: Evaluate once kw.pop('max_tokens'); assign in source target order to kw['max_completion_tokens']. Then Evaluate console.write(source_template_875_30); retain side effects and discard the expression result. Then Evaluate once True; assign in source target order to dropped.
          }
          else {
            // Source: vvaharness/backends/llm/openai.py:878-943
            if (the source predicate 'prompt_cache_key' in body and 'prompt_cache_key' in kw is truthy) {
              // Source: vvaharness/backends/llm/openai.py:882-886
              In source order: Evaluate _NO_CACHE_KEY_MODELS.add(model); retain side effects and discard the expression result. Then Evaluate kw.pop('prompt_cache_key', None); retain side effects and discard the expression result. Then Evaluate console.write(source_template_884_30); retain side effects and discard the expression result. Then Evaluate once True; assign in source target order to dropped.
            }
            else {
              // Source: vvaharness/backends/llm/openai.py:887-943
              if (the source predicate 'json_schema' in body and kw.get('response_format', {}).get('type') == 'json_schema' is truthy) {
                // Source: vvaharness/backends/llm/openai.py:892-903
                In source order: Evaluate _NO_JSON_SCHEMA_MODELS.add(model); retain side effects and discard the expression result. Then Evaluate once {'type': 'json_object'}; assign in source target order to kw['response_format']. Then Evaluate warn_once(_WARNED_DROPS, source_template_895_35, source_template_896_20); retain side effects and discard the expression result. Then Evaluate once True; assign in source target order to dropped.
              }
              else {
                // Source: vvaharness/backends/llm/openai.py:904-943
                if (the source predicate 'reasoning_effort' in kw and (effort_cls := classify_effort_rejection(e)) is not None is truthy) {
                  // Source: vvaharness/backends/llm/openai.py:908-908
                  In source order: Evaluate once kw['reasoning_effort']; assign in source target order to sent.
                  // Source: vvaharness/backends/llm/openai.py:909-931
                  if (the source predicate effort_cls == 'field' is truthy) {
                    // Source: vvaharness/backends/llm/openai.py:910-917
                    In source order: Evaluate EFFORT_REJECTIONS.field.add(model); retain side effects and discard the expression result. Then Evaluate kw.pop('reasoning_effort', None); retain side effects and discard the expression result. Then Evaluate COUNTERS.bump('llm_effort_field_dropped'); retain side effects and discard the expression result. Then Evaluate warn_once(_WARNED_DROPS, source_template_914_39, source_template_915_24); retain side effects and discard the expression result.
                  }
                  else {
                    // Source: vvaharness/backends/llm/openai.py:922-922
                    In source order: Evaluate once step_down(model, sent, e); assign in source target order to nxt.
                    // Source: vvaharness/backends/llm/openai.py:923-926
                    if (the source predicate nxt is None is truthy) {
                      // Source: vvaharness/backends/llm/openai.py:924-924
                      In source order: Evaluate kw.pop('reasoning_effort', None); retain side effects and discard the expression result.
                    }
                    else {
                      // Source: vvaharness/backends/llm/openai.py:926-926
                      In source order: Evaluate once nxt; assign in source target order to kw['reasoning_effort'].
                    }
                    // Source: vvaharness/backends/llm/openai.py:927-931
                    In source order: Evaluate COUNTERS.bump('llm_effort_tier_stepped_down'); retain side effects and discard the expression result. Then Evaluate warn_once(_WARNED_DROPS, source_template_929_39, source_template_930_24); retain side effects and discard the expression result.
                  }
                  // Source: vvaharness/backends/llm/openai.py:932-932
                  In source order: Evaluate once True; assign in source target order to dropped.
                }
                else {
                  // Source: vvaharness/backends/llm/openai.py:933-943
                  if (the source predicate 'stream_options' in body and 'stream_options' in kw is truthy) {
                    // Source: vvaharness/backends/llm/openai.py:936-943
                    In source order: Evaluate _NO_STREAM_OPTIONS_MODELS.add(model); retain side effects and discard the expression result. Then Evaluate kw.pop('stream_options', None); retain side effects and discard the expression result. Then Evaluate warn_once(_WARNED_DROPS, source_template_939_35, source_template_940_20); retain side effects and discard the expression result. Then Evaluate once True; assign in source target order to dropped.
                  }
                }
              }
            }
          }
        }
      }
      // Source: vvaharness/backends/llm/openai.py:944-948
      if (the source predicate dropped is truthy) {
        // Source: vvaharness/backends/llm/openai.py:946-947
        if (the source predicate attempt == attempts and attempts < _ATTEMPTS_CEILING is truthy) {
          // Source: vvaharness/backends/llm/openai.py:947-947
          In source order: Apply source augmented assignment attempts += 1 with source evaluation/in-place semantics.
        }
        // Source: vvaharness/backends/llm/openai.py:948-948
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/backends/llm/openai.py:949-951
      if (the source predicate _auth_failure_oai(e) is truthy) {
        // Source: vvaharness/backends/llm/openai.py:950-951
        Raise AuthenticationError(redact(str(e))[:400], status_code=e.status_code, backend='openai') with explicit source cause e.
      }
      // Source: vvaharness/backends/llm/openai.py:955-964
      if (the source predicate _is_transient_oai(e) and attempt < attempts is truthy) {
        // Source: vvaharness/backends/llm/openai.py:956-956
        In source order: Evaluate once jittered_delay(retry_wait); assign in source target order to wait.
        // Source: vvaharness/backends/llm/openai.py:957-959
        if (the source predicate (overrun := wait_overrun(wait, session_t0, session_budget, stage=tag or '', route='openai', effort=effort)) is truthy) {
          // Source: vvaharness/backends/llm/openai.py:959-959
          Raise overrun with explicit source cause e.
        }
        // Source: vvaharness/backends/llm/openai.py:960-963
        In source order: Evaluate console.write(source_template_960_30); retain side effects and discard the expression result. Then Evaluate time.sleep(wait); retain side effects and discard the expression result.
        // Source: vvaharness/backends/llm/openai.py:964-964
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/backends/llm/openai.py:965-969
      Raise RuntimeError(source_template_966_16) with explicit source cause e.
    }
    // Source: vvaharness/backends/llm/openai.py:970-1034
    On the first matching source exception openai.APIStatusError as e, in handler order {
      // Source: vvaharness/backends/llm/openai.py:971-971
      In source order: Evaluate _raise_if_refusal_rejection(e, tag=tag); retain side effects and discard the expression result.
      // Source: vvaharness/backends/llm/openai.py:976-999
      if (the source predicate _auth_failure_oai(e) is truthy) {
        // Source: vvaharness/backends/llm/openai.py:982-994
        if (the source predicate auth_attempt < _AUTH_MAX_RETRIES_OAI and attempt < attempts is truthy) {
          // Source: vvaharness/backends/llm/openai.py:983-984
          In source order: Evaluate once _AUTH_BACKOFF_OAI[min(auth_attempt, len(_AUTH_BACKOFF_OAI) - 1)]; assign in source target order to wait.
          // Source: vvaharness/backends/llm/openai.py:985-987
          if (the source predicate (overrun := wait_overrun(wait, session_t0, session_budget, stage=tag or '', route='openai', effort=effort)) is truthy) {
            // Source: vvaharness/backends/llm/openai.py:987-987
            Raise overrun with explicit source cause e.
          }
          // Source: vvaharness/backends/llm/openai.py:988-993
          In source order: Evaluate console.write(source_template_988_34); retain side effects and discard the expression result. Then Evaluate time.sleep(wait); retain side effects and discard the expression result. Then Apply source augmented assignment auth_attempt += 1 with source evaluation/in-place semantics.
          // Source: vvaharness/backends/llm/openai.py:994-994
          Continue the immediately enclosing source loop at its next iteration.
        }
        // Source: vvaharness/backends/llm/openai.py:997-999
        Raise AuthenticationError(redact(str(e))[:400], status_code=e.status_code, backend='openai') with explicit source cause e.
      }
      // Source: vvaharness/backends/llm/openai.py:1000-1009
      if (the source predicate _is_transient_oai(e) and attempt < attempts is truthy) {
        // Source: vvaharness/backends/llm/openai.py:1001-1001
        In source order: Evaluate once jittered_delay(retry_wait); assign in source target order to wait.
        // Source: vvaharness/backends/llm/openai.py:1002-1004
        if (the source predicate (overrun := wait_overrun(wait, session_t0, session_budget, stage=tag or '', route='openai', effort=effort)) is truthy) {
          // Source: vvaharness/backends/llm/openai.py:1004-1004
          Raise overrun with explicit source cause e.
        }
        // Source: vvaharness/backends/llm/openai.py:1005-1008
        In source order: Evaluate console.write(source_template_1005_30); retain side effects and discard the expression result. Then Evaluate time.sleep(wait); retain side effects and discard the expression result.
        // Source: vvaharness/backends/llm/openai.py:1009-1009
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/backends/llm/openai.py:1010-1016
      if (the source predicate server_error_probe is not None is truthy) {
        // Source: vvaharness/backends/llm/openai.py:1013-1016
        Raise RuntimeError(source_template_1014_20) with explicit source cause server_error_exc.
      }
      // Source: vvaharness/backends/llm/openai.py:1017-1024
      In source order: Evaluate once kw.get('reasoning_effort'); assign in source target order to sent. Then Evaluate once sent is not None and sent != REASONING_OFF and (e.status_code in SERVER_ERROR_STATUS) and (attempt < attempts or attempts < _ATTEMPTS_CEILING); assign in source target order to can_probe. Then Evaluate once next_effort_tier(sent) if can_probe else None; assign in source target order to nxt.
      // Source: vvaharness/backends/llm/openai.py:1025-1030
      if (the source predicate nxt is not None and EFFORT_REJECTIONS.probe_once((model, sent)) is truthy) {
        // Source: vvaharness/backends/llm/openai.py:1026-1027
        In source order: Evaluate once ((model, sent), e); assign in source target order to (server_error_probe, server_error_exc). Then Evaluate once nxt; assign in source target order to kw['reasoning_effort'].
        // Source: vvaharness/backends/llm/openai.py:1028-1029
        if (the source predicate attempt == attempts and attempts < _ATTEMPTS_CEILING is truthy) {
          // Source: vvaharness/backends/llm/openai.py:1029-1029
          In source order: Apply source augmented assignment attempts += 1 with source evaluation/in-place semantics.
        }
        // Source: vvaharness/backends/llm/openai.py:1030-1030
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/backends/llm/openai.py:1031-1034
      Raise RuntimeError(source_template_1032_16) with explicit source cause e.
    }
    // Source: vvaharness/backends/llm/openai.py:1035-1067
    On the first matching source exception openai.APIConnectionError as e, in handler order {
      // Source: vvaharness/backends/llm/openai.py:1038-1041
      if (the source predicate is_timeout_failure(e) is truthy) {
        // Source: vvaharness/backends/llm/openai.py:1039-1041
        Raise call_timeout_error(stage=tag or '', route='openai', budget_s=request_timeout, effort=effort, cause_text=source_template_1041_31) with explicit source cause e.
      }
      // Source: vvaharness/backends/llm/openai.py:1042-1042
      In source order: Evaluate once _cause_chain(e); assign in source target order to detail.
      // Source: vvaharness/backends/llm/openai.py:1047-1048
      if (the source predicate not streamed_any and (proxy := proxy_error(e, backend='openai')) is truthy) {
        // Source: vvaharness/backends/llm/openai.py:1048-1048
        Raise proxy with explicit source cause e.
      }
      // Source: vvaharness/backends/llm/openai.py:1049-1049
      In source order: Evaluate once 'mid-stream' if streamed_any else 'connection'; assign in source target order to where.
      // Source: vvaharness/backends/llm/openai.py:1050-1058
      if (the source predicate attempt < attempts is truthy) {
        // Source: vvaharness/backends/llm/openai.py:1051-1051
        In source order: Evaluate once jittered_delay(retry_wait); assign in source target order to wait.
        // Source: vvaharness/backends/llm/openai.py:1052-1054
        if (the source predicate (overrun := wait_overrun(wait, session_t0, session_budget, stage=tag or '', route='openai', effort=effort)) is truthy) {
          // Source: vvaharness/backends/llm/openai.py:1054-1054
          Raise overrun with explicit source cause e.
        }
        // Source: vvaharness/backends/llm/openai.py:1055-1057
        In source order: Evaluate console.write(source_template_1055_30); retain side effects and discard the expression result. Then Evaluate time.sleep(wait); retain side effects and discard the expression result.
        // Source: vvaharness/backends/llm/openai.py:1058-1058
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/backends/llm/openai.py:1059-1067
      Raise RuntimeError(source_template_1060_16) with explicit source cause e.
    }
    // Source: vvaharness/backends/llm/openai.py:1068-1071
    On the first matching source exception openai.APIError as e, in handler order {
      // Source: vvaharness/backends/llm/openai.py:1070-1070
      In source order: Evaluate _raise_if_refusal_rejection(e, tag=tag); retain side effects and discard the expression result.
      // Source: vvaharness/backends/llm/openai.py:1071-1071
      Raise the currently handled exception.
    }
  }
  // Source: vvaharness/backends/llm/openai.py:1073-1079
  if (the source predicate text is None is truthy) {
    // Source: vvaharness/backends/llm/openai.py:1075-1079
    Raise RuntimeError(source_template_1076_12).
  }
  // Source: vvaharness/backends/llm/openai.py:1081-1094
  if (the source predicate usage is not None is truthy) {
    // Source: vvaharness/backends/llm/openai.py:1082-1088
    In source order: Evaluate once usage.model_dump() if hasattr(usage, 'model_dump') else dict(usage); assign in source target order to u. Then Evaluate _note_unparsed_cache_keys(u); retain side effects and discard the expression result. Then Evaluate once _normalise_usage(u); assign in source target order to norm. Then Evaluate TOKENS.add(norm); retain side effects and discard the expression result. Then Evaluate once norm.get('cache_creation_input_tokens'); assign in source target order to written.
    // Source: vvaharness/backends/llm/openai.py:1089-1092
    In source order: Evaluate console.write(source_template_1089_22); retain side effects and discard the expression result.
  }
  else {
    // Source: vvaharness/backends/llm/openai.py:1094-1094
    In source order: Evaluate TOKENS.add(None); retain side effects and discard the expression result.
  }
  // Source: vvaharness/backends/llm/openai.py:1098-1101
  In source order: Evaluate once output_tokens_for_gate(None if usage is None else {'output_tokens': u.get('completion_tokens')}); assign in source target order to out_tokens. Then Evaluate check_response_quality(text.strip(), stage=tag or '', output_tokens=out_tokens); retain side effects and discard the expression result.
  // Source: vvaharness/backends/llm/openai.py:1102-1102
  End this invocation with text.strip().
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/openai.py:1107-1116
In source order: Evaluate once 25; assign in source target order to _MAX_TURNS. Then Evaluate once AGENTIC_MAX_TOKENS; assign in source target order to _AGENTIC_MAX_TOK. Then Evaluate once frozenset({'prompt_tokens_details.cached_tokens', 'prompt_tokens_details.cache_write_tokens'}); assign in source target order to _PARSED_USAGE_CACHE_KEYS.
// Source: vvaharness/backends/llm/openai.py:1119-1130
// Source signature: _note_unparsed_cache_keys(u: dict | None) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _note_unparsed_cache_keys(u) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/openai.py:1120-1120
  In source order: Retain source documentation literal source_literal_1120_4; it is not a model call.
  // Source: vvaharness/backends/llm/openai.py:1121-1122
  if (the source predicate not isinstance(u, dict) is truthy) {
    // Source: vvaharness/backends/llm/openai.py:1122-1122
    End this invocation with None.
  }
  // Source: vvaharness/backends/llm/openai.py:1123-1124
  In source order: Evaluate once dict(u); assign in source target order to flat. Then Evaluate once flat.pop('prompt_tokens_details', None); assign in source target order to ptd.
  // Source: vvaharness/backends/llm/openai.py:1125-1128
  if (the source predicate isinstance(ptd, dict) is truthy) {
    // Source: vvaharness/backends/llm/openai.py:1126-1128
    for each (k, v) in ptd.items() {
      // Source: vvaharness/backends/llm/openai.py:1127-1128
      if (the source predicate isinstance(k, str) is truthy) {
        // Source: vvaharness/backends/llm/openai.py:1128-1128
        In source order: Evaluate once v; assign in source target order to flat[f'prompt_tokens_details.{k}'].
      }
    }
  }
  // Source: vvaharness/backends/llm/openai.py:1129-1130
  In source order: Evaluate _cache.report_unparsed_cache_keys(flat, _PARSED_USAGE_CACHE_KEYS, via='openai', label='openai'); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/openai.py:1133-1156
// Source signature: _normalise_usage(u: dict) -> TokenUsage
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _normalise_usage(u) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/openai.py:1134-1135
  In source order: Retain source documentation literal source_literal_1134_4; it is not a model call. Then Evaluate once u.get('prompt_tokens_details') or {}; assign in source target order to ptd.
  // Source: vvaharness/backends/llm/openai.py:1136-1137
  if (the source predicate not isinstance(ptd, dict) is truthy) {
    // Source: vvaharness/backends/llm/openai.py:1137-1137
    In source order: Evaluate once {}; assign in source target order to ptd.
  }
  // Source: vvaharness/backends/llm/openai.py:1138-1138
  In source order: Evaluate once u.get('completion_tokens_details') or {}; assign in source target order to ctd.
  // Source: vvaharness/backends/llm/openai.py:1139-1140
  if (the source predicate not isinstance(ctd, dict) is truthy) {
    // Source: vvaharness/backends/llm/openai.py:1140-1140
    In source order: Evaluate once {}; assign in source target order to ctd.
  }
  // Source: vvaharness/backends/llm/openai.py:1141-1149
  In source order: Evaluate once ptd.get('cached_tokens', 0) or 0; assign in source target order to cached. Then For norm, assign {'input_tokens': max(0, (u.get('prompt_tokens', 0) or 0) - cached), 'output_tokens': u.get('completion_tokens'), 'cache_read_input_tokens': cached}; source annotation TokenUsage.
  // Source: vvaharness/backends/llm/openai.py:1150-1153
  if (the source predicate 'cache_write_tokens' in ptd is truthy) {
    // Source: vvaharness/backends/llm/openai.py:1151-1153
    In source order: Evaluate once ptd.get('cache_write_tokens') or 0; assign in source target order to written. Then Evaluate once written; assign in source target order to norm['cache_creation_input_tokens']. Then Evaluate once max(0, norm['input_tokens'] - written); assign in source target order to norm['input_tokens'].
  }
  // Source: vvaharness/backends/llm/openai.py:1154-1155
  if (the source predicate 'reasoning_tokens' in ctd is truthy) {
    // Source: vvaharness/backends/llm/openai.py:1155-1155
    In source order: Evaluate once ctd.get('reasoning_tokens') or 0; assign in source target order to norm['reasoning_tokens'].
  }
  // Source: vvaharness/backends/llm/openai.py:1156-1156
  End this invocation with norm.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/openai.py:1159-1168
// Source signature: _normalised_attempt_usage(usage) -> TokenUsage | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _normalised_attempt_usage(usage) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/openai.py:1160-1160
  In source order: Retain source documentation literal source_literal_1160_4; it is not a model call.
  // Source: vvaharness/backends/llm/openai.py:1164-1165
  if (the source predicate usage is None is truthy) {
    // Source: vvaharness/backends/llm/openai.py:1165-1165
    End this invocation with None.
  }
  // Source: vvaharness/backends/llm/openai.py:1166-1167
  In source order: Evaluate once usage.model_dump() if hasattr(usage, 'model_dump') else dict(usage); assign in source target order to u. Then Evaluate _note_unparsed_cache_keys(u); retain side effects and discard the expression result.
  // Source: vvaharness/backends/llm/openai.py:1168-1168
  End this invocation with _normalise_usage(u).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/openai.py:1171-1178
// Source signature: _bank_attempt_usage(usage) -> TokenUsage | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _bank_attempt_usage(usage) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/openai.py:1172-1177
  In source order: Retain source documentation literal source_literal_1172_4; it is not a model call. Then Evaluate once _normalised_attempt_usage(usage); assign in source target order to norm. Then Evaluate TOKENS.add(norm); retain side effects and discard the expression result.
  // Source: vvaharness/backends/llm/openai.py:1178-1178
  End this invocation with norm.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/openai.py:1181-1187
// Source signature: _record_usage(usage) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _record_usage(usage) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/openai.py:1182-1184
  if (the source predicate usage is None is truthy) {
    // Source: vvaharness/backends/llm/openai.py:1183-1183
    In source order: Evaluate TOKENS.add(None); retain side effects and discard the expression result.
    // Source: vvaharness/backends/llm/openai.py:1184-1184
    End this invocation with None.
  }
  // Source: vvaharness/backends/llm/openai.py:1185-1187
  In source order: Evaluate once usage.model_dump() if hasattr(usage, 'model_dump') else dict(usage); assign in source target order to u. Then Evaluate _note_unparsed_cache_keys(u); retain side effects and discard the expression result. Then Evaluate TOKENS.add(_normalise_usage(u)); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/openai.py:1193-1196
In source order: Evaluate once _localtools.TOOL_RESULT_CAP; assign in source target order to _TOOL_RESULT_CAP. Then Evaluate once _localtools.cap_tool_result; assign in source target order to _cap_tool_result. Then Evaluate once re.compile('context.?length|context length|exceed.*(?:token|limit)|too long', re.I); assign in source target order to _CTX_OVERFLOW_RX.
// Source: vvaharness/backends/llm/openai.py:1199-1204
// Source signature: _anthropic_tool_to_openai(t: dict) -> dict
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _anthropic_tool_to_openai(t) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/openai.py:1200-1200
  In source order: Retain source documentation literal source_literal_1200_4; it is not a model call.
  // Source: vvaharness/backends/llm/openai.py:1201-1204
  End this invocation with {'type': 'function', 'function': {'name': t['name'], 'description': t.get('description', ''), 'parameters': t.get('input_schema') or {'type': 'object'}}}.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/openai.py:1207-1207
In source order: Evaluate once '[evicted to fit context]'; assign in source target order to _EVICTED_MARK.
// Source: vvaharness/backends/llm/openai.py:1210-1218
// Source signature: _shrink_history(messages: list[dict]) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _shrink_history(messages) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/openai.py:1211-1211
  In source order: Retain source documentation literal source_literal_1211_4; it is not a model call.
  // Source: vvaharness/backends/llm/openai.py:1212-1217
  for each m in messages {
    // Source: vvaharness/backends/llm/openai.py:1213-1213
    In source order: Evaluate once m.get('content'); assign in source target order to c.
    // Source: vvaharness/backends/llm/openai.py:1214-1217
    if (the source predicate m.get('role') == 'tool' and isinstance(c, str) and (len(c) > 1200) and (not c.endswith(_EVICTED_MARK)) is truthy) {
      // Source: vvaharness/backends/llm/openai.py:1216-1216
      In source order: Evaluate once c[:800] + source_literal_1216_37 + _EVICTED_MARK; assign in source target order to m['content'].
      // Source: vvaharness/backends/llm/openai.py:1217-1217
      End this invocation with True.
    }
  }
  // Source: vvaharness/backends/llm/openai.py:1218-1218
  End this invocation with False.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/openai.py:1221-1229
// Source signature: _first_choice(resp, *, model: str, tag: str | None, turn: int)
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _first_choice(resp, model, tag, turn) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/openai.py:1222-1223
  In source order: Retain source documentation literal source_literal_1222_4; it is not a model call. Then Evaluate once getattr(resp, 'choices', None) or []; assign in source target order to choices.
  // Source: vvaharness/backends/llm/openai.py:1224-1228
  if (the source predicate not choices is truthy) {
    // Source: vvaharness/backends/llm/openai.py:1225-1228
    Raise RuntimeError(source_template_1226_12 + (source_template_1227_15 if tag else '') + ') — the gateway answered 200 with an empty completion; nothing can be parsed from it.').
  }
  // Source: vvaharness/backends/llm/openai.py:1229-1229
  End this invocation with choices[0].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/openai.py:1232-1367
// Source signature: _check_terminal_finish(choice, msg, *, send: Callable[[dict], Any], messages: list[dict], call_kw: dict, appended: bool, model: str, tag: str | None, requested: int, response_model: type[BaseModel] | None=None, dispatchable: bool=False, output_cap: int | None=None, effort: str | None=None, request_timeout: float | None=None)
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _check_terminal_finish(choice, msg, send, messages, call_kw, appended, model, tag, requested, response_model, dispatchable, output_cap, effort, request_timeout) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/openai.py:1240-1242
  In source order: Retain source documentation literal source_literal_1240_4; it is not a model call. Then Evaluate once getattr(choice, 'finish_reason', None); assign in source target order to finish. Then Evaluate once getattr(msg, 'refusal', None); assign in source target order to refusal.
  // Source: vvaharness/backends/llm/openai.py:1243-1246
  if (the source predicate finish == _OPENAI_FINISH_CONTENT_FILTER is truthy) {
    // Source: vvaharness/backends/llm/openai.py:1244-1246
    Raise model_refusal(route='openai', stage=tag or '', category=_OPENAI_FINISH_CONTENT_FILTER, detail=str(refusal) if refusal else '').
  }
  // Source: vvaharness/backends/llm/openai.py:1247-1364
  if (the source predicate finish == OPENAI_FINISH_LENGTH is truthy) {
    // Source: vvaharness/backends/llm/openai.py:1248-1250
    In source order: Evaluate once _MAX_TOKENS_KEY if _MAX_TOKENS_KEY in call_kw else _MAX_COMPLETION_TOKENS_KEY; assign in source target order to budget_key. Then Evaluate once truncation_retry_max(call_kw[budget_key], cap=output_cap); assign in source target order to retry_at.
    // Source: vvaharness/backends/llm/openai.py:1251-1260
    if (the source predicate retry_at is None is truthy) {
      // Source: vvaharness/backends/llm/openai.py:1256-1256
      In source order: Evaluate COUNTERS.bump(TRUNCATED_REPLIES_COUNTER); retain side effects and discard the expression result.
      // Source: vvaharness/backends/llm/openai.py:1257-1260
      Raise TruncatedResponseError(source_template_1258_16, stage=tag or '', requested=requested, retried=0).
    }
    // Source: vvaharness/backends/llm/openai.py:1261-1268
    In source order: Evaluate COUNTERS.bump(TRUNCATED_RETRY_ATTEMPTED_COUNTER); retain side effects and discard the expression result. Then Evaluate log.warning(Event.TRUNCATED_RETRY, route='openai', finish_reason=OPENAI_FINISH_LENGTH, budget_key=budget_key, budget=requested, retry_at=retry_at); retain side effects and discard the expression result. Then Evaluate _errlog.log(tag or 'openai', tag or 'truncation', source_template_1266_12, error_code=TruncatedResponseError.error_code, recovered=True); retain side effects and discard the expression result.
    // Source: vvaharness/backends/llm/openai.py:1269-1270
    if (the source predicate appended is truthy) {
      // Source: vvaharness/backends/llm/openai.py:1270-1270
      In source order: Evaluate messages.pop(); retain side effects and discard the expression result.
    }
    // Source: vvaharness/backends/llm/openai.py:1271-1271
    In source order: Evaluate once {**call_kw, 'model': model, budget_key: retry_at}; assign in source target order to retry_kw.
    // Source: vvaharness/backends/llm/openai.py:1272-1319
    Perform the following protected operations {
      // Source: vvaharness/backends/llm/openai.py:1273-1275
      In source order: Evaluate once time.monotonic(); assign in source target order to _t0. Then Evaluate once send(retry_kw); assign in source target order to resp. Then Evaluate note_budget_use(time.monotonic() - _t0, request_timeout, effort); retain side effects and discard the expression result.
    }
    // Source: vvaharness/backends/llm/openai.py:1276-1294
    On the first matching source exception (openai.BadRequestError, openai.UnprocessableEntityError) as e, in handler order {
      // Source: vvaharness/backends/llm/openai.py:1277-1278
      In source order: Evaluate _raise_if_refusal_rejection(e, tag=tag); retain side effects and discard the expression result. Then Evaluate once rejection_text(e).lower(); assign in source target order to body.
      // Source: vvaharness/backends/llm/openai.py:1279-1287
      if (the source predicate _MAX_TOKENS_KEY in body or _MAX_COMPLETION_TOKENS_KEY in body is truthy) {
        // Source: vvaharness/backends/llm/openai.py:1283-1283
        In source order: Evaluate COUNTERS.bump(TRUNCATED_REPLIES_COUNTER); retain side effects and discard the expression result.
        // Source: vvaharness/backends/llm/openai.py:1284-1287
        Raise TruncatedResponseError(source_template_1285_20, stage=tag or '', requested=requested, retried=retry_at) with explicit source cause e.
      }
      // Source: vvaharness/backends/llm/openai.py:1288-1290
      if (the source predicate _auth_failure_oai(e) is truthy) {
        // Source: vvaharness/backends/llm/openai.py:1289-1290
        Raise AuthenticationError(redact(str(e))[:400], status_code=e.status_code, backend='openai') with explicit source cause e.
      }
      // Source: vvaharness/backends/llm/openai.py:1291-1294
      Raise RuntimeError(source_template_1292_16) with explicit source cause e.
    }
    // Source: vvaharness/backends/llm/openai.py:1295-1307
    On the first matching source exception openai.APIStatusError as e, in handler order {
      // Source: vvaharness/backends/llm/openai.py:1296-1296
      In source order: Evaluate _raise_if_refusal_rejection(e, tag=tag); retain side effects and discard the expression result.
      // Source: vvaharness/backends/llm/openai.py:1300-1303
      if (the source predicate _auth_failure_oai(e) is truthy) {
        // Source: vvaharness/backends/llm/openai.py:1301-1303
        Raise AuthenticationError(redact(str(e))[:400], status_code=e.status_code, backend='openai') with explicit source cause e.
      }
      // Source: vvaharness/backends/llm/openai.py:1304-1307
      Raise RuntimeError(source_template_1305_16) with explicit source cause e.
    }
    // Source: vvaharness/backends/llm/openai.py:1308-1319
    On the first matching source exception openai.APIConnectionError as e, in handler order {
      // Source: vvaharness/backends/llm/openai.py:1309-1313
      if (the source predicate is_timeout_failure(e) is truthy) {
        // Source: vvaharness/backends/llm/openai.py:1310-1313
        Raise call_timeout_error(stage=tag or '', route='openai', budget_s=request_timeout, effort=effort, cause_text=source_template_1312_31) with explicit source cause e.
      }
      // Source: vvaharness/backends/llm/openai.py:1314-1315
      if (the source predicate (proxy := proxy_error(e, backend='openai')) is truthy) {
        // Source: vvaharness/backends/llm/openai.py:1315-1315
        Raise proxy with explicit source cause e.
      }
      // Source: vvaharness/backends/llm/openai.py:1316-1319
      Raise RuntimeError(source_template_1317_16) with explicit source cause e.
    }
    // Source: vvaharness/backends/llm/openai.py:1320-1323
    In source order: Evaluate _record_usage(getattr(resp, 'usage', None)); retain side effects and discard the expression result. Then Evaluate once _first_choice(resp, model=model, tag=tag, turn=-1); assign in source target order to retried_choice. Then Evaluate once retried_choice.message; assign in source target order to retried_msg. Then Evaluate once getattr(retried_msg, 'tool_calls', None) or []; assign in source target order to retried_calls.
    // Source: vvaharness/backends/llm/openai.py:1324-1330
    if (the source predicate appended is truthy) {
      // Source: vvaharness/backends/llm/openai.py:1325-1330
      In source order: Evaluate messages.append({'role': 'assistant', 'content': retried_msg.content, 'tool_calls': [tc.model_dump() for tc in retried_calls] if retried_calls else None, REASONING_ITEMS_KEY: getattr(retried_msg, 'reasoning_items', None) or []}); retain side effects and discard the expression result.
    }
    // Source: vvaharness/backends/llm/openai.py:1331-1336
    if (the source predicate getattr(retried_choice, 'finish_reason', None) == OPENAI_FINISH_LENGTH is truthy) {
      // Source: vvaharness/backends/llm/openai.py:1332-1332
      In source order: Evaluate COUNTERS.bump(TRUNCATED_REPLIES_COUNTER); retain side effects and discard the expression result.
      // Source: vvaharness/backends/llm/openai.py:1333-1336
      Raise TruncatedResponseError('agentic reply still hit the output-token budget after the doubled retry', stage=tag or '', requested=requested, retried=retry_at).
    }
    // Source: vvaharness/backends/llm/openai.py:1338-1340
    In source order: Evaluate once retried_calls if not dispatchable else []; assign in source target order to undispatched. Then Evaluate once next((tc for tc in undispatched if response_model is not None and tc.function.name == RESPONSE_MODEL_TOOL_NAME), None); assign in source target order to submit.
    // Source: vvaharness/backends/llm/openai.py:1341-1349
    if (the source predicate undispatched and submit is None is truthy) {
      // Source: vvaharness/backends/llm/openai.py:1345-1349
      Raise TruncatedResponseError(source_literal_1346_16, stage=tag or '', requested=requested, retried=retry_at).
    }
    // Source: vvaharness/backends/llm/openai.py:1350-1350
    In source order: Evaluate COUNTERS.bump(TRUNCATED_RETRY_RECOVERED_COUNTER); retain side effects and discard the expression result.
    // Source: vvaharness/backends/llm/openai.py:1351-1352
    if (the source predicate submit is None or response_model is None is truthy) {
      // Source: vvaharness/backends/llm/openai.py:1352-1352
      End this invocation with (retried_choice, retried_msg, None).
    }
    // Source: vvaharness/backends/llm/openai.py:1355-1364
    Perform the following protected operations {
      // Source: vvaharness/backends/llm/openai.py:1356-1356
      In source order: Evaluate once json.loads(submit.function.arguments or '{}'); assign in source target order to args.
      // Source: vvaharness/backends/llm/openai.py:1357-1358
      End this invocation with (retried_choice, retried_msg, response_model.model_validate(args).model_dump_json()).
    }
    // Source: vvaharness/backends/llm/openai.py:1359-1364
    On the first matching source exception Exception, in handler order {
      // Source: vvaharness/backends/llm/openai.py:1363-1363
      In source order: Evaluate log.warning(Event.RESPONSE_MODEL_RETRY_INVALID, tool=RESPONSE_MODEL_TOOL_NAME); retain side effects and discard the expression result.
      // Source: vvaharness/backends/llm/openai.py:1364-1364
      End this invocation with (retried_choice, retried_msg, None).
    }
  }
  // Source: vvaharness/backends/llm/openai.py:1365-1366
  if (the source predicate refusal and (not (msg.content or '').strip()) is truthy) {
    // Source: vvaharness/backends/llm/openai.py:1366-1366
    Raise model_refusal(route='openai', stage=tag or '', category=None, detail=str(refusal)).
  }
  // Source: vvaharness/backends/llm/openai.py:1367-1367
  End this invocation with (choice, msg, None).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/openai.py:1370-1382
// Source signature: _responses_allowed(model: str, override: bool | None) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _responses_allowed(model, override) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/openai.py:1371-1376
  In source order: Retain source documentation literal source_literal_1371_4; it is not a model call.
  // Source: vvaharness/backends/llm/openai.py:1377-1378
  if (the source predicate model in TRANSPORT_MEMORY.chat_only is truthy) {
    // Source: vvaharness/backends/llm/openai.py:1378-1378
    End this invocation with False.
  }
  // Source: vvaharness/backends/llm/openai.py:1379-1381
  In source order: Resolve source import from vvaharness.backends.harness.deepagents.options.model_building import resolve_use_responses_api; preserve alias and import-time effects.
  // Source: vvaharness/backends/llm/openai.py:1382-1382
  End this invocation with bool(resolve_use_responses_api(model, None, override)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/openai.py:1385-1391
// Source signature: _initial_transport(model: str, override: bool | None) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _initial_transport(model, override) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/openai.py:1386-1386
  In source order: Retain source documentation literal source_literal_1386_4; it is not a model call.
  // Source: vvaharness/backends/llm/openai.py:1387-1388
  if (the source predicate override is True and _responses_allowed(model, override) is truthy) {
    // Source: vvaharness/backends/llm/openai.py:1388-1388
    End this invocation with TRANSPORT_RESPONSES.
  }
  // Source: vvaharness/backends/llm/openai.py:1389-1390
  if (the source predicate model in EFFORT_REJECTIONS.tools_off and _responses_allowed(model, override) is truthy) {
    // Source: vvaharness/backends/llm/openai.py:1390-1390
    End this invocation with TRANSPORT_RESPONSES.
  }
  // Source: vvaharness/backends/llm/openai.py:1391-1391
  End this invocation with TRANSPORT_CHAT.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/openai.py:1394-1397
// Source signature: _turn_client(client: openai.OpenAI, session_t0: float, session_budget: float | None, request_timeout: float) -> openai.OpenAI
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _turn_client(client, session_t0, session_budget, request_timeout) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/openai.py:1396-1396
  In source order: Retain source documentation literal source_literal_1396_4; it is not a model call.
  // Source: vvaharness/backends/llm/openai.py:1397-1397
  End this invocation with client.with_options(**turn_options(session_t0, session_budget, request_timeout)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/openai.py:1400-1413
// Source signature: _send_turn(client: openai.OpenAI, transport: str, messages: list[dict], kw: dict) -> Any
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _send_turn(client, transport, messages, kw) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/openai.py:1401-1405
  In source order: Retain source documentation literal source_literal_1401_4; it is not a model call.
  // Source: vvaharness/backends/llm/openai.py:1406-1407
  if (the source predicate transport == TRANSPORT_CHAT is truthy) {
    // Source: vvaharness/backends/llm/openai.py:1407-1407
    End this invocation with client.chat.completions.create(messages=to_chat_messages(messages), **kw).
  }
  // Source: vvaharness/backends/llm/openai.py:1408-1412
  In source order: Evaluate once to_responses_request(messages, kw, include_encrypted=kw['model'] not in TRANSPORT_MEMORY.no_include); assign in source target order to request. Then Evaluate once from_response(client.responses.create(**request)); assign in source target order to resp. Then Evaluate TRANSPORT_MEMORY.responses_proven.add(kw['model']); retain side effects and discard the expression result. Then Evaluate COUNTERS.bump('openai_responses_api_calls'); retain side effects and discard the expression result.
  // Source: vvaharness/backends/llm/openai.py:1413-1413
  End this invocation with resp.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/openai.py:1416-1423
// Source signature: _learn_chat_only(model: str) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _learn_chat_only(model) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/openai.py:1417-1423
  In source order: Retain source documentation literal source_literal_1417_4; it is not a model call. Then Evaluate TRANSPORT_MEMORY.chat_only.add(model); retain side effects and discard the expression result. Then Evaluate COUNTERS.bump('openai_responses_fallback'); retain side effects and discard the expression result. Then Evaluate warn_once(_WARNED_DROPS, source_template_1421_23, source_template_1422_8); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/openai.py:1426-1430
// Source signature: _fall_back_to_chat(model: str, base_kw: dict) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _fall_back_to_chat(model, base_kw) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/openai.py:1427-1428
  In source order: Retain source documentation literal source_literal_1427_4; it is not a model call. Then Evaluate _learn_chat_only(model); retain side effects and discard the expression result.
  // Source: vvaharness/backends/llm/openai.py:1429-1430
  if (the source predicate model in EFFORT_REJECTIONS.tools_off is truthy) {
    // Source: vvaharness/backends/llm/openai.py:1430-1430
    In source order: Evaluate once REASONING_OFF; assign in source target order to base_kw['reasoning_effort'].
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/openai.py:1433-1441
// Source signature: _responses_failure_falls_back(model: str, e: BaseException) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _responses_failure_falls_back(model, e) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/openai.py:1434-1440
  In source order: Retain source documentation literal source_literal_1434_4; it is not a model call.
  // Source: vvaharness/backends/llm/openai.py:1441-1441
  End this invocation with is_responses_shape_rejection(e) or model not in TRANSPORT_MEMORY.responses_proven.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/openai.py:1444-1455
// Source signature: _handle_include_rejection(model: str, e: BaseException, *, transport: str) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _handle_include_rejection(model, e, transport) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/openai.py:1445-1445
  In source order: Retain source documentation literal source_literal_1445_4; it is not a model call.
  // Source: vvaharness/backends/llm/openai.py:1446-1447
  if (the source predicate transport != TRANSPORT_RESPONSES or not is_param_rejection(e, 'include') is truthy) {
    // Source: vvaharness/backends/llm/openai.py:1447-1447
    End this invocation with False.
  }
  // Source: vvaharness/backends/llm/openai.py:1448-1454
  if (the source predicate model not in TRANSPORT_MEMORY.no_include is truthy) {
    // Source: vvaharness/backends/llm/openai.py:1449-1454
    In source order: Evaluate TRANSPORT_MEMORY.no_include.add(model); retain side effects and discard the expression result. Then Evaluate warn_once(_WARNED_DROPS, source_template_1451_27, source_template_1452_12); retain side effects and discard the expression result.
  }
  // Source: vvaharness/backends/llm/openai.py:1455-1455
  End this invocation with True.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/openai.py:1458-1462
interface _EffortOutcome {
  Describe the source Python type, preserving its base/metaclass expression order: NamedTuple.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/llm/openai.py:1459-1462
  In source order: Retain source documentation literal source_literal_1459_4; it is not a model call. Then For transport, declare without assigning a value; source annotation str. Then For fail, assign False; source annotation bool.
}
// Source: vvaharness/backends/llm/openai.py:1465-1483
// Source signature: _handle_tools_conflict(model: str, base_kw: dict, override: bool | None) -> _EffortOutcome
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _handle_tools_conflict(model, base_kw, override) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/openai.py:1466-1468
  In source order: Retain source documentation literal source_literal_1466_4; it is not a model call. Then Evaluate EFFORT_REJECTIONS.tools_off.add(model); retain side effects and discard the expression result. Then Evaluate COUNTERS.bump('llm_effort_tools_off'); retain side effects and discard the expression result.
  // Source: vvaharness/backends/llm/openai.py:1469-1475
  if (the source predicate _responses_allowed(model, override) is truthy) {
    // Source: vvaharness/backends/llm/openai.py:1470-1474
    In source order: Evaluate warn_once(_WARNED_DROPS, source_template_1471_27, source_template_1472_12); retain side effects and discard the expression result.
    // Source: vvaharness/backends/llm/openai.py:1475-1475
    End this invocation with _EffortOutcome(TRANSPORT_RESPONSES).
  }
  // Source: vvaharness/backends/llm/openai.py:1476-1482
  In source order: Evaluate once REASONING_OFF; assign in source target order to base_kw['reasoning_effort']. Then Evaluate warn_once(_WARNED_DROPS, source_template_1478_23, source_template_1479_8); retain side effects and discard the expression result.
  // Source: vvaharness/backends/llm/openai.py:1483-1483
  End this invocation with _EffortOutcome(TRANSPORT_CHAT).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/openai.py:1486-1501
// Source signature: _handle_tier_rejection(model: str, base_kw: dict, e: BaseException, transport: str) -> _EffortOutcome
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _handle_tier_rejection(model, base_kw, e, transport) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/openai.py:1489-1491
  In source order: Retain source documentation literal source_literal_1489_4; it is not a model call. Then Evaluate once base_kw.get('reasoning_effort'); assign in source target order to sent. Then Evaluate once step_down(model, sent, e, transport); assign in source target order to nxt.
  // Source: vvaharness/backends/llm/openai.py:1492-1495
  if (the source predicate nxt is None is truthy) {
    // Source: vvaharness/backends/llm/openai.py:1493-1493
    In source order: Evaluate base_kw.pop('reasoning_effort', None); retain side effects and discard the expression result.
  }
  else {
    // Source: vvaharness/backends/llm/openai.py:1495-1495
    In source order: Evaluate once nxt; assign in source target order to base_kw['reasoning_effort'].
  }
  // Source: vvaharness/backends/llm/openai.py:1496-1500
  In source order: Evaluate COUNTERS.bump('llm_effort_tier_stepped_down'); retain side effects and discard the expression result. Then Evaluate warn_once(_WARNED_DROPS, source_template_1498_23, source_template_1499_8); retain side effects and discard the expression result.
  // Source: vvaharness/backends/llm/openai.py:1501-1501
  End this invocation with _EffortOutcome(transport).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/openai.py:1504-1511
// Source signature: _tools_off_exhausted(model: str, effort_cls: str, sent: str | None, transport: str) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _tools_off_exhausted(model, effort_cls, sent, transport) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/openai.py:1505-1509
  In source order: Retain source documentation literal source_literal_1505_4; it is not a model call.
  // Source: vvaharness/backends/llm/openai.py:1510-1511
  End this invocation with transport == TRANSPORT_CHAT and model in EFFORT_REJECTIONS.tools_off and (effort_cls == 'tools_conflict' or sent == REASONING_OFF).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/openai.py:1514-1523
// Source signature: _handle_field_rejection(model: str, base_kw: dict, transport: str) -> _EffortOutcome
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _handle_field_rejection(model, base_kw, transport) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/openai.py:1515-1522
  In source order: Retain source documentation literal source_literal_1515_4; it is not a model call. Then Evaluate EFFORT_REJECTIONS.field.add(model); retain side effects and discard the expression result. Then Evaluate base_kw.pop('reasoning_effort', None); retain side effects and discard the expression result. Then Evaluate COUNTERS.bump('llm_effort_field_dropped'); retain side effects and discard the expression result. Then Evaluate warn_once(_WARNED_DROPS, source_template_1520_23, source_template_1521_8); retain side effects and discard the expression result.
  // Source: vvaharness/backends/llm/openai.py:1523-1523
  End this invocation with _EffortOutcome(transport).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/openai.py:1526-1537
// Source signature: _handle_tier_or_noop(model: str, base_kw: dict, e: BaseException, sent: str | None, transport: str) -> _EffortOutcome | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _handle_tier_or_noop(model, base_kw, e, sent, transport) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/openai.py:1529-1534
  In source order: Retain source documentation literal source_literal_1529_4; it is not a model call.
  // Source: vvaharness/backends/llm/openai.py:1535-1536
  if (the source predicate sent is None is truthy) {
    // Source: vvaharness/backends/llm/openai.py:1536-1536
    End this invocation with None.
  }
  // Source: vvaharness/backends/llm/openai.py:1537-1537
  End this invocation with _handle_tier_rejection(model, base_kw, e, transport).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/openai.py:1540-1552
// Source signature: _dispatch_effort_class(model: str, base_kw: dict, e: BaseException, transport: str, override: bool | None) -> _EffortOutcome | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _dispatch_effort_class(model, base_kw, e, transport, override) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/openai.py:1543-1545
  In source order: Retain source documentation literal source_literal_1543_4; it is not a model call. Then Evaluate once classify_effort_rejection(e); assign in source target order to effort_cls. Then Evaluate once base_kw.get('reasoning_effort'); assign in source target order to sent.
  // Source: vvaharness/backends/llm/openai.py:1548-1549
  if (the source predicate effort_cls == 'tools_conflict' and transport == TRANSPORT_CHAT and (sent != REASONING_OFF) is truthy) {
    // Source: vvaharness/backends/llm/openai.py:1549-1549
    End this invocation with _handle_tools_conflict(model, base_kw, override).
  }
  // Source: vvaharness/backends/llm/openai.py:1550-1551
  if (the source predicate effort_cls == 'field' is truthy) {
    // Source: vvaharness/backends/llm/openai.py:1551-1551
    End this invocation with _handle_field_rejection(model, base_kw, transport).
  }
  // Source: vvaharness/backends/llm/openai.py:1552-1552
  End this invocation with _handle_tier_or_noop(model, base_kw, e, sent, transport).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/openai.py:1555-1573
// Source signature: _handle_effort_rejection(model: str, base_kw: dict, e: BaseException, *, transport: str, override: bool | None) -> _EffortOutcome | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _handle_effort_rejection(model, base_kw, e, transport, override) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/openai.py:1558-1566
  In source order: Retain source documentation literal source_literal_1558_4; it is not a model call. Then Evaluate once classify_effort_rejection(e); assign in source target order to effort_cls.
  // Source: vvaharness/backends/llm/openai.py:1567-1568
  if (the source predicate effort_cls is None is truthy) {
    // Source: vvaharness/backends/llm/openai.py:1568-1568
    End this invocation with None.
  }
  // Source: vvaharness/backends/llm/openai.py:1569-1569
  In source order: Evaluate once base_kw.get('reasoning_effort'); assign in source target order to sent.
  // Source: vvaharness/backends/llm/openai.py:1570-1572
  if (the source predicate _tools_off_exhausted(model, effort_cls, sent, transport) is truthy) {
    // Source: vvaharness/backends/llm/openai.py:1571-1571
    In source order: Evaluate EFFORT_REJECTIONS.tiers.add(_tiers_key(model, REASONING_OFF, transport)); retain side effects and discard the expression result.
    // Source: vvaharness/backends/llm/openai.py:1572-1572
    End this invocation with _EffortOutcome(transport, fail=True).
  }
  // Source: vvaharness/backends/llm/openai.py:1573-1573
  End this invocation with _dispatch_effort_class(model, base_kw, e, transport, override).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/openai.py:1576-1586
// Source signature: _run_localtool(name: str, args: dict, *, ok_tools: list[str], cwd: str, tag: str | None) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _run_localtool(name, args, ok_tools, cwd, tag) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/openai.py:1578-1578
  In source order: Retain source documentation literal source_literal_1578_4; it is not a model call.
  // Source: vvaharness/backends/llm/openai.py:1579-1581
  if (the source predicate name not in ok_tools is truthy) {
    // Source: vvaharness/backends/llm/openai.py:1581-1581
    End this invocation with _localtools.UNGRANTED_TOOL_ERROR.format(name=name).
  }
  // Source: vvaharness/backends/llm/openai.py:1582-1582
  In source order: Evaluate once _cap_tool_result(_localtools.execute(name, args, cwd=cwd)); assign in source target order to result.
  // Source: vvaharness/backends/llm/openai.py:1583-1585
  if (the source predicate not is_stage_only() is truthy) {
    // Source: vvaharness/backends/llm/openai.py:1584-1585
    In source order: Evaluate console.write(source_template_1584_22); retain side effects and discard the expression result.
  }
  // Source: vvaharness/backends/llm/openai.py:1586-1586
  End this invocation with result.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/openai.py:1589-2185
// Source signature: agentic(user_prompt: str, *, model: str, system_prompt: str | None=None, allowed_tools: list[str] | None=None, cwd: str, max_budget_usd: float | None=None, permission_mode: str='auto', max_turns: int | None=None, timeout: int | None=None, tag: str | None=None, extra_tools: list[dict] | None=None, extra_dispatch=None, max_output_tokens: int | None=None, response_model: type[BaseModel] | None=None, output_cap: int | None=None, submit_guard: Callable[[], str | None] | None=None, exhausted_tools: Callable[[], frozenset[str]] | None=None, effort: str | None=None, use_responses_api: bool | None=None) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn agentic(user_prompt, model, system_prompt, allowed_tools, cwd, max_budget_usd, permission_mode, max_turns, timeout, tag, extra_tools, extra_dispatch, max_output_tokens, response_model, output_cap, submit_guard, exhausted_tools, effort, use_responses_api) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/openai.py:1641-1649
  In source order: Evaluate _warn_max_budget_unenforced('agentic', max_budget_usd); retain side effects and discard the expression result. Then Evaluate once _get_client(); assign in source target order to client. Then Evaluate once effort_scaled_seconds(DEFAULT_REQUEST_TIMEOUT_SECONDS, effort, kind=ClockKind.REQUEST); assign in source target order to request_timeout. Then Evaluate once effort_scaled_seconds(timeout, effort, kind=ClockKind.SESSION) if timeout else None; assign in source target order to session_budget. Then Evaluate once time.monotonic(); assign in source target order to session_t0.
  // Source: vvaharness/backends/llm/openai.py:1650-1652
  In source order: Evaluate once _initial_transport(model, use_responses_api); assign in source target order to transport. Then Evaluate once int(max_turns) if max_turns else _MAX_TURNS; assign in source target order to turns_cap. Then Evaluate once int(max_output_tokens) if max_output_tokens else _AGENTIC_MAX_TOK; assign in source target order to out_cap.
  // Source: vvaharness/backends/llm/openai.py:1653-1654
  if (the source predicate output_cap is not None is truthy) {
    // Source: vvaharness/backends/llm/openai.py:1654-1654
    In source order: Evaluate once min(out_cap, output_cap); assign in source target order to out_cap.
  }
  // Source: vvaharness/backends/llm/openai.py:1655-1655
  In source order: Evaluate once _LEARNED_OUTPUT_CAP.get(model); assign in source target order to learned_cap.
  // Source: vvaharness/backends/llm/openai.py:1656-1657
  if (the source predicate learned_cap is not None is truthy) {
    // Source: vvaharness/backends/llm/openai.py:1657-1657
    In source order: Evaluate once min(out_cap, learned_cap); assign in source target order to out_cap.
  }
  // Source: vvaharness/backends/llm/openai.py:1661-1662
  In source order: Evaluate once list(DEFAULT_READ_TOOLS) if allowed_tools is None else list(allowed_tools); assign in source target order to allowed. Then Evaluate once _localtools.supported(allowed); assign in source target order to (ok_tools, missing).
  // Source: vvaharness/backends/llm/openai.py:1663-1668
  if (the source predicate missing is truthy) {
    // Source: vvaharness/backends/llm/openai.py:1664-1668
    Raise NotImplementedError(source_template_1665_12).
  }
  // Source: vvaharness/backends/llm/openai.py:1669-1671
  In source order: Evaluate once [*_localtools.schemas_for(ok_tools), *(_anthropic_tool_to_openai(t) for t in extra_tools or [])]; assign in source target order to tools. Then Evaluate once ok_tools + [t.get('name') for t in extra_tools or []]; assign in source target order to advertised.
  // Source: vvaharness/backends/llm/openai.py:1672-1674
  if (the source predicate response_model is not None is truthy) {
    // Source: vvaharness/backends/llm/openai.py:1673-1674
    In source order: Evaluate tools.append(_anthropic_tool_to_openai(response_model_tool(response_model))); retain side effects and discard the expression result. Then Evaluate once [*advertised, RESPONSE_MODEL_TOOL_NAME]; assign in source target order to advertised.
  }
  // Source: vvaharness/backends/llm/openai.py:1676-1676
  In source order: For messages, assign []; source annotation list[dict].
  // Source: vvaharness/backends/llm/openai.py:1677-1678
  if (the source predicate system_prompt is truthy) {
    // Source: vvaharness/backends/llm/openai.py:1678-1678
    In source order: Evaluate messages.append({'role': 'system', 'content': system_prompt}); retain side effects and discard the expression result.
  }
  // Source: vvaharness/backends/llm/openai.py:1679-1684
  In source order: Evaluate messages.append({'role': 'user', 'content': user_prompt}); retain side effects and discard the expression result. Then Evaluate console.write(source_template_1681_18); retain side effects and discard the expression result. Then For base_kw, assign {'model': model, 'tools': tools}; source annotation dict.
  // Source: vvaharness/backends/llm/openai.py:1685-1688
  if (the source predicate model in _USE_LEGACY_MAXTOK is truthy) {
    // Source: vvaharness/backends/llm/openai.py:1686-1686
    In source order: Evaluate once out_cap; assign in source target order to base_kw['max_tokens'].
  }
  else {
    // Source: vvaharness/backends/llm/openai.py:1688-1688
    In source order: Evaluate once out_cap; assign in source target order to base_kw['max_completion_tokens'].
  }
  // Source: vvaharness/backends/llm/openai.py:1692-1695
  if (the source predicate _cache_markers_enabled() and model not in _NO_CACHE_KEY_MODELS is truthy) {
    // Source: vvaharness/backends/llm/openai.py:1693-1695
    In source order: Evaluate once _prompt_cache_key(tag, model, cache_prefix=(system_prompt or '') + user_prompt, preceding=json.dumps(tools, default=str)); assign in source target order to base_kw['prompt_cache_key'].
  }
  // Source: vvaharness/backends/llm/openai.py:1696-1707
  In source order: Evaluate base_kw.update(_reasoning_effort_kw(model, effort, transport, with_tools=True)); retain side effects and discard the expression result. Then Evaluate once ''; assign in source target order to final_text. Then Evaluate once 0; assign in source target order to tool_calls_total. Then Evaluate once False; assign in source target order to schema_nudged. Then Evaluate once 0; assign in source target order to submit_rejects.
  // Source: vvaharness/backends/llm/openai.py:1710-1710
  In source order: For withdrawn, assign frozenset(); source annotation frozenset[str].
  // Source: vvaharness/backends/llm/openai.py:1711-2051
  for each turn in range(1, turns_cap + 1) {
    // Source: vvaharness/backends/llm/openai.py:1712-1716
    if (the source predicate session_budget and time.monotonic() - session_t0 >= session_budget is truthy) {
      // Source: vvaharness/backends/llm/openai.py:1714-1716
      Raise call_timeout_error(stage=tag or '', route='openai', budget_s=session_budget, effort=effort, cause_text=source_template_1716_27).
    }
    // Source: vvaharness/backends/llm/openai.py:1717-1726
    if (the source predicate exhausted_tools is not None is truthy) {
      // Source: vvaharness/backends/llm/openai.py:1718-1718
      In source order: Evaluate once exhausted_tools() - withdrawn; assign in source target order to newly_exhausted.
      // Source: vvaharness/backends/llm/openai.py:1719-1726
      if (the source predicate newly_exhausted is truthy) {
        // Source: vvaharness/backends/llm/openai.py:1720-1726
        In source order: Apply source augmented assignment withdrawn |= newly_exhausted with source evaluation/in-place semantics. Then Evaluate once [t for t in base_kw['tools'] if t.get('function', {}).get('name') not in withdrawn]; assign in source target order to base_kw['tools']. Then Evaluate console.write(source_template_1724_30); retain side effects and discard the expression result.
      }
    }
    // Source: vvaharness/backends/llm/openai.py:1727-1733
    In source order: Evaluate once None; assign in source target order to resp. Then Evaluate once 0; assign in source target order to shrinks. Then Evaluate once 0; assign in source target order to transients. Then Evaluate once None; assign in source target order to server_error_probe. Then Evaluate once None; assign in source target order to server_error_exc.
    // Source: vvaharness/backends/llm/openai.py:1734-1901
    while (the source predicate resp is None is truthy) {
      // Source: vvaharness/backends/llm/openai.py:1735-1901
      Perform the following protected operations {
        // Source: vvaharness/backends/llm/openai.py:1736-1739
        In source order: Evaluate once time.monotonic(); assign in source target order to _t0. Then Evaluate once _turn_client(client, session_t0, session_budget, request_timeout); assign in source target order to turn_client. Then Evaluate once _send_turn(turn_client, transport, messages, base_kw); assign in source target order to resp. Then Evaluate note_budget_use(time.monotonic() - _t0, request_timeout, effort); retain side effects and discard the expression result.
      }
      // Source: vvaharness/backends/llm/openai.py:1740-1827
      On the first matching source exception (openai.BadRequestError, openai.UnprocessableEntityError) as e, in handler order {
        // Source: vvaharness/backends/llm/openai.py:1741-1744
        In source order: Evaluate _raise_if_refusal_rejection(e, tag=tag); retain side effects and discard the expression result. Then Evaluate once rejection_text(e).lower(); assign in source target order to low. Then Evaluate once _MAX_TOKENS_KEY if _MAX_TOKENS_KEY in base_kw else _MAX_COMPLETION_TOKENS_KEY; assign in source target order to agentic_budget_key.
        // Source: vvaharness/backends/llm/openai.py:1745-1762
        if (the source predicate model not in _LEARNED_OUTPUT_CAP and (_MAX_TOKENS_KEY in low or _MAX_COMPLETION_TOKENS_KEY in low or _MAX_OUTPUT_TOKENS_KEY in low) is truthy) {
          // Source: vvaharness/backends/llm/openai.py:1748-1749
          In source order: Evaluate once _learned_cap_from_body(low, requested=base_kw[agentic_budget_key]); assign in source target order to learned.
          // Source: vvaharness/backends/llm/openai.py:1750-1762
          if (the source predicate learned is not None is truthy) {
            // Source: vvaharness/backends/llm/openai.py:1751-1761
            In source order: Evaluate once learned; assign in source target order to _LEARNED_OUTPUT_CAP[model]. Then Evaluate warn_once(_WARNED_DROPS, source_template_1753_43, source_template_1754_28); retain side effects and discard the expression result. Then Evaluate once learned; assign in source target order to base_kw[agentic_budget_key].
            // Source: vvaharness/backends/llm/openai.py:1762-1762
            Continue the immediately enclosing source loop at its next iteration.
          }
        }
        // Source: vvaharness/backends/llm/openai.py:1763-1766
        if (the source predicate 'max_completion_tokens' in base_kw and 'max_completion_tokens' in low is truthy) {
          // Source: vvaharness/backends/llm/openai.py:1764-1765
          In source order: Evaluate _USE_LEGACY_MAXTOK.add(model); retain side effects and discard the expression result. Then Evaluate once base_kw.pop('max_completion_tokens'); assign in source target order to base_kw['max_tokens'].
          // Source: vvaharness/backends/llm/openai.py:1766-1766
          Continue the immediately enclosing source loop at its next iteration.
        }
        // Source: vvaharness/backends/llm/openai.py:1768-1773
        if (the source predicate 'prompt_cache_key' in base_kw and 'prompt_cache_key' in low is truthy) {
          // Source: vvaharness/backends/llm/openai.py:1769-1772
          In source order: Evaluate _NO_CACHE_KEY_MODELS.add(model); retain side effects and discard the expression result. Then Evaluate base_kw.pop('prompt_cache_key', None); retain side effects and discard the expression result. Then Evaluate console.write(source_template_1771_34); retain side effects and discard the expression result.
          // Source: vvaharness/backends/llm/openai.py:1773-1773
          Continue the immediately enclosing source loop at its next iteration.
        }
        // Source: vvaharness/backends/llm/openai.py:1779-1780
        In source order: Evaluate once _handle_effort_rejection(model, base_kw, e, transport=transport, override=use_responses_api); assign in source target order to effort_outcome.
        // Source: vvaharness/backends/llm/openai.py:1781-1794
        if (the source predicate effort_outcome is not None is truthy) {
          // Source: vvaharness/backends/llm/openai.py:1782-1792
          if (the source predicate effort_outcome.fail is truthy) {
            // Source: vvaharness/backends/llm/openai.py:1785-1792
            Raise RuntimeError(source_template_1786_28) with explicit source cause e.
          }
          // Source: vvaharness/backends/llm/openai.py:1793-1793
          In source order: Evaluate once effort_outcome.transport; assign in source target order to transport.
          // Source: vvaharness/backends/llm/openai.py:1794-1794
          Continue the immediately enclosing source loop at its next iteration.
        }
        // Source: vvaharness/backends/llm/openai.py:1795-1796
        if (the source predicate _handle_include_rejection(model, e, transport=transport) is truthy) {
          // Source: vvaharness/backends/llm/openai.py:1796-1796
          Continue the immediately enclosing source loop at its next iteration.
        }
        // Source: vvaharness/backends/llm/openai.py:1797-1801
        if (the source predicate transport == TRANSPORT_RESPONSES and _responses_failure_falls_back(model, e) is truthy) {
          // Source: vvaharness/backends/llm/openai.py:1799-1800
          In source order: Evaluate _fall_back_to_chat(model, base_kw); retain side effects and discard the expression result. Then Evaluate once TRANSPORT_CHAT; assign in source target order to transport.
          // Source: vvaharness/backends/llm/openai.py:1801-1801
          Continue the immediately enclosing source loop at its next iteration.
        }
        // Source: vvaharness/backends/llm/openai.py:1803-1808
        if (the source predicate _CTX_OVERFLOW_RX.search(low) and shrinks < 16 and _shrink_history(messages) is truthy) {
          // Source: vvaharness/backends/llm/openai.py:1805-1807
          In source order: Apply source augmented assignment shrinks += 1 with source evaluation/in-place semantics. Then Evaluate console.write(source_template_1806_34); retain side effects and discard the expression result.
          // Source: vvaharness/backends/llm/openai.py:1808-1808
          Continue the immediately enclosing source loop at its next iteration.
        }
        // Source: vvaharness/backends/llm/openai.py:1809-1811
        if (the source predicate _auth_failure_oai(e) is truthy) {
          // Source: vvaharness/backends/llm/openai.py:1810-1811
          Raise AuthenticationError(redact(str(e))[:400], status_code=e.status_code, backend='openai') with explicit source cause e.
        }
        // Source: vvaharness/backends/llm/openai.py:1813-1823
        if (the source predicate _is_transient_oai(e) and transients < _AGENTIC_TRANSIENT_RETRIES is truthy) {
          // Source: vvaharness/backends/llm/openai.py:1814-1815
          In source order: Apply source augmented assignment transients += 1 with source evaluation/in-place semantics. Then Evaluate once jittered_delay(min(60, 10 * transients)); assign in source target order to wait.
          // Source: vvaharness/backends/llm/openai.py:1816-1818
          if (the source predicate (overrun := wait_overrun(wait, session_t0, session_budget, stage=tag or '', route='openai', effort=effort)) is truthy) {
            // Source: vvaharness/backends/llm/openai.py:1818-1818
            Raise overrun with explicit source cause e.
          }
          // Source: vvaharness/backends/llm/openai.py:1819-1822
          In source order: Evaluate console.write(source_template_1819_34); retain side effects and discard the expression result. Then Evaluate time.sleep(wait); retain side effects and discard the expression result.
          // Source: vvaharness/backends/llm/openai.py:1823-1823
          Continue the immediately enclosing source loop at its next iteration.
        }
        // Source: vvaharness/backends/llm/openai.py:1824-1827
        Raise RuntimeError(source_template_1825_20) with explicit source cause e.
      }
      // Source: vvaharness/backends/llm/openai.py:1828-1878
      On the first matching source exception openai.APIStatusError as e, in handler order {
        // Source: vvaharness/backends/llm/openai.py:1829-1829
        In source order: Evaluate _raise_if_refusal_rejection(e, tag=tag); retain side effects and discard the expression result.
        // Source: vvaharness/backends/llm/openai.py:1834-1837
        if (the source predicate _auth_failure_oai(e) is truthy) {
          // Source: vvaharness/backends/llm/openai.py:1835-1837
          Raise AuthenticationError(redact(str(e))[:400], status_code=e.status_code, backend='openai') with explicit source cause e.
        }
        // Source: vvaharness/backends/llm/openai.py:1838-1848
        if (the source predicate _is_transient_oai(e) and transients < _AGENTIC_TRANSIENT_RETRIES is truthy) {
          // Source: vvaharness/backends/llm/openai.py:1839-1840
          In source order: Apply source augmented assignment transients += 1 with source evaluation/in-place semantics. Then Evaluate once jittered_delay(min(60, 10 * transients)); assign in source target order to wait.
          // Source: vvaharness/backends/llm/openai.py:1841-1843
          if (the source predicate (overrun := wait_overrun(wait, session_t0, session_budget, stage=tag or '', route='openai', effort=effort)) is truthy) {
            // Source: vvaharness/backends/llm/openai.py:1843-1843
            Raise overrun with explicit source cause e.
          }
          // Source: vvaharness/backends/llm/openai.py:1844-1847
          In source order: Evaluate console.write(source_template_1844_34); retain side effects and discard the expression result. Then Evaluate time.sleep(wait); retain side effects and discard the expression result.
          // Source: vvaharness/backends/llm/openai.py:1848-1848
          Continue the immediately enclosing source loop at its next iteration.
        }
        // Source: vvaharness/backends/llm/openai.py:1849-1855
        if (the source predicate transport == TRANSPORT_RESPONSES and model not in TRANSPORT_MEMORY.responses_proven is truthy) {
          // Source: vvaharness/backends/llm/openai.py:1853-1854
          In source order: Evaluate _fall_back_to_chat(model, base_kw); retain side effects and discard the expression result. Then Evaluate once TRANSPORT_CHAT; assign in source target order to transport.
          // Source: vvaharness/backends/llm/openai.py:1855-1855
          Continue the immediately enclosing source loop at its next iteration.
        }
        // Source: vvaharness/backends/llm/openai.py:1856-1863
        if (the source predicate server_error_probe is not None is truthy) {
          // Source: vvaharness/backends/llm/openai.py:1859-1863
          Raise RuntimeError(source_template_1860_24) with explicit source cause server_error_exc.
        }
        // Source: vvaharness/backends/llm/openai.py:1864-1869
        In source order: Evaluate once base_kw.get('reasoning_effort'); assign in source target order to sent. Then Evaluate once sent is not None and sent != REASONING_OFF and (e.status_code in SERVER_ERROR_STATUS); assign in source target order to can_probe. Then Evaluate once next_effort_tier(sent) if can_probe else None; assign in source target order to nxt.
        // Source: vvaharness/backends/llm/openai.py:1870-1874
        if (the source predicate nxt is not None and EFFORT_REJECTIONS.probe_once((claimed := _tiers_key(model, sent, transport))) is truthy) {
          // Source: vvaharness/backends/llm/openai.py:1872-1873
          In source order: Evaluate once ((model, sent, claimed), e); assign in source target order to (server_error_probe, server_error_exc). Then Evaluate once nxt; assign in source target order to base_kw['reasoning_effort'].
          // Source: vvaharness/backends/llm/openai.py:1874-1874
          Continue the immediately enclosing source loop at its next iteration.
        }
        // Source: vvaharness/backends/llm/openai.py:1875-1878
        Raise RuntimeError(source_template_1876_20) with explicit source cause e.
      }
      // Source: vvaharness/backends/llm/openai.py:1879-1901
      On the first matching source exception openai.APIConnectionError as e, in handler order {
        // Source: vvaharness/backends/llm/openai.py:1880-1884
        if (the source predicate is_timeout_failure(e) is truthy) {
          // Source: vvaharness/backends/llm/openai.py:1881-1884
          Raise call_timeout_error(stage=tag or '', route='openai', budget_s=request_timeout, effort=effort, cause_text=source_template_1883_35) with explicit source cause e.
        }
        // Source: vvaharness/backends/llm/openai.py:1885-1886
        if (the source predicate (proxy := proxy_error(e, backend='openai')) is truthy) {
          // Source: vvaharness/backends/llm/openai.py:1886-1886
          Raise proxy with explicit source cause e.
        }
        // Source: vvaharness/backends/llm/openai.py:1887-1897
        if (the source predicate transients < _AGENTIC_TRANSIENT_RETRIES is truthy) {
          // Source: vvaharness/backends/llm/openai.py:1888-1889
          In source order: Apply source augmented assignment transients += 1 with source evaluation/in-place semantics. Then Evaluate once jittered_delay(min(60, 10 * transients)); assign in source target order to wait.
          // Source: vvaharness/backends/llm/openai.py:1890-1892
          if (the source predicate (overrun := wait_overrun(wait, session_t0, session_budget, stage=tag or '', route='openai', effort=effort)) is truthy) {
            // Source: vvaharness/backends/llm/openai.py:1892-1892
            Raise overrun with explicit source cause e.
          }
          // Source: vvaharness/backends/llm/openai.py:1893-1896
          In source order: Evaluate console.write(source_template_1893_34); retain side effects and discard the expression result. Then Evaluate time.sleep(wait); retain side effects and discard the expression result.
          // Source: vvaharness/backends/llm/openai.py:1897-1897
          Continue the immediately enclosing source loop at its next iteration.
        }
        // Source: vvaharness/backends/llm/openai.py:1898-1901
        Raise RuntimeError(source_template_1899_20) with explicit source cause e.
      }
    }
    // Source: vvaharness/backends/llm/openai.py:1903-1913
    if (the source predicate server_error_probe is not None is truthy) {
      // Source: vvaharness/backends/llm/openai.py:1904-1904
      In source order: Evaluate once server_error_probe; assign in source target order to (probed_model, probed_sent, probed_key).
      // Source: vvaharness/backends/llm/openai.py:1905-1906
      if (the source predicate (learned := EFFORT_REJECTIONS.recovered_twice(probed_key)) is truthy) {
        // Source: vvaharness/backends/llm/openai.py:1906-1906
        In source order: Evaluate EFFORT_REJECTIONS.tiers.add(probed_key); retain side effects and discard the expression result.
      }
      // Source: vvaharness/backends/llm/openai.py:1907-1913
      In source order: Evaluate COUNTERS.bump('llm_effort_tier_stepped_down_on_server_error'); retain side effects and discard the expression result. Then Evaluate warn_once(_WARNED_DROPS, source_template_1909_31, source_template_1910_16); retain side effects and discard the expression result.
    }
    // Source: vvaharness/backends/llm/openai.py:1914-1918
    In source order: Evaluate _record_usage(getattr(resp, 'usage', None)); retain side effects and discard the expression result. Then Evaluate once _first_choice(resp, model=model, tag=tag, turn=turn); assign in source target order to choice. Then Evaluate once choice.message; assign in source target order to msg. Then Evaluate once getattr(msg, 'tool_calls', None) or []; assign in source target order to calls. Then Evaluate once getattr(choice, 'finish_reason', None); assign in source target order to finish.
    // Source: vvaharness/backends/llm/openai.py:1920-1928
    In source order: Evaluate once {'role': 'assistant', 'content': msg.content, 'tool_calls': [tc.model_dump() for tc in calls] if calls else None, REASONING_ITEMS_KEY: getattr(msg, 'reasoning_items', None) or []}; assign in source target order to assistant. Then Evaluate messages.append(assistant); retain side effects and discard the expression result.
    // Source: vvaharness/backends/llm/openai.py:1934-1970
    if (the source predicate not calls or finish == OPENAI_FINISH_LENGTH is truthy) {
      // Source: vvaharness/backends/llm/openai.py:1935-1935
      In source order: Evaluate once _turn_client(client, session_t0, session_budget, request_timeout); assign in source target order to retry_client.
      // Source: vvaharness/backends/llm/openai.py:1937-1939
      // Source signature: _retry_send(kw: dict, *, _tc: openai.OpenAI=retry_client, _tp: str=transport) -> Any
      Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
      fn _retry_send(kw, _tc, _tp) {
        Bind arguments/defaults/annotations exactly as the source signature specifies.
        // Source: vvaharness/backends/llm/openai.py:1939-1939
        End this invocation with _send_turn(_tc, _tp, messages, kw).
        If execution reaches this end, finish with the source implicit None result.
      }
      // Source: vvaharness/backends/llm/openai.py:1941-1945
      In source order: Evaluate once _check_terminal_finish(choice, msg, send=_retry_send, messages=messages, call_kw=base_kw, appended=True, model=model, tag=tag, requested=out_cap, response_model=response_model, dispatchable=True, output_cap=output_cap, effort=effort, request_timeout=request_timeout); assign in source target order to (choice, msg, override).
      // Source: vvaharness/backends/llm/openai.py:1946-1949
      if (the source predicate override is not None is truthy) {
        // Source: vvaharness/backends/llm/openai.py:1947-1948
        In source order: Evaluate console.write(source_template_1947_30); retain side effects and discard the expression result.
        // Source: vvaharness/backends/llm/openai.py:1949-1949
        End this invocation with override.
      }
      // Source: vvaharness/backends/llm/openai.py:1954-1954
      In source order: Evaluate once getattr(msg, 'tool_calls', None) or []; assign in source target order to calls.
      // Source: vvaharness/backends/llm/openai.py:1955-1970
      if (the source predicate not calls is truthy) {
        // Source: vvaharness/backends/llm/openai.py:1956-1956
        In source order: Evaluate once (msg.content or '').strip(); assign in source target order to final_text.
        // Source: vvaharness/backends/llm/openai.py:1961-1967
        if (the source predicate response_model is not None and (not schema_nudged) is truthy) {
          // Source: vvaharness/backends/llm/openai.py:1962-1966
          In source order: Evaluate once True; assign in source target order to schema_nudged. Then Evaluate COUNTERS.bump('llm_structured_prose_reask'); retain side effects and discard the expression result. Then Evaluate log.warning(Event.STRUCTURED_PROSE_REASK, route='openai', model=model, tool=RESPONSE_MODEL_TOOL_NAME); retain side effects and discard the expression result. Then Evaluate messages.append({'role': 'user', 'content': STRUCTURED_PROSE_REASK}); retain side effects and discard the expression result.
          // Source: vvaharness/backends/llm/openai.py:1967-1967
          Continue the immediately enclosing source loop at its next iteration.
        }
        // Source: vvaharness/backends/llm/openai.py:1968-1969
        In source order: Evaluate console.write(source_template_1968_30); retain side effects and discard the expression result.
        // Source: vvaharness/backends/llm/openai.py:1970-1970
        End this invocation with final_text.
      }
    }
    // Source: vvaharness/backends/llm/openai.py:1972-2051
    for each (i, tc) in enumerate(calls) {
      // Source: vvaharness/backends/llm/openai.py:1973-1974
      In source order: Apply source augmented assignment tool_calls_total += 1 with source evaluation/in-place semantics. Then Evaluate once tc.function.name; assign in source target order to name.
      // Source: vvaharness/backends/llm/openai.py:1975-1983
      Perform the following protected operations {
        // Source: vvaharness/backends/llm/openai.py:1976-1977
        In source order: Evaluate once json.loads(tc.function.arguments or '{}'); assign in source target order to args. Then Evaluate once True; assign in source target order to args_valid.
      }
      // Source: vvaharness/backends/llm/openai.py:1978-1983
      On the first matching source exception json.JSONDecodeError, in handler order {
        // Source: vvaharness/backends/llm/openai.py:1980-1983
        In source order: Evaluate once ({}, False); assign in source target order to (args, args_valid). Then Evaluate once '{}'; assign in source target order to assistant['tool_calls'][i]['function']['arguments'].
      }
      // Source: vvaharness/backends/llm/openai.py:1984-2032
      if (the source predicate response_model is not None and name == RESPONSE_MODEL_TOOL_NAME is truthy) {
        // Source: vvaharness/backends/llm/openai.py:1990-2018
        Perform the following protected operations {
          // Source: vvaharness/backends/llm/openai.py:1991-1991
          In source order: Evaluate once response_model.model_validate(args); assign in source target order to validated.
        }
        // Source: vvaharness/backends/llm/openai.py:1992-2018
        On the first matching source exception Exception as exc, in handler order {
          // Source: vvaharness/backends/llm/openai.py:1996-1997
          In source order: Apply source augmented assignment submit_rejects += 1 with source evaluation/in-place semantics. Then Evaluate COUNTERS.bump('llm_structured_submit_rejected'); retain side effects and discard the expression result.
          // Source: vvaharness/backends/llm/openai.py:1998-2009
          if (the source predicate submit_rejects >= STRUCTURED_REASK_MAX is truthy) {
            // Source: vvaharness/backends/llm/openai.py:1999-2008
            In source order: Evaluate log.warning(Event.STRUCTURED_SUBMIT_REJECTED, route='openai', tool=RESPONSE_MODEL_TOOL_NAME, error=type(exc).__name__, rejects=submit_rejects); retain side effects and discard the expression result. Then Evaluate once structured_failure_detail(exc); assign in source target order to (detail, _). Then Evaluate _errlog.log(tag or 'openai', tag or 'structured', source_template_2006_28, detail=detail, reason='llm_structured_reask_gave_up', recovered=True); retain side effects and discard the expression result.
            // Source: vvaharness/backends/llm/openai.py:2009-2009
            End this invocation with json.dumps(args).
          }
          // Source: vvaharness/backends/llm/openai.py:2010-2017
          In source order: Evaluate console.write(source_template_2010_34); retain side effects and discard the expression result. Then Evaluate messages.append({'role': 'tool', 'tool_call_id': tc.id, 'content': source_template_2015_36}); retain side effects and discard the expression result.
          // Source: vvaharness/backends/llm/openai.py:2018-2018
          Continue the immediately enclosing source loop at its next iteration.
        }
        // Source: vvaharness/backends/llm/openai.py:2019-2029
        if (the source predicate submit_guard is not None is truthy) {
          // Source: vvaharness/backends/llm/openai.py:2020-2020
          In source order: Evaluate once submit_guard(); assign in source target order to hold_text.
          // Source: vvaharness/backends/llm/openai.py:2021-2029
          if (the source predicate hold_text is not None is truthy) {
            // Source: vvaharness/backends/llm/openai.py:2022-2028
            In source order: Evaluate console.write(source_template_2022_38); retain side effects and discard the expression result. Then Evaluate messages.append({'role': 'tool', 'tool_call_id': tc.id, 'content': hold_text}); retain side effects and discard the expression result.
            // Source: vvaharness/backends/llm/openai.py:2029-2029
            Continue the immediately enclosing source loop at its next iteration.
          }
        }
        // Source: vvaharness/backends/llm/openai.py:2030-2031
        In source order: Evaluate console.write(source_template_2030_30); retain side effects and discard the expression result.
        // Source: vvaharness/backends/llm/openai.py:2032-2032
        End this invocation with validated.model_dump_json().
      }
      // Source: vvaharness/backends/llm/openai.py:2037-2046
      if (the source predicate args_valid is truthy) {
        // Source: vvaharness/backends/llm/openai.py:2038-2038
        In source order: Evaluate once extra_dispatch(name, args) if extra_dispatch is not None else None; assign in source target order to result.
        // Source: vvaharness/backends/llm/openai.py:2039-2040
        if (the source predicate result is None is truthy) {
          // Source: vvaharness/backends/llm/openai.py:2040-2040
          In source order: Evaluate once _run_localtool(name, args, ok_tools=ok_tools, cwd=cwd, tag=tag); assign in source target order to result.
        }
      }
      else {
        // Source: vvaharness/backends/llm/openai.py:2042-2046
        In source order: Evaluate COUNTERS.bump('openai_tool_args_invalid_json'); retain side effects and discard the expression result. Then Evaluate log.warning(Event.TOOL_ARGS_INVALID_JSON, route='openai', tool=redact(name)[:200], tag=tag or None); retain side effects and discard the expression result. Then Evaluate once 'ERROR: tool arguments were not valid JSON'; assign in source target order to result.
      }
      // Source: vvaharness/backends/llm/openai.py:2047-2051
      In source order: Evaluate messages.append({'role': 'tool', 'tool_call_id': tc.id, 'content': result}); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/backends/llm/openai.py:2053-2061
  In source order: Evaluate log.warning(Event.LLM_TURN_CAP_EXHAUSTED, turns_cap=turns_cap, model=model, tag=tag); retain side effects and discard the expression result. Then Evaluate COUNTERS.bump('llm_turn_cap_exhausted'); retain side effects and discard the expression result. Then For forced_kw, assign {k: v for k, v in base_kw.items() if k != 'tools'}; source annotation dict. Then Evaluate once model; assign in source target order to forced_kw['model'].
  // Source: vvaharness/backends/llm/openai.py:2062-2074
  if (the source predicate response_model is not None is truthy) {
    // Source: vvaharness/backends/llm/openai.py:2063-2064
    In source order: Evaluate once [_anthropic_tool_to_openai(response_model_tool(response_model))]; assign in source target order to forced_kw['tools'].
    // Source: vvaharness/backends/llm/openai.py:2065-2068
    if (the source predicate model not in _NO_TOOL_CHOICE_MODELS is truthy) {
      // Source: vvaharness/backends/llm/openai.py:2066-2068
      In source order: Evaluate once {'type': 'function', 'function': {'name': RESPONSE_MODEL_TOOL_NAME}}; assign in source target order to forced_kw['tool_choice'].
    }
    // Source: vvaharness/backends/llm/openai.py:2069-2071
    In source order: Evaluate once source_template_2069_23; assign in source target order to instruction.
  }
  else {
    // Source: vvaharness/backends/llm/openai.py:2073-2074
    In source order: Evaluate once 'Tool budget exhausted. Reply now with your final answer based on what you have read so far; do not call tools.'; assign in source target order to instruction.
  }
  // Source: vvaharness/backends/llm/openai.py:2075-2076
  In source order: Evaluate messages.append({'role': 'user', 'content': instruction}); retain side effects and discard the expression result. Then Evaluate once 0; assign in source target order to final_transients.
  // Source: vvaharness/backends/llm/openai.py:2077-2157
  while (the source predicate True is truthy) {
    // Source: vvaharness/backends/llm/openai.py:2078-2157
    Perform the following protected operations {
      // Source: vvaharness/backends/llm/openai.py:2079-2082
      In source order: Evaluate once time.monotonic(); assign in source target order to _t0. Then Evaluate once _turn_client(client, session_t0, session_budget, request_timeout); assign in source target order to final_client. Then Evaluate once _send_turn(final_client, transport, messages, forced_kw); assign in source target order to resp. Then Evaluate note_budget_use(time.monotonic() - _t0, request_timeout, effort); retain side effects and discard the expression result.
      // Source: vvaharness/backends/llm/openai.py:2083-2083
      Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
    }
    // Source: vvaharness/backends/llm/openai.py:2084-2113
    On the first matching source exception (openai.BadRequestError, openai.UnprocessableEntityError) as e, in handler order {
      // Source: vvaharness/backends/llm/openai.py:2085-2085
      In source order: Evaluate _raise_if_refusal_rejection(e, tag=tag); retain side effects and discard the expression result.
      // Source: vvaharness/backends/llm/openai.py:2089-2094
      if (the source predicate 'tool_choice' in forced_kw and 'tool_choice' in rejection_text(e).lower() is truthy) {
        // Source: vvaharness/backends/llm/openai.py:2090-2093
        In source order: Evaluate _NO_TOOL_CHOICE_MODELS.add(model); retain side effects and discard the expression result. Then Evaluate forced_kw.pop('tool_choice', None); retain side effects and discard the expression result. Then Evaluate console.write(source_template_2092_30); retain side effects and discard the expression result.
        // Source: vvaharness/backends/llm/openai.py:2094-2094
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/backends/llm/openai.py:2095-2097
      if (the source predicate _auth_failure_oai(e) is truthy) {
        // Source: vvaharness/backends/llm/openai.py:2096-2097
        Raise AuthenticationError(redact(str(e))[:400], status_code=e.status_code, backend='openai') with explicit source cause e.
      }
      // Source: vvaharness/backends/llm/openai.py:2099-2109
      if (the source predicate _is_transient_oai(e) and final_transients < _AGENTIC_TRANSIENT_RETRIES is truthy) {
        // Source: vvaharness/backends/llm/openai.py:2100-2101
        In source order: Apply source augmented assignment final_transients += 1 with source evaluation/in-place semantics. Then Evaluate once jittered_delay(min(60, 10 * final_transients)); assign in source target order to wait.
        // Source: vvaharness/backends/llm/openai.py:2102-2104
        if (the source predicate (overrun := wait_overrun(wait, session_t0, session_budget, stage=tag or '', route='openai', effort=effort)) is truthy) {
          // Source: vvaharness/backends/llm/openai.py:2104-2104
          Raise overrun with explicit source cause e.
        }
        // Source: vvaharness/backends/llm/openai.py:2105-2108
        In source order: Evaluate console.write(source_template_2105_30); retain side effects and discard the expression result. Then Evaluate time.sleep(wait); retain side effects and discard the expression result.
        // Source: vvaharness/backends/llm/openai.py:2109-2109
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/backends/llm/openai.py:2110-2113
      Raise RuntimeError(source_template_2111_16) with explicit source cause e.
    }
    // Source: vvaharness/backends/llm/openai.py:2114-2134
    On the first matching source exception openai.APIStatusError as e, in handler order {
      // Source: vvaharness/backends/llm/openai.py:2115-2115
      In source order: Evaluate _raise_if_refusal_rejection(e, tag=tag); retain side effects and discard the expression result.
      // Source: vvaharness/backends/llm/openai.py:2116-2119
      if (the source predicate _auth_failure_oai(e) is truthy) {
        // Source: vvaharness/backends/llm/openai.py:2117-2119
        Raise AuthenticationError(redact(str(e))[:400], status_code=e.status_code, backend='openai') with explicit source cause e.
      }
      // Source: vvaharness/backends/llm/openai.py:2120-2130
      if (the source predicate _is_transient_oai(e) and final_transients < _AGENTIC_TRANSIENT_RETRIES is truthy) {
        // Source: vvaharness/backends/llm/openai.py:2121-2122
        In source order: Apply source augmented assignment final_transients += 1 with source evaluation/in-place semantics. Then Evaluate once jittered_delay(min(60, 10 * final_transients)); assign in source target order to wait.
        // Source: vvaharness/backends/llm/openai.py:2123-2125
        if (the source predicate (overrun := wait_overrun(wait, session_t0, session_budget, stage=tag or '', route='openai', effort=effort)) is truthy) {
          // Source: vvaharness/backends/llm/openai.py:2125-2125
          Raise overrun with explicit source cause e.
        }
        // Source: vvaharness/backends/llm/openai.py:2126-2129
        In source order: Evaluate console.write(source_template_2126_30); retain side effects and discard the expression result. Then Evaluate time.sleep(wait); retain side effects and discard the expression result.
        // Source: vvaharness/backends/llm/openai.py:2130-2130
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/backends/llm/openai.py:2131-2134
      Raise RuntimeError(source_template_2132_16) with explicit source cause e.
    }
    // Source: vvaharness/backends/llm/openai.py:2135-2157
    On the first matching source exception openai.APIConnectionError as e, in handler order {
      // Source: vvaharness/backends/llm/openai.py:2136-2140
      if (the source predicate is_timeout_failure(e) is truthy) {
        // Source: vvaharness/backends/llm/openai.py:2137-2140
        Raise call_timeout_error(stage=tag or '', route='openai', budget_s=request_timeout, effort=effort, cause_text=source_template_2139_31) with explicit source cause e.
      }
      // Source: vvaharness/backends/llm/openai.py:2141-2142
      if (the source predicate (proxy := proxy_error(e, backend='openai')) is truthy) {
        // Source: vvaharness/backends/llm/openai.py:2142-2142
        Raise proxy with explicit source cause e.
      }
      // Source: vvaharness/backends/llm/openai.py:2143-2153
      if (the source predicate final_transients < _AGENTIC_TRANSIENT_RETRIES is truthy) {
        // Source: vvaharness/backends/llm/openai.py:2144-2145
        In source order: Apply source augmented assignment final_transients += 1 with source evaluation/in-place semantics. Then Evaluate once jittered_delay(min(60, 10 * final_transients)); assign in source target order to wait.
        // Source: vvaharness/backends/llm/openai.py:2146-2148
        if (the source predicate (overrun := wait_overrun(wait, session_t0, session_budget, stage=tag or '', route='openai', effort=effort)) is truthy) {
          // Source: vvaharness/backends/llm/openai.py:2148-2148
          Raise overrun with explicit source cause e.
        }
        // Source: vvaharness/backends/llm/openai.py:2149-2152
        In source order: Evaluate console.write(source_template_2149_30); retain side effects and discard the expression result. Then Evaluate time.sleep(wait); retain side effects and discard the expression result.
        // Source: vvaharness/backends/llm/openai.py:2153-2153
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/backends/llm/openai.py:2154-2157
      Raise RuntimeError(source_template_2155_16) with explicit source cause e.
    }
  }
  // Source: vvaharness/backends/llm/openai.py:2158-2159
  In source order: Evaluate _record_usage(getattr(resp, 'usage', None)); retain side effects and discard the expression result. Then Evaluate once _first_choice(resp, model=model, tag=tag, turn=turns_cap); assign in source target order to final_choice.
  // Source: vvaharness/backends/llm/openai.py:2161-2163
  // Source signature: _final_retry_send(kw: dict, *, _tc: openai.OpenAI=final_client, _tp: str=transport) -> Any
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _final_retry_send(kw, _tc, _tp) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/llm/openai.py:2163-2163
    End this invocation with _send_turn(_tc, _tp, messages, kw).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/llm/openai.py:2165-2169
  In source order: Evaluate once _check_terminal_finish(final_choice, final_choice.message, send=_final_retry_send, messages=messages, call_kw=forced_kw, appended=False, model=model, tag=tag, requested=out_cap, response_model=response_model, output_cap=output_cap, effort=effort, request_timeout=request_timeout); assign in source target order to (final_choice, final_msg, override).
  // Source: vvaharness/backends/llm/openai.py:2170-2171
  if (the source predicate override is not None is truthy) {
    // Source: vvaharness/backends/llm/openai.py:2171-2171
    End this invocation with override.
  }
  // Source: vvaharness/backends/llm/openai.py:2172-2184
  if (the source predicate response_model is not None is truthy) {
    // Source: vvaharness/backends/llm/openai.py:2173-2184
    for each tc in getattr(final_msg, 'tool_calls', None) or [] {
      // Source: vvaharness/backends/llm/openai.py:2174-2175
      if (the source predicate tc.function.name != RESPONSE_MODEL_TOOL_NAME is truthy) {
        // Source: vvaharness/backends/llm/openai.py:2175-2175
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/backends/llm/openai.py:2176-2184
      Perform the following protected operations {
        // Source: vvaharness/backends/llm/openai.py:2177-2177
        In source order: Evaluate once json.loads(tc.function.arguments or '{}'); assign in source target order to args.
        // Source: vvaharness/backends/llm/openai.py:2178-2178
        End this invocation with response_model.model_validate(args).model_dump_json().
      }
      // Source: vvaharness/backends/llm/openai.py:2179-2184
      On the first matching source exception Exception as exc, in handler order {
        // Source: vvaharness/backends/llm/openai.py:2183-2184
        In source order: Evaluate log.warning(Event.RESPONSE_MODEL_FORCED_FINAL_INVALID, tool=RESPONSE_MODEL_TOOL_NAME, error=type(exc).__name__); retain side effects and discard the expression result.
      }
    }
  }
  // Source: vvaharness/backends/llm/openai.py:2185-2185
  End this invocation with (final_msg.content or '').strip().
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.util import logs` at source line 45: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import logs` at source line 45: `source_detail/vvaharness/util/logs.py.sudo.md`.
- `from vvaharness.backends.harness.models import AuthenticationError, TruncatedResponseError, truncated_below_budget` at source line 54: `source_detail/vvaharness/backends/harness/models.py.sudo.md`.
- `from vvaharness.backends.llm import cache as _cache` at source line 59: `source_detail/vvaharness/backends/llm/__init__.py.sudo.md`.
- `from vvaharness.backends.llm import cache as _cache` at source line 59: `source_detail/vvaharness/backends/llm/cache.py.sudo.md`.
- `from vvaharness.backends.llm import tools as _localtools` at source line 60: `source_detail/vvaharness/backends/llm/__init__.py.sudo.md`.
- `from vvaharness.backends.llm import tools as _localtools` at source line 60: `source_detail/vvaharness/backends/llm/tools.py.sudo.md`.
- `from vvaharness.backends.llm.models import AGENTIC_MAX_TOKENS, DEFAULT_READ_TOOLS, DEFAULT_REQUEST_TIMEOUT_SECONDS, EFFORT_REJECTIONS, LLM_TRUNCATED_BELOW_BUDGET_COUNTER, OPENAI_FINISH_LENGTH, RATE_LIMIT_TRANSIENT_RX, REASONING_OFF, RESPONSE_MODEL_TOOL_NAME, RETRYABLE_STATUS, SERVER_ERROR_STATUS, SERVER_ERROR_TRANSIENT_RX, STRUCTURED_PROSE_REASK, STRUCTURED_REASK_MAX, TRANSPORT_CHAT, TRANSPORT_MEMORY, TRANSPORT_RESPONSES, TRUNCATED_REPLIES_COUNTER, TRUNCATED_RETRY_ATTEMPTED_COUNTER, TRUNCATED_RETRY_RECOVERED_COUNTER, ClockKind, OpenAiConfig, _tiers_key, call_timeout_error, classify_effort_rejection, effort_after_rejections, effort_scaled_seconds, is_param_rejection, is_responses_shape_rejection, jittered_delay, model_refusal, model_refusal_from, next_effort_tier, note_budget_use, proxy_error, rejection_text, response_model_tool, step_down, truncation_retry_max, turn_options, wait_overrun` at source line 61: `source_detail/vvaharness/backends/llm/models.py.sudo.md`.
- `from vvaharness.backends.llm.openai_responses import REASONING_ITEMS_KEY, from_response, to_chat_messages, to_responses_request` at source line 104: `source_detail/vvaharness/backends/llm/openai_responses.py.sudo.md`.
- `from vvaharness.backends.llm.tls import coerce_verify, scoped_no_proxy_env, warn_verify_disabled` at source line 110: `source_detail/vvaharness/backends/llm/tls.py.sudo.md`.
- `from vvaharness.report.redact import redact` at source line 115: `source_detail/vvaharness/report/redact.py.sudo.md`.
- `from vvaharness.util import console` at source line 116: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import console` at source line 116: `source_detail/vvaharness/util/console.py.sudo.md`.
- `from vvaharness.util import errlog as _errlog` at source line 117: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import errlog as _errlog` at source line 117: `source_detail/vvaharness/util/errlog.py.sudo.md`.
- `from vvaharness.util.counters import COUNTERS` at source line 118: `source_detail/vvaharness/util/counters.py.sudo.md`.
- `from vvaharness.util.events import Event` at source line 119: `source_detail/vvaharness/util/events.py.sudo.md`.
- `from vvaharness.util.response_quality import check_response_quality, is_timeout_failure, output_tokens_for_gate, structured_failure_detail` at source line 120: `source_detail/vvaharness/util/response_quality.py.sudo.md`.
- `from vvaharness.util.scan_progress import get_active_tracker, is_stage_only` at source line 126: `source_detail/vvaharness/util/scan_progress.py.sudo.md`.
- `from vvaharness.util.tokens import TOKENS, TokenUsage, estimate_tokens` at source line 127: `source_detail/vvaharness/util/tokens.py.sudo.md`.
- `from vvaharness.util.warn_once import warn_once` at source line 128: `source_detail/vvaharness/util/warn_once.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.options.model_building import _to_openai_reasoning_effort` at source line 446: `source_detail/vvaharness/backends/harness/deepagents/options/model_building.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.options.model_building import resolve_use_responses_api` at source line 1379: `source_detail/vvaharness/backends/harness/deepagents/options/model_building.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../prompt_representation/vvaharness/backends/llm/openai.py.sudo.md). Exact strings in the evidence asset support this conversion.
