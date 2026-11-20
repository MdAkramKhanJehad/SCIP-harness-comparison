# vvaharness/backends/harness/deepagents/options/response_format.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/backends/harness/deepagents/options/response_format.py.evidence.json`. SHA-256: `880338b6cca60e9bf9512513f0393635eb8bb33eed24a51d4148937c716b57cb`.

```sudo
// Source: vvaharness/backends/harness/deepagents/options/response_format.py:15-22
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from typing import Any; preserve alias and import-time effects. Then Resolve source import from langchain.agents.structured_output import ToolStrategy; preserve alias and import-time effects. Then Resolve source import from pydantic import BaseModel, Field, create_model; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/deepagents/options/response_format.py:24-30
In source order: Resolve source import from vvaharness.backends.harness.deepagents.options.model_building import _FORCED_TOOL_CHOICE_UNSUPPORTED_MODELS; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.models import OneShotOptions; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.provider_routing import routes_to_anthropic; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm.models import with_submit_instruction; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.counters import COUNTERS; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/deepagents/options/response_format.py:31-34
In source order: Resolve source import from vvaharness.util.warn_once import warn_once; preserve alias and import-time effects. Then For _WARNED_DROPS, assign set(); source annotation set[str]. Then For _WARNED_UNSUPPORTED, assign set(); source annotation set[str].
// Source: vvaharness/backends/harness/deepagents/options/response_format.py:37-53
// Source signature: _pydantic_response_format(schema: dict[str, Any]) -> type[BaseModel]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _pydantic_response_format(schema) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/options/response_format.py:38-48
  In source order: Retain source documentation literal source_literal_38_4; it is not a model call. Then For type_map, assign {'string': str, 'integer': int, 'number': float, 'boolean': bool, 'array': list, 'object': dict}; source annotation dict[str, type]. Then Evaluate once set(schema.get('required', ())); assign in source target order to required. Then For fields, assign {}; source annotation dict[str, tuple[type, Any]].
  // Source: vvaharness/backends/harness/deepagents/options/response_format.py:49-52
  for each (name, prop) in schema.get('properties', {}).items() {
    // Source: vvaharness/backends/harness/deepagents/options/response_format.py:50-52
    In source order: Evaluate once type_map.get(prop.get('type'), str); assign in source target order to base. Then Evaluate once Field(...) if name in required else Field(default=None); assign in source target order to default. Then Evaluate once (base, default); assign in source target order to fields[name].
  }
  // Source: vvaharness/backends/harness/deepagents/options/response_format.py:53-53
  End this invocation with create_model('HarnessResponse', **fields).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/options/response_format.py:56-61
// Source signature: _strategy_for(schema: type, model_id: str, provider: str | None) -> ToolStrategy | type
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _strategy_for(schema, model_id, provider) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/options/response_format.py:57-57
  In source order: Retain source documentation literal source_literal_57_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/options/response_format.py:58-60
  if (the source predicate routes_to_anthropic(model_id, provider) and model_id not in _FORCED_TOOL_CHOICE_UNSUPPORTED_MODELS is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/response_format.py:60-60
    End this invocation with ToolStrategy(schema=schema).
  }
  // Source: vvaharness/backends/harness/deepagents/options/response_format.py:61-61
  End this invocation with schema.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/options/response_format.py:64-76
// Source signature: forcing_dropped_under_thinking(model: object, response_format: object) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn forcing_dropped_under_thinking(model, response_format) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/options/response_format.py:65-72
  In source order: Retain source documentation literal source_literal_65_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/options/response_format.py:73-74
  if (the source predicate not isinstance(response_format, ToolStrategy) is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/response_format.py:74-74
    End this invocation with False.
  }
  // Source: vvaharness/backends/harness/deepagents/options/response_format.py:75-75
  In source order: Evaluate once getattr(model, 'thinking', None) or {}; assign in source target order to thinking.
  // Source: vvaharness/backends/harness/deepagents/options/response_format.py:76-76
  End this invocation with thinking.get('type') in ('enabled', 'adaptive').
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/options/response_format.py:79-81
// Source signature: _model_tag(model: object) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _model_tag(model) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/options/response_format.py:80-80
  In source order: Retain source documentation literal source_literal_80_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/options/response_format.py:81-81
  End this invocation with str(getattr(model, 'model', None) or getattr(model, 'model_name', None) or 'unknown').
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/options/response_format.py:84-98
// Source signature: _warn_tool_choice_dropped(model: object) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _warn_tool_choice_dropped(model) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/options/response_format.py:85-98
  In source order: Retain source documentation literal source_literal_85_4; it is not a model call. Then Evaluate once _model_tag(model); assign in source target order to tag. Then Evaluate warn_once(_WARNED_DROPS, tag, source_template_93_8); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/options/response_format.py:101-103
// Source signature: _forcing_unsupported(model: object) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _forcing_unsupported(model) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/options/response_format.py:102-102
  In source order: Retain source documentation literal source_literal_102_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/options/response_format.py:103-103
  End this invocation with _model_tag(model) in _FORCED_TOOL_CHOICE_UNSUPPORTED_MODELS.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/options/response_format.py:106-116
// Source signature: _warn_tool_choice_unsupported(model: object) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _warn_tool_choice_unsupported(model) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/options/response_format.py:107-116
  In source order: Retain source documentation literal source_literal_107_4; it is not a model call. Then Evaluate once _model_tag(model); assign in source target order to tag. Then Evaluate warn_once(_WARNED_UNSUPPORTED, tag, source_template_111_8); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/options/response_format.py:119-121
// Source signature: _tool_name_for(response_model: type) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _tool_name_for(response_model) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/options/response_format.py:120-120
  In source order: Retain source documentation literal source_literal_120_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/options/response_format.py:121-121
  End this invocation with ToolStrategy(schema=response_model).schema_specs[0].name.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/options/response_format.py:124-143
// Source signature: submit_instructed_prompt(system_prompt: str | None, model: object, response_model: type | None, response_format: object) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn submit_instructed_prompt(system_prompt, model, response_model, response_format) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/options/response_format.py:128-131
  In source order: Retain source documentation literal source_literal_128_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/options/response_format.py:132-133
  if (the source predicate response_model is None is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/response_format.py:133-133
    End this invocation with system_prompt.
  }
  // Source: vvaharness/backends/harness/deepagents/options/response_format.py:134-141
  if (the source predicate forcing_dropped_under_thinking(model, response_format) is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/response_format.py:135-136
    In source order: Evaluate COUNTERS.bump('deepagents_tool_choice_dropped'); retain side effects and discard the expression result. Then Evaluate _warn_tool_choice_dropped(model); retain side effects and discard the expression result.
  }
  else {
    // Source: vvaharness/backends/harness/deepagents/options/response_format.py:137-141
    if (the source predicate _forcing_unsupported(model) is truthy) {
      // Source: vvaharness/backends/harness/deepagents/options/response_format.py:138-139
      In source order: Evaluate COUNTERS.bump('deepagents_tool_choice_unsupported'); retain side effects and discard the expression result. Then Evaluate _warn_tool_choice_unsupported(model); retain side effects and discard the expression result.
    }
    else {
      // Source: vvaharness/backends/harness/deepagents/options/response_format.py:141-141
      End this invocation with system_prompt.
    }
  }
  // Source: vvaharness/backends/harness/deepagents/options/response_format.py:142-142
  In source order: Evaluate once _tool_name_for(response_model); assign in source target order to tool_name.
  // Source: vvaharness/backends/harness/deepagents/options/response_format.py:143-143
  End this invocation with with_submit_instruction(system_prompt, response_model, tool_name=tool_name).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/options/response_format.py:146-152
// Source signature: _response_format(response_model: type | None, model_id: str, provider: str | None) -> ToolStrategy | type | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _response_format(response_model, model_id, provider) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/options/response_format.py:149-149
  In source order: Retain source documentation literal source_literal_149_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/options/response_format.py:150-151
  if (the source predicate response_model is None is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/response_format.py:151-151
    End this invocation with None.
  }
  // Source: vvaharness/backends/harness/deepagents/options/response_format.py:152-152
  End this invocation with _strategy_for(response_model, model_id, provider).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/options/response_format.py:155-164
// Source signature: _oneshot_response_format(options: OneShotOptions) -> ToolStrategy | type | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _oneshot_response_format(options) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/options/response_format.py:158-158
  In source order: Retain source documentation literal source_literal_158_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/options/response_format.py:159-160
  if (the source predicate options.response_model is not None is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/response_format.py:160-160
    End this invocation with _strategy_for(options.response_model, options.model, options.model_provider).
  }
  // Source: vvaharness/backends/harness/deepagents/options/response_format.py:161-163
  if (the source predicate options.output_schema is not None is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/response_format.py:162-162
    In source order: Evaluate once _pydantic_response_format(dict(options.output_schema)); assign in source target order to derived.
    // Source: vvaharness/backends/harness/deepagents/options/response_format.py:163-163
    End this invocation with _strategy_for(derived, options.model, options.model_provider).
  }
  // Source: vvaharness/backends/harness/deepagents/options/response_format.py:164-164
  End this invocation with None.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.backends.harness.deepagents.options.model_building import _FORCED_TOOL_CHOICE_UNSUPPORTED_MODELS` at source line 24: `source_detail/vvaharness/backends/harness/deepagents/options/model_building.py.sudo.md`.
- `from vvaharness.backends.harness.models import OneShotOptions` at source line 27: `source_detail/vvaharness/backends/harness/models.py.sudo.md`.
- `from vvaharness.backends.harness.provider_routing import routes_to_anthropic` at source line 28: `source_detail/vvaharness/backends/harness/provider_routing.py.sudo.md`.
- `from vvaharness.backends.llm.models import with_submit_instruction` at source line 29: `source_detail/vvaharness/backends/llm/models.py.sudo.md`.
- `from vvaharness.util.counters import COUNTERS` at source line 30: `source_detail/vvaharness/util/counters.py.sudo.md`.
- `from vvaharness.util.warn_once import warn_once` at source line 31: `source_detail/vvaharness/util/warn_once.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../../../prompt_representation/vvaharness/backends/harness/deepagents/options/response_format.py.sudo.md). Exact strings in the evidence asset support this conversion.
