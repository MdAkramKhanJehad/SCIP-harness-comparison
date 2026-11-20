# P10-ev-core unresolved

No `// unresolved:` markers were written. All 27 source files in the area were read in full.

Notes for later readers (not unresolved behaviour):
- vvah/vvaharness/exploit_verification/errors.sudo, safety.sudo, settings.sudo, classify/llm.sudo, auth_provider.sudo — exception subclassing is written as an empty interface plus a `// subclass of X` comment, because CONVENTIONS section 1 excludes `extends`/`inherit`. A grammar form for "error type B is a kind of A" would remove the comment; no new grammar was used.
- Calls into `executor/`, `mapping/`, `payloads/`, `collection/`, `replay/` are referenced by module and function name and marked "batch P11-ev-exec"; their behaviour is rendered by that batch, not here.
