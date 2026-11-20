# vvaharness/remediation_agent/report_parser/finding.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/remediation_agent/report_parser/finding.py.evidence.json`. SHA-256: `e7511000c3a7ef46488c51db4243f6584d83b29787406137dac3a4f42ca39dee`.

```sudo
// Source: vvaharness/remediation_agent/report_parser/finding.py:15-19
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import re; preserve alias and import-time effects. Then Resolve source import from dataclasses import dataclass; preserve alias and import-time effects.
// Source: vvaharness/remediation_agent/report_parser/finding.py:23-43
// Source: vvaharness/remediation_agent/report_parser/finding.py:22-22
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass.
// Source: vvaharness/remediation_agent/report_parser/finding.py:23-43
interface Finding {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/remediation_agent/report_parser/finding.py:24-29
  In source order: Retain source documentation literal source_literal_24_4; it is not a model call. Then For index, declare without assigning a value; source annotation int. Then For severity, declare without assigning a value; source annotation str. Then For title, declare without assigning a value; source annotation str. Then For file, assign None; source annotation str | None.
  // Source: vvaharness/remediation_agent/report_parser/finding.py:30-31
  In source order: For body, assign ''; source annotation str. Then For done, assign False; source annotation bool.
  // Source: vvaharness/remediation_agent/report_parser/finding.py:34-36
  // Source: vvaharness/remediation_agent/report_parser/finding.py:33-33
  Before creating this callable, evaluate and retain decorators top-to-bottom: property.
  // Source: vvaharness/remediation_agent/report_parser/finding.py:34-36
  // Source signature: label(self) -> str
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn label(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/remediation_agent/report_parser/finding.py:35-35
    In source order: Evaluate once source_template_35_14 if self.file else ''; assign in source target order to loc.
    // Source: vvaharness/remediation_agent/report_parser/finding.py:36-36
    End this invocation with source_template_36_15.
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vvaharness/remediation_agent/report_parser/finding.py:39-43
  // Source: vvaharness/remediation_agent/report_parser/finding.py:38-38
  Before creating this callable, evaluate and retain decorators top-to-bottom: property.
  // Source: vvaharness/remediation_agent/report_parser/finding.py:39-43
  // Source signature: slug(self) -> str
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn slug(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/remediation_agent/report_parser/finding.py:40-42
    In source order: Retain source documentation literal source_literal_40_8; it is not a model call. Then Evaluate once re.sub('[^a-z0-9]+', '-', self.title.lower()).strip('-'); assign in source target order to base. Then Evaluate once base[:60].rstrip('-') or 'finding'; assign in source target order to base.
    // Source: vvaharness/remediation_agent/report_parser/finding.py:43-43
    End this invocation with source_template_43_15.
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
```

## Local import links

No statically resolved in-checkout import; external calls remain explicit dependency boundaries.
