# vvaharness/remediation_agent/models/fixer.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/remediation_agent/models/fixer.py.evidence.json`. SHA-256: `fb7b69a23240f9f91d36c40c08748c5bf8fcd81da1010ed9f2f9526ef2efc605`.

```sudo
// Source: vvaharness/remediation_agent/models/fixer.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import json; preserve alias and import-time effects. Then Resolve source import from typing import Literal; preserve alias and import-time effects. Then Resolve source import from pydantic import BaseModel, Field, model_validator; preserve alias and import-time effects.
// Source: vvaharness/remediation_agent/models/fixer.py:23-23
In source order: Evaluate once Literal['applied', 'already_applied', 'not_applied', 'tool_error']; assign in source target order to FixerStatus.
// Source: vvaharness/remediation_agent/models/fixer.py:26-51
interface FixerResult {
  Describe the source Python type, preserving its base/metaclass expression order: BaseModel.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/remediation_agent/models/fixer.py:27-32
  In source order: Retain source documentation literal source_literal_27_4; it is not a model call. Then For status, declare without assigning a value; source annotation FixerStatus. Then For files_changed, assign Field(default_factory=list); source annotation list[str]. Then For summary, declare without assigning a value; source annotation str. Then For error, assign ''; source annotation str.
  // Source: vvaharness/remediation_agent/models/fixer.py:33-33
  In source order: For retryable, assign False; source annotation bool.
  // Source: vvaharness/remediation_agent/models/fixer.py:36-46
  // Source: vvaharness/remediation_agent/models/fixer.py:35-35
  Before creating this callable, evaluate and retain decorators top-to-bottom: model_validator(mode='after').
  // Source: vvaharness/remediation_agent/models/fixer.py:36-46
  // Source signature: _status_has_evidence(self) -> FixerResult
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _status_has_evidence(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/remediation_agent/models/fixer.py:37-37
    In source order: Retain source documentation literal source_literal_37_8; it is not a model call.
    // Source: vvaharness/remediation_agent/models/fixer.py:38-39
    if (the source predicate self.status == 'applied' and (not self.files_changed) is truthy) {
      // Source: vvaharness/remediation_agent/models/fixer.py:39-39
      Raise ValueError('status=applied requires at least one changed file').
    }
    // Source: vvaharness/remediation_agent/models/fixer.py:40-41
    if (the source predicate self.status != 'applied' and self.files_changed is truthy) {
      // Source: vvaharness/remediation_agent/models/fixer.py:41-41
      Raise ValueError('only status=applied may report changed files').
    }
    // Source: vvaharness/remediation_agent/models/fixer.py:42-43
    if (the source predicate self.retryable and self.status != 'tool_error' is truthy) {
      // Source: vvaharness/remediation_agent/models/fixer.py:43-43
      Raise ValueError('retryable=true is valid only for status=tool_error').
    }
    // Source: vvaharness/remediation_agent/models/fixer.py:44-45
    if (the source predicate self.status == 'tool_error' and (not self.error.strip()) is truthy) {
      // Source: vvaharness/remediation_agent/models/fixer.py:45-45
      Raise ValueError('status=tool_error requires an error description').
    }
    // Source: vvaharness/remediation_agent/models/fixer.py:46-46
    End this invocation with self.
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vvaharness/remediation_agent/models/fixer.py:49-51
  // Source: vvaharness/remediation_agent/models/fixer.py:48-48
  Before creating this callable, evaluate and retain decorators top-to-bottom: classmethod.
  // Source: vvaharness/remediation_agent/models/fixer.py:49-51
  // Source signature: schema_json_compact(cls) -> str
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn schema_json_compact(cls) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/remediation_agent/models/fixer.py:50-50
    In source order: Retain source documentation literal source_literal_50_8; it is not a model call.
    // Source: vvaharness/remediation_agent/models/fixer.py:51-51
    End this invocation with json.dumps(cls.model_json_schema(), separators=(',', ':')).
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
}
// Source: vvaharness/remediation_agent/models/fixer.py:54-54
In source order: Evaluate once ['FixerResult', 'FixerStatus']; assign in source target order to __all__.
```

## Local import links

No statically resolved in-checkout import; external calls remain explicit dependency boundaries.
