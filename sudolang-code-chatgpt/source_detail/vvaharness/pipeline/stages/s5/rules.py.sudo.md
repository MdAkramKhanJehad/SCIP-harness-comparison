# vvaharness/pipeline/stages/s5/rules.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/pipeline/stages/s5/rules.py.evidence.json`. SHA-256: `03612fc11fd94178319dfb9f8235ea50e6ebff7a84ce400f2dfb32ff5e061467`.

```sudo
// Source: vvaharness/pipeline/stages/s5/rules.py:15-26
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import re; preserve alias and import-time effects. Then Resolve source import from vvaharness.models import Finding, VulnClass; preserve alias and import-time effects. Then Evaluate once re.compile(source_literal_23_4, re.IGNORECASE); assign in source target order to EXCLUDE_PATH_RE.
// Source: vvaharness/pipeline/stages/s5/rules.py:29-50
In source order: For HARDCODED_CWES, assign frozenset({'CWE-798', 'CWE-259', 'CWE-321', 'CWE-256'}); source annotation frozenset[str]. Then For CONTROL_ABSENCE_CWES, assign frozenset({'CWE-352', 'CWE-1004', 'CWE-614', 'CWE-307', 'CWE-778', 'CWE-311', 'CWE-312', 'CWE-532', 'CWE-209'}); source annotation frozenset[str]. Then Evaluate once re.compile(source_literal_39_4); assign in source target order to SECRET_TEXT_RX.
// Source: vvaharness/pipeline/stages/s5/rules.py:53-60
// Source signature: is_secret_class(f: Finding) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn is_secret_class(f) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s5/rules.py:54-54
  In source order: Retain source documentation literal source_literal_54_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s5/rules.py:55-56
  if (the source predicate f.vuln_class == VulnClass.INFO_LEAK is truthy) {
    // Source: vvaharness/pipeline/stages/s5/rules.py:56-56
    End this invocation with True.
  }
  // Source: vvaharness/pipeline/stages/s5/rules.py:57-58
  if (the source predicate f.cwe and (f.cwe in HARDCODED_CWES or f.cwe in CONTROL_ABSENCE_CWES) is truthy) {
    // Source: vvaharness/pipeline/stages/s5/rules.py:58-58
    End this invocation with True.
  }
  // Source: vvaharness/pipeline/stages/s5/rules.py:59-59
  In source order: Evaluate once ' '.join((s for s in (f.title, f.description, f.code_snippet) if s)); assign in source target order to haystack.
  // Source: vvaharness/pipeline/stages/s5/rules.py:60-60
  End this invocation with bool(SECRET_TEXT_RX.search(haystack)).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.models import Finding, VulnClass` at source line 20: `source_detail/vvaharness/models/__init__.py.sudo.md`.
