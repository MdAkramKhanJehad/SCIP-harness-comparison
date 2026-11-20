# vvaharness/backends/llm/cli/session.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/backends/llm/cli/session.py.evidence.json`. SHA-256: `20fe3d7d02c9e738e90f33b74b03febd73b74186d5b53a751b7635f77055a268`.

```sudo
// Source: vvaharness/backends/llm/cli/session.py:15-20
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import json; preserve alias and import-time effects. Then Resolve source import import subprocess; preserve alias and import-time effects. Then Resolve source import import threading; preserve alias and import-time effects.
// Source: vvaharness/backends/llm/cli/session.py:21-25
In source order: Resolve source import import time; preserve alias and import-time effects. Then Resolve source import import uuid; preserve alias and import-time effects. Then Resolve source import from collections.abc import Sequence; preserve alias and import-time effects. Then Resolve source import from dataclasses import dataclass; preserve alias and import-time effects. Then Resolve source import from typing import Final; preserve alias and import-time effects.
// Source: vvaharness/backends/llm/cli/session.py:27-34
In source order: Resolve source import from vvaharness.backends.harness.deepagents.limits import MODEL_MAX_OUTPUT_TOKENS; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.models import CallTimeoutError, SessionNotResumableError; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm.cli import cancel as _cancel; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm.cli import discovery as _discovery; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm.cli import env as _env; preserve alias and import-time effects.
// Source: vvaharness/backends/llm/cli/session.py:35-45
In source order: Resolve source import from vvaharness.backends.llm.cli import envelope as _envelope; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm.cli import process as _process; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm.cli import retry as _retry; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm.models import ClockKind, call_timeout_error, effort_scaled_seconds, note_budget_use, truncation_retry_max; preserve alias and import-time effects. Then Resolve source import from vvaharness.report.redact import redact; preserve alias and import-time effects.
// Source: vvaharness/backends/llm/cli/session.py:46-50
In source order: Resolve source import from vvaharness.util import console, logs; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import errlog as _errlog; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.counters import COUNTERS; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.events import Event; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.git_paths import git_dir_spellings; preserve alias and import-time effects.
// Source: vvaharness/backends/llm/cli/session.py:51-57
In source order: Resolve source import from vvaharness.util.tokens import TOKENS; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.warn_once import warn_once; preserve alias and import-time effects. Then Evaluate once logs.get_logger(__name__); assign in source target order to log. Then For _WARNED_CAPS, assign set(); source annotation set[str].
// Source: vvaharness/backends/llm/cli/session.py:61-70
// Source: vvaharness/backends/llm/cli/session.py:60-60
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass.
// Source: vvaharness/backends/llm/cli/session.py:61-70
interface _CliPin {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/llm/cli/session.py:62-67
  In source order: Retain source documentation literal source_literal_62_4; it is not a model call. Then For cmd, declare without assigning a value; source annotation list[str]. Then For model, declare without assigning a value; source annotation str. Then For cwd, declare without assigning a value; source annotation str. Then For env, declare without assigning a value; source annotation dict | None.
  // Source: vvaharness/backends/llm/cli/session.py:68-70
  In source order: For json_schema, declare without assigning a value; source annotation dict | None. Then For tier, declare without assigning a value; source annotation str | None. Then For exited, declare without assigning a value; source annotation threading.Event.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vvaharness/backends/llm/cli/session.py:74-90
In source order: For _PINNED_CLI, assign {}; source annotation dict[str, _CliPin]. Then Evaluate once threading.Lock(); assign in source target order to _PINNED_CLI_LOCK. Then For _RESUME_EXIT_GRACE_S, assign 5; source annotation Final. Then For _READ_DENY_DIRS, assign ('.git', '.hg', '.svn', 'checkpoints', 'security-scan'); source annotation Final[tuple[str, ...]]. Then For _GIT_WRITE_DENY_RULES, assign tuple((source_template_86_4 for d in git_dir_spellings() for tool in ('Edit', 'Write') for where in ('./', '**/') for tail in ('', '/**'))); source annotation Final[tuple[str, ...]].
// Source: vvaharness/backends/llm/cli/session.py:93-93
In source order: For _AGENTIC_TIMEOUT, assign 3600; source annotation Final.
// Source: vvaharness/backends/llm/cli/session.py:96-140
interface _TurnWatchdog {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/llm/cli/session.py:97-97
  In source order: Retain source documentation literal source_literal_97_4; it is not a model call.
  // Source: vvaharness/backends/llm/cli/session.py:102-108
  // Source signature: __init__(self, cap: int, *, by_message: bool=False) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self, cap, by_message) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/llm/cli/session.py:103-107
    In source order: Evaluate once cap; assign in source target order to self.cap. Then Evaluate once by_message; assign in source target order to self.by_message. Then Evaluate once 0; assign in source target order to self.seen. Then Evaluate once False; assign in source target order to self.tripped. Then Evaluate once cap + 1 if by_message else cap; assign in source target order to self._trip_at.
    // Source: vvaharness/backends/llm/cli/session.py:108-108
    In source order: For self._ids, assign set(); source annotation set[str].
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/llm/cli/session.py:110-119
  // Source signature: _counts(self, evt: dict) -> bool
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _counts(self, evt) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/llm/cli/session.py:111-113
    In source order: Retain source documentation literal source_literal_111_8; it is not a model call. Then Evaluate once evt.get('message'); assign in source target order to msg. Then Evaluate once msg.get('id') if self.by_message and isinstance(msg, dict) else None; assign in source target order to msg_id.
    // Source: vvaharness/backends/llm/cli/session.py:114-115
    if (the source predicate not isinstance(msg_id, str) is truthy) {
      // Source: vvaharness/backends/llm/cli/session.py:115-115
      End this invocation with True.
    }
    // Source: vvaharness/backends/llm/cli/session.py:116-117
    if (the source predicate msg_id in self._ids is truthy) {
      // Source: vvaharness/backends/llm/cli/session.py:117-117
      End this invocation with False.
    }
    // Source: vvaharness/backends/llm/cli/session.py:118-118
    In source order: Evaluate self._ids.add(msg_id); retain side effects and discard the expression result.
    // Source: vvaharness/backends/llm/cli/session.py:119-119
    End this invocation with True.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/llm/cli/session.py:121-124
  // Source signature: describe(self) -> str
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn describe(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/llm/cli/session.py:122-123
    In source order: Retain source documentation literal source_literal_122_8; it is not a model call. Then Evaluate once ('messages', '>') if self.by_message else ('events', '>='); assign in source target order to (unit, op).
    // Source: vvaharness/backends/llm/cli/session.py:124-124
    End this invocation with source_template_124_15.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/llm/cli/session.py:126-140
  // Source signature: __call__(self, line: str) -> bool
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __call__(self, line) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/llm/cli/session.py:127-127
    In source order: Retain source documentation literal source_literal_127_8; it is not a model call.
    // Source: vvaharness/backends/llm/cli/session.py:128-129
    if (the source predicate self.tripped is truthy) {
      // Source: vvaharness/backends/llm/cli/session.py:129-129
      End this invocation with False.
    }
    // Source: vvaharness/backends/llm/cli/session.py:130-133
    Perform the following protected operations {
      // Source: vvaharness/backends/llm/cli/session.py:131-131
      In source order: Evaluate once json.loads(line); assign in source target order to evt.
    }
    // Source: vvaharness/backends/llm/cli/session.py:132-133
    On the first matching source exception (json.JSONDecodeError, TypeError), in handler order {
      // Source: vvaharness/backends/llm/cli/session.py:133-133
      End this invocation with False.
    }
    // Source: vvaharness/backends/llm/cli/session.py:134-135
    if (the source predicate not isinstance(evt, dict) or evt.get('type') != 'assistant' or (not self._counts(evt)) is truthy) {
      // Source: vvaharness/backends/llm/cli/session.py:135-135
      End this invocation with False.
    }
    // Source: vvaharness/backends/llm/cli/session.py:136-136
    In source order: Apply source augmented assignment self.seen += 1 with source evaluation/in-place semantics.
    // Source: vvaharness/backends/llm/cli/session.py:137-139
    if (the source predicate self.seen >= self._trip_at is truthy) {
      // Source: vvaharness/backends/llm/cli/session.py:138-138
      In source order: Evaluate once True; assign in source target order to self.tripped.
      // Source: vvaharness/backends/llm/cli/session.py:139-139
      End this invocation with True.
    }
    // Source: vvaharness/backends/llm/cli/session.py:140-140
    End this invocation with False.
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vvaharness/backends/llm/cli/session.py:145-149
In source order: Evaluate once source_literal_146_4; assign in source target order to _FINAL_ANSWER_INSTRUCTION.
// Source: vvaharness/backends/llm/cli/session.py:152-190
// Source signature: _finalize_via_resume(session_id: str, *, model: str, cwd: str, timeout: int, tag: str | None, env: dict | None=None, json_schema: dict | None=None, instruction: str=_FINAL_ANSWER_INSTRUCTION, fail_detail: dict | None=None) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _finalize_via_resume(session_id, model, cwd, timeout, tag, env, json_schema, instruction, fail_detail) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli/session.py:158-162
  In source order: Retain source documentation literal source_literal_158_4; it is not a model call.
  // Source: vvaharness/backends/llm/cli/session.py:163-164
  if (the source predicate fail_detail is None is truthy) {
    // Source: vvaharness/backends/llm/cli/session.py:164-164
    In source order: Evaluate once {}; assign in source target order to fail_detail.
  }
  // Source: vvaharness/backends/llm/cli/session.py:165-166
  In source order: Evaluate once [*_discovery._CLAUDE_CMD, '-p', '--resume', session_id, '--model', model, '--tools', '', '--output-format', 'json']; assign in source target order to cmd.
  // Source: vvaharness/backends/llm/cli/session.py:168-169
  if (the source predicate json_schema and _discovery._cli_capabilities()['json_schema'] is truthy) {
    // Source: vvaharness/backends/llm/cli/session.py:169-169
    In source order: Apply source augmented assignment cmd += ['--json-schema', json.dumps(json_schema)] with source evaluation/in-place semantics.
  }
  // Source: vvaharness/backends/llm/cli/session.py:170-171
  In source order: Apply source augmented assignment cmd += _confinement_argv(allowed_tools=None, disallowed_tools=None, permission_prompts=None) with source evaluation/in-place semantics.
  // Source: vvaharness/backends/llm/cli/session.py:172-176
  Perform the following protected operations {
    // Source: vvaharness/backends/llm/cli/session.py:173-173
    In source order: Evaluate once _process._run(cmd, input=instruction, cwd=cwd, timeout=timeout, env=env); assign in source target order to result.
  }
  // Source: vvaharness/backends/llm/cli/session.py:174-176
  On the first matching source exception Exception as exc, in handler order {
    // Source: vvaharness/backends/llm/cli/session.py:175-175
    In source order: Evaluate once type(exc).__name__; assign in source target order to fail_detail['cause'].
    // Source: vvaharness/backends/llm/cli/session.py:176-176
    End this invocation with None.
  }
  // Source: vvaharness/backends/llm/cli/session.py:177-184
  if (the source predicate result.returncode != 0 is truthy) {
    // Source: vvaharness/backends/llm/cli/session.py:181-183
    In source order: Evaluate _envelope._raise_if_refused_exit(result.stdout, tag=tag); retain side effects and discard the expression result. Then Evaluate once result.returncode; assign in source target order to fail_detail['rc']. Then Evaluate once result.stderr; assign in source target order to fail_detail['stderr'].
    // Source: vvaharness/backends/llm/cli/session.py:184-184
    End this invocation with None.
  }
  // Source: vvaharness/backends/llm/cli/session.py:185-189
  In source order: Evaluate once _envelope._parse_envelope(result.stdout); assign in source target order to text. Then Evaluate _envelope._note_unparsed_cache_keys(text.usage); retain side effects and discard the expression result. Then Evaluate TOKENS.add(text.usage, usd=text.usd, turns=text.turns); retain side effects and discard the expression result. Then Evaluate _envelope._raise_if_refused(text.stop_reason, tag=tag, stdout=result.stdout); retain side effects and discard the expression result.
  // Source: vvaharness/backends/llm/cli/session.py:190-190
  End this invocation with text.text or None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cli/session.py:193-212
// Source signature: _recover_timed_out_session(*, session_id: str, model: str, cwd: str, wall_clock: int, tag: str | None, env: dict | None=None, json_schema: dict | None=None) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _recover_timed_out_session(session_id, model, cwd, wall_clock, tag, env, json_schema) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli/session.py:197-203
  In source order: Retain source documentation literal source_literal_197_4; it is not a model call. Then Evaluate once source_template_198_14 if tag else ''; assign in source target order to tag_sfx. Then Evaluate console.write(source_template_199_18); retain side effects and discard the expression result. Then Evaluate once _finalize_via_resume(session_id, model=model, cwd=cwd, timeout=min(300, wall_clock), tag=tag, env=env, json_schema=json_schema); assign in source target order to final.
  // Source: vvaharness/backends/llm/cli/session.py:204-205
  if (the source predicate final is None is truthy) {
    // Source: vvaharness/backends/llm/cli/session.py:205-205
    End this invocation with None.
  }
  // Source: vvaharness/backends/llm/cli/session.py:206-211
  In source order: Evaluate COUNTERS.bump('cli_timeout_finalized'); retain side effects and discard the expression result. Then Evaluate _errlog.log(tag or 'cli', tag or 'timeout', source_template_209_8, error_code=CallTimeoutError.error_code, recovered=True); retain side effects and discard the expression result.
  // Source: vvaharness/backends/llm/cli/session.py:212-212
  End this invocation with final.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cli/session.py:215-218
// Source signature: release_pinned_session(stage_id: str) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn release_pinned_session(stage_id) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli/session.py:216-216
  In source order: Retain source documentation literal source_literal_216_4; it is not a model call.
  // Source: vvaharness/backends/llm/cli/session.py:217-218
  Enter source context managers left-to-right: _PINNED_CLI_LOCK {
    // Source: vvaharness/backends/llm/cli/session.py:218-218
    In source order: Evaluate _PINNED_CLI.pop(stage_id, None); retain side effects and discard the expression result.
  }
  Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cli/session.py:221-228
// Source signature: _resume_fail_detail(fail_detail: dict) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _resume_fail_detail(fail_detail) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli/session.py:222-222
  In source order: Retain source documentation literal source_literal_222_4; it is not a model call.
  // Source: vvaharness/backends/llm/cli/session.py:223-225
  if (the source predicate 'rc' in fail_detail is truthy) {
    // Source: vvaharness/backends/llm/cli/session.py:224-225
    End this invocation with source_template_224_16.
  }
  // Source: vvaharness/backends/llm/cli/session.py:226-227
  if (the source predicate 'cause' in fail_detail is truthy) {
    // Source: vvaharness/backends/llm/cli/session.py:227-227
    End this invocation with source_template_227_15.
  }
  // Source: vvaharness/backends/llm/cli/session.py:228-228
  End this invocation with ''.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cli/session.py:231-258
// Source signature: resume_agentic(session_id: str, instruction: str, *, timeout: float | None, tag: str | None) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn resume_agentic(session_id, instruction, timeout, tag) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli/session.py:233-233
  In source order: Retain source documentation literal source_literal_233_4; it is not a model call.
  // Source: vvaharness/backends/llm/cli/session.py:234-235
  Enter source context managers left-to-right: _PINNED_CLI_LOCK {
    // Source: vvaharness/backends/llm/cli/session.py:235-235
    In source order: Evaluate once _PINNED_CLI.get(session_id); assign in source target order to pin.
  }
  Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
  // Source: vvaharness/backends/llm/cli/session.py:236-238
  if (the source predicate pin is None is truthy) {
    // Source: vvaharness/backends/llm/cli/session.py:237-238
    Raise SessionNotResumableError(source_template_238_12).
  }
  // Source: vvaharness/backends/llm/cli/session.py:240-242
  if (the source predicate not _discovery._cli_capabilities().get('resume', False) is truthy) {
    // Source: vvaharness/backends/llm/cli/session.py:241-242
    Raise SessionNotResumableError(source_template_242_12).
  }
  // Source: vvaharness/backends/llm/cli/session.py:244-246
  if (the source predicate not pin.exited.wait(_RESUME_EXIT_GRACE_S) is truthy) {
    // Source: vvaharness/backends/llm/cli/session.py:245-246
    Raise SessionNotResumableError(source_template_246_12).
  }
  // Source: vvaharness/backends/llm/cli/session.py:248-254
  In source order: Evaluate once timeout if timeout is not None and timeout > 0 else _AGENTIC_TIMEOUT; assign in source target order to raw. Then Evaluate once effort_scaled_seconds(raw, pin.tier, kind=ClockKind.SESSION); assign in source target order to budget. Then Evaluate once pin.cmd[pin.cmd.index('--session-id') + 1]; assign in source target order to live_id. Then For fail_detail, assign {}; source annotation dict. Then Evaluate once _finalize_via_resume(live_id, model=pin.model, cwd=pin.cwd, timeout=budget, tag=tag, env=pin.env, json_schema=pin.json_schema, instruction=instruction, fail_detail=fail_detail); assign in source target order to final.
  // Source: vvaharness/backends/llm/cli/session.py:255-257
  if (the source predicate final is None is truthy) {
    // Source: vvaharness/backends/llm/cli/session.py:256-257
    Raise SessionNotResumableError(source_template_257_12).
  }
  // Source: vvaharness/backends/llm/cli/session.py:258-258
  End this invocation with final.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cli/session.py:261-268
// Source signature: _bare_tool_names(allowed_tools: Sequence[str] | None) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _bare_tool_names(allowed_tools) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli/session.py:262-263
  In source order: Retain source documentation literal source_literal_262_4; it is not a model call. Then For out, assign []; source annotation list[str].
  // Source: vvaharness/backends/llm/cli/session.py:264-267
  for each raw in allowed_tools or () {
    // Source: vvaharness/backends/llm/cli/session.py:265-265
    In source order: Evaluate once str(raw).split('(', 1)[0].strip(); assign in source target order to bare.
    // Source: vvaharness/backends/llm/cli/session.py:266-267
    if (the source predicate bare and bare not in out is truthy) {
      // Source: vvaharness/backends/llm/cli/session.py:267-267
      In source order: Evaluate out.append(bare); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/backends/llm/cli/session.py:268-268
  End this invocation with out.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cli/session.py:271-320
// Source signature: _confinement_argv(*, allowed_tools, disallowed_tools, permission_prompts: str | None) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _confinement_argv(allowed_tools, disallowed_tools, permission_prompts) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli/session.py:273-276
  In source order: Retain source documentation literal source_literal_273_4; it is not a model call. Then Evaluate once _discovery._cli_capabilities(); assign in source target order to caps. Then For argv, assign []; source annotation list[str].
  // Source: vvaharness/backends/llm/cli/session.py:278-284
  // Source signature: _gate(cap: str, flags: list[str], lost: str) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _gate(cap, flags, lost) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/llm/cli/session.py:279-281
    if (the source predicate caps.get(cap) is truthy) {
      // Source: vvaharness/backends/llm/cli/session.py:280-280
      In source order: Evaluate argv.extend(flags); retain side effects and discard the expression result.
      // Source: vvaharness/backends/llm/cli/session.py:281-281
      End this invocation with None.
    }
    // Source: vvaharness/backends/llm/cli/session.py:282-284
    In source order: Evaluate warn_once(_WARNED_CAPS, cap, source_template_283_18); retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/llm/cli/session.py:286-286
  In source order: Evaluate once _bare_tool_names(allowed_tools); assign in source target order to native.
  // Source: vvaharness/backends/llm/cli/session.py:287-297
  if (the source predicate native is truthy) {
    // Source: vvaharness/backends/llm/cli/session.py:288-291
    In source order: Evaluate _gate('tools', ['--tools', ','.join(native)], source_literal_289_14); retain side effects and discard the expression result.
  }
  else {
    // Source: vvaharness/backends/llm/cli/session.py:292-297
    if (the source predicate allowed_tools is not None is truthy) {
      // Source: vvaharness/backends/llm/cli/session.py:294-297
      In source order: Evaluate _gate('tools', ['--tools', ''], source_literal_295_14); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/backends/llm/cli/session.py:299-301
  In source order: Evaluate once [*(str(t) for t in disallowed_tools or ()), *(source_template_300_14 for d in _READ_DENY_DIRS), *_GIT_WRITE_DENY_RULES]; assign in source target order to deny.
  // Source: vvaharness/backends/llm/cli/session.py:302-304
  if (the source predicate deny is truthy) {
    // Source: vvaharness/backends/llm/cli/session.py:303-304
    In source order: Evaluate _gate('disallowed_tools', ['--disallowedTools', *deny], source_template_304_14); retain side effects and discard the expression result.
  }
  // Source: vvaharness/backends/llm/cli/session.py:305-307
  if (the source predicate permission_prompts is truthy) {
    // Source: vvaharness/backends/llm/cli/session.py:306-307
    In source order: Evaluate _gate('permission_prompts', ['--permission-prompts', permission_prompts], 'an action that would raise a permission prompt is not auto-denied.'); retain side effects and discard the expression result.
  }
  // Source: vvaharness/backends/llm/cli/session.py:308-312
  if (the source predicate _env._cfg.get('restricted', True) is truthy) {
    // Source: vvaharness/backends/llm/cli/session.py:309-312
    In source order: Evaluate _gate('restricted', ['--restricted'], source_literal_310_14); retain side effects and discard the expression result.
  }
  // Source: vvaharness/backends/llm/cli/session.py:313-319
  In source order: Evaluate _gate('setting_sources', ['--setting-sources', 'user'], "the SCANNED repository's .claude/settings.json and .claude/commands are loaded into this session."); retain side effects and discard the expression result. Then Evaluate _gate('strict_mcp_config', ['--strict-mcp-config'], "the SCANNED repository's .mcp.json servers can be started on this host."); retain side effects and discard the expression result. Then Evaluate _gate('disable_slash_commands', ['--disable-slash-commands'], 'skills and slash commands remain loaded as prompt-injection surface.'); retain side effects and discard the expression result.
  // Source: vvaharness/backends/llm/cli/session.py:320-320
  End this invocation with argv.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cli/session.py:323-561
// Source signature: agentic(user_prompt: str, *, model: str, system_prompt: str | None=None, allowed_tools: list[str] | None=None, cwd: str, max_budget_usd: float | None=None, max_tokens: int | None=None, permission_mode: str='auto', max_turns: int | None=None, timeout: int | None=None, tag: str | None=None, stream_cb=None, json_schema: dict | None=None, disallowed_tools=None, permission_prompts: str | None=None, extra_tools=None, extra_dispatch=None, effort: str | None=None, session_id: str='') -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn agentic(user_prompt, model, system_prompt, allowed_tools, cwd, max_budget_usd, max_tokens, permission_mode, max_turns, timeout, tag, stream_cb, json_schema, disallowed_tools, permission_prompts, extra_tools, extra_dispatch, effort, session_id) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli/session.py:346-346
  In source order: Retain source documentation literal source_literal_346_4; it is not a model call.
  // Source: vvaharness/backends/llm/cli/session.py:348-352
  if (the source predicate extra_tools is truthy) {
    // Source: vvaharness/backends/llm/cli/session.py:349-352
    Raise NotImplementedError(source_literal_350_12).
  }
  // Source: vvaharness/backends/llm/cli/session.py:354-355
  if (the source predicate _cancel._ABORT.is_set() is truthy) {
    // Source: vvaharness/backends/llm/cli/session.py:355-355
    Raise RuntimeError('aborted by user (Ctrl-C)').
  }
  // Source: vvaharness/backends/llm/cli/session.py:356-356
  In source order: Evaluate once [*_discovery._CLAUDE_CMD, '-p', '--model', model, *_env._effort_argv(effort)]; assign in source target order to cmd.
  // Source: vvaharness/backends/llm/cli/session.py:358-360
  if (the source predicate system_prompt is truthy) {
    // Source: vvaharness/backends/llm/cli/session.py:360-360
    In source order: Apply source augmented assignment cmd += ['--system-prompt', system_prompt] with source evaluation/in-place semantics.
  }
  // Source: vvaharness/backends/llm/cli/session.py:361-363
  if (the source predicate allowed_tools is truthy) {
    // Source: vvaharness/backends/llm/cli/session.py:363-363
    In source order: Apply source augmented assignment cmd += ['--allowedTools'] + list(allowed_tools) with source evaluation/in-place semantics.
  }
  // Source: vvaharness/backends/llm/cli/session.py:364-372
  if (the source predicate json_schema is truthy) {
    // Source: vvaharness/backends/llm/cli/session.py:365-372
    if (the source predicate _discovery._cli_capabilities()['json_schema'] is truthy) {
      // Source: vvaharness/backends/llm/cli/session.py:367-367
      In source order: Apply source augmented assignment cmd += ['--json-schema', json.dumps(json_schema)] with source evaluation/in-place semantics.
    }
    else {
      // Source: vvaharness/backends/llm/cli/session.py:369-372
      In source order: Evaluate warn_once(_WARNED_CAPS, 'json_schema_agentic', source_literal_370_22); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/backends/llm/cli/session.py:373-375
  In source order: Apply source augmented assignment cmd += _confinement_argv(allowed_tools=allowed_tools, disallowed_tools=disallowed_tools, permission_prompts=permission_prompts) with source evaluation/in-place semantics.
  // Source: vvaharness/backends/llm/cli/session.py:377-378
  if (the source predicate max_budget_usd and _discovery._cli_capabilities().get('max_budget') is truthy) {
    // Source: vvaharness/backends/llm/cli/session.py:378-378
    In source order: Apply source augmented assignment cmd += ['--max-budget-usd', str(max_budget_usd)] with source evaluation/in-place semantics.
  }
  // Source: vvaharness/backends/llm/cli/session.py:379-379
  In source order: Evaluate once bool(max_turns) and bool(_discovery._cli_capabilities().get('max_turns')); assign in source target order to native_turn_cap.
  // Source: vvaharness/backends/llm/cli/session.py:380-381
  if (the source predicate native_turn_cap is truthy) {
    // Source: vvaharness/backends/llm/cli/session.py:381-381
    In source order: Apply source augmented assignment cmd += ['--max-turns', str(int(max_turns))] with source evaluation/in-place semantics.
  }
  // Source: vvaharness/backends/llm/cli/session.py:383-388
  In source order: Apply source augmented assignment cmd += ['--permission-mode', _discovery._safe_permission_mode(permission_mode)] with source evaluation/in-place semantics. Then Apply source augmented assignment cmd += ['--output-format', 'stream-json', '--verbose'] with source evaluation/in-place semantics. Then Evaluate once _env._effective_effort(effort); assign in source target order to tier. Then Evaluate once int(timeout) if timeout else _AGENTIC_TIMEOUT; assign in source target order to raw_wall_clock. Then Evaluate once effort_scaled_seconds(raw_wall_clock, tier, kind=ClockKind.SESSION); assign in source target order to wall_clock.
  // Source: vvaharness/backends/llm/cli/session.py:390-397
  In source order: Evaluate once int(max_turns) if max_turns and (not native_turn_cap) else None; assign in source target order to watchdog_cap. Then Evaluate once allowed_tools is not None and (not _bare_tool_names(allowed_tools)); assign in source target order to by_message. Then Evaluate once wall_clock / raw_wall_clock; assign in source target order to _factor. Then Evaluate once source_template_395_18 if _factor != 1.0 else ''; assign in source target order to _factor_sfx. Then Evaluate once source_template_397_14 if tag else ''; assign in source target order to tag_sfx.
  // Source: vvaharness/backends/llm/cli/session.py:398-408
  In source order: Evaluate console.write(source_template_398_18); retain side effects and discard the expression result. Then Evaluate once 0; assign in source target order to pending_attempt. Then Evaluate once 0; assign in source target order to trunc_retried. Then Evaluate once _env._call_env(max_tokens=max_tokens, effort=effort); assign in source target order to env. Then Evaluate once False; assign in source target order to timeout_retried.
  // Source: vvaharness/backends/llm/cli/session.py:410-410
  In source order: Evaluate once False; assign in source target order to pin_released.
  // Source: vvaharness/backends/llm/cli/session.py:411-561
  while (the source predicate True is truthy) {
    // Source: vvaharness/backends/llm/cli/session.py:414-417
    In source order: Evaluate once str(uuid.uuid4()); assign in source target order to cli_session_id. Then Evaluate once [*cmd, '--session-id', cli_session_id]; assign in source target order to attempt_cmd. Then Evaluate once _TurnWatchdog(watchdog_cap, by_message=by_message) if watchdog_cap else None; assign in source target order to watchdog.
    // Source: vvaharness/backends/llm/cli/session.py:419-425
    if (the source predicate session_id and (not pin_released) is truthy) {
      // Source: vvaharness/backends/llm/cli/session.py:422-425
      Enter source context managers left-to-right: _PINNED_CLI_LOCK {
        // Source: vvaharness/backends/llm/cli/session.py:423-425
        In source order: Evaluate once _CliPin(cmd=attempt_cmd, model=model, cwd=cwd, env=env, json_schema=json_schema, tier=tier, exited=threading.Event()); assign in source target order to _PINNED_CLI[session_id].
      }
      Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    }
    // Source: vvaharness/backends/llm/cli/session.py:427-428
    In source order: Evaluate once time.monotonic(); assign in source target order to _attempt_start. Then For timed_out, assign None; source annotation subprocess.TimeoutExpired | None.
    // Source: vvaharness/backends/llm/cli/session.py:429-454
    Perform the following protected operations {
      // Source: vvaharness/backends/llm/cli/session.py:430-442
      In source order: Evaluate once _retry._run_with_retry(attempt_cmd, label=source_template_432_22, input=user_prompt, cwd=cwd, timeout=wall_clock, timeout_retries=0, env=env, heartbeat_label=None if stream_cb or watchdog else source_template_439_38, stream_cb=stream_cb, should_stop=watchdog); assign in source target order to result.
    }
    // Source: vvaharness/backends/llm/cli/session.py:443-444
    On the first matching source exception subprocess.TimeoutExpired as e, in handler order {
      // Source: vvaharness/backends/llm/cli/session.py:444-444
      In source order: Evaluate once e; assign in source target order to timed_out.
    }
    On every exit from this protected/handler/normal-completion region {
      // Source: vvaharness/backends/llm/cli/session.py:448-454
      if (the source predicate session_id is truthy) {
        // Source: vvaharness/backends/llm/cli/session.py:449-450
        Enter source context managers left-to-right: _PINNED_CLI_LOCK {
          // Source: vvaharness/backends/llm/cli/session.py:450-450
          In source order: Evaluate once _PINNED_CLI.get(session_id); assign in source target order to pin.
        }
        Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
        // Source: vvaharness/backends/llm/cli/session.py:451-454
        if (the source predicate pin is None is truthy) {
          // Source: vvaharness/backends/llm/cli/session.py:452-452
          In source order: Evaluate once True; assign in source target order to pin_released.
        }
        else {
          // Source: vvaharness/backends/llm/cli/session.py:454-454
          In source order: Evaluate pin.exited.set(); retain side effects and discard the expression result.
        }
      }
    }
    // Source: vvaharness/backends/llm/cli/session.py:455-455
    In source order: Evaluate once attempt_cmd[attempt_cmd.index('--session-id') + 1]; assign in source target order to session_id_live.
    // Source: vvaharness/backends/llm/cli/session.py:456-477
    if (the source predicate timed_out is not None is truthy) {
      // Source: vvaharness/backends/llm/cli/session.py:457-462
      if (the source predicate session_id is truthy) {
        // Source: vvaharness/backends/llm/cli/session.py:460-462
        Raise call_timeout_error(stage=tag or '', route='cli', budget_s=wall_clock, effort=tier, cause_text=source_template_462_31) with explicit source cause timed_out.
      }
      // Source: vvaharness/backends/llm/cli/session.py:467-469
      In source order: Evaluate once _recover_timed_out_session(session_id=session_id_live, model=model, cwd=cwd, wall_clock=wall_clock, tag=tag, env=env, json_schema=json_schema); assign in source target order to salvaged.
      // Source: vvaharness/backends/llm/cli/session.py:470-471
      if (the source predicate salvaged is not None is truthy) {
        // Source: vvaharness/backends/llm/cli/session.py:471-471
        End this invocation with _retry._accept_reply(salvaged, trunc_retried=trunc_retried).
      }
      // Source: vvaharness/backends/llm/cli/session.py:472-474
      if (the source predicate not timeout_retried is truthy) {
        // Source: vvaharness/backends/llm/cli/session.py:473-473
        In source order: Evaluate once True; assign in source target order to timeout_retried.
        // Source: vvaharness/backends/llm/cli/session.py:474-474
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/backends/llm/cli/session.py:475-477
      Raise call_timeout_error(stage=tag or '', route='cli', budget_s=wall_clock, effort=tier, cause_text=source_template_477_27) with explicit source cause timed_out.
    }
    // Source: vvaharness/backends/llm/cli/session.py:478-478
    In source order: Evaluate note_budget_use(time.monotonic() - _attempt_start, wall_clock, tier); retain side effects and discard the expression result.
    // Source: vvaharness/backends/llm/cli/session.py:481-507
    if (the source predicate watchdog is not None and _process._was_stopped(result) is truthy) {
      // Source: vvaharness/backends/llm/cli/session.py:482-484
      In source order: Evaluate console.write(source_template_482_26); retain side effects and discard the expression result. Then Evaluate COUNTERS.bump('cli_turn_watchdog_stops'); retain side effects and discard the expression result.
      // Source: vvaharness/backends/llm/cli/session.py:487-491
      if (the source predicate session_id is truthy) {
        // Source: vvaharness/backends/llm/cli/session.py:488-489
        Enter source context managers left-to-right: _PINNED_CLI_LOCK {
          // Source: vvaharness/backends/llm/cli/session.py:489-489
          In source order: Evaluate once _PINNED_CLI.get(session_id); assign in source target order to pin.
        }
        Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
        // Source: vvaharness/backends/llm/cli/session.py:490-491
        if (the source predicate pin is not None is truthy) {
          // Source: vvaharness/backends/llm/cli/session.py:491-491
          In source order: Evaluate pin.exited.clear(); retain side effects and discard the expression result.
        }
      }
      // Source: vvaharness/backends/llm/cli/session.py:492-501
      Perform the following protected operations {
        // Source: vvaharness/backends/llm/cli/session.py:493-495
        In source order: Evaluate once _finalize_via_resume(session_id_live, model=model, cwd=cwd, timeout=min(300, wall_clock), tag=tag, env=env, json_schema=json_schema); assign in source target order to final.
      }
      On every exit from this protected/handler/normal-completion region {
        // Source: vvaharness/backends/llm/cli/session.py:497-501
        if (the source predicate session_id is truthy) {
          // Source: vvaharness/backends/llm/cli/session.py:498-499
          Enter source context managers left-to-right: _PINNED_CLI_LOCK {
            // Source: vvaharness/backends/llm/cli/session.py:499-499
            In source order: Evaluate once _PINNED_CLI.get(session_id); assign in source target order to pin.
          }
          Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
          // Source: vvaharness/backends/llm/cli/session.py:500-501
          if (the source predicate pin is not None is truthy) {
            // Source: vvaharness/backends/llm/cli/session.py:501-501
            In source order: Evaluate pin.exited.set(); retain side effects and discard the expression result.
          }
        }
      }
      // Source: vvaharness/backends/llm/cli/session.py:502-503
      if (the source predicate final is truthy) {
        // Source: vvaharness/backends/llm/cli/session.py:503-503
        End this invocation with _retry._accept_reply(final, trunc_retried=trunc_retried).
      }
      // Source: vvaharness/backends/llm/cli/session.py:505-506
      In source order: Evaluate once _envelope._parse_envelope(result.stdout).text; assign in source target order to streamed. Then Evaluate log.warning(Event.CLI_RESUME_FAILED); retain side effects and discard the expression result.
      // Source: vvaharness/backends/llm/cli/session.py:507-507
      End this invocation with _retry._accept_reply(streamed, trunc_retried=trunc_retried).
    }
    // Source: vvaharness/backends/llm/cli/session.py:509-527
    if (the source predicate result.returncode != 0 is truthy) {
      // Source: vvaharness/backends/llm/cli/session.py:510-511
      In source order: Evaluate _envelope._raise_if_refused_exit(result.stdout, tag=tag); retain side effects and discard the expression result. Then Evaluate once _retry._truncation_cap(result); assign in source target order to cap.
      // Source: vvaharness/backends/llm/cli/session.py:512-515
      if (the source predicate cap is None is truthy) {
        // Source: vvaharness/backends/llm/cli/session.py:513-515
        Raise RuntimeError(_discovery._format_cli_error('claude CLI agentic failed', attempt_cmd, result)).
      }
      // Source: vvaharness/backends/llm/cli/session.py:516-518
      In source order: Evaluate once trunc_retried or max_tokens or cap; assign in source target order to requested. Then Evaluate once None if trunc_retried else truncation_retry_max(requested, cap=MODEL_MAX_OUTPUT_TOKENS); assign in source target order to retry_at.
      // Source: vvaharness/backends/llm/cli/session.py:519-525
      if (the source predicate retry_at is not None is truthy) {
        // Source: vvaharness/backends/llm/cli/session.py:520-524
        In source order: Evaluate _retry._log_truncation_retry(tag=tag, requested=requested, retry_at=retry_at, label='cli'); retain side effects and discard the expression result. Then Evaluate once dict(env or {}); assign in source target order to env. Then Evaluate once str(retry_at); assign in source target order to env['CLAUDE_CODE_MAX_OUTPUT_TOKENS']. Then Evaluate once retry_at; assign in source target order to trunc_retried.
        // Source: vvaharness/backends/llm/cli/session.py:525-525
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/backends/llm/cli/session.py:526-527
      Raise _retry._truncation_error(requested=requested, retried=trunc_retried, tag=tag, retry_at=retry_at).
    }
    // Source: vvaharness/backends/llm/cli/session.py:530-534
    In source order: Evaluate once result.stdout; assign in source target order to stdout. Then Evaluate once _envelope._parse_envelope(stdout); assign in source target order to (text, usage, turns, usd, stop_reason, model_usage). Then Evaluate _envelope._note_unparsed_cache_keys(usage); retain side effects and discard the expression result. Then Evaluate TOKENS.add(usage, usd=usd, turns=turns); retain side effects and discard the expression result. Then Evaluate _retry._log_usage(usage, stop_reason=stop_reason, model_usage=model_usage); retain side effects and discard the expression result.
    // Source: vvaharness/backends/llm/cli/session.py:535-535
    In source order: Evaluate _envelope._raise_if_refused(stop_reason, tag=tag, stdout=stdout); retain side effects and discard the expression result.
    // Source: vvaharness/backends/llm/cli/session.py:537-539
    if (the source predicate not _retry._is_pending_result(text) is truthy) {
      // Source: vvaharness/backends/llm/cli/session.py:539-539
      End this invocation with _retry._accept_reply(text, trunc_retried=trunc_retried).
    }
    // Source: vvaharness/backends/llm/cli/session.py:541-542
    In source order: Apply source augmented assignment pending_attempt += 1 with source evaluation/in-place semantics. Then Evaluate once redact((text or '').strip().replace(source_literal_542_54, ' '))[:200]; assign in source target order to snippet.
    // Source: vvaharness/backends/llm/cli/session.py:543-548
    if (the source predicate pending_attempt > _retry._PENDING_MAX_RETRIES is truthy) {
      // Source: vvaharness/backends/llm/cli/session.py:544-548
      Raise RuntimeError(source_template_545_16).
    }
    // Source: vvaharness/backends/llm/cli/session.py:549-555
    In source order: Evaluate once _retry._PENDING_BACKOFF[min(pending_attempt - 1, len(_retry._PENDING_BACKOFF) - 1)]; assign in source target order to wait. Then Evaluate console.write(source_template_552_12); retain side effects and discard the expression result. Then Evaluate once 0; assign in source target order to slept.
    // Source: vvaharness/backends/llm/cli/session.py:556-561
    while (the source predicate slept < wait is truthy) {
      // Source: vvaharness/backends/llm/cli/session.py:557-558
      if (the source predicate _cancel._ABORT.is_set() is truthy) {
        // Source: vvaharness/backends/llm/cli/session.py:558-558
        Raise RuntimeError('aborted by user (Ctrl-C)').
      }
      // Source: vvaharness/backends/llm/cli/session.py:559-561
      In source order: Evaluate once min(5, wait - slept); assign in source target order to step. Then Evaluate time.sleep(step); retain side effects and discard the expression result. Then Apply source augmented assignment slept += step with source evaluation/in-place semantics.
    }
  }
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.backends.harness.deepagents.limits import MODEL_MAX_OUTPUT_TOKENS` at source line 27: `source_detail/vvaharness/backends/harness/deepagents/limits.py.sudo.md`.
- `from vvaharness.backends.harness.models import CallTimeoutError, SessionNotResumableError` at source line 28: `source_detail/vvaharness/backends/harness/models.py.sudo.md`.
- `from vvaharness.backends.llm.cli import cancel as _cancel` at source line 32: `source_detail/vvaharness/backends/llm/cli/__init__.py.sudo.md`.
- `from vvaharness.backends.llm.cli import cancel as _cancel` at source line 32: `source_detail/vvaharness/backends/llm/cli/cancel.py.sudo.md`.
- `from vvaharness.backends.llm.cli import discovery as _discovery` at source line 33: `source_detail/vvaharness/backends/llm/cli/__init__.py.sudo.md`.
- `from vvaharness.backends.llm.cli import discovery as _discovery` at source line 33: `source_detail/vvaharness/backends/llm/cli/discovery.py.sudo.md`.
- `from vvaharness.backends.llm.cli import env as _env` at source line 34: `source_detail/vvaharness/backends/llm/cli/__init__.py.sudo.md`.
- `from vvaharness.backends.llm.cli import env as _env` at source line 34: `source_detail/vvaharness/backends/llm/cli/env.py.sudo.md`.
- `from vvaharness.backends.llm.cli import envelope as _envelope` at source line 35: `source_detail/vvaharness/backends/llm/cli/__init__.py.sudo.md`.
- `from vvaharness.backends.llm.cli import envelope as _envelope` at source line 35: `source_detail/vvaharness/backends/llm/cli/envelope.py.sudo.md`.
- `from vvaharness.backends.llm.cli import process as _process` at source line 36: `source_detail/vvaharness/backends/llm/cli/__init__.py.sudo.md`.
- `from vvaharness.backends.llm.cli import process as _process` at source line 36: `source_detail/vvaharness/backends/llm/cli/process.py.sudo.md`.
- `from vvaharness.backends.llm.cli import retry as _retry` at source line 37: `source_detail/vvaharness/backends/llm/cli/__init__.py.sudo.md`.
- `from vvaharness.backends.llm.cli import retry as _retry` at source line 37: `source_detail/vvaharness/backends/llm/cli/retry.py.sudo.md`.
- `from vvaharness.backends.llm.models import ClockKind, call_timeout_error, effort_scaled_seconds, note_budget_use, truncation_retry_max` at source line 38: `source_detail/vvaharness/backends/llm/models.py.sudo.md`.
- `from vvaharness.report.redact import redact` at source line 45: `source_detail/vvaharness/report/redact.py.sudo.md`.
- `from vvaharness.util import console, logs` at source line 46: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import console, logs` at source line 46: `source_detail/vvaharness/util/console.py.sudo.md`.
- `from vvaharness.util import console, logs` at source line 46: `source_detail/vvaharness/util/logs.py.sudo.md`.
- `from vvaharness.util import errlog as _errlog` at source line 47: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import errlog as _errlog` at source line 47: `source_detail/vvaharness/util/errlog.py.sudo.md`.
- `from vvaharness.util.counters import COUNTERS` at source line 48: `source_detail/vvaharness/util/counters.py.sudo.md`.
- `from vvaharness.util.events import Event` at source line 49: `source_detail/vvaharness/util/events.py.sudo.md`.
- `from vvaharness.util.git_paths import git_dir_spellings` at source line 50: `source_detail/vvaharness/util/git_paths.py.sudo.md`.
- `from vvaharness.util.tokens import TOKENS` at source line 51: `source_detail/vvaharness/util/tokens.py.sudo.md`.
- `from vvaharness.util.warn_once import warn_once` at source line 52: `source_detail/vvaharness/util/warn_once.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../../prompt_representation/vvaharness/backends/llm/cli/session.py.sudo.md). Exact strings in the evidence asset support this conversion.
