# vvaharness/config/constants.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/config/constants.py.evidence.json`. SHA-256: `4e760c79bea695ce62f832ed05dd2ef6c791ee1d9cf2639e5c5c503d9748b0b6`.

```sudo
// Source: vvaharness/config/constants.py:15-23
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from typing import Final; preserve alias and import-time effects. Then For LOCAL_OVERLAY_NAME, assign 'config.local.yaml'; source annotation Final[str]. Then For NO_LOCAL_CONFIG_ENV, assign 'VVAHARNESS_NO_LOCAL_CONFIG'; source annotation Final[str].
// Source: vvaharness/config/constants.py:26-73
In source order: For SECRET_NAME_PATTERNS, assign frozenset({'API_KEY', 'APIKEY', 'TOKEN', 'SECRET', 'PASSWORD', 'PASSWD', 'CREDENTIAL', 'PRIVATE_KEY'}); source annotation Final[frozenset[str]]. Then For SECRET_SEGMENT_PATTERNS, assign frozenset({'AUTH'}); source annotation Final[frozenset[str]]. Then For CREDENTIAL_DESTINATIONS, assign frozenset({'sdk.api_key', 'openai.api_key', 'batch.git_token', 'output.ingest_token'}); source annotation Final[frozenset[str]]. Then For ENDPOINT_KEYS, assign frozenset({'sdk.base_url', 'openai.base_url', 'output.ingest_url', 'batch.git_base_url'}); source annotation Final[frozenset[str]]. Then For TLS_ROUTING_KEYS, assign frozenset({'verify_ssl', 'ca_cert', 'client_cert', 'no_proxy', 'cache_route'}); source annotation Final[frozenset[str]].
// Source: vvaharness/config/constants.py:76-81
// Source signature: is_secret_var_name(name: str) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn is_secret_var_name(name) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/config/constants.py:77-78
  In source order: Retain source documentation literal source_literal_77_4; it is not a model call. Then Evaluate once name.upper(); assign in source target order to upper.
  // Source: vvaharness/config/constants.py:79-80
  if (the source predicate any((pat in upper for pat in SECRET_NAME_PATTERNS)) is truthy) {
    // Source: vvaharness/config/constants.py:80-80
    End this invocation with True.
  }
  // Source: vvaharness/config/constants.py:81-81
  End this invocation with any((seg.endswith(pat) for seg in upper.split('_') for pat in SECRET_SEGMENT_PATTERNS)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/config/constants.py:84-93
In source order: Evaluate once ['CREDENTIAL_DESTINATIONS', 'ENDPOINT_KEYS', 'LOCAL_OVERLAY_NAME', 'NO_LOCAL_CONFIG_ENV', 'SECRET_NAME_PATTERNS', 'SECRET_SEGMENT_PATTERNS', 'TLS_ROUTING_KEYS', 'is_secret_var_name']; assign in source target order to __all__.
```

## Local import links

No statically resolved in-checkout import; external calls remain explicit dependency boundaries.
