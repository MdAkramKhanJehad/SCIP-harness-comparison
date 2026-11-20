# vvaharness/pipeline/stages/s3_decompose.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/pipeline/stages/s3_decompose.py.evidence.json`. SHA-256: `14653c37b3fd103260f3593effcfe54c74420b7a972031c94a91ccd5fb9500e8`.

```sudo
// Source: vvaharness/pipeline/stages/s3_decompose.py:15-22
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import logs; preserve alias and import-time effects. Then Evaluate once logs.get_logger(__name__); assign in source target order to log.
// Source: vvaharness/pipeline/stages/s3_decompose.py:24-29
In source order: Resolve source import from vvaharness.lang.detect import detect_languages; preserve alias and import-time effects. Then Resolve source import from vvaharness.models import ContextPackage, InvestigationUnit, TaskManifest, UnitSize; preserve alias and import-time effects. Then Resolve source import from vvaharness.models.scan.work import threat_unit_id; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import console; preserve alias and import-time effects. Then Evaluate once 1000; assign in source target order to _LOC_KILO.
// Source: vvaharness/pipeline/stages/s3_decompose.py:30-38
In source order: Evaluate once 0.9; assign in source target order to _P90_FRACTION. Then Evaluate once 2000; assign in source target order to _SMALL_UNIT_LOC_MAX. Then Evaluate once 8000; assign in source target order to _MEDIUM_UNIT_LOC_MAX. Then Evaluate once {'low': 1, 'medium': 2, 'high': 3, 'critical': 4, 'existential': 5}; assign in source target order to _IMPACT_ORDINAL. Then Evaluate once {'very_rare': 1, 'rare': 2, 'possible': 3, 'likely': 4, 'almost_certain': 5}; assign in source target order to _LIKELIHOOD_ORDINAL.
// Source: vvaharness/pipeline/stages/s3_decompose.py:39-41
In source order: Evaluate once _IMPACT_ORDINAL['medium']; assign in source target order to _DEFAULT_IMPACT_ORDINAL. Then Evaluate once _LIKELIHOOD_ORDINAL['possible']; assign in source target order to _DEFAULT_LIKELIHOOD_ORDINAL. Then Evaluate once max(_IMPACT_ORDINAL.values()) * max(_LIKELIHOOD_ORDINAL.values()); assign in source target order to _MAX_RISK_SCORE.
// Source: vvaharness/pipeline/stages/s3_decompose.py:44-71
// Source signature: run(ctx: ContextPackage, cfg) -> TaskManifest
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn run(ctx, cfg) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s3_decompose.py:45-51
  In source order: Evaluate log.info('s3/decompose: starting task decomposition - threats=%d modules=%d', len(ctx.threat_model.threats) if ctx.threat_model else 0, len(ctx.modules)); retain side effects and discard the expression result. Then Evaluate once TaskManifest(units=[]); assign in source target order to manifest. Then Evaluate once _investigation_units(manifest, ctx); assign in source target order to n_threat. Then Evaluate once Path(ctx.repo_root); assign in source target order to repo_root.
  // Source: vvaharness/pipeline/stages/s3_decompose.py:52-53
  for each u in manifest.units {
    // Source: vvaharness/pipeline/stages/s3_decompose.py:53-53
    In source order: Evaluate once detect_languages(u.files, repo_root=repo_root); assign in source target order to u.languages.
  }
  // Source: vvaharness/pipeline/stages/s3_decompose.py:55-58
  In source order: Evaluate once _coverage_report(manifest, ctx); assign in source target order to manifest.unreachable_files. Then Evaluate _report_unit_loc(manifest, repo_root); retain side effects and discard the expression result. Then Evaluate once getattr(cfg, '_scan_progress', None); assign in source target order to tracker.
  // Source: vvaharness/pipeline/stages/s3_decompose.py:59-61
  if (the source predicate tracker is not None is truthy) {
    // Source: vvaharness/pipeline/stages/s3_decompose.py:60-61
    for each unit in manifest.units {
      // Source: vvaharness/pipeline/stages/s3_decompose.py:61-61
      In source order: Evaluate tracker.queued(unit); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/pipeline/stages/s3_decompose.py:63-70
  In source order: Evaluate console.write(source_template_64_8); retain side effects and discard the expression result. Then Evaluate log.info('s3/decompose: decomposition complete - units=%d (threat=%d)', len(manifest.units), n_threat); retain side effects and discard the expression result.
  // Source: vvaharness/pipeline/stages/s3_decompose.py:71-71
  End this invocation with manifest.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s3_decompose.py:74-78
// Source signature: _threat_risk_rank(t) -> int
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _threat_risk_rank(t) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s3_decompose.py:75-77
  In source order: Retain source documentation literal source_literal_75_4; it is not a model call. Then Evaluate once _IMPACT_ORDINAL.get(t.impact, _DEFAULT_IMPACT_ORDINAL) * _LIKELIHOOD_ORDINAL.get(t.likelihood, _DEFAULT_LIKELIHOOD_ORDINAL); assign in source target order to score.
  // Source: vvaharness/pipeline/stages/s3_decompose.py:78-78
  End this invocation with _MAX_RISK_SCORE + 1 - score.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s3_decompose.py:81-87
// Source signature: _file_module_index(ctx: ContextPackage) -> dict[str, str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _file_module_index(ctx) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s3_decompose.py:82-83
  In source order: Retain source documentation literal source_literal_82_4; it is not a model call. Then For file_community, assign {}; source annotation dict[str, str].
  // Source: vvaharness/pipeline/stages/s3_decompose.py:84-86
  for each m in ctx.modules {
    // Source: vvaharness/pipeline/stages/s3_decompose.py:85-86
    for each f in m.files {
      // Source: vvaharness/pipeline/stages/s3_decompose.py:86-86
      In source order: Evaluate file_community.setdefault(f, m.name); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/pipeline/stages/s3_decompose.py:87-87
  End this invocation with file_community.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s3_decompose.py:90-150
// Source signature: _investigation_units(manifest: TaskManifest, ctx: ContextPackage) -> int
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _investigation_units(manifest, ctx) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s3_decompose.py:91-92
  In source order: Retain source documentation literal source_literal_91_4; it is not a model call. Then Evaluate once ctx.threat_model; assign in source target order to tm.
  // Source: vvaharness/pipeline/stages/s3_decompose.py:93-94
  if (the source predicate not tm or not tm.threats is truthy) {
    // Source: vvaharness/pipeline/stages/s3_decompose.py:94-94
    End this invocation with 0.
  }
  // Source: vvaharness/pipeline/stages/s3_decompose.py:96-101
  In source order: Evaluate once set(ctx.all_files); assign in source target order to all_files. Then Evaluate once _file_module_index(ctx); assign in source target order to file_community. Then Evaluate once Path(ctx.repo_root); assign in source target order to repo_root. Then Evaluate once max((u.risk_rank for u in manifest.units), default=0); assign in source target order to base_rank. Then Evaluate once 0; assign in source target order to added.
  // Source: vvaharness/pipeline/stages/s3_decompose.py:102-103
  In source order: Evaluate once 0; assign in source target order to with_surface. Then Evaluate once {u.id for u in manifest.units}; assign in source target order to used_ids.
  // Source: vvaharness/pipeline/stages/s3_decompose.py:104-145
  for each (threat_id, t) in zip(tm.threat_ids(), tm.threats, strict=True) {
    // Source: vvaharness/pipeline/stages/s3_decompose.py:105-105
    In source order: Evaluate once [f for f in dict.fromkeys(t.surface_files) if f in all_files]; assign in source target order to files.
    // Source: vvaharness/pipeline/stages/s3_decompose.py:106-110
    if (the source predicate not files is truthy) {
      // Source: vvaharness/pipeline/stages/s3_decompose.py:107-109
      In source order: Evaluate manifest.threats_without_unit.append(threat_id); retain side effects and discard the expression result. Then Evaluate console.write(source_template_108_26); retain side effects and discard the expression result.
      // Source: vvaharness/pipeline/stages/s3_decompose.py:110-110
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/pipeline/stages/s3_decompose.py:111-113
    In source order: Apply source augmented assignment with_surface += 1 with source evaluation/in-place semantics. Then Evaluate once threat_unit_id(threat_id); assign in source target order to cid.
    // Source: vvaharness/pipeline/stages/s3_decompose.py:114-118
    if (the source predicate cid in used_ids is truthy) {
      // Source: vvaharness/pipeline/stages/s3_decompose.py:115-115
      In source order: Evaluate once 2; assign in source target order to n.
      // Source: vvaharness/pipeline/stages/s3_decompose.py:116-117
      while (the source predicate source_template_116_18 in used_ids is truthy) {
        // Source: vvaharness/pipeline/stages/s3_decompose.py:117-117
        In source order: Apply source augmented assignment n += 1 with source evaluation/in-place semantics.
      }
      // Source: vvaharness/pipeline/stages/s3_decompose.py:118-118
      In source order: Evaluate once source_template_118_18; assign in source target order to cid.
    }
    // Source: vvaharness/pipeline/stages/s3_decompose.py:119-144
    In source order: Evaluate used_ids.add(cid); retain side effects and discard the expression result. Then Evaluate once set(files); assign in source target order to fset. Then Evaluate once [s for s in ctx.unsafe_sinks if s.file in fset]; assign in source target order to sinks. Then Evaluate once sum((_count_loc(repo_root / f) for f in files)); assign in source target order to loc. Then Evaluate manifest.units.append(InvestigationUnit(id=cid, threat=t.threat, surface=t.surface, actor=t.actor, asset=t.asset, impact=t.impact, likelihood=t.likelihood, controls=t.controls, evidence=t.evidence, file_ids=files, sinks=sinks, entry_points=[e for e in ctx.entry_points if e.file in fset], related_cves=[c.id for c in ctx.known_cves if set(c.affected_files) & fset], communities=sorted({file_community.get(f, source_template_140_54) for f in files}), cwes=sorted({c for s in sinks for c in s.cwe}), risk_rank=base_rank + _threat_risk_rank(t), size=_size_for(loc))); retain side effects and discard the expression result.
    // Source: vvaharness/pipeline/stages/s3_decompose.py:145-145
    In source order: Apply source augmented assignment added += 1 with source evaluation/in-place semantics.
  }
  // Source: vvaharness/pipeline/stages/s3_decompose.py:147-149
  In source order: Evaluate console.write(source_template_147_18); retain side effects and discard the expression result.
  // Source: vvaharness/pipeline/stages/s3_decompose.py:150-150
  End this invocation with added.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s3_decompose.py:153-158
// Source signature: _size_for(loc: int) -> UnitSize
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _size_for(loc) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s3_decompose.py:154-155
  if (the source predicate loc < _SMALL_UNIT_LOC_MAX is truthy) {
    // Source: vvaharness/pipeline/stages/s3_decompose.py:155-155
    End this invocation with UnitSize.SMALL.
  }
  // Source: vvaharness/pipeline/stages/s3_decompose.py:156-157
  if (the source predicate loc < _MEDIUM_UNIT_LOC_MAX is truthy) {
    // Source: vvaharness/pipeline/stages/s3_decompose.py:157-157
    End this invocation with UnitSize.MEDIUM.
  }
  // Source: vvaharness/pipeline/stages/s3_decompose.py:158-158
  End this invocation with UnitSize.LARGE.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s3_decompose.py:161-171
// Source signature: _coverage_report(manifest: TaskManifest, ctx: ContextPackage) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _coverage_report(manifest, ctx) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s3_decompose.py:162-163
  In source order: Retain source documentation literal source_literal_162_4; it is not a model call. Then For covered, assign set(); source annotation set[str].
  // Source: vvaharness/pipeline/stages/s3_decompose.py:164-165
  for each u in manifest.units {
    // Source: vvaharness/pipeline/stages/s3_decompose.py:165-165
    In source order: Evaluate covered.update(u.files); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s3_decompose.py:166-166
  In source order: Evaluate once sorted(set(ctx.all_files) - covered); assign in source target order to unreachable.
  // Source: vvaharness/pipeline/stages/s3_decompose.py:167-169
  if (the source predicate unreachable is truthy) {
    // Source: vvaharness/pipeline/stages/s3_decompose.py:168-169
    In source order: Evaluate console.write(source_template_168_22); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s3_decompose.py:171-171
  End this invocation with unreachable.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s3_decompose.py:174-183
// Source signature: _report_unit_loc(manifest: TaskManifest, repo_root: Path) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _report_unit_loc(manifest, repo_root) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s3_decompose.py:175-176
  In source order: Evaluate once sorted((sum((_count_loc(repo_root / f) for f in u.files)) for u in manifest.units)); assign in source target order to locs.
  // Source: vvaharness/pipeline/stages/s3_decompose.py:177-178
  if (the source predicate not locs is truthy) {
    // Source: vvaharness/pipeline/stages/s3_decompose.py:178-178
    End this invocation with None.
  }
  // Source: vvaharness/pipeline/stages/s3_decompose.py:179-183
  In source order: Evaluate once len(locs); assign in source target order to n. Then Evaluate once lambda x: source_template_180_20 if x >= _LOC_KILO else str(x); assign in source target order to fmt. Then Evaluate once locs[min(n - 1, int(n * _P90_FRACTION))]; assign in source target order to p90. Then Evaluate console.write(source_template_182_18); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s3_decompose.py:186-186
In source order: For _LOC_CACHE, assign {}; source annotation dict[str, int].
// Source: vvaharness/pipeline/stages/s3_decompose.py:189-201
// Source signature: _count_loc(p: Path) -> int
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _count_loc(p) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s3_decompose.py:190-192
  In source order: Retain source documentation literal source_literal_190_4; it is not a model call. Then Evaluate once str(p); assign in source target order to k. Then Evaluate once _LOC_CACHE.get(k); assign in source target order to v.
  // Source: vvaharness/pipeline/stages/s3_decompose.py:193-194
  if (the source predicate v is not None is truthy) {
    // Source: vvaharness/pipeline/stages/s3_decompose.py:194-194
    End this invocation with v.
  }
  // Source: vvaharness/pipeline/stages/s3_decompose.py:195-199
  Perform the following protected operations {
    // Source: vvaharness/pipeline/stages/s3_decompose.py:196-197
    Enter source context managers left-to-right: p.open('r', encoding='utf-8', errors='replace') bound to fh {
      // Source: vvaharness/pipeline/stages/s3_decompose.py:197-197
      In source order: Evaluate once sum((1 for _ in fh)); assign in source target order to v.
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
  }
  // Source: vvaharness/pipeline/stages/s3_decompose.py:198-199
  On the first matching source exception OSError, in handler order {
    // Source: vvaharness/pipeline/stages/s3_decompose.py:199-199
    In source order: Evaluate once 0; assign in source target order to v.
  }
  // Source: vvaharness/pipeline/stages/s3_decompose.py:200-200
  In source order: Evaluate once v; assign in source target order to _LOC_CACHE[k].
  // Source: vvaharness/pipeline/stages/s3_decompose.py:201-201
  End this invocation with v.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.util import logs` at source line 20: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import logs` at source line 20: `source_detail/vvaharness/util/logs.py.sudo.md`.
- `from vvaharness.lang.detect import detect_languages` at source line 24: `source_detail/vvaharness/lang/detect.py.sudo.md`.
- `from vvaharness.models import ContextPackage, InvestigationUnit, TaskManifest, UnitSize` at source line 25: `source_detail/vvaharness/models/__init__.py.sudo.md`.
- `from vvaharness.models.scan.work import threat_unit_id` at source line 26: `source_detail/vvaharness/models/scan/work.py.sudo.md`.
- `from vvaharness.util import console` at source line 27: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import console` at source line 27: `source_detail/vvaharness/util/console.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../prompt_representation/vvaharness/pipeline/stages/s3_decompose.py.sudo.md). Exact strings in the evidence asset support this conversion.
