# vvaharness/pipeline/stages/s5/__init__.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/pipeline/stages/s5/__init__.py.evidence.json`. SHA-256: `504f76f6ec2c39949051b5b6a80ad9b919052d3a424acb243ee3d1fa132857de`.

```sudo
// Source: vvaharness/pipeline/stages/s5/__init__.py:15-23
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from vvaharness.models import ContextPackage, DroppedFinding, Finding; preserve alias and import-time effects. Then Resolve source import from vvaharness.pipeline.callgraph_consumer import entry_anchor_lines, seed_paths_by_file; preserve alias and import-time effects. Then Resolve source import from vvaharness.pipeline.stages import s7_dedup; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s5/__init__.py:24-28
In source order: Resolve source import from vvaharness.pipeline.stages.s5 import detectors, reanchor; preserve alias and import-time effects. Then Resolve source import from vvaharness.pipeline.stages.s5.enrich import FileCache, enrich; preserve alias and import-time effects. Then Resolve source import from vvaharness.pipeline.stages.s5.gates import reject, reject_path; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import console, logs; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.config import knob; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s5/__init__.py:29-31
In source order: Resolve source import from vvaharness.util.counters import COUNTERS; preserve alias and import-time effects. Then Evaluate once logs.get_logger(__name__); assign in source target order to log.
// Source: vvaharness/pipeline/stages/s5/__init__.py:34-37
// Source signature: _dropped(f: Finding, reason: str, detail: str) -> DroppedFinding
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _dropped(f, reason, detail) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s5/__init__.py:35-35
  In source order: Retain source documentation literal source_literal_35_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s5/__init__.py:36-37
  End this invocation with DroppedFinding(file=f.file, line=f.line_start, vuln_class=f.vuln_class, title=f.title, chunk_id=f.chunk_id, reason=reason, detail=detail).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s5/__init__.py:40-48
// Source signature: _line_tolerance(cfg) -> int
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _line_tolerance(cfg) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s5/__init__.py:41-45
  In source order: Retain source documentation literal source_literal_41_4; it is not a model call. Then Evaluate once getattr(cfg, 'step5_prefilter', None); assign in source target order to s5. Then Evaluate once getattr(cfg, 'step7_dedup', None); assign in source target order to s7. Then Evaluate once getattr(s5, 'line_tolerance', None); assign in source target order to tol.
  // Source: vvaharness/pipeline/stages/s5/__init__.py:46-47
  if (the source predicate tol is None is truthy) {
    // Source: vvaharness/pipeline/stages/s5/__init__.py:47-47
    In source order: Evaluate once getattr(s7, 'line_tolerance', 3); assign in source target order to tol.
  }
  // Source: vvaharness/pipeline/stages/s5/__init__.py:48-48
  End this invocation with int(tol).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s5/__init__.py:51-56
// Source signature: _breakdown(dropped: list[DroppedFinding]) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _breakdown(dropped) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s5/__init__.py:52-53
  In source order: Retain source documentation literal source_literal_52_4; it is not a model call. Then For by, assign {}; source annotation dict[str, int].
  // Source: vvaharness/pipeline/stages/s5/__init__.py:54-55
  for each d in dropped {
    // Source: vvaharness/pipeline/stages/s5/__init__.py:55-55
    In source order: Evaluate once by.get(d.reason, 0) + 1; assign in source target order to by[d.reason].
  }
  // Source: vvaharness/pipeline/stages/s5/__init__.py:56-56
  End this invocation with ', '.join((source_template_56_21 for k, n in sorted(by.items()))).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s5/__init__.py:59-119
// Source signature: run(findings: list[Finding], ctx: ContextPackage, cfg) -> tuple[list[Finding], list[DroppedFinding]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn run(findings, ctx, cfg) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s5/__init__.py:61-65
  In source order: Retain source documentation literal source_literal_61_4; it is not a model call. Then Evaluate log.info('s5/enrich: starting - findings=%d', len(findings)); retain side effects and discard the expression result. Then Evaluate once FileCache(ctx.repo_root, max_kb=int(knob(cfg, 'step1.max_file_kb', 1024))); assign in source target order to cache. Then Evaluate once set(ctx.all_files) if ctx.all_files else None; assign in source target order to valid_files. Then Evaluate once entry_anchor_lines(ctx); assign in source target order to anchors.
  // Source: vvaharness/pipeline/stages/s5/__init__.py:66-69
  In source order: Evaluate once seed_paths_by_file(ctx.seed_taint_paths); assign in source target order to seeds. Then Evaluate once _line_tolerance(cfg); assign in source target order to tol. Then Evaluate once None; assign in source target order to reanchorer.
  // Source: vvaharness/pipeline/stages/s5/__init__.py:70-73
  if (the source predicate knob(cfg, 'step5_prefilter.sink_reanchor', True) is truthy) {
    // Source: vvaharness/pipeline/stages/s5/__init__.py:71-73
    In source order: Evaluate once reanchor.Reanchorer(cache, reanchor.sink_patterns_by_cwe(), int(knob(cfg, 'step5_prefilter.sink_reanchor_max_move_lines', 40))); assign in source target order to reanchorer.
  }
  // Source: vvaharness/pipeline/stages/s5/__init__.py:75-78
  In source order: For keep, assign []; source annotation list[Finding]. Then For pre_anchor, assign []; source annotation list[int]. Then For dropped, assign []; source annotation list[DroppedFinding].
  // Source: vvaharness/pipeline/stages/s5/__init__.py:79-94
  for each raw in findings {
    // Source: vvaharness/pipeline/stages/s5/__init__.py:81-82
    In source order: Evaluate once raw; assign in source target order to f. Then Evaluate once reject_path(raw, valid_files); assign in source target order to verdict.
    // Source: vvaharness/pipeline/stages/s5/__init__.py:83-85
    if (the source predicate verdict is None is truthy) {
      // Source: vvaharness/pipeline/stages/s5/__init__.py:84-85
      In source order: Evaluate once enrich(raw, cache, anchors, seeds, reanchorer); assign in source target order to f. Then Evaluate once reject(f, valid_files, cache.lines(f.file)); assign in source target order to verdict.
    }
    // Source: vvaharness/pipeline/stages/s5/__init__.py:86-90
    if (the source predicate verdict is None is truthy) {
      // Source: vvaharness/pipeline/stages/s5/__init__.py:87-89
      In source order: Evaluate once int(raw.line_start); assign in source target order to f.pre_anchor_line. Then Evaluate keep.append(f); retain side effects and discard the expression result. Then Evaluate pre_anchor.append(int(raw.line_start)); retain side effects and discard the expression result.
      // Source: vvaharness/pipeline/stages/s5/__init__.py:90-90
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/pipeline/stages/s5/__init__.py:91-94
    In source order: Evaluate once verdict; assign in source target order to (reason, detail). Then Evaluate COUNTERS.bump(source_template_93_22); retain side effects and discard the expression result. Then Evaluate dropped.append(_dropped(f, reason, detail)); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s5/__init__.py:96-100
  In source order: Evaluate once s7_dedup.prefilter(keep, tol, pre_anchor); assign in source target order to (keep, dup_dropped). Then Evaluate dropped.extend(dup_dropped); retain side effects and discard the expression result. Then Evaluate once 0; assign in source target order to n_det.
  // Source: vvaharness/pipeline/stages/s5/__init__.py:101-112
  if (the source predicate knob(cfg, 'step5_detectors.enabled', True) is truthy) {
    // Source: vvaharness/pipeline/stages/s5/__init__.py:102-102
    In source order: Evaluate once int(knob(cfg, 'step5_detectors.max_rows', 200)); assign in source target order to max_rows.
    // Source: vvaharness/pipeline/stages/s5/__init__.py:103-112
    for each row in detectors.run(keep, ctx, cache, tol, max_rows) {
      // Source: vvaharness/pipeline/stages/s5/__init__.py:105-106
      In source order: Evaluate once enrich(row, cache, anchors, seeds); assign in source target order to f. Then Evaluate once reject(f, valid_files, cache.lines(f.file)); assign in source target order to verdict.
      // Source: vvaharness/pipeline/stages/s5/__init__.py:107-110
      if (the source predicate verdict is None is truthy) {
        // Source: vvaharness/pipeline/stages/s5/__init__.py:108-109
        In source order: Evaluate keep.append(f); retain side effects and discard the expression result. Then Apply source augmented assignment n_det += 1 with source evaluation/in-place semantics.
        // Source: vvaharness/pipeline/stages/s5/__init__.py:110-110
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/pipeline/stages/s5/__init__.py:111-112
      In source order: Evaluate COUNTERS.bump('s5_det_rejected'); retain side effects and discard the expression result. Then Evaluate dropped.append(_dropped(f, *verdict)); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/pipeline/stages/s5/__init__.py:114-118
  In source order: Evaluate once source_template_114_11 if dropped else ' (nothing dropped)'; assign in source target order to tail. Then Evaluate once source_template_115_14 if n_det else ''; assign in source target order to det_sfx. Then Evaluate console.write(source_template_116_18); retain side effects and discard the expression result. Then Evaluate log.info('s5/enrich: complete - input=%d output=%d dropped=%d detector=%d', len(findings), len(keep), len(dropped), n_det); retain side effects and discard the expression result.
  // Source: vvaharness/pipeline/stages/s5/__init__.py:119-119
  End this invocation with (keep, dropped).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.models import ContextPackage, DroppedFinding, Finding` at source line 18: `source_detail/vvaharness/models/__init__.py.sudo.md`.
