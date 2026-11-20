# vvaharness/pipeline/stages/s5/detectors.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/pipeline/stages/s5/detectors.py.evidence.json`. SHA-256: `b1298c585596815989172a2e370d4501adf094ec729ddfc1db12ffa70f97e370`.

```sudo
// Source: vvaharness/pipeline/stages/s5/detectors.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from pathlib import PurePosixPath; preserve alias and import-time effects. Then Resolve source import from vvaharness.detect.matcher import Hit, compile_detectors, detector_hits; preserve alias and import-time effects. Then Resolve source import from vvaharness.detect.patterns import detector_corpus; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s5/detectors.py:22-26
In source order: Resolve source import from vvaharness.lang.detect import EXT_TO_LANG; preserve alias and import-time effects. Then Resolve source import from vvaharness.models import ContextPackage, Finding, VulnClass; preserve alias and import-time effects. Then Resolve source import from vvaharness.pipeline.stages.s5.enrich import FileCache; preserve alias and import-time effects. Then Resolve source import from vvaharness.pipeline.stages.s5.rules import EXCLUDE_PATH_RE; preserve alias and import-time effects. Then Resolve source import from vvaharness.rules.cwe import weakness_key; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s5/detectors.py:27-32
In source order: Resolve source import from vvaharness.util.counters import COUNTERS; preserve alias and import-time effects. Then For _DETECTOR_LANGS, assign frozenset({'python', 'javascript', 'typescript', 'web-template'}); source annotation frozenset[str].
// Source: vvaharness/pipeline/stages/s5/detectors.py:35-36
// Source signature: _file_lang(rel: str) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _file_lang(rel) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s5/detectors.py:36-36
  End this invocation with EXT_TO_LANG.get(PurePosixPath(rel).suffix.lower()).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s5/detectors.py:39-44
// Source signature: _in_scope(rel: str, lang: str | None) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _in_scope(rel, lang) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s5/detectors.py:40-40
  In source order: Retain source documentation literal source_literal_40_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s5/detectors.py:41-42
  if (the source predicate lang not in _DETECTOR_LANGS is truthy) {
    // Source: vvaharness/pipeline/stages/s5/detectors.py:42-42
    End this invocation with False.
  }
  // Source: vvaharness/pipeline/stages/s5/detectors.py:43-43
  In source order: Evaluate once PurePosixPath(rel).name.lower(); assign in source target order to name.
  // Source: vvaharness/pipeline/stages/s5/detectors.py:44-44
  End this invocation with not (EXCLUDE_PATH_RE.search(rel) or '.min.' in name).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s5/detectors.py:47-64
// Source signature: _mint(hit: Hit) -> Finding
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _mint(hit) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s5/detectors.py:48-50
  In source order: Retain source documentation literal source_literal_48_4; it is not a model call. Then Evaluate once hit.spec; assign in source target order to spec. Then Evaluate once spec.cwe == 'CWE-79'; assign in source target order to xss.
  // Source: vvaharness/pipeline/stages/s5/detectors.py:51-64
  End this invocation with Finding(title=spec.title or spec.rule_id, file=hit.file, line_start=hit.line, line_end=hit.line_end, vuln_class=VulnClass.INJECTION if xss else VulnClass.OTHER, vuln_class_label='' if xss else spec.kind, cwe=spec.cwe, origin='detector', chunk_id=spec.rule_id, description=source_template_61_21).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s5/detectors.py:68-71
In source order: Evaluate once {'detector-httpresponse-concat': 'html-concat', 'detector-html-string-concat': 'html-concat'}; assign in source target order to _SPAN_FAMILY.
// Source: vvaharness/pipeline/stages/s5/detectors.py:74-103
// Source signature: _dedup(rows: list[Finding], kept: list[Finding], tol: int) -> list[Finding]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _dedup(rows, kept, tol) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s5/detectors.py:75-76
  In source order: Retain source documentation literal source_literal_75_4; it is not a model call. Then For kept_lines, assign {}; source annotation dict[tuple[str, str], list[int]].
  // Source: vvaharness/pipeline/stages/s5/detectors.py:77-80
  for each f in kept {
    // Source: vvaharness/pipeline/stages/s5/detectors.py:78-78
    In source order: Evaluate once weakness_key(f.cwe); assign in source target order to key.
    // Source: vvaharness/pipeline/stages/s5/detectors.py:79-80
    if (the source predicate key is truthy) {
      // Source: vvaharness/pipeline/stages/s5/detectors.py:80-80
      In source order: Evaluate kept_lines.setdefault((f.file, key), []).append(int(f.line_start)); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/pipeline/stages/s5/detectors.py:81-85
  In source order: For out, assign []; source annotation list[Finding]. Then For by_rule, assign {}; source annotation dict[tuple[str, str, str], list[int]]. Then For by_span, assign {}; source annotation dict[tuple[str, str, str], list[tuple[int, int]]].
  // Source: vvaharness/pipeline/stages/s5/detectors.py:86-102
  for each row in rows {
    // Source: vvaharness/pipeline/stages/s5/detectors.py:87-93
    In source order: Evaluate once int(row.line_start); assign in source target order to line. Then Evaluate once max(line, int(row.line_end or line)); assign in source target order to end. Then Evaluate once (row.file, row.cwe or '', row.chunk_id); assign in source target order to rule_key. Then Evaluate once (row.file, row.cwe or '', _SPAN_FAMILY.get(row.chunk_id, row.chunk_id)); assign in source target order to span_key. Then Evaluate once (row.file, weakness_key(row.cwe) or ''); assign in source target order to site_key.
    // Source: vvaharness/pipeline/stages/s5/detectors.py:94-99
    if (the source predicate any((abs(line - n) <= tol for n in by_rule.get(rule_key, []))) or any((s <= end and line <= e for s, e in by_span.get(span_key, []))) or any((abs(line - n) <= tol or line <= n <= end for n in kept_lines.get(site_key, []))) is truthy) {
      // Source: vvaharness/pipeline/stages/s5/detectors.py:98-98
      In source order: Evaluate COUNTERS.bump('s5_det_dup_suppressed'); retain side effects and discard the expression result.
      // Source: vvaharness/pipeline/stages/s5/detectors.py:99-99
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/pipeline/stages/s5/detectors.py:100-102
    In source order: Evaluate by_rule.setdefault(rule_key, []).append(line); retain side effects and discard the expression result. Then Evaluate by_span.setdefault(span_key, []).append((line, end)); retain side effects and discard the expression result. Then Evaluate out.append(row); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s5/detectors.py:103-103
  End this invocation with out.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s5/detectors.py:106-116
// Source signature: _cap(survivors: list[Finding], compiled, max_rows: int) -> list[Finding]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _cap(survivors, compiled, max_rows) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s5/detectors.py:107-107
  In source order: Retain source documentation literal source_literal_107_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s5/detectors.py:108-109
  if (the source predicate max_rows <= 0 or len(survivors) <= max_rows is truthy) {
    // Source: vvaharness/pipeline/stages/s5/detectors.py:109-109
    End this invocation with survivors.
  }
  // Source: vvaharness/pipeline/stages/s5/detectors.py:110-115
  In source order: Evaluate once {d.spec.rule_id: i for i, d in enumerate(compiled)}; assign in source target order to priority. Then Evaluate once sorted(range(len(survivors)), key=lambda i: (priority.get(survivors[i].chunk_id, len(priority)), i)); assign in source target order to ranked. Then Evaluate once frozenset(ranked[:max_rows]); assign in source target order to keep_idx. Then Evaluate COUNTERS.bump('s5_det_overflow_suppressed', len(survivors) - max_rows); retain side effects and discard the expression result.
  // Source: vvaharness/pipeline/stages/s5/detectors.py:116-116
  End this invocation with [row for i, row in enumerate(survivors) if i in keep_idx].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s5/detectors.py:119-145
// Source signature: run(kept: list[Finding], ctx: ContextPackage, cache: FileCache, line_tol: int, max_rows: int=200) -> list[Finding]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn run(kept, ctx, cache, line_tol, max_rows) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s5/detectors.py:121-122
  In source order: Retain source documentation literal source_literal_121_4; it is not a model call. Then Evaluate once compile_detectors(detector_corpus()); assign in source target order to compiled.
  // Source: vvaharness/pipeline/stages/s5/detectors.py:123-124
  if (the source predicate not compiled is truthy) {
    // Source: vvaharness/pipeline/stages/s5/detectors.py:124-124
    End this invocation with [].
  }
  // Source: vvaharness/pipeline/stages/s5/detectors.py:125-127
  In source order: Evaluate once {lang: [d for d in compiled if lang in d.spec.languages] for lang in _DETECTOR_LANGS}; assign in source target order to by_lang. Then For rows, assign []; source annotation list[Finding].
  // Source: vvaharness/pipeline/stages/s5/detectors.py:128-139
  for each rel in sorted(set(ctx.all_files)) {
    // Source: vvaharness/pipeline/stages/s5/detectors.py:129-129
    In source order: Evaluate once _file_lang(rel); assign in source target order to lang.
    // Source: vvaharness/pipeline/stages/s5/detectors.py:130-131
    if (the source predicate not _in_scope(rel, lang) is truthy) {
      // Source: vvaharness/pipeline/stages/s5/detectors.py:131-131
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/pipeline/stages/s5/detectors.py:132-132
    In source order: Evaluate once by_lang.get(lang or ''); assign in source target order to live.
    // Source: vvaharness/pipeline/stages/s5/detectors.py:133-134
    if (the source predicate not live is truthy) {
      // Source: vvaharness/pipeline/stages/s5/detectors.py:134-134
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/pipeline/stages/s5/detectors.py:135-135
    In source order: Evaluate once cache.lines(rel); assign in source target order to lines.
    // Source: vvaharness/pipeline/stages/s5/detectors.py:136-137
    if (the source predicate lines is None is truthy) {
      // Source: vvaharness/pipeline/stages/s5/detectors.py:137-137
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/pipeline/stages/s5/detectors.py:138-139
    for each hit in detector_hits(rel, lines, live) {
      // Source: vvaharness/pipeline/stages/s5/detectors.py:139-139
      In source order: Evaluate rows.append(_mint(hit)); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/pipeline/stages/s5/detectors.py:140-140
  In source order: Evaluate once _cap(_dedup(rows, kept, line_tol), compiled, max_rows); assign in source target order to survivors.
  // Source: vvaharness/pipeline/stages/s5/detectors.py:141-144
  for each row in survivors {
    // Source: vvaharness/pipeline/stages/s5/detectors.py:142-144
    In source order: Evaluate COUNTERS.bump('s5_det_emitted'); retain side effects and discard the expression result. Then Evaluate once row.chunk_id.removeprefix('detector-').replace('-', '_'); assign in source target order to rule. Then Evaluate COUNTERS.bump(source_template_144_22); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s5/detectors.py:145-145
  End this invocation with survivors.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.detect.matcher import Hit, compile_detectors, detector_hits` at source line 20: `source_detail/vvaharness/detect/matcher.py.sudo.md`.
- `from vvaharness.detect.patterns import detector_corpus` at source line 21: `source_detail/vvaharness/detect/patterns.py.sudo.md`.
- `from vvaharness.lang.detect import EXT_TO_LANG` at source line 22: `source_detail/vvaharness/lang/detect.py.sudo.md`.
- `from vvaharness.models import ContextPackage, Finding, VulnClass` at source line 23: `source_detail/vvaharness/models/__init__.py.sudo.md`.
- `from vvaharness.pipeline.stages.s5.enrich import FileCache` at source line 24: `source_detail/vvaharness/pipeline/stages/s5/enrich.py.sudo.md`.
- `from vvaharness.pipeline.stages.s5.rules import EXCLUDE_PATH_RE` at source line 25: `source_detail/vvaharness/pipeline/stages/s5/rules.py.sudo.md`.
- `from vvaharness.rules.cwe import weakness_key` at source line 26: `source_detail/vvaharness/rules/cwe.py.sudo.md`.
- `from vvaharness.util.counters import COUNTERS` at source line 27: `source_detail/vvaharness/util/counters.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../../prompt_representation/vvaharness/pipeline/stages/s5/detectors.py.sudo.md). Exact strings in the evidence asset support this conversion.
