# vvaharness/pipeline/stages/s1_preprocess.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/pipeline/stages/s1_preprocess.py.evidence.json`. SHA-256: `5e56808364c59b4fe2ce3f74156ec0bec242bd9f85edc3318a3e09834c342bb4`.

```sudo
// Source: vvaharness/pipeline/stages/s1_preprocess.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import logs; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm import tools as _localtools; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s1_preprocess.py:22-36
In source order: Resolve source import from vvaharness.codegraph import GraphHandle, communities_as_modules, primary_language, system_context_notes; preserve alias and import-time effects. Then Resolve source import from vvaharness.lang.detect import EXT_TO_LANG; preserve alias and import-time effects. Then Resolve source import from vvaharness.models import CVE, ContextPackage, Control; preserve alias and import-time effects. Then Resolve source import from vvaharness.scope import EmptyScopeError, _dedup_configs, _resolve_scope_path, _walk_repo; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import console; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s1_preprocess.py:37-44
In source order: Resolve source import from vvaharness.util import errlog as _errlog; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.events import Event; preserve alias and import-time effects. Then Evaluate once logs.get_logger(__name__); assign in source target order to log. Then Evaluate once '::'; assign in source target order to QSEP. Then Evaluate once '<module>'; assign in source target order to MODULE_SCOPE.
// Source: vvaharness/pipeline/stages/s1_preprocess.py:47-48
// Source signature: q_join(file: str, name: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn q_join(file, name) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s1_preprocess.py:48-48
  End this invocation with source_template_48_11.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s1_preprocess.py:51-55
// Source signature: q_split(qname: str) -> tuple[str, str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn q_split(qname) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s1_preprocess.py:52-54
  if (the source predicate QSEP in qname is truthy) {
    // Source: vvaharness/pipeline/stages/s1_preprocess.py:53-53
    In source order: Evaluate once qname.rpartition(QSEP); assign in source target order to (f, _, n).
    // Source: vvaharness/pipeline/stages/s1_preprocess.py:54-54
    End this invocation with (f, n).
  }
  // Source: vvaharness/pipeline/stages/s1_preprocess.py:55-55
  End this invocation with ('', qname).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s1_preprocess.py:58-59
// Source signature: q_file(qname: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn q_file(qname) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s1_preprocess.py:59-59
  End this invocation with q_split(qname)[0].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s1_preprocess.py:62-63
// Source signature: q_name(qname: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn q_name(qname) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s1_preprocess.py:63-63
  End this invocation with q_split(qname)[1].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s1_preprocess.py:66-73
// Source signature: _modules_from_graph(graph_handle: GraphHandle, resolve_in_scope) -> list[dict]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _modules_from_graph(graph_handle, resolve_in_scope) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s1_preprocess.py:67-68
  In source order: Retain source documentation literal source_literal_67_4; it is not a model call. Then For modules, assign []; source annotation list[dict].
  // Source: vvaharness/pipeline/stages/s1_preprocess.py:69-72
  for each (name, files) in communities_as_modules(graph_handle).items() {
    // Source: vvaharness/pipeline/stages/s1_preprocess.py:70-70
    In source order: Evaluate once sorted({hit for f in files if (hit := resolve_in_scope(f))}); assign in source target order to in_scope.
    // Source: vvaharness/pipeline/stages/s1_preprocess.py:71-72
    if (the source predicate in_scope is truthy) {
      // Source: vvaharness/pipeline/stages/s1_preprocess.py:72-72
      In source order: Evaluate modules.append({'name': name, 'files': in_scope}); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/pipeline/stages/s1_preprocess.py:73-73
  End this invocation with modules.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s1_preprocess.py:76-207
// Source signature: run(repo_root: str, cfg, known_cves: list[CVE], controls: list[Control], seed=None, graph_handle: GraphHandle | None=None) -> ContextPackage
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn run(repo_root, cfg, known_cves, controls, seed, graph_handle) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s1_preprocess.py:78-78
  In source order: Retain source documentation literal source_literal_78_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s1_preprocess.py:80-83
  if (the source predicate seed is not None and getattr(seed, 'all_files', None) is truthy) {
    // Source: vvaharness/pipeline/stages/s1_preprocess.py:81-81
    In source order: Evaluate once (list(seed.all_files), dict(seed.excluded)); assign in source target order to (all_files, excluded).
  }
  else {
    // Source: vvaharness/pipeline/stages/s1_preprocess.py:83-83
    In source order: Evaluate once _walk_repo(repo_root, cfg); assign in source target order to (all_files, excluded).
  }
  // Source: vvaharness/pipeline/stages/s1_preprocess.py:85-88
  In source order: Evaluate _localtools.set_scope(repo_root, all_files); retain side effects and discard the expression result. Then Evaluate once _dedup_configs(all_files, Path(repo_root), cfg); assign in source target order to (all_files, dedup_report). Then Evaluate once dedup_report; assign in source target order to excluded['config_dedup']. Then Evaluate once getattr(cfg, '_scan_progress', None); assign in source target order to tracker.
  // Source: vvaharness/pipeline/stages/s1_preprocess.py:89-90
  if (the source predicate tracker is not None is truthy) {
    // Source: vvaharness/pipeline/stages/s1_preprocess.py:90-90
    In source order: Evaluate tracker.discovered(all_files); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s1_preprocess.py:93-99
  In source order: Evaluate once set(all_files); assign in source target order to keep. Then Evaluate once sorted((d.name for d in Path(repo_root).iterdir() if d.is_dir() and d.name not in ('checkpoints', 'security-scan'))); assign in source target order to top_dirs. Then For ambiguous, assign []; source annotation list[str].
  // Source: vvaharness/pipeline/stages/s1_preprocess.py:101-105
  // Source signature: _resolve_in_scope(path: str) -> str | None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _resolve_in_scope(path) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/pipeline/stages/s1_preprocess.py:102-102
    In source order: Evaluate once _resolve_scope_path(path, repo_root, keep, top_dirs); assign in source target order to (hit, amb).
    // Source: vvaharness/pipeline/stages/s1_preprocess.py:103-104
    if (the source predicate amb is truthy) {
      // Source: vvaharness/pipeline/stages/s1_preprocess.py:104-104
      In source order: Evaluate ambiguous.append(path); retain side effects and discard the expression result.
    }
    // Source: vvaharness/pipeline/stages/s1_preprocess.py:105-105
    End this invocation with hit.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/pipeline/stages/s1_preprocess.py:107-107
  In source order: For data, assign {'unsafe_sinks': [], 'entry_points': []}; source annotation dict.
  // Source: vvaharness/pipeline/stages/s1_preprocess.py:109-147
  if (the source predicate seed is truthy) {
    // Source: vvaharness/pipeline/stages/s1_preprocess.py:110-119
    In source order: Evaluate once [dict(s.model_dump(), file=hit) for s in seed.unsafe_sinks if (hit := _resolve_in_scope(s.file))]; assign in source target order to seed_sinks. Then Evaluate once [dict(e.model_dump(), file=hit) for e in seed.entry_points if (hit := _resolve_in_scope(e.file))]; assign in source target order to seed_eps. Then Evaluate data['unsafe_sinks'].extend(seed_sinks); retain side effects and discard the expression result. Then Evaluate data['entry_points'].extend(seed_eps); retain side effects and discard the expression result. Then Evaluate log.info('s1/preprocess: merged s0 seed - sinks=%d entry_points=%d', len(seed_sinks), len(seed_eps)); retain side effects and discard the expression result.
    // Source: vvaharness/pipeline/stages/s1_preprocess.py:121-121
    In source order: For seed_paths, assign []; source annotation list[list[str]].
    // Source: vvaharness/pipeline/stages/s1_preprocess.py:122-130
    for each path in getattr(seed, 'taint_paths', None) or [] {
      // Source: vvaharness/pipeline/stages/s1_preprocess.py:123-123
      In source order: Evaluate once []; assign in source target order to resolved.
      // Source: vvaharness/pipeline/stages/s1_preprocess.py:124-128
      for each hop in path {
        // Source: vvaharness/pipeline/stages/s1_preprocess.py:125-126
        In source order: Evaluate once hop.rpartition(':'); assign in source target order to (f, sep, ln). Then Evaluate once _resolve_in_scope(f or hop); assign in source target order to hit.
        // Source: vvaharness/pipeline/stages/s1_preprocess.py:127-128
        if (the source predicate hit is truthy) {
          // Source: vvaharness/pipeline/stages/s1_preprocess.py:128-128
          In source order: Evaluate resolved.append(source_template_128_36 if sep else hit); retain side effects and discard the expression result.
        }
      }
      // Source: vvaharness/pipeline/stages/s1_preprocess.py:129-130
      if (the source predicate len(resolved) >= 2 is truthy) {
        // Source: vvaharness/pipeline/stages/s1_preprocess.py:130-130
        In source order: Evaluate seed_paths.append(resolved); retain side effects and discard the expression result.
      }
    }
    // Source: vvaharness/pipeline/stages/s1_preprocess.py:131-135
    In source order: Evaluate once seed_paths; assign in source target order to data['seed_taint_paths']. Then Evaluate log.debug('s1/preprocess: seed taint paths processed - paths=%d', len(seed_paths)); retain side effects and discard the expression result. Then For framework_unresolvable, assign set(); source annotation set[str].
    // Source: vvaharness/pipeline/stages/s1_preprocess.py:136-138
    for each ep in getattr(seed, 'entry_points', []) or [] {
      // Source: vvaharness/pipeline/stages/s1_preprocess.py:137-138
      if (the source predicate getattr(ep, 'kind', '').lower() == 'framework' and (not _resolve_in_scope(ep.file)) is truthy) {
        // Source: vvaharness/pipeline/stages/s1_preprocess.py:138-138
        In source order: Evaluate framework_unresolvable.add(source_template_138_43); retain side effects and discard the expression result.
      }
    }
    // Source: vvaharness/pipeline/stages/s1_preprocess.py:139-143
    if (the source predicate framework_unresolvable is truthy) {
      // Source: vvaharness/pipeline/stages/s1_preprocess.py:140-143
      In source order: Evaluate once ', '.join(sorted(framework_unresolvable)[:3]); assign in source target order to sample. Then Evaluate once source_template_141_20 if len(framework_unresolvable) > 3 else ''; assign in source target order to n_str. Then Evaluate log.warning(Event.S1_FRAMEWORK_ENTRY_UNRESOLVED, count=len(framework_unresolvable), sample=source_template_143_31); retain side effects and discard the expression result.
    }
    // Source: vvaharness/pipeline/stages/s1_preprocess.py:145-147
    if (the source predicate seed_sinks or seed_eps or seed_paths is truthy) {
      // Source: vvaharness/pipeline/stages/s1_preprocess.py:146-147
      In source order: Evaluate console.write(source_template_146_26); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/pipeline/stages/s1_preprocess.py:149-152
  if (the source predicate ambiguous is truthy) {
    // Source: vvaharness/pipeline/stages/s1_preprocess.py:150-152
    In source order: Evaluate once sorted(set(ambiguous)); assign in source target order to uniq. Then Evaluate once ', '.join(uniq[:5]) + ('…' if len(uniq) > 5 else ''); assign in source target order to sample. Then Evaluate log.warning(Event.S1_AMBIGUOUS_PATHS_DROPPED, count=len(ambiguous), sample=sample); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s1_preprocess.py:154-154
  In source order: Evaluate once repo_root; assign in source target order to data['repo_root'].
  // Source: vvaharness/pipeline/stages/s1_preprocess.py:155-161
  if (the source predicate graph_handle is not None is truthy) {
    // Source: vvaharness/pipeline/stages/s1_preprocess.py:156-158
    In source order: Evaluate once primary_language(graph_handle); assign in source target order to data['language']. Then Evaluate once _modules_from_graph(graph_handle, _resolve_in_scope); assign in source target order to data['modules']. Then Evaluate once system_context_notes(graph_handle); assign in source target order to data['notes'].
  }
  else {
    // Source: vvaharness/pipeline/stages/s1_preprocess.py:160-161
    In source order: Evaluate once []; assign in source target order to data['modules']. Then Evaluate once ''; assign in source target order to data['notes'].
  }
  // Source: vvaharness/pipeline/stages/s1_preprocess.py:163-170
  if (the source predicate not data.get('language') is truthy) {
    // Source: vvaharness/pipeline/stages/s1_preprocess.py:164-164
    In source order: For ext_counts, assign {}; source annotation dict[str, int].
    // Source: vvaharness/pipeline/stages/s1_preprocess.py:165-168
    for each f in all_files {
      // Source: vvaharness/pipeline/stages/s1_preprocess.py:166-166
      In source order: Evaluate once EXT_TO_LANG.get(Path(f).suffix.lower()); assign in source target order to lang.
      // Source: vvaharness/pipeline/stages/s1_preprocess.py:167-168
      if (the source predicate lang is truthy) {
        // Source: vvaharness/pipeline/stages/s1_preprocess.py:168-168
        In source order: Evaluate once ext_counts.get(lang, 0) + 1; assign in source target order to ext_counts[lang].
      }
    }
    // Source: vvaharness/pipeline/stages/s1_preprocess.py:169-170
    In source order: Evaluate once max(ext_counts, key=lambda k: ext_counts[k]) if ext_counts else 'unknown'; assign in source target order to data['language'].
  }
  // Source: vvaharness/pipeline/stages/s1_preprocess.py:171-177
  In source order: Evaluate once all_files; assign in source target order to data['all_files']. Then Evaluate once excluded; assign in source target order to data['excluded']. Then Evaluate once [c.model_dump() for c in known_cves]; assign in source target order to data['known_cves']. Then Evaluate once [c.model_dump() for c in controls]; assign in source target order to data['design_controls']. Then Evaluate once ContextPackage.model_validate(data); assign in source target order to pkg.
  // Source: vvaharness/pipeline/stages/s1_preprocess.py:178-182
  In source order: Evaluate once sum(excluded['dirs'].values()); assign in source target order to n_ex_dirs. Then Evaluate once sum(excluded['exts'].values()); assign in source target order to n_ex_exts. Then Evaluate once sum(excluded['globs'].values()); assign in source target order to n_ex_globs. Then Evaluate once excluded['oversize']; assign in source target order to n_ex_size. Then Evaluate once (excluded.get('config_dedup') or {}).get('dropped', 0) or 0; assign in source target order to n_ex_dedup.
  // Source: vvaharness/pipeline/stages/s1_preprocess.py:183-190
  In source order: Evaluate once len(pkg.all_files); assign in source target order to n_in_scope. Then Evaluate once n_in_scope + n_ex_dirs + n_ex_exts + n_ex_globs + n_ex_size + n_ex_dedup; assign in source target order to n_total. Then Evaluate console.write(source_template_185_18); retain side effects and discard the expression result. Then Evaluate console.counts('s1', 'done', modules=len(pkg.modules), entry_points=len(pkg.entry_points), sinks=len(pkg.unsafe_sinks), files_in_scope=n_in_scope); retain side effects and discard the expression result.
  // Source: vvaharness/pipeline/stages/s1_preprocess.py:192-198
  if (the source predicate not n_in_scope is truthy) {
    // Source: vvaharness/pipeline/stages/s1_preprocess.py:193-198
    Raise EmptyScopeError(source_template_194_12).
  }
  // Source: vvaharness/pipeline/stages/s1_preprocess.py:200-206
  if (the source predicate n_in_scope and (not pkg.modules) and (not pkg.entry_points) and (not pkg.unsafe_sinks) is truthy) {
    // Source: vvaharness/pipeline/stages/s1_preprocess.py:202-206
    In source order: Evaluate _errlog.log('s1', 'context-package', source_template_203_20, reason='s1_zero_output', files_in_scope=n_in_scope); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s1_preprocess.py:207-207
  End this invocation with pkg.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.util import logs` at source line 17: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import logs` at source line 17: `source_detail/vvaharness/util/logs.py.sudo.md`.
- `from vvaharness.backends.llm import tools as _localtools` at source line 21: `source_detail/vvaharness/backends/llm/__init__.py.sudo.md`.
- `from vvaharness.backends.llm import tools as _localtools` at source line 21: `source_detail/vvaharness/backends/llm/tools.py.sudo.md`.
- `from vvaharness.codegraph import GraphHandle, communities_as_modules, primary_language, system_context_notes` at source line 22: `source_detail/vvaharness/codegraph/__init__.py.sudo.md`.
- `from vvaharness.lang.detect import EXT_TO_LANG` at source line 28: `source_detail/vvaharness/lang/detect.py.sudo.md`.
- `from vvaharness.models import CVE, ContextPackage, Control` at source line 29: `source_detail/vvaharness/models/__init__.py.sudo.md`.
- `from vvaharness.scope import EmptyScopeError, _dedup_configs, _resolve_scope_path, _walk_repo` at source line 30: `source_detail/vvaharness/scope/__init__.py.sudo.md`.
- `from vvaharness.util import console` at source line 36: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import console` at source line 36: `source_detail/vvaharness/util/console.py.sudo.md`.
- `from vvaharness.util import errlog as _errlog` at source line 37: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import errlog as _errlog` at source line 37: `source_detail/vvaharness/util/errlog.py.sudo.md`.
- `from vvaharness.util.events import Event` at source line 38: `source_detail/vvaharness/util/events.py.sudo.md`.
