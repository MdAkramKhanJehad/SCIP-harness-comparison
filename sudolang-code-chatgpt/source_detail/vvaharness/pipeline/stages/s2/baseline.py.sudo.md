# vvaharness/pipeline/stages/s2/baseline.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/pipeline/stages/s2/baseline.py.evidence.json`. SHA-256: `0cd48a453bc06a0a2eea7311f71787580e6aa637f45bde6e7a3b9cfce7d53275`.

```sudo
// Source: vvaharness/pipeline/stages/s2/baseline.py:16-22
In source order: Retain source documentation literal source_literal_16_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import re; preserve alias and import-time effects. Then Resolve source import from collections.abc import Collection; preserve alias and import-time effects. Then Resolve source import from vvaharness.models import Threat, ThreatModel; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s2/baseline.py:23-26
In source order: Resolve source import from vvaharness.rules.repo_kinds import BASELINES; preserve alias and import-time effects. Then Evaluate once re.compile('baseline:\\s*(BL-[A-Z]+-\\w+)'); assign in source target order to _BASELINE_EVIDENCE_RX.
// Source: vvaharness/pipeline/stages/s2/baseline.py:29-31
// Source signature: _required_baselines(kinds: set[str]) -> set[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _required_baselines(kinds) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s2/baseline.py:30-30
  In source order: Retain source documentation literal source_literal_30_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s2/baseline.py:31-31
  End this invocation with {bid for k in kinds for bid, _ in BASELINES.get(k, ())}.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s2/baseline.py:34-41
// Source signature: _baseline_audit(tm: ThreatModel, kinds: set[str]) -> set[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _baseline_audit(tm, kinds) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s2/baseline.py:35-40
  In source order: Retain source documentation literal source_literal_35_4; it is not a model call. Then Evaluate once _required_baselines(kinds); assign in source target order to required. Then Evaluate once {m.group(1) for t in tm.threats if (m := _BASELINE_EVIDENCE_RX.match(t.evidence or ''))}; assign in source target order to as_threat. Then Evaluate once {q.split(':', 1)[0].strip() for q in tm.open_questions if q.startswith('BL-')}; assign in source target order to as_question.
  // Source: vvaharness/pipeline/stages/s2/baseline.py:41-41
  End this invocation with required - as_threat - as_question.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s2/baseline.py:47-58
In source order: For _BASELINE_TEXT_BY_ID, assign {bid: text for _entries in BASELINES.values() for bid, text in _entries}; source annotation dict[str, str]. Then For _COVERED_BY_ALIAS, assign {'BL-IAC-TLS': ('BL-WEB-A02',)}; source annotation dict[str, tuple[str, ...]]. Then Evaluate once {'the', 'and', 'for', 'via', 'not', 'any', 'use', 'non', 'its', 'that', 'this', 'from', 'into', 'with', 'owasp', 'cwe'}; assign in source target order to _CATEGORY_STOPWORDS.
// Source: vvaharness/pipeline/stages/s2/baseline.py:61-68
// Source signature: _stem(word: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _stem(word) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s2/baseline.py:62-62
  In source order: Retain source documentation literal source_literal_62_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s2/baseline.py:63-64
  if (the source predicate len(word) < 6 is truthy) {
    // Source: vvaharness/pipeline/stages/s2/baseline.py:64-64
    End this invocation with word.
  }
  // Source: vvaharness/pipeline/stages/s2/baseline.py:65-67
  for each suffix in ('ed', 'es', 's') {
    // Source: vvaharness/pipeline/stages/s2/baseline.py:66-67
    if (the source predicate word.endswith(suffix) is truthy) {
      // Source: vvaharness/pipeline/stages/s2/baseline.py:67-67
      End this invocation with word[:-len(suffix)].
    }
  }
  // Source: vvaharness/pipeline/stages/s2/baseline.py:68-68
  End this invocation with word.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s2/baseline.py:71-76
// Source signature: _category_terms(bid: str) -> frozenset[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _category_terms(bid) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s2/baseline.py:72-74
  In source order: Retain source documentation literal source_literal_72_4; it is not a model call. Then Evaluate once _BASELINE_TEXT_BY_ID.get(bid, ''); assign in source target order to text. Then Evaluate once re.findall('[A-Za-z]+', text.lower()); assign in source target order to words.
  // Source: vvaharness/pipeline/stages/s2/baseline.py:75-76
  End this invocation with frozenset((_stem(w) for w in words if len(w) >= 3 and w not in _CATEGORY_STOPWORDS)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s2/baseline.py:80-80
In source order: Evaluate once 2; assign in source target order to _MIN_CATEGORY_TERM_MATCHES.
// Source: vvaharness/pipeline/stages/s2/baseline.py:83-100
// Source signature: _category_covered_elsewhere(bid: str, threats: list[Threat], disposed: Collection[str]=()) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _category_covered_elsewhere(bid, threats, disposed) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s2/baseline.py:85-87
  In source order: Retain source documentation literal source_literal_85_4; it is not a model call. Then Evaluate once _category_terms(bid); assign in source target order to own_terms. Then For alias_terms, assign frozenset(); source annotation frozenset[str].
  // Source: vvaharness/pipeline/stages/s2/baseline.py:88-90
  for each alias_bid in _COVERED_BY_ALIAS.get(bid, ()) {
    // Source: vvaharness/pipeline/stages/s2/baseline.py:89-90
    if (the source predicate alias_bid in disposed is truthy) {
      // Source: vvaharness/pipeline/stages/s2/baseline.py:90-90
      In source order: Apply source augmented assignment alias_terms |= _category_terms(alias_bid) with source evaluation/in-place semantics.
    }
  }
  // Source: vvaharness/pipeline/stages/s2/baseline.py:91-91
  In source order: Evaluate once own_terms | alias_terms; assign in source target order to terms.
  // Source: vvaharness/pipeline/stages/s2/baseline.py:92-93
  if (the source predicate len(terms) < _MIN_CATEGORY_TERM_MATCHES is truthy) {
    // Source: vvaharness/pipeline/stages/s2/baseline.py:93-93
    End this invocation with False.
  }
  // Source: vvaharness/pipeline/stages/s2/baseline.py:94-99
  for each t in threats {
    // Source: vvaharness/pipeline/stages/s2/baseline.py:95-96
    In source order: Evaluate once t.threat.lower(); assign in source target order to text. Then Evaluate once {term for term in terms if term in text}; assign in source target order to matched.
    // Source: vvaharness/pipeline/stages/s2/baseline.py:98-99
    if (the source predicate len(matched) >= _MIN_CATEGORY_TERM_MATCHES and matched & own_terms is truthy) {
      // Source: vvaharness/pipeline/stages/s2/baseline.py:99-99
      End this invocation with True.
    }
  }
  // Source: vvaharness/pipeline/stages/s2/baseline.py:100-100
  End this invocation with False.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.models import Threat, ThreatModel` at source line 22: `source_detail/vvaharness/models/__init__.py.sudo.md`.
- `from vvaharness.rules.repo_kinds import BASELINES` at source line 23: `source_detail/vvaharness/rules/repo_kinds.py.sudo.md`.
