# vvaharness/util/exceptions.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/util/exceptions.py.evidence.json`. SHA-256: `c9d050da2c16012956ca8347fd46d815a8fe08e2e72ab0287260d9fe50e1c04b`.

```sudo
// Source: vvaharness/util/exceptions.py:15-16
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects.
// Source: vvaharness/util/exceptions.py:19-28
interface S2HollowAfterRetry {
  Describe the source Python type, preserving its base/metaclass expression order: Exception.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/util/exceptions.py:20-22
  In source order: Retain source documentation literal source_literal_20_4; it is not a model call. Then For reason, declare without assigning a value; source annotation str.
  // Source: vvaharness/util/exceptions.py:24-28
  // Source signature: __init__(self, reason: str) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self, reason) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/util/exceptions.py:25-28
    In source order: Evaluate super().__init__(source_template_26_12); retain side effects and discard the expression result. Then Evaluate once reason; assign in source target order to self.reason.
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vvaharness/util/exceptions.py:31-41
// Source signature: exception_chain(exc: BaseException) -> list[BaseException]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn exception_chain(exc) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/exceptions.py:32-34
  In source order: Retain source documentation literal source_literal_32_4; it is not a model call. Then For links, assign [exc]; source annotation list[BaseException]. Then For seen, assign {id(exc)}; source annotation set[int].
  // Source: vvaharness/util/exceptions.py:35-40
  while (the source predicate True is truthy) {
    // Source: vvaharness/util/exceptions.py:36-36
    In source order: Evaluate once links[-1].__cause__; assign in source target order to cause.
    // Source: vvaharness/util/exceptions.py:37-38
    if (the source predicate cause is None or id(cause) in seen is truthy) {
      // Source: vvaharness/util/exceptions.py:38-38
      Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
    }
    // Source: vvaharness/util/exceptions.py:39-40
    In source order: Evaluate seen.add(id(cause)); retain side effects and discard the expression result. Then Evaluate links.append(cause); retain side effects and discard the expression result.
  }
  // Source: vvaharness/util/exceptions.py:41-41
  End this invocation with links.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

No statically resolved in-checkout import; external calls remain explicit dependency boundaries.
