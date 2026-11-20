# vvaharness/validation/session/__init__.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/validation/session/__init__.py.evidence.json`. SHA-256: `5fb4bac1b1ca3734a1a26f7c88e7479abecd6aa9876d359a284bef33e9cd1004`.

```sudo
// Source: vvaharness/validation/session/__init__.py:15-23
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from vvaharness.validation.session.config_inject import inject_claude_config; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.session.errors import ValidationSessionError; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.session.launch_prompt import build_launch_prompt; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.session.launcher import build_validation_options, launch_session; preserve alias and import-time effects.
// Source: vvaharness/validation/session/__init__.py:25-31
In source order: Evaluate once ['ValidationSessionError', 'build_launch_prompt', 'build_validation_options', 'inject_claude_config', 'launch_session']; assign in source target order to __all__.
```

## Local import links

- `from vvaharness.validation.session.config_inject import inject_claude_config` at source line 17: `source_detail/vvaharness/validation/session/config_inject.py.sudo.md`.
- `from vvaharness.validation.session.errors import ValidationSessionError` at source line 18: `source_detail/vvaharness/validation/session/errors.py.sudo.md`.
- `from vvaharness.validation.session.launch_prompt import build_launch_prompt` at source line 19: `source_detail/vvaharness/validation/session/launch_prompt.py.sudo.md`.
- `from vvaharness.validation.session.launcher import build_validation_options, launch_session` at source line 20: `source_detail/vvaharness/validation/session/launcher.py.sudo.md`.
