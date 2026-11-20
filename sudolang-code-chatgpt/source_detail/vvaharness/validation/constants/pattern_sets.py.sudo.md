# vvaharness/validation/constants/pattern_sets.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/validation/constants/pattern_sets.py.evidence.json`. SHA-256: `3dfa2f13ab1c808f00b9f418c0a250b242903848d0b691c05ecc17635e084ebe`.

```sudo
// Source: vvaharness/validation/constants/pattern_sets.py:15-22
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import re; preserve alias and import-time effects. Then Resolve source import from vvaharness.scope import _INSECURE_RX, _SECRET_RX; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.constants.artifacts import DIFF_FILENAME; preserve alias and import-time effects.
// Source: vvaharness/validation/constants/pattern_sets.py:24-33
In source order: For DEFAULT_PATTERN_SETS, assign {'secret_exposure': ('hardcoded secret or credential', _SECRET_RX), 'insecure_value': ('insecure configuration value', _INSECURE_RX)}; source annotation dict[str, tuple[str, re.Pattern[str]]]. Then For SKIP_IN_SCAN, assign frozenset({DIFF_FILENAME}); source annotation frozenset[str]. Then For NUL_BYTE, assign b'\x00'; source annotation bytes. Then For BUILTIN_RULE, assign '__builtin__'; source annotation str.
```

## Local import links

- `from vvaharness.scope import _INSECURE_RX, _SECRET_RX` at source line 21: `source_detail/vvaharness/scope/__init__.py.sudo.md`.
- `from vvaharness.validation.constants.artifacts import DIFF_FILENAME` at source line 22: `source_detail/vvaharness/validation/constants/artifacts.py.sudo.md`.
