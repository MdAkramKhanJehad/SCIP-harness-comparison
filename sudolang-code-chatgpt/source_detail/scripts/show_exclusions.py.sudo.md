# scripts/show_exclusions.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/scripts/show_exclusions.py.evidence.json`. SHA-256: `0f843035277ce6e840fd0fb169c83ba825346f804753d562c0d87869e360dee1`.

```sudo
// Source: scripts/show_exclusions.py:15-24
In source order: Resolve source import import sys; preserve alias and import-time effects. Then Resolve source import from vvaharness import config as cm; preserve alias and import-time effects. Then Resolve source import from vvaharness.orchestrator import _default_config; preserve alias and import-time effects. Then Resolve source import from vvaharness.scope import _DEFAULT_EXCLUDE_DIRS, _DEFAULT_EXCLUDE_EXTS, _DEFAULT_EXCLUDE_GLOBS, _exclusion_sets; preserve alias and import-time effects. Then Evaluate once cm.load(_default_config()); assign in source target order to cfg.
// Source: scripts/show_exclusions.py:25-30
In source order: Evaluate once _exclusion_sets(cfg); assign in source target order to (dirs, exts, globs). Then Evaluate once {d.lower() for d in getattr(cfg.step1, 'exclude_dirs', None) or []}; assign in source target order to cfg_dirs. Then Evaluate once set(getattr(cfg.step1, 'exclude_exts', None) or []); assign in source target order to cfg_exts. Then Evaluate once set(getattr(cfg.step1, 'exclude_globs', None) or []); assign in source target order to cfg_globs. Then Evaluate once {d.lower() for d in _DEFAULT_EXCLUDE_DIRS}; assign in source target order to def_dirs.
// Source: scripts/show_exclusions.py:33-36
// Source signature: tag(x, in_default, in_cfg)
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn tag(x, in_default, in_cfg) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: scripts/show_exclusions.py:34-34
  if (the source predicate in_default and in_cfg is truthy) {
    // Source: scripts/show_exclusions.py:34-34
    End this invocation with 'both   '.
  }
  // Source: scripts/show_exclusions.py:35-35
  if (the source predicate in_cfg is truthy) {
    // Source: scripts/show_exclusions.py:35-35
    End this invocation with 'config '.
  }
  // Source: scripts/show_exclusions.py:36-36
  End this invocation with 'builtin'.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: scripts/show_exclusions.py:39-39
In source order: Evaluate print(source_template_39_6); retain side effects and discard the expression result.
// Source: scripts/show_exclusions.py:40-41
for each x in sorted(dirs) {
  // Source: scripts/show_exclusions.py:41-41
  In source order: Evaluate print(source_template_41_10); retain side effects and discard the expression result.
}
// Source: scripts/show_exclusions.py:43-43
In source order: Evaluate print(source_template_43_6); retain side effects and discard the expression result.
// Source: scripts/show_exclusions.py:44-45
for each x in sorted(exts) {
  // Source: scripts/show_exclusions.py:45-45
  In source order: Evaluate print(source_template_45_10); retain side effects and discard the expression result.
}
// Source: scripts/show_exclusions.py:47-47
In source order: Evaluate print(source_template_47_6); retain side effects and discard the expression result.
// Source: scripts/show_exclusions.py:48-49
for each g in globs {
  // Source: scripts/show_exclusions.py:49-49
  In source order: Evaluate print(source_template_49_10); retain side effects and discard the expression result.
}
// Source: scripts/show_exclusions.py:51-56
In source order: Evaluate print(source_template_51_6); retain side effects and discard the expression result. Then Evaluate print(source_template_52_6); retain side effects and discard the expression result. Then Evaluate once []; assign in source target order to warn.
// Source: scripts/show_exclusions.py:57-59
for each e in sorted(exts) {
  // Source: scripts/show_exclusions.py:58-59
  if (the source predicate not e.startswith('.') is truthy) {
    // Source: scripts/show_exclusions.py:59-59
    In source order: Evaluate warn.append(source_template_59_20); retain side effects and discard the expression result.
  }
}
// Source: scripts/show_exclusions.py:60-60
In source order: Evaluate once {}; assign in source target order to seen.
// Source: scripts/show_exclusions.py:61-63
for each e in exts {
  // Source: scripts/show_exclusions.py:62-63
  In source order: Evaluate once e.lower(); assign in source target order to k. Then Evaluate seen.setdefault(k, []).append(e); retain side effects and discard the expression result.
}
// Source: scripts/show_exclusions.py:64-66
for each (k, v) in seen.items() {
  // Source: scripts/show_exclusions.py:65-66
  if (the source predicate len(v) > 1 is truthy) {
    // Source: scripts/show_exclusions.py:66-66
    In source order: Evaluate warn.append(source_template_66_20); retain side effects and discard the expression result.
  }
}
// Source: scripts/show_exclusions.py:67-69
if (the source predicate warn is truthy) {
  // Source: scripts/show_exclusions.py:68-69
  In source order: Evaluate print(source_literal_68_10); retain side effects and discard the expression result. Then Evaluate print(source_literal_69_10.join(warn)); retain side effects and discard the expression result.
}
```

## Local import links

- `from vvaharness import config as cm` at source line 17: `source_detail/vvaharness/__init__.py.sudo.md`.
- `from vvaharness import config as cm` at source line 17: `source_detail/vvaharness/config/__init__.py.sudo.md`.
- `from vvaharness.orchestrator import _default_config` at source line 18: `source_detail/vvaharness/orchestrator/__init__.py.sudo.md`.
- `from vvaharness.scope import _DEFAULT_EXCLUDE_DIRS, _DEFAULT_EXCLUDE_EXTS, _DEFAULT_EXCLUDE_GLOBS, _exclusion_sets` at source line 19: `source_detail/vvaharness/scope/__init__.py.sudo.md`.
