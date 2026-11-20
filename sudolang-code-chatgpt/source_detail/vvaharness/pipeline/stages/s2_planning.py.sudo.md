# vvaharness/pipeline/stages/s2_planning.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/pipeline/stages/s2_planning.py.evidence.json`. SHA-256: `0bcfb8950ed967728af659b819f5ab4c5cc7aa696129907144661c6115bc62e4`.

```sudo
// Source: vvaharness/pipeline/stages/s2_planning.py:15-67
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Evaluate once source_literal_20_4; assign in source target order to PLAN_SYSTEM_PROMPT. Then Evaluate once source_literal_57_4; assign in source target order to PLAN_TOOL_DESCRIPTION. Then Evaluate once ['PLAN_SYSTEM_PROMPT', 'PLAN_TOOL_DESCRIPTION']; assign in source target order to __all__.
```

## Local import links

No statically resolved in-checkout import; external calls remain explicit dependency boundaries.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../prompt_representation/vvaharness/pipeline/stages/s2_planning.py.sudo.md). Exact strings in the evidence asset support this conversion.
