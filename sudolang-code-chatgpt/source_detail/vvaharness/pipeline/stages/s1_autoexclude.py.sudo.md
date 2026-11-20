# vvaharness/pipeline/stages/s1_autoexclude.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/pipeline/stages/s1_autoexclude.py.evidence.json`. SHA-256: `8ddd90e0a4102e39fd495095364c58b40a7121d19bc12a5bbc114b0d1a1b4c7f`.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:15-20
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import logs; preserve alias and import-time effects. Then Resolve source import import os; preserve alias and import-time effects. Then Resolve source import import re; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:21-28
In source order: Resolve source import from collections import Counter; preserve alias and import-time effects. Then Resolve source import from pathlib import Path, PurePosixPath; preserve alias and import-time effects. Then Resolve source import import yaml; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm import deepagents as _deepagents; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm.models import refusal_resend_allowed; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:29-33
In source order: Resolve source import from vvaharness.detect.matcher import compile_detectors, detector_hits; preserve alias and import-time effects. Then Resolve source import from vvaharness.detect.patterns import detector_corpus; preserve alias and import-time effects. Then Resolve source import from vvaharness.lang.detect import EXT_TO_LANG, is_web_template; preserve alias and import-time effects. Then Resolve source import from vvaharness.pipeline.stages.s5.enrich import FileCache; preserve alias and import-time effects. Then Resolve source import from vvaharness.report.redact import redact, redact_counts; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:34-43
In source order: Resolve source import from vvaharness.scope import _DEDUP_DEFAULTS, _exclusion_sets, glob_hit, scope_after; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import console; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import errlog as _errlog; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.config import knob; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.counters import COUNTERS; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:44-104
In source order: Resolve source import from vvaharness.util.response_quality import dispatch_or_retry_unforced, stage_floors; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.events import Event; preserve alias and import-time effects. Then Evaluate once logs.get_logger(__name__); assign in source target order to log. Then Evaluate once source_literal_49_10; assign in source target order to _SYSTEM. Then Evaluate once re.compile(source_literal_99_4, re.IGNORECASE); assign in source target order to _EXCERPT_NAMES.
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:105-109
In source order: Evaluate once 1500; assign in source target order to _EXCERPT_CHARS. Then Evaluate once 12; assign in source target order to _EXCERPT_MAX. Then Evaluate once 2; assign in source target order to _TREE_DEPTH. Then Evaluate once 60; assign in source target order to _TREE_MAX_CHILDREN. Then Evaluate once 40; assign in source target order to _EXT_TOP_N.
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:110-119
In source order: Evaluate once 15; assign in source target order to _LARGEST_N. Then Evaluate once {'enabled': bool, 'exts': list, 'min_cluster_size': int, 'keep_per_top_dir': bool, 'promote_on_secret_hit': bool, 'promote_on_insecure_value': bool, 'max_file_kb': int}; assign in source target order to _DEDUP_KEYS. Then Evaluate once 40; assign in source target order to _MIN_RESPONSE_CHARS. Then Evaluate once 10; assign in source target order to _MIN_RESPONSE_TOKENS. Then Evaluate once 's1 autoexclude'; assign in source target order to _TAG.
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:122-122
In source order: Evaluate once 0.1; assign in source target order to _AGGRESSIVE_KEEP_RATIO.
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:125-235
// Source signature: _survey(repo_root: Path, base_dirs: set[str], base_exts: set[str], base_globs: list[str]) -> tuple[str, int]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _survey(repo_root, base_dirs, base_exts, base_globs) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:127-127
  In source order: Retain source documentation literal source_literal_127_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:128-130
  // Source signature: globbed(rel: str) -> bool
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn globbed(rel) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/pipeline/stages/s1_autoexclude.py:130-130
    End this invocation with glob_hit(rel, base_globs) is not None.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:133-137
  In source order: For tree, assign {'': [set(), 0, 0]}; source annotation dict[str, list]. Then For ext_hist, assign Counter(); source annotation Counter[str]. Then For excerpts, assign []; source annotation list[tuple[str, str]]. Then For largest, assign []; source annotation list[tuple[int, str]]. Then Evaluate once 0; assign in source target order to n_files.
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:138-138
  In source order: Evaluate once Path(repo_root).resolve(); assign in source target order to root_resolved.
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:140-194
  for each (dirpath, dirnames, filenames) in os.walk(repo_root) {
    // Source: vvaharness/pipeline/stages/s1_autoexclude.py:141-148
    In source order: Evaluate once str(PurePosixPath(Path(dirpath).relative_to(repo_root))); assign in source target order to rel_dir. Then Evaluate once '' if rel_dir == '.' else rel_dir; assign in source target order to rel_dir. Then Evaluate once 0 if not rel_dir else rel_dir.count('/') + 1; assign in source target order to depth. Then Evaluate once sorted((d for d in dirnames if d.lower() not in base_dirs and (not globbed(source_template_147_28 if rel_dir else d)))); assign in source target order to dirnames[:].
    // Source: vvaharness/pipeline/stages/s1_autoexclude.py:149-151
    if (the source predicate depth <= _TREE_DEPTH is truthy) {
      // Source: vvaharness/pipeline/stages/s1_autoexclude.py:150-151
      In source order: Evaluate once tree.setdefault(rel_dir, [set(), 0, depth]); assign in source target order to node. Then Evaluate node[0].update(dirnames); retain side effects and discard the expression result.
    }
    // Source: vvaharness/pipeline/stages/s1_autoexclude.py:152-194
    for each fn in filenames {
      // Source: vvaharness/pipeline/stages/s1_autoexclude.py:153-156
      In source order: Evaluate once source_template_153_18 if rel_dir else fn; assign in source target order to rel. Then Evaluate once fn.lower(); assign in source target order to name. Then Evaluate once Path(fn).suffix.lower(); assign in source target order to suffix.
      // Source: vvaharness/pipeline/stages/s1_autoexclude.py:157-158
      if (the source predicate any((suffix == e or name.endswith(e) for e in base_exts)) or globbed(rel) is truthy) {
        // Source: vvaharness/pipeline/stages/s1_autoexclude.py:158-158
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/pipeline/stages/s1_autoexclude.py:159-161
      In source order: Evaluate once suffix or '(none)'; assign in source target order to ext. Then Apply source augmented assignment n_files += 1 with source evaluation/in-place semantics. Then Apply source augmented assignment ext_hist[ext] += 1 with source evaluation/in-place semantics.
      // Source: vvaharness/pipeline/stages/s1_autoexclude.py:162-165
      Perform the following protected operations {
        // Source: vvaharness/pipeline/stages/s1_autoexclude.py:163-163
        In source order: Evaluate once (Path(dirpath) / fn).stat().st_size; assign in source target order to sz.
      }
      // Source: vvaharness/pipeline/stages/s1_autoexclude.py:164-165
      On the first matching source exception OSError, in handler order {
        // Source: vvaharness/pipeline/stages/s1_autoexclude.py:165-165
        In source order: Evaluate once 0; assign in source target order to sz.
      }
      // Source: vvaharness/pipeline/stages/s1_autoexclude.py:166-169
      if (the source predicate len(largest) < _LARGEST_N or sz > largest[-1][0] is truthy) {
        // Source: vvaharness/pipeline/stages/s1_autoexclude.py:167-169
        In source order: Evaluate largest.append((sz, rel)); retain side effects and discard the expression result. Then Evaluate largest.sort(reverse=True); retain side effects and discard the expression result. Then Delete source targets in order: largest[_LARGEST_N:].
      }
      // Source: vvaharness/pipeline/stages/s1_autoexclude.py:170-170
      In source order: Evaluate once rel_dir; assign in source target order to anc.
      // Source: vvaharness/pipeline/stages/s1_autoexclude.py:171-176
      while (the source predicate True is truthy) {
        // Source: vvaharness/pipeline/stages/s1_autoexclude.py:172-173
        if (the source predicate anc in tree is truthy) {
          // Source: vvaharness/pipeline/stages/s1_autoexclude.py:173-173
          In source order: Apply source augmented assignment tree[anc][1] += 1 with source evaluation/in-place semantics.
        }
        // Source: vvaharness/pipeline/stages/s1_autoexclude.py:174-175
        if (the source predicate not anc is truthy) {
          // Source: vvaharness/pipeline/stages/s1_autoexclude.py:175-175
          Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
        }
        // Source: vvaharness/pipeline/stages/s1_autoexclude.py:176-176
        In source order: Evaluate once anc.rpartition('/')[0]; assign in source target order to anc.
      }
      // Source: vvaharness/pipeline/stages/s1_autoexclude.py:177-194
      if (the source predicate depth <= _TREE_DEPTH and len(excerpts) < _EXCERPT_MAX and (sz <= 5000000) and _EXCERPT_NAMES.match(fn) is truthy) {
        // Source: vvaharness/pipeline/stages/s1_autoexclude.py:180-180
        In source order: Evaluate once Path(dirpath) / fn; assign in source target order to fp.
        // Source: vvaharness/pipeline/stages/s1_autoexclude.py:182-188
        if (the source predicate fp.is_symlink() is truthy) {
          // Source: vvaharness/pipeline/stages/s1_autoexclude.py:183-188
          Perform the following protected operations {
            // Source: vvaharness/pipeline/stages/s1_autoexclude.py:184-186
            if (the source predicate not fp.resolve(strict=False).is_relative_to(root_resolved) is truthy) {
              // Source: vvaharness/pipeline/stages/s1_autoexclude.py:186-186
              Continue the immediately enclosing source loop at its next iteration.
            }
          }
          // Source: vvaharness/pipeline/stages/s1_autoexclude.py:187-188
          On the first matching source exception OSError, in handler order {
            // Source: vvaharness/pipeline/stages/s1_autoexclude.py:188-188
            Continue the immediately enclosing source loop at its next iteration.
          }
        }
        // Source: vvaharness/pipeline/stages/s1_autoexclude.py:189-194
        Perform the following protected operations {
          // Source: vvaharness/pipeline/stages/s1_autoexclude.py:190-192
          In source order: Evaluate once fp.read_text(encoding='utf-8', errors='replace')[:_EXCERPT_CHARS]; assign in source target order to txt. Then Evaluate excerpts.append((rel, txt.rstrip())); retain side effects and discard the expression result.
        }
        // Source: vvaharness/pipeline/stages/s1_autoexclude.py:193-194
        On the first matching source exception OSError, in handler order {
          // Source: vvaharness/pipeline/stages/s1_autoexclude.py:194-194
          In source order: Perform no operation at this source statement.
        }
      }
    }
  }
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:196-209
  // Source signature: render_tree() -> str
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn render_tree() {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/pipeline/stages/s1_autoexclude.py:197-197
    In source order: Evaluate once [source_template_197_17]; assign in source target order to lines.
    // Source: vvaharness/pipeline/stages/s1_autoexclude.py:198-208
    for each (rel, (subs, cnt, depth)) in sorted(tree.items()) {
      // Source: vvaharness/pipeline/stages/s1_autoexclude.py:199-200
      if (the source predicate not rel is truthy) {
        // Source: vvaharness/pipeline/stages/s1_autoexclude.py:200-200
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/pipeline/stages/s1_autoexclude.py:201-202
      In source order: Evaluate once '  ' * depth; assign in source target order to indent. Then Evaluate lines.append(source_template_202_25); retain side effects and discard the expression result.
      // Source: vvaharness/pipeline/stages/s1_autoexclude.py:203-208
      if (the source predicate depth == _TREE_DEPTH and subs is truthy) {
        // Source: vvaharness/pipeline/stages/s1_autoexclude.py:204-206
        In source order: Evaluate once sorted(subs); assign in source target order to kids. Then Evaluate once kids[:_TREE_MAX_CHILDREN]; assign in source target order to shown. Then Evaluate lines.extend((source_template_206_29 for k in shown)); retain side effects and discard the expression result.
        // Source: vvaharness/pipeline/stages/s1_autoexclude.py:207-208
        if (the source predicate len(kids) > _TREE_MAX_CHILDREN is truthy) {
          // Source: vvaharness/pipeline/stages/s1_autoexclude.py:208-208
          In source order: Evaluate lines.append(source_template_208_33); retain side effects and discard the expression result.
        }
      }
    }
    // Source: vvaharness/pipeline/stages/s1_autoexclude.py:209-209
    End this invocation with source_literal_209_15.join(lines).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:211-213
  In source order: Evaluate once source_literal_211_16.join((source_template_212_8 for ext, n in ext_hist.most_common(_EXT_TOP_N))) or '  (none)'; assign in source target order to ext_block.
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:214-215
  if (the source predicate len(ext_hist) > _EXT_TOP_N is truthy) {
    // Source: vvaharness/pipeline/stages/s1_autoexclude.py:215-215
    In source order: Apply source augmented assignment ext_block += source_template_215_21 with source evaluation/in-place semantics.
  }
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:217-234
  In source order: Evaluate once source_literal_217_16.join((source_template_218_8 for rel, txt in excerpts)) or '(no README/build files found at depth ≤2)'; assign in source target order to exc_block. Then Evaluate once source_literal_221_18.join((source_template_222_8 for sz, rel in largest)) or '  (none)'; assign in source target order to large_block. Then Evaluate once source_template_226_8; assign in source target order to survey.
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:235-235
  End this invocation with (survey, n_files).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:239-244
In source order: Evaluate once re.compile('```(?P<lang>[A-Za-z0-9_+.-]*)[^\\S\\n]*\\n(?P<body>.*?)(?:\\n```|\\Z)', re.DOTALL); assign in source target order to _FENCE_RX. Then Evaluate once frozenset({'exclude_dirs', 'exclude_exts', 'exclude_globs', 'max_file_kb', 'config_dedup'}); assign in source target order to _OVERLAY_KEYS.
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:247-254
// Source signature: _yaml_candidates(text: str) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _yaml_candidates(text) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:248-253
  In source order: Retain source documentation literal source_literal_248_4; it is not a model call. Then Evaluate once [(m.group('lang').lower(), m.group('body')) for m in _FENCE_RX.finditer(text)]; assign in source target order to blocks. Then Evaluate once [b for lang, b in blocks if lang in ('yaml', 'yml')]; assign in source target order to labelled. Then Evaluate once [b for lang, b in blocks if not lang]; assign in source target order to unlabelled. Then Evaluate once [b for lang, b in blocks if lang and lang not in ('yaml', 'yml')]; assign in source target order to other.
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:254-254
  End this invocation with [*labelled, *unlabelled, *other, text].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:257-284
// Source signature: _extract_yaml(text: str) -> dict
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _extract_yaml(text) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:258-261
  In source order: Retain source documentation literal source_literal_258_4; it is not a model call. Then For first_dict, assign None; source annotation dict | None. Then Evaluate once False; assign in source target order to parsed_any. Then For err, assign None; source annotation yaml.YAMLError | None.
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:262-278
  for each blob in _yaml_candidates(text) {
    // Source: vvaharness/pipeline/stages/s1_autoexclude.py:263-267
    Perform the following protected operations {
      // Source: vvaharness/pipeline/stages/s1_autoexclude.py:264-264
      In source order: Evaluate once yaml.safe_load(blob) or {}; assign in source target order to data.
    }
    // Source: vvaharness/pipeline/stages/s1_autoexclude.py:265-267
    On the first matching source exception yaml.YAMLError as e, in handler order {
      // Source: vvaharness/pipeline/stages/s1_autoexclude.py:266-266
      In source order: Evaluate once err or e; assign in source target order to err.
      // Source: vvaharness/pipeline/stages/s1_autoexclude.py:267-267
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/pipeline/stages/s1_autoexclude.py:268-268
    In source order: Evaluate once True; assign in source target order to parsed_any.
    // Source: vvaharness/pipeline/stages/s1_autoexclude.py:269-270
    if (the source predicate not isinstance(data, dict) is truthy) {
      // Source: vvaharness/pipeline/stages/s1_autoexclude.py:270-270
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/pipeline/stages/s1_autoexclude.py:271-272
    if (the source predicate set(data) == {'step1'} and isinstance(data['step1'], dict) is truthy) {
      // Source: vvaharness/pipeline/stages/s1_autoexclude.py:272-272
      In source order: Evaluate once data['step1']; assign in source target order to data.
    }
    // Source: vvaharness/pipeline/stages/s1_autoexclude.py:273-274
    if (the source predicate not isinstance(data, dict) is truthy) {
      // Source: vvaharness/pipeline/stages/s1_autoexclude.py:274-274
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/pipeline/stages/s1_autoexclude.py:275-276
    if (the source predicate _OVERLAY_KEYS & set(data) is truthy) {
      // Source: vvaharness/pipeline/stages/s1_autoexclude.py:276-276
      End this invocation with data.
    }
    // Source: vvaharness/pipeline/stages/s1_autoexclude.py:277-278
    if (the source predicate first_dict is None is truthy) {
      // Source: vvaharness/pipeline/stages/s1_autoexclude.py:278-278
      In source order: Evaluate once data; assign in source target order to first_dict.
    }
  }
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:279-280
  if (the source predicate first_dict is not None is truthy) {
    // Source: vvaharness/pipeline/stages/s1_autoexclude.py:280-280
    End this invocation with first_dict.
  }
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:281-283
  if (the source predicate not parsed_any and err is not None is truthy) {
    // Source: vvaharness/pipeline/stages/s1_autoexclude.py:283-283
    In source order: Evaluate log.warning(Event.S1_MODEL_YAML_UNPARSEABLE, detail=redact(str(err))[:200]); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:284-284
  End this invocation with {}.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:288-288
In source order: Evaluate once re.compile('^(?:\\*\\*/)?\\*(\\.[A-Za-z0-9_]+)$'); assign in source target order to _BARE_LANG_GLOB.
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:291-300
// Source signature: _erases_language(entry: str) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _erases_language(entry) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:292-293
  In source order: Retain source documentation literal source_literal_292_4; it is not a model call. Then Evaluate once _BARE_LANG_GLOB.match(entry); assign in source target order to m.
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:294-299
  if (the source predicate m is truthy) {
    // Source: vvaharness/pipeline/stages/s1_autoexclude.py:295-295
    In source order: Evaluate once m.group(1).lower(); assign in source target order to ext.
  }
  else {
    // Source: vvaharness/pipeline/stages/s1_autoexclude.py:296-299
    if (the source predicate re.fullmatch('\\.[A-Za-z0-9_]+', entry) is truthy) {
      // Source: vvaharness/pipeline/stages/s1_autoexclude.py:297-297
      In source order: Evaluate once entry.lower(); assign in source target order to ext.
    }
    else {
      // Source: vvaharness/pipeline/stages/s1_autoexclude.py:299-299
      End this invocation with None.
    }
  }
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:300-300
  End this invocation with ext if ext in EXT_TO_LANG else None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:304-309
In source order: Evaluate once frozenset({'dist', 'build', 'out', 'output', 'target', 'coverage', 'vendor', 'vendored', 'third_party', 'thirdparty', 'external', 'node_modules', 'bower_components', 'jspm_packages', 'site-packages', '.next', '.nuxt', '_site', '__snapshots__'}); assign in source target order to _VENDOR_PATH_SEGMENTS.
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:312-319
// Source signature: _is_vendor_or_build_entry(entry: str) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _is_vendor_or_build_entry(entry) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:313-315
  In source order: Retain source documentation literal source_literal_313_4; it is not a model call. Then Evaluate once entry.lower(); assign in source target order to low.
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:316-317
  if (the source predicate '.min.' in low is truthy) {
    // Source: vvaharness/pipeline/stages/s1_autoexclude.py:317-317
    End this invocation with True.
  }
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:318-318
  In source order: Evaluate once [p for p in re.split('[\\\\/]+', low) if p not in ('', '*', '**')]; assign in source target order to parts.
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:319-319
  End this invocation with any((p in _VENDOR_PATH_SEGMENTS for p in parts)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:322-324
// Source signature: _template_files(inventory: list[str]) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _template_files(inventory) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:323-323
  In source order: Retain source documentation literal source_literal_323_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:324-324
  End this invocation with [rel for rel in inventory if is_web_template(rel)].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:328-335
In source order: Evaluate once frozenset({'.pem', '.key', '.ppk', '.p12', '.pfx', '.jks', '.keystore', '.p8', '.pkcs12', '.asc', '.gpg', '.ovpn'}); assign in source target order to _KEY_MATERIAL_EXTS. Then Evaluate once ('id_rsa', 'id_dsa', 'id_ecdsa', 'id_ed25519'); assign in source target order to _KEY_MATERIAL_NAME_PREFIXES. Then Evaluate once frozenset({'.htpasswd', '.git-credentials', '.npmrc', '.pypirc', '.netrc'}); assign in source target order to _KEY_MATERIAL_NAMES.
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:338-343
// Source signature: _is_key_material(rel: str) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _is_key_material(rel) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:339-340
  In source order: Retain source documentation literal source_literal_339_4; it is not a model call. Then Evaluate once rel.rsplit('/', 1)[-1].lower(); assign in source target order to name.
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:341-342
  if (the source predicate name in _KEY_MATERIAL_NAMES or name.startswith(_KEY_MATERIAL_NAME_PREFIXES) is truthy) {
    // Source: vvaharness/pipeline/stages/s1_autoexclude.py:342-342
    End this invocation with True.
  }
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:343-343
  End this invocation with Path(name).suffix in _KEY_MATERIAL_EXTS.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:346-348
// Source signature: _key_material_files(inventory: list[str]) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _key_material_files(inventory) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:347-347
  In source order: Retain source documentation literal source_literal_347_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:348-348
  End this invocation with [rel for rel in inventory if _is_key_material(rel)].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:351-365
// Source signature: _secret_bearing_files(inventory: list[str], repo_root: str) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _secret_bearing_files(inventory, repo_root) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:352-354
  In source order: Retain source documentation literal source_literal_352_4; it is not a model call. Then Evaluate once Path(repo_root); assign in source target order to root. Then For hits, assign []; source annotation list[str].
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:355-364
  for each rel in inventory {
    // Source: vvaharness/pipeline/stages/s1_autoexclude.py:356-361
    Perform the following protected operations {
      // Source: vvaharness/pipeline/stages/s1_autoexclude.py:357-359
      Enter source context managers left-to-right: (root / rel).open('r', encoding='utf-8', errors='replace') bound to fh {
        // Source: vvaharness/pipeline/stages/s1_autoexclude.py:359-359
        In source order: Evaluate once fh.read(_EXCERPT_CHARS); assign in source target order to head.
      }
      Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    }
    // Source: vvaharness/pipeline/stages/s1_autoexclude.py:360-361
    On the first matching source exception OSError, in handler order {
      // Source: vvaharness/pipeline/stages/s1_autoexclude.py:361-361
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/pipeline/stages/s1_autoexclude.py:362-362
    In source order: Evaluate once redact_counts(head); assign in source target order to (_, counts).
    // Source: vvaharness/pipeline/stages/s1_autoexclude.py:363-364
    if (the source predicate counts is truthy) {
      // Source: vvaharness/pipeline/stages/s1_autoexclude.py:364-364
      In source order: Evaluate hits.append(rel); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:365-365
  End this invocation with hits.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:368-370
In source order: Evaluate once frozenset({'javascript', 'typescript'}); assign in source target order to _CLIENT_SINK_LANGUAGES. Then Evaluate once compile_detectors([spec for spec in detector_corpus() if spec.rule_id == 'detector-docwrite-location']); assign in source target order to _CLIENT_SINK_DETECTORS.
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:373-389
// Source signature: _client_sink_files(inventory: list[str], repo_root: str, cfg) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _client_sink_files(inventory, repo_root, cfg) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:374-380
  In source order: Retain source documentation literal source_literal_374_4; it is not a model call. Then Evaluate once FileCache(repo_root, max_kb=getattr(cfg.step1, 'max_file_kb', 1024)); assign in source target order to cache. Then For hits, assign []; source annotation list[str].
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:381-388
  for each rel in inventory {
    // Source: vvaharness/pipeline/stages/s1_autoexclude.py:382-383
    if (the source predicate EXT_TO_LANG.get(Path(rel).suffix.lower()) not in _CLIENT_SINK_LANGUAGES is truthy) {
      // Source: vvaharness/pipeline/stages/s1_autoexclude.py:383-383
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/pipeline/stages/s1_autoexclude.py:384-385
    if (the source predicate _is_vendor_or_build_entry(rel) is truthy) {
      // Source: vvaharness/pipeline/stages/s1_autoexclude.py:385-385
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/pipeline/stages/s1_autoexclude.py:386-386
    In source order: Evaluate once cache.lines(rel); assign in source target order to lines.
    // Source: vvaharness/pipeline/stages/s1_autoexclude.py:387-388
    if (the source predicate lines and detector_hits(rel, lines, _CLIENT_SINK_DETECTORS) is truthy) {
      // Source: vvaharness/pipeline/stages/s1_autoexclude.py:388-388
      In source order: Evaluate hits.append(rel); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:389-389
  End this invocation with hits.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:392-411
// Source signature: _removes_protected_files(protected: list[str], kind: str, entry: str) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _removes_protected_files(protected, kind, entry) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:394-397
  In source order: Retain source documentation literal source_literal_394_4; it is not a model call. Then Evaluate once entry.lower(); assign in source target order to entry_l. Then For hits, assign []; source annotation list[str].
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:398-410
  for each rel in protected {
    // Source: vvaharness/pipeline/stages/s1_autoexclude.py:399-409
    if (the source predicate kind == 'dir' is truthy) {
      // Source: vvaharness/pipeline/stages/s1_autoexclude.py:400-401
      if (the source predicate all((part.lower() != entry_l for part in rel.split('/')[:-1])) is truthy) {
        // Source: vvaharness/pipeline/stages/s1_autoexclude.py:401-401
        Continue the immediately enclosing source loop at its next iteration.
      }
    }
    else {
      // Source: vvaharness/pipeline/stages/s1_autoexclude.py:402-409
      if (the source predicate kind == 'ext' is truthy) {
        // Source: vvaharness/pipeline/stages/s1_autoexclude.py:404-405
        In source order: Evaluate once rel.rsplit('/', 1)[-1].lower(); assign in source target order to name. Then Evaluate once Path(rel).suffix.lower(); assign in source target order to suffix.
        // Source: vvaharness/pipeline/stages/s1_autoexclude.py:406-407
        if (the source predicate not (suffix == entry_l or name.endswith(entry_l)) is truthy) {
          // Source: vvaharness/pipeline/stages/s1_autoexclude.py:407-407
          Continue the immediately enclosing source loop at its next iteration.
        }
      }
      else {
        // Source: vvaharness/pipeline/stages/s1_autoexclude.py:408-409
        if (the source predicate glob_hit(rel, [entry]) is None is truthy) {
          // Source: vvaharness/pipeline/stages/s1_autoexclude.py:409-409
          Continue the immediately enclosing source loop at its next iteration.
        }
      }
    }
    // Source: vvaharness/pipeline/stages/s1_autoexclude.py:410-410
    In source order: Evaluate hits.append(rel); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:411-411
  End this invocation with hits.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:414-433
// Source signature: _norm_list(v, *, lower: bool=False) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _norm_list(v, lower) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:415-416
  if (the source predicate not v is truthy) {
    // Source: vvaharness/pipeline/stages/s1_autoexclude.py:416-416
    End this invocation with [].
  }
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:417-418
  if (the source predicate isinstance(v, str) is truthy) {
    // Source: vvaharness/pipeline/stages/s1_autoexclude.py:418-418
    In source order: Evaluate once [v]; assign in source target order to v.
  }
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:419-419
  In source order: For out, assign []; source annotation list[str].
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:420-426
  for each x in v {
    // Source: vvaharness/pipeline/stages/s1_autoexclude.py:421-422
    if (the source predicate not isinstance(x, str) is truthy) {
      // Source: vvaharness/pipeline/stages/s1_autoexclude.py:422-422
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/pipeline/stages/s1_autoexclude.py:423-423
    In source order: Evaluate once x.strip().strip('/\\'); assign in source target order to x.
    // Source: vvaharness/pipeline/stages/s1_autoexclude.py:424-425
    if (the source predicate not x is truthy) {
      // Source: vvaharness/pipeline/stages/s1_autoexclude.py:425-425
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/pipeline/stages/s1_autoexclude.py:426-426
    In source order: Evaluate out.append(x.lower() if lower else x); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:427-428
  In source order: For seen, assign set(); source annotation set[str]. Then Evaluate once []; assign in source target order to uniq.
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:429-432
  for each x in out {
    // Source: vvaharness/pipeline/stages/s1_autoexclude.py:430-432
    if (the source predicate x not in seen is truthy) {
      // Source: vvaharness/pipeline/stages/s1_autoexclude.py:431-432
      In source order: Evaluate seen.add(x); retain side effects and discard the expression result. Then Evaluate uniq.append(x); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:433-433
  End this invocation with uniq.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:436-473
// Source signature: vet_config_dedup(dd: dict) -> dict
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn vet_config_dedup(dd) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:437-437
  In source order: Retain source documentation literal source_literal_437_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:439-440
  if (the source predicate not isinstance(dd, dict) is truthy) {
    // Source: vvaharness/pipeline/stages/s1_autoexclude.py:440-440
    End this invocation with dd.
  }
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:441-441
  In source order: Evaluate once dict(dd); assign in source target order to out.
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:442-452
  for each flag in ('promote_on_secret_hit', 'promote_on_insecure_value') {
    // Source: vvaharness/pipeline/stages/s1_autoexclude.py:443-452
    if (the source predicate out.get(flag) is False is truthy) {
      // Source: vvaharness/pipeline/stages/s1_autoexclude.py:444-452
      In source order: Evaluate log.warning(Event.S1_CONFIG_DEDUP_VETOED, key=source_template_444_58, proposed=False, reason='a credential-bearing config file could be silently dropped as a near-duplicate'); retain side effects and discard the expression result. Then Evaluate _errlog.log(_TAG, _TAG, source_template_447_24, reason='s1_autoexclude_dedup_flag_veto', recovered=True, flag=flag); retain side effects and discard the expression result. Then Evaluate COUNTERS.bump('s1_autoexclude_dedup_flag_veto'); retain side effects and discard the expression result. Then Delete source targets in order: out[flag].
    }
  }
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:453-453
  In source order: Evaluate once out.get('exts'); assign in source target order to xs.
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:454-472
  if (the source predicate isinstance(xs, list) is truthy) {
    // Source: vvaharness/pipeline/stages/s1_autoexclude.py:455-456
    In source order: Evaluate once [e for e in xs if isinstance(e, str) and (e.lower() in _KEY_MATERIAL_EXTS or _erases_language(e))]; assign in source target order to bad.
    // Source: vvaharness/pipeline/stages/s1_autoexclude.py:457-472
    if (the source predicate bad is truthy) {
      // Source: vvaharness/pipeline/stages/s1_autoexclude.py:458-468
      In source order: Evaluate once [e for e in xs if e not in bad]; assign in source target order to kept. Then Evaluate log.warning(Event.S1_CONFIG_DEDUP_VETOED, key='config_dedup.exts', exts=sorted(bad), reason='key material, a scanner-known language or a server-side template is never safe to drop as a near-duplicate'); retain side effects and discard the expression result. Then Evaluate _errlog.log(_TAG, _TAG, source_template_462_24, reason='s1_autoexclude_dedup_ext_veto', recovered=True, exts=bad); retain side effects and discard the expression result. Then Evaluate COUNTERS.bump('s1_autoexclude_dedup_ext_veto'); retain side effects and discard the expression result.
      // Source: vvaharness/pipeline/stages/s1_autoexclude.py:469-472
      if (the source predicate kept is truthy) {
        // Source: vvaharness/pipeline/stages/s1_autoexclude.py:470-470
        In source order: Evaluate once kept; assign in source target order to out['exts'].
      }
      else {
        // Source: vvaharness/pipeline/stages/s1_autoexclude.py:472-472
        In source order: Delete source targets in order: out['exts'].
      }
    }
  }
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:473-473
  End this invocation with out.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:476-580
// Source signature: vet_overlay(repo_root: str | Path, cfg, *, dirs: list[str], exts: list[str], globs: list[str], inventory: list[str] | None=None) -> tuple[list[str], list[str], list[str]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn vet_overlay(repo_root, cfg, dirs, exts, globs, inventory) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:480-484
  In source order: Retain source documentation literal source_literal_480_4; it is not a model call. Then Evaluate once str(repo_root); assign in source target order to repo_root. Then Evaluate once [x for x in exts + globs if _erases_language(x)]; assign in source target order to vetoed.
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:485-497
  if (the source predicate vetoed is truthy) {
    // Source: vvaharness/pipeline/stages/s1_autoexclude.py:486-497
    In source order: Evaluate once [e for e in exts if _erases_language(e) is None]; assign in source target order to exts. Then Evaluate once [g for g in globs if _erases_language(g) is None]; assign in source target order to globs. Then Evaluate log.warning(Event.S1_OVERLAY_VETOED_LANGUAGE, entries=sorted(vetoed), reason='would erase scannable source'); retain side effects and discard the expression result. Then Evaluate _errlog.log(_TAG, _TAG, source_template_492_20, reason='s1_autoexclude_language_veto', recovered=True, entries=vetoed); retain side effects and discard the expression result. Then Evaluate COUNTERS.bump('s1_autoexclude_language_veto', len(vetoed)); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:500-500
  In source order: Evaluate once inventory if inventory is not None else scope_after(repo_root, cfg); assign in source target order to inv.
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:502-533
  // Source signature: _run_containment_veto(protected: list[str], *, noun: str, label: str, reason: str, counter: str, counter_files: str, errlog_files_key: str, counter_vendor: str) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _run_containment_veto(protected, noun, label, reason, counter, counter_files, errlog_files_key, counter_vendor) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/pipeline/stages/s1_autoexclude.py:506-506
    In source order: Bind names in enclosing nonlocal scope: dirs, exts, globs.
    // Source: vvaharness/pipeline/stages/s1_autoexclude.py:508-530
    // Source signature: _veto(entries: list[str], kind: str) -> list[str]
    Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
    fn _veto(entries, kind) {
      Bind arguments/defaults/annotations exactly as the source signature specifies.
      // Source: vvaharness/pipeline/stages/s1_autoexclude.py:509-509
      In source order: For kept, assign []; source annotation list[str].
      // Source: vvaharness/pipeline/stages/s1_autoexclude.py:510-529
      for each entry in entries {
        // Source: vvaharness/pipeline/stages/s1_autoexclude.py:511-514
        if (the source predicate _is_vendor_or_build_entry(entry) is truthy) {
          // Source: vvaharness/pipeline/stages/s1_autoexclude.py:512-513
          In source order: Evaluate kept.append(entry); retain side effects and discard the expression result. Then Evaluate COUNTERS.bump(counter_vendor); retain side effects and discard the expression result.
          // Source: vvaharness/pipeline/stages/s1_autoexclude.py:514-514
          Continue the immediately enclosing source loop at its next iteration.
        }
        // Source: vvaharness/pipeline/stages/s1_autoexclude.py:515-515
        In source order: Evaluate once _removes_protected_files(protected, kind, entry); assign in source target order to hits.
        // Source: vvaharness/pipeline/stages/s1_autoexclude.py:516-518
        if (the source predicate not hits is truthy) {
          // Source: vvaharness/pipeline/stages/s1_autoexclude.py:517-517
          In source order: Evaluate kept.append(entry); retain side effects and discard the expression result.
          // Source: vvaharness/pipeline/stages/s1_autoexclude.py:518-518
          Continue the immediately enclosing source loop at its next iteration.
        }
        // Source: vvaharness/pipeline/stages/s1_autoexclude.py:519-529
        In source order: Evaluate log.warning(Event.S1_OVERLAY_VETOED, entry=entry, would_exclude=len(hits), kind=noun, example=hits[0]); retain side effects and discard the expression result. Then Evaluate _errlog.log(_TAG, _TAG, source_template_523_28, reason=reason, recovered=True, entry=entry, **{errlog_files_key: len(hits)}); retain side effects and discard the expression result. Then Evaluate COUNTERS.bump(counter); retain side effects and discard the expression result. Then Evaluate COUNTERS.bump(counter_files, len(hits)); retain side effects and discard the expression result.
      }
      // Source: vvaharness/pipeline/stages/s1_autoexclude.py:530-530
      End this invocation with kept.
      If execution reaches this end, finish with the source implicit None result.
    }
    // Source: vvaharness/pipeline/stages/s1_autoexclude.py:532-533
    In source order: Evaluate once (_veto(dirs, 'dir'), _veto(exts, 'ext'), _veto(globs, 'glob')); assign in source target order to (dirs, exts, globs).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:536-545
  if (the source predicate getattr(cfg.step1, 'auto_exclude_protect_templates', True) is truthy) {
    // Source: vvaharness/pipeline/stages/s1_autoexclude.py:537-545
    In source order: Evaluate _run_containment_veto(_template_files(inv), noun='server-side template file(s)', label='template-containment', reason='s1_autoexclude_template_veto', counter='s1_autoexclude_template_veto', counter_files='s1_autoexclude_template_files_protected', errlog_files_key='n_template_files', counter_vendor='s1_autoexclude_template_veto_vendor_exempt'); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:547-556
  if (the source predicate getattr(cfg.step1, 'auto_exclude_protect_key_material', True) is truthy) {
    // Source: vvaharness/pipeline/stages/s1_autoexclude.py:548-556
    In source order: Evaluate _run_containment_veto(_key_material_files(inv), noun='key-material file(s)', label='key-material-containment', reason='s1_autoexclude_key_material_veto', counter='s1_autoexclude_key_material_veto', counter_files='s1_autoexclude_key_material_files_protected', errlog_files_key='n_key_material_files', counter_vendor='s1_autoexclude_key_material_veto_vendor_exempt'); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:558-567
  if (the source predicate getattr(cfg.step1, 'auto_exclude_protect_secrets', True) is truthy) {
    // Source: vvaharness/pipeline/stages/s1_autoexclude.py:559-567
    In source order: Evaluate _run_containment_veto(_secret_bearing_files(inv, repo_root), noun='secret-bearing file(s)', label='secret-bearing-containment', reason='s1_autoexclude_secret_bearing_veto', counter='s1_autoexclude_secret_bearing_veto', counter_files='s1_autoexclude_secret_bearing_files_protected', errlog_files_key='n_secret_bearing_files', counter_vendor='s1_autoexclude_secret_bearing_veto_vendor_exempt'); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:569-578
  if (the source predicate getattr(cfg.step1, 'auto_exclude_protect_client_sinks', True) is truthy) {
    // Source: vvaharness/pipeline/stages/s1_autoexclude.py:570-578
    In source order: Evaluate _run_containment_veto(_client_sink_files(inv, repo_root, cfg), noun='first-party client file(s) with a DOM sink', label='client-sink-containment', reason='s1_autoexclude_client_sink_veto', counter='s1_autoexclude_client_sink_veto', counter_files='s1_autoexclude_client_sink_files_protected', errlog_files_key='n_client_sink_files', counter_vendor='s1_autoexclude_client_sink_veto_vendor_exempt'); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:580-580
  End this invocation with (dirs, exts, globs).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:583-759
// Source signature: run(repo_root: str | Path, cfg, *, out_path: str | Path) -> Path
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn run(repo_root, cfg, out_path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:584-589
  In source order: Retain source documentation literal source_literal_584_4; it is not a model call. Then Evaluate once str(repo_root); assign in source target order to repo_root. Then Evaluate once Path(out_path); assign in source target order to out. Then Evaluate out.parent.mkdir(parents=True, exist_ok=True); retain side effects and discard the expression result. Then Evaluate once _exclusion_sets(cfg); assign in source target order to (base_dirs, base_exts, base_globs).
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:590-592
  In source order: Evaluate once int(getattr(cfg.step1, 'max_file_kb', 1024)); assign in source target order to cur_max_kb. Then Evaluate once dict(_DEDUP_DEFAULTS); assign in source target order to cur_dedup. Then Evaluate once getattr(cfg.step1, 'config_dedup', None); assign in source target order to user_dd.
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:593-597
  if (the source predicate user_dd is not None is truthy) {
    // Source: vvaharness/pipeline/stages/s1_autoexclude.py:594-597
    In source order: Evaluate once user_dd if isinstance(user_dd, dict) else getattr(user_dd, '_data', None) or vars(user_dd); assign in source target order to raw_dd. Then Evaluate cur_dedup.update({k: v for k, v in raw_dd.items() if v is not None}); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:599-639
  In source order: Evaluate once _survey(Path(repo_root), base_dirs, base_exts, base_globs); assign in source target order to (survey, n_files). Then Evaluate once getattr(cfg.models, 'autoexclude', None) or cfg.models.preprocess; assign in source target order to model. Then Evaluate once int(getattr(cfg.step1, 'auto_exclude_max_tokens', 8000)); assign in source target order to max_tok. Then Evaluate once source_template_603_18; assign in source target order to user_prompt. Then Evaluate console.write(source_template_638_18); retain side effects and discard the expression result.
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:640-640
  In source order: Evaluate once knob(cfg, 'step1.auto_exclude_effort', None) or None; assign in source target order to effort.
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:642-655
  // Source signature: _dispatch(*, drop_thinking: bool) -> str
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _dispatch(drop_thinking) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/pipeline/stages/s1_autoexclude.py:643-655
    End this invocation with _deepagents.dispatch_prompt(user_prompt, model=model, cfg=cfg, cwd=repo_root, system_prompt=_SYSTEM, max_tokens=max_tok, tag=_TAG, graph_name='s1-autoexclude', effort=None if drop_thinking else effort).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:658-663
  Enter source context managers left-to-right: stage_floors(_TAG, min_chars=_MIN_RESPONSE_CHARS, min_tokens=_MIN_RESPONSE_TOKENS) {
    // Source: vvaharness/pipeline/stages/s1_autoexclude.py:660-663
    In source order: Evaluate once dispatch_or_retry_unforced(_dispatch, 'survey', stage='s1', effort=_deepagents.droppable_effort(model, effort, agentic=False), resend_refusal=refusal_resend_allowed(cfg, model)); assign in source target order to raw.
  }
  Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:665-671
  In source order: Evaluate once _extract_yaml(raw); assign in source target order to data. Then Evaluate once {d.lower() for d in base_dirs}; assign in source target order to base_dirs_l. Then Evaluate once {e.lower() for e in base_exts}; assign in source target order to base_exts_l. Then Evaluate once [d for d in _norm_list(data.get('exclude_dirs')) if d.lower() not in base_dirs_l]; assign in source target order to dirs. Then Evaluate once []; assign in source target order to exts.
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:672-676
  for each e in _norm_list(data.get('exclude_exts'), lower=True) {
    // Source: vvaharness/pipeline/stages/s1_autoexclude.py:673-674
    if (the source predicate not e.startswith('.') is truthy) {
      // Source: vvaharness/pipeline/stages/s1_autoexclude.py:674-674
      In source order: Evaluate once '.' + e; assign in source target order to e.
    }
    // Source: vvaharness/pipeline/stages/s1_autoexclude.py:675-676
    if (the source predicate e not in base_exts_l is truthy) {
      // Source: vvaharness/pipeline/stages/s1_autoexclude.py:676-676
      In source order: Evaluate exts.append(e); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:677-688
  In source order: Evaluate once [g for g in _norm_list(data.get('exclude_globs')) if g not in set(base_globs)]; assign in source target order to globs. Then Evaluate once scope_after(repo_root, cfg); assign in source target order to inv. Then Evaluate once vet_overlay(repo_root, cfg, dirs=dirs, exts=exts, globs=globs, inventory=inv); assign in source target order to (dirs, exts, globs). Then Evaluate once data.get('max_file_kb'); assign in source target order to mfk. Then Evaluate once int(mfk) if isinstance(mfk, (int, float)) and int(mfk) > 0 and (int(mfk) != cur_max_kb) else None; assign in source target order to new_max_kb.
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:691-696
  In source order: Evaluate once len(inv); assign in source target order to n_before. Then Evaluate once scope_after(repo_root, cfg, dirs=dirs, exts=exts, globs=globs, max_file_kb=new_max_kb); assign in source target order to after. Then Evaluate once len(after); assign in source target order to n_after. Then Evaluate once sorted(set(inv) - set(after)); assign in source target order to removed.
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:697-712
  if (the source predicate n_before and (not n_after) is truthy) {
    // Source: vvaharness/pipeline/stages/s1_autoexclude.py:699-706
    In source order: Evaluate log.warning(Event.S1_OVERLAY_EMPTIES_SCOPE, files_before=n_before, files_after=0, remedy='scanning with global step1 only'); retain side effects and discard the expression result. Then Evaluate _errlog.log(_TAG, _TAG, source_template_702_20, reason='s1_autoexclude_empty_scope', files_before=n_before); retain side effects and discard the expression result. Then Evaluate once ([], [], [], None); assign in source target order to (dirs, exts, globs, new_max_kb).
  }
  else {
    // Source: vvaharness/pipeline/stages/s1_autoexclude.py:707-712
    if (the source predicate n_before and n_after / n_before < _AGGRESSIVE_KEEP_RATIO is truthy) {
      // Source: vvaharness/pipeline/stages/s1_autoexclude.py:709-712
      In source order: Evaluate once ', '.join(removed[:3]); assign in source target order to sample. Then Evaluate log.warning(Event.S1_OVERLAY_AGGRESSIVE, files_before=n_before, files_after=n_after, dropped=source_template_711_28, example=sample or None, remedy='re-run with --no-auto-step1 if coverage looks wrong'); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:714-715
  In source order: For overlay, assign {'exclude_dirs': dirs, 'exclude_exts': exts, 'exclude_globs': globs}; source annotation dict.
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:716-717
  if (the source predicate new_max_kb is not None is truthy) {
    // Source: vvaharness/pipeline/stages/s1_autoexclude.py:717-717
    In source order: Evaluate once new_max_kb; assign in source target order to overlay['max_file_kb'].
  }
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:719-719
  In source order: Evaluate once data.get('config_dedup'); assign in source target order to dd_in.
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:720-738
  if (the source predicate isinstance(dd_in, dict) is truthy) {
    // Source: vvaharness/pipeline/stages/s1_autoexclude.py:721-721
    In source order: For dd_out, assign {}; source annotation dict.
    // Source: vvaharness/pipeline/stages/s1_autoexclude.py:722-734
    for each (k, typ) in _DEDUP_KEYS.items() {
      // Source: vvaharness/pipeline/stages/s1_autoexclude.py:723-724
      if (the source predicate k not in dd_in is truthy) {
        // Source: vvaharness/pipeline/stages/s1_autoexclude.py:724-724
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/pipeline/stages/s1_autoexclude.py:725-725
      In source order: Evaluate once dd_in[k]; assign in source target order to v.
      // Source: vvaharness/pipeline/stages/s1_autoexclude.py:726-734
      if (the source predicate typ is list is truthy) {
        // Source: vvaharness/pipeline/stages/s1_autoexclude.py:727-728
        In source order: Evaluate once [('.' + e.lstrip('.')).lower() for e in _norm_list(v, lower=True)]; assign in source target order to xs.
        // Source: vvaharness/pipeline/stages/s1_autoexclude.py:729-730
        if (the source predicate xs is truthy) {
          // Source: vvaharness/pipeline/stages/s1_autoexclude.py:730-730
          In source order: Evaluate once xs; assign in source target order to dd_out[k].
        }
      }
      else {
        // Source: vvaharness/pipeline/stages/s1_autoexclude.py:731-734
        if (the source predicate typ is bool and isinstance(v, bool) is truthy) {
          // Source: vvaharness/pipeline/stages/s1_autoexclude.py:732-732
          In source order: Evaluate once v; assign in source target order to dd_out[k].
        }
        else {
          // Source: vvaharness/pipeline/stages/s1_autoexclude.py:733-734
          if (the source predicate typ is int and isinstance(v, (int, float)) is truthy) {
            // Source: vvaharness/pipeline/stages/s1_autoexclude.py:734-734
            In source order: Evaluate once int(v); assign in source target order to dd_out[k].
          }
        }
      }
    }
    // Source: vvaharness/pipeline/stages/s1_autoexclude.py:736-736
    In source order: Evaluate once vet_config_dedup(dd_out); assign in source target order to dd_out.
    // Source: vvaharness/pipeline/stages/s1_autoexclude.py:737-738
    if (the source predicate dd_out is truthy) {
      // Source: vvaharness/pipeline/stages/s1_autoexclude.py:738-738
      In source order: Evaluate once dd_out; assign in source target order to overlay['config_dedup'].
    }
  }
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:741-744
  if (the source predicate 'config_dedup' in overlay is truthy) {
    // Source: vvaharness/pipeline/stages/s1_autoexclude.py:742-742
    In source order: Evaluate once vet_config_dedup(overlay['config_dedup']); assign in source target order to overlay['config_dedup'].
    // Source: vvaharness/pipeline/stages/s1_autoexclude.py:743-744
    if (the source predicate not overlay['config_dedup'] is truthy) {
      // Source: vvaharness/pipeline/stages/s1_autoexclude.py:744-744
      In source order: Delete source targets in order: overlay['config_dedup'].
    }
  }
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:746-751
  In source order: Evaluate out.write_text(source_literal_747_8 + yaml.safe_dump(overlay, sort_keys=False, default_flow_style=False), encoding='utf-8'); retain side effects and discard the expression result. Then Evaluate once []; assign in source target order to extras.
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:752-753
  if (the source predicate 'max_file_kb' in overlay is truthy) {
    // Source: vvaharness/pipeline/stages/s1_autoexclude.py:753-753
    In source order: Evaluate extras.append(source_template_753_22); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:754-755
  if (the source predicate 'config_dedup' in overlay is truthy) {
    // Source: vvaharness/pipeline/stages/s1_autoexclude.py:755-755
    In source order: Evaluate extras.append(source_template_755_22); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:756-758
  In source order: Evaluate console.write(source_template_756_18); retain side effects and discard the expression result.
  // Source: vvaharness/pipeline/stages/s1_autoexclude.py:759-759
  End this invocation with out.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.util import logs` at source line 17: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import logs` at source line 17: `source_detail/vvaharness/util/logs.py.sudo.md`.
- `from vvaharness.backends.llm import deepagents as _deepagents` at source line 27: `source_detail/vvaharness/backends/llm/__init__.py.sudo.md`.
- `from vvaharness.backends.llm import deepagents as _deepagents` at source line 27: `source_detail/vvaharness/backends/llm/deepagents.py.sudo.md`.
- `from vvaharness.backends.llm.models import refusal_resend_allowed` at source line 28: `source_detail/vvaharness/backends/llm/models.py.sudo.md`.
- `from vvaharness.detect.matcher import compile_detectors, detector_hits` at source line 29: `source_detail/vvaharness/detect/matcher.py.sudo.md`.
- `from vvaharness.detect.patterns import detector_corpus` at source line 30: `source_detail/vvaharness/detect/patterns.py.sudo.md`.
- `from vvaharness.lang.detect import EXT_TO_LANG, is_web_template` at source line 31: `source_detail/vvaharness/lang/detect.py.sudo.md`.
- `from vvaharness.pipeline.stages.s5.enrich import FileCache` at source line 32: `source_detail/vvaharness/pipeline/stages/s5/enrich.py.sudo.md`.
- `from vvaharness.report.redact import redact, redact_counts` at source line 33: `source_detail/vvaharness/report/redact.py.sudo.md`.
- `from vvaharness.scope import _DEDUP_DEFAULTS, _exclusion_sets, glob_hit, scope_after` at source line 34: `source_detail/vvaharness/scope/__init__.py.sudo.md`.
- `from vvaharness.util import console` at source line 40: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import console` at source line 40: `source_detail/vvaharness/util/console.py.sudo.md`.
- `from vvaharness.util import errlog as _errlog` at source line 41: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import errlog as _errlog` at source line 41: `source_detail/vvaharness/util/errlog.py.sudo.md`.
- `from vvaharness.util.config import knob` at source line 42: `source_detail/vvaharness/util/config.py.sudo.md`.
- `from vvaharness.util.counters import COUNTERS` at source line 43: `source_detail/vvaharness/util/counters.py.sudo.md`.
- `from vvaharness.util.response_quality import dispatch_or_retry_unforced, stage_floors` at source line 44: `source_detail/vvaharness/util/response_quality.py.sudo.md`.
- `from vvaharness.util.events import Event` at source line 45: `source_detail/vvaharness/util/events.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../prompt_representation/vvaharness/pipeline/stages/s1_autoexclude.py.sudo.md). Exact strings in the evidence asset support this conversion.
