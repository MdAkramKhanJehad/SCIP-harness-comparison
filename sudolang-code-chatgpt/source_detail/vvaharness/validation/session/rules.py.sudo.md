# vvaharness/validation/session/rules.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/validation/session/rules.py.evidence.json`. SHA-256: `0dd9e1def3b6c181ce9194765f088e0068adf7fbbe3cd11d37991afc06c32fa9`.

```sudo
// Source: vvaharness/validation/session/rules.py:15-26
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import re; preserve alias and import-time effects. Then Evaluate once re.compile('\\A\\s*<!--.*?-->\\s*', re.DOTALL); assign in source target order to _LICENCE_COMMENT. Then Evaluate once 'scoring-matrix.md'; assign in source target order to SCORING_RULES.
// Source: vvaharness/validation/session/rules.py:27-27
In source order: Evaluate once 'adversarial-review.md'; assign in source target order to ADVERSARIAL_RULES.
// Source: vvaharness/validation/session/rules.py:30-38
// Source signature: _rules_text(filename: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _rules_text(filename) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/session/rules.py:31-35
  In source order: Retain source documentation literal source_literal_31_4; it is not a model call. Then Resolve source import from vvaharness.validation.session import config_inject; preserve alias and import-time effects. Then Evaluate once config_inject.CLAUDE_CONFIG_SOURCE / 'rules' / filename; assign in source target order to path.
  // Source: vvaharness/validation/session/rules.py:36-37
  if (the source predicate not path.is_file() is truthy) {
    // Source: vvaharness/validation/session/rules.py:37-37
    Raise FileNotFoundError(source_template_37_32).
  }
  // Source: vvaharness/validation/session/rules.py:38-38
  End this invocation with _LICENCE_COMMENT.sub('', path.read_text(encoding='utf-8')).strip().
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/session/rules.py:41-43
// Source signature: orchestrator_rules_text() -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn orchestrator_rules_text() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/session/rules.py:42-42
  In source order: Retain source documentation literal source_literal_42_4; it is not a model call.
  // Source: vvaharness/validation/session/rules.py:43-43
  End this invocation with source_template_43_11.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/session/rules.py:46-48
// Source signature: persona_rules_text() -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn persona_rules_text() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/session/rules.py:47-47
  In source order: Retain source documentation literal source_literal_47_4; it is not a model call.
  // Source: vvaharness/validation/session/rules.py:48-48
  End this invocation with _rules_text(ADVERSARIAL_RULES).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/session/rules.py:51-56
In source order: Evaluate once ['ADVERSARIAL_RULES', 'SCORING_RULES', 'orchestrator_rules_text', 'persona_rules_text']; assign in source target order to __all__.
```

## Local import links

- `from vvaharness.validation.session import config_inject` at source line 33: `source_detail/vvaharness/validation/session/__init__.py.sudo.md`.
- `from vvaharness.validation.session import config_inject` at source line 33: `source_detail/vvaharness/validation/session/config_inject.py.sudo.md`.
