# vvaharness/evidence/configs.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/evidence/configs.py.evidence.json`. SHA-256: `9b3847f6d0f4bf50843d8c9ed7924aacfc9f9ae807b82e0f7219a32244869c7d`.

```sudo
// Source: vvaharness/evidence/configs.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from pathlib import Path, PurePosixPath; preserve alias and import-time effects. Then Resolve source import from vvaharness.evidence._grouping import _round_robin_select; preserve alias and import-time effects. Then Resolve source import from vvaharness.evidence.read import _cap_text, _read_capped; preserve alias and import-time effects.
// Source: vvaharness/evidence/configs.py:22-30
In source order: Resolve source import from vvaharness.lang.detect import SECURITY_CONFIG_NAMES; preserve alias and import-time effects. Then Resolve source import from vvaharness.report.redact import redact; preserve alias and import-time effects. Then Resolve source import from vvaharness.scope.configs import _rep_score; preserve alias and import-time effects. Then Evaluate once {'.yml', '.yaml', '.json', '.toml', '.ini', '.properties', '.conf', '.cfg', '.env'}; assign in source target order to _CONFIG_EXTS. Then Evaluate once 500000; assign in source target order to _CONFIG_REP_RAW_CEILING.
// Source: vvaharness/evidence/configs.py:33-53
// Source signature: _select_config_reps(full_files: list[str], max_reps: int) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _select_config_reps(full_files, max_reps) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/evidence/configs.py:34-35
  In source order: Retain source documentation literal source_literal_34_4; it is not a model call. Then For by_dir, assign {}; source annotation dict[str, list[str]].
  // Source: vvaharness/evidence/configs.py:36-42
  for each rel in full_files {
    // Source: vvaharness/evidence/configs.py:37-39
    In source order: Evaluate once PurePosixPath(rel); assign in source target order to p. Then Evaluate once p.suffix.lower(); assign in source target order to suffix. Then Evaluate once p.name.lower(); assign in source target order to name.
    // Source: vvaharness/evidence/configs.py:40-42
    if (the source predicate suffix in _CONFIG_EXTS or name in _CONFIG_EXTS or name in SECURITY_CONFIG_NAMES is truthy) {
      // Source: vvaharness/evidence/configs.py:41-42
      In source order: Evaluate once str(p.parent) if str(p.parent) != '.' else ''; assign in source target order to parent. Then Evaluate by_dir.setdefault(parent, []).append(rel); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/evidence/configs.py:44-50
  for each d in by_dir {
    // Source: vvaharness/evidence/configs.py:46-50
    In source order: Evaluate by_dir[d].sort(key=lambda f: (PurePosixPath(f).name.lower() not in SECURITY_CONFIG_NAMES, _rep_score(f, 0)[0], f)); retain side effects and discard the expression result.
  }
  // Source: vvaharness/evidence/configs.py:52-52
  In source order: Evaluate once _round_robin_select(by_dir, max_reps, keys=sorted(by_dir)); assign in source target order to pairs.
  // Source: vvaharness/evidence/configs.py:53-53
  End this invocation with [rel for _dir, rel in pairs].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/evidence/configs.py:56-74
// Source signature: _config_rep_contents(root: Path, rel_paths: list[str], cap_chars: int, max_bodies: int) -> list[tuple[str, str]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _config_rep_contents(root, rel_paths, cap_chars, max_bodies) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/evidence/configs.py:58-64
  In source order: Retain source documentation literal source_literal_58_4; it is not a model call. Then For reps, assign []; source annotation list[tuple[str, str]]. Then Evaluate once max(_CONFIG_REP_RAW_CEILING, cap_chars * 4); assign in source target order to read_ceiling. Then Evaluate once frozenset(sorted(rel_paths, key=lambda r: PurePosixPath(r).name.lower() not in SECURITY_CONFIG_NAMES)[:max(max_bodies, 0)]); assign in source target order to with_bodies.
  // Source: vvaharness/evidence/configs.py:65-73
  for each rel in rel_paths {
    // Source: vvaharness/evidence/configs.py:66-66
    In source order: Evaluate once ''; assign in source target order to body.
    // Source: vvaharness/evidence/configs.py:67-72
    if (the source predicate cap_chars > 0 and rel in with_bodies is truthy) {
      // Source: vvaharness/evidence/configs.py:69-70
      In source order: Evaluate once _read_capped(root, root / rel, read_ceiling, whole_or_nothing=True); assign in source target order to raw.
      // Source: vvaharness/evidence/configs.py:71-72
      if (the source predicate raw is truthy) {
        // Source: vvaharness/evidence/configs.py:72-72
        In source order: Evaluate once _cap_text(redact(raw), cap_chars); assign in source target order to body.
      }
    }
    // Source: vvaharness/evidence/configs.py:73-73
    In source order: Evaluate reps.append((rel, body)); retain side effects and discard the expression result.
  }
  // Source: vvaharness/evidence/configs.py:74-74
  End this invocation with reps.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/evidence/configs.py:77-81
// Source signature: gather_config_reps(root: Path, full_files: list[str], max_reps: int, cap_chars: int, max_bodies: int) -> list[tuple[str, str]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn gather_config_reps(root, full_files, max_reps, cap_chars, max_bodies) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/evidence/configs.py:79-79
  In source order: Retain source documentation literal source_literal_79_4; it is not a model call.
  // Source: vvaharness/evidence/configs.py:80-81
  End this invocation with _config_rep_contents(root, _select_config_reps(full_files, max_reps), cap_chars, max_bodies).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.evidence._grouping import _round_robin_select` at source line 20: `source_detail/vvaharness/evidence/_grouping.py.sudo.md`.
- `from vvaharness.evidence.read import _cap_text, _read_capped` at source line 21: `source_detail/vvaharness/evidence/read.py.sudo.md`.
- `from vvaharness.lang.detect import SECURITY_CONFIG_NAMES` at source line 22: `source_detail/vvaharness/lang/detect.py.sudo.md`.
- `from vvaharness.report.redact import redact` at source line 23: `source_detail/vvaharness/report/redact.py.sudo.md`.
- `from vvaharness.scope.configs import _rep_score` at source line 24: `source_detail/vvaharness/scope/configs.py.sudo.md`.
