# vvaharness/validation/hints/loader.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/validation/hints/loader.py.evidence.json`. SHA-256: `82f321f27b675059b304cf118a27339a4c81d38b99b5fa9f14cc2b24c53e6e11`.

```sudo
// Source: vvaharness/validation/hints/loader.py:15-22
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import import yaml; preserve alias and import-time effects. Then Resolve source import from pydantic import BaseModel, ConfigDict; preserve alias and import-time effects.
// Source: vvaharness/validation/hints/loader.py:24-27
In source order: Resolve source import from vvaharness.validation.constants.artifacts import INPUTS_DIRNAME, VALIDATOR_HINTS_FILENAME; preserve alias and import-time effects.
// Source: vvaharness/validation/hints/loader.py:30-32
// Source signature: _hints_path() -> Path
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _hints_path() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/hints/loader.py:31-31
  In source order: Retain source documentation literal source_literal_31_4; it is not a model call.
  // Source: vvaharness/validation/hints/loader.py:32-32
  End this invocation with Path.cwd() / INPUTS_DIRNAME / VALIDATOR_HINTS_FILENAME.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/hints/loader.py:35-41
// Source signature: _parse_hints(path: Path) -> dict[str, object] | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _parse_hints(path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/hints/loader.py:36-36
  In source order: Retain source documentation literal source_literal_36_4; it is not a model call.
  // Source: vvaharness/validation/hints/loader.py:37-40
  Perform the following protected operations {
    // Source: vvaharness/validation/hints/loader.py:38-38
    In source order: Evaluate once yaml.safe_load(path.read_text(encoding='utf-8')); assign in source target order to loaded.
  }
  // Source: vvaharness/validation/hints/loader.py:39-40
  On the first matching source exception (OSError, yaml.YAMLError), in handler order {
    // Source: vvaharness/validation/hints/loader.py:40-40
    End this invocation with None.
  }
  // Source: vvaharness/validation/hints/loader.py:41-41
  End this invocation with loaded if isinstance(loaded, dict) else {}.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/hints/loader.py:44-56
// Source signature: _resolve_raw() -> dict[str, object]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _resolve_raw() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/hints/loader.py:45-46
  In source order: Retain source documentation literal source_literal_45_4; it is not a model call. Then Evaluate once _hints_path(); assign in source target order to path.
  // Source: vvaharness/validation/hints/loader.py:47-48
  if (the source predicate not path.exists() is truthy) {
    // Source: vvaharness/validation/hints/loader.py:48-48
    End this invocation with {}.
  }
  // Source: vvaharness/validation/hints/loader.py:49-49
  In source order: Evaluate once _parse_hints(path); assign in source target order to raw.
  // Source: vvaharness/validation/hints/loader.py:50-55
  if (the source predicate raw is None is truthy) {
    // Source: vvaharness/validation/hints/loader.py:51-54
    In source order: Evaluate print(source_template_52_12); retain side effects and discard the expression result.
    // Source: vvaharness/validation/hints/loader.py:55-55
    End this invocation with {}.
  }
  // Source: vvaharness/validation/hints/loader.py:56-56
  End this invocation with raw.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/hints/loader.py:59-74
interface CweHints {
  Describe the source Python type, preserving its base/metaclass expression order: BaseModel.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/validation/hints/loader.py:60-64
  In source order: Retain source documentation literal source_literal_60_4; it is not a model call. Then Evaluate once ConfigDict(extra='ignore'); assign in source target order to model_config. Then For hints, declare without assigning a value; source annotation dict[str, list[str]].
  // Source: vvaharness/validation/hints/loader.py:67-74
  // Source: vvaharness/validation/hints/loader.py:66-66
  Before creating this callable, evaluate and retain decorators top-to-bottom: classmethod.
  // Source: vvaharness/validation/hints/loader.py:67-74
  // Source signature: load(cls) -> CweHints
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn load(cls) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/validation/hints/loader.py:68-70
    In source order: Retain source documentation literal source_literal_68_8; it is not a model call. Then Evaluate once _resolve_raw(); assign in source target order to raw. Then For cleaned, assign {}; source annotation dict[str, list[str]].
    // Source: vvaharness/validation/hints/loader.py:71-73
    for each (key, val) in raw.items() {
      // Source: vvaharness/validation/hints/loader.py:72-73
      if (the source predicate isinstance(key, str) and isinstance(val, list) is truthy) {
        // Source: vvaharness/validation/hints/loader.py:73-73
        In source order: Evaluate once [str(h) for h in val]; assign in source target order to cleaned[key.strip()].
      }
    }
    // Source: vvaharness/validation/hints/loader.py:74-74
    End this invocation with cls(hints=cleaned).
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
}
// Source: vvaharness/validation/hints/loader.py:77-77
In source order: For _REGISTRY, assign None; source annotation CweHints | None.
// Source: vvaharness/validation/hints/loader.py:80-85
// Source signature: _registry() -> CweHints
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _registry() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/hints/loader.py:81-82
  In source order: Retain source documentation literal source_literal_81_4; it is not a model call. Then Bind names in module scope: _REGISTRY.
  // Source: vvaharness/validation/hints/loader.py:83-84
  if (the source predicate _REGISTRY is None is truthy) {
    // Source: vvaharness/validation/hints/loader.py:84-84
    In source order: Evaluate once CweHints.load(); assign in source target order to _REGISTRY.
  }
  // Source: vvaharness/validation/hints/loader.py:85-85
  End this invocation with _REGISTRY.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/hints/loader.py:88-96
// Source signature: hints_for(category: str) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn hints_for(category) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/hints/loader.py:89-91
  In source order: Retain source documentation literal source_literal_89_4; it is not a model call. Then Evaluate once _registry(); assign in source target order to reg. Then Evaluate once reg.hints.get(category.strip()); assign in source target order to direct.
  // Source: vvaharness/validation/hints/loader.py:92-93
  if (the source predicate direct is not None is truthy) {
    // Source: vvaharness/validation/hints/loader.py:93-93
    End this invocation with direct.
  }
  // Source: vvaharness/validation/hints/loader.py:95-95
  In source order: Evaluate once category.split(':')[0].strip(); assign in source target order to prefix.
  // Source: vvaharness/validation/hints/loader.py:96-96
  End this invocation with reg.hints.get(prefix, []).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.validation.constants.artifacts import INPUTS_DIRNAME, VALIDATOR_HINTS_FILENAME` at source line 24: `source_detail/vvaharness/validation/constants/artifacts.py.sudo.md`.
