# vvaharness/backends/harness/__init__.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/backends/harness/__init__.py.evidence.json`. SHA-256: `659aae4758c7e48e23903f7529b122413a7cd48c4ef45f46824a711b5053e36e`.

```sudo
// Source: vvaharness/backends/harness/__init__.py:15-59
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from vvaharness.backends.harness.harness import Harness; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.models import DEFAULT_GRAPH_NAME, LEGACY_AGENT_TOOL, LOGICAL_TO_NATIVE, MCP_TOOL_PREFIX, MUTATING_TOOLS, NATIVE_CONTENT_TOOLS, NATIVE_WRITE_TOOLS, ORCHESTRATION_TOOLS, READ_ONLY_TOOLS, READ_TOOLS, UNCONDITIONALLY_DENIED_TOOLS, EffortLevel, FactToolSpec, HarnessAssistantText, HarnessCLINotFoundError, HarnessConnectionError, HarnessError, HarnessJSONDecodeError, HarnessMessage, HarnessMessageParseError, HarnessProcessError, HarnessResult, HarnessSessionInit, HarnessToolResult, HarnessToolUse, OneShotOptions, OneShotResult, PermissionDecision, Provider, SessionOptions, SettingSource, StreamingOptions, SubagentDefinition, ToolBuilder, ToolPolicy, compose_tool_builders; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.permission_rules import evaluate_write; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.permissions import PermissionsPolicy; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/__init__.py:60-105
In source order: Resolve source import from vvaharness.backends.harness.provider_routing import routes_to_anthropic; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.registry import get_harness; preserve alias and import-time effects. Then Evaluate once ['DEFAULT_GRAPH_NAME', 'LEGACY_AGENT_TOOL', 'LOGICAL_TO_NATIVE', 'MCP_TOOL_PREFIX', 'MUTATING_TOOLS', 'NATIVE_CONTENT_TOOLS', 'NATIVE_WRITE_TOOLS', 'ORCHESTRATION_TOOLS', 'READ_ONLY_TOOLS', 'READ_TOOLS', 'UNCONDITIONALLY_DENIED_TOOLS', 'EffortLevel', 'FactToolSpec', 'Harness', 'HarnessAssistantText', 'HarnessCLINotFoundError', 'HarnessConnectionError', 'HarnessError', 'HarnessJSONDecodeError', 'HarnessMessage', 'HarnessMessageParseError', 'HarnessProcessError', 'HarnessResult', 'HarnessSessionInit', 'HarnessToolResult', 'HarnessToolUse', 'OneShotOptions', 'OneShotResult', 'PermissionDecision', 'PermissionsPolicy', 'Provider', 'SessionOptions', 'SettingSource', 'StreamingOptions', 'SubagentDefinition', 'ToolBuilder', 'ToolPolicy', 'compose_tool_builders', 'evaluate_write', 'get_harness', 'routes_to_anthropic']; assign in source target order to __all__.
```

## Local import links

- `from vvaharness.backends.harness.harness import Harness` at source line 19: `source_detail/vvaharness/backends/harness/harness.py.sudo.md`.
- `from vvaharness.backends.harness.models import DEFAULT_GRAPH_NAME, LEGACY_AGENT_TOOL, LOGICAL_TO_NATIVE, MCP_TOOL_PREFIX, MUTATING_TOOLS, NATIVE_CONTENT_TOOLS, NATIVE_WRITE_TOOLS, ORCHESTRATION_TOOLS, READ_ONLY_TOOLS, READ_TOOLS, UNCONDITIONALLY_DENIED_TOOLS, EffortLevel, FactToolSpec, HarnessAssistantText, HarnessCLINotFoundError, HarnessConnectionError, HarnessError, HarnessJSONDecodeError, HarnessMessage, HarnessMessageParseError, HarnessProcessError, HarnessResult, HarnessSessionInit, HarnessToolResult, HarnessToolUse, OneShotOptions, OneShotResult, PermissionDecision, Provider, SessionOptions, SettingSource, StreamingOptions, SubagentDefinition, ToolBuilder, ToolPolicy, compose_tool_builders` at source line 20: `source_detail/vvaharness/backends/harness/models.py.sudo.md`.
- `from vvaharness.backends.harness.permission_rules import evaluate_write` at source line 58: `source_detail/vvaharness/backends/harness/permission_rules.py.sudo.md`.
- `from vvaharness.backends.harness.permissions import PermissionsPolicy` at source line 59: `source_detail/vvaharness/backends/harness/permissions.py.sudo.md`.
- `from vvaharness.backends.harness.provider_routing import routes_to_anthropic` at source line 60: `source_detail/vvaharness/backends/harness/provider_routing.py.sudo.md`.
- `from vvaharness.backends.harness.registry import get_harness` at source line 61: `source_detail/vvaharness/backends/harness/registry.py.sudo.md`.
