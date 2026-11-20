# vvaharness/validation/constants/tools.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/validation/constants/tools.py.evidence.json`. SHA-256: `99e740b57dff0a690ff639667f37b3ec1e4c02468b2b25445b7c646bec706868`.

```sudo
// Source: vvaharness/validation/constants/tools.py:15-30
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from typing import Final; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness import READ_TOOLS; preserve alias and import-time effects. Then For FACT_TOOLS, assign ('DiffTouched', 'ChangedLines', 'DiffImpactMap', 'PatternScan', 'TestInventory'); source annotation Final[tuple[str, ...]].
// Source: vvaharness/validation/constants/tools.py:33-33
In source order: For DEFAULT_FACT_TOOLS, assign (*sorted(READ_TOOLS), *FACT_TOOLS); source annotation Final[tuple[str, ...]].
```

## Local import links

- `from vvaharness.backends.harness import READ_TOOLS` at source line 21: `source_detail/vvaharness/backends/harness/__init__.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../prompt_representation/vvaharness/validation/constants/tools.py.sudo.md). Exact strings in the evidence asset support this conversion.
