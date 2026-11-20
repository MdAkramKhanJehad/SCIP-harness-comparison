# Unresolved items, P9-skills-util

No `// unresolved:` markers were written in this area.

Notes:
- How a backend turns `skill_root` into skills a model can see (frontmatter `description` selection) is outside this area; marked `// external:` in every SKILL.sudo.md and in `vvah/vvaharness/skills/__init__.sudo`.
- No harness code runs any `probe.sh`; whether a model runs it is the model's decision (stated in each probe.sudo header).
- `vvaharness/util/net.py` is imported only by `vvaharness/exploit_verification/safety.py` (rendered by batch P10-ev-core).

Grammar: none needed. Pass-1 files used a `??` null-coalescing operator (not in SudoLang); it was replaced with `if` expressions rather than proposed as an extension.
