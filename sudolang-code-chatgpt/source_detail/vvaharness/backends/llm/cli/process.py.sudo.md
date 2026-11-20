# vvaharness/backends/llm/cli/process.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/backends/llm/cli/process.py.evidence.json`. SHA-256: `97783ba9974d48b9784246aa534525730887d65c7ae7f6dfe8fda3ece9454a22`.

```sudo
// Source: vvaharness/backends/llm/cli/process.py:15-20
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import json; preserve alias and import-time effects. Then Resolve source import import os; preserve alias and import-time effects. Then Resolve source import import re; preserve alias and import-time effects.
// Source: vvaharness/backends/llm/cli/process.py:21-26
In source order: Resolve source import import subprocess; preserve alias and import-time effects. Then Resolve source import import sys; preserve alias and import-time effects. Then Resolve source import import threading; preserve alias and import-time effects. Then Resolve source import import time; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm.cli import cancel as _cancel; preserve alias and import-time effects.
// Source: vvaharness/backends/llm/cli/process.py:27-34
In source order: Resolve source import from vvaharness.backends.llm.cli import env as _env; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm.models import TIMEOUT_STOP_GRACE_SECONDS; preserve alias and import-time effects. Then Resolve source import from vvaharness.report.redact import redact; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import console, logs; preserve alias and import-time effects. Then Evaluate once logs.get_logger(__name__); assign in source target order to log.
// Source: vvaharness/backends/llm/cli/process.py:37-108
// Source signature: _run(cmd: list[str], *, input: str | None=None, cwd: str | None=None, timeout: int=600, env: dict | None=None, heartbeat_label: str | None=None, heartbeat_interval: int=300, stream_cb=None, should_stop=None) -> subprocess.CompletedProcess
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _run(cmd, input, cwd, timeout, env, heartbeat_label, heartbeat_interval, stream_cb, should_stop) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli/process.py:44-45
  In source order: Retain source documentation literal source_literal_44_4; it is not a model call. Then Evaluate once {**os.environ, **_env._tls_extra, **(env or {})}; assign in source target order to proc_env.
  // Source: vvaharness/backends/llm/cli/process.py:47-52
  if (the source predicate stream_cb is not None or should_stop is not None is truthy) {
    // Source: vvaharness/backends/llm/cli/process.py:49-52
    End this invocation with _run_streaming(cmd, input=input, cwd=cwd, timeout=timeout, proc_env=proc_env, stream_cb=stream_cb or (lambda _line: None), should_stop=should_stop).
  }
  // Source: vvaharness/backends/llm/cli/process.py:54-56
  In source order: Evaluate once time.monotonic(); assign in source target order to start. Then Evaluate once start + timeout; assign in source target order to deadline. Then Evaluate once input; assign in source target order to pending_input.
  // Source: vvaharness/backends/llm/cli/process.py:58-108
  Enter source context managers left-to-right: subprocess.Popen(cmd, stdin=subprocess.PIPE if input is not None else None, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding='utf-8', errors='replace', cwd=cwd, env=proc_env, **_cancel._NEW_GROUP_KW) bound to proc {
    // Source: vvaharness/backends/llm/cli/process.py:70-71
    Enter source context managers left-to-right: _cancel._LIVE_LOCK {
      // Source: vvaharness/backends/llm/cli/process.py:71-71
      In source order: Evaluate _cancel._LIVE.add(proc); retain side effects and discard the expression result.
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    // Source: vvaharness/backends/llm/cli/process.py:72-106
    Perform the following protected operations {
      // Source: vvaharness/backends/llm/cli/process.py:73-95
      while (the source predicate True is truthy) {
        // Source: vvaharness/backends/llm/cli/process.py:74-77
        if (the source predicate _cancel._ABORT.is_set() is truthy) {
          // Source: vvaharness/backends/llm/cli/process.py:75-76
          In source order: Evaluate _cancel._kill_tree(proc); retain side effects and discard the expression result. Then Evaluate once proc.communicate(); assign in source target order to (out, err).
          // Source: vvaharness/backends/llm/cli/process.py:77-77
          Raise RuntimeError('aborted by user (Ctrl-C)').
        }
        // Source: vvaharness/backends/llm/cli/process.py:78-78
        In source order: Evaluate once deadline - time.monotonic(); assign in source target order to remaining.
        // Source: vvaharness/backends/llm/cli/process.py:79-82
        if (the source predicate remaining <= 0 is truthy) {
          // Source: vvaharness/backends/llm/cli/process.py:80-81
          In source order: Evaluate _cancel._stop_tree(proc, TIMEOUT_STOP_GRACE_SECONDS); retain side effects and discard the expression result. Then Evaluate once proc.communicate(); assign in source target order to (out, err).
          // Source: vvaharness/backends/llm/cli/process.py:82-82
          Raise subprocess.TimeoutExpired(cmd, timeout, output=out, stderr=err).
        }
        // Source: vvaharness/backends/llm/cli/process.py:84-95
        Perform the following protected operations {
          // Source: vvaharness/backends/llm/cli/process.py:85-88
          In source order: Evaluate once proc.communicate(input=pending_input, timeout=min(float(heartbeat_interval), remaining)); assign in source target order to (out, err).
          // Source: vvaharness/backends/llm/cli/process.py:89-89
          Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
        }
        // Source: vvaharness/backends/llm/cli/process.py:90-95
        On the first matching source exception subprocess.TimeoutExpired, in handler order {
          // Source: vvaharness/backends/llm/cli/process.py:91-94
          if (the source predicate heartbeat_label is truthy) {
            // Source: vvaharness/backends/llm/cli/process.py:92-94
            In source order: Evaluate once int(time.monotonic() - start); assign in source target order to elapsed. Then Evaluate console.write(source_template_94_28); retain side effects and discard the expression result.
          }
          // Source: vvaharness/backends/llm/cli/process.py:95-95
          In source order: Evaluate once None; assign in source target order to pending_input.
        }
      }
    }
    // Source: vvaharness/backends/llm/cli/process.py:96-103
    On the first matching source exception KeyboardInterrupt, in handler order {
      // Source: vvaharness/backends/llm/cli/process.py:97-98
      In source order: Evaluate _cancel._ABORT.set(); retain side effects and discard the expression result. Then Evaluate _cancel._kill_tree(proc); retain side effects and discard the expression result.
      // Source: vvaharness/backends/llm/cli/process.py:99-102
      Perform the following protected operations {
        // Source: vvaharness/backends/llm/cli/process.py:100-100
        In source order: Evaluate proc.communicate(timeout=2); retain side effects and discard the expression result.
      }
      // Source: vvaharness/backends/llm/cli/process.py:101-102
      On the first matching source exception Exception, in handler order {
        // Source: vvaharness/backends/llm/cli/process.py:102-102
        In source order: Perform no operation at this source statement.
      }
      // Source: vvaharness/backends/llm/cli/process.py:103-103
      Raise the currently handled exception.
    }
    On every exit from this protected/handler/normal-completion region {
      // Source: vvaharness/backends/llm/cli/process.py:105-106
      Enter source context managers left-to-right: _cancel._LIVE_LOCK {
        // Source: vvaharness/backends/llm/cli/process.py:106-106
        In source order: Evaluate _cancel._LIVE.discard(proc); retain side effects and discard the expression result.
      }
      Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    }
    // Source: vvaharness/backends/llm/cli/process.py:108-108
    End this invocation with subprocess.CompletedProcess(proc.args, proc.returncode, out, err).
  }
  Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cli/process.py:111-202
// Source signature: _run_streaming(cmd: list[str], *, input: str | None, cwd: str | None, timeout: int, proc_env: dict, stream_cb, should_stop=None) -> subprocess.CompletedProcess
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _run_streaming(cmd, input, cwd, timeout, proc_env, stream_cb, should_stop) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli/process.py:115-119
  In source order: Retain source documentation literal source_literal_115_4; it is not a model call. Then For chunks, assign []; source annotation list[str]. Then For err_chunks, assign []; source annotation list[str]. Then Evaluate once threading.Event(); assign in source target order to stopped.
  // Source: vvaharness/backends/llm/cli/process.py:121-138
  // Source signature: _reader(pipe)
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _reader(pipe) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/llm/cli/process.py:122-134
    for each line in iter(pipe.readline, '') {
      // Source: vvaharness/backends/llm/cli/process.py:123-123
      In source order: Evaluate chunks.append(line); retain side effects and discard the expression result.
      // Source: vvaharness/backends/llm/cli/process.py:124-127
      Perform the following protected operations {
        // Source: vvaharness/backends/llm/cli/process.py:125-125
        In source order: Evaluate stream_cb(line); retain side effects and discard the expression result.
      }
      // Source: vvaharness/backends/llm/cli/process.py:126-127
      On the first matching source exception Exception, in handler order {
        // Source: vvaharness/backends/llm/cli/process.py:127-127
        In source order: Perform no operation at this source statement.
      }
      // Source: vvaharness/backends/llm/cli/process.py:128-134
      if (the source predicate should_stop is not None and (not stopped.is_set()) is truthy) {
        // Source: vvaharness/backends/llm/cli/process.py:129-134
        Perform the following protected operations {
          // Source: vvaharness/backends/llm/cli/process.py:130-132
          if (the source predicate should_stop(line) is truthy) {
            // Source: vvaharness/backends/llm/cli/process.py:131-132
            In source order: Evaluate stopped.set(); retain side effects and discard the expression result. Then Evaluate _cancel._kill_tree(proc); retain side effects and discard the expression result.
          }
        }
        // Source: vvaharness/backends/llm/cli/process.py:133-134
        On the first matching source exception Exception, in handler order {
          // Source: vvaharness/backends/llm/cli/process.py:134-134
          In source order: Perform no operation at this source statement.
        }
      }
    }
    // Source: vvaharness/backends/llm/cli/process.py:135-138
    Perform the following protected operations {
      // Source: vvaharness/backends/llm/cli/process.py:136-136
      In source order: Evaluate pipe.close(); retain side effects and discard the expression result.
    }
    // Source: vvaharness/backends/llm/cli/process.py:137-138
    On the first matching source exception Exception, in handler order {
      // Source: vvaharness/backends/llm/cli/process.py:138-138
      In source order: Perform no operation at this source statement.
    }
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/llm/cli/process.py:140-150
  // Source signature: _err_reader(pipe)
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _err_reader(pipe) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/llm/cli/process.py:141-141
    In source order: Retain source documentation literal source_literal_141_8; it is not a model call.
    // Source: vvaharness/backends/llm/cli/process.py:142-146
    Perform the following protected operations {
      // Source: vvaharness/backends/llm/cli/process.py:143-144
      for each line in iter(pipe.readline, '') {
        // Source: vvaharness/backends/llm/cli/process.py:144-144
        In source order: Evaluate err_chunks.append(line); retain side effects and discard the expression result.
      }
    }
    // Source: vvaharness/backends/llm/cli/process.py:145-146
    On the first matching source exception Exception, in handler order {
      // Source: vvaharness/backends/llm/cli/process.py:146-146
      In source order: Perform no operation at this source statement.
    }
    // Source: vvaharness/backends/llm/cli/process.py:147-150
    Perform the following protected operations {
      // Source: vvaharness/backends/llm/cli/process.py:148-148
      In source order: Evaluate pipe.close(); retain side effects and discard the expression result.
    }
    // Source: vvaharness/backends/llm/cli/process.py:149-150
    On the first matching source exception Exception, in handler order {
      // Source: vvaharness/backends/llm/cli/process.py:150-150
      In source order: Perform no operation at this source statement.
    }
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/llm/cli/process.py:152-196
  Enter source context managers left-to-right: subprocess.Popen(cmd, stdin=subprocess.PIPE if input is not None else None, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding='utf-8', errors='replace', cwd=cwd, env=proc_env, bufsize=1, **_cancel._NEW_GROUP_KW) bound to proc {
    // Source: vvaharness/backends/llm/cli/process.py:165-166
    Enter source context managers left-to-right: _cancel._LIVE_LOCK {
      // Source: vvaharness/backends/llm/cli/process.py:166-166
      In source order: Evaluate _cancel._LIVE.add(proc); retain side effects and discard the expression result.
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    // Source: vvaharness/backends/llm/cli/process.py:167-171
    In source order: Evaluate once threading.Thread(target=_reader, args=(proc.stdout,), daemon=True); assign in source target order to reader. Then Evaluate once threading.Thread(target=_err_reader, args=(proc.stderr,), daemon=True); assign in source target order to err_thread. Then Evaluate reader.start(); retain side effects and discard the expression result. Then Evaluate err_thread.start(); retain side effects and discard the expression result.
    // Source: vvaharness/backends/llm/cli/process.py:172-194
    Perform the following protected operations {
      // Source: vvaharness/backends/llm/cli/process.py:173-178
      if (the source predicate input is not None is truthy) {
        // Source: vvaharness/backends/llm/cli/process.py:174-178
        Perform the following protected operations {
          // Source: vvaharness/backends/llm/cli/process.py:175-176
          In source order: Evaluate proc.stdin.write(input); retain side effects and discard the expression result. Then Evaluate proc.stdin.close(); retain side effects and discard the expression result.
        }
        // Source: vvaharness/backends/llm/cli/process.py:177-178
        On the first matching source exception BrokenPipeError, in handler order {
          // Source: vvaharness/backends/llm/cli/process.py:178-178
          In source order: Perform no operation at this source statement.
        }
      }
      // Source: vvaharness/backends/llm/cli/process.py:179-187
      Perform the following protected operations {
        // Source: vvaharness/backends/llm/cli/process.py:180-180
        In source order: Evaluate proc.wait(timeout=timeout); retain side effects and discard the expression result.
      }
      // Source: vvaharness/backends/llm/cli/process.py:181-187
      On the first matching source exception subprocess.TimeoutExpired, in handler order {
        // Source: vvaharness/backends/llm/cli/process.py:182-184
        In source order: Evaluate _cancel._stop_tree(proc, TIMEOUT_STOP_GRACE_SECONDS); retain side effects and discard the expression result. Then Evaluate reader.join(timeout=2); retain side effects and discard the expression result. Then Evaluate err_thread.join(timeout=2); retain side effects and discard the expression result.
        // Source: vvaharness/backends/llm/cli/process.py:185-187
        Raise subprocess.TimeoutExpired(cmd, timeout, output=''.join(chunks), stderr=''.join(err_chunks)).
      }
    }
    // Source: vvaharness/backends/llm/cli/process.py:188-191
    On the first matching source exception KeyboardInterrupt, in handler order {
      // Source: vvaharness/backends/llm/cli/process.py:189-190
      In source order: Evaluate _cancel._ABORT.set(); retain side effects and discard the expression result. Then Evaluate _cancel._kill_tree(proc); retain side effects and discard the expression result.
      // Source: vvaharness/backends/llm/cli/process.py:191-191
      Raise the currently handled exception.
    }
    On every exit from this protected/handler/normal-completion region {
      // Source: vvaharness/backends/llm/cli/process.py:193-194
      Enter source context managers left-to-right: _cancel._LIVE_LOCK {
        // Source: vvaharness/backends/llm/cli/process.py:194-194
        In source order: Evaluate _cancel._LIVE.discard(proc); retain side effects and discard the expression result.
      }
      Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    }
    // Source: vvaharness/backends/llm/cli/process.py:195-196
    In source order: Evaluate reader.join(timeout=5); retain side effects and discard the expression result. Then Evaluate err_thread.join(timeout=5); retain side effects and discard the expression result.
  }
  Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
  // Source: vvaharness/backends/llm/cli/process.py:197-198
  In source order: Evaluate once subprocess.CompletedProcess(cmd, proc.returncode, ''.join(chunks), ''.join(err_chunks)); assign in source target order to result.
  // Source: vvaharness/backends/llm/cli/process.py:199-201
  if (the source predicate stopped.is_set() is truthy) {
    // Source: vvaharness/backends/llm/cli/process.py:201-201
    In source order: Evaluate _WATCHDOG_STOPPED.add(id(result)); retain side effects and discard the expression result.
  }
  // Source: vvaharness/backends/llm/cli/process.py:202-202
  End this invocation with result.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cli/process.py:206-206
In source order: For _WATCHDOG_STOPPED, assign set(); source annotation set[int].
// Source: vvaharness/backends/llm/cli/process.py:209-215
// Source signature: _was_stopped(result: subprocess.CompletedProcess) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _was_stopped(result) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli/process.py:210-211
  In source order: Retain source documentation literal source_literal_210_4; it is not a model call. Then Evaluate once id(result); assign in source target order to key.
  // Source: vvaharness/backends/llm/cli/process.py:212-214
  if (the source predicate key in _WATCHDOG_STOPPED is truthy) {
    // Source: vvaharness/backends/llm/cli/process.py:213-213
    In source order: Evaluate _WATCHDOG_STOPPED.discard(key); retain side effects and discard the expression result.
    // Source: vvaharness/backends/llm/cli/process.py:214-214
    End this invocation with True.
  }
  // Source: vvaharness/backends/llm/cli/process.py:215-215
  End this invocation with False.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cli/process.py:219-219
In source order: Evaluate once re.compile('[\x00-\x1f\x7f-\x9f]'); assign in source target order to _TERMINAL_CONTROL_RX.
// Source: vvaharness/backends/llm/cli/process.py:222-223
// Source signature: _trace_print(text: str, out) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _trace_print(text, out) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli/process.py:223-223
  In source order: Evaluate print(_TERMINAL_CONTROL_RX.sub(' ', text), file=out, flush=True); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cli/process.py:226-266
// Source signature: stream_trace(line: str, *, out=None) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn stream_trace(line, out) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli/process.py:227-229
  In source order: Retain source documentation literal source_literal_227_4; it is not a model call. Then Evaluate once out or sys.stderr; assign in source target order to out. Then Evaluate once (line or '').strip(); assign in source target order to line.
  // Source: vvaharness/backends/llm/cli/process.py:230-231
  if (the source predicate not line is truthy) {
    // Source: vvaharness/backends/llm/cli/process.py:231-231
    End this invocation with None.
  }
  // Source: vvaharness/backends/llm/cli/process.py:232-235
  Perform the following protected operations {
    // Source: vvaharness/backends/llm/cli/process.py:233-233
    In source order: Evaluate once json.loads(line); assign in source target order to evt.
  }
  // Source: vvaharness/backends/llm/cli/process.py:234-235
  On the first matching source exception (json.JSONDecodeError, TypeError), in handler order {
    // Source: vvaharness/backends/llm/cli/process.py:235-235
    End this invocation with None.
  }
  // Source: vvaharness/backends/llm/cli/process.py:236-236
  In source order: Evaluate once evt.get('type'); assign in source target order to etype.
  // Source: vvaharness/backends/llm/cli/process.py:237-266
  if (the source predicate etype == 'assistant' is truthy) {
    // Source: vvaharness/backends/llm/cli/process.py:238-250
    for each blk in (evt.get('message', {}) or {}).get('content', []) or [] {
      // Source: vvaharness/backends/llm/cli/process.py:239-240
      if (the source predicate not isinstance(blk, dict) is truthy) {
        // Source: vvaharness/backends/llm/cli/process.py:240-240
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/backends/llm/cli/process.py:241-250
      if (the source predicate blk.get('type') == 'text' and blk.get('text', '').strip() is truthy) {
        // Source: vvaharness/backends/llm/cli/process.py:242-242
        In source order: Evaluate _trace_print(source_template_242_29, out); retain side effects and discard the expression result.
      }
      else {
        // Source: vvaharness/backends/llm/cli/process.py:243-250
        if (the source predicate blk.get('type') == 'tool_use' is truthy) {
          // Source: vvaharness/backends/llm/cli/process.py:244-247
          In source order: Evaluate once blk.get('name', '?'); assign in source target order to name. Then Evaluate once blk.get('input', {}) or {}; assign in source target order to args. Then Evaluate once ', '.join((source_template_246_33 for k, v in args.items())); assign in source target order to summ. Then Evaluate once redact(summ); assign in source target order to summ.
          // Source: vvaharness/backends/llm/cli/process.py:248-249
          if (the source predicate len(summ) > 160 is truthy) {
            // Source: vvaharness/backends/llm/cli/process.py:249-249
            In source order: Evaluate once summ[:157] + '...'; assign in source target order to summ.
          }
          // Source: vvaharness/backends/llm/cli/process.py:250-250
          In source order: Evaluate _trace_print(source_template_250_29, out); retain side effects and discard the expression result.
        }
      }
    }
  }
  else {
    // Source: vvaharness/backends/llm/cli/process.py:251-266
    if (the source predicate etype == 'user' is truthy) {
      // Source: vvaharness/backends/llm/cli/process.py:253-261
      for each blk in (evt.get('message', {}) or {}).get('content', []) or [] {
        // Source: vvaharness/backends/llm/cli/process.py:254-261
        if (the source predicate isinstance(blk, dict) and blk.get('type') == 'tool_result' is truthy) {
          // Source: vvaharness/backends/llm/cli/process.py:255-255
          In source order: Evaluate once blk.get('content'); assign in source target order to content.
          // Source: vvaharness/backends/llm/cli/process.py:256-259
          if (the source predicate isinstance(content, list) is truthy) {
            // Source: vvaharness/backends/llm/cli/process.py:257-259
            In source order: Evaluate once ' '.join((c.get('text', '') for c in content if isinstance(c, dict))); assign in source target order to content.
          }
          // Source: vvaharness/backends/llm/cli/process.py:260-261
          In source order: Evaluate once len(str(content or '')); assign in source target order to n. Then Evaluate _trace_print(source_template_261_29, out); retain side effects and discard the expression result.
        }
      }
    }
    else {
      // Source: vvaharness/backends/llm/cli/process.py:262-266
      if (the source predicate etype == 'result' is truthy) {
        // Source: vvaharness/backends/llm/cli/process.py:263-266
        if (the source predicate evt.get('is_error') is truthy) {
          // Source: vvaharness/backends/llm/cli/process.py:264-266
          In source order: Evaluate _trace_print(source_template_265_16, out); retain side effects and discard the expression result.
        }
      }
    }
  }
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.backends.llm.cli import cancel as _cancel` at source line 26: `source_detail/vvaharness/backends/llm/cli/__init__.py.sudo.md`.
- `from vvaharness.backends.llm.cli import cancel as _cancel` at source line 26: `source_detail/vvaharness/backends/llm/cli/cancel.py.sudo.md`.
- `from vvaharness.backends.llm.cli import env as _env` at source line 27: `source_detail/vvaharness/backends/llm/cli/__init__.py.sudo.md`.
- `from vvaharness.backends.llm.cli import env as _env` at source line 27: `source_detail/vvaharness/backends/llm/cli/env.py.sudo.md`.
- `from vvaharness.backends.llm.models import TIMEOUT_STOP_GRACE_SECONDS` at source line 28: `source_detail/vvaharness/backends/llm/models.py.sudo.md`.
- `from vvaharness.report.redact import redact` at source line 31: `source_detail/vvaharness/report/redact.py.sudo.md`.
- `from vvaharness.util import console, logs` at source line 32: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import console, logs` at source line 32: `source_detail/vvaharness/util/console.py.sudo.md`.
- `from vvaharness.util import console, logs` at source line 32: `source_detail/vvaharness/util/logs.py.sudo.md`.
