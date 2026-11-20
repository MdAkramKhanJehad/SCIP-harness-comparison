# vvaharness/evidence/gather.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/evidence/gather.py.evidence.json`. SHA-256: `6127e019810a981b8f9790a25a02b2ad950b54f6e33d1b1af736430f2c6fe90e`.

```sudo
// Source: vvaharness/evidence/gather.py:15-20
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from collections import Counter; preserve alias and import-time effects. Then Resolve source import from dataclasses import dataclass; preserve alias and import-time effects. Then Resolve source import from pathlib import Path, PurePosixPath; preserve alias and import-time effects.
// Source: vvaharness/evidence/gather.py:22-27
In source order: Resolve source import from pydantic import BaseModel, ConfigDict; preserve alias and import-time effects. Then Resolve source import from vvaharness.evidence.api_artefacts import gather_api_artefacts; preserve alias and import-time effects. Then Resolve source import from vvaharness.evidence.configs import gather_config_reps; preserve alias and import-time effects. Then Resolve source import from vvaharness.evidence.docs import gather_docs; preserve alias and import-time effects. Then Resolve source import from vvaharness.evidence.manifests import gather_manifests; preserve alias and import-time effects.
// Source: vvaharness/evidence/gather.py:28-32
In source order: Resolve source import from vvaharness.lang.detect import EXT_TO_LANG, LANG_DISPLAY; preserve alias and import-time effects. Then Resolve source import from vvaharness.models import ContextPackage; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import logs; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.counters import COUNTERS; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.events import Event; preserve alias and import-time effects.
// Source: vvaharness/evidence/gather.py:34-36
In source order: Evaluate once logs.get_logger(__name__); assign in source target order to log. Then Evaluate once {ext: LANG_DISPLAY.get(key, key) for ext, key in EXT_TO_LANG.items()}; assign in source target order to _LANG_BY_EXT.
// Source: vvaharness/evidence/gather.py:39-48
// Source signature: _cap_int(s2: object, key: str, default: int) -> int
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _cap_int(s2, key, default) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/evidence/gather.py:40-41
  In source order: Retain source documentation literal source_literal_40_4; it is not a model call. Then Evaluate once getattr(s2, key, None); assign in source target order to v.
  // Source: vvaharness/evidence/gather.py:42-43
  if (the source predicate v is None is truthy) {
    // Source: vvaharness/evidence/gather.py:43-43
    End this invocation with default.
  }
  // Source: vvaharness/evidence/gather.py:44-47
  Perform the following protected operations {
    // Source: vvaharness/evidence/gather.py:45-45
    In source order: Evaluate once int(v); assign in source target order to n.
  }
  // Source: vvaharness/evidence/gather.py:46-47
  On the first matching source exception (TypeError, ValueError, OverflowError), in handler order {
    // Source: vvaharness/evidence/gather.py:47-47
    End this invocation with default.
  }
  // Source: vvaharness/evidence/gather.py:48-48
  End this invocation with n if n >= 0 else default.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/evidence/gather.py:52-72
// Source: vvaharness/evidence/gather.py:51-51
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vvaharness/evidence/gather.py:52-72
interface _Caps {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/evidence/gather.py:53-58
  In source order: Retain source documentation literal source_literal_53_4; it is not a model call. Then For doc_cap, declare without assigning a value; source annotation int. Then For manifest_cap, declare without assigning a value; source annotation int. Then For manifest_total_cap, declare without assigning a value; source annotation int. Then For max_manifest_depth, declare without assigning a value; source annotation int.
  // Source: vvaharness/evidence/gather.py:59-63
  In source order: For max_manifests, declare without assigning a value; source annotation int. Then For max_manifests_per_kind, declare without assigning a value; source annotation int. Then For max_graph_files, declare without assigning a value; source annotation int. Then For max_entry_points, declare without assigning a value; source annotation int. Then For max_graph_sinks, declare without assigning a value; source annotation int.
  // Source: vvaharness/evidence/gather.py:64-68
  In source order: For max_modules, declare without assigning a value; source annotation int. Then For max_graph_edges, declare without assigning a value; source annotation int. Then For max_config_reps, declare without assigning a value; source annotation int. Then For max_config_rep_chars, declare without assigning a value; source annotation int. Then For max_config_rep_bodies, declare without assigning a value; source annotation int.
  // Source: vvaharness/evidence/gather.py:69-72
  In source order: For max_api_artefacts, declare without assigning a value; source annotation int. Then For max_modules_prompt, declare without assigning a value; source annotation int. Then For max_entry_points_prompt, declare without assigning a value; source annotation int. Then For max_inventory_files, declare without assigning a value; source annotation int.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vvaharness/evidence/gather.py:75-96
// Source signature: _resolve_caps(s2: object) -> _Caps
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _resolve_caps(s2) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/evidence/gather.py:76-96
  End this invocation with _Caps(doc_cap=_cap_int(s2, 'max_doc_chars', 20000), manifest_cap=_cap_int(s2, 'max_manifest_chars', 4000), manifest_total_cap=_cap_int(s2, 'max_manifest_total_chars', 24000), max_manifest_depth=_cap_int(s2, 'max_manifest_depth', 3), max_manifests=_cap_int(s2, 'max_manifests', 12), max_manifests_per_kind=max(1, _cap_int(s2, 'max_manifests_per_kind', 2)), max_graph_files=_cap_int(s2, 'max_graph_files', 220), max_entry_points=_cap_int(s2, 'max_entry_points', 400), max_graph_sinks=_cap_int(s2, 'max_graph_sinks', 80), max_modules=_cap_int(s2, 'max_modules', 100), max_graph_edges=_cap_int(s2, 'max_graph_edges', 100), max_config_reps=_cap_int(s2, 'max_config_reps', 80), max_config_rep_chars=_cap_int(s2, 'max_config_rep_chars', 2000), max_config_rep_bodies=_cap_int(s2, 'max_config_rep_bodies', 12), max_api_artefacts=_cap_int(s2, 'max_api_artefacts', 100), max_modules_prompt=_cap_int(s2, 'max_prompt_modules', 100), max_entry_points_prompt=_cap_int(s2, 'max_prompt_entry_points', 400), max_inventory_files=_cap_int(s2, 'max_inventory_files', 1200)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/evidence/gather.py:99-119
interface ThreatEvidence {
  Describe the source Python type, preserving its base/metaclass expression order: BaseModel.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/evidence/gather.py:100-106
  In source order: Retain source documentation literal source_literal_100_4; it is not a model call. Then Evaluate once ConfigDict(frozen=True, extra='forbid'); assign in source target order to model_config. Then For file_count, declare without assigning a value; source annotation int. Then For original_file_count, declare without assigning a value; source annotation int. Then For primary_language, declare without assigning a value; source annotation str.
  // Source: vvaharness/evidence/gather.py:107-111
  In source order: For languages, assign (); source annotation tuple[tuple[str, int], ...]. Then For top_dirs, assign (); source annotation tuple[str, ...]. Then For modules, assign (); source annotation tuple[tuple[str, str, int], ...]. Then For modules_truncated, assign False; source annotation bool. Then For entry_points, assign (); source annotation tuple[tuple[str, bool, str, str], ...].
  // Source: vvaharness/evidence/gather.py:112-116
  In source order: For entry_points_truncated, assign False; source annotation bool. Then For config_reps, assign (); source annotation tuple[tuple[str, str], ...]. Then For api_artefacts, assign (); source annotation tuple[str, ...]. Then For docs, assign (); source annotation tuple[tuple[str, str], ...]. Then For manifests, assign (); source annotation tuple[tuple[str, str], ...].
  // Source: vvaharness/evidence/gather.py:117-119
  In source order: For inventory, assign (); source annotation tuple[str, ...]. Then For inventory_truncated, assign False; source annotation bool. Then For s1_notes, assign ''; source annotation str.
}
// Source: vvaharness/evidence/gather.py:122-134
// Source signature: _build_frontier(ctx: ContextPackage | None, caps: _Caps) -> ContextPackage | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _build_frontier(ctx, caps) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/evidence/gather.py:123-123
  In source order: Retain source documentation literal source_literal_123_4; it is not a model call.
  // Source: vvaharness/evidence/gather.py:124-125
  if (the source predicate not ctx is truthy) {
    // Source: vvaharness/evidence/gather.py:125-125
    End this invocation with None.
  }
  // Source: vvaharness/evidence/gather.py:126-133
  In source order: Evaluate once ctx.ast_context_view(max_files=caps.max_graph_files, max_entry_points=caps.max_entry_points, max_sinks=caps.max_graph_sinks, max_modules=caps.max_modules, max_edges=caps.max_graph_edges); assign in source target order to frontier. Then Evaluate _note_frontier_cuts(ctx, frontier, caps); retain side effects and discard the expression result.
  // Source: vvaharness/evidence/gather.py:134-134
  End this invocation with frontier.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/evidence/gather.py:137-143
// Source signature: _note_cut(counter: str, kind: str, total: int, kept: int, cap_keys: list[str]) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _note_cut(counter, kind, total, kept, cap_keys) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/evidence/gather.py:138-138
  In source order: Retain source documentation literal source_literal_138_4; it is not a model call.
  // Source: vvaharness/evidence/gather.py:139-140
  if (the source predicate kept >= total is truthy) {
    // Source: vvaharness/evidence/gather.py:140-140
    End this invocation with None.
  }
  // Source: vvaharness/evidence/gather.py:141-143
  In source order: Evaluate COUNTERS.bump(counter, total - kept); retain side effects and discard the expression result. Then Evaluate log.warning(Event.S2_CAP_TRUNCATED, kind=kind, kept=kept, total=total, excluded=total - kept, cap=','.join((source_template_143_52 for k in cap_keys))); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/evidence/gather.py:146-166
// Source signature: _note_frontier_cuts(ctx: ContextPackage, frontier: ContextPackage, caps: _Caps) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _note_frontier_cuts(ctx, frontier, caps) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/evidence/gather.py:147-152
  In source order: Retain source documentation literal source_literal_147_4; it is not a model call. Then Evaluate once set(frontier.all_files); assign in source target order to allowed. Then Evaluate _note_cut('s2_frontier_files_excluded', 'files', len(ctx.all_files), len(frontier.all_files), ['max_graph_files']); retain side effects and discard the expression result.
  // Source: vvaharness/evidence/gather.py:153-162
  for each (kind, files, kept, key, limit) in (('entry_points', [e.file for e in ctx.entry_points], len(frontier.entry_points), 'max_entry_points', caps.max_entry_points), ('sinks', [s.file for s in ctx.unsafe_sinks], len(frontier.unsafe_sinks), 'max_graph_sinks', caps.max_graph_sinks)) {
    // Source: vvaharness/evidence/gather.py:159-162
    In source order: Evaluate once sum((f in allowed for f in files)); assign in source target order to inside. Then Evaluate _note_cut(source_template_160_18, kind, len(files), kept, [k for k, hit in (('max_graph_files', inside < len(files)), (key, inside > limit)) if hit]); retain side effects and discard the expression result.
  }
  // Source: vvaharness/evidence/gather.py:163-166
  In source order: Evaluate once sum((any((p in allowed for p in m.files)) for m in ctx.modules)); assign in source target order to inside. Then Evaluate _note_cut('s2_frontier_modules_excluded', 'modules', len(ctx.modules), len(frontier.modules), [k for k, hit in (('max_graph_files', inside < len(ctx.modules)), ('max_modules', inside > caps.max_modules)) if hit]); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/evidence/gather.py:169-175
// Source signature: _language_counts(full_files: list[str]) -> Counter[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _language_counts(full_files) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/evidence/gather.py:170-170
  In source order: For counts, assign Counter(); source annotation Counter[str].
  // Source: vvaharness/evidence/gather.py:171-174
  for each rel in full_files {
    // Source: vvaharness/evidence/gather.py:172-172
    In source order: Evaluate once _LANG_BY_EXT.get(PurePosixPath(rel).suffix.lower()); assign in source target order to lang.
    // Source: vvaharness/evidence/gather.py:173-174
    if (the source predicate lang is truthy) {
      // Source: vvaharness/evidence/gather.py:174-174
      In source order: Apply source augmented assignment counts[lang] += 1 with source evaluation/in-place semantics.
    }
  }
  // Source: vvaharness/evidence/gather.py:175-175
  End this invocation with counts.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/evidence/gather.py:178-182
// Source signature: _sorted_entry_points(active_ctx: ContextPackage | None) -> list[tuple[str, bool, str, str]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _sorted_entry_points(active_ctx) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/evidence/gather.py:179-181
  In source order: Evaluate once [(e.kind, e.reachable_from_unauth, e.file, e.function) for e in (active_ctx.entry_points if active_ctx else [])]; assign in source target order to eps. Then Evaluate eps.sort(key=lambda t: (t[0] != 'network', not t[1], t[0], t[2])); retain side effects and discard the expression result.
  // Source: vvaharness/evidence/gather.py:182-182
  End this invocation with eps.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/evidence/gather.py:185-235
// Source signature: gather(repo_root: str, cfg: object, ctx: ContextPackage | None) -> ThreatEvidence
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn gather(repo_root, cfg, ctx) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/evidence/gather.py:186-191
  In source order: Retain source documentation literal source_literal_186_4; it is not a model call. Then Evaluate once Path(repo_root); assign in source target order to root. Then Evaluate once _resolve_caps(getattr(cfg, 'step2', None)); assign in source target order to caps. Then Evaluate once _build_frontier(ctx, caps); assign in source target order to frontier. Then Evaluate once frontier or ctx; assign in source target order to active_ctx.
  // Source: vvaharness/evidence/gather.py:192-198
  In source order: Evaluate once list(active_ctx.all_files) if active_ctx else []; assign in source target order to frontier_files. Then Evaluate once list(ctx.all_files) if ctx else frontier_files; assign in source target order to full_files. Then Evaluate once [(m.name, m.purpose, m.loc) for m in (active_ctx.modules if active_ctx else [])]; assign in source target order to modules. Then Evaluate once _sorted_entry_points(active_ctx); assign in source target order to eps. Then Evaluate once gather_docs(root, full_files, caps.doc_cap); assign in source target order to docs.
  // Source: vvaharness/evidence/gather.py:199-205
  In source order: Evaluate once gather_manifests(root, (caps.max_manifest_depth, caps.max_manifests, caps.max_manifests_per_kind), caps.manifest_cap, caps.manifest_total_cap); assign in source target order to manifests. Then Evaluate once gather_config_reps(root, full_files, caps.max_config_reps, caps.max_config_rep_chars, caps.max_config_rep_bodies); assign in source target order to cfg_reps. Then Evaluate once gather_api_artefacts(full_files, caps.max_api_artefacts); assign in source target order to api_artefacts. Then Evaluate once sorted({rel.split('/', 1)[0] for rel in full_files if '/' in rel}); assign in source target order to top_dirs.
  // Source: vvaharness/evidence/gather.py:208-216
  for each (counter, kind, total, limit, key) in (('s2_prompt_modules_truncated', 'prompt_modules', len(modules), caps.max_modules_prompt, 'max_prompt_modules'), ('s2_prompt_entry_points_truncated', 'prompt_entry_points', len(eps), caps.max_entry_points_prompt, 'max_prompt_entry_points'), ('s2_inventory_files_truncated', 'inventory_files', len(full_files), caps.max_inventory_files, 'max_inventory_files')) {
    // Source: vvaharness/evidence/gather.py:216-216
    In source order: Evaluate _note_cut(counter, kind, total, min(total, limit), [key]); retain side effects and discard the expression result.
  }
  // Source: vvaharness/evidence/gather.py:218-235
  End this invocation with ThreatEvidence(file_count=len(frontier_files), original_file_count=len(ctx.all_files) if ctx else len(frontier_files), primary_language=ctx.language if ctx else '', languages=tuple(_language_counts(full_files).most_common()), top_dirs=tuple(top_dirs), modules=tuple(modules[:caps.max_modules_prompt]), modules_truncated=len(modules) > caps.max_modules_prompt, entry_points=tuple(eps[:caps.max_entry_points_prompt]), entry_points_truncated=len(eps) > caps.max_entry_points_prompt, config_reps=tuple(cfg_reps), api_artefacts=tuple(api_artefacts), docs=tuple(docs), manifests=tuple(manifests), inventory=tuple(sorted(full_files)[:caps.max_inventory_files]), inventory_truncated=len(full_files) > caps.max_inventory_files, s1_notes=getattr(ctx, 'notes', '') if ctx else '').
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.evidence.api_artefacts import gather_api_artefacts` at source line 24: `source_detail/vvaharness/evidence/api_artefacts.py.sudo.md`.
- `from vvaharness.evidence.configs import gather_config_reps` at source line 25: `source_detail/vvaharness/evidence/configs.py.sudo.md`.
- `from vvaharness.evidence.docs import gather_docs` at source line 26: `source_detail/vvaharness/evidence/docs.py.sudo.md`.
- `from vvaharness.evidence.manifests import gather_manifests` at source line 27: `source_detail/vvaharness/evidence/manifests.py.sudo.md`.
- `from vvaharness.lang.detect import EXT_TO_LANG, LANG_DISPLAY` at source line 28: `source_detail/vvaharness/lang/detect.py.sudo.md`.
- `from vvaharness.models import ContextPackage` at source line 29: `source_detail/vvaharness/models/__init__.py.sudo.md`.
- `from vvaharness.util import logs` at source line 30: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import logs` at source line 30: `source_detail/vvaharness/util/logs.py.sudo.md`.
- `from vvaharness.util.counters import COUNTERS` at source line 31: `source_detail/vvaharness/util/counters.py.sudo.md`.
- `from vvaharness.util.events import Event` at source line 32: `source_detail/vvaharness/util/events.py.sudo.md`.
