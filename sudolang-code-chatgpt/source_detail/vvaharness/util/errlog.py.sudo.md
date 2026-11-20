# vvaharness/util/errlog.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/util/errlog.py.evidence.json`. SHA-256: `bc2922b8aab5c8a91926102ab4477956a4735972aaba4eb115ced991eff66e4f`.

```sudo
// Source: vvaharness/util/errlog.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import logs; preserve alias and import-time effects. Then Resolve source import import json; preserve alias and import-time effects. Then Resolve source import import os; preserve alias and import-time effects.
// Source: vvaharness/util/errlog.py:22-27
In source order: Resolve source import import threading; preserve alias and import-time effects. Then Resolve source import import traceback; preserve alias and import-time effects. Then Resolve source import from datetime import UTC, datetime; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from vvaharness.report.redact import redact; preserve alias and import-time effects.
// Source: vvaharness/util/errlog.py:28-34
In source order: Resolve source import from vvaharness.util.exceptions import exception_chain; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.events import Event; preserve alias and import-time effects. Then Evaluate once logs.get_logger(__name__); assign in source target order to _log. Then For _path, assign Path('pipeline-errors.jsonl'); source annotation Path. Then Evaluate once threading.Lock(); assign in source target order to _lock.
// Source: vvaharness/util/errlog.py:37-37
In source order: Evaluate once '_vvah_errlog_recorded'; assign in source target order to _LOGGED_ATTR.
// Source: vvaharness/util/errlog.py:40-43
// Source signature: configure(path: str | Path) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn configure(path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/errlog.py:41-43
  In source order: Bind names in module scope: _path. Then Evaluate once Path(path); assign in source target order to _path. Then Evaluate _path.parent.mkdir(parents=True, exist_ok=True); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/errlog.py:46-48
// Source signature: current_path() -> Path
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn current_path() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/errlog.py:47-47
  In source order: Retain source documentation literal source_literal_47_4; it is not a model call.
  // Source: vvaharness/util/errlog.py:48-48
  End this invocation with _path.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/errlog.py:51-74
// Source signature: counts_by_stage(path: str | Path | None=None, *, include_recovered: bool=True) -> dict[str, int]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn counts_by_stage(path, include_recovered) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/errlog.py:53-56
  In source order: Retain source documentation literal source_literal_53_4; it is not a model call. Then Evaluate once Path(path) if path is not None else _path; assign in source target order to p. Then For counts, assign {}; source annotation dict[str, int].
  // Source: vvaharness/util/errlog.py:57-73
  Perform the following protected operations {
    // Source: vvaharness/util/errlog.py:58-71
    Enter source context managers left-to-right: p.open('r', encoding='utf-8') bound to f {
      // Source: vvaharness/util/errlog.py:59-71
      for each ln in f {
        // Source: vvaharness/util/errlog.py:60-60
        In source order: Evaluate once ln.strip(); assign in source target order to ln.
        // Source: vvaharness/util/errlog.py:61-62
        if (the source predicate not ln is truthy) {
          // Source: vvaharness/util/errlog.py:62-62
          Continue the immediately enclosing source loop at its next iteration.
        }
        // Source: vvaharness/util/errlog.py:63-66
        Perform the following protected operations {
          // Source: vvaharness/util/errlog.py:64-64
          In source order: Evaluate once json.loads(ln); assign in source target order to rec.
        }
        // Source: vvaharness/util/errlog.py:65-66
        On the first matching source exception (json.JSONDecodeError, ValueError), in handler order {
          // Source: vvaharness/util/errlog.py:66-66
          Continue the immediately enclosing source loop at its next iteration.
        }
        // Source: vvaharness/util/errlog.py:67-68
        if (the source predicate not include_recovered and rec.get('recovered') is True is truthy) {
          // Source: vvaharness/util/errlog.py:68-68
          Continue the immediately enclosing source loop at its next iteration.
        }
        // Source: vvaharness/util/errlog.py:69-69
        In source order: Evaluate once rec.get('stage'); assign in source target order to stage.
        // Source: vvaharness/util/errlog.py:70-71
        if (the source predicate isinstance(stage, str) is truthy) {
          // Source: vvaharness/util/errlog.py:71-71
          In source order: Evaluate once counts.get(stage, 0) + 1; assign in source target order to counts[stage].
        }
      }
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
  }
  // Source: vvaharness/util/errlog.py:72-73
  On the first matching source exception OSError, in handler order {
    // Source: vvaharness/util/errlog.py:73-73
    End this invocation with counts.
  }
  // Source: vvaharness/util/errlog.py:74-74
  End this invocation with counts.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/errlog.py:77-87
// Source signature: count_for_stage(stage_id: str, path: str | Path | None=None, *, include_recovered: bool=True) -> int
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn count_for_stage(stage_id, path, include_recovered) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/errlog.py:79-81
  In source order: Retain source documentation literal source_literal_79_4; it is not a model call. Then Evaluate once 0; assign in source target order to total.
  // Source: vvaharness/util/errlog.py:82-86
  for each (label, n) in counts_by_stage(path, include_recovered=include_recovered).items() {
    // Source: vvaharness/util/errlog.py:84-86
    if (the source predicate label == stage_id or (label.startswith(stage_id) and (not label[len(stage_id)].isalnum())) is truthy) {
      // Source: vvaharness/util/errlog.py:86-86
      In source order: Apply source augmented assignment total += n with source evaluation/in-place semantics.
    }
  }
  // Source: vvaharness/util/errlog.py:87-87
  End this invocation with total.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/errlog.py:90-117
// Source signature: last_message_for_stage(stage_id: str, path: str | Path | None=None) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn last_message_for_stage(stage_id, path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/errlog.py:91-94
  In source order: Retain source documentation literal source_literal_91_4; it is not a model call. Then Evaluate once Path(path) if path is not None else _path; assign in source target order to p. Then For last, assign None; source annotation str | None.
  // Source: vvaharness/util/errlog.py:95-116
  Perform the following protected operations {
    // Source: vvaharness/util/errlog.py:96-114
    Enter source context managers left-to-right: p.open('r', encoding='utf-8') bound to f {
      // Source: vvaharness/util/errlog.py:97-114
      for each ln in f {
        // Source: vvaharness/util/errlog.py:98-98
        In source order: Evaluate once ln.strip(); assign in source target order to ln.
        // Source: vvaharness/util/errlog.py:99-100
        if (the source predicate not ln is truthy) {
          // Source: vvaharness/util/errlog.py:100-100
          Continue the immediately enclosing source loop at its next iteration.
        }
        // Source: vvaharness/util/errlog.py:101-104
        Perform the following protected operations {
          // Source: vvaharness/util/errlog.py:102-102
          In source order: Evaluate once json.loads(ln); assign in source target order to rec.
        }
        // Source: vvaharness/util/errlog.py:103-104
        On the first matching source exception (json.JSONDecodeError, ValueError), in handler order {
          // Source: vvaharness/util/errlog.py:104-104
          Continue the immediately enclosing source loop at its next iteration.
        }
        // Source: vvaharness/util/errlog.py:105-106
        if (the source predicate rec.get('recovered') is True is truthy) {
          // Source: vvaharness/util/errlog.py:106-106
          Continue the immediately enclosing source loop at its next iteration.
        }
        // Source: vvaharness/util/errlog.py:107-107
        In source order: Evaluate once rec.get('stage'); assign in source target order to label.
        // Source: vvaharness/util/errlog.py:108-109
        if (the source predicate not isinstance(label, str) is truthy) {
          // Source: vvaharness/util/errlog.py:109-109
          Continue the immediately enclosing source loop at its next iteration.
        }
        // Source: vvaharness/util/errlog.py:110-114
        if (the source predicate label == stage_id or (label.startswith(stage_id) and (not label[len(stage_id)].isalnum())) is truthy) {
          // Source: vvaharness/util/errlog.py:112-112
          In source order: Evaluate once rec.get('error'); assign in source target order to err.
          // Source: vvaharness/util/errlog.py:113-114
          if (the source predicate isinstance(err, str) is truthy) {
            // Source: vvaharness/util/errlog.py:114-114
            In source order: Evaluate once err; assign in source target order to last.
          }
        }
      }
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
  }
  // Source: vvaharness/util/errlog.py:115-116
  On the first matching source exception OSError, in handler order {
    // Source: vvaharness/util/errlog.py:116-116
    End this invocation with None.
  }
  // Source: vvaharness/util/errlog.py:117-117
  End this invocation with last.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/errlog.py:120-126
// Source signature: already_logged(error: BaseException) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn already_logged(error) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/errlog.py:121-121
  In source order: Retain source documentation literal source_literal_121_4; it is not a model call.
  // Source: vvaharness/util/errlog.py:123-125
  for each err in exception_chain(error) {
    // Source: vvaharness/util/errlog.py:124-125
    if (the source predicate getattr(err, _LOGGED_ATTR, False) is truthy) {
      // Source: vvaharness/util/errlog.py:125-125
      End this invocation with True.
    }
  }
  // Source: vvaharness/util/errlog.py:126-126
  End this invocation with False.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/errlog.py:129-136
// Source signature: _provider_excerpt(error: BaseException) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _provider_excerpt(error) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/errlog.py:130-130
  In source order: Retain source documentation literal source_literal_130_4; it is not a model call.
  // Source: vvaharness/util/errlog.py:132-135
  for each err in exception_chain(error) {
    // Source: vvaharness/util/errlog.py:133-133
    In source order: Evaluate once getattr(err, 'stderr', None); assign in source target order to stderr.
    // Source: vvaharness/util/errlog.py:134-135
    if (the source predicate isinstance(stderr, str) and stderr.strip() is truthy) {
      // Source: vvaharness/util/errlog.py:135-135
      End this invocation with redact(stderr)[-2000:].
    }
  }
  // Source: vvaharness/util/errlog.py:136-136
  End this invocation with None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/errlog.py:139-198
// Source signature: log(stage: str, unit: str, error: BaseException | str, *, recovered: bool=False, **extra) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn log(stage, unit, error, recovered, extra) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/errlog.py:141-141
  In source order: Retain source documentation literal source_literal_141_4; it is not a model call.
  // Source: vvaharness/util/errlog.py:142-166
  if (the source predicate isinstance(error, BaseException) is truthy) {
    // Source: vvaharness/util/errlog.py:143-144
    In source order: Evaluate once source_template_143_14; assign in source target order to msg. Then Evaluate once None; assign in source target order to code.
    // Source: vvaharness/util/errlog.py:145-149
    for each _link in exception_chain(error) {
      // Source: vvaharness/util/errlog.py:146-146
      In source order: Evaluate once getattr(_link, 'error_code', None); assign in source target order to _code.
      // Source: vvaharness/util/errlog.py:147-149
      if (the source predicate isinstance(_code, str) is truthy) {
        // Source: vvaharness/util/errlog.py:148-148
        In source order: Evaluate once _code; assign in source target order to code.
        // Source: vvaharness/util/errlog.py:149-149
        Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
      }
    }
    // Source: vvaharness/util/errlog.py:150-151
    if (the source predicate code is not None and 'error_code' not in extra is truthy) {
      // Source: vvaharness/util/errlog.py:151-151
      In source order: Evaluate once code; assign in source target order to extra['error_code'].
    }
    // Source: vvaharness/util/errlog.py:153-155
    In source order: Evaluate once next((c for c in (getattr(link, 'category', None) for link in exception_chain(error)) if isinstance(c, str)), None); assign in source target order to category.
    // Source: vvaharness/util/errlog.py:156-157
    if (the source predicate category is not None and 'category' not in extra is truthy) {
      // Source: vvaharness/util/errlog.py:157-157
      In source order: Evaluate once category; assign in source target order to extra['category'].
    }
    // Source: vvaharness/util/errlog.py:158-161
    if (the source predicate 'stderr' not in extra is truthy) {
      // Source: vvaharness/util/errlog.py:159-159
      In source order: Evaluate once _provider_excerpt(error); assign in source target order to excerpt.
      // Source: vvaharness/util/errlog.py:160-161
      if (the source predicate excerpt is not None is truthy) {
        // Source: vvaharness/util/errlog.py:161-161
        In source order: Evaluate once excerpt; assign in source target order to extra['stderr'].
      }
    }
    // Source: vvaharness/util/errlog.py:163-164
    In source order: Evaluate once redact(''.join(traceback.format_exception(type(error), error, error.__traceback__)))[-4000:]; assign in source target order to tb.
  }
  else {
    // Source: vvaharness/util/errlog.py:166-166
    In source order: Evaluate once (str(error), None); assign in source target order to (msg, tb).
  }
  // Source: vvaharness/util/errlog.py:168-178
  In source order: Evaluate once redact(msg); assign in source target order to msg. Then Evaluate once {k: redact(v) if isinstance(v, str) else v for k, v in extra.items()}; assign in source target order to safe_extra. Then Evaluate once {'ts': datetime.now(UTC).isoformat(timespec='seconds'), 'stage': stage, 'unit': redact(unit) if isinstance(unit, str) else unit, 'error': msg, **safe_extra}; assign in source target order to rec.
  // Source: vvaharness/util/errlog.py:179-181
  if (the source predicate recovered is truthy) {
    // Source: vvaharness/util/errlog.py:181-181
    In source order: Evaluate once True; assign in source target order to rec['recovered'].
  }
  // Source: vvaharness/util/errlog.py:182-183
  if (the source predicate tb is truthy) {
    // Source: vvaharness/util/errlog.py:183-183
    In source order: Evaluate once tb; assign in source target order to rec['traceback'].
  }
  // Source: vvaharness/util/errlog.py:184-192
  Perform the following protected operations {
    // Source: vvaharness/util/errlog.py:185-188
    Enter source context managers left-to-right: _lock {
      // Source: vvaharness/util/errlog.py:186-188
      Enter source context managers left-to-right: open(_path, 'a', encoding='utf-8', opener=lambda path, flags: os.open(path, flags, 384)) bound to f {
        // Source: vvaharness/util/errlog.py:188-188
        In source order: Evaluate f.write(json.dumps(rec, ensure_ascii=False) + source_literal_188_62); retain side effects and discard the expression result.
      }
      Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
  }
  // Source: vvaharness/util/errlog.py:189-192
  On the first matching source exception Exception as e, in handler order {
    // Source: vvaharness/util/errlog.py:190-191
    In source order: Evaluate _log.warning(Event.ERRLOG_WRITE_FAILED, stage=rec.get('stage'), unit=rec.get('unit'), detail=str(e)); retain side effects and discard the expression result.
    // Source: vvaharness/util/errlog.py:192-192
    End this invocation with None.
  }
  // Source: vvaharness/util/errlog.py:193-198
  if (the source predicate isinstance(error, BaseException) and (not recovered) is truthy) {
    // Source: vvaharness/util/errlog.py:195-198
    Perform the following protected operations {
      // Source: vvaharness/util/errlog.py:196-196
      In source order: Evaluate setattr(error, _LOGGED_ATTR, True); retain side effects and discard the expression result.
    }
    // Source: vvaharness/util/errlog.py:197-198
    On the first matching source exception AttributeError, in handler order {
      // Source: vvaharness/util/errlog.py:198-198
      In source order: Perform no operation at this source statement.
    }
  }
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.util import logs` at source line 18: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import logs` at source line 18: `source_detail/vvaharness/util/logs.py.sudo.md`.
- `from vvaharness.report.redact import redact` at source line 27: `source_detail/vvaharness/report/redact.py.sudo.md`.
- `from vvaharness.util.exceptions import exception_chain` at source line 28: `source_detail/vvaharness/util/exceptions.py.sudo.md`.
- `from vvaharness.util.events import Event` at source line 29: `source_detail/vvaharness/util/events.py.sudo.md`.
