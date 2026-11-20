# vvaharness/rules/cwe.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/rules/cwe.py.evidence.json`. SHA-256: `407dd698177f22877ede1dd9e6f2d9da38fbf7a702de021f73399f58511b2b7b`.

```sudo
// Source: vvaharness/rules/cwe.py:15-34
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import re; preserve alias and import-time effects. Then For OWASP_2025_BY_SEMANTIC, assign {'html-response': ('A03:2025-Injection',), 'command-exec': ('A03:2025-Injection',), 'sql-exec': ('A03:2025-Injection',), 'url-fetch': ('A10:2025-SSRF', 'A03:2025-Injection'), 'file-io': ('A01:2025-Broken-Access-Control', 'A03:2025-Injection'), 'deserialization': ('A08:2025-Software-and-Data-Integrity-Failures',), 'template-render': ('A03:2025-Injection',), 'credentials': ('A02:2025-Cryptographic-Failures',)}; source annotation dict[str, tuple[str, ...]]. Then Evaluate once re.compile('CWE[-_ ]?0*(\\d{1,4})', re.IGNORECASE); assign in source target order to _CWE_RE.
// Source: vvaharness/rules/cwe.py:37-40
// Source signature: norm_cwe(value: object) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn norm_cwe(value) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/rules/cwe.py:38-39
  In source order: Retain source documentation literal source_literal_38_4; it is not a model call. Then Evaluate once _CWE_RE.search(str(value or '')); assign in source target order to match.
  // Source: vvaharness/rules/cwe.py:40-40
  End this invocation with source_template_40_11 if match else None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/rules/cwe.py:44-60
In source order: For _WEAKNESS_CLUSTERS, assign (('CWE-89', 'CWE-943', 'CWE-564'), ('CWE-78', 'CWE-77'), ('CWE-22', 'CWE-23', 'CWE-36'), ('CWE-79', 'CWE-80'), ('CWE-862', 'CWE-285', 'CWE-284')); source annotation tuple[tuple[str, ...], ...]. Then For _WEAKNESS_KEY, assign {c: cluster[0] for cluster in _WEAKNESS_CLUSTERS for c in cluster}; source annotation dict[str, str]. Then For _GENERIC_PARENT_CWES, assign frozenset({'CWE-20', 'CWE-74'}); source annotation frozenset[str].
// Source: vvaharness/rules/cwe.py:63-66
// Source signature: weakness_key(value: object) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn weakness_key(value) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/rules/cwe.py:64-65
  In source order: Retain source documentation literal source_literal_64_4; it is not a model call. Then Evaluate once norm_cwe(value); assign in source target order to cwe.
  // Source: vvaharness/rules/cwe.py:66-66
  End this invocation with _WEAKNESS_KEY.get(cwe, cwe) if cwe else None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/rules/cwe.py:69-84
// Source signature: same_weakness(cwe_a: object, cwe_b: object) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn same_weakness(cwe_a, cwe_b) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/rules/cwe.py:70-73
  In source order: Retain source documentation literal source_literal_70_4; it is not a model call. Then Evaluate once norm_cwe(cwe_a); assign in source target order to a. Then Evaluate once norm_cwe(cwe_b); assign in source target order to b.
  // Source: vvaharness/rules/cwe.py:74-75
  if (the source predicate not a or not b is truthy) {
    // Source: vvaharness/rules/cwe.py:75-75
    End this invocation with False.
  }
  // Source: vvaharness/rules/cwe.py:76-77
  if (the source predicate a == b is truthy) {
    // Source: vvaharness/rules/cwe.py:77-77
    End this invocation with True.
  }
  // Source: vvaharness/rules/cwe.py:78-79
  In source order: Evaluate once a in _GENERIC_PARENT_CWES; assign in source target order to a_generic. Then Evaluate once b in _GENERIC_PARENT_CWES; assign in source target order to b_generic.
  // Source: vvaharness/rules/cwe.py:80-81
  if (the source predicate a_generic != b_generic is truthy) {
    // Source: vvaharness/rules/cwe.py:81-81
    End this invocation with True.
  }
  // Source: vvaharness/rules/cwe.py:82-83
  if (the source predicate a_generic and b_generic is truthy) {
    // Source: vvaharness/rules/cwe.py:83-83
    End this invocation with False.
  }
  // Source: vvaharness/rules/cwe.py:84-84
  End this invocation with weakness_key(a) == weakness_key(b).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/rules/cwe.py:87-92
In source order: Evaluate once ['OWASP_2025_BY_SEMANTIC', 'norm_cwe', 'same_weakness', 'weakness_key']; assign in source target order to __all__.
```

## Local import links

No statically resolved in-checkout import; external calls remain explicit dependency boundaries.
