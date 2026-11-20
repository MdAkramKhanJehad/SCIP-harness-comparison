# vvaharness/backends/llm/tool_adapter.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/backends/llm/tool_adapter.py.evidence.json`. SHA-256: `7b7dab400a62c95af804b6ba20f7c4519e1c90a690d896c5c09ae98a84858572`.

```sudo
// Source: vvaharness/backends/llm/tool_adapter.py:15-22
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import json; preserve alias and import-time effects. Then Resolve source import from dataclasses import dataclass, field; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects.
// Source: vvaharness/backends/llm/tool_adapter.py:23-29
In source order: Resolve source import from typing import TYPE_CHECKING, Any; preserve alias and import-time effects. Then Resolve source import from pydantic import ValidationError; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm import tools as _localtools; preserve alias and import-time effects. Then Resolve source import from vvaharness.report.redact import redact, redact_counts; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import console; preserve alias and import-time effects.
// Source: vvaharness/backends/llm/tool_adapter.py:30-32
In source order: Resolve source import from vvaharness.util.counters import COUNTERS; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.scan_progress import is_stage_only; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.warn_once import warn_once; preserve alias and import-time effects.
// Source: vvaharness/backends/llm/tool_adapter.py:34-35
if (the source predicate TYPE_CHECKING is truthy) {
  // Source: vvaharness/backends/llm/tool_adapter.py:35-35
  In source order: Resolve source import from collections.abc import Sequence; preserve alias and import-time effects.
}
// Source: vvaharness/backends/llm/tool_adapter.py:38-41
In source order: Evaluate once 'llm_adapter_evidence_gate_unenforced'; assign in source target order to EVIDENCE_UNENFORCED_COUNTER. Then For _WARNED, assign set(); source annotation set[str].
// Source: vvaharness/backends/llm/tool_adapter.py:44-55
// Source signature: _materialize(tool_builder: Any, *, model: str, cwd: str, fact_tools: Sequence[str]) -> list[Any]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _materialize(tool_builder, model, cwd, fact_tools) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/tool_adapter.py:46-49
  In source order: Retain source documentation literal source_literal_46_4; it is not a model call. Then Resolve source import from vvaharness.backends.harness import StreamingOptions; preserve alias and import-time effects. Then Evaluate once set(fact_tools); assign in source target order to wanted.
  // Source: vvaharness/backends/llm/tool_adapter.py:50-51
  if (the source predicate not wanted is truthy) {
    // Source: vvaharness/backends/llm/tool_adapter.py:51-51
    End this invocation with [].
  }
  // Source: vvaharness/backends/llm/tool_adapter.py:52-54
  In source order: Evaluate once StreamingOptions(model=model, cwd=Path(cwd), fact_tools=tuple(fact_tools)); assign in source target order to options. Then Evaluate once tool_builder(options, allowed_tools=()) or []; assign in source target order to built.
  // Source: vvaharness/backends/llm/tool_adapter.py:55-55
  End this invocation with [t for t in built if getattr(t, 'name', None) in wanted].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/tool_adapter.py:58-65
// Source signature: _tool_schema(langchain_tool: Any) -> dict[str, Any]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _tool_schema(langchain_tool) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/tool_adapter.py:59-64
  In source order: Retain source documentation literal source_literal_59_4; it is not a model call. Then Evaluate once dict(getattr(langchain_tool, 'args', None) or {}); assign in source target order to args. Then Evaluate once [name for name, spec in args.items() if isinstance(spec, dict) and 'default' not in spec]; assign in source target order to required.
  // Source: vvaharness/backends/llm/tool_adapter.py:65-65
  End this invocation with {'type': 'object', 'properties': args, 'required': required}.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/tool_adapter.py:68-73
// Source signature: _anthropic_schema(langchain_tool: Any) -> dict[str, Any]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _anthropic_schema(langchain_tool) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/tool_adapter.py:69-71
  In source order: Retain source documentation literal source_literal_69_4; it is not a model call. Then Evaluate once str(getattr(langchain_tool, 'name', '') or ''); assign in source target order to name. Then Evaluate once (getattr(langchain_tool, 'description', '') or '').strip(); assign in source target order to desc.
  // Source: vvaharness/backends/llm/tool_adapter.py:72-73
  End this invocation with {'name': name, 'description': desc or name, 'input_schema': _tool_schema(langchain_tool)}.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/tool_adapter.py:76-85
// Source signature: _budget_refusal(parent_middleware: Sequence[Any], name: str) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _budget_refusal(parent_middleware, name) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/tool_adapter.py:77-77
  In source order: Retain source documentation literal source_literal_77_4; it is not a model call.
  // Source: vvaharness/backends/llm/tool_adapter.py:78-84
  for each mw in parent_middleware or () {
    // Source: vvaharness/backends/llm/tool_adapter.py:79-79
    In source order: Evaluate once getattr(mw, 'refusal_for', None); assign in source target order to refusal.
    // Source: vvaharness/backends/llm/tool_adapter.py:80-81
    if (the source predicate refusal is None is truthy) {
      // Source: vvaharness/backends/llm/tool_adapter.py:81-81
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/backends/llm/tool_adapter.py:82-82
    In source order: Evaluate once refusal(name); assign in source target order to text.
    // Source: vvaharness/backends/llm/tool_adapter.py:83-84
    if (the source predicate text is truthy) {
      // Source: vvaharness/backends/llm/tool_adapter.py:84-84
      End this invocation with text.
    }
  }
  // Source: vvaharness/backends/llm/tool_adapter.py:85-85
  End this invocation with None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/tool_adapter.py:88-95
// Source signature: _required_fact_tools(parent_middleware: Sequence[Any]) -> frozenset[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _required_fact_tools(parent_middleware) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/tool_adapter.py:89-90
  In source order: Retain source documentation literal source_literal_89_4; it is not a model call. Then For required, assign set(); source annotation set[str].
  // Source: vvaharness/backends/llm/tool_adapter.py:91-94
  for each mw in parent_middleware or () {
    // Source: vvaharness/backends/llm/tool_adapter.py:92-92
    In source order: Evaluate once getattr(mw, 'required_tools', None); assign in source target order to names.
    // Source: vvaharness/backends/llm/tool_adapter.py:93-94
    if (the source predicate names is truthy) {
      // Source: vvaharness/backends/llm/tool_adapter.py:94-94
      In source order: Apply source augmented assignment required |= set(names) with source evaluation/in-place semantics.
    }
  }
  // Source: vvaharness/backends/llm/tool_adapter.py:95-95
  End this invocation with frozenset(required).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/tool_adapter.py:98-105
// Source signature: _serialize(result: object) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _serialize(result) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/tool_adapter.py:99-99
  In source order: Retain source documentation literal source_literal_99_4; it is not a model call.
  // Source: vvaharness/backends/llm/tool_adapter.py:100-101
  if (the source predicate isinstance(result, str) is truthy) {
    // Source: vvaharness/backends/llm/tool_adapter.py:101-101
    End this invocation with result.
  }
  // Source: vvaharness/backends/llm/tool_adapter.py:102-105
  Perform the following protected operations {
    // Source: vvaharness/backends/llm/tool_adapter.py:103-103
    End this invocation with json.dumps(result, default=str).
  }
  // Source: vvaharness/backends/llm/tool_adapter.py:104-105
  On the first matching source exception (TypeError, ValueError), in handler order {
    // Source: vvaharness/backends/llm/tool_adapter.py:105-105
    End this invocation with str(result).
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/tool_adapter.py:109-218
// Source: vvaharness/backends/llm/tool_adapter.py:108-108
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass.
// Source: vvaharness/backends/llm/tool_adapter.py:109-218
interface ToolStack {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/llm/tool_adapter.py:110-118
  In source order: Retain source documentation literal source_literal_110_4; it is not a model call. Then For schemas, declare without assigning a value; source annotation list[dict[str, Any]]. Then For names, declare without assigning a value; source annotation tuple[str, ...]. Then For required, assign frozenset(); source annotation frozenset[str]. Then For _tools, assign field(default_factory=dict); source annotation dict[str, Any].
  // Source: vvaharness/backends/llm/tool_adapter.py:119-120
  In source order: For _middleware, assign (); source annotation tuple[Any, ...]. Then For _called, assign field(default_factory=set); source annotation set[str].
  // Source: vvaharness/backends/llm/tool_adapter.py:123-132
  // Source: vvaharness/backends/llm/tool_adapter.py:122-122
  Before creating this callable, evaluate and retain decorators top-to-bottom: staticmethod.
  // Source: vvaharness/backends/llm/tool_adapter.py:123-132
  // Source signature: _validation_error(lc_tool: Any, args: dict[str, Any]) -> ValidationError | None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _validation_error(lc_tool, args) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/llm/tool_adapter.py:124-125
    In source order: Retain source documentation literal source_literal_124_8; it is not a model call. Then Evaluate once getattr(lc_tool, 'args_schema', None); assign in source target order to schema.
    // Source: vvaharness/backends/llm/tool_adapter.py:126-127
    if (the source predicate not hasattr(schema, 'model_validate') is truthy) {
      // Source: vvaharness/backends/llm/tool_adapter.py:127-127
      End this invocation with None.
    }
    // Source: vvaharness/backends/llm/tool_adapter.py:128-131
    Perform the following protected operations {
      // Source: vvaharness/backends/llm/tool_adapter.py:129-129
      In source order: Evaluate schema.model_validate(args or {}); retain side effects and discard the expression result.
    }
    // Source: vvaharness/backends/llm/tool_adapter.py:130-131
    On the first matching source exception ValidationError as exc, in handler order {
      // Source: vvaharness/backends/llm/tool_adapter.py:131-131
      End this invocation with exc.
    }
    // Source: vvaharness/backends/llm/tool_adapter.py:132-132
    End this invocation with None.
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vvaharness/backends/llm/tool_adapter.py:134-140
  // Source signature: _tool_fault(self, name: str, args: dict[str, Any], exc: Exception, *, tag: str | None) -> str
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _tool_fault(self, name, args, exc, tag) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/llm/tool_adapter.py:136-139
    In source order: Retain source documentation literal source_literal_136_8; it is not a model call. Then Evaluate COUNTERS.bump(source_template_137_22); retain side effects and discard the expression result. Then Evaluate once source_template_138_14; assign in source target order to err. Then Evaluate self._log_dispatch(name, args, err, tag=tag); retain side effects and discard the expression result.
    // Source: vvaharness/backends/llm/tool_adapter.py:140-140
    End this invocation with err.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/llm/tool_adapter.py:142-152
  // Source signature: _rejected(self, lc_tool: Any, name: str, args: dict[str, Any], *, tag: str | None) -> str | None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _rejected(self, lc_tool, name, args, tag) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/llm/tool_adapter.py:144-145
    In source order: Retain source documentation literal source_literal_144_8; it is not a model call. Then Evaluate once self._validation_error(lc_tool, args); assign in source target order to invalid.
    // Source: vvaharness/backends/llm/tool_adapter.py:146-147
    if (the source predicate invalid is not None is truthy) {
      // Source: vvaharness/backends/llm/tool_adapter.py:147-147
      End this invocation with self._tool_fault(name, args, invalid, tag=tag).
    }
    // Source: vvaharness/backends/llm/tool_adapter.py:148-148
    In source order: Evaluate once _budget_refusal(self._middleware, name); assign in source target order to refusal.
    // Source: vvaharness/backends/llm/tool_adapter.py:149-151
    if (the source predicate refusal is not None is truthy) {
      // Source: vvaharness/backends/llm/tool_adapter.py:150-150
      In source order: Evaluate self._log_dispatch(name, args, source_template_150_43, tag=tag); retain side effects and discard the expression result.
      // Source: vvaharness/backends/llm/tool_adapter.py:151-151
      End this invocation with refusal.
    }
    // Source: vvaharness/backends/llm/tool_adapter.py:152-152
    End this invocation with None.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/llm/tool_adapter.py:154-175
  // Source signature: dispatch(self, name: str, args: dict[str, Any], *, tag: str | None=None) -> str | None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn dispatch(self, name, args, tag) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/llm/tool_adapter.py:156-157
    In source order: Retain source documentation literal source_literal_156_8; it is not a model call. Then Evaluate once self._tools.get(name); assign in source target order to lc_tool.
    // Source: vvaharness/backends/llm/tool_adapter.py:158-159
    if (the source predicate lc_tool is None is truthy) {
      // Source: vvaharness/backends/llm/tool_adapter.py:159-159
      End this invocation with None.
    }
    // Source: vvaharness/backends/llm/tool_adapter.py:160-160
    In source order: Evaluate once self._rejected(lc_tool, name, args, tag=tag); assign in source target order to rejection.
    // Source: vvaharness/backends/llm/tool_adapter.py:161-162
    if (the source predicate rejection is not None is truthy) {
      // Source: vvaharness/backends/llm/tool_adapter.py:162-162
      End this invocation with rejection.
    }
    // Source: vvaharness/backends/llm/tool_adapter.py:163-163
    In source order: Evaluate self._called.add(name); retain side effects and discard the expression result.
    // Source: vvaharness/backends/llm/tool_adapter.py:164-167
    for each mw in self._middleware or () {
      // Source: vvaharness/backends/llm/tool_adapter.py:165-165
      In source order: Evaluate once getattr(mw, 'note_call', None); assign in source target order to note.
      // Source: vvaharness/backends/llm/tool_adapter.py:166-167
      if (the source predicate note is not None is truthy) {
        // Source: vvaharness/backends/llm/tool_adapter.py:167-167
        In source order: Evaluate note(name); retain side effects and discard the expression result.
      }
    }
    // Source: vvaharness/backends/llm/tool_adapter.py:168-171
    Perform the following protected operations {
      // Source: vvaharness/backends/llm/tool_adapter.py:169-169
      In source order: Evaluate once lc_tool.invoke(dict(args or {})); assign in source target order to result.
    }
    // Source: vvaharness/backends/llm/tool_adapter.py:170-171
    On the first matching source exception Exception as exc, in handler order {
      // Source: vvaharness/backends/llm/tool_adapter.py:171-171
      End this invocation with self._tool_fault(name, args, exc, tag=tag).
    }
    // Source: vvaharness/backends/llm/tool_adapter.py:172-174
    In source order: Evaluate once redact_counts(_serialize(result)); assign in source target order to (masked, _). Then Evaluate once _localtools.cap_tool_result(masked); assign in source target order to out. Then Evaluate self._log_dispatch(name, args, source_template_174_39, tag=tag); retain side effects and discard the expression result.
    // Source: vvaharness/backends/llm/tool_adapter.py:175-175
    End this invocation with out.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/llm/tool_adapter.py:177-182
  // Source signature: _log_dispatch(self, name: str, args: dict[str, Any], outcome: str, *, tag: str | None=None) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _log_dispatch(self, name, args, outcome, tag) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/llm/tool_adapter.py:179-180
    if (the source predicate is_stage_only() is truthy) {
      // Source: vvaharness/backends/llm/tool_adapter.py:180-180
      End this invocation with None.
    }
    // Source: vvaharness/backends/llm/tool_adapter.py:181-182
    In source order: Evaluate console.write(source_template_181_22); retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/llm/tool_adapter.py:184-192
  // Source signature: exhausted_tools(self) -> frozenset[str]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn exhausted_tools(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/llm/tool_adapter.py:185-186
    In source order: Retain source documentation literal source_literal_185_8; it is not a model call. Then For out, assign set(); source annotation set[str].
    // Source: vvaharness/backends/llm/tool_adapter.py:187-191
    for each mw in self._middleware or () {
      // Source: vvaharness/backends/llm/tool_adapter.py:188-188
      In source order: Evaluate once getattr(mw, 'exhausted_tools', None); assign in source target order to names.
      // Source: vvaharness/backends/llm/tool_adapter.py:189-190
      if (the source predicate names is None is truthy) {
        // Source: vvaharness/backends/llm/tool_adapter.py:190-190
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/backends/llm/tool_adapter.py:191-191
      In source order: Apply source augmented assignment out |= set(names()) with source evaluation/in-place semantics.
    }
    // Source: vvaharness/backends/llm/tool_adapter.py:192-192
    End this invocation with frozenset(out).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/llm/tool_adapter.py:194-203
  // Source signature: submit_guard(self) -> str | None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn submit_guard(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/llm/tool_adapter.py:195-195
    In source order: Retain source documentation literal source_literal_195_8; it is not a model call.
    // Source: vvaharness/backends/llm/tool_adapter.py:196-202
    for each mw in self._middleware or () {
      // Source: vvaharness/backends/llm/tool_adapter.py:197-197
      In source order: Evaluate once getattr(mw, 'hold_for_verdict', None); assign in source target order to hold.
      // Source: vvaharness/backends/llm/tool_adapter.py:198-199
      if (the source predicate hold is None is truthy) {
        // Source: vvaharness/backends/llm/tool_adapter.py:199-199
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/backends/llm/tool_adapter.py:200-200
      In source order: Evaluate once hold(); assign in source target order to text.
      // Source: vvaharness/backends/llm/tool_adapter.py:201-202
      if (the source predicate text is truthy) {
        // Source: vvaharness/backends/llm/tool_adapter.py:202-202
        End this invocation with text.
      }
    }
    // Source: vvaharness/backends/llm/tool_adapter.py:203-203
    End this invocation with None.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/llm/tool_adapter.py:205-218
  // Source signature: report_evidence_degradation(self, *, tag: str, label: str) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn report_evidence_degradation(self, tag, label) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/llm/tool_adapter.py:206-206
    In source order: Retain source documentation literal source_literal_206_8; it is not a model call.
    // Source: vvaharness/backends/llm/tool_adapter.py:208-209
    if (the source predicate not self.required or self.required & self._called is truthy) {
      // Source: vvaharness/backends/llm/tool_adapter.py:209-209
      End this invocation with None.
    }
    // Source: vvaharness/backends/llm/tool_adapter.py:210-218
    In source order: Evaluate COUNTERS.bump(EVIDENCE_UNENFORCED_COUNTER); retain side effects and discard the expression result. Then Evaluate warn_once(_WARNED, source_template_212_21, source_template_213_12); retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vvaharness/backends/llm/tool_adapter.py:221-238
// Source signature: build(tool_builder: Any, *, model: str, cwd: str, fact_tools: Sequence[str], parent_middleware: Sequence[Any]=()) -> ToolStack | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn build(tool_builder, model, cwd, fact_tools, parent_middleware) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/tool_adapter.py:224-224
  In source order: Retain source documentation literal source_literal_224_4; it is not a model call.
  // Source: vvaharness/backends/llm/tool_adapter.py:226-227
  if (the source predicate tool_builder is None or not fact_tools is truthy) {
    // Source: vvaharness/backends/llm/tool_adapter.py:227-227
    End this invocation with None.
  }
  // Source: vvaharness/backends/llm/tool_adapter.py:228-229
  In source order: Evaluate once _materialize(tool_builder, model=model, cwd=cwd, fact_tools=fact_tools); assign in source target order to lc_tools.
  // Source: vvaharness/backends/llm/tool_adapter.py:230-231
  if (the source predicate not lc_tools is truthy) {
    // Source: vvaharness/backends/llm/tool_adapter.py:231-231
    End this invocation with None.
  }
  // Source: vvaharness/backends/llm/tool_adapter.py:232-238
  End this invocation with ToolStack(schemas=[_anthropic_schema(t) for t in lc_tools], names=tuple((str(t.name) for t in lc_tools)), required=_required_fact_tools(parent_middleware), _tools={str(t.name): t for t in lc_tools}, _middleware=tuple(parent_middleware or ())).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/tool_adapter.py:241-245
In source order: Evaluate once ['EVIDENCE_UNENFORCED_COUNTER', 'ToolStack', 'build']; assign in source target order to __all__.
```

