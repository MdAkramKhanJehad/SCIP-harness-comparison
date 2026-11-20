# vvaharness/util/net.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/util/net.py.evidence.json`. SHA-256: `343e1f63ef4d290c1f387348dc7a5d581456926d11f25019bc9189f40e433755`.

```sudo
// Source: vvaharness/util/net.py:15-22
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import ipaddress; preserve alias and import-time effects. Then Evaluate once {'localhost', 'localhost.'}; assign in source target order to _LOCAL_NAMES.
// Source: vvaharness/util/net.py:25-30
// Source signature: ip_literal(host: str)
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn ip_literal(host) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/net.py:26-26
  In source order: Retain source documentation literal source_literal_26_4; it is not a model call.
  // Source: vvaharness/util/net.py:27-30
  Perform the following protected operations {
    // Source: vvaharness/util/net.py:28-28
    End this invocation with ipaddress.ip_address(host.strip().strip('[]')).
  }
  // Source: vvaharness/util/net.py:29-30
  On the first matching source exception ValueError, in handler order {
    // Source: vvaharness/util/net.py:30-30
    End this invocation with None.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/net.py:33-41
// Source signature: is_loopback_host(host: str) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn is_loopback_host(host) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/net.py:34-34
  In source order: Retain source documentation literal source_literal_34_4; it is not a model call.
  // Source: vvaharness/util/net.py:35-36
  if (the source predicate not host is truthy) {
    // Source: vvaharness/util/net.py:36-36
    End this invocation with False.
  }
  // Source: vvaharness/util/net.py:37-37
  In source order: Evaluate once host.strip().strip('[]'); assign in source target order to h.
  // Source: vvaharness/util/net.py:38-39
  if (the source predicate h.lower() in _LOCAL_NAMES is truthy) {
    // Source: vvaharness/util/net.py:39-39
    End this invocation with True.
  }
  // Source: vvaharness/util/net.py:40-40
  In source order: Evaluate once ip_literal(h); assign in source target order to ip.
  // Source: vvaharness/util/net.py:41-41
  End this invocation with bool(ip and ip.is_loopback).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

No statically resolved in-checkout import; external calls remain explicit dependency boundaries.
