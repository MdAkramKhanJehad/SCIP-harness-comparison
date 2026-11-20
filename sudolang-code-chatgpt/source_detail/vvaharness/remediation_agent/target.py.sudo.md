# vvaharness/remediation_agent/target.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/remediation_agent/target.py.evidence.json`. SHA-256: `685ea6a0af3090ed9f8865ba9a6962cfcffe77c2da43ba013b0f93a82d3757a6`.

```sudo
// Source: vvaharness/remediation_agent/target.py:15-20
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import hashlib; preserve alias and import-time effects. Then Resolve source import import re; preserve alias and import-time effects. Then Resolve source import from dataclasses import dataclass; preserve alias and import-time effects.
// Source: vvaharness/remediation_agent/target.py:22-24
In source order: Resolve source import from vvaharness.models import Finding; preserve alias and import-time effects. Then Evaluate once ['RemediationTarget']; assign in source target order to __all__.
// Source: vvaharness/remediation_agent/target.py:28-66
// Source: vvaharness/remediation_agent/target.py:27-27
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass.
// Source: vvaharness/remediation_agent/target.py:28-66
interface RemediationTarget {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/remediation_agent/target.py:29-33
  In source order: Retain source documentation literal source_literal_29_4; it is not a model call. Then For finding, declare without assigning a value; source annotation Finding. Then For index, declare without assigning a value; source annotation int. Then For done, assign False; source annotation bool.
  // Source: vvaharness/remediation_agent/target.py:36-38
  // Source: vvaharness/remediation_agent/target.py:35-35
  Before creating this callable, evaluate and retain decorators top-to-bottom: property.
  // Source: vvaharness/remediation_agent/target.py:36-38
  // Source signature: case_id(self) -> str
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn case_id(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/remediation_agent/target.py:37-37
    In source order: Retain source documentation literal source_literal_37_8; it is not a model call.
    // Source: vvaharness/remediation_agent/target.py:38-38
    End this invocation with self.finding.case_id or _derive_case_id(self.finding).
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vvaharness/remediation_agent/target.py:41-43
  // Source: vvaharness/remediation_agent/target.py:40-40
  Before creating this callable, evaluate and retain decorators top-to-bottom: property.
  // Source: vvaharness/remediation_agent/target.py:41-43
  // Source signature: severity(self) -> str
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn severity(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/remediation_agent/target.py:42-42
    In source order: Retain source documentation literal source_literal_42_8; it is not a model call.
    // Source: vvaharness/remediation_agent/target.py:43-43
    End this invocation with self.finding.severity.value.upper().
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vvaharness/remediation_agent/target.py:46-48
  // Source: vvaharness/remediation_agent/target.py:45-45
  Before creating this callable, evaluate and retain decorators top-to-bottom: property.
  // Source: vvaharness/remediation_agent/target.py:46-48
  // Source signature: title(self) -> str
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn title(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/remediation_agent/target.py:47-47
    In source order: Retain source documentation literal source_literal_47_8; it is not a model call.
    // Source: vvaharness/remediation_agent/target.py:48-48
    End this invocation with self.finding.title.
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vvaharness/remediation_agent/target.py:51-53
  // Source: vvaharness/remediation_agent/target.py:50-50
  Before creating this callable, evaluate and retain decorators top-to-bottom: property.
  // Source: vvaharness/remediation_agent/target.py:51-53
  // Source signature: file(self) -> str
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn file(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/remediation_agent/target.py:52-52
    In source order: Retain source documentation literal source_literal_52_8; it is not a model call.
    // Source: vvaharness/remediation_agent/target.py:53-53
    End this invocation with self.finding.file.
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vvaharness/remediation_agent/target.py:56-59
  // Source: vvaharness/remediation_agent/target.py:55-55
  Before creating this callable, evaluate and retain decorators top-to-bottom: property.
  // Source: vvaharness/remediation_agent/target.py:56-59
  // Source signature: label(self) -> str
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn label(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/remediation_agent/target.py:57-58
    In source order: Retain source documentation literal source_literal_57_8; it is not a model call. Then Evaluate once source_template_58_14 if self.finding.file else ''; assign in source target order to loc.
    // Source: vvaharness/remediation_agent/target.py:59-59
    End this invocation with source_template_59_15.
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vvaharness/remediation_agent/target.py:62-66
  // Source: vvaharness/remediation_agent/target.py:61-61
  Before creating this callable, evaluate and retain decorators top-to-bottom: property.
  // Source: vvaharness/remediation_agent/target.py:62-66
  // Source signature: slug(self) -> str
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn slug(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/remediation_agent/target.py:63-65
    In source order: Retain source documentation literal source_literal_63_8; it is not a model call. Then Evaluate once re.sub('[^a-z0-9]+', '-', self.finding.title.lower()).strip('-'); assign in source target order to base. Then Evaluate once base[:60].rstrip('-') or 'finding'; assign in source target order to base.
    // Source: vvaharness/remediation_agent/target.py:66-66
    End this invocation with source_template_66_15.
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vvaharness/remediation_agent/target.py:69-73
// Source signature: _derive_case_id(finding: Finding) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _derive_case_id(finding) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/target.py:70-72
  In source order: Retain source documentation literal source_literal_70_4; it is not a model call. Then Evaluate once source_template_71_11.encode(); assign in source target order to seed. Then Evaluate once hashlib.sha1(seed).hexdigest()[:6]; assign in source target order to digest.
  // Source: vvaharness/remediation_agent/target.py:73-73
  End this invocation with source_template_73_11.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.models import Finding` at source line 22: `source_detail/vvaharness/models/__init__.py.sudo.md`.
