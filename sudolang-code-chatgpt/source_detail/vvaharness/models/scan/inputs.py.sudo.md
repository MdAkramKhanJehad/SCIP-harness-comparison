# vvaharness/models/scan/inputs.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/models/scan/inputs.py.evidence.json`. SHA-256: `b3278eabaf6e6cdcf00492214df6dddc2e13f9f5885d09b3e72ce0a6efa516a2`.

```sudo
// Source: vvaharness/models/scan/inputs.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import logging; preserve alias and import-time effects. Then Resolve source import from typing import Literal; preserve alias and import-time effects. Then Resolve source import from pydantic import BaseModel, field_validator; preserve alias and import-time effects.
// Source: vvaharness/models/scan/inputs.py:23-25
In source order: Resolve source import from vvaharness.models.scan._coerce import _coerce_enum; preserve alias and import-time effects. Then Evaluate once logging.getLogger(__name__); assign in source target order to log.
// Source: vvaharness/models/scan/inputs.py:31-36
interface CVE {
  Describe the source Python type, preserving its base/metaclass expression order: BaseModel.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/models/scan/inputs.py:32-36
  In source order: For id, declare without assigning a value; source annotation str. Then For summary, declare without assigning a value; source annotation str. Then For affected_files, assign []; source annotation list[str]. Then For cvss, assign None; source annotation float | None. Then For patched, assign False; source annotation bool.
}
// Source: vvaharness/models/scan/inputs.py:39-48
In source order: Evaluate once {'auth', 'sandbox', 'input-validation', 'aslr', 'cfi', 'other'}; assign in source target order to _CONTROL_KINDS. Then Evaluate once {'authn': 'auth', 'authentication': 'auth', 'authz': 'auth', 'authorization': 'auth', 'rbac': 'auth', 'iam': 'auth', 'sso': 'auth', 'waf': 'input-validation', 'validation': 'input-validation', 'input_validation': 'input-validation', 'sanitization': 'input-validation', 'sanitisation': 'input-validation', 'encoding': 'input-validation', 'seccomp': 'sandbox', 'container': 'sandbox', 'isolation': 'sandbox', 'chroot': 'sandbox', 'jail': 'sandbox'}; assign in source target order to _CONTROL_KIND_ALIAS.
// Source: vvaharness/models/scan/inputs.py:51-61
interface Control {
  Describe the source Python type, preserving its base/metaclass expression order: BaseModel.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/models/scan/inputs.py:52-56
  In source order: Retain source documentation literal source_literal_52_4; it is not a model call. Then For name, declare without assigning a value; source annotation str. Then For kind, declare without assigning a value; source annotation Literal['auth', 'sandbox', 'input-validation', 'aslr', 'cfi', 'other']. Then For protects, assign []; source annotation list[str]. Then For notes, assign ''; source annotation str.
  // Source: vvaharness/models/scan/inputs.py:60-61
  // Source: vvaharness/models/scan/inputs.py:58-59
  Before creating this callable, evaluate and retain decorators top-to-bottom: field_validator('kind', mode='before'), classmethod.
  // Source: vvaharness/models/scan/inputs.py:60-61
  // Source signature: _v_kind(cls, v)
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _v_kind(cls, v) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/models/scan/inputs.py:61-61
    End this invocation with _coerce_enum(v, _CONTROL_KINDS, _CONTROL_KIND_ALIAS, 'other').
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
}
// Source: vvaharness/models/scan/inputs.py:64-86
interface AppProfile {
  Describe the source Python type, preserving its base/metaclass expression order: BaseModel.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/models/scan/inputs.py:65-69
  In source order: Retain source documentation literal source_literal_65_4; it is not a model call. Then For application_id, declare without assigning a value; source annotation str. Then For name, assign ''; source annotation str. Then For externally_facing, assign False; source annotation bool. Then For pci_scoped, assign False; source annotation bool.
  // Source: vvaharness/models/scan/inputs.py:70-72
  In source order: For processes_pan, assign False; source annotation bool. Then For pii, assign False; source annotation bool. Then For source, assign ''; source annotation str.
  // Source: vvaharness/models/scan/inputs.py:74-86
  // Source signature: to_prompt_block(self) -> str
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn to_prompt_block(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/models/scan/inputs.py:75-75
    In source order: Evaluate once []; assign in source target order to sens.
    // Source: vvaharness/models/scan/inputs.py:76-76
    if (the source predicate self.pci_scoped is truthy) {
      // Source: vvaharness/models/scan/inputs.py:76-76
      In source order: Evaluate sens.append('PCI-scoped'); retain side effects and discard the expression result.
    }
    // Source: vvaharness/models/scan/inputs.py:77-77
    if (the source predicate self.processes_pan is truthy) {
      // Source: vvaharness/models/scan/inputs.py:77-77
      In source order: Evaluate sens.append('processes PAN'); retain side effects and discard the expression result.
    }
    // Source: vvaharness/models/scan/inputs.py:78-78
    if (the source predicate self.pii is truthy) {
      // Source: vvaharness/models/scan/inputs.py:78-78
      In source order: Evaluate sens.append('handles PII'); retain side effects and discard the expression result.
    }
    // Source: vvaharness/models/scan/inputs.py:79-86
    End this invocation with source_template_80_12.
    If execution reaches this end, finish with the source implicit None result.
  }
}
```

## Local import links

- `from vvaharness.models.scan._coerce import _coerce_enum` at source line 23: `source_detail/vvaharness/models/scan/_coerce.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../prompt_representation/vvaharness/models/scan/inputs.py.sudo.md). Exact strings in the evidence asset support this conversion.
