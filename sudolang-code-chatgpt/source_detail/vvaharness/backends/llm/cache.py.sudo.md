# vvaharness/backends/llm/cache.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/backends/llm/cache.py.evidence.json`. SHA-256: `b049c17db2964be53bcdeda1792602ab00bbc317e61293f7daaeacafc2142e38`.

```sudo
// Source: vvaharness/backends/llm/cache.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from collections.abc import Mapping; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.provider_routing import routes_to_anthropic; preserve alias and import-time effects. Then Resolve source import from vvaharness.report.redact import redact; preserve alias and import-time effects.
// Source: vvaharness/backends/llm/cache.py:22-32
In source order: Resolve source import from vvaharness.util import console; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.tokens import TOKENS, unparsed_cache_keys; preserve alias and import-time effects. Then Evaluate once 1.35; assign in source target order to CACHE_EST_MARGIN. Then Evaluate once ('off', 'false', 'no', '0', 'none'); assign in source target order to _DISABLED_SPELLINGS. Then Evaluate once 'breakpoint'; assign in source target order to PREFIX_CACHE_BREAKPOINT.
// Source: vvaharness/backends/llm/cache.py:33-34
In source order: Evaluate once 'implicit'; assign in source target order to PREFIX_CACHE_IMPLICIT. Then Evaluate once 'none'; assign in source target order to PREFIX_CACHE_NONE.
// Source: vvaharness/backends/llm/cache.py:37-48
// Source signature: prefix_cache_class(via: str, *, model_id: str='', provider: str | None=None) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn prefix_cache_class(via, model_id, provider) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cache.py:39-39
  In source order: Retain source documentation literal source_literal_39_4; it is not a model call.
  // Source: vvaharness/backends/llm/cache.py:40-41
  if (the source predicate via == 'sdk' is truthy) {
    // Source: vvaharness/backends/llm/cache.py:41-41
    End this invocation with PREFIX_CACHE_BREAKPOINT.
  }
  // Source: vvaharness/backends/llm/cache.py:42-43
  if (the source predicate via == 'openai' is truthy) {
    // Source: vvaharness/backends/llm/cache.py:43-43
    End this invocation with PREFIX_CACHE_IMPLICIT.
  }
  // Source: vvaharness/backends/llm/cache.py:44-47
  if (the source predicate via == 'deepagents' is truthy) {
    // Source: vvaharness/backends/llm/cache.py:45-46
    if (the source predicate routes_to_anthropic(model_id, provider) is truthy) {
      // Source: vvaharness/backends/llm/cache.py:46-46
      End this invocation with PREFIX_CACHE_BREAKPOINT.
    }
    // Source: vvaharness/backends/llm/cache.py:47-47
    End this invocation with PREFIX_CACHE_IMPLICIT.
  }
  // Source: vvaharness/backends/llm/cache.py:48-48
  End this invocation with PREFIX_CACHE_NONE.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cache.py:51-56
// Source signature: markers_enabled(cfg: Mapping) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn markers_enabled(cfg) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cache.py:52-53
  In source order: Retain source documentation literal source_literal_52_4; it is not a model call. Then Evaluate once cfg.get('cache_markers', 'on'); assign in source target order to v.
  // Source: vvaharness/backends/llm/cache.py:54-55
  if (the source predicate isinstance(v, bool) is truthy) {
    // Source: vvaharness/backends/llm/cache.py:55-55
    End this invocation with v.
  }
  // Source: vvaharness/backends/llm/cache.py:56-56
  End this invocation with str(v).strip().lower() not in _DISABLED_SPELLINGS.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cache.py:60-62
In source order: Evaluate once frozenset({'cache_creation_input_tokens', 'cache_read_input_tokens', 'cache_creation'}); assign in source target order to ANTHROPIC_PARSED_CACHE_KEYS.
// Source: vvaharness/backends/llm/cache.py:65-67
// Source signature: note_unparsed_cache_keys(usage: dict | None, *, via: str) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn note_unparsed_cache_keys(usage, via) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cache.py:66-67
  In source order: Retain source documentation literal source_literal_66_4; it is not a model call. Then Evaluate report_unparsed_cache_keys(usage, ANTHROPIC_PARSED_CACHE_KEYS, via=via, label=via); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cache.py:70-81
// Source signature: report_unparsed_cache_keys(usage: dict | None, parsed, *, via: str, label: str) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn report_unparsed_cache_keys(usage, parsed, via, label) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cache.py:72-76
  In source order: Retain source documentation literal source_literal_72_4; it is not a model call. Then Evaluate once unparsed_cache_keys(usage, parsed); assign in source target order to keys. Then Evaluate once getattr(TOKENS, 'note_cache_unparsed', None); assign in source target order to note.
  // Source: vvaharness/backends/llm/cache.py:77-81
  if (the source predicate note is not None and note(keys, via=via) is truthy) {
    // Source: vvaharness/backends/llm/cache.py:78-81
    In source order: Evaluate console.write(source_template_78_22); retain side effects and discard the expression result.
  }
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.backends.harness.provider_routing import routes_to_anthropic` at source line 20: `source_detail/vvaharness/backends/harness/provider_routing.py.sudo.md`.
- `from vvaharness.report.redact import redact` at source line 21: `source_detail/vvaharness/report/redact.py.sudo.md`.
- `from vvaharness.util import console` at source line 22: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import console` at source line 22: `source_detail/vvaharness/util/console.py.sudo.md`.
- `from vvaharness.util.tokens import TOKENS, unparsed_cache_keys` at source line 23: `source_detail/vvaharness/util/tokens.py.sudo.md`.