## Local import links

- `from vvaharness.backends.llm import tools as _localtools` at source line 27: `source_detail/vvaharness/backends/llm/__init__.py.sudo.md`.
- `from vvaharness.backends.llm import tools as _localtools` at source line 27: `source_detail/vvaharness/backends/llm/tools.py.sudo.md`.
- `from vvaharness.report.redact import redact, redact_counts` at source line 28: `source_detail/vvaharness/report/redact.py.sudo.md`.
- `from vvaharness.util import console` at source line 29: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import console` at source line 29: `source_detail/vvaharness/util/console.py.sudo.md`.
- `from vvaharness.util.counters import COUNTERS` at source line 30: `source_detail/vvaharness/util/counters.py.sudo.md`.
- `from vvaharness.util.scan_progress import is_stage_only` at source line 31: `source_detail/vvaharness/util/scan_progress.py.sudo.md`.
- `from vvaharness.util.warn_once import warn_once` at source line 32: `source_detail/vvaharness/util/warn_once.py.sudo.md`.
- `from vvaharness.backends.harness import StreamingOptions` at source line 47: `source_detail/vvaharness/backends/harness/__init__.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../prompt_representation/vvaharness/backends/llm/tool_adapter.py.sudo.md). Exact strings in the evidence asset support this conversion.
