# vvaharness/backends/harness/deepagents/limits.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/backends/harness/deepagents/limits.py.evidence.json`. SHA-256: `5adc132c09ac23d58145f7c3f2a4752a93252fc3737ba4b71c67d5f4437b5c3d`.

```sudo
// Source: vvaharness/backends/harness/deepagents/limits.py:15-36
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then For RECURSION_HEADROOM, assign 900; source annotation int. Then For MODEL_TIMEOUT_SECONDS, assign 1800.0; source annotation float. Then For MODEL_MAX_OUTPUT_TOKENS, assign 64000; source annotation int.
// Source: vvaharness/backends/harness/deepagents/limits.py:39-42
In source order: For MODEL_MAX_RETRIES, assign 2; source annotation int. Then Evaluate once ['MODEL_MAX_OUTPUT_TOKENS', 'MODEL_MAX_RETRIES', 'MODEL_TIMEOUT_SECONDS', 'RECURSION_HEADROOM']; assign in source target order to __all__.
```

## Local import links

No statically resolved in-checkout import; external calls remain explicit dependency boundaries.
