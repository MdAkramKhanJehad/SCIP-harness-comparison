# vvaharness/validation/constants/artifacts.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/validation/constants/artifacts.py.evidence.json`. SHA-256: `4452ded8baf674bfe5516ddd53f87e54833d6237bdaf8ae10835e8ceaf74f464`.

```sudo
// Source: vvaharness/validation/constants/artifacts.py:15-22
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from typing import Final; preserve alias and import-time effects. Then Resolve source import from vvaharness.models import CaseState; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.enums import EffortLevel, Provider; preserve alias and import-time effects.
// Source: vvaharness/validation/constants/artifacts.py:24-30
In source order: For MANIFEST_FILENAME, assign 'manifest.json'; source annotation Final. Then For DIFF_FILENAME, assign 'diff.patch'; source annotation Final. Then For VALIDATION_REPORT_FILENAME, assign 'validation_report.json'; source annotation Final. Then For SYNTHESIZED_GATES_FILENAME, assign 'synthesized_gates.json'; source annotation Final. Then For APP_DIRNAME, assign 'app'; source annotation Final.
// Source: vvaharness/validation/constants/artifacts.py:31-43
In source order: For REMEDIATION_DIRNAME, assign 'security-remediation'; source annotation Final. Then For FINDING_CASE_FILENAME, assign 'finding_case.json'; source annotation Final. Then For FINDING_CASE_GLOB, assign source_template_33_27; source annotation Final. Then For VALIDATABLE_STATES, assign frozenset({CaseState.OPEN, CaseState.REMEDIATED, CaseState.FAILED}); source annotation Final[frozenset[CaseState]]. Then For SCAN_DIRNAME, assign 'security-scan'; source annotation Final.
// Source: vvaharness/validation/constants/artifacts.py:44-65
In source order: For SCAN_REPORT_GLOB, assign '*_report.sarif'; source annotation Final. Then For CLAUDE_DIRNAME, assign '.claude'; source annotation Final. Then For AGENT_INSTRUCTION_FILENAMES, assign ('CLAUDE.md', 'CLAUDE.local.md', 'AGENTS.md', 'GEMINI.md', '.cursorrules'); source annotation Final[tuple[str, ...]]. Then For MCP_CONFIG_FILENAME, assign '.mcp.json'; source annotation Final. Then For LOGGING_DIRNAME, assign 'logging'; source annotation Final.
// Source: vvaharness/validation/constants/artifacts.py:66-72
In source order: For ORCHESTRATOR_LOG_DIRNAME, assign 'orchestrator'; source annotation Final. Then For SUBAGENTS_LOG_DIRNAME, assign 'subagents'; source annotation Final. Then For ENV_MODEL, assign 'VVAHARNESS_MODEL'; source annotation Final. Then For ENV_EFFORT, assign 'VVAHARNESS_EFFORT'; source annotation Final. Then For ENV_MAX_TURNS, assign 'VVAHARNESS_MAX_TURNS'; source annotation Final.
// Source: vvaharness/validation/constants/artifacts.py:73-77
In source order: For ENV_MAX_RETRIES, assign 'VVAHARNESS_MAX_RETRIES'; source annotation Final. Then For ENV_CLAUDE_BINARY, assign 'VVAHARNESS_CLAUDE_BINARY'; source annotation Final. Then For ENV_GHE_TOKEN, assign 'VVAHARNESS_GHE_TOKEN'; source annotation Final. Then For ENV_GHE_ARCHIVED_TOKEN, assign 'VVAHARNESS_GHE_ARCHIVED_TOKEN'; source annotation Final. Then For ENV_VIA, assign 'VVAHARNESS_VIA'; source annotation Final.
// Source: vvaharness/validation/constants/artifacts.py:78-84
In source order: For ENV_MODEL_PROVIDER, assign 'VVAHARNESS_MODEL_PROVIDER'; source annotation Final. Then For ENV_MAX_BUDGET_USD, assign 'VVAHARNESS_MAX_BUDGET_USD'; source annotation Final. Then For ENV_MAX_FINDINGS, assign 'VVAHARNESS_MAX_FINDINGS'; source annotation Final. Then For ENV_VALIDATE_TOOLS, assign 'VVAHARNESS_VALIDATE_TOOLS'; source annotation Final. Then For ENV_SECURITY_ARCHITECT_MODEL, assign 'VVAHARNESS_SECURITY_ARCHITECT_MODEL'; source annotation Final.
// Source: vvaharness/validation/constants/artifacts.py:85-91
In source order: For ENV_PENETRATION_TESTER_MODEL, assign 'VVAHARNESS_PENETRATION_TESTER_MODEL'; source annotation Final. Then For ENV_CROSS_REPO_ANALYZER_MODEL, assign 'VVAHARNESS_CROSS_REPO_ANALYZER_MODEL'; source annotation Final. Then For SESSION_ENV_FLAG, assign 'VALIDATION_SESSION'; source annotation Final. Then For SESSION_ENV_TARGET_DIR, assign 'VALIDATION_TARGET_DIR'; source annotation Final. Then For SESSION_ENV_OUTPUT_DIR, assign 'VALIDATION_OUTPUT_DIR'; source annotation Final.
// Source: vvaharness/validation/constants/artifacts.py:92-97
In source order: For SESSION_ENV_MANIFEST, assign 'VALIDATION_MANIFEST'; source annotation Final. Then For SESSION_ENV_LOG_DIR, assign 'VALIDATION_LOG_DIR'; source annotation Final. Then For SESSION_ENV_JIRA_KEY, assign 'JIRA_KEY'; source annotation Final. Then For SESSION_ENV_SESSION_ID, assign 'SESSION_ID'; source annotation Final. Then For SESSION_ENV_PROJECT_DIR, assign 'CLAUDE_PROJECT_DIR'; source annotation Final.
// Source: vvaharness/validation/constants/artifacts.py:98-106
In source order: For SESSION_ENV_GH_TOKEN, assign 'GH_ENTERPRISE_TOKEN'; source annotation Final. Then For SESSION_ENV_GH_ARCHIVED_TOKEN, assign 'GH_ARCHIVED_TOKEN'; source annotation Final. Then For BACKEND_OPENAI, assign 'openai'; source annotation Final. Then For BACKEND_DEEPAGENTS, assign 'deepagents'; source annotation Final. Then For PROVIDER_OPENAI, assign Provider.OPENAI.value; source annotation Final.
// Source: vvaharness/validation/constants/artifacts.py:107-115
In source order: For PROVIDER_ANTHROPIC, assign Provider.ANTHROPIC.value; source annotation Final. Then For VALIDATE_COMMAND, assign 'validate'; source annotation Final. Then For VALIDATE_ALIAS_S11, assign 's11'; source annotation Final. Then For VALIDATE_COMMANDS, assign (VALIDATE_COMMAND, VALIDATE_ALIAS_S11); source annotation Final. Then For ANTHROPIC_API_KEY, assign 'ANTHROPIC_API_KEY'; source annotation Final.
// Source: vvaharness/validation/constants/artifacts.py:116-125
In source order: For ANTHROPIC_AUTH_TOKEN, assign 'ANTHROPIC_AUTH_TOKEN'; source annotation Final. Then For SESSION_LOG_FILENAME, assign 'session.jsonl'; source annotation Final. Then For VALIDATION_SESSION_LOG_PREFIX, assign 'validation_session_'; source annotation Final. Then For CMD_PREVIEW_LEN, assign 80; source annotation Final. Then For STDERR_TAIL_LINES, assign 3; source annotation Final.
// Source: vvaharness/validation/constants/artifacts.py:128-132
In source order: For DEFAULT_CLAUDE_BINARY, assign 'claude'; source annotation Final. Then For DEFAULT_MODEL, assign 'claude-opus-4-8[1m]'; source annotation Final. Then For DEFAULT_MAX_TURNS, assign 50; source annotation Final. Then For DEFAULT_VALIDATION_VIA, assign 'deepagents'; source annotation Final. Then For DEFAULT_MAX_BUDGET_USD, assign 15.0; source annotation Final.
// Source: vvaharness/validation/constants/artifacts.py:133-140
In source order: For DEFAULT_MAX_FINDINGS, assign 20; source annotation Final. Then For DEFAULT_EFFORT, assign EffortLevel.HIGH; source annotation Final. Then For DEFAULT_TIMEOUT_S, assign 3600; source annotation Final. Then For DEFAULT_PERSONA_MAX_MODEL_CALLS, assign 60; source annotation Final. Then For DEFAULT_ORCHESTRATOR_MAX_MODEL_CALLS, assign 40; source annotation Final.
// Source: vvaharness/validation/constants/artifacts.py:142-148
In source order: For TARGETS_DIRNAME, assign 'targets'; source annotation Final. Then For OUTPUTS_DIRNAME, assign 'outputs'; source annotation Final. Then For PROMPTS_DIRNAME, assign 'prompts'; source annotation Final. Then For INPUTS_DIRNAME, assign 'inputs'; source annotation Final. Then For VALIDATOR_HINTS_FILENAME, assign 'validator_hints.yaml'; source annotation Final.
// Source: vvaharness/validation/constants/artifacts.py:150-152
In source order: For SYSTEM_PROMPT_FILENAME, assign 'system.md'; source annotation Final. Then For MISSING_FIELD_PLACEHOLDER, assign 'N/A'; source annotation Final.
```

## Local import links

- `from vvaharness.models import CaseState` at source line 21: `source_detail/vvaharness/models/__init__.py.sudo.md`.
- `from vvaharness.validation.enums import EffortLevel, Provider` at source line 22: `source_detail/vvaharness/validation/enums/__init__.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../prompt_representation/vvaharness/validation/constants/artifacts.py.sudo.md). Exact strings in the evidence asset support this conversion.
