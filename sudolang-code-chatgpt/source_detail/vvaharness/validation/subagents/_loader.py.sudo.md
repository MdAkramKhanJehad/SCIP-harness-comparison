# vvaharness/validation/subagents/_loader.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/validation/subagents/_loader.py.evidence.json`. SHA-256: `eafda7d6e490fd39596e5a2b69f01be85cff47beec3d37988b7410ad0710ccc5`.

```sudo
// Source: vvaharness/validation/subagents/_loader.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from collections.abc import Iterable, Iterator; preserve alias and import-time effects. Then Resolve source import from dataclasses import replace; preserve alias and import-time effects. Then Resolve source import from importlib.resources import files; preserve alias and import-time effects.
// Source: vvaharness/validation/subagents/_loader.py:22-27
In source order: Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness import SubagentDefinition; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.constants.tools import FACT_TOOLS; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.models.persona_report import PersonaReport; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.subagents._frontmatter import parse_frontmatter; preserve alias and import-time effects.
// Source: vvaharness/validation/subagents/_loader.py:28-28
In source order: Resolve source import from vvaharness.validation.subagents.models import SubagentFrontmatterMeta; preserve alias and import-time effects.
// Source: vvaharness/validation/subagents/_loader.py:31-33
// Source signature: _optional_str_tuple(value: list[str] | None) -> tuple[str, ...] | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _optional_str_tuple(value) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/subagents/_loader.py:32-32
  In source order: Retain source documentation literal source_literal_32_4; it is not a model call.
  // Source: vvaharness/validation/subagents/_loader.py:33-33
  End this invocation with tuple(value) if isinstance(value, list) and value else None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/subagents/_loader.py:36-57
// Source signature: _build_subagent_definition(meta: SubagentFrontmatterMeta, prompt: str) -> SubagentDefinition
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _build_subagent_definition(meta, prompt) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/subagents/_loader.py:40-41
  In source order: Retain source documentation literal source_literal_40_4; it is not a model call. Then Evaluate once meta.get('name'); assign in source target order to name.
  // Source: vvaharness/validation/subagents/_loader.py:42-43
  if (the source predicate not isinstance(name, str) or not name is truthy) {
    // Source: vvaharness/validation/subagents/_loader.py:43-43
    Raise ValueError("subagent frontmatter missing 'name'").
  }
  // Source: vvaharness/validation/subagents/_loader.py:44-44
  In source order: Evaluate once meta.get('description'); assign in source target order to description.
  // Source: vvaharness/validation/subagents/_loader.py:45-46
  if (the source predicate not isinstance(description, str) or not description is truthy) {
    // Source: vvaharness/validation/subagents/_loader.py:46-46
    Raise ValueError(source_template_46_25).
  }
  // Source: vvaharness/validation/subagents/_loader.py:47-47
  In source order: Evaluate once meta.get('model'); assign in source target order to model.
  // Source: vvaharness/validation/subagents/_loader.py:48-57
  End this invocation with SubagentDefinition(name=name, description=description, prompt=prompt, tools=_optional_str_tuple(meta.get('allowedTools')), disallowed_tools=_optional_str_tuple(meta.get('deniedTools')), model=model if isinstance(model, str) else None, skills=_optional_str_tuple(meta.get('skills')), response_model=PersonaReport).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/subagents/_loader.py:60-65
// Source signature: _iter_bundled_files() -> Iterator[Path]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _iter_bundled_files() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/subagents/_loader.py:61-62
  In source order: Retain source documentation literal source_literal_61_4; it is not a model call. Then Evaluate once files('vvaharness.validation.subagents'); assign in source target order to pkg_root.
  // Source: vvaharness/validation/subagents/_loader.py:63-65
  for each entry in pkg_root.iterdir() {
    // Source: vvaharness/validation/subagents/_loader.py:64-65
    if (the source predicate entry.name.endswith('.md') is truthy) {
      // Source: vvaharness/validation/subagents/_loader.py:65-65
      In source order: Yield Path(str(entry)); suspend this generator until resumed.
    }
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/subagents/_loader.py:68-111
// Source signature: load_agents(names: Iterable[str] | None=None, model_overrides: dict[str, str] | None=None, tools_override: tuple[str, ...] | None=None, prompt_suffix: str | None=None, max_model_calls: int | None=None) -> dict[str, SubagentDefinition]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn load_agents(names, model_overrides, tools_override, prompt_suffix, max_model_calls) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/subagents/_loader.py:75-87
  In source order: Retain source documentation literal source_literal_75_4; it is not a model call. Then For wanted, assign set(names) if names is not None else None; source annotation set[str] | None. Then Evaluate once model_overrides or {}; assign in source target order to overrides. Then For result, assign {}; source annotation dict[str, SubagentDefinition].
  // Source: vvaharness/validation/subagents/_loader.py:88-109
  for each path in _iter_bundled_files() {
    // Source: vvaharness/validation/subagents/_loader.py:89-91
    In source order: Evaluate once path.read_text(encoding='utf-8'); assign in source target order to text. Then Evaluate once parse_frontmatter(text); assign in source target order to (meta, prompt). Then Evaluate once _build_subagent_definition(meta, prompt); assign in source target order to subagent.
    // Source: vvaharness/validation/subagents/_loader.py:92-93
    if (the source predicate wanted is not None and subagent.name not in wanted is truthy) {
      // Source: vvaharness/validation/subagents/_loader.py:93-93
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/validation/subagents/_loader.py:94-95
    if (the source predicate subagent.name in overrides is truthy) {
      // Source: vvaharness/validation/subagents/_loader.py:95-95
      In source order: Evaluate once replace(subagent, model=overrides[subagent.name]); assign in source target order to subagent.
    }
    // Source: vvaharness/validation/subagents/_loader.py:96-102
    if (the source predicate tools_override is not None is truthy) {
      // Source: vvaharness/validation/subagents/_loader.py:97-102
      In source order: Evaluate once set(tools_override); assign in source target order to override_set. Then Evaluate once tuple((t for t in subagent.tools or () if t in override_set or t in FACT_TOOLS)); assign in source target order to narrowed. Then Evaluate once replace(subagent, tools=narrowed); assign in source target order to subagent.
    }
    // Source: vvaharness/validation/subagents/_loader.py:103-106
    if (the source predicate prompt_suffix is truthy) {
      // Source: vvaharness/validation/subagents/_loader.py:104-106
      In source order: Evaluate once replace(subagent, prompt=source_template_105_33); assign in source target order to subagent.
    }
    // Source: vvaharness/validation/subagents/_loader.py:108-109
    In source order: Evaluate once replace(subagent, max_model_calls=max_model_calls or None); assign in source target order to subagent. Then Evaluate once subagent; assign in source target order to result[subagent.name].
  }
  // Source: vvaharness/validation/subagents/_loader.py:110-110
  In source order: Evaluate _assert_all_found(wanted, set(result.keys())); retain side effects and discard the expression result.
  // Source: vvaharness/validation/subagents/_loader.py:111-111
  End this invocation with result.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/subagents/_loader.py:114-120
// Source signature: _assert_all_found(wanted: set[str] | None, found: set[str]) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _assert_all_found(wanted, found) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/subagents/_loader.py:115-115
  In source order: Retain source documentation literal source_literal_115_4; it is not a model call.
  // Source: vvaharness/validation/subagents/_loader.py:116-117
  if (the source predicate wanted is None is truthy) {
    // Source: vvaharness/validation/subagents/_loader.py:117-117
    End this invocation with None.
  }
  // Source: vvaharness/validation/subagents/_loader.py:118-118
  In source order: Evaluate once wanted - found; assign in source target order to missing.
  // Source: vvaharness/validation/subagents/_loader.py:119-120
  if (the source predicate missing is truthy) {
    // Source: vvaharness/validation/subagents/_loader.py:120-120
    Raise ValueError(source_template_120_25).
  }
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.backends.harness import SubagentDefinition` at source line 24: `source_detail/vvaharness/backends/harness/__init__.py.sudo.md`.
- `from vvaharness.validation.constants.tools import FACT_TOOLS` at source line 25: `source_detail/vvaharness/validation/constants/tools.py.sudo.md`.
- `from vvaharness.validation.models.persona_report import PersonaReport` at source line 26: `source_detail/vvaharness/validation/models/persona_report.py.sudo.md`.
- `from vvaharness.validation.subagents._frontmatter import parse_frontmatter` at source line 27: `source_detail/vvaharness/validation/subagents/_frontmatter.py.sudo.md`.
- `from vvaharness.validation.subagents.models import SubagentFrontmatterMeta` at source line 28: `source_detail/vvaharness/validation/subagents/models.py.sudo.md`.
