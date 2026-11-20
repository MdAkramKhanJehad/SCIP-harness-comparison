# vvaharness/pipeline/stages/s7/__init__.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/pipeline/stages/s7/__init__.py.evidence.json`. SHA-256: `4cb89493efc1aae2cfb9e33a99d6241ca01e966e4423f201bc0b9bf0c2655b42`.

```sudo
// Source: vvaharness/pipeline/stages/s7/__init__.py:16-33
In source order: Retain source documentation literal source_literal_16_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from vvaharness.pipeline.stages.s7.collapse import STRICT_CWE_CLASS, TRIVIAL_REASON, attach_duplicates, collapse_trivial, cwe_conflict, dedup_locations, dup_location; preserve alias and import-time effects. Then Resolve source import from vvaharness.pipeline.stages.s7.outcomes import DedupDecision, DedupDecisions, parse_decisions; preserve alias and import-time effects. Then Resolve source import from vvaharness.pipeline.stages.s7.prompts import SYSTEM, build_payload; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s7/__init__.py:34-46
In source order: Resolve source import from vvaharness.pipeline.stages.s7.session import MIN_RESPONSE_CHARS, MIN_RESPONSE_TOKENS, semantic_dedup; preserve alias and import-time effects. Then Evaluate once ['MIN_RESPONSE_CHARS', 'MIN_RESPONSE_TOKENS', 'STRICT_CWE_CLASS', 'SYSTEM', 'TRIVIAL_REASON', 'DedupDecision', 'DedupDecisions', 'attach_duplicates', 'build_payload', 'collapse_trivial', 'cwe_conflict', 'dedup_locations', 'title_overlap', 'dup_location', 'parse_decisions', 'semantic_dedup']; assign in source target order to __all__.
```

## Local import links

- `from vvaharness.pipeline.stages.s7.collapse import STRICT_CWE_CLASS, TRIVIAL_REASON, attach_duplicates, collapse_trivial, cwe_conflict, dedup_locations, dup_location` at source line 19: `source_detail/vvaharness/pipeline/stages/s7/collapse.py.sudo.md`.
- `from vvaharness.pipeline.stages.s7.outcomes import DedupDecision, DedupDecisions, parse_decisions` at source line 28: `source_detail/vvaharness/pipeline/stages/s7/outcomes.py.sudo.md`.
- `from vvaharness.pipeline.stages.s7.prompts import SYSTEM, build_payload` at source line 33: `source_detail/vvaharness/pipeline/stages/s7/prompts.py.sudo.md`.
- `from vvaharness.pipeline.stages.s7.session import MIN_RESPONSE_CHARS, MIN_RESPONSE_TOKENS, semantic_dedup` at source line 34: `source_detail/vvaharness/pipeline/stages/s7/session.py.sudo.md`.
