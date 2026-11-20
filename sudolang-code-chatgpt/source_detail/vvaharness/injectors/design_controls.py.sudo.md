# vvaharness/injectors/design_controls.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/injectors/design_controls.py.evidence.json`. SHA-256: `6909276c44c84a738579aec74a7f3bd46425b7215c7689482dc6bb7de95d78ca`.

```sudo
// Source: vvaharness/injectors/design_controls.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import logs; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import import yaml; preserve alias and import-time effects.
// Source: vvaharness/injectors/design_controls.py:22-28
In source order: Resolve source import from pydantic import ValidationError; preserve alias and import-time effects. Then Resolve source import from vvaharness.models import Control; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import errlog as _errlog; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.events import Event; preserve alias and import-time effects. Then Evaluate once logs.get_logger(__name__); assign in source target order to log.
// Source: vvaharness/injectors/design_controls.py:31-53
// Source signature: load_controls(path: str | Path) -> list[Control]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn load_controls(path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/injectors/design_controls.py:32-32
  In source order: Evaluate once Path(path); assign in source target order to p.
  // Source: vvaharness/injectors/design_controls.py:33-34
  if (the source predicate not p.exists() is truthy) {
    // Source: vvaharness/injectors/design_controls.py:34-34
    End this invocation with [].
  }
  // Source: vvaharness/injectors/design_controls.py:39-53
  Perform the following protected operations {
    // Source: vvaharness/injectors/design_controls.py:40-40
    In source order: Evaluate once yaml.safe_load(p.read_text(encoding='utf-8')) or {}; assign in source target order to data.
    // Source: vvaharness/injectors/design_controls.py:41-48
    if (the source predicate isinstance(data, dict) is truthy) {
      // Source: vvaharness/injectors/design_controls.py:42-42
      In source order: Evaluate once data.get('controls'); assign in source target order to items.
      // Source: vvaharness/injectors/design_controls.py:43-46
      if (the source predicate items is None is truthy) {
        // Source: vvaharness/injectors/design_controls.py:44-46
        Raise ValueError("controls file is a YAML mapping without a 'controls' key — expected a list or {controls: [...]}").
      }
    }
    else {
      // Source: vvaharness/injectors/design_controls.py:48-48
      In source order: Evaluate once data; assign in source target order to items.
    }
    // Source: vvaharness/injectors/design_controls.py:49-49
    End this invocation with [Control.model_validate(item) for item in items].
  }
  // Source: vvaharness/injectors/design_controls.py:50-53
  On the first matching source exception (OSError, ValueError, TypeError, yaml.YAMLError, ValidationError) as e, in handler order {
    // Source: vvaharness/injectors/design_controls.py:51-52
    In source order: Evaluate log.warning(Event.DESIGN_CONTROLS_UNREADABLE, path=p, error=type(e).__name__, detail=str(e)); retain side effects and discard the expression result. Then Evaluate _errlog.log('inject.controls', str(p), e); retain side effects and discard the expression result.
    // Source: vvaharness/injectors/design_controls.py:53-53
    End this invocation with [].
  }
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.util import logs` at source line 17: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import logs` at source line 17: `source_detail/vvaharness/util/logs.py.sudo.md`.
- `from vvaharness.models import Control` at source line 24: `source_detail/vvaharness/models/__init__.py.sudo.md`.
- `from vvaharness.util import errlog as _errlog` at source line 25: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import errlog as _errlog` at source line 25: `source_detail/vvaharness/util/errlog.py.sudo.md`.
- `from vvaharness.util.events import Event` at source line 26: `source_detail/vvaharness/util/events.py.sudo.md`.
