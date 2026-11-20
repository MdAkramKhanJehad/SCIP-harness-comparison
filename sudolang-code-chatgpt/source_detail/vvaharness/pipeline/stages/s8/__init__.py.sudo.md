# vvaharness/pipeline/stages/s8/__init__.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/pipeline/stages/s8/__init__.py.evidence.json`. SHA-256: `a3333c4c03b1a8fb916bef23b525ede5d0d4d7550f098c361ff6607e84d86680`.

```sudo
// Source: vvaharness/pipeline/stages/s8/__init__.py:16-47
In source order: Retain source documentation literal source_literal_16_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from vvaharness.pipeline.stages.s8.outcomes import CVSS_BAND_TO_SEV, ChainEntry, ChainReport, RankedEntry, coerce_sev, deterministic_report, final_severity, finding_ids, hydrate_report, offensive_rank, parse_chain_reply, ranked_finding, sev_from_band, severity_prose_mismatch, severity_sort_order, templated_summary; preserve alias and import-time effects. Then Resolve source import from vvaharness.pipeline.stages.s8.prompts import SYSTEM, build_prompt, reachability_for_finding; preserve alias and import-time effects. Then Resolve source import from vvaharness.pipeline.stages.s8.session import MIN_RESPONSE_CHARS, MIN_RESPONSE_TOKENS, TAG, chain_call; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s8/__init__.py:49-57
In source order: Evaluate once ['CVSS_BAND_TO_SEV', 'MIN_RESPONSE_CHARS', 'MIN_RESPONSE_TOKENS', 'SYSTEM', 'TAG', 'ChainEntry', 'ChainReport', 'RankedEntry', 'build_prompt', 'chain_call', 'coerce_sev', 'deterministic_report', 'final_severity', 'finding_ids', 'hydrate_report', 'offensive_rank', 'parse_chain_reply', 'ranked_finding', 'reachability_for_finding', 'sev_from_band', 'severity_prose_mismatch', 'severity_sort_order', 'templated_summary']; assign in source target order to __all__.
```

## Local import links

- `from vvaharness.pipeline.stages.s8.outcomes import CVSS_BAND_TO_SEV, ChainEntry, ChainReport, RankedEntry, coerce_sev, deterministic_report, final_severity, finding_ids, hydrate_report, offensive_rank, parse_chain_reply, ranked_finding, sev_from_band, severity_prose_mismatch, severity_sort_order, templated_summary` at source line 19: `source_detail/vvaharness/pipeline/stages/s8/outcomes.py.sudo.md`.
- `from vvaharness.pipeline.stages.s8.prompts import SYSTEM, build_prompt, reachability_for_finding` at source line 37: `source_detail/vvaharness/pipeline/stages/s8/prompts.py.sudo.md`.
- `from vvaharness.pipeline.stages.s8.session import MIN_RESPONSE_CHARS, MIN_RESPONSE_TOKENS, TAG, chain_call` at source line 42: `source_detail/vvaharness/pipeline/stages/s8/session.py.sudo.md`.
