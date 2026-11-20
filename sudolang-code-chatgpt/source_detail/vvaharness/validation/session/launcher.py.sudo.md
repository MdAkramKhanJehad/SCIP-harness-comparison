# vvaharness/validation/session/launcher.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/validation/session/launcher.py.evidence.json`. SHA-256: `49bc6509f70ac1f345ce0cb2bbff2ffd01ec8c675f0560f86d8eddaddee63b6b`.

```sudo
// Source: vvaharness/validation/session/launcher.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import asyncio; preserve alias and import-time effects. Then Resolve source import import contextlib; preserve alias and import-time effects. Then Resolve source import import dataclasses; preserve alias and import-time effects.
// Source: vvaharness/validation/session/launcher.py:22-26
In source order: Resolve source import import json; preserve alias and import-time effects. Then Resolve source import import os; preserve alias and import-time effects. Then Resolve source import import shutil; preserve alias and import-time effects. Then Resolve source import import time; preserve alias and import-time effects. Then Resolve source import from collections.abc import AsyncIterator, Awaitable, Callable; preserve alias and import-time effects.
// Source: vvaharness/validation/session/launcher.py:27-42
In source order: Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from typing import Any, Final, cast; preserve alias and import-time effects. Then Resolve source import from pydantic import BaseModel; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness import Harness, HarnessCLINotFoundError, HarnessError, HarnessMessage, HarnessResult, HarnessToolUse, StreamingOptions, get_harness; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.capabilities import capabilities_for; preserve alias and import-time effects.
// Source: vvaharness/validation/session/launcher.py:43-51
In source order: Resolve source import from vvaharness.backends.harness.claude.facts import SUBMIT_PROMPT_SUFFIX; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.deepagents.model_call_budget import ModelCallBudget; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.repeat_guard import guard_repeats; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm.deepagents import raise_if_refused; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm.models import TIMEOUT_STOP_GRACE_SECONDS, ModelRefusal, call_timeout_error; preserve alias and import-time effects.
// Source: vvaharness/validation/session/launcher.py:52-74
In source order: Resolve source import from vvaharness.report.redact import redact_tree; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import console, logs; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.config import Config; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.constants.artifacts import ANTHROPIC_API_KEY, ANTHROPIC_AUTH_TOKEN, LOGGING_DIRNAME, MANIFEST_FILENAME, ORCHESTRATOR_LOG_DIRNAME, SESSION_ENV_FLAG, SESSION_ENV_GH_ARCHIVED_TOKEN, SESSION_ENV_GH_TOKEN, SESSION_ENV_JIRA_KEY, SESSION_ENV_LOG_DIR, SESSION_ENV_MANIFEST, SESSION_ENV_OUTPUT_DIR, SESSION_ENV_PROJECT_DIR, SESSION_ENV_SESSION_ID, SESSION_ENV_TARGET_DIR, SYNTHESIZED_GATES_FILENAME, VALIDATION_REPORT_FILENAME; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.constants.paths import FIX_VALIDATION; preserve alias and import-time effects.
// Source: vvaharness/validation/session/launcher.py:75-79
In source order: Resolve source import from vvaharness.validation.io.message_logger import stream_and_log; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.io.persona_report_stash import extract_subagent_reports; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.models import HarnessTerminalState, Manifest, PersonaReport; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.session.config_inject import inject_claude_config; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.session.errors import ValidationSessionError; preserve alias and import-time effects.
// Source: vvaharness/validation/session/launcher.py:80-95
In source order: Resolve source import from vvaharness.validation.session.launch_prompt import build_launch_prompt; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.session.rules import orchestrator_rules_text, persona_rules_text; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.session.setup import DEFAULT_FACT_TOOLS, VALIDATION_GRAPH_NAME, VALIDATION_POLICY, ValidationOutput, build_validation_tools, validation_skill_root, validation_write_gate; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.subagents import load_agents; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.synthesis._consensus import synthesize_gates_for_finding; preserve alias and import-time effects.
// Source: vvaharness/validation/session/launcher.py:96-114
In source order: Resolve source import from vvaharness.validation.tools.fact_specs import build_validation_fact_specs; preserve alias and import-time effects. Then Evaluate once logs.get_logger(__name__); assign in source target order to log. Then For _DEFAULT_VALIDATE_ENV_VARS, assign (ANTHROPIC_API_KEY, ANTHROPIC_AUTH_TOKEN, 'ANTHROPIC_BASE_URL', 'OPENAI_API_KEY', 'OPENAI_BASE_URL'); source annotation tuple[str, ...]. Then For _BACKSTOP_GRACE_S, assign 2 * TIMEOUT_STOP_GRACE_SECONDS; source annotation Final. Then For _HEARTBEAT_SECS, assign 60.0; source annotation Final.
// Source: vvaharness/validation/session/launcher.py:118-123
// Source: vvaharness/validation/session/launcher.py:117-117
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclasses.dataclass.
// Source: vvaharness/validation/session/launcher.py:118-123
interface _HeartbeatState {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/validation/session/launcher.py:119-123
  In source order: Retain source documentation literal source_literal_119_4; it is not a model call. Then For last_activity, assign dataclasses.field(default_factory=time.monotonic); source annotation float. Then For tool_counts, assign dataclasses.field(default_factory=dict); source annotation dict[str, int].
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vvaharness/validation/session/launcher.py:126-140
// Source signature: _heartbeat_ticker(state: _HeartbeatState, case_label: str, started: float) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _heartbeat_ticker(state, case_label, started) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  This callable produces a coroutine or async generator; await/suspension positions remain in source expressions.
  // Source: vvaharness/validation/session/launcher.py:127-127
  In source order: Retain source documentation literal source_literal_127_4; it is not a model call.
  // Source: vvaharness/validation/session/launcher.py:128-140
  while (the source predicate True is truthy) {
    // Source: vvaharness/validation/session/launcher.py:129-136
    In source order: Evaluate await asyncio.sleep(_HEARTBEAT_SECS); retain side effects and discard the expression result. Then Evaluate once int(time.monotonic() - started); assign in source target order to elapsed. Then Evaluate once int(time.monotonic() - state.last_activity); assign in source target order to quiet_now. Then Evaluate once ' '.join((source_template_133_12 for agent, n in sorted(state.tool_counts.items()))) or 'none'; assign in source target order to counts. Then Evaluate once 'waiting on model' if quiet_now >= _HEARTBEAT_SECS else 'in progress'; assign in source target order to status.
    // Source: vvaharness/validation/session/launcher.py:137-140
    In source order: Evaluate console.write(source_template_138_12); retain side effects and discard the expression result.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/session/launcher.py:143-173
// Source signature: _build_env(config: Config, manifest: Manifest, workspace: Path, output_dir: Path) -> dict[str, str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _build_env(config, manifest, workspace, output_dir) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/session/launcher.py:149-164
  In source order: Retain source documentation literal source_literal_149_4; it is not a model call. Then Evaluate once os.environ.get(ANTHROPIC_AUTH_TOKEN) or os.environ.get(ANTHROPIC_API_KEY, ''); assign in source target order to effective_api_key. Then For env, assign {ANTHROPIC_API_KEY: effective_api_key, SESSION_ENV_FLAG: 'true', SESSION_ENV_TARGET_DIR: str(workspace), SESSION_ENV_OUTPUT_DIR: str(output_dir), SESSION_ENV_MANIFEST: str(workspace / MANIFEST_FILENAME), SESSION_ENV_LOG_DIR: str(workspace / LOGGING_DIRNAME), SESSION_ENV_JIRA_KEY: manifest.case_id, SESSION_ENV_SESSION_ID: manifest.session_id, SESSION_ENV_PROJECT_DIR: str(workspace)}; source annotation dict[str, str].
  // Source: vvaharness/validation/session/launcher.py:165-168
  for each name in _DEFAULT_VALIDATE_ENV_VARS {
    // Source: vvaharness/validation/session/launcher.py:166-166
    In source order: Evaluate once os.environ.get(name); assign in source target order to value.
    // Source: vvaharness/validation/session/launcher.py:167-168
    if (the source predicate value is not None is truthy) {
      // Source: vvaharness/validation/session/launcher.py:168-168
      In source order: Evaluate once value; assign in source target order to env[name].
    }
  }
  // Source: vvaharness/validation/session/launcher.py:169-170
  if (the source predicate config.ghe.token is truthy) {
    // Source: vvaharness/validation/session/launcher.py:170-170
    In source order: Evaluate once config.ghe.token; assign in source target order to env[SESSION_ENV_GH_TOKEN].
  }
  // Source: vvaharness/validation/session/launcher.py:171-172
  if (the source predicate config.ghe.archived_token is truthy) {
    // Source: vvaharness/validation/session/launcher.py:172-172
    In source order: Evaluate once config.ghe.archived_token; assign in source target order to env[SESSION_ENV_GH_ARCHIVED_TOKEN].
  }
  // Source: vvaharness/validation/session/launcher.py:173-173
  End this invocation with env.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/session/launcher.py:176-186
// Source signature: _persona_overrides(config: Config) -> dict[str, str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _persona_overrides(config) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/session/launcher.py:177-177
  In source order: Retain source documentation literal source_literal_177_4; it is not a model call.
  // Source: vvaharness/validation/session/launcher.py:178-186
  End this invocation with {name: model for name, model in (('security-architect', config.agent.security_architect_model), ('penetration-tester', config.agent.penetration_tester_model), ('cross-repo-analyzer', config.agent.cross_repo_analyzer_model)) if model}.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/session/launcher.py:189-211
// Source signature: _resolve_binary(binary: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _resolve_binary(binary) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/session/launcher.py:190-191
  In source order: Retain source documentation literal source_literal_190_4; it is not a model call. Then Evaluate once Path(binary); assign in source target order to configured.
  // Source: vvaharness/validation/session/launcher.py:192-195
  if (the source predicate configured.is_absolute() is truthy) {
    // Source: vvaharness/validation/session/launcher.py:193-194
    if (the source predicate configured.is_file() is truthy) {
      // Source: vvaharness/validation/session/launcher.py:194-194
      End this invocation with str(configured.resolve()).
    }
    // Source: vvaharness/validation/session/launcher.py:195-195
    Raise HarnessCLINotFoundError(source_template_195_38).
  }
  // Source: vvaharness/validation/session/launcher.py:196-198
  if (the source predicate not binary or configured.name != binary or '\\' in binary or (':' in binary) is truthy) {
    // Source: vvaharness/validation/session/launcher.py:197-198
    Raise HarnessCLINotFoundError(source_template_198_12).
  }
  // Source: vvaharness/validation/session/launcher.py:199-199
  In source order: Evaluate once Path.cwd().resolve(); assign in source target order to cwd.
  // Source: vvaharness/validation/session/launcher.py:200-208
  for each entry in os.environ.get('PATH', os.defpath).split(os.pathsep) {
    // Source: vvaharness/validation/session/launcher.py:201-201
    In source order: Evaluate once Path(entry); assign in source target order to directory.
    // Source: vvaharness/validation/session/launcher.py:202-203
    if (the source predicate not directory.is_absolute() or directory.resolve().is_relative_to(cwd) is truthy) {
      // Source: vvaharness/validation/session/launcher.py:203-203
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/validation/session/launcher.py:204-204
    In source order: Evaluate once shutil.which(str(directory / binary)); assign in source target order to found.
    // Source: vvaharness/validation/session/launcher.py:205-208
    if (the source predicate found is truthy) {
      // Source: vvaharness/validation/session/launcher.py:206-206
      In source order: Evaluate once Path(found); assign in source target order to resolved.
      // Source: vvaharness/validation/session/launcher.py:207-208
      if (the source predicate resolved.is_absolute() and (not resolved.resolve().is_relative_to(cwd)) is truthy) {
        // Source: vvaharness/validation/session/launcher.py:208-208
        End this invocation with str(resolved.resolve()).
      }
    }
  }
  // Source: vvaharness/validation/session/launcher.py:209-211
  Raise HarnessCLINotFoundError(source_template_210_8).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/session/launcher.py:214-225
// Source signature: _write_workspace_json(workspace: Path, filename: str, payload: Any) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _write_workspace_json(workspace, filename, payload) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/session/launcher.py:215-217
  In source order: Retain source documentation literal source_literal_215_4; it is not a model call. Then Evaluate once workspace / filename; assign in source target order to dest. Then Evaluate once dest.with_suffix(source_template_217_27); assign in source target order to tmp.
  // Source: vvaharness/validation/session/launcher.py:218-225
  Perform the following protected operations {
    // Source: vvaharness/validation/session/launcher.py:219-221
    In source order: Evaluate once json.dumps(redact_tree(payload), indent=2) + source_literal_219_60; assign in source target order to text. Then Evaluate tmp.write_text(text, encoding='utf-8'); retain side effects and discard the expression result. Then Evaluate tmp.replace(dest); retain side effects and discard the expression result.
  }
  // Source: vvaharness/validation/session/launcher.py:222-225
  On the first matching source exception (OSError, TypeError, ValueError), in handler order {
    // Source: vvaharness/validation/session/launcher.py:223-223
    In source order: Evaluate log.exception('cannot write %s', dest); retain side effects and discard the expression result.
    // Source: vvaharness/validation/session/launcher.py:224-225
    Enter source context managers left-to-right: contextlib.suppress(OSError) {
      // Source: vvaharness/validation/session/launcher.py:225-225
      In source order: Evaluate tmp.unlink(missing_ok=True); retain side effects and discard the expression result.
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/session/launcher.py:228-245
// Source signature: _write_validation_outputs(workspace: Path, structured: Any) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _write_validation_outputs(workspace, structured) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/session/launcher.py:229-229
  In source order: Retain source documentation literal source_literal_229_4; it is not a model call.
  // Source: vvaharness/validation/session/launcher.py:230-231
  if (the source predicate isinstance(structured, BaseModel) is truthy) {
    // Source: vvaharness/validation/session/launcher.py:231-231
    In source order: Evaluate once structured.model_dump(mode='json'); assign in source target order to structured.
  }
  // Source: vvaharness/validation/session/launcher.py:232-234
  if (the source predicate not isinstance(structured, dict) is truthy) {
    // Source: vvaharness/validation/session/launcher.py:233-233
    In source order: Evaluate log.warning('structured validation output is not a dict; skipping host write'); retain side effects and discard the expression result.
    // Source: vvaharness/validation/session/launcher.py:234-234
    End this invocation with None.
  }
  // Source: vvaharness/validation/session/launcher.py:235-237
  In source order: Evaluate once structured.get('findings'); assign in source target order to findings. Then Evaluate once structured.get('synthesized_gates'); assign in source target order to gates. Then Evaluate once structured.get('target_jira_status'); assign in source target order to target_status.
  // Source: vvaharness/validation/session/launcher.py:238-243
  if (the source predicate findings is not None is truthy) {
    // Source: vvaharness/validation/session/launcher.py:239-243
    In source order: Evaluate _write_workspace_json(workspace, VALIDATION_REPORT_FILENAME, {'target_jira_status': target_status, 'findings': findings}); retain side effects and discard the expression result.
  }
  // Source: vvaharness/validation/session/launcher.py:244-245
  if (the source predicate gates is not None is truthy) {
    // Source: vvaharness/validation/session/launcher.py:245-245
    In source order: Evaluate _write_workspace_json(workspace, SYNTHESIZED_GATES_FILENAME, gates); retain side effects and discard the expression result.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/session/launcher.py:248-260
// Source signature: _synthesize_gates(reports: list[PersonaReport], tracking_ids: list[str]) -> list[dict]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _synthesize_gates(reports, tracking_ids) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/session/launcher.py:251-252
  In source order: Retain source documentation literal source_literal_251_4; it is not a model call. Then For synthesized, assign []; source annotation list[dict].
  // Source: vvaharness/validation/session/launcher.py:253-259
  for each tracking_id in tracking_ids {
    // Source: vvaharness/validation/session/launcher.py:254-254
    In source order: Evaluate once synthesize_gates_for_finding(reports, tracking_id); assign in source target order to gates.
    // Source: vvaharness/validation/session/launcher.py:255-259
    if (the source predicate gates is truthy) {
      // Source: vvaharness/validation/session/launcher.py:256-259
      In source order: Evaluate synthesized.append({'tracking_id': tracking_id, 'gates': [gate.model_dump() for gate in gates]}); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/validation/session/launcher.py:260-260
  End this invocation with synthesized.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/session/launcher.py:263-283
// Source signature: _write_host_synthesized_gates(workspace: Path, terminal_state: HarnessTerminalState, tracking_ids: list[str]) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _write_host_synthesized_gates(workspace, terminal_state, tracking_ids) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/session/launcher.py:268-268
  In source order: Retain source documentation literal source_literal_268_4; it is not a model call.
  // Source: vvaharness/validation/session/launcher.py:269-271
  if (the source predicate not isinstance(terminal_state, dict) is truthy) {
    // Source: vvaharness/validation/session/launcher.py:270-270
    In source order: Evaluate log.warning('terminal harness state is not a dict; skipping host synthesis'); retain side effects and discard the expression result.
    // Source: vvaharness/validation/session/launcher.py:271-271
    End this invocation with None.
  }
  // Source: vvaharness/validation/session/launcher.py:272-273
  In source order: Evaluate once extract_subagent_reports(terminal_state); assign in source target order to reports. Then Evaluate once sorted(set(FIX_VALIDATION.agent_names) - {r.persona for r in reports}); assign in source target order to missing.
  // Source: vvaharness/validation/session/launcher.py:274-276
  if (the source predicate missing is truthy) {
    // Source: vvaharness/validation/session/launcher.py:275-276
    In source order: Evaluate console.write(source_template_275_22); retain side effects and discard the expression result.
  }
  // Source: vvaharness/validation/session/launcher.py:277-279
  if (the source predicate not reports is truthy) {
    // Source: vvaharness/validation/session/launcher.py:278-278
    In source order: Evaluate log.warning('no valid persona reports extracted; skipping host synthesis'); retain side effects and discard the expression result.
    // Source: vvaharness/validation/session/launcher.py:279-279
    End this invocation with None.
  }
  // Source: vvaharness/validation/session/launcher.py:281-281
  In source order: Evaluate once _synthesize_gates(reports, tracking_ids); assign in source target order to synthesized.
  // Source: vvaharness/validation/session/launcher.py:282-283
  if (the source predicate synthesized is truthy) {
    // Source: vvaharness/validation/session/launcher.py:283-283
    In source order: Evaluate _write_workspace_json(workspace, SYNTHESIZED_GATES_FILENAME, synthesized); retain side effects and discard the expression result.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/session/launcher.py:286-296
// Source signature: _orchestrator_call_budget(config: Config) -> ModelCallBudget | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _orchestrator_call_budget(config) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/session/launcher.py:287-288
  In source order: Retain source documentation literal source_literal_287_4; it is not a model call. Then Evaluate once config.agent.orchestrator_max_model_calls; assign in source target order to limit.
  // Source: vvaharness/validation/session/launcher.py:289-290
  if (the source predicate limit <= 0 is truthy) {
    // Source: vvaharness/validation/session/launcher.py:290-290
    End this invocation with None.
  }
  // Source: vvaharness/validation/session/launcher.py:291-296
  End this invocation with ModelCallBudget(limit=limit, outcome_tools=frozenset({ValidationOutput.__name__}), counter='s11_orchestrator_model_call_budget_final_turn', stage='s11').
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/session/launcher.py:299-345
// Source signature: build_validation_options(config: Config, manifest: Manifest, workspace: Path, output_dir: Path, system_prompt: str | None) -> StreamingOptions
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn build_validation_options(config, manifest, workspace, output_dir, system_prompt) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/session/launcher.py:306-308
  In source order: Retain source documentation literal source_literal_306_4; it is not a model call. Then Evaluate once FIX_VALIDATION; assign in source target order to path_cfg. Then Evaluate once _injects_claude_config(config); assign in source target order to injects_claude.
  // Source: vvaharness/validation/session/launcher.py:309-345
  End this invocation with StreamingOptions(model=config.agent.model, model_provider=config.agent.provider, use_responses_api=config.agent.use_responses_api, cwd=workspace, env=_build_env(config, manifest, workspace, output_dir), effort=config.agent.effort, max_turns=config.agent.max_turns, max_budget_usd=config.agent.max_budget_usd, timeout=config.agent.timeout, system_prompt=system_prompt, setting_sources=('project',), cli_path=_resolve_binary(config.agent.binary) if injects_claude else None, tool_policy=VALIDATION_POLICY, permissions=validation_write_gate(workspace), response_model=ValidationOutput, force_verdict_only=True, tool_builder=build_validation_tools, fact_tools=DEFAULT_FACT_TOOLS, fact_tool_specs=build_validation_fact_specs(workspace), skill_root=validation_skill_root(workspace) if injects_claude else None, graph_name=VALIDATION_GRAPH_NAME, agents=load_agents(path_cfg.agent_names, model_overrides=_persona_overrides(config), tools_override=config.agent.validate_tools, prompt_suffix=SUBMIT_PROMPT_SUFFIX if injects_claude else persona_rules_text(), max_model_calls=config.agent.max_model_calls), parent_middleware=tuple((m for m in (_orchestrator_call_budget(config),) if m is not None)), cache_markers=config.agent.cache_markers).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/session/launcher.py:348-350
// Source signature: _injects_claude_config(config: Config) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _injects_claude_config(config) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/session/launcher.py:349-349
  In source order: Retain source documentation literal source_literal_349_4; it is not a model call.
  // Source: vvaharness/validation/session/launcher.py:350-350
  End this invocation with capabilities_for(config.agent.via).reads_injected_claude_config.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/session/launcher.py:353-366
// Source signature: _rules_section(config: Config) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _rules_section(config) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/session/launcher.py:354-354
  In source order: Retain source documentation literal source_literal_354_4; it is not a model call.
  // Source: vvaharness/validation/session/launcher.py:355-361
  if (the source predicate _injects_claude_config(config) is truthy) {
    // Source: vvaharness/validation/session/launcher.py:356-361
    End this invocation with source_literal_357_12.
  }
  // Source: vvaharness/validation/session/launcher.py:362-366
  End this invocation with source_template_363_8.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/session/launcher.py:369-371
// Source signature: _synthesizes_gates_on_host(config: Config) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _synthesizes_gates_on_host(config) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/session/launcher.py:370-370
  In source order: Retain source documentation literal source_literal_370_4; it is not a model call.
  // Source: vvaharness/validation/session/launcher.py:371-371
  End this invocation with capabilities_for(config.agent.via).returns_schema_validated_reports.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/session/launcher.py:374-394
// Source signature: _synthesis_section(config: Config) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _synthesis_section(config) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/session/launcher.py:375-375
  In source order: Retain source documentation literal source_literal_375_4; it is not a model call.
  // Source: vvaharness/validation/session/launcher.py:376-383
  if (the source predicate _synthesizes_gates_on_host(config) is truthy) {
    // Source: vvaharness/validation/session/launcher.py:377-383
    End this invocation with source_literal_378_12.
  }
  // Source: vvaharness/validation/session/launcher.py:384-394
  End this invocation with source_literal_385_8.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/session/launcher.py:397-409
// Source signature: _load_system_prompt(config: Config, path_cfg: object) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _load_system_prompt(config, path_cfg) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/session/launcher.py:398-399
  In source order: Retain source documentation literal source_literal_398_4; it is not a model call. Then Evaluate once getattr(path_cfg, 'system_prompt_file', None); assign in source target order to prompt_file.
  // Source: vvaharness/validation/session/launcher.py:400-401
  if (the source predicate not prompt_file is truthy) {
    // Source: vvaharness/validation/session/launcher.py:401-401
    End this invocation with None.
  }
  // Source: vvaharness/validation/session/launcher.py:402-402
  In source order: Evaluate once config.paths.prompts_dir / prompt_file; assign in source target order to path.
  // Source: vvaharness/validation/session/launcher.py:403-404
  if (the source predicate not path.exists() is truthy) {
    // Source: vvaharness/validation/session/launcher.py:404-404
    End this invocation with None.
  }
  // Source: vvaharness/validation/session/launcher.py:405-409
  End this invocation with source_template_406_8.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/session/launcher.py:412-412
In source order: Evaluate once 'error_max_structured_output_retries'; assign in source target order to _STRUCTURED_RETRY_SUBTYPE.
// Source: vvaharness/validation/session/launcher.py:415-428
// Source signature: _failure_reason(terminal: HarnessResult | None, exit_code: int) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _failure_reason(terminal, exit_code) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/session/launcher.py:416-416
  In source order: Retain source documentation literal source_literal_416_4; it is not a model call.
  // Source: vvaharness/validation/session/launcher.py:417-418
  if (the source predicate terminal is None is truthy) {
    // Source: vvaharness/validation/session/launcher.py:418-418
    End this invocation with source_template_418_15.
  }
  // Source: vvaharness/validation/session/launcher.py:419-419
  In source order: Evaluate once [source_template_419_13]; assign in source target order to parts.
  // Source: vvaharness/validation/session/launcher.py:420-425
  if (the source predicate terminal.subtype == _STRUCTURED_RETRY_SUBTYPE is truthy) {
    // Source: vvaharness/validation/session/launcher.py:421-425
    In source order: Evaluate parts.append(source_literal_422_12); retain side effects and discard the expression result.
  }
  // Source: vvaharness/validation/session/launcher.py:426-427
  if (the source predicate terminal.errors is truthy) {
    // Source: vvaharness/validation/session/launcher.py:427-427
    In source order: Evaluate parts.append('errors: ' + ' | '.join((str(e) for e in terminal.errors))); retain side effects and discard the expression result.
  }
  // Source: vvaharness/validation/session/launcher.py:428-428
  End this invocation with ' -- '.join(parts).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/session/launcher.py:431-456
// Source signature: _bounded_stream(do_stream: Callable[[], Awaitable[tuple[int, str]]], timeout: float | None, effort: str | None) -> tuple[int, str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _bounded_stream(do_stream, timeout, effort) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  This callable produces a coroutine or async generator; await/suspension positions remain in source expressions.
  // Source: vvaharness/validation/session/launcher.py:436-441
  In source order: Retain source documentation literal source_literal_436_4; it is not a model call.
  // Source: vvaharness/validation/session/launcher.py:442-443
  if (the source predicate timeout is None or timeout <= 0 is truthy) {
    // Source: vvaharness/validation/session/launcher.py:443-443
    End this invocation with await do_stream().
  }
  // Source: vvaharness/validation/session/launcher.py:444-444
  In source order: Evaluate once asyncio.timeout(timeout + _BACKSTOP_GRACE_S); assign in source target order to deadline.
  // Source: vvaharness/validation/session/launcher.py:445-456
  Perform the following protected operations {
    // Source: vvaharness/validation/session/launcher.py:446-447
    Await and enter source context managers left-to-right: deadline {
      // Source: vvaharness/validation/session/launcher.py:447-447
      End this invocation with await do_stream().
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics and await async exits.
  }
  // Source: vvaharness/validation/session/launcher.py:448-456
  On the first matching source exception TimeoutError as exc, in handler order {
    // Source: vvaharness/validation/session/launcher.py:451-452
    if (the source predicate not deadline.expired() is truthy) {
      // Source: vvaharness/validation/session/launcher.py:452-452
      Raise the currently handled exception.
    }
    // Source: vvaharness/validation/session/launcher.py:453-456
    Raise call_timeout_error(stage='s11', route='backstop', budget_s=timeout, effort=effort, cause_text=source_template_455_23) with explicit source cause exc.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/session/launcher.py:461-513
// Source signature: _stream_session(harness: Harness, prompt: str, options: StreamingOptions, session_id: str, log_dir: Path, *, case_label: str='', route: str='') -> tuple[int, str | None, list[HarnessMessage]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _stream_session(harness, prompt, options, session_id, log_dir, case_label, route) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  This callable produces a coroutine or async generator; await/suspension positions remain in source expressions.
  // Source: vvaharness/validation/session/launcher.py:471-483
  In source order: Retain source documentation literal source_literal_471_4; it is not a model call. Then For messages, assign []; source annotation list[HarnessMessage]. Then Evaluate once _HeartbeatState(); assign in source target order to heartbeat. Then Evaluate once time.monotonic(); assign in source target order to started. Then Evaluate once asyncio.create_task(_heartbeat_ticker(heartbeat, case_label or session_id, started)); assign in source target order to ticker.
  // Source: vvaharness/validation/session/launcher.py:485-495
  // Source signature: _do_stream() -> tuple[int, str]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _do_stream() {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    This callable produces a coroutine or async generator; await/suspension positions remain in source expressions.
    // Source: vvaharness/validation/session/launcher.py:486-495
    End this invocation with await stream_and_log(_log_stream(guard_repeats(harness.run_streaming(prompt, options), stage='s11', route=route), messages, heartbeat), log_dir=log_dir / ORCHESTRATOR_LOG_DIRNAME, session_id=session_id, live=False).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/validation/session/launcher.py:497-512
  Perform the following protected operations {
    // Source: vvaharness/validation/session/launcher.py:498-500
    In source order: Evaluate once await _bounded_stream(_do_stream, getattr(options, 'timeout', None), getattr(options, 'effort', None)); assign in source target order to (exit_code, observed_sid).
  }
  // Source: vvaharness/validation/session/launcher.py:501-502
  On the first matching source exception HarnessCLINotFoundError, in handler order {
    // Source: vvaharness/validation/session/launcher.py:502-502
    Raise the currently handled exception.
  }
  // Source: vvaharness/validation/session/launcher.py:503-508
  On the first matching source exception HarnessError as e, in handler order {
    // Source: vvaharness/validation/session/launcher.py:504-508
    Raise ValidationSessionError(source_template_505_12, cause=e, exit_code=getattr(e, 'exit_code', None)) with explicit source cause e.
  }
  On every exit from this protected/handler/normal-completion region {
    // Source: vvaharness/validation/session/launcher.py:510-510
    In source order: Evaluate ticker.cancel(); retain side effects and discard the expression result.
    // Source: vvaharness/validation/session/launcher.py:511-512
    Enter source context managers left-to-right: contextlib.suppress(asyncio.CancelledError) {
      // Source: vvaharness/validation/session/launcher.py:512-512
      In source order: Evaluate await ticker; retain side effects and discard the expression result.
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
  }
  // Source: vvaharness/validation/session/launcher.py:513-513
  End this invocation with (exit_code, observed_sid, messages).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/session/launcher.py:516-524
// Source signature: _raise_if_session_refused(terminal: HarnessResult | None, exit_code: int) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _raise_if_session_refused(terminal, exit_code) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/session/launcher.py:517-517
  In source order: Retain source documentation literal source_literal_517_4; it is not a model call.
  // Source: vvaharness/validation/session/launcher.py:518-524
  Perform the following protected operations {
    // Source: vvaharness/validation/session/launcher.py:519-519
    In source order: Evaluate raise_if_refused(terminal, tag='s11'); retain side effects and discard the expression result.
  }
  // Source: vvaharness/validation/session/launcher.py:520-524
  On the first matching source exception ModelRefusal as exc, in handler order {
    // Source: vvaharness/validation/session/launcher.py:521-524
    Raise ValidationSessionError(source_template_522_12, cause=exc, exit_code=exit_code) with explicit source cause exc.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/session/launcher.py:528-577
// Source signature: _run_and_check(*, harness: Harness, prompt: str, options: StreamingOptions, session_id: str, log_dir: Path, workspace: Path, tracking_ids: list[str], host_gate_synthesis: bool=True, route: str='') -> int
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _run_and_check(harness, prompt, options, session_id, log_dir, workspace, tracking_ids, host_gate_synthesis, route) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  This callable produces a coroutine or async generator; await/suspension positions remain in source expressions.
  // Source: vvaharness/validation/session/launcher.py:540-548
  In source order: Retain source documentation literal source_literal_540_4; it is not a model call. Then Evaluate once await _stream_session(harness, prompt, options, session_id, log_dir, case_label=', '.join(tracking_ids) if tracking_ids else session_id, route=route); assign in source target order to (exit_code, observed_sid, messages). Then Evaluate once next((m for m in reversed(messages) if isinstance(m, HarnessResult)), None); assign in source target order to terminal.
  // Source: vvaharness/validation/session/launcher.py:550-555
  if (the source predicate exit_code != 0 is truthy) {
    // Source: vvaharness/validation/session/launcher.py:551-551
    In source order: Evaluate log.error('Session %s exited with code %d', session_id, exit_code); retain side effects and discard the expression result.
    // Source: vvaharness/validation/session/launcher.py:552-555
    Raise ValidationSessionError(_failure_reason(terminal, exit_code), exit_code=exit_code).
  }
  // Source: vvaharness/validation/session/launcher.py:557-557
  In source order: Evaluate _raise_if_session_refused(terminal, exit_code); retain side effects and discard the expression result.
  // Source: vvaharness/validation/session/launcher.py:558-559
  if (the source predicate terminal is not None and terminal.structured is not None is truthy) {
    // Source: vvaharness/validation/session/launcher.py:559-559
    In source order: Evaluate _write_validation_outputs(workspace, terminal.structured); retain side effects and discard the expression result.
  }
  // Source: vvaharness/validation/session/launcher.py:561-564
  if (the source predicate host_gate_synthesis and terminal is not None and (terminal.state is not None) is truthy) {
    // Source: vvaharness/validation/session/launcher.py:562-564
    In source order: Evaluate _write_host_synthesized_gates(workspace, cast(HarnessTerminalState, terminal.state), tracking_ids); retain side effects and discard the expression result.
  }
  // Source: vvaharness/validation/session/launcher.py:566-575
  if (the source predicate terminal is not None and terminal.structured is None and (not host_gate_synthesis or terminal.state is None) is truthy) {
    // Source: vvaharness/validation/session/launcher.py:571-575
    Raise ValidationSessionError(source_literal_572_12, exit_code=exit_code).
  }
  // Source: vvaharness/validation/session/launcher.py:576-576
  In source order: Evaluate log.debug('Session %s completed (observed_sid=%s)', session_id, observed_sid); retain side effects and discard the expression result.
  // Source: vvaharness/validation/session/launcher.py:577-577
  End this invocation with exit_code.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/session/launcher.py:580-593
// Source signature: _log_stream(source: AsyncIterator[HarnessMessage], collected: list[HarnessMessage], heartbeat: _HeartbeatState | None=None) -> AsyncIterator[HarnessMessage]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _log_stream(source, collected, heartbeat) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  This callable produces a coroutine or async generator; await/suspension positions remain in source expressions.
  // Source: vvaharness/validation/session/launcher.py:585-585
  In source order: Retain source documentation literal source_literal_585_4; it is not a model call.
  // Source: vvaharness/validation/session/launcher.py:586-593
  Obtain/advance the following source async iterator by awaiting, without inventing parallel dispatch.
  for each msg in source {
    // Source: vvaharness/validation/session/launcher.py:587-587
    In source order: Evaluate collected.append(msg); retain side effects and discard the expression result.
    // Source: vvaharness/validation/session/launcher.py:588-592
    if (the source predicate heartbeat is not None is truthy) {
      // Source: vvaharness/validation/session/launcher.py:589-589
      In source order: Evaluate once time.monotonic(); assign in source target order to heartbeat.last_activity.
      // Source: vvaharness/validation/session/launcher.py:590-592
      if (the source predicate isinstance(msg, HarnessToolUse) is truthy) {
        // Source: vvaharness/validation/session/launcher.py:591-592
        In source order: Evaluate once msg.agent or 'orchestrator'; assign in source target order to agent. Then Evaluate once heartbeat.tool_counts.get(agent, 0) + 1; assign in source target order to heartbeat.tool_counts[agent].
      }
    }
    // Source: vvaharness/validation/session/launcher.py:593-593
    In source order: Yield msg; suspend this generator until resumed.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/session/launcher.py:596-631
// Source signature: launch_session(config: Config, manifest: Manifest, workspace_dir: Path, output_dir: Path, harness: Harness | None=None) -> int
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn launch_session(config, manifest, workspace_dir, output_dir, harness) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  This callable produces a coroutine or async generator; await/suspension positions remain in source expressions.
  // Source: vvaharness/validation/session/launcher.py:603-603
  In source order: Retain source documentation literal source_literal_603_4; it is not a model call.
  // Source: vvaharness/validation/session/launcher.py:604-605
  if (the source predicate _injects_claude_config(config) is truthy) {
    // Source: vvaharness/validation/session/launcher.py:605-605
    In source order: Evaluate inject_claude_config(workspace_dir); retain side effects and discard the expression result.
  }
  // Source: vvaharness/validation/session/launcher.py:606-620
  In source order: Evaluate output_dir.mkdir(parents=True, exist_ok=True); retain side effects and discard the expression result. Then Evaluate once FIX_VALIDATION; assign in source target order to path_cfg. Then Evaluate once build_validation_options(config=config, manifest=manifest, workspace=workspace_dir, output_dir=output_dir, system_prompt=_load_system_prompt(config, path_cfg)); assign in source target order to options. Then Evaluate log.info('Launching validation session %s for %s in %s', manifest.session_id, manifest.case_id, workspace_dir); retain side effects and discard the expression result. Then Evaluate once [manifest.case_id] if manifest.case_id else []; assign in source target order to tracking_ids.
  // Source: vvaharness/validation/session/launcher.py:621-631
  End this invocation with await _run_and_check(harness=harness if harness is not None else get_harness(config.agent.via), prompt=build_launch_prompt(manifest), options=options, session_id=manifest.session_id, log_dir=workspace_dir / LOGGING_DIRNAME, workspace=workspace_dir, tracking_ids=tracking_ids, host_gate_synthesis=_synthesizes_gates_on_host(config), route=config.agent.via).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.backends.harness import Harness, HarnessCLINotFoundError, HarnessError, HarnessMessage, HarnessResult, HarnessToolUse, StreamingOptions, get_harness` at source line 32: `source_detail/vvaharness/backends/harness/__init__.py.sudo.md`.
