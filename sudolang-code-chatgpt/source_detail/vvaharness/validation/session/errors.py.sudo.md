# vvaharness/validation/session/errors.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/validation/session/errors.py.evidence.json`. SHA-256: `757f1cc6e39669323b8bc985f151d19f08e219468184a407025f2c4f0b52bad8`.

```sudo
// Source: vvaharness/validation/session/errors.py:15-18
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from vvaharness.backends.harness import HarnessError, HarnessProcessError; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.constants.artifacts import STDERR_TAIL_LINES; preserve alias and import-time effects.
// Source: vvaharness/validation/session/errors.py:21-45
interface ValidationSessionError {
  Describe the source Python type, preserving its base/metaclass expression order: Exception.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/validation/session/errors.py:22-22
  In source order: Retain source documentation literal source_literal_22_4; it is not a model call.
  // Source: vvaharness/validation/session/errors.py:24-33
  // Source signature: __init__(self, message: str, cause: Exception | None=None, exit_code: int | None=None) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self, message, cause, exit_code) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/validation/session/errors.py:30-33
    In source order: Retain source documentation literal source_literal_30_8; it is not a model call. Then Evaluate super().__init__(message); retain side effects and discard the expression result. Then Evaluate once cause; assign in source target order to self.cause. Then Evaluate once exit_code; assign in source target order to self.exit_code.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/validation/session/errors.py:35-45
  // Source signature: reason_string(self) -> str
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn reason_string(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/validation/session/errors.py:36-37
    In source order: Retain source documentation literal source_literal_36_8; it is not a model call. Then Evaluate once [str(self)]; assign in source target order to parts.
    // Source: vvaharness/validation/session/errors.py:38-39
    if (the source predicate self.exit_code is not None is truthy) {
      // Source: vvaharness/validation/session/errors.py:39-39
      In source order: Evaluate parts.append(source_template_39_25); retain side effects and discard the expression result.
    }
    // Source: vvaharness/validation/session/errors.py:40-44
    if (the source predicate isinstance(self.cause, HarnessProcessError) and self.cause.stderr is truthy) {
      // Source: vvaharness/validation/session/errors.py:41-42
      In source order: Evaluate once self.cause.stderr.splitlines()[-STDERR_TAIL_LINES:]; assign in source target order to tail. Then Evaluate parts.append('stderr: ' + ' | '.join(tail)); retain side effects and discard the expression result.
    }
    else {
      // Source: vvaharness/validation/session/errors.py:43-44
      if (the source predicate isinstance(self.cause, HarnessError) or self.cause is not None is truthy) {
        // Source: vvaharness/validation/session/errors.py:44-44
        In source order: Evaluate parts.append(source_template_44_25); retain side effects and discard the expression result.
      }
    }
    // Source: vvaharness/validation/session/errors.py:45-45
    End this invocation with ' -- '.join(parts).
    If execution reaches this end, finish with the source implicit None result.
  }
}
```

## Local import links

- `from vvaharness.backends.harness import HarnessError, HarnessProcessError` at source line 17: `source_detail/vvaharness/backends/harness/__init__.py.sudo.md`.
- `from vvaharness.validation.constants.artifacts import STDERR_TAIL_LINES` at source line 18: `source_detail/vvaharness/validation/constants/artifacts.py.sudo.md`.
