# vvaharness/validation/scoring/_configs.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/validation/scoring/_configs.py.evidence.json`. SHA-256: `5da9528093189596a35ee29e834c825aaf800cf3f1cd2b3fdba212eacefdbf73`.

```sudo
// Source: vvaharness/validation/scoring/_configs.py:15-26
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from typing import Final; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.constants.scoring import CRITERION_NAME_FIELD, FIX_POLICY, STATUS_MULTIPLIER; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.models.scoring import ScoringConfig; preserve alias and import-time effects.
// Source: vvaharness/validation/scoring/_configs.py:28-39
In source order: Resolve source import from ._justify import build_fix_justification; preserve alias and import-time effects. Then Evaluate once ['FIX_CONFIG']; assign in source target order to __all__. Then For FIX_CONFIG, assign ScoringConfig.from_policy(FIX_POLICY, name='fix', criterion_name_field=CRITERION_NAME_FIELD, status_multiplier=STATUS_MULTIPLIER, justify=build_fix_justification); source annotation Final[ScoringConfig].
```

## Local import links

- `from vvaharness.validation.constants.scoring import CRITERION_NAME_FIELD, FIX_POLICY, STATUS_MULTIPLIER` at source line 21: `source_detail/vvaharness/validation/constants/scoring.py.sudo.md`.
- `from vvaharness.validation.models.scoring import ScoringConfig` at source line 26: `source_detail/vvaharness/validation/models/scoring.py.sudo.md`.
- `from ._justify import build_fix_justification` at source line 28: `source_detail/vvaharness/validation/scoring/_justify.py.sudo.md`.
