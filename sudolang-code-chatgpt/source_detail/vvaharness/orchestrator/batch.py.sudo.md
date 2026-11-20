# vvaharness/orchestrator/batch.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/orchestrator/batch.py.evidence.json`. SHA-256: `dd625e08d6fdf762a9976f1d592cbe6f076b965f56046388af1ff5816fe83e60`.

```sudo
// Source: vvaharness/orchestrator/batch.py:14-19
In source order: Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import logs; preserve alias and import-time effects. Then Retain source documentation literal source_literal_17_0; it is not a model call. Then Resolve source import import csv; preserve alias and import-time effects. Then Resolve source import import fnmatch; preserve alias and import-time effects.
// Source: vvaharness/orchestrator/batch.py:20-24
In source order: Resolve source import import hashlib; preserve alias and import-time effects. Then Resolve source import import json; preserve alias and import-time effects. Then Resolve source import import os; preserve alias and import-time effects. Then Resolve source import import re; preserve alias and import-time effects. Then Resolve source import import shutil; preserve alias and import-time effects.
// Source: vvaharness/orchestrator/batch.py:25-29
In source order: Resolve source import import subprocess; preserve alias and import-time effects. Then Resolve source import import sys; preserve alias and import-time effects. Then Resolve source import import time; preserve alias and import-time effects. Then Resolve source import import traceback; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects.
// Source: vvaharness/orchestrator/batch.py:31-37
In source order: Resolve source import from vvaharness.backends.harness.models import AuthenticationError, ProxyError; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm import cli; preserve alias and import-time effects. Then Resolve source import from vvaharness.models import _md_cell; preserve alias and import-time effects. Then Resolve source import from vvaharness.orchestrator import store as _store; preserve alias and import-time effects. Then Resolve source import from vvaharness.orchestrator.case_rollup import EXIT_NOT_REMEDIATED; preserve alias and import-time effects.
// Source: vvaharness/orchestrator/batch.py:38-42
In source order: Resolve source import from vvaharness.orchestrator.cleanup import _preserve_set, _purge_clone, _rmtree_rw; preserve alias and import-time effects. Then Resolve source import from vvaharness.orchestrator.cmdb import _load_app_profile; preserve alias and import-time effects. Then Resolve source import from vvaharness.orchestrator.scan import ScanOutcome, scan_repo; preserve alias and import-time effects. Then Resolve source import from vvaharness.report.redact import reset_known_values as _reset_redact_known_values; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import console; preserve alias and import-time effects.
// Source: vvaharness/orchestrator/batch.py:43-47
In source order: Resolve source import from vvaharness.util import errlog as _errlog; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.counters import COUNTERS; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.events import Event; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.response_quality import reset_counters as _reset_quality_counters; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.stage_telemetry import CACHED_PROVENANCE, STAGES; preserve alias and import-time effects.
// Source: vvaharness/orchestrator/batch.py:48-51
In source order: Resolve source import from vvaharness.util.tokens import TOKENS; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.warn_once import reset_warn_once_registries as _reset_warn_once; preserve alias and import-time effects. Then Evaluate once logs.get_logger(__name__); assign in source target order to log.
// Source: vvaharness/orchestrator/batch.py:54-58
// Source signature: _module_name_from(ref: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _module_name_from(ref) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/batch.py:55-55
  In source order: Evaluate once ref.rstrip('/').split('/')[-1]; assign in source target order to tail.
  // Source: vvaharness/orchestrator/batch.py:56-57
  if (the source predicate tail.lower().endswith('.git') is truthy) {
    // Source: vvaharness/orchestrator/batch.py:57-57
    In source order: Evaluate once tail[:-4]; assign in source target order to tail.
  }
  // Source: vvaharness/orchestrator/batch.py:58-58
  End this invocation with tail or 'repo'.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/batch.py:61-62
// Source signature: _is_remote(ref: str) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _is_remote(ref) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/batch.py:62-62
  End this invocation with ref.startswith(('http://', 'https://', 'git@', 'ssh://')) or ref.endswith('.git').
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/batch.py:66-66
In source order: Evaluate once re.compile('(\\w[\\w+.\\-]*://)[^/@\\s]+@'); assign in source target order to _URL_USERINFO_RX.
// Source: vvaharness/orchestrator/batch.py:69-72
// Source signature: _scrub_url_secrets(s: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _scrub_url_secrets(s) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/batch.py:70-71
  if (the source predicate not s is truthy) {
    // Source: vvaharness/orchestrator/batch.py:71-71
    End this invocation with s.
  }
  // Source: vvaharness/orchestrator/batch.py:72-72
  End this invocation with _URL_USERINFO_RX.sub('\\1***@', s).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/batch.py:75-77
// Source signature: _clone_url_for(repo_name: str, base: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _clone_url_for(repo_name, base) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/batch.py:76-76
  In source order: Retain source documentation literal source_literal_76_4; it is not a model call.
  // Source: vvaharness/orchestrator/batch.py:77-77
  End this invocation with source_template_77_11.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/batch.py:81-82
// Source signature: _state_root() -> Path
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _state_root() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/batch.py:82-82
  End this invocation with _store.state_root().
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/batch.py:85-87
// Source signature: _ref_id(ref: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _ref_id(ref) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/batch.py:86-86
  In source order: Retain source documentation literal source_literal_86_4; it is not a model call.
  // Source: vvaharness/orchestrator/batch.py:87-87
  End this invocation with hashlib.sha256(str(ref).encode('utf-8')).hexdigest()[:32].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/batch.py:90-92
// Source signature: _stage_marker_path(dest: Path) -> Path
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _stage_marker_path(dest) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/batch.py:91-91
  In source order: Evaluate once hashlib.sha256(str(Path(dest).resolve()).encode('utf-8')).hexdigest()[:32]; assign in source target order to key.
  // Source: vvaharness/orchestrator/batch.py:92-92
  End this invocation with _state_root() / 'stage-markers' / source_template_92_45.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/batch.py:95-104
// Source signature: _write_stage_marker(dest: Path, ref: str, kind: str) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _write_stage_marker(dest, ref, kind) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/batch.py:96-97
  In source order: Retain source documentation literal source_literal_96_4; it is not a model call. Then Evaluate once _stage_marker_path(dest); assign in source target order to mp.
  // Source: vvaharness/orchestrator/batch.py:98-104
  Perform the following protected operations {
    // Source: vvaharness/orchestrator/batch.py:100-102
    In source order: Evaluate _store.ensure_state_dir('stage-markers'); retain side effects and discard the expression result. Then Evaluate mp.write_text(json.dumps({'v': 1, 'kind': kind, 'ref_id': _ref_id(ref)}), encoding='utf-8'); retain side effects and discard the expression result.
  }
  // Source: vvaharness/orchestrator/batch.py:103-104
  On the first matching source exception OSError as e, in handler order {
    // Source: vvaharness/orchestrator/batch.py:104-104
    In source order: Evaluate log.warning(Event.BATCH_MARKER_WRITE_FAILED, path=dest, detail=str(e)); retain side effects and discard the expression result.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/batch.py:107-113
// Source signature: _stage_dir_bound(dest: Path, ref: str) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _stage_dir_bound(dest, ref) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/batch.py:108-108
  In source order: Retain source documentation literal source_literal_108_4; it is not a model call.
  // Source: vvaharness/orchestrator/batch.py:109-112
  Perform the following protected operations {
    // Source: vvaharness/orchestrator/batch.py:110-110
    In source order: Evaluate once json.loads(_stage_marker_path(dest).read_text(encoding='utf-8')); assign in source target order to data.
  }
  // Source: vvaharness/orchestrator/batch.py:111-112
  On the first matching source exception (OSError, ValueError), in handler order {
    // Source: vvaharness/orchestrator/batch.py:112-112
    End this invocation with False.
  }
  // Source: vvaharness/orchestrator/batch.py:113-113
  End this invocation with isinstance(data, dict) and data.get('ref_id') == _ref_id(ref).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/batch.py:116-129
// Source signature: _assign_slugs(repos: list[dict]) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _assign_slugs(repos) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/batch.py:117-119
  In source order: Retain source documentation literal source_literal_117_4; it is not a model call. Then For slugs, assign []; source annotation list[str]. Then For used, assign set(); source annotation set[str].
  // Source: vvaharness/orchestrator/batch.py:120-128
  for each r in repos {
    // Source: vvaharness/orchestrator/batch.py:121-123
    In source order: Evaluate once _module_name_from(r['repo_name']); assign in source target order to base. Then Evaluate once base; assign in source target order to slug. Then Evaluate once r['repo_name']; assign in source target order to salt.
    // Source: vvaharness/orchestrator/batch.py:124-126
    while (the source predicate slug in used is truthy) {
      // Source: vvaharness/orchestrator/batch.py:125-126
      In source order: Evaluate once source_template_125_19; assign in source target order to slug. Then Evaluate once slug + r['repo_name']; assign in source target order to salt.
    }
    // Source: vvaharness/orchestrator/batch.py:127-128
    In source order: Evaluate used.add(slug); retain side effects and discard the expression result. Then Evaluate slugs.append(slug); retain side effects and discard the expression result.
  }
  // Source: vvaharness/orchestrator/batch.py:129-129
  End this invocation with slugs.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/batch.py:133-134
In source order: Evaluate once 64 * 1024 * 1024; assign in source target order to _MANIFEST_MAX_BYTES. Then Evaluate once 200000; assign in source target order to _MANIFEST_MAX_ROWS.
// Source: vvaharness/orchestrator/batch.py:137-147
// Source signature: _check_manifest_size(list_file: Path) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _check_manifest_size(list_file) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/batch.py:138-138
  In source order: Retain source documentation literal source_literal_138_4; it is not a model call.
  // Source: vvaharness/orchestrator/batch.py:139-142
  Perform the following protected operations {
    // Source: vvaharness/orchestrator/batch.py:140-140
    In source order: Evaluate once list_file.stat().st_size; assign in source target order to size.
  }
  // Source: vvaharness/orchestrator/batch.py:141-142
  On the first matching source exception OSError as e, in handler order {
    // Source: vvaharness/orchestrator/batch.py:142-142
    Raise ValueError(source_template_142_25).
  }
  // Source: vvaharness/orchestrator/batch.py:143-147
  if (the source predicate size > _MANIFEST_MAX_BYTES is truthy) {
    // Source: vvaharness/orchestrator/batch.py:144-147
    Raise ValueError(source_template_145_12).
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/batch.py:150-226
// Source signature: _parse_repo_csv(list_file: Path, git_base_url: str | None) -> list[dict]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _parse_repo_csv(list_file, git_base_url) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/batch.py:151-152
  In source order: Retain source documentation literal source_literal_151_4; it is not a model call. Then Evaluate _check_manifest_size(list_file); retain side effects and discard the expression result.
  // Source: vvaharness/orchestrator/batch.py:154-219
  Enter source context managers left-to-right: open(list_file, newline='', encoding='utf-8-sig') bound to fh {
    // Source: vvaharness/orchestrator/batch.py:155-155
    In source order: Evaluate once csv.reader(fh); assign in source target order to rows.
    // Source: vvaharness/orchestrator/batch.py:156-159
    Perform the following protected operations {
      // Source: vvaharness/orchestrator/batch.py:157-157
      In source order: Evaluate once next(rows); assign in source target order to header.
    }
    // Source: vvaharness/orchestrator/batch.py:158-159
    On the first matching source exception StopIteration, in handler order {
      // Source: vvaharness/orchestrator/batch.py:159-159
      Raise ValueError(source_template_159_29).
    }
    // Source: vvaharness/orchestrator/batch.py:161-161
    In source order: Evaluate once {str(h).strip().lower(): i for i, h in enumerate(header) if h}; assign in source target order to hdr.
    // Source: vvaharness/orchestrator/batch.py:162-166
    // Source signature: col(*names)
    Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
    fn col(names) {
      Bind arguments/defaults/annotations exactly as the source signature specifies.
      // Source: vvaharness/orchestrator/batch.py:163-165
      for each n in names {
        // Source: vvaharness/orchestrator/batch.py:164-165
        if (the source predicate n in hdr is truthy) {
          // Source: vvaharness/orchestrator/batch.py:165-165
          End this invocation with hdr[n].
        }
      }
      // Source: vvaharness/orchestrator/batch.py:166-166
      End this invocation with None.
      If execution reaches this end, finish with the source implicit None result.
    }
    // Source: vvaharness/orchestrator/batch.py:167-169
    In source order: Evaluate once col('appid', 'application_id', 'app_id', 'applicationid'); assign in source target order to i_app. Then Evaluate once col('reponame', 'repository_name', 'repo_name', 'repo'); assign in source target order to i_repo. Then Evaluate once col('path', 'url', 'repo_url', 'ref'); assign in source target order to i_path.
    // Source: vvaharness/orchestrator/batch.py:170-173
    if (the source predicate i_app is None or i_repo is None is truthy) {
      // Source: vvaharness/orchestrator/batch.py:171-173
      Raise ValueError(source_template_172_16).
    }
    // Source: vvaharness/orchestrator/batch.py:174-177
    if (the source predicate i_path is None and (not git_base_url) is truthy) {
      // Source: vvaharness/orchestrator/batch.py:175-177
      Raise ValueError(source_template_176_16).
    }
    // Source: vvaharness/orchestrator/batch.py:179-181
    In source order: For entries, assign []; source annotation list[dict]. Then For errors, assign []; source annotation list[str]. Then For seen, assign set(); source annotation set[str].
    // Source: vvaharness/orchestrator/batch.py:182-219
    for each (lineno, row) in enumerate(rows, 2) {
      // Source: vvaharness/orchestrator/batch.py:183-186
      if (the source predicate lineno - 1 > _MANIFEST_MAX_ROWS is truthy) {
        // Source: vvaharness/orchestrator/batch.py:184-186
        Raise ValueError(source_template_185_20).
      }
      // Source: vvaharness/orchestrator/batch.py:187-190
      // Source signature: at(i)
      Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
      fn at(i) {
        Bind arguments/defaults/annotations exactly as the source signature specifies.
        // Source: vvaharness/orchestrator/batch.py:188-189
        if (the source predicate i is None or i >= len(row) is truthy) {
          // Source: vvaharness/orchestrator/batch.py:189-189
          End this invocation with ''.
        }
        // Source: vvaharness/orchestrator/batch.py:190-190
        End this invocation with str(row[i]).strip().
        If execution reaches this end, finish with the source implicit None result.
      }
      // Source: vvaharness/orchestrator/batch.py:191-191
      In source order: Evaluate once (at(i_app), at(i_repo), at(i_path)); assign in source target order to (app_id, repo_name, ref).
      // Source: vvaharness/orchestrator/batch.py:192-193
      if (the source predicate not app_id and (not repo_name) is truthy) {
        // Source: vvaharness/orchestrator/batch.py:193-193
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/orchestrator/batch.py:194-196
      if (the source predicate not app_id or not repo_name is truthy) {
        // Source: vvaharness/orchestrator/batch.py:195-195
        In source order: Evaluate errors.append(source_template_195_30); retain side effects and discard the expression result.
        // Source: vvaharness/orchestrator/batch.py:196-196
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/orchestrator/batch.py:197-204
      if (the source predicate not ref is truthy) {
        // Source: vvaharness/orchestrator/batch.py:199-203
        if (the source predicate not git_base_url is truthy) {
          // Source: vvaharness/orchestrator/batch.py:200-202
          In source order: Evaluate errors.append(source_template_201_24); retain side effects and discard the expression result.
          // Source: vvaharness/orchestrator/batch.py:203-203
          Continue the immediately enclosing source loop at its next iteration.
        }
        // Source: vvaharness/orchestrator/batch.py:204-204
        In source order: Evaluate once _clone_url_for(repo_name, git_base_url); assign in source target order to ref.
      }
      // Source: vvaharness/orchestrator/batch.py:205-208
      if (the source predicate ref.lstrip().startswith('-') is truthy) {
        // Source: vvaharness/orchestrator/batch.py:207-207
        In source order: Evaluate errors.append(source_template_207_30); retain side effects and discard the expression result.
        // Source: vvaharness/orchestrator/batch.py:208-208
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/orchestrator/batch.py:209-212
      if (the source predicate not _is_remote(ref) and (not Path(ref).is_dir()) is truthy) {
        // Source: vvaharness/orchestrator/batch.py:210-211
        In source order: Evaluate errors.append(source_template_210_30); retain side effects and discard the expression result.
        // Source: vvaharness/orchestrator/batch.py:212-212
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/orchestrator/batch.py:213-215
      if (the source predicate ref in seen is truthy) {
        // Source: vvaharness/orchestrator/batch.py:214-214
        In source order: Evaluate errors.append(source_template_214_30); retain side effects and discard the expression result.
        // Source: vvaharness/orchestrator/batch.py:215-215
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/orchestrator/batch.py:216-219
      In source order: Evaluate seen.add(ref); retain side effects and discard the expression result. Then Evaluate entries.append({'application_id': app_id, 'repo_name': repo_name, 'ref': ref}); retain side effects and discard the expression result.
    }
  }
  Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
  // Source: vvaharness/orchestrator/batch.py:221-223
  if (the source predicate errors is truthy) {
    // Source: vvaharness/orchestrator/batch.py:222-223
    Raise ValueError(source_template_222_25 + source_literal_223_27.join(errors)).
  }
  // Source: vvaharness/orchestrator/batch.py:224-225
  if (the source predicate not entries is truthy) {
    // Source: vvaharness/orchestrator/batch.py:225-225
    Raise ValueError(source_template_225_25).
  }
  // Source: vvaharness/orchestrator/batch.py:226-226
  End this invocation with entries.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/batch.py:229-287
// Source signature: _parse_repo_file(list_file: Path) -> list[dict]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _parse_repo_file(list_file) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/batch.py:230-234
  In source order: Retain source documentation literal source_literal_230_4; it is not a model call. Then Evaluate _check_manifest_size(list_file); retain side effects and discard the expression result. Then For entries, assign []; source annotation list[dict]. Then For errors, assign []; source annotation list[str]. Then For seen, assign set(); source annotation set[str].
  // Source: vvaharness/orchestrator/batch.py:237-279
  Enter source context managers left-to-right: open(list_file, encoding='utf-8') bound to fh {
    // Source: vvaharness/orchestrator/batch.py:238-279
    for each (lineno, raw) in enumerate(fh, 1) {
      // Source: vvaharness/orchestrator/batch.py:239-242
      if (the source predicate lineno > _MANIFEST_MAX_ROWS is truthy) {
        // Source: vvaharness/orchestrator/batch.py:240-242
        Raise ValueError(source_template_241_20).
      }
      // Source: vvaharness/orchestrator/batch.py:243-243
      In source order: Evaluate once raw.strip(); assign in source target order to line.
      // Source: vvaharness/orchestrator/batch.py:244-245
      if (the source predicate not line or line.startswith('#') is truthy) {
        // Source: vvaharness/orchestrator/batch.py:245-245
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/orchestrator/batch.py:247-247
      In source order: Evaluate once [p.strip() for p in line.split(',')]; assign in source target order to parts.
      // Source: vvaharness/orchestrator/batch.py:248-251
      if (the source predicate len(parts) != 3 is truthy) {
        // Source: vvaharness/orchestrator/batch.py:249-250
        In source order: Evaluate errors.append(source_template_249_30); retain side effects and discard the expression result.
        // Source: vvaharness/orchestrator/batch.py:251-251
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/orchestrator/batch.py:253-253
      In source order: Evaluate once parts; assign in source target order to (app_id, repo_name, ref).
      // Source: vvaharness/orchestrator/batch.py:254-255
      if (the source predicate not app_id is truthy) {
        // Source: vvaharness/orchestrator/batch.py:255-255
        In source order: Evaluate errors.append(source_template_255_30); retain side effects and discard the expression result.
      }
      // Source: vvaharness/orchestrator/batch.py:256-257
      if (the source predicate not repo_name is truthy) {
        // Source: vvaharness/orchestrator/batch.py:257-257
        In source order: Evaluate errors.append(source_template_257_30); retain side effects and discard the expression result.
      }
      // Source: vvaharness/orchestrator/batch.py:258-259
      if (the source predicate not ref is truthy) {
        // Source: vvaharness/orchestrator/batch.py:259-259
        In source order: Evaluate errors.append(source_template_259_30); retain side effects and discard the expression result.
      }
      // Source: vvaharness/orchestrator/batch.py:260-261
      if (the source predicate not (app_id and repo_name and ref) is truthy) {
        // Source: vvaharness/orchestrator/batch.py:261-261
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/orchestrator/batch.py:263-266
      if (the source predicate ref.lstrip().startswith('-') is truthy) {
        // Source: vvaharness/orchestrator/batch.py:265-265
        In source order: Evaluate errors.append(source_template_265_30); retain side effects and discard the expression result.
        // Source: vvaharness/orchestrator/batch.py:266-266
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/orchestrator/batch.py:267-270
      if (the source predicate not _is_remote(ref) and (not Path(ref).is_dir()) is truthy) {
        // Source: vvaharness/orchestrator/batch.py:268-269
        In source order: Evaluate errors.append(source_template_268_30); retain side effects and discard the expression result.
        // Source: vvaharness/orchestrator/batch.py:270-270
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/orchestrator/batch.py:272-274
      if (the source predicate ref in seen is truthy) {
        // Source: vvaharness/orchestrator/batch.py:273-273
        In source order: Evaluate errors.append(source_template_273_30); retain side effects and discard the expression result.
        // Source: vvaharness/orchestrator/batch.py:274-274
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/orchestrator/batch.py:275-279
      In source order: Evaluate seen.add(ref); retain side effects and discard the expression result. Then Evaluate entries.append({'application_id': app_id, 'repo_name': repo_name, 'ref': ref}); retain side effects and discard the expression result.
    }
  }
  Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
  // Source: vvaharness/orchestrator/batch.py:281-284
  if (the source predicate errors is truthy) {
    // Source: vvaharness/orchestrator/batch.py:282-283
    In source order: Evaluate once source_template_282_14 + source_literal_283_16.join(errors); assign in source target order to msg.
    // Source: vvaharness/orchestrator/batch.py:284-284
    Raise ValueError(msg).
  }
  // Source: vvaharness/orchestrator/batch.py:285-286
  if (the source predicate not entries is truthy) {
    // Source: vvaharness/orchestrator/batch.py:286-286
    Raise ValueError(source_template_286_25).
  }
  // Source: vvaharness/orchestrator/batch.py:287-287
  End this invocation with entries.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/batch.py:290-294
// Source signature: _with_token(url: str, token: str | None) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _with_token(url, token) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/batch.py:291-292
  if (the source predicate not token or not url.startswith(('http://', 'https://')) or '@' in url.split('//', 1)[1] is truthy) {
    // Source: vvaharness/orchestrator/batch.py:292-292
    End this invocation with url.
  }
  // Source: vvaharness/orchestrator/batch.py:293-293
  In source order: Evaluate once url.split('://', 1); assign in source target order to (scheme, rest).
  // Source: vvaharness/orchestrator/batch.py:294-294
  End this invocation with source_template_294_11.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/batch.py:297-350
// Source signature: _acquire_repo(ref: str, workspace: Path, git_token: str | None, dest_name: str | None=None) -> Path
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _acquire_repo(ref, workspace, git_token, dest_name) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/batch.py:299-299
  In source order: Retain source documentation literal source_literal_299_4; it is not a model call.
  // Source: vvaharness/orchestrator/batch.py:300-304
  if (the source predicate not _is_remote(ref) is truthy) {
    // Source: vvaharness/orchestrator/batch.py:301-301
    In source order: Evaluate once Path(ref); assign in source target order to p.
    // Source: vvaharness/orchestrator/batch.py:302-303
    if (the source predicate not p.is_dir() is truthy) {
      // Source: vvaharness/orchestrator/batch.py:303-303
      Raise RuntimeError(source_template_303_31).
    }
    // Source: vvaharness/orchestrator/batch.py:304-304
    End this invocation with p.
  }
  // Source: vvaharness/orchestrator/batch.py:306-308
  In source order: Evaluate workspace.mkdir(parents=True, exist_ok=True); retain side effects and discard the expression result. Then Evaluate once ''.join((c if c.isalnum() or c in '._-' else '_' for c in dest_name or _module_name_from(ref))); assign in source target order to safe.
  // Source: vvaharness/orchestrator/batch.py:310-313
  if (the source predicate safe in ('.', '..') or not safe.strip('.') is truthy) {
    // Source: vvaharness/orchestrator/batch.py:311-313
    Raise RuntimeError(source_template_312_12).
  }
  // Source: vvaharness/orchestrator/batch.py:314-314
  In source order: Evaluate once workspace / safe; assign in source target order to dest.
  // Source: vvaharness/orchestrator/batch.py:315-328
  if (the source predicate dest.exists() is truthy) {
    // Source: vvaharness/orchestrator/batch.py:316-316
    In source order: Evaluate once any((p for p in dest.iterdir() if p.name != '.git')); assign in source target order to has_content.
    // Source: vvaharness/orchestrator/batch.py:318-320
    if (the source predicate has_content and _stage_dir_bound(dest, ref) is truthy) {
      // Source: vvaharness/orchestrator/batch.py:319-319
      In source order: Evaluate console.write(source_template_319_26); retain side effects and discard the expression result.
      // Source: vvaharness/orchestrator/batch.py:320-320
      End this invocation with dest.
    }
    // Source: vvaharness/orchestrator/batch.py:321-325
    In source order: Evaluate once 'empty' if not has_content else 'unverified (no matching stage marker — stale, foreign, or pre-seeded)'; assign in source target order to reason. Then Evaluate console.write(source_template_324_22); retain side effects and discard the expression result. Then Evaluate _rmtree_rw(dest); retain side effects and discard the expression result.
    // Source: vvaharness/orchestrator/batch.py:326-328
    if (the source predicate dest.exists() is truthy) {
      // Source: vvaharness/orchestrator/batch.py:327-327
      In source order: Evaluate console.write(source_template_327_26); retain side effects and discard the expression result.
      // Source: vvaharness/orchestrator/batch.py:328-328
      End this invocation with dest.
    }
  }
  // Source: vvaharness/orchestrator/batch.py:329-331
  In source order: Evaluate once _with_token(ref, git_token); assign in source target order to clone_url. Then Evaluate console.write(source_template_330_18); retain side effects and discard the expression result. Then Evaluate once {**os.environ, 'GIT_TERMINAL_PROMPT': '0'}; assign in source target order to env.
  // Source: vvaharness/orchestrator/batch.py:333-341
  Perform the following protected operations {
    // Source: vvaharness/orchestrator/batch.py:334-337
    In source order: Evaluate once subprocess.run(['git', '-c', 'core.longpaths=true', 'clone', '--depth', '1', '--', clone_url, str(dest)], capture_output=True, text=True, env=env, timeout=600); assign in source target order to r.
  }
  // Source: vvaharness/orchestrator/batch.py:338-341
  On the first matching source exception subprocess.TimeoutExpired, in handler order {
    // Source: vvaharness/orchestrator/batch.py:339-341
    Raise RuntimeError(source_template_340_12).
  }
  // Source: vvaharness/orchestrator/batch.py:342-348
  if (the source predicate r.returncode != 0 is truthy) {
    // Source: vvaharness/orchestrator/batch.py:343-343
    In source order: Evaluate once r.stderr.strip() or r.stdout.strip(); assign in source target order to err.
    // Source: vvaharness/orchestrator/batch.py:344-345
    if (the source predicate git_token is truthy) {
      // Source: vvaharness/orchestrator/batch.py:345-345
      In source order: Evaluate once err.replace(git_token, '***'); assign in source target order to err.
    }
    // Source: vvaharness/orchestrator/batch.py:347-347
    In source order: Evaluate once _scrub_url_secrets(err); assign in source target order to err.
    // Source: vvaharness/orchestrator/batch.py:348-348
    Raise RuntimeError(source_template_348_27).
  }
  // Source: vvaharness/orchestrator/batch.py:349-349
  In source order: Evaluate _write_stage_marker(dest, ref, 'remote'); retain side effects and discard the expression result.
  // Source: vvaharness/orchestrator/batch.py:350-350
  End this invocation with dest.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/batch.py:353-369
// Source signature: _outcome_status(outcome: ScanOutcome) -> dict[str, object]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _outcome_status(outcome) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/batch.py:354-354
  In source order: Retain source documentation literal source_literal_354_4; it is not a model call.
  // Source: vvaharness/orchestrator/batch.py:355-363
  if (the source predicate outcome.exit_code == 0 is truthy) {
    // Source: vvaharness/orchestrator/batch.py:356-356
    In source order: Evaluate once ('OK', ''); assign in source target order to (status, error).
  }
  else {
    // Source: vvaharness/orchestrator/batch.py:357-363
    if (the source predicate outcome.exit_code == EXIT_NOT_REMEDIATED is truthy) {
      // Source: vvaharness/orchestrator/batch.py:359-360
      In source order: Evaluate once 'NOT_REMEDIATED'; assign in source target order to status. Then Evaluate once 'the scan completed but nothing it remediated validated as fixed'; assign in source target order to error.
    }
    else {
      // Source: vvaharness/orchestrator/batch.py:362-363
      In source order: Evaluate once 'DEGRADED'; assign in source target order to status. Then Evaluate once source_template_363_16; assign in source target order to error.
    }
  }
  // Source: vvaharness/orchestrator/batch.py:364-369
  End this invocation with {'status': status, 'findings': outcome.finding_count, 'report': str(outcome.report_path) if outcome.report_path else '', 'error': error}.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/batch.py:372-377
// Source signature: _split_non_ok(results: list[dict]) -> tuple[list[dict], list[dict]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _split_non_ok(results) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/batch.py:373-376
  In source order: Retain source documentation literal source_literal_373_4; it is not a model call. Then Evaluate once [r for r in results if r['status'] == 'NOT_REMEDIATED']; assign in source target order to unremediated. Then Evaluate once [r for r in results if r['status'] not in ('OK', 'NOT_REMEDIATED')]; assign in source target order to failures.
  // Source: vvaharness/orchestrator/batch.py:377-377
  End this invocation with (unremediated, failures).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/batch.py:380-504
// Source signature: run_batch(list_file: Path, args, cfg) -> int
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn run_batch(list_file, args, cfg) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/batch.py:381-383
  In source order: Evaluate once getattr(cfg, 'batch', None); assign in source target order to batch_cfg. Then Evaluate once getattr(batch_cfg, 'git_token', None) or None; assign in source target order to git_token. Then Evaluate once getattr(batch_cfg, 'git_base_url', None) or None; assign in source target order to git_base.
  // Source: vvaharness/orchestrator/batch.py:384-391
  Perform the following protected operations {
    // Source: vvaharness/orchestrator/batch.py:385-388
    if (the source predicate list_file.suffix.lower() == '.csv' is truthy) {
      // Source: vvaharness/orchestrator/batch.py:386-386
      In source order: Evaluate once _parse_repo_csv(list_file, git_base); assign in source target order to entries.
    }
    else {
      // Source: vvaharness/orchestrator/batch.py:388-388
      In source order: Evaluate once _parse_repo_file(list_file); assign in source target order to entries.
    }
  }
  // Source: vvaharness/orchestrator/batch.py:389-391
  On the first matching source exception ValueError as e, in handler order {
    // Source: vvaharness/orchestrator/batch.py:390-390
    In source order: Evaluate log.error(Event.BATCH_ROW_INVALID, detail=str(e)); retain side effects and discard the expression result.
    // Source: vvaharness/orchestrator/batch.py:391-391
    End this invocation with 2.
  }
  // Source: vvaharness/orchestrator/batch.py:394-395
  In source order: Evaluate once [p.lower() for p in getattr(batch_cfg, 'skip_repo_patterns', None) or []]; assign in source target order to skip_pats.
  // Source: vvaharness/orchestrator/batch.py:396-413
  if (the source predicate skip_pats is truthy) {
    // Source: vvaharness/orchestrator/batch.py:397-397
    In source order: For kept, assign []; source annotation list[dict].
    // Source: vvaharness/orchestrator/batch.py:398-406
    for each e in entries {
      // Source: vvaharness/orchestrator/batch.py:399-401
      In source order: Evaluate once e['repo_name']; assign in source target order to name. Then Evaluate once next((p for p in skip_pats if fnmatch.fnmatch(name.lower(), p)), None); assign in source target order to hit.
      // Source: vvaharness/orchestrator/batch.py:402-406
      if (the source predicate hit is truthy) {
        // Source: vvaharness/orchestrator/batch.py:403-404
        In source order: Evaluate console.write(source_template_403_30); retain side effects and discard the expression result.
      }
      else {
        // Source: vvaharness/orchestrator/batch.py:406-406
        In source order: Evaluate kept.append(e); retain side effects and discard the expression result.
      }
    }
    // Source: vvaharness/orchestrator/batch.py:407-409
    if (the source predicate len(kept) != len(entries) is truthy) {
      // Source: vvaharness/orchestrator/batch.py:408-409
      In source order: Evaluate console.write(source_template_408_26); retain side effects and discard the expression result.
    }
    // Source: vvaharness/orchestrator/batch.py:410-410
    In source order: Evaluate once kept; assign in source target order to entries.
    // Source: vvaharness/orchestrator/batch.py:411-413
    if (the source predicate not entries is truthy) {
      // Source: vvaharness/orchestrator/batch.py:412-412
      In source order: Evaluate log.error(Event.BATCH_ALL_ROWS_SKIPPED, path=list_file); retain side effects and discard the expression result.
      // Source: vvaharness/orchestrator/batch.py:413-413
      End this invocation with 2.
    }
  }
  // Source: vvaharness/orchestrator/batch.py:415-415
  In source order: Evaluate once Path(args.workspace); assign in source target order to workspace.
  // Source: vvaharness/orchestrator/batch.py:417-419
  if (the source predicate getattr(args, 'group_by_app', False) is truthy) {
    // Source: vvaharness/orchestrator/batch.py:418-419
    End this invocation with _run_batch_grouped(entries, workspace, git_token, args, cfg, list_file).
  }
  // Source: vvaharness/orchestrator/batch.py:421-422
  In source order: For results, assign []; source annotation list[dict]. Then Evaluate once time.time(); assign in source target order to batch_t0.
  // Source: vvaharness/orchestrator/batch.py:424-479
  for each (i, entry) in enumerate(entries, 1) {
    // Source: vvaharness/orchestrator/batch.py:425-430
    In source order: Evaluate once entry['ref']; assign in source target order to ref. Then Evaluate once entry['repo_name']; assign in source target order to repo_name. Then Evaluate once entry['application_id']; assign in source target order to app_id. Then Evaluate console.write(source_template_428_22); retain side effects and discard the expression result. Then Evaluate TOKENS.reset(); retain side effects and discard the expression result.
    // Source: vvaharness/orchestrator/batch.py:431-436
    In source order: Evaluate STAGES.reset(); retain side effects and discard the expression result. Then Evaluate COUNTERS.reset(); retain side effects and discard the expression result. Then Evaluate CACHED_PROVENANCE.reset(); retain side effects and discard the expression result. Then Evaluate _reset_quality_counters(); retain side effects and discard the expression result. Then Evaluate _reset_warn_once(); retain side effects and discard the expression result.
    // Source: vvaharness/orchestrator/batch.py:438-441
    In source order: Evaluate _reset_redact_known_values(); retain side effects and discard the expression result. Then Evaluate cli.reset_abort(); retain side effects and discard the expression result. Then Evaluate once time.time(); assign in source target order to t0. Then For cloned, assign None; source annotation Path | None.
    // Source: vvaharness/orchestrator/batch.py:442-479
    Perform the following protected operations {
      // Source: vvaharness/orchestrator/batch.py:443-444
      In source order: Evaluate once _acquire_repo(ref, workspace, git_token, dest_name=repo_name); assign in source target order to local.
      // Source: vvaharness/orchestrator/batch.py:445-446
      if (the source predicate _is_remote(ref) is truthy) {
        // Source: vvaharness/orchestrator/batch.py:446-446
        In source order: Evaluate once local; assign in source target order to cloned.
      }
      // Source: vvaharness/orchestrator/batch.py:447-453
      if (the source predicate args.stop_after == 'clone' is truthy) {
        // Source: vvaharness/orchestrator/batch.py:448-452
        In source order: Evaluate results.append({'ref': ref, 'module': repo_name, 'app_id': app_id, 'status': 'OK', 'findings': 0, 'report': str(local), 'elapsed': time.time() - t0, 'error': ''}); retain side effects and discard the expression result.
        // Source: vvaharness/orchestrator/batch.py:453-453
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/orchestrator/batch.py:454-460
      In source order: Evaluate once scan_repo(local, repo_name, app_id, args, cfg, path_prefix=repo_name); assign in source target order to outcome. Then Evaluate results.append({'ref': ref, 'module': repo_name, 'app_id': app_id, **_outcome_status(outcome), 'elapsed': time.time() - t0}); retain side effects and discard the expression result.
    }
    // Source: vvaharness/orchestrator/batch.py:461-466
    On the first matching source exception KeyboardInterrupt, in handler order {
      // Source: vvaharness/orchestrator/batch.py:462-465
      In source order: Evaluate results.append({'ref': ref, 'module': repo_name, 'app_id': app_id, 'status': 'ABORTED', 'findings': 0, 'report': '', 'elapsed': time.time() - t0, 'error': 'interrupted by user'}); retain side effects and discard the expression result.
      // Source: vvaharness/orchestrator/batch.py:466-466
      Raise the currently handled exception.
    }
    // Source: vvaharness/orchestrator/batch.py:467-469
    On the first matching source exception (AuthenticationError, ProxyError, _store.StoreError), in handler order {
      // Source: vvaharness/orchestrator/batch.py:469-469
      Raise the currently handled exception.
    }
    // Source: vvaharness/orchestrator/batch.py:470-476
    On the first matching source exception Exception as e, in handler order {
      // Source: vvaharness/orchestrator/batch.py:472-476
      In source order: Evaluate traceback.print_exc(file=sys.stderr); retain side effects and discard the expression result. Then Evaluate _errlog.log('batch', repo_name, e, app_id=app_id, ref=ref); retain side effects and discard the expression result. Then Evaluate results.append({'ref': ref, 'module': repo_name, 'app_id': app_id, 'status': 'FAILED', 'findings': 0, 'report': '', 'elapsed': time.time() - t0, 'error': str(e)[:500]}); retain side effects and discard the expression result.
    }
    On every exit from this protected/handler/normal-completion region {
      // Source: vvaharness/orchestrator/batch.py:478-479
      if (the source predicate cloned and (not args.keep_clones) and (args.stop_after != 'clone') is truthy) {
        // Source: vvaharness/orchestrator/batch.py:479-479
        In source order: Evaluate _purge_clone(cloned, _preserve_set(cfg)); retain side effects and discard the expression result.
      }
    }
  }
  // Source: vvaharness/orchestrator/batch.py:481-488
  In source order: Evaluate once workspace / 'batch_summary.md'; assign in source target order to summary_path. Then Evaluate workspace.mkdir(parents=True, exist_ok=True); retain side effects and discard the expression result. Then Evaluate summary_path.write_text(_render_batch_summary(results, list_file, time.time() - batch_t0), encoding='utf-8'); retain side effects and discard the expression result. Then Evaluate console.write(source_template_486_18); retain side effects and discard the expression result. Then Evaluate once _split_non_ok(results); assign in source target order to (unremediated, failed).
  // Source: vvaharness/orchestrator/batch.py:489-491
  if (the source predicate not (unremediated or failed) is truthy) {
    // Source: vvaharness/orchestrator/batch.py:490-490
    In source order: Evaluate console.write(source_template_490_22); retain side effects and discard the expression result.
    // Source: vvaharness/orchestrator/batch.py:491-491
    End this invocation with 0.
  }
  // Source: vvaharness/orchestrator/batch.py:492-496
  if (the source predicate unremediated is truthy) {
    // Source: vvaharness/orchestrator/batch.py:493-494
    In source order: Evaluate console.write(source_template_493_22); retain side effects and discard the expression result.
    // Source: vvaharness/orchestrator/batch.py:495-496
    for each r in unremediated {
      // Source: vvaharness/orchestrator/batch.py:496-496
      In source order: Evaluate console.write(source_template_496_26); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/orchestrator/batch.py:497-503
  if (the source predicate failed is truthy) {
    // Source: vvaharness/orchestrator/batch.py:498-498
    In source order: Evaluate console.write(source_template_498_22); retain side effects and discard the expression result.
    // Source: vvaharness/orchestrator/batch.py:499-501
    for each r in failed {
      // Source: vvaharness/orchestrator/batch.py:500-501
      In source order: Evaluate console.write(source_template_500_26); retain side effects and discard the expression result.
    }
    // Source: vvaharness/orchestrator/batch.py:503-503
    End this invocation with 1.
  }
  // Source: vvaharness/orchestrator/batch.py:504-504
  End this invocation with EXIT_NOT_REMEDIATED.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/batch.py:507-532
// Source signature: _stage_repo(ref: str, app_dir: Path, slug: str, git_token: str | None) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _stage_repo(ref, app_dir, slug, git_token) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/batch.py:508-508
  In source order: Retain source documentation literal source_literal_508_4; it is not a model call.
  // Source: vvaharness/orchestrator/batch.py:509-511
  if (the source predicate _is_remote(ref) is truthy) {
    // Source: vvaharness/orchestrator/batch.py:510-510
    In source order: Evaluate _acquire_repo(ref, app_dir, git_token, dest_name=slug); retain side effects and discard the expression result.
    // Source: vvaharness/orchestrator/batch.py:511-511
    End this invocation with None.
  }
  // Source: vvaharness/orchestrator/batch.py:512-512
  In source order: Evaluate once Path(ref); assign in source target order to src.
  // Source: vvaharness/orchestrator/batch.py:513-514
  if (the source predicate not src.is_dir() is truthy) {
    // Source: vvaharness/orchestrator/batch.py:514-514
    Raise RuntimeError(source_template_514_27).
  }
  // Source: vvaharness/orchestrator/batch.py:515-515
  In source order: Evaluate once app_dir / slug; assign in source target order to dest.
  // Source: vvaharness/orchestrator/batch.py:516-526
  if (the source predicate dest.exists() is truthy) {
    // Source: vvaharness/orchestrator/batch.py:518-520
    if (the source predicate _stage_dir_bound(dest, ref) is truthy) {
      // Source: vvaharness/orchestrator/batch.py:519-519
      In source order: Evaluate console.write(source_template_519_26); retain side effects and discard the expression result.
      // Source: vvaharness/orchestrator/batch.py:520-520
      End this invocation with None.
    }
    // Source: vvaharness/orchestrator/batch.py:521-523
    In source order: Evaluate console.write(source_template_521_22); retain side effects and discard the expression result. Then Evaluate _rmtree_rw(dest); retain side effects and discard the expression result.
    // Source: vvaharness/orchestrator/batch.py:524-526
    if (the source predicate dest.exists() is truthy) {
      // Source: vvaharness/orchestrator/batch.py:525-525
      In source order: Evaluate console.write(source_template_525_26); retain side effects and discard the expression result.
      // Source: vvaharness/orchestrator/batch.py:526-526
      End this invocation with None.
    }
  }
  // Source: vvaharness/orchestrator/batch.py:527-532
  In source order: Evaluate app_dir.mkdir(parents=True, exist_ok=True); retain side effects and discard the expression result. Then Evaluate console.write(source_template_528_18); retain side effects and discard the expression result. Then Evaluate shutil.copytree(src, dest, symlinks=True, ignore=shutil.ignore_patterns('.git')); retain side effects and discard the expression result. Then Evaluate _write_stage_marker(dest, ref, 'local'); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/batch.py:535-542
// Source signature: _app_module_name(app_id: str, repos: list[dict]) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _app_module_name(app_id, repos) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/batch.py:536-536
  In source order: Evaluate once _load_app_profile(app_id); assign in source target order to (profile, _).
  // Source: vvaharness/orchestrator/batch.py:537-539
  if (the source predicate profile and profile.name is truthy) {
    // Source: vvaharness/orchestrator/batch.py:538-538
    In source order: Evaluate once ''.join((c if c.isalnum() or c in '._-' else '_' for c in profile.name)); assign in source target order to safe.
    // Source: vvaharness/orchestrator/batch.py:539-539
    End this invocation with safe or source_template_539_23.
  }
  // Source: vvaharness/orchestrator/batch.py:540-541
  if (the source predicate len(repos) == 1 is truthy) {
    // Source: vvaharness/orchestrator/batch.py:541-541
    End this invocation with _module_name_from(repos[0]['repo_name']).
  }
  // Source: vvaharness/orchestrator/batch.py:542-542
  End this invocation with source_template_542_11.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/batch.py:545-647
// Source signature: _run_batch_grouped(entries: list[dict], workspace: Path, git_token: str | None, args, cfg, list_file: Path) -> int
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _run_batch_grouped(entries, workspace, git_token, args, cfg, list_file) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/batch.py:548-549
  In source order: Resolve source import from collections import defaultdict; preserve alias and import-time effects. Then For groups, assign defaultdict(list); source annotation dict[str, list[dict]].
  // Source: vvaharness/orchestrator/batch.py:550-551
  for each e in entries {
    // Source: vvaharness/orchestrator/batch.py:551-551
    In source order: Evaluate groups[e['application_id']].append(e); retain side effects and discard the expression result.
  }
  // Source: vvaharness/orchestrator/batch.py:553-554
  In source order: For results, assign []; source annotation list[dict]. Then Evaluate once time.time(); assign in source target order to batch_t0.
  // Source: vvaharness/orchestrator/batch.py:556-624
  for each (n, (app_id, repos)) in enumerate(sorted(groups.items()), 1) {
    // Source: vvaharness/orchestrator/batch.py:558-565
    In source order: Evaluate once ''.join((c if c.isalnum() or c in '._-' else '_' for c in str(app_id))).strip('.') or 'app'; assign in source target order to safe_app. Then Evaluate once workspace / safe_app; assign in source target order to app_dir. Then Evaluate once _assign_slugs(repos); assign in source target order to slugs. Then Evaluate console.write(source_template_562_22); retain side effects and discard the expression result. Then Evaluate TOKENS.reset(); retain side effects and discard the expression result.
    // Source: vvaharness/orchestrator/batch.py:566-570
    In source order: Evaluate STAGES.reset(); retain side effects and discard the expression result. Then Evaluate COUNTERS.reset(); retain side effects and discard the expression result. Then Evaluate CACHED_PROVENANCE.reset(); retain side effects and discard the expression result. Then Evaluate _reset_quality_counters(); retain side effects and discard the expression result. Then Evaluate _reset_warn_once(); retain side effects and discard the expression result.
    // Source: vvaharness/orchestrator/batch.py:571-573
    In source order: Evaluate _reset_redact_known_values(); retain side effects and discard the expression result. Then Evaluate cli.reset_abort(); retain side effects and discard the expression result. Then Evaluate once time.time(); assign in source target order to t0.
    // Source: vvaharness/orchestrator/batch.py:574-624
    Perform the following protected operations {
      // Source: vvaharness/orchestrator/batch.py:575-575
      In source order: For staged, assign []; source annotation list[str].
      // Source: vvaharness/orchestrator/batch.py:576-584
      for each (r, slug) in zip(repos, slugs) {
        // Source: vvaharness/orchestrator/batch.py:577-584
        Perform the following protected operations {
          // Source: vvaharness/orchestrator/batch.py:578-579
          In source order: Evaluate _stage_repo(r['ref'], app_dir, slug, git_token); retain side effects and discard the expression result. Then Evaluate staged.append(slug); retain side effects and discard the expression result.
        }
        // Source: vvaharness/orchestrator/batch.py:580-581
        On the first matching source exception _store.StoreError, in handler order {
          // Source: vvaharness/orchestrator/batch.py:581-581
          Raise the currently handled exception.
        }
        // Source: vvaharness/orchestrator/batch.py:582-584
        On the first matching source exception Exception as ce, in handler order {
          // Source: vvaharness/orchestrator/batch.py:583-584
          In source order: Evaluate log.warning(Event.BATCH_REPO_SKIPPED, repo=slug, detail=str(ce)); retain side effects and discard the expression result. Then Evaluate _errlog.log('batch.clone', slug, ce, app_id=app_id); retain side effects and discard the expression result.
        }
      }
      // Source: vvaharness/orchestrator/batch.py:585-587
      if (the source predicate not staged is truthy) {
        // Source: vvaharness/orchestrator/batch.py:586-587
        Raise RuntimeError(source_template_587_20).
      }
      // Source: vvaharness/orchestrator/batch.py:588-590
      if (the source predicate len(staged) < len(repos) is truthy) {
        // Source: vvaharness/orchestrator/batch.py:589-590
        In source order: Evaluate console.write(source_template_589_30); retain side effects and discard the expression result.
      }
      // Source: vvaharness/orchestrator/batch.py:591-591
      In source order: Evaluate once _app_module_name(app_id, repos); assign in source target order to module.
      // Source: vvaharness/orchestrator/batch.py:592-599
      if (the source predicate args.stop_after == 'clone' is truthy) {
        // Source: vvaharness/orchestrator/batch.py:593-598
        In source order: Evaluate results.append({'ref': source_template_594_27, 'module': module, 'app_id': app_id, 'status': 'OK', 'findings': 0, 'report': str(app_dir), 'elapsed': time.time() - t0, 'error': ''}); retain side effects and discard the expression result.
        // Source: vvaharness/orchestrator/batch.py:599-599
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/orchestrator/batch.py:600-605
      In source order: Evaluate once scan_repo(app_dir, module, app_id, args, cfg); assign in source target order to outcome. Then Evaluate results.append({'ref': source_template_602_23, 'module': module, 'app_id': app_id, **_outcome_status(outcome), 'elapsed': time.time() - t0}); retain side effects and discard the expression result.
    }
    // Source: vvaharness/orchestrator/batch.py:606-611
    On the first matching source exception KeyboardInterrupt, in handler order {
      // Source: vvaharness/orchestrator/batch.py:607-610
      In source order: Evaluate results.append({'ref': source_template_607_35, 'module': str(app_id), 'app_id': app_id, 'status': 'ABORTED', 'findings': 0, 'report': '', 'elapsed': time.time() - t0, 'error': 'interrupted by user'}); retain side effects and discard the expression result.
      // Source: vvaharness/orchestrator/batch.py:611-611
      Raise the currently handled exception.
    }
    // Source: vvaharness/orchestrator/batch.py:612-614
    On the first matching source exception (AuthenticationError, ProxyError, _store.StoreError), in handler order {
      // Source: vvaharness/orchestrator/batch.py:614-614
      Raise the currently handled exception.
    }
    // Source: vvaharness/orchestrator/batch.py:615-621
    On the first matching source exception Exception as e, in handler order {
      // Source: vvaharness/orchestrator/batch.py:616-621
      In source order: Evaluate traceback.print_exc(file=sys.stderr); retain side effects and discard the expression result. Then Evaluate _errlog.log('batch', source_template_617_33, e, app_id=app_id); retain side effects and discard the expression result. Then Evaluate results.append({'ref': source_template_618_35, 'module': str(app_id), 'app_id': app_id, 'status': 'FAILED', 'findings': 0, 'report': '', 'elapsed': time.time() - t0, 'error': str(e)[:500]}); retain side effects and discard the expression result.
    }
    On every exit from this protected/handler/normal-completion region {
      // Source: vvaharness/orchestrator/batch.py:623-624
      if (the source predicate not args.keep_clones and args.stop_after != 'clone' is truthy) {
        // Source: vvaharness/orchestrator/batch.py:624-624
        In source order: Evaluate _purge_clone(app_dir, _preserve_set(cfg)); retain side effects and discard the expression result.
      }
    }
  }
  // Source: vvaharness/orchestrator/batch.py:626-633
  In source order: Evaluate once workspace / 'batch_summary.md'; assign in source target order to summary_path. Then Evaluate workspace.mkdir(parents=True, exist_ok=True); retain side effects and discard the expression result. Then Evaluate summary_path.write_text(_render_batch_summary(results, list_file, time.time() - batch_t0), encoding='utf-8'); retain side effects and discard the expression result. Then Evaluate console.write(source_template_631_18); retain side effects and discard the expression result. Then Evaluate once _split_non_ok(results); assign in source target order to (unremediated, failed).
  // Source: vvaharness/orchestrator/batch.py:634-636
  if (the source predicate not (unremediated or failed) is truthy) {
    // Source: vvaharness/orchestrator/batch.py:635-635
    In source order: Evaluate console.write(source_template_635_22); retain side effects and discard the expression result.
    // Source: vvaharness/orchestrator/batch.py:636-636
    End this invocation with 0.
  }
  // Source: vvaharness/orchestrator/batch.py:637-641
  if (the source predicate unremediated is truthy) {
    // Source: vvaharness/orchestrator/batch.py:638-639
    In source order: Evaluate console.write(source_template_638_22); retain side effects and discard the expression result.
    // Source: vvaharness/orchestrator/batch.py:640-641
    for each r in unremediated {
      // Source: vvaharness/orchestrator/batch.py:641-641
      In source order: Evaluate console.write(source_template_641_26); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/orchestrator/batch.py:642-646
  if (the source predicate failed is truthy) {
    // Source: vvaharness/orchestrator/batch.py:643-643
    In source order: Evaluate console.write(source_template_643_22); retain side effects and discard the expression result.
    // Source: vvaharness/orchestrator/batch.py:644-645
    for each r in failed {
      // Source: vvaharness/orchestrator/batch.py:645-645
      In source order: Evaluate console.write(source_template_645_26); retain side effects and discard the expression result.
    }
    // Source: vvaharness/orchestrator/batch.py:646-646
    End this invocation with 1.
  }
  // Source: vvaharness/orchestrator/batch.py:647-647
  End this invocation with EXIT_NOT_REMEDIATED.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/batch.py:650-693
// Source signature: _render_batch_summary(results: list[dict], list_file: Path, elapsed: float) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _render_batch_summary(results, list_file, elapsed) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/batch.py:651-654
  In source order: Evaluate once sum((1 for r in results if r['status'] == 'OK')); assign in source target order to ok. Then Evaluate once _split_non_ok(results); assign in source target order to (unremediated, failed). Then Evaluate once source_template_654_13; assign in source target order to counts.
  // Source: vvaharness/orchestrator/batch.py:655-656
  if (the source predicate unremediated is truthy) {
    // Source: vvaharness/orchestrator/batch.py:656-656
    In source order: Apply source augmented assignment counts += source_template_656_18 with source evaluation/in-place semantics.
  }
  // Source: vvaharness/orchestrator/batch.py:657-667
  In source order: Apply source augmented assignment counts += source_template_657_14 with source evaluation/in-place semantics. Then Evaluate once ['# Agentic SAST batch summary', '', source_template_661_8, source_template_662_8, source_template_663_8, '', '| # | App ID | Repo | Status | Findings | Elapsed (s) | Report | Source |', '|--:|---|---|---|--:|--:|---|---|']; assign in source target order to out.
  // Source: vvaharness/orchestrator/batch.py:668-675
  for each (i, r) in enumerate(results, 1) {
    // Source: vvaharness/orchestrator/batch.py:670-675
    In source order: Evaluate once source_template_670_15 if r['report'] else ''; assign in source target order to rep. Then Evaluate once _md_cell(_scrub_url_secrets(r['ref'])); assign in source target order to src. Then Evaluate out.append(source_template_673_19); retain side effects and discard the expression result.
  }
  // Source: vvaharness/orchestrator/batch.py:677-685
  if (the source predicate unremediated is truthy) {
    // Source: vvaharness/orchestrator/batch.py:678-680
    In source order: Evaluate out.extend(['', '## Not remediated', '', 'These scans ran to completion. Nothing they remediated validated as fixed.', '']); retain side effects and discard the expression result.
    // Source: vvaharness/orchestrator/batch.py:681-685
    for each r in unremediated {
      // Source: vvaharness/orchestrator/batch.py:682-685
      In source order: Evaluate out.extend([source_template_682_24, source_template_683_24, '']); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/orchestrator/batch.py:686-692
  if (the source predicate failed is truthy) {
    // Source: vvaharness/orchestrator/batch.py:687-687
    In source order: Evaluate out.extend(['', '## Failures', '']); retain side effects and discard the expression result.
    // Source: vvaharness/orchestrator/batch.py:688-692
    for each r in failed {
      // Source: vvaharness/orchestrator/batch.py:689-692
      In source order: Evaluate out.extend([source_template_689_24, source_template_690_24, source_template_692_24, '']); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/orchestrator/batch.py:693-693
  End this invocation with source_literal_693_11.join(out) + source_literal_693_28.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.util import logs` at source line 15: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import logs` at source line 15: `source_detail/vvaharness/util/logs.py.sudo.md`.
- `from vvaharness.backends.harness.models import AuthenticationError, ProxyError` at source line 31: `source_detail/vvaharness/backends/harness/models.py.sudo.md`.
- `from vvaharness.backends.llm import cli` at source line 32: `source_detail/vvaharness/backends/llm/__init__.py.sudo.md`.
- `from vvaharness.backends.llm import cli` at source line 32: `source_detail/vvaharness/backends/llm/cli/__init__.py.sudo.md`.
- `from vvaharness.models import _md_cell` at source line 35: `source_detail/vvaharness/models/__init__.py.sudo.md`.
- `from vvaharness.orchestrator import store as _store` at source line 36: `source_detail/vvaharness/orchestrator/__init__.py.sudo.md`.
- `from vvaharness.orchestrator import store as _store` at source line 36: `source_detail/vvaharness/orchestrator/store/__init__.py.sudo.md`.
- `from vvaharness.orchestrator.case_rollup import EXIT_NOT_REMEDIATED` at source line 37: `source_detail/vvaharness/orchestrator/case_rollup.py.sudo.md`.
- `from vvaharness.orchestrator.cleanup import _preserve_set, _purge_clone, _rmtree_rw` at source line 38: `source_detail/vvaharness/orchestrator/cleanup.py.sudo.md`.
- `from vvaharness.orchestrator.cmdb import _load_app_profile` at source line 39: `source_detail/vvaharness/orchestrator/cmdb.py.sudo.md`.
- `from vvaharness.orchestrator.scan import ScanOutcome, scan_repo` at source line 40: `source_detail/vvaharness/orchestrator/scan.py.sudo.md`.
- `from vvaharness.report.redact import reset_known_values as _reset_redact_known_values` at source line 41: `source_detail/vvaharness/report/redact.py.sudo.md`.
- `from vvaharness.util import console` at source line 42: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import console` at source line 42: `source_detail/vvaharness/util/console.py.sudo.md`.
- `from vvaharness.util import errlog as _errlog` at source line 43: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import errlog as _errlog` at source line 43: `source_detail/vvaharness/util/errlog.py.sudo.md`.
- `from vvaharness.util.counters import COUNTERS` at source line 44: `source_detail/vvaharness/util/counters.py.sudo.md`.
- `from vvaharness.util.events import Event` at source line 45: `source_detail/vvaharness/util/events.py.sudo.md`.
- `from vvaharness.util.response_quality import reset_counters as _reset_quality_counters` at source line 46: `source_detail/vvaharness/util/response_quality.py.sudo.md`.
- `from vvaharness.util.stage_telemetry import CACHED_PROVENANCE, STAGES` at source line 47: `source_detail/vvaharness/util/stage_telemetry.py.sudo.md`.
- `from vvaharness.util.tokens import TOKENS` at source line 48: `source_detail/vvaharness/util/tokens.py.sudo.md`.
- `from vvaharness.util.warn_once import reset_warn_once_registries as _reset_warn_once` at source line 49: `source_detail/vvaharness/util/warn_once.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../prompt_representation/vvaharness/orchestrator/batch.py.sudo.md). Exact strings in the evidence asset support this conversion.
