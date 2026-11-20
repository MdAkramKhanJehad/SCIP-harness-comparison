# vvaharness/plugins/semgrep/__init__.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/plugins/semgrep/__init__.py.evidence.json`. SHA-256: `8dc60a781f39f8bdf9ea99b98795b427946402ec73b2e03f467fdec7fae8322f`.

```sudo
// Source: vvaharness/plugins/semgrep/__init__.py:15-23
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from vvaharness.plugins.semgrep.enricher import SemgrepEnricher; preserve alias and import-time effects. Then Resolve source import from vvaharness.plugins.semgrep.findings import SemgrepFindingsError, findings_from_semgrep, read_semgrep_json; preserve alias and import-time effects. Then Resolve source import from vvaharness.plugins.semgrep.plugin import VERSION, SemgrepConfigError, SemgrepPlugin; preserve alias and import-time effects. Then Resolve source import from vvaharness.plugins.semgrep.tools import SEMGREP_TOOL_NAMES, SEMGREP_TOOLS; preserve alias and import-time effects.
// Source: vvaharness/plugins/semgrep/__init__.py:24-37
In source order: Resolve source import from vvaharness.plugins.semgrep.triage import semgrep_triage_subagent; preserve alias and import-time effects. Then Evaluate once ['SEMGREP_TOOLS', 'SEMGREP_TOOL_NAMES', 'VERSION', 'SemgrepConfigError', 'SemgrepEnricher', 'SemgrepFindingsError', 'SemgrepPlugin', 'findings_from_semgrep', 'read_semgrep_json', 'semgrep_triage_subagent']; assign in source target order to __all__.
```

## Local import links

- `from vvaharness.plugins.semgrep.enricher import SemgrepEnricher` at source line 16: `source_detail/vvaharness/plugins/semgrep/enricher.py.sudo.md`.
- `from vvaharness.plugins.semgrep.findings import SemgrepFindingsError, findings_from_semgrep, read_semgrep_json` at source line 17: `source_detail/vvaharness/plugins/semgrep/findings.py.sudo.md`.
- `from vvaharness.plugins.semgrep.plugin import VERSION, SemgrepConfigError, SemgrepPlugin` at source line 22: `source_detail/vvaharness/plugins/semgrep/plugin.py.sudo.md`.
- `from vvaharness.plugins.semgrep.tools import SEMGREP_TOOL_NAMES, SEMGREP_TOOLS` at source line 23: `source_detail/vvaharness/plugins/semgrep/tools.py.sudo.md`.
- `from vvaharness.plugins.semgrep.triage import semgrep_triage_subagent` at source line 24: `source_detail/vvaharness/plugins/semgrep/triage.py.sudo.md`.
