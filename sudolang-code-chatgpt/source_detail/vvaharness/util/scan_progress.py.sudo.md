# vvaharness/util/scan_progress.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/util/scan_progress.py.evidence.json`. SHA-256: `16b4988812168892d087f6ce642912a5aa168a0266d660c9769fcf1a6bb6741e`.

```sudo
// Source: vvaharness/util/scan_progress.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import atexit; preserve alias and import-time effects. Then Resolve source import import os; preserve alias and import-time effects. Then Resolve source import import threading; preserve alias and import-time effects.
// Source: vvaharness/util/scan_progress.py:22-28
In source order: Resolve source import import time; preserve alias and import-time effects. Then Resolve source import from dataclasses import dataclass, field; preserve alias and import-time effects. Then Resolve source import from typing import Literal; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import console; preserve alias and import-time effects. Then Evaluate once Literal['compact', 'verbose', 'summary_only', 'stage_only', 'llm_debug', 'live']; assign in source target order to Style.
// Source: vvaharness/util/scan_progress.py:30-50
In source order: For _STYLES, assign ('compact', 'verbose', 'summary_only', 'stage_only', 'llm_debug', 'live'); source annotation tuple[str, ...]. Then For _STAGE_LABELS, assign {'s0': 'static seed', 's1': 'pre-process', 's2': 'threat model', 's3': 'decompose', 's4': 'deep dive', 's5': 'detectors', 's6': 'verify', 's7': 'dedup', 's8': 'chain', 's9': 'report', 's10': 'remediate'}; source annotation dict[str, str]. Then Evaluate once 8; assign in source target order to _LIVE_REFRESH_HZ. Then For _OUTCOME_GLYPH, assign {'completed': '✓', 'completed_with_errors': '⚠', 'error': '✗', 'cached': '⤼', 'skipped': '–'}; source annotation dict[str, str]. Then For _OUTCOME_STYLE, assign {'completed': 'ok', 'completed_with_errors': 'warn', 'error': 'fail', 'cached': 'muted', 'skipped': 'muted'}; source annotation dict[str, str].
// Source: vvaharness/util/scan_progress.py:53-57
// Source signature: _clock(seconds: float) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _clock(seconds) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/scan_progress.py:54-54
  In source order: Retain source documentation literal source_literal_54_4; it is not a model call.
  // Source: vvaharness/util/scan_progress.py:55-56
  if (the source predicate seconds < 60 is truthy) {
    // Source: vvaharness/util/scan_progress.py:56-56
    End this invocation with source_template_56_15.
  }
  // Source: vvaharness/util/scan_progress.py:57-57
  End this invocation with source_template_57_11.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/scan_progress.py:59-63
In source order: Evaluate once ('s0', 's1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 's10'); assign in source target order to _STAGE_ORDER. Then For _ACTIVE_TRACKER, assign None; source annotation ScanProgress | None.
// Source: vvaharness/util/scan_progress.py:66-71
// Source signature: _stderr_is_a_terminal() -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _stderr_is_a_terminal() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/scan_progress.py:67-70
  In source order: Retain source documentation literal source_literal_67_4; it is not a model call. Then Resolve source import import sys; preserve alias and import-time effects. Then Evaluate once getattr(sys.stderr, 'isatty', None); assign in source target order to isatty.
  // Source: vvaharness/util/scan_progress.py:71-71
  End this invocation with bool(callable(isatty) and isatty()).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/scan_progress.py:74-77
// Source signature: set_active_tracker(tracker: ScanProgress | None) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn set_active_tracker(tracker) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/scan_progress.py:75-77
  In source order: Retain source documentation literal source_literal_75_4; it is not a model call. Then Bind names in module scope: _ACTIVE_TRACKER. Then Evaluate once tracker; assign in source target order to _ACTIVE_TRACKER.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/scan_progress.py:80-82
// Source signature: get_active_tracker() -> ScanProgress | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn get_active_tracker() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/scan_progress.py:81-81
  In source order: Retain source documentation literal source_literal_81_4; it is not a model call.
  // Source: vvaharness/util/scan_progress.py:82-82
  End this invocation with _ACTIVE_TRACKER.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/scan_progress.py:85-88
// Source signature: is_stage_only() -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn is_stage_only() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/scan_progress.py:86-87
  In source order: Retain source documentation literal source_literal_86_4; it is not a model call. Then Evaluate once get_active_tracker(); assign in source target order to tracker.
  // Source: vvaharness/util/scan_progress.py:88-88
  End this invocation with bool(tracker and tracker.enabled and (tracker.style == 'stage_only')).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/scan_progress.py:92-102
// Source: vvaharness/util/scan_progress.py:91-91
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass.
// Source: vvaharness/util/scan_progress.py:92-102
interface UnitProgress {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/util/scan_progress.py:93-97
  In source order: For unit_id, declare without assigning a value; source annotation str. Then For files, declare without assigning a value; source annotation list[str]. Then For rank, declare without assigning a value; source annotation int. Then For lens, declare without assigning a value; source annotation str. Then For threat, declare without assigning a value; source annotation str.
  // Source: vvaharness/util/scan_progress.py:98-102
  In source order: For state, assign 'queued'; source annotation Literal['queued', 'scanning', 'scanned']. Then For outcome, assign None; source annotation str | None. Then For findings, assign 0; source annotation int. Then For started_at, assign field(default_factory=time.monotonic); source annotation float. Then For elapsed, assign 0.0; source annotation float.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vvaharness/util/scan_progress.py:105-469
interface ScanProgress {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/util/scan_progress.py:106-106
  In source order: Retain source documentation literal source_literal_106_4; it is not a model call.
  // Source: vvaharness/util/scan_progress.py:108-128
  // Source signature: __init__(self, *, enabled: bool=False, style: Style='compact', repo_name: str='')
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self, enabled, style, repo_name) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/util/scan_progress.py:111-113
    In source order: Evaluate once enabled; assign in source target order to self.enabled. Then Evaluate once style; assign in source target order to self.style. Then Evaluate once repo_name; assign in source target order to self.repo_name.
    // Source: vvaharness/util/scan_progress.py:114-119
    Perform the following protected operations {
      // Source: vvaharness/util/scan_progress.py:115-117
      In source order: Evaluate once int(os.environ.get('VVAHARNESS_SCAN_PROGRESS_LLM_MAX_CHARS', '12000')); assign in source target order to self._llm_max_chars.
    }
    // Source: vvaharness/util/scan_progress.py:118-119
    On the first matching source exception ValueError, in handler order {
      // Source: vvaharness/util/scan_progress.py:119-119
      In source order: Evaluate once 12000; assign in source target order to self._llm_max_chars.
    }
    // Source: vvaharness/util/scan_progress.py:120-124
    In source order: Evaluate once threading.Lock(); assign in source target order to self._lock. Then For self._total_files, assign 0; source annotation int. Then For self._units, assign {}; source annotation dict[str, UnitProgress]. Then For self._stages, assign {}; source annotation dict[str, dict[str, float | str]]. Then For self._n_scanning, assign 0; source annotation int.
    // Source: vvaharness/util/scan_progress.py:125-128
    In source order: For self._n_scanned, assign 0; source annotation int. Then For self._start, assign time.monotonic(); source annotation float. Then For self._live, assign None; source annotation object | None. Then For self._findings, assign 0; source annotation int.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/util/scan_progress.py:132-144
  // Source: vvaharness/util/scan_progress.py:131-131
  Before creating this callable, evaluate and retain decorators top-to-bottom: classmethod.
  // Source: vvaharness/util/scan_progress.py:132-144
  // Source signature: from_cfg(cls, cfg, repo_name: str='') -> ScanProgress
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn from_cfg(cls, cfg, repo_name) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/util/scan_progress.py:133-136
    In source order: Retain source documentation literal source_literal_133_8; it is not a model call. Then Evaluate once getattr(cfg, 'scan_progress', None); assign in source target order to sp. Then Evaluate once bool(getattr(sp, 'enabled', False)) if sp else False; assign in source target order to enabled. Then Evaluate once os.environ.get('VVAHARNESS_SCAN_PROGRESS_ENABLED', '').lower(); assign in source target order to env_enabled.
    // Source: vvaharness/util/scan_progress.py:137-138
    if (the source predicate env_enabled in ('1', 'true', 'yes') is truthy) {
      // Source: vvaharness/util/scan_progress.py:138-138
      In source order: Evaluate once True; assign in source target order to enabled.
    }
    // Source: vvaharness/util/scan_progress.py:139-139
    In source order: For style, assign str(getattr(sp, 'style', 'compact')) if sp else 'compact'; source annotation Style.
    // Source: vvaharness/util/scan_progress.py:140-141
    if (the source predicate style not in _STYLES is truthy) {
      // Source: vvaharness/util/scan_progress.py:141-141
      In source order: Evaluate once 'compact'; assign in source target order to style.
    }
    // Source: vvaharness/util/scan_progress.py:142-143
    if (the source predicate style == 'live' and (not _stderr_is_a_terminal()) is truthy) {
      // Source: vvaharness/util/scan_progress.py:143-143
      In source order: Evaluate once 'compact'; assign in source target order to style.
    }
    // Source: vvaharness/util/scan_progress.py:144-144
    End this invocation with cls(enabled=enabled, style=style, repo_name=repo_name).
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vvaharness/util/scan_progress.py:147-163
  // Source signature: stage_started(self, stage_id: str, label: str='') -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn stage_started(self, stage_id, label) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/util/scan_progress.py:148-148
    In source order: Retain source documentation literal source_literal_148_8; it is not a model call.
    // Source: vvaharness/util/scan_progress.py:149-150
    if (the source predicate not self.enabled is truthy) {
      // Source: vvaharness/util/scan_progress.py:150-150
      End this invocation with None.
    }
    // Source: vvaharness/util/scan_progress.py:151-151
    In source order: Evaluate self.start_live(); retain side effects and discard the expression result.
    // Source: vvaharness/util/scan_progress.py:152-163
    Enter source context managers left-to-right: self._lock {
      // Source: vvaharness/util/scan_progress.py:153-155
      In source order: Evaluate once {'state': 'started', 'start': time.monotonic(), 'label': label}; assign in source target order to self._stages[stage_id].
      // Source: vvaharness/util/scan_progress.py:156-157
      if (the source predicate self.style == 'summary_only' is truthy) {
        // Source: vvaharness/util/scan_progress.py:157-157
        End this invocation with None.
      }
      // Source: vvaharness/util/scan_progress.py:158-158
      In source order: Evaluate once source_template_158_20 if label else ''; assign in source target order to extra.
      // Source: vvaharness/util/scan_progress.py:159-163
      if (the source predicate self.style == 'stage_only' is truthy) {
        // Source: vvaharness/util/scan_progress.py:160-161
        In source order: Evaluate self._emit(source_template_160_27); retain side effects and discard the expression result.
      }
      else {
        // Source: vvaharness/util/scan_progress.py:163-163
        In source order: Evaluate self._emit(source_template_163_27); retain side effects and discard the expression result.
      }
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/util/scan_progress.py:165-187
  // Source signature: stage_done(self, stage_id: str, *, outcome: str='completed', detail: str='') -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn stage_done(self, stage_id, outcome, detail) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/util/scan_progress.py:167-167
    In source order: Retain source documentation literal source_literal_167_8; it is not a model call.
    // Source: vvaharness/util/scan_progress.py:168-169
    if (the source predicate not self.enabled is truthy) {
      // Source: vvaharness/util/scan_progress.py:169-169
      End this invocation with None.
    }
    // Source: vvaharness/util/scan_progress.py:170-187
    Enter source context managers left-to-right: self._lock {
      // Source: vvaharness/util/scan_progress.py:171-175
      In source order: Evaluate once self._stages.get(stage_id, {'start': time.monotonic()}); assign in source target order to rec. Then Evaluate once max(0.0, time.monotonic() - float(rec.get('start', time.monotonic()))); assign in source target order to elapsed. Then Evaluate once outcome; assign in source target order to rec['state']. Then Evaluate once elapsed; assign in source target order to rec['elapsed']. Then Evaluate once rec; assign in source target order to self._stages[stage_id].
      // Source: vvaharness/util/scan_progress.py:176-177
      if (the source predicate self.style == 'summary_only' is truthy) {
        // Source: vvaharness/util/scan_progress.py:177-177
        End this invocation with None.
      }
      // Source: vvaharness/util/scan_progress.py:178-183
      if (the source predicate self.style == 'stage_only' is truthy) {
        // Source: vvaharness/util/scan_progress.py:179-182
        In source order: Evaluate self._emit(source_template_179_27); retain side effects and discard the expression result. Then Evaluate self._emit(''); retain side effects and discard the expression result.
        // Source: vvaharness/util/scan_progress.py:183-183
        End this invocation with None.
      }
      // Source: vvaharness/util/scan_progress.py:184-184
      In source order: Evaluate once source_template_184_18; assign in source target order to msg.
      // Source: vvaharness/util/scan_progress.py:185-186
      if (the source predicate detail is truthy) {
        // Source: vvaharness/util/scan_progress.py:186-186
        In source order: Apply source augmented assignment msg += source_template_186_23 with source evaluation/in-place semantics.
      }
      // Source: vvaharness/util/scan_progress.py:187-187
      In source order: Evaluate self._emit(msg); retain side effects and discard the expression result.
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/util/scan_progress.py:189-196
  // Source signature: stage_note(self, stage_id: str, detail: str) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn stage_note(self, stage_id, detail) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/util/scan_progress.py:190-190
    In source order: Retain source documentation literal source_literal_190_8; it is not a model call.
    // Source: vvaharness/util/scan_progress.py:191-192
    if (the source predicate not self.enabled or not detail is truthy) {
      // Source: vvaharness/util/scan_progress.py:192-192
      End this invocation with None.
    }
    // Source: vvaharness/util/scan_progress.py:193-196
    Enter source context managers left-to-right: self._lock {
      // Source: vvaharness/util/scan_progress.py:194-195
      if (the source predicate self.style in ('summary_only', 'stage_only') is truthy) {
        // Source: vvaharness/util/scan_progress.py:195-195
        End this invocation with None.
      }
      // Source: vvaharness/util/scan_progress.py:196-196
      In source order: Evaluate self._emit(source_template_196_23); retain side effects and discard the expression result.
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/util/scan_progress.py:198-209
  // Source signature: discovered(self, all_files: list[str]) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn discovered(self, all_files) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/util/scan_progress.py:199-199
    In source order: Retain source documentation literal source_literal_199_8; it is not a model call.
    // Source: vvaharness/util/scan_progress.py:200-201
    if (the source predicate not self.enabled is truthy) {
      // Source: vvaharness/util/scan_progress.py:201-201
      End this invocation with None.
    }
    // Source: vvaharness/util/scan_progress.py:202-209
    Enter source context managers left-to-right: self._lock {
      // Source: vvaharness/util/scan_progress.py:203-203
      In source order: Evaluate once len(all_files); assign in source target order to self._total_files.
      // Source: vvaharness/util/scan_progress.py:204-205
      if (the source predicate self.style in ('summary_only', 'stage_only') is truthy) {
        // Source: vvaharness/util/scan_progress.py:205-205
        End this invocation with None.
      }
      // Source: vvaharness/util/scan_progress.py:206-209
      In source order: Evaluate once source_template_206_20 if self.repo_name else ''; assign in source target order to label. Then Evaluate self._emit(source_template_208_16); retain side effects and discard the expression result.
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/util/scan_progress.py:211-234
  // Source signature: queued(self, unit) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn queued(self, unit) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/util/scan_progress.py:212-212
    In source order: Retain source documentation literal source_literal_212_8; it is not a model call.
    // Source: vvaharness/util/scan_progress.py:213-214
    if (the source predicate not self.enabled is truthy) {
      // Source: vvaharness/util/scan_progress.py:214-214
      End this invocation with None.
    }
    // Source: vvaharness/util/scan_progress.py:215-222
    In source order: Evaluate once '+'.join((getattr(unit, 'languages', None) or [])[:3]) or 'generic'; assign in source target order to lens. Then Evaluate once UnitProgress(unit_id=unit.id, files=list(getattr(unit, 'files', []) or []), rank=getattr(unit, 'risk_rank', 0), lens=lens, threat=(getattr(unit, 'threat', '') or '')[:80]); assign in source target order to cp.
    // Source: vvaharness/util/scan_progress.py:223-234
    Enter source context managers left-to-right: self._lock {
      // Source: vvaharness/util/scan_progress.py:224-224
      In source order: Evaluate once cp; assign in source target order to self._units[unit.id].
      // Source: vvaharness/util/scan_progress.py:225-226
      if (the source predicate self.style in ('summary_only', 'stage_only') is truthy) {
        // Source: vvaharness/util/scan_progress.py:226-226
        End this invocation with None.
      }
      // Source: vvaharness/util/scan_progress.py:227-231
      In source order: Evaluate once len(cp.files); assign in source target order to file_count. Then Evaluate self._emit(source_template_229_16); retain side effects and discard the expression result.
      // Source: vvaharness/util/scan_progress.py:232-234
      if (the source predicate self.style in ('verbose', 'llm_debug') is truthy) {
        // Source: vvaharness/util/scan_progress.py:233-234
        for each f in cp.files {
          // Source: vvaharness/util/scan_progress.py:234-234
          In source order: Evaluate self._emit(source_template_234_31); retain side effects and discard the expression result.
        }
      }
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/util/scan_progress.py:236-258
  // Source signature: scanning(self, unit) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn scanning(self, unit) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/util/scan_progress.py:237-237
    In source order: Retain source documentation literal source_literal_237_8; it is not a model call.
    // Source: vvaharness/util/scan_progress.py:238-239
    if (the source predicate not self.enabled is truthy) {
      // Source: vvaharness/util/scan_progress.py:239-239
      End this invocation with None.
    }
    // Source: vvaharness/util/scan_progress.py:240-258
    Enter source context managers left-to-right: self._lock {
      // Source: vvaharness/util/scan_progress.py:241-241
      In source order: Evaluate once self._units.get(unit.id); assign in source target order to cp.
      // Source: vvaharness/util/scan_progress.py:242-244
      if (the source predicate cp is truthy) {
        // Source: vvaharness/util/scan_progress.py:243-244
        In source order: Evaluate once 'scanning'; assign in source target order to cp.state. Then Evaluate once time.monotonic(); assign in source target order to cp.started_at.
      }
      // Source: vvaharness/util/scan_progress.py:245-247
      In source order: Apply source augmented assignment self._n_scanning += 1 with source evaluation/in-place semantics. Then Evaluate once len(self._units); assign in source target order to n_total. Then Evaluate once self._n_scanned; assign in source target order to n_done.
      // Source: vvaharness/util/scan_progress.py:248-249
      if (the source predicate self.style == 'summary_only' is truthy) {
        // Source: vvaharness/util/scan_progress.py:249-249
        End this invocation with None.
      }
      // Source: vvaharness/util/scan_progress.py:250-255
      In source order: Evaluate once len(getattr(unit, 'files', []) or []); assign in source target order to file_count. Then Evaluate self._emit(source_template_252_16); retain side effects and discard the expression result.
      // Source: vvaharness/util/scan_progress.py:256-258
      if (the source predicate self.style in ('verbose', 'llm_debug') is truthy) {
        // Source: vvaharness/util/scan_progress.py:257-258
        for each f in getattr(unit, 'files', []) or [] {
          // Source: vvaharness/util/scan_progress.py:258-258
          In source order: Evaluate self._emit(source_template_258_31); retain side effects and discard the expression result.
        }
      }
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/util/scan_progress.py:260-293
  // Source signature: scanned(self, unit, *, outcome: str, n_findings: int=0) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn scanned(self, unit, outcome, n_findings) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/util/scan_progress.py:261-262
    In source order: Retain source documentation literal source_literal_261_8; it is not a model call.
    // Source: vvaharness/util/scan_progress.py:263-264
    if (the source predicate not self.enabled is truthy) {
      // Source: vvaharness/util/scan_progress.py:264-264
      End this invocation with None.
    }
    // Source: vvaharness/util/scan_progress.py:265-293
    Enter source context managers left-to-right: self._lock {
      // Source: vvaharness/util/scan_progress.py:266-267
      In source order: Evaluate once self._units.get(unit.id); assign in source target order to cp. Then Evaluate once cp is None or cp.outcome is None; assign in source target order to first.
      // Source: vvaharness/util/scan_progress.py:268-272
      if (the source predicate cp is truthy) {
        // Source: vvaharness/util/scan_progress.py:269-272
        In source order: Evaluate once 'scanned'; assign in source target order to cp.state. Then Evaluate once outcome; assign in source target order to cp.outcome. Then Evaluate once n_findings; assign in source target order to cp.findings. Then Evaluate once time.monotonic() - cp.started_at; assign in source target order to cp.elapsed.
      }
      // Source: vvaharness/util/scan_progress.py:273-273
      In source order: Evaluate once max(0, self._n_scanning - 1); assign in source target order to self._n_scanning.
      // Source: vvaharness/util/scan_progress.py:274-276
      if (the source predicate first is truthy) {
        // Source: vvaharness/util/scan_progress.py:275-276
        In source order: Apply source augmented assignment self._n_scanned += 1 with source evaluation/in-place semantics. Then Apply source augmented assignment self._findings += max(0, n_findings) with source evaluation/in-place semantics.
      }
      // Source: vvaharness/util/scan_progress.py:277-278
      if (the source predicate self.style == 'summary_only' is truthy) {
        // Source: vvaharness/util/scan_progress.py:278-278
        End this invocation with None.
      }
      // Source: vvaharness/util/scan_progress.py:279-287
      In source order: Evaluate once source_template_279_24 if cp else '?'; assign in source target order to elapsed_s. Then Evaluate once {'completed': '✓', 'error': '✗', 'guardrail': '⊘', 'uninvestigated': '∅', 'failed': '⚠'}.get(outcome, '?'); assign in source target order to icon. Then Evaluate once source_template_282_28 if n_findings else ''; assign in source target order to finding_note. Then Evaluate self._emit(source_template_284_16); retain side effects and discard the expression result. Then Evaluate once getattr(unit, 'files', []) or []; assign in source target order to files.
      // Source: vvaharness/util/scan_progress.py:288-290
      In source order: Evaluate once self.style in ('verbose', 'llm_debug') or (self.style == 'compact' and (n_findings > 0 or outcome != 'completed')); assign in source target order to show_files.
      // Source: vvaharness/util/scan_progress.py:291-293
      if (the source predicate show_files is truthy) {
        // Source: vvaharness/util/scan_progress.py:292-293
        for each f in files {
          // Source: vvaharness/util/scan_progress.py:293-293
          In source order: Evaluate self._emit(source_template_293_31); retain side effects and discard the expression result.
        }
      }
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/util/scan_progress.py:295-336
  // Source signature: print_summary(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn print_summary(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/util/scan_progress.py:296-296
    In source order: Retain source documentation literal source_literal_296_8; it is not a model call.
    // Source: vvaharness/util/scan_progress.py:297-298
    if (the source predicate not self.enabled or self.style == 'stage_only' is truthy) {
      // Source: vvaharness/util/scan_progress.py:298-298
      End this invocation with None.
    }
    // Source: vvaharness/util/scan_progress.py:299-336
    Enter source context managers left-to-right: self._lock {
      // Source: vvaharness/util/scan_progress.py:300-302
      In source order: Evaluate once len(self._units); assign in source target order to total. Then For outcomes, assign {}; source annotation dict[str, int]. Then For scanned_files, assign set(); source annotation set[str].
      // Source: vvaharness/util/scan_progress.py:303-307
      for each cp in self._units.values() {
        // Source: vvaharness/util/scan_progress.py:304-305
        In source order: Evaluate once cp.outcome or 'pending'; assign in source target order to o. Then Evaluate once outcomes.get(o, 0) + 1; assign in source target order to outcomes[o].
        // Source: vvaharness/util/scan_progress.py:306-307
        if (the source predicate cp.state == 'scanned' is truthy) {
          // Source: vvaharness/util/scan_progress.py:307-307
          In source order: Evaluate scanned_files.update(cp.files); retain side effects and discard the expression result.
        }
      }
      // Source: vvaharness/util/scan_progress.py:308-319
      In source order: Evaluate once total - self._n_scanned; assign in source target order to remaining. Then Evaluate once self._stages.get('s4', {}).get('start'); assign in source target order to stage_start. Then Evaluate once max(0.0, time.monotonic() - float(stage_start)) if stage_start is not None else 0.0; assign in source target order to elapsed. Then Evaluate once '  '.join((source_template_314_16 for k, v in sorted(outcomes.items()))); assign in source target order to outcome_str. Then Evaluate self._emit(source_template_317_16); retain side effects and discard the expression result.
      // Source: vvaharness/util/scan_progress.py:320-321
      if (the source predicate outcome_str is truthy) {
        // Source: vvaharness/util/scan_progress.py:321-321
        In source order: Evaluate self._emit(source_template_321_27); retain side effects and discard the expression result.
      }
      // Source: vvaharness/util/scan_progress.py:322-326
      if (the source predicate remaining > 0 is truthy) {
        // Source: vvaharness/util/scan_progress.py:323-326
        In source order: Evaluate self._emit(source_template_324_20); retain side effects and discard the expression result.
      }
      // Source: vvaharness/util/scan_progress.py:328-336
      if (the source predicate total > 1 is truthy) {
        // Source: vvaharness/util/scan_progress.py:329-336
        for each cp in sorted(self._units.values(), key=lambda c: c.unit_id) {
          // Source: vvaharness/util/scan_progress.py:330-331
          if (the source predicate cp.state != 'scanned' is truthy) {
            // Source: vvaharness/util/scan_progress.py:331-331
            Continue the immediately enclosing source loop at its next iteration.
          }
          // Source: vvaharness/util/scan_progress.py:332-336
          In source order: Evaluate once source_template_332_35 if cp.findings else ''; assign in source target order to finding_note. Then Evaluate self._emit(source_template_334_24); retain side effects and discard the expression result.
        }
      }
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/util/scan_progress.py:338-352
  // Source signature: llm_payload(self, *, phase: str, backend: str, model_id: str, tag: str='', user_prompt: str='', system_prompt: str='') -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn llm_payload(self, phase, backend, model_id, tag, user_prompt, system_prompt) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/util/scan_progress.py:341-341
    In source order: Retain source documentation literal source_literal_341_8; it is not a model call.
    // Source: vvaharness/util/scan_progress.py:342-343
    if (the source predicate not self.enabled or self.style != 'llm_debug' is truthy) {
      // Source: vvaharness/util/scan_progress.py:343-343
      End this invocation with None.
    }
    // Source: vvaharness/util/scan_progress.py:344-352
    Enter source context managers left-to-right: self._lock {
      // Source: vvaharness/util/scan_progress.py:345-349
      In source order: Evaluate once source_template_345_23 if tag else ''; assign in source target order to tag_note. Then Evaluate self._emit(source_template_347_16); retain side effects and discard the expression result.
      // Source: vvaharness/util/scan_progress.py:350-351
      if (the source predicate system_prompt is truthy) {
        // Source: vvaharness/util/scan_progress.py:351-351
        In source order: Evaluate self._emit_prompt_block('system', system_prompt); retain side effects and discard the expression result.
      }
      // Source: vvaharness/util/scan_progress.py:352-352
      In source order: Evaluate self._emit_prompt_block('user', user_prompt); retain side effects and discard the expression result.
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/util/scan_progress.py:354-375
  // Source signature: _emit_prompt_block(self, label: str, text: str) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _emit_prompt_block(self, label, text) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/util/scan_progress.py:355-355
    In source order: Evaluate once text or ''; assign in source target order to payload.
    // Source: vvaharness/util/scan_progress.py:356-362
    Perform the following protected operations {
      // Source: vvaharness/util/scan_progress.py:357-359
      In source order: Resolve source import from vvaharness.report.redact import redact; preserve alias and import-time effects. Then Evaluate once redact(payload); assign in source target order to payload.
    }
    // Source: vvaharness/util/scan_progress.py:360-362
    On the first matching source exception Exception, in handler order {
      // Source: vvaharness/util/scan_progress.py:362-362
      In source order: Perform no operation at this source statement.
    }
    // Source: vvaharness/util/scan_progress.py:363-368
    In source order: Evaluate once len(payload); assign in source target order to total. Then Evaluate once payload[:self._llm_max_chars]; assign in source target order to shown. Then Evaluate self._emit(source_template_366_12); retain side effects and discard the expression result.
    // Source: vvaharness/util/scan_progress.py:369-370
    for each ln in shown.splitlines() or [''] {
      // Source: vvaharness/util/scan_progress.py:370-370
      In source order: Evaluate self._emit(source_template_370_23); retain side effects and discard the expression result.
    }
    // Source: vvaharness/util/scan_progress.py:371-374
    if (the source predicate total > len(shown) is truthy) {
      // Source: vvaharness/util/scan_progress.py:372-374
      In source order: Evaluate self._emit(source_template_373_16); retain side effects and discard the expression result.
    }
    // Source: vvaharness/util/scan_progress.py:375-375
    In source order: Evaluate self._emit(source_template_375_19); retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/util/scan_progress.py:380-385
  // Source: vvaharness/util/scan_progress.py:379-379
  Before creating this callable, evaluate and retain decorators top-to-bottom: staticmethod.
  // Source: vvaharness/util/scan_progress.py:380-385
  // Source signature: _stage_number(stage_id: str) -> str
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _stage_number(stage_id) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/util/scan_progress.py:381-384
    Perform the following protected operations {
      // Source: vvaharness/util/scan_progress.py:382-382
      In source order: Evaluate once _STAGE_ORDER.index(stage_id) + 1; assign in source target order to index.
    }
    // Source: vvaharness/util/scan_progress.py:383-384
    On the first matching source exception ValueError, in handler order {
      // Source: vvaharness/util/scan_progress.py:384-384
      End this invocation with source_template_384_19.
    }
    // Source: vvaharness/util/scan_progress.py:385-385
    End this invocation with source_template_385_15.
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vvaharness/util/scan_progress.py:387-391
  // Source signature: _emit(self, line: str) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _emit(self, line) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/util/scan_progress.py:388-388
    In source order: Retain source documentation literal source_literal_388_8; it is not a model call.
    // Source: vvaharness/util/scan_progress.py:389-390
    if (the source predicate self._live is not None is truthy) {
      // Source: vvaharness/util/scan_progress.py:390-390
      End this invocation with None.
    }
    // Source: vvaharness/util/scan_progress.py:391-391
    In source order: Evaluate console.write(line); retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/util/scan_progress.py:393-410
  // Source signature: start_live(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn start_live(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/util/scan_progress.py:394-394
    In source order: Retain source documentation literal source_literal_394_8; it is not a model call.
    // Source: vvaharness/util/scan_progress.py:395-396
    if (the source predicate self._live is not None or self.style != 'live' or (not self.enabled) is truthy) {
      // Source: vvaharness/util/scan_progress.py:396-396
      End this invocation with None.
    }
    // Source: vvaharness/util/scan_progress.py:397-399
    if (the source predicate not _stderr_is_a_terminal() is truthy) {
      // Source: vvaharness/util/scan_progress.py:398-398
      In source order: Evaluate once 'compact'; assign in source target order to self.style.
      // Source: vvaharness/util/scan_progress.py:399-399
      End this invocation with None.
    }
    // Source: vvaharness/util/scan_progress.py:400-408
    Perform the following protected operations {
      // Source: vvaharness/util/scan_progress.py:401-405
      In source order: Resolve source import from rich.live import Live; preserve alias and import-time effects. Then Evaluate once Live(get_renderable=self._render, console=console.console(), refresh_per_second=_LIVE_REFRESH_HZ, transient=False); assign in source target order to live. Then Evaluate live.start(); retain side effects and discard the expression result.
    }
    // Source: vvaharness/util/scan_progress.py:406-408
    On the first matching source exception (ImportError, OSError, ValueError), in handler order {
      // Source: vvaharness/util/scan_progress.py:407-407
      In source order: Evaluate once 'compact'; assign in source target order to self.style.
      // Source: vvaharness/util/scan_progress.py:408-408
      End this invocation with None.
    }
    // Source: vvaharness/util/scan_progress.py:409-410
    In source order: Evaluate once live; assign in source target order to self._live. Then Evaluate atexit.register(self.stop_live); retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/util/scan_progress.py:412-420
  // Source signature: stop_live(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn stop_live(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/util/scan_progress.py:413-414
    In source order: Retain source documentation literal source_literal_413_8; it is not a model call. Then Evaluate once (self._live, None); assign in source target order to (live, self._live).
    // Source: vvaharness/util/scan_progress.py:415-416
    if (the source predicate live is None is truthy) {
      // Source: vvaharness/util/scan_progress.py:416-416
      End this invocation with None.
    }
    // Source: vvaharness/util/scan_progress.py:417-420
    Perform the following protected operations {
      // Source: vvaharness/util/scan_progress.py:418-418
      In source order: Evaluate live.stop(); retain side effects and discard the expression result.
    }
    // Source: vvaharness/util/scan_progress.py:419-420
    On the first matching source exception OSError, in handler order {
      // Source: vvaharness/util/scan_progress.py:420-420
      In source order: Evaluate once 'compact'; assign in source target order to self.style.
    }
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/util/scan_progress.py:422-429
  // Source signature: _render(self)
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _render(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/util/scan_progress.py:423-423
    In source order: Retain source documentation literal source_literal_423_8; it is not a model call.
    // Source: vvaharness/util/scan_progress.py:424-429
    Perform the following protected operations {
      // Source: vvaharness/util/scan_progress.py:425-425
      End this invocation with self._stage_table().
    }
    // Source: vvaharness/util/scan_progress.py:426-429
    On the first matching source exception Exception, in handler order {
      // Source: vvaharness/util/scan_progress.py:427-427
      In source order: Resolve source import from rich.text import Text; preserve alias and import-time effects.
      // Source: vvaharness/util/scan_progress.py:429-429
      End this invocation with Text('').
    }
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/util/scan_progress.py:431-469
  // Source signature: _stage_table(self)
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _stage_table(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/util/scan_progress.py:432-436
    In source order: Resolve source import from rich.spinner import Spinner; preserve alias and import-time effects. Then Resolve source import from rich.table import Table; preserve alias and import-time effects. Then Resolve source import from rich.text import Text; preserve alias and import-time effects. Then Evaluate once Table(box=None, pad_edge=False, show_edge=False, header_style='muted'); assign in source target order to table.
    // Source: vvaharness/util/scan_progress.py:437-438
    for each column in ('', 'stage', 'what', 'status', 'time') {
      // Source: vvaharness/util/scan_progress.py:438-438
      In source order: Evaluate table.add_column(column, overflow='fold'); retain side effects and discard the expression result.
    }
    // Source: vvaharness/util/scan_progress.py:439-442
    Enter source context managers left-to-right: self._lock {
      // Source: vvaharness/util/scan_progress.py:440-442
      In source order: Evaluate once dict(self._stages); assign in source target order to stages. Then Evaluate once (self._n_scanning, self._n_scanned, len(self._units)); assign in source target order to (scanning, scanned, units). Then Evaluate once (self._findings, self._start); assign in source target order to (findings, started).
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    // Source: vvaharness/util/scan_progress.py:443-457
    for each (index, stage_id) in enumerate(_STAGE_ORDER) {
      // Source: vvaharness/util/scan_progress.py:444-446
      In source order: Evaluate once stages.get(stage_id); assign in source target order to record. Then Evaluate once str(record.get('state', '')) if record else ''; assign in source target order to state. Then Evaluate once str(record.get('label', '')) if record else ''; assign in source target order to label.
      // Source: vvaharness/util/scan_progress.py:447-454
      if (the source predicate state == 'started' is truthy) {
        // Source: vvaharness/util/scan_progress.py:448-449
        In source order: Evaluate once (Spinner('dots', style='model'), time.monotonic() - float(record.get('start', started))); assign in source target order to (status, clock).
      }
      else {
        // Source: vvaharness/util/scan_progress.py:450-454
        if (the source predicate record is truthy) {
          // Source: vvaharness/util/scan_progress.py:451-452
          In source order: Evaluate once (Text(_OUTCOME_GLYPH.get(state, state), style=_OUTCOME_STYLE.get(state, 'muted')), float(record.get('elapsed', 0.0))); assign in source target order to (status, clock).
        }
        else {
          // Source: vvaharness/util/scan_progress.py:454-454
          In source order: Evaluate once (Text('·', style='muted'), None); assign in source target order to (status, clock).
        }
      }
      // Source: vvaharness/util/scan_progress.py:455-457
      In source order: Evaluate table.add_row(Text(source_template_455_31, style='muted'), Text(stage_id.upper()), Text(label or _STAGE_LABELS.get(stage_id, ''), style='muted'), status, Text('' if clock is None else _clock(clock), style='muted')); retain side effects and discard the expression result.
    }
    // Source: vvaharness/util/scan_progress.py:458-460
    In source order: Evaluate once Text('  '); assign in source target order to header. Then Evaluate header.append(self.repo_name or 'scan', style='heading'); retain side effects and discard the expression result. Then Evaluate header.append(source_template_460_22, style='muted'); retain side effects and discard the expression result.
    // Source: vvaharness/util/scan_progress.py:461-464
    if (the source predicate units is truthy) {
      // Source: vvaharness/util/scan_progress.py:462-462
      In source order: Evaluate header.append(source_template_462_26, style='muted'); retain side effects and discard the expression result.
      // Source: vvaharness/util/scan_progress.py:463-464
      if (the source predicate scanning is truthy) {
        // Source: vvaharness/util/scan_progress.py:464-464
        In source order: Evaluate header.append(source_template_464_30, style='muted'); retain side effects and discard the expression result.
      }
    }
    // Source: vvaharness/util/scan_progress.py:465-466
    if (the source predicate findings is truthy) {
      // Source: vvaharness/util/scan_progress.py:466-466
      In source order: Evaluate header.append(source_template_466_26, style='model'); retain side effects and discard the expression result.
    }
    // Source: vvaharness/util/scan_progress.py:467-467
    In source order: Resolve source import from rich.console import Group; preserve alias and import-time effects.
    // Source: vvaharness/util/scan_progress.py:469-469
    End this invocation with Group(Text(''), header, Text(''), table, Text('')).
    If execution reaches this end, finish with the source implicit None result.
  }
}
```

## Local import links

- `from vvaharness.util import console` at source line 26: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import console` at source line 26: `source_detail/vvaharness/util/console.py.sudo.md`.
- `from vvaharness.report.redact import redact` at source line 357: `source_detail/vvaharness/report/redact.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../prompt_representation/vvaharness/util/scan_progress.py.sudo.md). Exact strings in the evidence asset support this conversion.
