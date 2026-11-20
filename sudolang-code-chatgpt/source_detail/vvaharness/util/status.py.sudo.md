# vvaharness/util/status.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/util/status.py.evidence.json`. SHA-256: `0891e4808290ea8c7c96e0cde6c7fde2ecf0b8bd43e13fae229d4eed537d7ca4`.

```sudo
// Source: vvaharness/util/status.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import itertools; preserve alias and import-time effects. Then Resolve source import import json; preserve alias and import-time effects. Then Resolve source import import os; preserve alias and import-time effects.
// Source: vvaharness/util/status.py:22-26
In source order: Resolve source import import shutil; preserve alias and import-time effects. Then Resolve source import import sys; preserve alias and import-time effects. Then Resolve source import import threading; preserve alias and import-time effects. Then Resolve source import import time; preserve alias and import-time effects. Then Resolve source import from contextlib import contextmanager; preserve alias and import-time effects.
// Source: vvaharness/util/status.py:27-32
In source order: Resolve source import from dataclasses import dataclass; preserve alias and import-time effects. Then Resolve source import from datetime import UTC, datetime; preserve alias and import-time effects. Then Resolve source import from vvaharness.report.redact import redact; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import errlog as _errlog; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.stage_telemetry import STAGES; preserve alias and import-time effects.
// Source: vvaharness/util/status.py:34-39
In source order: Evaluate once '⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏'; assign in source target order to _SPIN. Then Evaluate once ('\x1b[36m', '\x1b[32m', '\x1b[31m', '\x1b[33m', '\x1b[2m', '\x1b[0m'); assign in source target order to (_CYAN, _GREEN, _RED, _YELLOW, _DIM, _RST). Then Evaluate once ('✓', '⚠', '✗'); assign in source target order to (OK_MARK, WARN_MARK, FAIL_MARK).
// Source: vvaharness/util/status.py:43-50
// Source: vvaharness/util/status.py:42-42
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass.
// Source: vvaharness/util/status.py:43-50
interface StageResult {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/util/status.py:44-46
  In source order: Retain source documentation literal source_literal_44_4; it is not a model call. Then For incomplete_detail, assign ''; source annotation str.
  // Source: vvaharness/util/status.py:48-50
  // Source signature: mark_incomplete(self, detail: str) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn mark_incomplete(self, detail) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/util/status.py:49-50
    In source order: Retain source documentation literal source_literal_49_8; it is not a model call. Then Evaluate once detail; assign in source target order to self.incomplete_detail.
    If execution reaches this end, finish with the source implicit None result.
  }
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vvaharness/util/status.py:53-57
// Source signature: _is_tty(stream) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _is_tty(stream) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/status.py:54-57
  Perform the following protected operations {
    // Source: vvaharness/util/status.py:55-55
    End this invocation with bool(stream.isatty()).
  }
  // Source: vvaharness/util/status.py:56-57
  On the first matching source exception Exception, in handler order {
    // Source: vvaharness/util/status.py:57-57
    End this invocation with False.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/status.py:60-96
interface _Spinner {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/util/status.py:61-61
  In source order: Retain source documentation literal source_literal_61_4; it is not a model call.
  // Source: vvaharness/util/status.py:63-67
  // Source signature: __init__(self, label, out, n=None, total=None)
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self, label, out, n, total) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/util/status.py:64-67
    In source order: Evaluate once (label, out, n, total); assign in source target order to (self._label, self._out, self._n, self._total). Then Evaluate once threading.Event(); assign in source target order to self._stop. Then Evaluate once time.time(); assign in source target order to self._t0. Then Evaluate once threading.Thread(target=self._run, daemon=True); assign in source target order to self._thread.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/util/status.py:69-71
  // Source signature: start(self)
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn start(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/util/status.py:70-70
    In source order: Evaluate self._thread.start(); retain side effects and discard the expression result.
    // Source: vvaharness/util/status.py:71-71
    End this invocation with self.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/util/status.py:73-90
  // Source signature: _run(self)
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _run(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/util/status.py:74-74
    In source order: Evaluate once source_template_74_14 if self._n and self._total else ''; assign in source target order to tag.
    // Source: vvaharness/util/status.py:75-90
    for each frame in itertools.cycle(_SPIN) {
      // Source: vvaharness/util/status.py:76-77
      if (the source predicate self._stop.is_set() is truthy) {
        // Source: vvaharness/util/status.py:77-77
        Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
      }
      // Source: vvaharness/util/status.py:78-83
      In source order: Evaluate once int(time.time() - self._t0); assign in source target order to el. Then Evaluate once shutil.get_terminal_size((80, 24)).columns; assign in source target order to cols. Then Evaluate once source_template_81_21; assign in source target order to prefix. Then Evaluate once source_template_82_21; assign in source target order to suffix. Then Evaluate once cols - len(prefix) - len(suffix) - 1; assign in source target order to budget.
      // Source: vvaharness/util/status.py:84-84
      In source order: Evaluate once self._label; assign in source target order to label.
      // Source: vvaharness/util/status.py:85-86
      if (the source predicate budget > 1 and len(label) > budget is truthy) {
        // Source: vvaharness/util/status.py:86-86
        In source order: Evaluate once label[:budget - 1] + '…'; assign in source target order to label.
      }
      // Source: vvaharness/util/status.py:87-90
      In source order: Evaluate self._out.write(source_template_87_28); retain side effects and discard the expression result. Then Evaluate self._out.flush(); retain side effects and discard the expression result. Then Evaluate self._stop.wait(0.12); retain side effects and discard the expression result.
    }
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/util/status.py:92-96
  // Source signature: stop(self)
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn stop(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/util/status.py:93-96
    In source order: Evaluate self._stop.set(); retain side effects and discard the expression result. Then Evaluate self._thread.join(timeout=1); retain side effects and discard the expression result. Then Evaluate self._out.write('\r\x1b[K'); retain side effects and discard the expression result. Then Evaluate self._out.flush(); retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vvaharness/util/status.py:99-101
// Source signature: json_logs_enabled() -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn json_logs_enabled() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/status.py:100-100
  In source order: Retain source documentation literal source_literal_100_4; it is not a model call.
  // Source: vvaharness/util/status.py:101-101
  End this invocation with os.environ.get('VVAHARNESS_JSON_LOGS', '').lower() in ('1', 'true', 'yes').
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/status.py:104-111
// Source signature: emit_event(event: str, *, stream=None, **fields) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn emit_event(event, stream, fields) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/status.py:105-105
  In source order: Retain source documentation literal source_literal_105_4; it is not a model call.
  // Source: vvaharness/util/status.py:106-107
  if (the source predicate not json_logs_enabled() is truthy) {
    // Source: vvaharness/util/status.py:107-107
    End this invocation with None.
  }
  // Source: vvaharness/util/status.py:108-111
  In source order: Evaluate once stream if stream is not None else sys.stderr; assign in source target order to out. Then Evaluate once {'ts': datetime.now(UTC).isoformat(), 'event': event}; assign in source target order to rec. Then Evaluate rec.update({k: v for k, v in fields.items() if v is not None}); retain side effects and discard the expression result. Then Evaluate print(json.dumps(rec, separators=(',', ':')), file=out, flush=True); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/status.py:115-192
// Source: vvaharness/util/status.py:114-114
Before creating this callable, evaluate and retain decorators top-to-bottom: contextmanager.
// Source: vvaharness/util/status.py:115-192
// Source signature: stage(label: str, *, n: int | None=None, total: int | None=None, stream=None, animate: bool | None=None, stage_id: str | None=None)
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn stage(label, n, total, stream, animate, stage_id) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/status.py:118-123
  In source order: Retain source documentation literal source_literal_118_4; it is not a model call. Then Evaluate once stream if stream is not None else sys.stderr; assign in source target order to out. Then Evaluate once source_template_121_10 if n is not None and total is not None else ''; assign in source target order to tag. Then Evaluate once json_logs_enabled(); assign in source target order to as_json. Then Evaluate once _is_tty(out); assign in source target order to auto_animate.
  // Source: vvaharness/util/status.py:124-128
  In source order: Evaluate once (auto_animate if animate is None else animate) and (not as_json); assign in source target order to animate. Then Evaluate once time.time(); assign in source target order to t0. Then Evaluate once None; assign in source target order to spin. Then Evaluate once _errlog.count_for_stage(stage_id, include_recovered=False) if stage_id else 0; assign in source target order to err0.
  // Source: vvaharness/util/status.py:129-130
  if (the source predicate stage_id is truthy) {
    // Source: vvaharness/util/status.py:130-130
    In source order: Evaluate STAGES.start(stage_id, label); retain side effects and discard the expression result.
  }
  // Source: vvaharness/util/status.py:131-137
  if (the source predicate as_json is truthy) {
    // Source: vvaharness/util/status.py:132-133
    In source order: Evaluate emit_event('stage_start', stage=label, n=n, total=total, stage_id=stage_id, stream=out); retain side effects and discard the expression result.
  }
  else {
    // Source: vvaharness/util/status.py:134-137
    if (the source predicate animate is truthy) {
      // Source: vvaharness/util/status.py:135-135
      In source order: Evaluate once _Spinner(label, out, n, total).start(); assign in source target order to spin.
    }
    else {
      // Source: vvaharness/util/status.py:137-137
      In source order: Evaluate print(source_template_137_14, file=out, flush=True); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/util/status.py:138-138
  In source order: Evaluate once StageResult(); assign in source target order to result.
  // Source: vvaharness/util/status.py:139-192
  Perform the following protected operations {
    // Source: vvaharness/util/status.py:140-140
    In source order: Yield result; suspend this generator until resumed.
  }
  // Source: vvaharness/util/status.py:141-158
  On the first matching source exception BaseException as e, in handler order {
    // Source: vvaharness/util/status.py:142-142
    In source order: Evaluate once round(time.time() - t0, 2); assign in source target order to dt.
    // Source: vvaharness/util/status.py:143-144
    if (the source predicate spin is truthy) {
      // Source: vvaharness/util/status.py:144-144
      In source order: Evaluate spin.stop(); retain side effects and discard the expression result.
    }
    // Source: vvaharness/util/status.py:145-146
    if (the source predicate stage_id is truthy) {
      // Source: vvaharness/util/status.py:146-146
      In source order: Evaluate STAGES.done(stage_id, outcome='error', duration_sec=dt); retain side effects and discard the expression result.
    }
    // Source: vvaharness/util/status.py:147-154
    if (the source predicate as_json is truthy) {
      // Source: vvaharness/util/status.py:148-150
      In source order: Evaluate emit_event('stage_fail', stage=label, n=n, total=total, duration_sec=dt, stage_id=stage_id, error=redact(source_template_150_36), stream=out); retain side effects and discard the expression result.
    }
    else {
      // Source: vvaharness/util/status.py:152-154
      In source order: Evaluate once source_template_152_16 if animate else FAIL_MARK; assign in source target order to x. Then Evaluate print(source_template_153_18, file=out, flush=True); retain side effects and discard the expression result.
    }
    // Source: vvaharness/util/status.py:156-157
    if (the source predicate not as_json is truthy) {
      // Source: vvaharness/util/status.py:157-157
      In source order: Evaluate print(file=out, flush=True); retain side effects and discard the expression result.
    }
    // Source: vvaharness/util/status.py:158-158
    Raise the currently handled exception.
  }
  Only when the protected body falls through normally, without exception, return, break or continue {
    // Source: vvaharness/util/status.py:160-160
    In source order: Evaluate once round(time.time() - t0, 2); assign in source target order to dt.
    // Source: vvaharness/util/status.py:161-162
    if (the source predicate spin is truthy) {
      // Source: vvaharness/util/status.py:162-162
      In source order: Evaluate spin.stop(); retain side effects and discard the expression result.
    }
    // Source: vvaharness/util/status.py:164-165
    In source order: Evaluate once _errlog.count_for_stage(stage_id, include_recovered=False) - err0 if stage_id else 0; assign in source target order to n_err.
    // Source: vvaharness/util/status.py:166-168
    if (the source predicate stage_id is truthy) {
      // Source: vvaharness/util/status.py:167-168
      In source order: Evaluate once 'completed_with_errors' if n_err > 0 else 'completed'; assign in source target order to outcome. Then Evaluate STAGES.done(stage_id, outcome=outcome, duration_sec=dt); retain side effects and discard the expression result.
    }
    // Source: vvaharness/util/status.py:170-173
    In source order: Evaluate once source_template_170_16 if n_err > 0 else ''; assign in source target order to note. Then Evaluate once (WARN_MARK, _YELLOW) if n_err > 0 else (OK_MARK, _GREEN); assign in source target order to (mark, colour).
    // Source: vvaharness/util/status.py:174-189
    if (the source predicate result.incomplete_detail and as_json is truthy) {
      // Source: vvaharness/util/status.py:175-177
      In source order: Evaluate emit_event('stage_incomplete', stage=label, n=n, total=total, duration_sec=dt, stage_id=stage_id, detail=result.incomplete_detail, stream=out); retain side effects and discard the expression result.
    }
    else {
      // Source: vvaharness/util/status.py:178-189
      if (the source predicate as_json is truthy) {
        // Source: vvaharness/util/status.py:179-181
        In source order: Evaluate emit_event('stage_ok', stage=label, n=n, total=total, duration_sec=dt, stage_id=stage_id, errors=n_err if n_err > 0 else None, stream=out); retain side effects and discard the expression result.
      }
      else {
        // Source: vvaharness/util/status.py:182-189
        if (the source predicate result.incomplete_detail is truthy) {
          // Source: vvaharness/util/status.py:183-184
          In source order: Evaluate print(source_template_183_18, file=out, flush=True); retain side effects and discard the expression result.
        }
        else {
          // Source: vvaharness/util/status.py:185-189
          if (the source predicate animate is truthy) {
            // Source: vvaharness/util/status.py:186-187
            In source order: Evaluate print(source_template_186_18, file=out, flush=True); retain side effects and discard the expression result.
          }
          else {
            // Source: vvaharness/util/status.py:189-189
            In source order: Evaluate print(source_template_189_18, file=out, flush=True); retain side effects and discard the expression result.
          }
        }
      }
    }
    // Source: vvaharness/util/status.py:191-192
    if (the source predicate not as_json is truthy) {
      // Source: vvaharness/util/status.py:192-192
      In source order: Evaluate print(file=out, flush=True); retain side effects and discard the expression result.
    }
  }
  If execution reaches this end, finish with the source implicit None result.
}
At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
```

## Local import links

- `from vvaharness.report.redact import redact` at source line 30: `source_detail/vvaharness/report/redact.py.sudo.md`.
- `from vvaharness.util import errlog as _errlog` at source line 31: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import errlog as _errlog` at source line 31: `source_detail/vvaharness/util/errlog.py.sudo.md`.
- `from vvaharness.util.stage_telemetry import STAGES` at source line 32: `source_detail/vvaharness/util/stage_telemetry.py.sudo.md`.
