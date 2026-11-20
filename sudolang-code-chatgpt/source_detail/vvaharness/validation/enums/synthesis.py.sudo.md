# vvaharness/validation/enums/synthesis.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/validation/enums/synthesis.py.evidence.json`. SHA-256: `c64dbe2f91144b702ada6275daffeae209ae275a3a9e339e993bc0ed312c6015`.

```sudo
// Source: vvaharness/validation/enums/synthesis.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from enum import StrEnum; preserve alias and import-time effects. Then Evaluate once ['SynthesisConfidence']; assign in source target order to __all__.
// Source: vvaharness/validation/enums/synthesis.py:24-28
interface SynthesisConfidence {
  Describe the source Python type, preserving its base/metaclass expression order: StrEnum.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/validation/enums/synthesis.py:25-28
  In source order: Retain source documentation literal source_literal_25_4; it is not a model call. Then Evaluate once 'HIGH'; assign in source target order to HIGH. Then Evaluate once 'FLAGGED'; assign in source target order to FLAGGED.
}
```

## Local import links

No statically resolved in-checkout import; external calls remain explicit dependency boundaries.
