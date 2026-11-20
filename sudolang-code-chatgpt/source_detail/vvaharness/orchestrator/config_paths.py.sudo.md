# vvaharness/orchestrator/config_paths.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/orchestrator/config_paths.py.evidence.json`. SHA-256: `7cffdd3d6f9affee62fb6282aa8de97c0af240ca6dbbabfc9996733fcf90556e`.

```sudo
// Source: vvaharness/orchestrator/config_paths.py:16-21
In source order: Retain source documentation literal source_literal_16_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import logs; preserve alias and import-time effects. Then Resolve source import import os; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects.
// Source: vvaharness/orchestrator/config_paths.py:23-29
In source order: Resolve source import from vvaharness.config import ConfigPolicyError, is_network_path; preserve alias and import-time effects. Then Resolve source import from vvaharness.exploit_verification.settings import EV_MODULES as _EV_MODULES; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.events import Event; preserve alias and import-time effects. Then Evaluate once logs.get_logger(__name__); assign in source target order to log.
// Source: vvaharness/orchestrator/config_paths.py:32-33
// Source signature: _app_root() -> Path
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _app_root() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/config_paths.py:33-33
  End this invocation with Path(__file__).resolve().parent.parent.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/config_paths.py:36-40
// Source signature: _default_config() -> Path
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _default_config() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/config_paths.py:37-37
  In source order: Evaluate once Path.cwd() / 'config.yaml'; assign in source target order to cwd_cfg.
  // Source: vvaharness/orchestrator/config_paths.py:38-39
  if (the source predicate cwd_cfg.exists() is truthy) {
    // Source: vvaharness/orchestrator/config_paths.py:39-39
    End this invocation with cwd_cfg.
  }
  // Source: vvaharness/orchestrator/config_paths.py:40-40
  End this invocation with _packaged_default().
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/config_paths.py:43-45
// Source signature: _packaged_default() -> Path
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _packaged_default() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/config_paths.py:44-44
  In source order: Retain source documentation literal source_literal_44_4; it is not a model call.
  // Source: vvaharness/orchestrator/config_paths.py:45-45
  End this invocation with _app_root() / 'config' / 'profiles' / 'default.yaml'.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/config_paths.py:48-67
// Source signature: _path_within(candidate, root) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _path_within(candidate, root) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/config_paths.py:49-49
  In source order: Retain source documentation literal source_literal_49_4; it is not a model call.
  // Source: vvaharness/orchestrator/config_paths.py:50-53
  Perform the following protected operations {
    // Source: vvaharness/orchestrator/config_paths.py:51-51
    In source order: Evaluate once (Path(candidate).resolve(), Path(root).resolve()); assign in source target order to (cand, base).
  }
  // Source: vvaharness/orchestrator/config_paths.py:52-53
  On the first matching source exception (OSError, RuntimeError), in handler order {
    // Source: vvaharness/orchestrator/config_paths.py:53-53
    End this invocation with False.
  }
  // Source: vvaharness/orchestrator/config_paths.py:54-55
  if (the source predicate cand.is_relative_to(base) is truthy) {
    // Source: vvaharness/orchestrator/config_paths.py:55-55
    End this invocation with True.
  }
  // Source: vvaharness/orchestrator/config_paths.py:57-60
  Perform the following protected operations {
    // Source: vvaharness/orchestrator/config_paths.py:58-58
    In source order: Evaluate once base.stat(); assign in source target order to base_st.
  }
  // Source: vvaharness/orchestrator/config_paths.py:59-60
  On the first matching source exception OSError, in handler order {
    // Source: vvaharness/orchestrator/config_paths.py:60-60
    End this invocation with False.
  }
  // Source: vvaharness/orchestrator/config_paths.py:61-66
  for each p in (cand, *cand.parents) {
    // Source: vvaharness/orchestrator/config_paths.py:62-66
    Perform the following protected operations {
      // Source: vvaharness/orchestrator/config_paths.py:63-64
      if (the source predicate os.path.samestat(p.stat(), base_st) is truthy) {
        // Source: vvaharness/orchestrator/config_paths.py:64-64
        End this invocation with True.
      }
    }
    // Source: vvaharness/orchestrator/config_paths.py:65-66
    On the first matching source exception OSError, in handler order {
      // Source: vvaharness/orchestrator/config_paths.py:66-66
      Continue the immediately enclosing source loop at its next iteration.
    }
  }
  // Source: vvaharness/orchestrator/config_paths.py:67-67
  End this invocation with False.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/config_paths.py:70-86
// Source signature: trusted_config(config: str, boundary: str | Path | None, *, explicit: bool, quiet: bool=False) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn trusted_config(config, boundary, explicit, quiet) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/config_paths.py:72-72
  In source order: Retain source documentation literal source_literal_72_4; it is not a model call.
  // Source: vvaharness/orchestrator/config_paths.py:74-75
  if (the source predicate boundary is None or os.environ.get('VVAHARNESS_ALLOW_CWD_CONFIG') is truthy) {
    // Source: vvaharness/orchestrator/config_paths.py:75-75
    End this invocation with config.
  }
  // Source: vvaharness/orchestrator/config_paths.py:76-77
  if (the source predicate not _path_within(config, boundary) is truthy) {
    // Source: vvaharness/orchestrator/config_paths.py:77-77
    End this invocation with config.
  }
  // Source: vvaharness/orchestrator/config_paths.py:78-82
  if (the source predicate explicit is truthy) {
    // Source: vvaharness/orchestrator/config_paths.py:79-82
    Raise ConfigPolicyError(source_template_80_12).
  }
  // Source: vvaharness/orchestrator/config_paths.py:83-85
  if (the source predicate not quiet is truthy) {
    // Source: vvaharness/orchestrator/config_paths.py:84-85
    In source order: Evaluate log.warning(Event.CONFIG_INSIDE_TARGET, path=config, override='VVAHARNESS_ALLOW_CWD_CONFIG=1'); retain side effects and discard the expression result.
  }
  // Source: vvaharness/orchestrator/config_paths.py:86-86
  End this invocation with str(_packaged_default()).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/config_paths.py:89-101
// Source signature: _resolve_against(base: Path, p: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _resolve_against(base, p) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/config_paths.py:91-94
  if (the source predicate is_network_path(p) is truthy) {
    // Source: vvaharness/orchestrator/config_paths.py:92-94
    Raise ValueError(source_template_93_12).
  }
  // Source: vvaharness/orchestrator/config_paths.py:95-96
  In source order: Evaluate once Path(p); assign in source target order to pp. Then Evaluate once pp if pp.is_absolute() else base / pp; assign in source target order to resolved.
  // Source: vvaharness/orchestrator/config_paths.py:97-100
  if (the source predicate is_network_path(resolved) is truthy) {
    // Source: vvaharness/orchestrator/config_paths.py:98-100
    Raise ValueError(source_template_99_12).
  }
  // Source: vvaharness/orchestrator/config_paths.py:101-101
  End this invocation with str(resolved).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/config_paths.py:105-110
In source order: Evaluate once ('graph_annotate', 'callgraph_creation', 'autoexclude', 'preprocess', 'threatmodel', 'decompose', 'deepdive', 'verify', 'dedup', 'chain', 'remediate', 'validate', 'exploit_verification'); assign in source target order to _MODEL_ROLES. Then Evaluate once frozenset({'graph_annotate', 'callgraph_creation'}); assign in source target order to _CALLGRAPH_ROLES.
// Source: vvaharness/orchestrator/config_paths.py:113-119
// Source signature: _callgraph_llm_selected(cfg) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _callgraph_llm_selected(cfg) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/config_paths.py:114-118
  In source order: Retain source documentation literal source_literal_114_4; it is not a model call. Then Evaluate once getattr(cfg, 'step0', None); assign in source target order to step0. Then Evaluate once str(getattr(step0, 'callgraph_detection', 'rules') or 'rules').strip().lower(); assign in source target order to mode.
  // Source: vvaharness/orchestrator/config_paths.py:119-119
  End this invocation with mode == 'llm'.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/config_paths.py:123-130
In source order: For _SUB_ROLES, assign {'validate': ('orchestrator',), 'exploit_verification': _EV_MODULES}; source annotation dict[str, tuple[str, ...]]. Then For EV_MODEL_ROLES, assign tuple((source_template_130_4 for s in _SUB_ROLES['exploit_verification'])); source annotation tuple[str, ...].
// Source: vvaharness/orchestrator/config_paths.py:132-150
// Source signature: _iter_model_roles(cfg)
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _iter_model_roles(cfg) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/config_paths.py:133-133
  In source order: Retain source documentation literal source_literal_133_4; it is not a model call.
  // Source: vvaharness/orchestrator/config_paths.py:134-150
  for each r in _MODEL_ROLES {
    // Source: vvaharness/orchestrator/config_paths.py:135-136
    if (the source predicate r in _CALLGRAPH_ROLES and (not _callgraph_llm_selected(cfg)) is truthy) {
      // Source: vvaharness/orchestrator/config_paths.py:136-136
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/orchestrator/config_paths.py:137-137
    In source order: Evaluate once getattr(cfg.models, r, None); assign in source target order to m.
    // Source: vvaharness/orchestrator/config_paths.py:138-139
    if (the source predicate m is None is truthy) {
      // Source: vvaharness/orchestrator/config_paths.py:139-139
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/orchestrator/config_paths.py:140-140
    In source order: Evaluate once _SUB_ROLES.get(r); assign in source target order to subs.
    // Source: vvaharness/orchestrator/config_paths.py:141-143
    if (the source predicate subs is None is truthy) {
      // Source: vvaharness/orchestrator/config_paths.py:142-142
      In source order: Yield (r, m); suspend this generator until resumed.
      // Source: vvaharness/orchestrator/config_paths.py:143-143
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/orchestrator/config_paths.py:144-150
    for each sub in subs {
      // Source: vvaharness/orchestrator/config_paths.py:145-145
      In source order: Evaluate once getattr(m, sub, None); assign in source target order to node.
      // Source: vvaharness/orchestrator/config_paths.py:147-148
      if (the source predicate node is None is truthy) {
        // Source: vvaharness/orchestrator/config_paths.py:148-148
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/orchestrator/config_paths.py:150-150
      In source order: Yield (r if len(subs) == 1 else source_template_150_44, node); suspend this generator until resumed.
    }
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/config_paths.py:154-162
In source order: For ROLE_EFFORT_KEY, assign {'autoexclude': ('step1', 'auto_exclude_effort'), 'threatmodel': ('step2', 'effort'), 'deepdive': ('step4', 'effort'), 'verify': ('step6_verify', 'effort'), 'dedup': ('step7_dedup', 'effort'), 'chain': ('step8', 'effort'), 'validate': ('step_validate', 'effort')}; source annotation dict[str, tuple[str, str]].
// Source: vvaharness/orchestrator/config_paths.py:165-181
// Source signature: role_effort(cfg: object, role: str) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn role_effort(cfg, role) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/config_paths.py:166-166
  In source order: Retain source documentation literal source_literal_166_4; it is not a model call.
  // Source: vvaharness/orchestrator/config_paths.py:168-170
  if (the source predicate role.startswith('exploit_verification.') is truthy) {
    // Source: vvaharness/orchestrator/config_paths.py:169-169
    In source order: Resolve source import from vvaharness.exploit_verification.settings import ev_effort; preserve alias and import-time effects.
    // Source: vvaharness/orchestrator/config_paths.py:170-170
    End this invocation with ev_effort(cfg, role.split('.', 1)[1]).
  }
  // Source: vvaharness/orchestrator/config_paths.py:171-171
  In source order: Resolve source import from vvaharness.util.config import knob; preserve alias and import-time effects.
  // Source: vvaharness/orchestrator/config_paths.py:172-177
  if (the source predicate role == 'preprocess' is truthy) {
    // Source: vvaharness/orchestrator/config_paths.py:175-176
    if (the source predicate getattr(getattr(cfg, 'models', None), 'autoexclude', None) is not None is truthy) {
      // Source: vvaharness/orchestrator/config_paths.py:176-176
      End this invocation with None.
    }
    // Source: vvaharness/orchestrator/config_paths.py:177-177
    End this invocation with knob(cfg, 'step1.auto_exclude_effort', None) or None.
  }
  // Source: vvaharness/orchestrator/config_paths.py:178-178
  In source order: Evaluate once ROLE_EFFORT_KEY.get(role); assign in source target order to knob_path.
  // Source: vvaharness/orchestrator/config_paths.py:179-180
  if (the source predicate knob_path is None is truthy) {
    // Source: vvaharness/orchestrator/config_paths.py:180-180
    End this invocation with None.
  }
  // Source: vvaharness/orchestrator/config_paths.py:181-181
  End this invocation with knob(cfg, '.'.join(knob_path), None) or None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/config_paths.py:184-202
// Source signature: highest_effort(tiers) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn highest_effort(tiers) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/config_paths.py:185-191
  In source order: Retain source documentation literal source_literal_185_4; it is not a model call. Then Resolve source import from vvaharness.backends.llm.models import EFFORT_TIME_FACTOR, ClockKind; preserve alias and import-time effects. Then Evaluate once list(EFFORT_TIME_FACTOR[ClockKind.REQUEST]); assign in source target order to order. Then Evaluate once -1; assign in source target order to best_rank. Then For best, assign None; source annotation str | None.
  // Source: vvaharness/orchestrator/config_paths.py:192-201
  for each tier in tiers {
    // Source: vvaharness/orchestrator/config_paths.py:193-194
    if (the source predicate tier is None is truthy) {
      // Source: vvaharness/orchestrator/config_paths.py:194-194
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/orchestrator/config_paths.py:195-198
    Perform the following protected operations {
      // Source: vvaharness/orchestrator/config_paths.py:196-196
      In source order: Evaluate once order.index(tier); assign in source target order to rank.
    }
    // Source: vvaharness/orchestrator/config_paths.py:197-198
    On the first matching source exception ValueError, in handler order {
      // Source: vvaharness/orchestrator/config_paths.py:198-198
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/orchestrator/config_paths.py:199-201
    if (the source predicate rank > best_rank is truthy) {
      // Source: vvaharness/orchestrator/config_paths.py:200-201
      In source order: Evaluate once rank; assign in source target order to best_rank. Then Evaluate once str(tier); assign in source target order to best.
    }
  }
  // Source: vvaharness/orchestrator/config_paths.py:202-202
  End this invocation with best.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.util import logs` at source line 18: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import logs` at source line 18: `source_detail/vvaharness/util/logs.py.sudo.md`.
- `from vvaharness.config import ConfigPolicyError, is_network_path` at source line 23: `source_detail/vvaharness/config/__init__.py.sudo.md`.
- `from vvaharness.exploit_verification.settings import EV_MODULES as _EV_MODULES` at source line 26: `source_detail/vvaharness/exploit_verification/settings.py.sudo.md`.
- `from vvaharness.util.events import Event` at source line 27: `source_detail/vvaharness/util/events.py.sudo.md`.
- `from vvaharness.util.config import knob` at source line 171: `source_detail/vvaharness/util/config.py.sudo.md`.
- `from vvaharness.backends.llm.models import EFFORT_TIME_FACTOR, ClockKind` at source line 188: `source_detail/vvaharness/backends/llm/models.py.sudo.md`.
- `from vvaharness.exploit_verification.settings import ev_effort` at source line 169: `source_detail/vvaharness/exploit_verification/settings.py.sudo.md`.
