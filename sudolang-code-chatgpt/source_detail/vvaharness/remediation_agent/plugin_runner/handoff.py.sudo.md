# vvaharness/remediation_agent/plugin_runner/handoff.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/remediation_agent/plugin_runner/handoff.py.evidence.json`. SHA-256: `4c51980f154704535fb4da44fa253549f8a46675b5ff1c4a287b52f8fd1fddad`.

```sudo
// Source: vvaharness/remediation_agent/plugin_runner/handoff.py:15-20
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import logs; preserve alias and import-time effects. Then Resolve source import import json; preserve alias and import-time effects. Then Resolve source import from collections.abc import Awaitable, Callable, Mapping, Sequence; preserve alias and import-time effects.
// Source: vvaharness/remediation_agent/plugin_runner/handoff.py:21-27
In source order: Resolve source import from typing import Any; preserve alias and import-time effects. Then Resolve source import from langchain.agents.middleware.types import AgentMiddleware, ToolCallRequest; preserve alias and import-time effects. Then Resolve source import from langchain_core.messages import ToolMessage; preserve alias and import-time effects. Then Resolve source import from langgraph.types import Command; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.models import FixerResult; preserve alias and import-time effects.
// Source: vvaharness/remediation_agent/plugin_runner/handoff.py:28-34
In source order: Resolve source import from vvaharness.util import console; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.events import Event; preserve alias and import-time effects. Then Evaluate once logs.get_logger(__name__); assign in source target order to log. Then Evaluate once 'task'; assign in source target order to _TASK_TOOL. Then Evaluate once 'fixer'; assign in source target order to _FIXER.
// Source: vvaharness/remediation_agent/plugin_runner/handoff.py:35-40
In source order: Evaluate once ('VULNERABILITY CONTEXT:', 'TARGET FILES:', 'EDIT INSTRUCTIONS:', 'SUCCESS CRITERIA:'); assign in source target order to _REQUIRED_SECTIONS.
// Source: vvaharness/remediation_agent/plugin_runner/handoff.py:43-193
interface FixerDispatchGuard {
  Describe the source Python type, preserving its base/metaclass expression order: AgentMiddleware.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:44-44
  In source order: Retain source documentation literal source_literal_44_4; it is not a model call.
  // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:46-53
  // Source signature: __init__(self, *, finding_context: str, primary_file: str='') -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self, finding_context, primary_file) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:47-51
    In source order: Evaluate super().__init__(); retain side effects and discard the expression result. Then Evaluate once finding_context; assign in source target order to self._finding_context. Then Evaluate once primary_file; assign in source target order to self._primary_file. Then Evaluate once 0; assign in source target order to self._attempts. Then Evaluate once False; assign in source target order to self._retry_allowed.
    // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:52-53
    In source order: Evaluate once False; assign in source target order to self._terminal. Then Evaluate once 0; assign in source target order to self._malformed_rejections.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:55-62
  // Source signature: _refusal(self, request: ToolCallRequest, detail: str) -> ToolMessage
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _refusal(self, request, detail) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:56-56
    In source order: Evaluate log.warning(Event.FIXER_DISPATCH_REFUSED, detail=detail); retain side effects and discard the expression result.
    // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:57-62
    End this invocation with ToolMessage(content=source_template_58_20, name=_TASK_TOOL, tool_call_id=request.tool_call.get('id') or '', status='error').
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:64-112
  // Source signature: _prepare(self, request: ToolCallRequest) -> ToolCallRequest | ToolMessage
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _prepare(self, request) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:65-65
    In source order: Evaluate once request.tool_call; assign in source target order to call.
    // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:66-67
    if (the source predicate call.get('name') != _TASK_TOOL is truthy) {
      // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:67-67
      End this invocation with request.
    }
    // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:68-68
    In source order: Evaluate once call.get('args'); assign in source target order to args.
    // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:69-71
    if (the source predicate not isinstance(args, Mapping) is truthy) {
      // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:70-70
      In source order: Evaluate once True; assign in source target order to self._terminal.
      // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:71-71
      End this invocation with self._refusal(request, 'task arguments were not an object; return Not Fixed').
    }
    // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:72-74
    if (the source predicate args.get('subagent_type') != _FIXER is truthy) {
      // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:73-73
      In source order: Evaluate once True; assign in source target order to self._terminal.
      // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:74-74
      End this invocation with self._refusal(request, "S10 permits only subagent_type='fixer'").
    }
    // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:75-77
    if (the source predicate self._terminal is truthy) {
      // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:76-77
      End this invocation with self._refusal(request, 'the fixer already returned a completed result; do not retry').
    }
    // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:78-80
    if (the source predicate self._attempts and (not self._retry_allowed) is truthy) {
      // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:79-80
      End this invocation with self._refusal(request, 'a retry is allowed only after an explicit transient tool error').
    }
    // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:82-83
    In source order: Evaluate once args.get('description'); assign in source target order to description. Then Evaluate once _invalid_spec(description, self._primary_file); assign in source target order to problem.
    // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:84-96
    if (the source predicate problem is truthy) {
      // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:86-86
      In source order: Apply source augmented assignment self._malformed_rejections += 1 with source evaluation/in-place semantics.
      // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:87-92
      if (the source predicate self._malformed_rejections >= 2 is truthy) {
        // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:88-88
        In source order: Evaluate once True; assign in source target order to self._terminal.
        // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:89-92
        End this invocation with self._refusal(request, source_template_91_20).
      }
      // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:93-96
      End this invocation with self._refusal(request, source_template_95_16).
    }
    // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:97-97
    Enforce source assert isinstance(description, str); retain Python optimization-dependent assert behavior.
    // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:99-111
    In source order: Apply source augmented assignment self._attempts += 1 with source evaluation/in-place semantics. Then Evaluate once False; assign in source target order to self._retry_allowed. Then Evaluate once source_template_102_12; assign in source target order to enriched. Then Evaluate once {**args, 'description': enriched}; assign in source target order to amended_args. Then Evaluate console.write(source_template_109_12); retain side effects and discard the expression result.
    // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:112-112
    End this invocation with request.override(tool_call={**call, 'args': amended_args}).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:114-133
  // Source signature: _observe(self, result: ToolMessage | Command[Any]) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _observe(self, result) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:115-115
    In source order: Evaluate once _result_message(result); assign in source target order to message.
    // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:116-118
    if (the source predicate message is None is truthy) {
      // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:117-117
      In source order: Evaluate once True; assign in source target order to self._terminal.
      // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:118-118
      End this invocation with None.
    }
    // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:119-121
    if (the source predicate getattr(message, 'status', 'success') == 'error' is truthy) {
      // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:120-120
      In source order: Evaluate self._record_transient(); retain side effects and discard the expression result.
      // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:121-121
      End this invocation with None.
    }
    // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:122-122
    In source order: Evaluate once _fixer_result(message.content); assign in source target order to parsed.
    // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:123-125
    if (the source predicate parsed is not None and parsed.status == 'tool_error' and parsed.retryable is truthy) {
      // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:124-124
      In source order: Evaluate self._record_transient(); retain side effects and discard the expression result.
      // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:125-125
      End this invocation with None.
    }
    // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:127-127
    In source order: Evaluate once True; assign in source target order to self._terminal.
    // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:128-133
    if (the source predicate parsed is None is truthy) {
      // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:129-131
      In source order: Evaluate log.warning('fixer returned an invalid result; no retry permitted'); retain side effects and discard the expression result.
    }
    else {
      // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:132-133
      if (the source predicate parsed.status != 'applied' is truthy) {
        // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:133-133
        In source order: Evaluate log.warning(Event.FIXER_STATUS_NO_RETRY, status=parsed.status); retain side effects and discard the expression result.
      }
    }
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:135-145
  // Source signature: _record_transient(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _record_transient(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:136-145
    if (the source predicate self._attempts < 2 is truthy) {
      // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:137-140
      In source order: Evaluate once True; assign in source target order to self._retry_allowed. Then Evaluate log.warning('fixer reported a transient tool error — one retry is permitted'); retain side effects and discard the expression result.
    }
    else {
      // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:142-145
      In source order: Evaluate once True; assign in source target order to self._terminal. Then Evaluate log.warning('fixer transient retry exhausted — return Not Fixed'); retain side effects and discard the expression result.
    }
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:147-169
  // Source signature: wrap_tool_call(self, request: ToolCallRequest, handler: Callable[[ToolCallRequest], ToolMessage | Command[Any]]) -> ToolMessage | Command[Any]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn wrap_tool_call(self, request, handler) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:152-152
    In source order: Retain source documentation literal source_literal_152_8; it is not a model call.
    // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:153-154
    if (the source predicate request.tool_call.get('name') != _TASK_TOOL is truthy) {
      // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:154-154
      End this invocation with handler(request).
    }
    // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:155-155
    In source order: Evaluate once self._prepare(request); assign in source target order to prepared.
    // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:156-157
    if (the source predicate isinstance(prepared, ToolMessage) is truthy) {
      // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:157-157
      End this invocation with prepared.
    }
    // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:158-166
    Perform the following protected operations {
      // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:159-159
      In source order: Evaluate once handler(prepared); assign in source target order to result.
    }
    // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:160-166
    On the first matching source exception Exception as exc, in handler order {
      // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:161-161
      In source order: Evaluate self._record_transient(); retain side effects and discard the expression result.
      // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:162-166
      End this invocation with self._refusal(request, source_template_164_16).
    }
    // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:167-168
    if (the source predicate request.tool_call.get('name') == _TASK_TOOL is truthy) {
      // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:168-168
      In source order: Evaluate self._observe(result); retain side effects and discard the expression result.
    }
    // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:169-169
    End this invocation with result.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:171-193
  // Source signature: awrap_tool_call(self, request: ToolCallRequest, handler: Callable[[ToolCallRequest], Awaitable[ToolMessage | Command[Any]]]) -> ToolMessage | Command[Any]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn awrap_tool_call(self, request, handler) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    This callable produces a coroutine or async generator; await/suspension positions remain in source expressions.
    // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:176-176
    In source order: Retain source documentation literal source_literal_176_8; it is not a model call.
    // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:177-178
    if (the source predicate request.tool_call.get('name') != _TASK_TOOL is truthy) {
      // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:178-178
      End this invocation with await handler(request).
    }
    // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:179-179
    In source order: Evaluate once self._prepare(request); assign in source target order to prepared.
    // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:180-181
    if (the source predicate isinstance(prepared, ToolMessage) is truthy) {
      // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:181-181
      End this invocation with prepared.
    }
    // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:182-190
    Perform the following protected operations {
      // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:183-183
      In source order: Evaluate once await handler(prepared); assign in source target order to result.
    }
    // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:184-190
    On the first matching source exception Exception as exc, in handler order {
      // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:185-185
      In source order: Evaluate self._record_transient(); retain side effects and discard the expression result.
      // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:186-190
      End this invocation with self._refusal(request, source_template_188_16).
    }
    // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:191-192
    if (the source predicate request.tool_call.get('name') == _TASK_TOOL is truthy) {
      // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:192-192
      In source order: Evaluate self._observe(result); retain side effects and discard the expression result.
    }
    // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:193-193
    End this invocation with result.
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vvaharness/remediation_agent/plugin_runner/handoff.py:196-223
// Source signature: _invalid_spec(description: object, primary_file: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _invalid_spec(description, primary_file) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:197-197
  In source order: Retain source documentation literal source_literal_197_4; it is not a model call.
  // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:198-199
  if (the source predicate not isinstance(description, str) or not description.strip() is truthy) {
    // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:199-199
    End this invocation with 'missing description'.
  }
  // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:200-203
  In source order: Evaluate once description.casefold(); assign in source target order to folded. Then Evaluate once [section.casefold() for section in _REQUIRED_SECTIONS]; assign in source target order to markers. Then Evaluate once [section for section, marker in zip(_REQUIRED_SECTIONS, markers) if marker not in folded]; assign in source target order to missing.
  // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:204-205
  if (the source predicate missing is truthy) {
    // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:205-205
    End this invocation with source_template_205_15.
  }
  // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:206-206
  In source order: Evaluate once [folded.index(marker) for marker in markers]; assign in source target order to positions.
  // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:207-208
  if (the source predicate positions != sorted(positions) is truthy) {
    // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:208-208
    End this invocation with 'required sections are out of order'.
  }
  // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:209-209
  In source order: For bodies, assign {}; source annotation dict[str, str].
  // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:210-215
  for each (index, (section, marker)) in enumerate(zip(_REQUIRED_SECTIONS, markers)) {
    // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:211-213
    In source order: Evaluate once positions[index] + len(marker); assign in source target order to start. Then Evaluate once positions[index + 1] if index + 1 < len(positions) else len(description); assign in source target order to end. Then Evaluate once description[start:end].strip(); assign in source target order to bodies[section].
    // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:214-215
    if (the source predicate not bodies[section] is truthy) {
      // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:215-215
      End this invocation with source_template_215_19.
    }
  }
  // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:216-216
  In source order: Evaluate once bodies['TARGET FILES:'].casefold(); assign in source target order to target_files.
  // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:217-218
  if (the source predicate primary_file and primary_file.casefold() not in target_files is truthy) {
    // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:218-218
    End this invocation with source_template_218_15.
  }
  // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:219-222
  for each section in ('VULNERABILITY CONTEXT:', 'EDIT INSTRUCTIONS:', 'SUCCESS CRITERIA:') {
    // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:221-222
    if (the source predicate len(bodies[section]) < 12 is truthy) {
      // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:222-222
      End this invocation with source_template_222_19.
    }
  }
  // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:223-223
  End this invocation with ''.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/plugin_runner/handoff.py:226-233
// Source signature: _result_message(result: ToolMessage | Command[Any]) -> ToolMessage | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _result_message(result) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:227-228
  if (the source predicate isinstance(result, ToolMessage) is truthy) {
    // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:228-228
    End this invocation with result.
  }
  // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:229-230
  In source order: Evaluate once getattr(result, 'update', None); assign in source target order to update. Then Evaluate once update.get('messages', []) if isinstance(update, Mapping) else []; assign in source target order to messages.
  // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:231-232
  if (the source predicate isinstance(messages, Sequence) is truthy) {
    // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:232-232
    End this invocation with next((m for m in reversed(messages) if isinstance(m, ToolMessage)), None).
  }
  // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:233-233
  End this invocation with None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/plugin_runner/handoff.py:236-242
// Source signature: _fixer_result(content: object) -> FixerResult | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _fixer_result(content) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:237-238
  if (the source predicate not isinstance(content, str) is truthy) {
    // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:238-238
    End this invocation with None.
  }
  // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:239-242
  Perform the following protected operations {
    // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:240-240
    End this invocation with FixerResult.model_validate(json.loads(content)).
  }
  // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:241-242
  On the first matching source exception (ValueError, TypeError, json.JSONDecodeError), in handler order {
    // Source: vvaharness/remediation_agent/plugin_runner/handoff.py:242-242
    End this invocation with None.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/plugin_runner/handoff.py:245-245
In source order: Evaluate once ['FixerDispatchGuard']; assign in source target order to __all__.
```

## Local import links

- `from vvaharness.util import logs` at source line 17: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import logs` at source line 17: `source_detail/vvaharness/util/logs.py.sudo.md`.
- `from vvaharness.remediation_agent.models import FixerResult` at source line 27: `source_detail/vvaharness/remediation_agent/models/__init__.py.sudo.md`.
- `from vvaharness.util import console` at source line 28: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import console` at source line 28: `source_detail/vvaharness/util/console.py.sudo.md`.
- `from vvaharness.util.events import Event` at source line 29: `source_detail/vvaharness/util/events.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../prompt_representation/vvaharness/remediation_agent/plugin_runner/handoff.py.sudo.md). Exact strings in the evidence asset support this conversion.
