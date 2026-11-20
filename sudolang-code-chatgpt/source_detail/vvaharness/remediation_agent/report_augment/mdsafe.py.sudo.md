# vvaharness/remediation_agent/report_augment/mdsafe.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/remediation_agent/report_augment/mdsafe.py.evidence.json`. SHA-256: `32364c265603fb457e9356bd7d0e75109303737183828653f3abfdfe4ca15c50`.

```sudo
// Source: vvaharness/remediation_agent/report_augment/mdsafe.py:15-26
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from vvaharness.models import _MD_INVISIBLE_RX, _MD_LINEBREAK_RX; preserve alias and import-time effects. Then Evaluate once {'\\': '\\\\', '`': '\\`', '*': '\\*', '_': '\\_', '[': '\\[', ']': '\\]', '|': '\\|', '#': '\\#', '<': '&lt;', '>': '&gt;', '&': '&amp;'}; assign in source target order to _MD_ESCAPE.
// Source: vvaharness/remediation_agent/report_augment/mdsafe.py:29-33
// Source signature: _md_escape(value: object) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _md_escape(value) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/report_augment/mdsafe.py:30-32
  In source order: Retain source documentation literal source_literal_30_4; it is not a model call. Then Evaluate once _MD_LINEBREAK_RX.sub(' ', str(value)); assign in source target order to text. Then Evaluate once _MD_INVISIBLE_RX.sub('', text); assign in source target order to text.
  // Source: vvaharness/remediation_agent/report_augment/mdsafe.py:33-33
  End this invocation with ''.join((_MD_ESCAPE.get(ch, ch) for ch in text)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/report_augment/mdsafe.py:36-43
// Source signature: _md_code_span(value: object) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _md_code_span(value) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/report_augment/mdsafe.py:37-42
  In source order: Retain source documentation literal source_literal_37_4; it is not a model call. Then Evaluate once _MD_LINEBREAK_RX.sub(' ', str(value)); assign in source target order to text. Then Evaluate once _MD_INVISIBLE_RX.sub('', text); assign in source target order to text. Then Evaluate once text.replace('`', ''); assign in source target order to text. Then Evaluate once text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;'); assign in source target order to text.
  // Source: vvaharness/remediation_agent/report_augment/mdsafe.py:43-43
  End this invocation with source_template_43_11.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.models import _MD_INVISIBLE_RX, _MD_LINEBREAK_RX` at source line 19: `source_detail/vvaharness/models/__init__.py.sudo.md`.
