# vvaharness/backends/harness/claude/models.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/backends/harness/claude/models.py.evidence.json`. SHA-256: `175a24b9cfed1e0d9f8f5fc6c9f1925c2db8c8e6aff461e6960a2ed860ba27f9`.

```sudo
// Source: vvaharness/backends/harness/claude/models.py:15-33
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from claude_agent_sdk import CLIConnectionError, CLIJSONDecodeError, CLINotFoundError; preserve alias and import-time effects. Then Resolve source import from claude_agent_sdk._errors import MessageParseError; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.models import HarnessCLINotFoundError, HarnessConnectionError, HarnessJSONDecodeError, HarnessMessageParseError; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/claude/models.py:36-43
In source order: For SDK_ERROR_MAP, assign ((CLINotFoundError, HarnessCLINotFoundError), (CLIConnectionError, HarnessConnectionError), (CLIJSONDecodeError, HarnessJSONDecodeError), (MessageParseError, HarnessMessageParseError)); source annotation tuple[tuple[type[Exception], type[Exception]], ...]. Then Evaluate once ['SDK_ERROR_MAP']; assign in source target order to __all__.
```

## Local import links

- `from vvaharness.backends.harness.models import HarnessCLINotFoundError, HarnessConnectionError, HarnessJSONDecodeError, HarnessMessageParseError` at source line 28: `source_detail/vvaharness/backends/harness/models.py.sudo.md`.
