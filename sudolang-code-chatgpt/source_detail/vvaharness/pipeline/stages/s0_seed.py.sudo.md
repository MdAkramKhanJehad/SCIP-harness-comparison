# vvaharness/pipeline/stages/s0_seed.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/pipeline/stages/s0_seed.py.evidence.json`. SHA-256: `168fed33e5dde7fc49830000be263a93f859a2daaea9c6be6d9f7f909b4f6912`.

```sudo
// Source: vvaharness/pipeline/stages/s0_seed.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from vvaharness.lang.detect import VVAH_LANGUAGES, canonical_lang, detect_languages; preserve alias and import-time effects. Then Resolve source import from vvaharness.models.scan import SeedPackage; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s0_seed.py:22-37
In source order: Resolve source import from vvaharness.scope import _walk_repo; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import console, logs; preserve alias and import-time effects. Then Evaluate once logs.get_logger(__name__); assign in source target order to log. Then For _KIND_HINTS, assign {'http': 'network', 'request': 'network', 'route': 'network', 'controller': 'network', 'servlet': 'network', 'handler': 'network', 'graphql': 'network', 'grpc': 'network', 'websocket': 'network', 'queue': 'ipc', 'kafka': 'ipc', 'jms': 'ipc', 'amqp': 'ipc', 'argv': 'cli', 'stdin': 'cli', 'flag': 'cli', 'env': 'file', 'config': 'file', 'fileread': 'file', 'deseriali': 'deserialization', 'unmarshal': 'deserialization', 'pickle': 'deserialization', 'yaml-load': 'deserialization'}; source annotation dict[str, str].
// Source: vvaharness/pipeline/stages/s0_seed.py:40-56
// Source signature: _filter_step0_languages(langs: list[str], cfg) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _filter_step0_languages(langs, cfg) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s0_seed.py:41-43
  In source order: Retain source documentation literal source_literal_41_4; it is not a model call. Then Evaluate once getattr(cfg, 'step0', None); assign in source target order to step0. Then Evaluate once getattr(step0, 'languages', None) if step0 is not None else None; assign in source target order to raw.
  // Source: vvaharness/pipeline/stages/s0_seed.py:44-45
  if (the source predicate not raw is truthy) {
    // Source: vvaharness/pipeline/stages/s0_seed.py:45-45
    End this invocation with langs.
  }
  // Source: vvaharness/pipeline/stages/s0_seed.py:46-46
  In source order: For allow, assign set(); source annotation set[str].
  // Source: vvaharness/pipeline/stages/s0_seed.py:47-55
  for each x in raw {
    // Source: vvaharness/pipeline/stages/s0_seed.py:48-49
    if (the source predicate not str(x).strip() is truthy) {
      // Source: vvaharness/pipeline/stages/s0_seed.py:49-49
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/pipeline/stages/s0_seed.py:50-51
    In source order: Evaluate once canonical_lang(x); assign in source target order to canon. Then Evaluate allow.add(canon); retain side effects and discard the expression result.
    // Source: vvaharness/pipeline/stages/s0_seed.py:53-55
    if (the source predicate canon not in VVAH_LANGUAGES is truthy) {
      // Source: vvaharness/pipeline/stages/s0_seed.py:54-55
      In source order: Evaluate console.write(source_template_54_26); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/pipeline/stages/s0_seed.py:56-56
  End this invocation with [l for l in langs if l in allow].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s0_seed.py:59-79
// Source signature: run(repo_root: str, cfg, ckpt_dir: Path | None=None) -> SeedPackage
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn run(repo_root, cfg, ckpt_dir) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s0_seed.py:60-64
  In source order: Retain source documentation literal source_literal_60_4; it is not a model call. Then Evaluate log.info('s0/seed: starting AST-based seed generation for %s', repo_root); retain side effects and discard the expression result. Then Evaluate once _walk_repo(repo_root, cfg); assign in source target order to (all_files, excluded). Then Evaluate once set(all_files); assign in source target order to in_scope. Then Evaluate once _filter_step0_languages(detect_languages(all_files), cfg); assign in source target order to langs.
  // Source: vvaharness/pipeline/stages/s0_seed.py:65-78
  In source order: Evaluate log.info('s0/seed: file walk complete - total=%d excluded=%d in_scope=%d langs=%s', len(all_files) + len(excluded), len(excluded), len(in_scope), langs); retain side effects and discard the expression result. Then Resolve source import from vvaharness.detect import scan as _detect_scan; preserve alias and import-time effects. Then Evaluate once _detect_scan(Path(repo_root), sorted(in_scope)); assign in source target order to result. Then Evaluate once SeedPackage(entry_points=result.entry_points, unsafe_sinks=result.unsafe_sinks, languages=langs, all_files=all_files, excluded=excluded); assign in source target order to seed. Then Evaluate log.info('s0/seed: seed generation complete - entry_points=%d sinks=%d paths=%d', len(seed.entry_points), len(seed.unsafe_sinks), len(seed.taint_paths)); retain side effects and discard the expression result.
  // Source: vvaharness/pipeline/stages/s0_seed.py:79-79
  End this invocation with seed.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.lang.detect import VVAH_LANGUAGES, canonical_lang, detect_languages` at source line 20: `source_detail/vvaharness/lang/detect.py.sudo.md`.
- `from vvaharness.models.scan import SeedPackage` at source line 21: `source_detail/vvaharness/models/scan/__init__.py.sudo.md`.
- `from vvaharness.scope import _walk_repo` at source line 22: `source_detail/vvaharness/scope/__init__.py.sudo.md`.
- `from vvaharness.util import console, logs` at source line 23: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import console, logs` at source line 23: `source_detail/vvaharness/util/console.py.sudo.md`.
- `from vvaharness.util import console, logs` at source line 23: `source_detail/vvaharness/util/logs.py.sudo.md`.
- `from vvaharness.detect import scan as _detect_scan` at source line 68: `source_detail/vvaharness/detect/__init__.py.sudo.md`.
