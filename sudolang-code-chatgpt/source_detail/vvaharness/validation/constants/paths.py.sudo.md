# vvaharness/validation/constants/paths.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/validation/constants/paths.py.evidence.json`. SHA-256: `34d7fdef209192d989d6e7ec8078231e706cc528d09fc65cf3fbe58272be6763`.

```sudo
// Source: vvaharness/validation/constants/paths.py:15-22
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from dataclasses import dataclass; preserve alias and import-time effects. Then Resolve source import from typing import Final; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.constants.artifacts import SYSTEM_PROMPT_FILENAME; preserve alias and import-time effects.
// Source: vvaharness/validation/constants/paths.py:24-24
In source order: Evaluate once ['FIX_VALIDATION', 'PathConfig']; assign in source target order to __all__.
// Source: vvaharness/validation/constants/paths.py:28-32
// Source: vvaharness/validation/constants/paths.py:27-27
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vvaharness/validation/constants/paths.py:28-32
interface PathConfig {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/validation/constants/paths.py:29-32
  In source order: Retain source documentation literal source_literal_29_4; it is not a model call. Then For agent_names, declare without assigning a value; source annotation tuple[str, ...]. Then For system_prompt_file, declare without assigning a value; source annotation str.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vvaharness/validation/constants/paths.py:35-38
In source order: For FIX_VALIDATION, assign PathConfig(agent_names=('security-architect', 'penetration-tester', 'cross-repo-analyzer'), system_prompt_file=SYSTEM_PROMPT_FILENAME); source annotation Final[PathConfig].
```

## Local import links

- `from vvaharness.validation.constants.artifacts import SYSTEM_PROMPT_FILENAME` at source line 22: `source_detail/vvaharness/validation/constants/artifacts.py.sudo.md`.
