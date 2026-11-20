# vvaharness/backends/harness/deepagents/models.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/backends/harness/deepagents/models.py.evidence.json`. SHA-256: `c13075760795ca4b6340d9c9de0181aca09b27dde95efb4e51607d9b09aa7f43`.

```sudo
// Source: vvaharness/backends/harness/deepagents/models.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from collections.abc import Mapping; preserve alias and import-time effects. Then Resolve source import from dataclasses import dataclass; preserve alias and import-time effects. Then Resolve source import from typing import Final, NamedTuple, NotRequired, TypedDict; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/deepagents/models.py:23-27
In source order: Resolve source import from deepagents import HarnessProfile; preserve alias and import-time effects. Then Resolve source import from deepagents.middleware.filesystem import FilesystemPermission; preserve alias and import-time effects. Then Resolve source import from langchain.agents.middleware.types import AgentMiddleware; preserve alias and import-time effects. Then Resolve source import from langchain.agents.structured_output import ToolStrategy; preserve alias and import-time effects. Then Resolve source import from langchain_core.language_models import BaseChatModel; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/deepagents/models.py:28-33
In source order: Resolve source import from langchain_core.messages import BaseMessage; preserve alias and import-time effects. Then Resolve source import from langchain_core.tools import BaseTool; preserve alias and import-time effects. Then Resolve source import from langgraph.graph.state import CompiledStateGraph; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.models import NATIVE_WRITE_TOOLS; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.git_paths import git_dir_spellings; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/deepagents/models.py:34-43
In source order: Resolve source import from vvaharness.util.tokens import TokenUsage; preserve alias and import-time effects. Then Evaluate once 'SSL_CERT_FILE'; assign in source target order to SSL_CERT_FILE_VAR. Then Evaluate once 'SSL_CERT_DIR'; assign in source target order to SSL_CERT_DIR_VAR. Then Evaluate once 'VVAHARNESS_TLS_CLIENT_CERT'; assign in source target order to TLS_CLIENT_CERT_VAR. Then Evaluate once 'VVAHARNESS_TLS_CLIENT_KEY'; assign in source target order to TLS_CLIENT_KEY_VAR.
// Source: vvaharness/backends/harness/deepagents/models.py:45-45
In source order: Evaluate once 'VVAHARNESS_TLS_VERIFY'; assign in source target order to TLS_VERIFY_VAR.
// Source: vvaharness/backends/harness/deepagents/models.py:48-50
// Source signature: anthropic_key(env: dict[str, str]) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn anthropic_key(env) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/models.py:49-49
  In source order: Retain source documentation literal source_literal_49_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/models.py:50-50
  End this invocation with env.get('ANTHROPIC_API_KEY') or env.get('ANTHROPIC_AUTH_TOKEN').
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/models.py:53-55
// Source signature: anthropic_base(env: dict[str, str]) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn anthropic_base(env) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/models.py:54-54
  In source order: Retain source documentation literal source_literal_54_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/models.py:55-55
  End this invocation with env.get('ANTHROPIC_BASE_URL').
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/models.py:58-60
// Source signature: openai_key(env: dict[str, str]) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn openai_key(env) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/models.py:59-59
  In source order: Retain source documentation literal source_literal_59_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/models.py:60-60
  End this invocation with env.get('OPENAI_API_KEY').
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/models.py:63-65
// Source signature: openai_base(env: dict[str, str]) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn openai_base(env) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/models.py:64-64
  In source order: Retain source documentation literal source_literal_64_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/models.py:65-65
  End this invocation with env.get('OPENAI_BASE_URL').
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/models.py:69-101
// Source: vvaharness/backends/harness/deepagents/models.py:68-68
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True, slots=True).
// Source: vvaharness/backends/harness/deepagents/models.py:69-101
interface ModelKey {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/harness/deepagents/models.py:70-75
  In source order: Retain source documentation literal source_literal_70_4; it is not a model call. Then For model_id, declare without assigning a value; source annotation str. Then For provider, declare without assigning a value; source annotation str. Then For openai_key, declare without assigning a value; source annotation str. Then For openai_base, declare without assigning a value; source annotation str.
  // Source: vvaharness/backends/harness/deepagents/models.py:76-80
  In source order: For anthropic_key, declare without assigning a value; source annotation str. Then For anthropic_base, declare without assigning a value; source annotation str. Then For effort, assign None; source annotation str | None. Then For use_responses_api, assign None; source annotation bool | None.
  // Source: vvaharness/backends/harness/deepagents/models.py:83-101
  // Source: vvaharness/backends/harness/deepagents/models.py:82-82
  Before creating this callable, evaluate and retain decorators top-to-bottom: classmethod.
  // Source: vvaharness/backends/harness/deepagents/models.py:83-101
  // Source signature: of(cls, model_id: str, env: dict[str, str], provider: str | None, effort: str | None=None, use_responses_api: bool | None=None) -> ModelKey
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn of(cls, model_id, env, provider, effort, use_responses_api) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/models.py:91-91
    In source order: Retain source documentation literal source_literal_91_8; it is not a model call.
    // Source: vvaharness/backends/harness/deepagents/models.py:92-101
    End this invocation with cls(model_id=model_id, provider=provider or '', openai_key=openai_key(env) or '', openai_base=openai_base(env) or '', anthropic_key=anthropic_key(env) or '', anthropic_base=anthropic_base(env) or '', effort=effort, use_responses_api=use_responses_api).
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vvaharness/backends/harness/deepagents/models.py:105-131
In source order: Evaluate once HarnessProfile(excluded_tools=NATIVE_WRITE_TOOLS); assign in source target order to READ_ONLY_HARNESS_PROFILE. Then For READ_ONLY_PERMISSIONS, assign [FilesystemPermission(operations=['write'], paths=['/**', '/.*', '/.*/**', '/**/.*', '/**/.*/**'], mode='deny')]; source annotation list[FilesystemPermission]. Then For GIT_INTERNALS_DENY, assign [FilesystemPermission(operations=['write'], paths=[p for d in git_dir_spellings() for p in (source_template_122_25, source_template_122_34, source_template_122_46, source_template_122_58)], mode='deny')]; source annotation list[FilesystemPermission]. Then For DELETE_TOOL_NAME, assign 'delete'; source annotation Final. Then For SUBAGENT_DISPATCH_TOOL, assign 'task'; source annotation Final.
// Source: vvaharness/backends/harness/deepagents/models.py:134-136
In source order: For ALL_NATIVE_TOOLS, assign frozenset({'ls', 'read_file', 'write_file', 'edit_file', 'glob', 'grep', 'delete', 'execute'}); source annotation Final[frozenset[str]].
// Source: vvaharness/backends/harness/deepagents/models.py:139-149
interface SubagentSpec {
  Describe the source Python type, preserving its base/metaclass expression order: TypedDict.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/harness/deepagents/models.py:140-145
  In source order: Retain source documentation literal source_literal_140_4; it is not a model call. Then For name, declare without assigning a value; source annotation str. Then For description, declare without assigning a value; source annotation str. Then For system_prompt, declare without assigning a value; source annotation str. Then For model, declare without assigning a value; source annotation BaseChatModel.
  // Source: vvaharness/backends/harness/deepagents/models.py:146-149
  In source order: For tools, declare without assigning a value; source annotation list[BaseTool]. Then For middleware, declare without assigning a value; source annotation NotRequired[list[AgentMiddleware]]. Then For response_format, declare without assigning a value; source annotation NotRequired[ToolStrategy | type]. Then For skills, declare without assigning a value; source annotation NotRequired[list[str]].
}
// Source: vvaharness/backends/harness/deepagents/models.py:152-155
interface GraphConfigurable {
  Describe the source Python type, preserving its base/metaclass expression order: TypedDict.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/harness/deepagents/models.py:153-155
  In source order: Retain source documentation literal source_literal_153_4; it is not a model call. Then For thread_id, declare without assigning a value; source annotation str.
}
// Source: vvaharness/backends/harness/deepagents/models.py:158-162
interface GraphInvokeConfig {
  Describe the source Python type, preserving its base/metaclass expression order: TypedDict.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/harness/deepagents/models.py:159-162
  In source order: Retain source documentation literal source_literal_159_4; it is not a model call. Then For configurable, declare without assigning a value; source annotation GraphConfigurable. Then For recursion_limit, declare without assigning a value; source annotation NotRequired[int].
}
// Source: vvaharness/backends/harness/deepagents/models.py:165-169
interface CompiledGraph {
  Describe the source Python type, preserving its base/metaclass expression order: NamedTuple.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/harness/deepagents/models.py:166-169
  In source order: Retain source documentation literal source_literal_166_4; it is not a model call. Then For graph, declare without assigning a value; source annotation CompiledStateGraph. Then For config, declare without assigning a value; source annotation GraphInvokeConfig.
}
// Source: vvaharness/backends/harness/deepagents/models.py:172-178
interface DeepAgentsGraphState {
  Describe the source Python type, preserving its base/metaclass expression order: TypedDict, total=False.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/harness/deepagents/models.py:173-178
  In source order: Retain source documentation literal source_literal_173_4; it is not a model call. Then For messages, declare without assigning a value; source annotation list[BaseMessage]. Then For structured_response, declare without assigning a value; source annotation object. Then For usage, declare without assigning a value; source annotation TokenUsage. Then For sdk_persona_reports, declare without assigning a value; source annotation list[dict[str, object]].
}
// Source: vvaharness/backends/harness/deepagents/models.py:181-185
interface StreamEvent {
  Describe the source Python type, preserving its base/metaclass expression order: NamedTuple.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/harness/deepagents/models.py:182-185
  In source order: Retain source documentation literal source_literal_182_4; it is not a model call. Then For namespace, declare without assigning a value; source annotation tuple[str, ...]. Then For payload, declare without assigning a value; source annotation Mapping[str, DeepAgentsGraphState].
}
// Source: vvaharness/backends/harness/deepagents/models.py:188-211
In source order: Evaluate once ['ALL_NATIVE_TOOLS', 'DELETE_TOOL_NAME', 'GIT_INTERNALS_DENY', 'READ_ONLY_HARNESS_PROFILE', 'READ_ONLY_PERMISSIONS', 'SSL_CERT_DIR_VAR', 'SSL_CERT_FILE_VAR', 'SUBAGENT_DISPATCH_TOOL', 'TLS_CLIENT_CERT_VAR', 'TLS_CLIENT_KEY_VAR', 'TLS_VERIFY_VAR', 'CompiledGraph', 'DeepAgentsGraphState', 'GraphConfigurable', 'GraphInvokeConfig', 'ModelKey', 'StreamEvent', 'SubagentSpec', 'anthropic_base', 'anthropic_key', 'openai_base', 'openai_key']; assign in source target order to __all__.
```

## Local import links

- `from vvaharness.backends.harness.models import NATIVE_WRITE_TOOLS` at source line 32: `source_detail/vvaharness/backends/harness/models.py.sudo.md`.
- `from vvaharness.util.git_paths import git_dir_spellings` at source line 33: `source_detail/vvaharness/util/git_paths.py.sudo.md`.
- `from vvaharness.util.tokens import TokenUsage` at source line 34: `source_detail/vvaharness/util/tokens.py.sudo.md`.
