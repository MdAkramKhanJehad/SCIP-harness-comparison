# vvaharness/validation/constants/policy.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/validation/constants/policy.py.evidence.json`. SHA-256: `437375a631e612ba3bb023d46831a983ff2747ce2525f0923d42df7c7403791f`.

```sudo
// Source: vvaharness/validation/constants/policy.py:15-31
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness import ToolPolicy; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.constants.artifacts import SYNTHESIZED_GATES_FILENAME, VALIDATION_REPORT_FILENAME; preserve alias and import-time effects. Then Evaluate once ToolPolicy(allowed_tools=('Read', 'Grep', 'Glob', 'Agent'), disallowed_tools=('Write', 'Edit', 'NotebookEdit', 'Bash')); assign in source target order to VALIDATION_POLICY.
// Source: vvaharness/validation/constants/policy.py:34-39
In source order: For DEFAULT_ALLOWED_OUTPUT_FILES, assign frozenset({VALIDATION_REPORT_FILENAME, SYNTHESIZED_GATES_FILENAME}); source annotation frozenset[str]. Then Evaluate once ['DEFAULT_ALLOWED_OUTPUT_FILES', 'VALIDATION_POLICY']; assign in source target order to __all__.
```

## Local import links

- `from vvaharness.backends.harness import ToolPolicy` at source line 21: `source_detail/vvaharness/backends/harness/__init__.py.sudo.md`.
- `from vvaharness.validation.constants.artifacts import SYNTHESIZED_GATES_FILENAME, VALIDATION_REPORT_FILENAME` at source line 22: `source_detail/vvaharness/validation/constants/artifacts.py.sudo.md`.
