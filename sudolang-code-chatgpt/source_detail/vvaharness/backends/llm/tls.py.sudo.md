# vvaharness/backends/llm/tls.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/backends/llm/tls.py.evidence.json`. SHA-256: `ecc22e7aad47faaacb475c78ce589ca8c668095e757bf1717b04e77cb99c2ec5`.

```sudo
// Source: vvaharness/backends/llm/tls.py:15-22
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import os; preserve alias and import-time effects. Then Resolve source import import ssl; preserve alias and import-time effects. Then Resolve source import from collections.abc import Iterator; preserve alias and import-time effects.
// Source: vvaharness/backends/llm/tls.py:23-30
In source order: Resolve source import from contextlib import contextmanager; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import logs; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.events import Event; preserve alias and import-time effects. Then Evaluate once logs.get_logger(__name__); assign in source target order to log. Then Evaluate once {'true', '1', 'yes', 'on'}; assign in source target order to _TRUE.
// Source: vvaharness/backends/llm/tls.py:31-34
In source order: Evaluate once {'false', '0', 'no', 'off'}; assign in source target order to _FALSE. Then Evaluate once ('NO_PROXY', 'no_proxy'); assign in source target order to _NO_PROXY_KEYS. Then Evaluate once 'sk-ant-oat'; assign in source target order to _OAUTH_TOKEN_PREFIX. Then Evaluate once 'oauth-2025-04-20'; assign in source target order to _OAUTH_BETA_HEADER.
// Source: vvaharness/backends/llm/tls.py:37-45
// Source signature: anthropic_auth_kwargs(token: str | None) -> dict[str, object]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn anthropic_auth_kwargs(token) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/tls.py:38-39
  In source order: Retain source documentation literal source_literal_38_4; it is not a model call. Then Evaluate once (token or '').strip(); assign in source target order to token.
  // Source: vvaharness/backends/llm/tls.py:40-44
  if (the source predicate token.startswith(_OAUTH_TOKEN_PREFIX) is truthy) {
    // Source: vvaharness/backends/llm/tls.py:41-44
    End this invocation with {'auth_token': token, 'default_headers': {'anthropic-beta': _OAUTH_BETA_HEADER}}.
  }
  // Source: vvaharness/backends/llm/tls.py:45-45
  End this invocation with {'api_key': token} if token else {}.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/tls.py:48-50
// Source signature: is_anthropic_oauth_token(token: str | None) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn is_anthropic_oauth_token(token) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/tls.py:49-49
  In source order: Retain source documentation literal source_literal_49_4; it is not a model call.
  // Source: vvaharness/backends/llm/tls.py:50-50
  End this invocation with (token or '').strip().startswith(_OAUTH_TOKEN_PREFIX).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/tls.py:53-64
// Source signature: coerce_verify(value)
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn coerce_verify(value) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/tls.py:54-54
  In source order: Retain source documentation literal source_literal_54_4; it is not a model call.
  // Source: vvaharness/backends/llm/tls.py:56-57
  if (the source predicate value is None or isinstance(value, bool) is truthy) {
    // Source: vvaharness/backends/llm/tls.py:57-57
    End this invocation with value.
  }
  // Source: vvaharness/backends/llm/tls.py:58-63
  if (the source predicate isinstance(value, str) is truthy) {
    // Source: vvaharness/backends/llm/tls.py:59-59
    In source order: Evaluate once value.strip().lower(); assign in source target order to low.
    // Source: vvaharness/backends/llm/tls.py:60-61
    if (the source predicate low in _FALSE is truthy) {
      // Source: vvaharness/backends/llm/tls.py:61-61
      End this invocation with False.
    }
    // Source: vvaharness/backends/llm/tls.py:62-63
    if (the source predicate low in _TRUE is truthy) {
      // Source: vvaharness/backends/llm/tls.py:63-63
      End this invocation with True.
    }
  }
  // Source: vvaharness/backends/llm/tls.py:64-64
  End this invocation with value.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/tls.py:67-70
// Source signature: chain_paths(cert: str | tuple[str, ...] | list[str]) -> tuple[str, ...]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn chain_paths(cert) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/tls.py:68-68
  In source order: Retain source documentation literal source_literal_68_4; it is not a model call.
  // Source: vvaharness/backends/llm/tls.py:70-70
  End this invocation with tuple(cert) if isinstance(cert, (tuple, list)) else (cert,).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/tls.py:73-86
// Source signature: resolve_client_chain(cert: str | tuple[str, ...] | list[str] | None, *, label: str, noun: str='client_cert') -> str | tuple[str, ...] | list[str] | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn resolve_client_chain(cert, label, noun) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/tls.py:77-77
  In source order: Retain source documentation literal source_literal_77_4; it is not a model call.
  // Source: vvaharness/backends/llm/tls.py:79-80
  if (the source predicate not cert is truthy) {
    // Source: vvaharness/backends/llm/tls.py:80-80
    End this invocation with None.
  }
  // Source: vvaharness/backends/llm/tls.py:81-82
  In source order: Evaluate once chain_paths(cert); assign in source target order to paths. Then Evaluate once next((p for p in paths if p and (not os.path.exists(p))), None); assign in source target order to missing.
  // Source: vvaharness/backends/llm/tls.py:83-85
  if (the source predicate missing is not None is truthy) {
    // Source: vvaharness/backends/llm/tls.py:84-84
    In source order: Evaluate log.warning(Event.TLS_CLIENT_CHAIN_MISSING, route=label, kind=noun, path=missing); retain side effects and discard the expression result.
    // Source: vvaharness/backends/llm/tls.py:85-85
    End this invocation with None.
  }
  // Source: vvaharness/backends/llm/tls.py:86-86
  End this invocation with cert.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/tls.py:89-101
// Source signature: load_client_chain(context: ssl.SSLContext, cert: str | tuple[str, ...] | list[str], *, label: str) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn load_client_chain(context, cert, label) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/tls.py:92-94
  In source order: Retain source documentation literal source_literal_92_4; it is not a model call. Then Evaluate once chain_paths(cert); assign in source target order to args.
  // Source: vvaharness/backends/llm/tls.py:95-100
  Perform the following protected operations {
    // Source: vvaharness/backends/llm/tls.py:96-96
    In source order: Evaluate context.load_cert_chain(*args); retain side effects and discard the expression result.
  }
  // Source: vvaharness/backends/llm/tls.py:97-100
  On the first matching source exception Exception as exc, in handler order {
    // Source: vvaharness/backends/llm/tls.py:98-99
    In source order: Evaluate log.warning(Event.TLS_CLIENT_CHAIN_UNLOADABLE, route=label, path=args[0], error=type(exc).__name__); retain side effects and discard the expression result.
    // Source: vvaharness/backends/llm/tls.py:100-100
    End this invocation with False.
  }
  // Source: vvaharness/backends/llm/tls.py:101-101
  End this invocation with True.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/tls.py:104-110
// Source signature: warn_verify_disabled(base: str | None, *, label: str, default_endpoint: str='<default endpoint>', ca_hint: str='ca_cert') -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn warn_verify_disabled(base, label, default_endpoint, ca_hint) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/tls.py:107-110
  In source order: Retain source documentation literal source_literal_107_4; it is not a model call. Then Evaluate log.warning(Event.TLS_VERIFY_DISABLED, route=label, base_url=base or default_endpoint, ca_hint=ca_hint); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/tls.py:113-118
// Source signature: _restore_env_value(key: str, value: str | None) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _restore_env_value(key, value) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/tls.py:114-114
  In source order: Retain source documentation literal source_literal_114_4; it is not a model call.
  // Source: vvaharness/backends/llm/tls.py:115-118
  if (the source predicate value is None is truthy) {
    // Source: vvaharness/backends/llm/tls.py:116-116
    In source order: Evaluate os.environ.pop(key, None); retain side effects and discard the expression result.
  }
  else {
    // Source: vvaharness/backends/llm/tls.py:118-118
    In source order: Evaluate once value; assign in source target order to os.environ[key].
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/tls.py:122-133
// Source: vvaharness/backends/llm/tls.py:121-121
Before creating this callable, evaluate and retain decorators top-to-bottom: contextmanager.
// Source: vvaharness/backends/llm/tls.py:122-133
// Source signature: scoped_no_proxy_env(no_proxy: str | None) -> Iterator[None]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn scoped_no_proxy_env(no_proxy) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/tls.py:123-123
  In source order: Retain source documentation literal source_literal_123_4; it is not a model call.
  // Source: vvaharness/backends/llm/tls.py:124-126
  if (the source predicate not no_proxy is truthy) {
    // Source: vvaharness/backends/llm/tls.py:125-125
    In source order: Yield None; suspend this generator until resumed.
    // Source: vvaharness/backends/llm/tls.py:126-126
    End this invocation with None.
  }
  // Source: vvaharness/backends/llm/tls.py:127-127
  In source order: Evaluate once {key: os.environ.get(key) for key in _NO_PROXY_KEYS}; assign in source target order to prior.
  // Source: vvaharness/backends/llm/tls.py:128-133
  Perform the following protected operations {
    // Source: vvaharness/backends/llm/tls.py:129-130
    In source order: Evaluate os.environ.update(dict.fromkeys(_NO_PROXY_KEYS, no_proxy)); retain side effects and discard the expression result. Then Yield None; suspend this generator until resumed.
  }
  On every exit from this protected/handler/normal-completion region {
    // Source: vvaharness/backends/llm/tls.py:132-133
    for each (key, value) in prior.items() {
      // Source: vvaharness/backends/llm/tls.py:133-133
      In source order: Evaluate _restore_env_value(key, value); retain side effects and discard the expression result.
    }
  }
  If execution reaches this end, finish with the source implicit None result.
}
At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
```

## Local import links

- `from vvaharness.util import logs` at source line 25: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import logs` at source line 25: `source_detail/vvaharness/util/logs.py.sudo.md`.
- `from vvaharness.util.events import Event` at source line 26: `source_detail/vvaharness/util/events.py.sudo.md`.