- `from vvaharness.pipeline.callgraph_consumer import entry_anchor_lines, seed_paths_by_file` at source line 19: `source_detail/vvaharness/pipeline/callgraph_consumer.py.sudo.md`.
- `from vvaharness.pipeline.stages import s7_dedup` at source line 23: `source_detail/vvaharness/pipeline/stages/s7_dedup.py.sudo.md`.
- `from vvaharness.pipeline.stages.s5 import detectors, reanchor` at source line 24: `source_detail/vvaharness/pipeline/stages/s5/__init__.py.sudo.md`.
- `from vvaharness.pipeline.stages.s5 import detectors, reanchor` at source line 24: `source_detail/vvaharness/pipeline/stages/s5/detectors.py.sudo.md`.
- `from vvaharness.pipeline.stages.s5 import detectors, reanchor` at source line 24: `source_detail/vvaharness/pipeline/stages/s5/reanchor.py.sudo.md`.
- `from vvaharness.pipeline.stages.s5.enrich import FileCache, enrich` at source line 25: `source_detail/vvaharness/pipeline/stages/s5/enrich.py.sudo.md`.
- `from vvaharness.pipeline.stages.s5.gates import reject, reject_path` at source line 26: `source_detail/vvaharness/pipeline/stages/s5/gates.py.sudo.md`.
- `from vvaharness.util import console, logs` at source line 27: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import console, logs` at source line 27: `source_detail/vvaharness/util/console.py.sudo.md`.
- `from vvaharness.util import console, logs` at source line 27: `source_detail/vvaharness/util/logs.py.sudo.md`.
- `from vvaharness.util.config import knob` at source line 28: `source_detail/vvaharness/util/config.py.sudo.md`.
- `from vvaharness.util.counters import COUNTERS` at source line 29: `source_detail/vvaharness/util/counters.py.sudo.md`.
