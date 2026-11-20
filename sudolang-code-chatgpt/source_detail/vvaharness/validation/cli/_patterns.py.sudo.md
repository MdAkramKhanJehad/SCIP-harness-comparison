# vvaharness/validation/cli/_patterns.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/validation/cli/_patterns.py.evidence.json`. SHA-256: `2c6d5ef07ac9769e9a7ca692df77f6b3d2f372af08ce4ef6f4af9e911291c2ff`.

```sudo
// Source: vvaharness/validation/cli/_patterns.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import re; preserve alias and import-time effects. Then Evaluate once re.compile('[^\\w\\-]'); assign in source target order to _UNSAFE.
```

## Local import links

No statically resolved in-checkout import; external calls remain explicit dependency boundaries.
