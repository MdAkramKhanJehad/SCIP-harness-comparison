# vvaharness/cli/_paths.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/cli/_paths.py.evidence.json`. SHA-256: `6184afd1cdaabc6458db1d31d01abef520c60d278da8a01d471952c809c8e40b`.

```sudo
// Source: vvaharness/cli/_paths.py:16-21
In source order: Retain source documentation literal source_literal_16_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import sys; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from typing import TYPE_CHECKING; preserve alias and import-time effects.
// Source: vvaharness/cli/_paths.py:23-23
In source order: Resolve source import from vvaharness.util import console; preserve alias and import-time effects.
// Source: vvaharness/cli/_paths.py:25-26
if (the source predicate TYPE_CHECKING is truthy) {
  // Source: vvaharness/cli/_paths.py:26-26
  In source order: Resolve source import from vvaharness.config import Config; preserve alias and import-time effects.
}
// Source: vvaharness/cli/_paths.py:29-39
// Source signature: _load_and_configure(cfg_path: str, label: str) -> Config | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _load_and_configure(cfg_path, label) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/cli/_paths.py:30-32
  In source order: Retain source documentation literal source_literal_30_4; it is not a model call. Then Resolve source import from vvaharness import config as config_mod; preserve alias and import-time effects. Then Resolve source import from vvaharness.orchestrator import configure_backends; preserve alias and import-time effects.
  // Source: vvaharness/cli/_paths.py:33-37
  Perform the following protected operations {
    // Source: vvaharness/cli/_paths.py:34-34
    In source order: Evaluate once config_mod.load(cfg_path); assign in source target order to cfg.
  }
  // Source: vvaharness/cli/_paths.py:35-37
  On the first matching source exception config_mod.ConfigPolicyError as e, in handler order {
    // Source: vvaharness/cli/_paths.py:36-36
    In source order: Evaluate console.write(source_template_36_22); retain side effects and discard the expression result.
    // Source: vvaharness/cli/_paths.py:37-37
    End this invocation with None.
  }
  // Source: vvaharness/cli/_paths.py:38-38
  In source order: Evaluate configure_backends(cfg, Path(cfg_path).resolve().parent); retain side effects and discard the expression result.
  // Source: vvaharness/cli/_paths.py:39-39
  End this invocation with cfg.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/cli/_paths.py:41-53
// Source signature: _config_path_from_explicit(rest: list[str]) -> tuple[str, bool]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _config_path_from_explicit(rest) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/cli/_paths.py:42-44
  In source order: Retain source documentation literal source_literal_42_4; it is not a model call. Then Resolve source import from vvaharness.orchestrator import _default_config; preserve alias and import-time effects. Then For found, assign None; source annotation str | None.
  // Source: vvaharness/cli/_paths.py:45-50
  for each (i, a) in enumerate(rest) {
    // Source: vvaharness/cli/_paths.py:47-50
    if (the source predicate a == '--config' and i + 1 < len(rest) is truthy) {
      // Source: vvaharness/cli/_paths.py:48-48
      In source order: Evaluate once rest[i + 1]; assign in source target order to found.
    }
    else {
      // Source: vvaharness/cli/_paths.py:49-50
      if (the source predicate a.startswith('--config=') is truthy) {
        // Source: vvaharness/cli/_paths.py:50-50
        In source order: Evaluate once a.split('=', 1)[1]; assign in source target order to found.
      }
    }
  }
  // Source: vvaharness/cli/_paths.py:51-52
  if (the source predicate found is not None is truthy) {
    // Source: vvaharness/cli/_paths.py:52-52
    End this invocation with (found, True).
  }
  // Source: vvaharness/cli/_paths.py:53-53
  End this invocation with (str(_default_config()), False).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/cli/_paths.py:55-57
// Source signature: _config_path_from(rest: list[str]) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _config_path_from(rest) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/cli/_paths.py:56-56
  In source order: Retain source documentation literal source_literal_56_4; it is not a model call.
  // Source: vvaharness/cli/_paths.py:57-57
  End this invocation with _config_path_from_explicit(rest)[0].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/cli/_paths.py:59-61
// Source signature: _config_trust_boundary(rest: list[str]) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _config_trust_boundary(rest) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/cli/_paths.py:60-60
  In source order: Retain source documentation literal source_literal_60_4; it is not a model call.
  // Source: vvaharness/cli/_paths.py:61-61
  End this invocation with _repo_from(rest).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/cli/_paths.py:63-79
// Source signature: _check_python() -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _check_python() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/cli/_paths.py:64-64
  In source order: Retain source documentation literal source_literal_64_4; it is not a model call.
  // Source: vvaharness/cli/_paths.py:65-69
  Perform the following protected operations {
    // Source: vvaharness/cli/_paths.py:66-67
    In source order: Resolve source import from importlib.metadata import metadata; preserve alias and import-time effects. Then Evaluate once metadata('vvaharness').get('Requires-Python') or ''; assign in source target order to req.
  }
  // Source: vvaharness/cli/_paths.py:68-69
  On the first matching source exception Exception, in handler order {
    // Source: vvaharness/cli/_paths.py:69-69
    End this invocation with None.
  }
  // Source: vvaharness/cli/_paths.py:70-71
  In source order: Resolve source import import re; preserve alias and import-time effects. Then Evaluate once re.search('>=\\s*(\\d+)\\.(\\d+)', req); assign in source target order to m.
  // Source: vvaharness/cli/_paths.py:72-73
  if (the source predicate not m is truthy) {
    // Source: vvaharness/cli/_paths.py:73-73
    End this invocation with None.
  }
  // Source: vvaharness/cli/_paths.py:74-74
  In source order: Evaluate once (int(m.group(1)), int(m.group(2))); assign in source target order to floor.
  // Source: vvaharness/cli/_paths.py:75-78
  if (the source predicate sys.version_info[:2] < floor is truthy) {
    // Source: vvaharness/cli/_paths.py:76-76
    In source order: Evaluate once '.'.join((str(v) for v in sys.version_info[:3])); assign in source target order to cur.
    // Source: vvaharness/cli/_paths.py:77-78
    End this invocation with source_template_77_16.
  }
  // Source: vvaharness/cli/_paths.py:79-79
  End this invocation with None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/cli/_paths.py:81-88
// Source signature: _repo_from(rest: list[str]) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _repo_from(rest) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/cli/_paths.py:82-82
  In source order: Retain source documentation literal source_literal_82_4; it is not a model call.
  // Source: vvaharness/cli/_paths.py:83-87
  for each (i, a) in enumerate(rest) {
    // Source: vvaharness/cli/_paths.py:84-85
    if (the source predicate a == '--repo' and i + 1 < len(rest) is truthy) {
      // Source: vvaharness/cli/_paths.py:85-85
      End this invocation with rest[i + 1].
    }
    // Source: vvaharness/cli/_paths.py:86-87
    if (the source predicate a.startswith('--repo=') is truthy) {
      // Source: vvaharness/cli/_paths.py:87-87
      End this invocation with a.split('=', 1)[1].
    }
  }
  // Source: vvaharness/cli/_paths.py:88-88
  End this invocation with None.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.util import console` at source line 23: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import console` at source line 23: `source_detail/vvaharness/util/console.py.sudo.md`.
- `from vvaharness.config import Config` at source line 26: `source_detail/vvaharness/config/__init__.py.sudo.md`.
- `from vvaharness import config as config_mod` at source line 31: `source_detail/vvaharness/__init__.py.sudo.md`.
- `from vvaharness import config as config_mod` at source line 31: `source_detail/vvaharness/config/__init__.py.sudo.md`.
- `from vvaharness.orchestrator import configure_backends` at source line 32: `source_detail/vvaharness/orchestrator/__init__.py.sudo.md`.
- `from vvaharness.orchestrator import _default_config` at source line 43: `source_detail/vvaharness/orchestrator/__init__.py.sudo.md`.