- `from vvaharness.backends.harness.capabilities import capabilities_for` at source line 42: `source_detail/vvaharness/backends/harness/capabilities.py.sudo.md`.
- `from vvaharness.backends.harness.claude.facts import SUBMIT_PROMPT_SUFFIX` at source line 43: `source_detail/vvaharness/backends/harness/claude/facts.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.model_call_budget import ModelCallBudget` at source line 44: `source_detail/vvaharness/backends/harness/deepagents/model_call_budget.py.sudo.md`.
- `from vvaharness.backends.harness.repeat_guard import guard_repeats` at source line 45: `source_detail/vvaharness/backends/harness/repeat_guard.py.sudo.md`.
- `from vvaharness.backends.llm.deepagents import raise_if_refused` at source line 46: `source_detail/vvaharness/backends/llm/deepagents.py.sudo.md`.
- `from vvaharness.backends.llm.models import TIMEOUT_STOP_GRACE_SECONDS, ModelRefusal, call_timeout_error` at source line 47: `source_detail/vvaharness/backends/llm/models.py.sudo.md`.
- `from vvaharness.report.redact import redact_tree` at source line 52: `source_detail/vvaharness/report/redact.py.sudo.md`.
- `from vvaharness.util import console, logs` at source line 53: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import console, logs` at source line 53: `source_detail/vvaharness/util/console.py.sudo.md`.
- `from vvaharness.util import console, logs` at source line 53: `source_detail/vvaharness/util/logs.py.sudo.md`.
- `from vvaharness.validation.config import Config` at source line 54: `source_detail/vvaharness/validation/config/__init__.py.sudo.md`.
- `from vvaharness.validation.constants.artifacts import ANTHROPIC_API_KEY, ANTHROPIC_AUTH_TOKEN, LOGGING_DIRNAME, MANIFEST_FILENAME, ORCHESTRATOR_LOG_DIRNAME, SESSION_ENV_FLAG, SESSION_ENV_GH_ARCHIVED_TOKEN, SESSION_ENV_GH_TOKEN, SESSION_ENV_JIRA_KEY, SESSION_ENV_LOG_DIR, SESSION_ENV_MANIFEST, SESSION_ENV_OUTPUT_DIR, SESSION_ENV_PROJECT_DIR, SESSION_ENV_SESSION_ID, SESSION_ENV_TARGET_DIR, SYNTHESIZED_GATES_FILENAME, VALIDATION_REPORT_FILENAME` at source line 55: `source_detail/vvaharness/validation/constants/artifacts.py.sudo.md`.
- `from vvaharness.validation.constants.paths import FIX_VALIDATION` at source line 74: `source_detail/vvaharness/validation/constants/paths.py.sudo.md`.
- `from vvaharness.validation.io.message_logger import stream_and_log` at source line 75: `source_detail/vvaharness/validation/io/message_logger.py.sudo.md`.
- `from vvaharness.validation.io.persona_report_stash import extract_subagent_reports` at source line 76: `source_detail/vvaharness/validation/io/persona_report_stash.py.sudo.md`.
- `from vvaharness.validation.models import HarnessTerminalState, Manifest, PersonaReport` at source line 77: `source_detail/vvaharness/validation/models/__init__.py.sudo.md`.
- `from vvaharness.validation.session.config_inject import inject_claude_config` at source line 78: `source_detail/vvaharness/validation/session/config_inject.py.sudo.md`.
- `from vvaharness.validation.session.errors import ValidationSessionError` at source line 79: `source_detail/vvaharness/validation/session/errors.py.sudo.md`.
- `from vvaharness.validation.session.launch_prompt import build_launch_prompt` at source line 80: `source_detail/vvaharness/validation/session/launch_prompt.py.sudo.md`.
- `from vvaharness.validation.session.rules import orchestrator_rules_text, persona_rules_text` at source line 81: `source_detail/vvaharness/validation/session/rules.py.sudo.md`.
- `from vvaharness.validation.session.setup import DEFAULT_FACT_TOOLS, VALIDATION_GRAPH_NAME, VALIDATION_POLICY, ValidationOutput, build_validation_tools, validation_skill_root, validation_write_gate` at source line 85: `source_detail/vvaharness/validation/session/setup.py.sudo.md`.
- `from vvaharness.validation.subagents import load_agents` at source line 94: `source_detail/vvaharness/validation/subagents/__init__.py.sudo.md`.
- `from vvaharness.validation.synthesis._consensus import synthesize_gates_for_finding` at source line 95: `source_detail/vvaharness/validation/synthesis/_consensus.py.sudo.md`.
- `from vvaharness.validation.tools.fact_specs import build_validation_fact_specs` at source line 96: `source_detail/vvaharness/validation/tools/fact_specs.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../prompt_representation/vvaharness/validation/session/launcher.py.sudo.md). Exact strings in the evidence asset support this conversion.
