# vvaharness/util/logs.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/util/logs.py.evidence.json`. SHA-256: `d831278ac5dc3c0d5209fbf6c2e879836d40859838b74f83856121a765c808a1`.

```sudo
// Source: vvaharness/util/logs.py:15-20
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import logging; preserve alias and import-time effects. Then Resolve source import import os; preserve alias and import-time effects. Then Resolve source import import sys; preserve alias and import-time effects.
// Source: vvaharness/util/logs.py:21-28
In source order: Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from typing import Any; preserve alias and import-time effects. Then Resolve source import import structlog; preserve alias and import-time effects. Then Resolve source import from vvaharness.report.redact import redact; preserve alias and import-time effects. Then Evaluate once ['LEVELS', 'configure', 'get_logger']; assign in source target order to __all__.
// Source: vvaharness/util/logs.py:31-39
In source order: Evaluate once 'vvaharness'; assign in source target order to _ROOT. Then For LEVELS, assign ('critical', 'error', 'warning', 'info', 'debug'); source annotation tuple[str, ...]. Then Evaluate once 'warning'; assign in source target order to _DEFAULT_LEVEL. Then Evaluate once False; assign in source target order to _CLI_MODE.
// Source: vvaharness/util/logs.py:42-49
// Source signature: get_logger(name: str) -> Any
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn get_logger(name) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/logs.py:43-43
  In source order: Retain source documentation literal source_literal_43_4; it is not a model call.
  // Source: vvaharness/util/logs.py:44-49
  End this invocation with structlog.wrap_logger(logging.getLogger(name), processors=[structlog.stdlib.filter_by_level, *_SHARED, _final], wrapper_class=structlog.stdlib.BoundLogger).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/logs.py:52-64
// Source signature: _final(logger: Any, name: str, event: dict[str, Any]) -> Any
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _final(logger, name, event) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/logs.py:53-54
  In source order: Retain source documentation literal source_literal_53_4; it is not a model call.
  // Source: vvaharness/util/logs.py:55-56
  if (the source predicate _CLI_MODE is truthy) {
    // Source: vvaharness/util/logs.py:56-56
    End this invocation with structlog.stdlib.ProcessorFormatter.wrap_for_formatter(logger, name, event).
  }
  // Source: vvaharness/util/logs.py:57-58
  In source order: Evaluate once structlog.stdlib.render_to_log_kwargs(logger, name, event); assign in source target order to kwargs. Then Evaluate once kwargs['extra'].get('exception'); assign in source target order to exc.
  // Source: vvaharness/util/logs.py:59-63
  if (the source predicate exc is truthy) {
    // Source: vvaharness/util/logs.py:62-63
    In source order: Evaluate once source_template_62_24; assign in source target order to kwargs['msg']. Then Evaluate once False; assign in source target order to kwargs['exc_info'].
  }
  // Source: vvaharness/util/logs.py:64-64
  End this invocation with kwargs.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/logs.py:67-80
interface _StderrHandler {
  Describe the source Python type, preserving its base/metaclass expression order: logging.StreamHandler.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/util/logs.py:68-68
  In source order: Retain source documentation literal source_literal_68_4; it is not a model call.
  // Source: vvaharness/util/logs.py:70-72
  // Source signature: __init__(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/util/logs.py:71-72
    In source order: Evaluate logging.Handler.__init__(self); retain side effects and discard the expression result. Then For self._explicit, assign None; source annotation Any.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/util/logs.py:75-76
  // Source: vvaharness/util/logs.py:74-74
  Before creating this callable, evaluate and retain decorators top-to-bottom: property.
  // Source: vvaharness/util/logs.py:75-76
  // Source signature: stream(self) -> Any
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn stream(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/util/logs.py:76-76
    End this invocation with sys.stderr if self._explicit is None else self._explicit.
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vvaharness/util/logs.py:79-80
  // Source: vvaharness/util/logs.py:78-78
  Before creating this callable, evaluate and retain decorators top-to-bottom: stream.setter.
  // Source: vvaharness/util/logs.py:79-80
  // Source signature: stream(self, value: Any) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn stream(self, value) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/util/logs.py:80-80
    In source order: Evaluate once value; assign in source target order to self._explicit.
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
}
// Source: vvaharness/util/logs.py:83-89
// Source signature: _event_code(_logger: Any, _name: str, event: dict[str, Any]) -> dict[str, Any]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _event_code(_logger, _name, event) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/logs.py:84-86
  In source order: Retain source documentation literal source_literal_84_4; it is not a model call. Then Resolve source import from vvaharness.util.events import Event; preserve alias and import-time effects. Then Evaluate once event.get('event'); assign in source target order to ev.
  // Source: vvaharness/util/logs.py:87-88
  if (the source predicate isinstance(ev, Event) is truthy) {
    // Source: vvaharness/util/logs.py:88-88
    In source order: Evaluate once (ev.name, ev.value); assign in source target order to (event['code'], event['event']).
  }
  // Source: vvaharness/util/logs.py:89-89
  End this invocation with event.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/logs.py:92-105
// Source signature: _redact_value(v: Any) -> Any
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _redact_value(v) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/logs.py:93-94
  In source order: Retain source documentation literal source_literal_93_4; it is not a model call.
  // Source: vvaharness/util/logs.py:95-96
  if (the source predicate isinstance(v, str) is truthy) {
    // Source: vvaharness/util/logs.py:96-96
    End this invocation with redact(v).
  }
  // Source: vvaharness/util/logs.py:97-98
  if (the source predicate isinstance(v, (BaseException, os.PathLike)) is truthy) {
    // Source: vvaharness/util/logs.py:98-98
    End this invocation with redact(str(v)).
  }
  // Source: vvaharness/util/logs.py:99-102
  if (the source predicate isinstance(v, (list, tuple, set, frozenset)) is truthy) {
    // Source: vvaharness/util/logs.py:100-100
    In source order: Evaluate once [_redact_value(x) for x in v]; assign in source target order to items.
    // Source: vvaharness/util/logs.py:102-102
    End this invocation with type(v)(*items) if hasattr(v, '_fields') else type(v)(items).
  }
  // Source: vvaharness/util/logs.py:103-104
  if (the source predicate isinstance(v, dict) is truthy) {
    // Source: vvaharness/util/logs.py:104-104
    End this invocation with {k: _redact_value(x) for k, x in v.items()}.
  }
  // Source: vvaharness/util/logs.py:105-105
  End this invocation with v.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/logs.py:108-110
// Source signature: _redact_event(_logger: Any, _name: str, event: dict[str, Any]) -> dict[str, Any]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _redact_event(_logger, _name, event) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/logs.py:109-109
  In source order: Retain source documentation literal source_literal_109_4; it is not a model call.
  // Source: vvaharness/util/logs.py:110-110
  End this invocation with {k: _redact_value(v) for k, v in event.items()}.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/logs.py:113-117
In source order: Evaluate once {'critical': 'FATAL', 'error': 'ERROR', 'warning': 'WARN', 'info': 'INFO', 'debug': 'DEBUG'}; assign in source target order to _TAG. Then Evaluate once {'critical': '1;31', 'error': '31', 'warning': '33', 'info': '36', 'debug': '2'}; assign in source target order to _ANSI. Then Evaluate once '\x1b[0m'; assign in source target order to _RESET. Then Evaluate once ('event', 'level', 'logger', 'timestamp', 'code', 'exc_info', 'exception', 'func_name', 'lineno', 'stack'); assign in source target order to _SKIP.
// Source: vvaharness/util/logs.py:120-125
// Source signature: _abbreviate(dotted: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _abbreviate(dotted) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/logs.py:121-122
  In source order: Retain source documentation literal source_literal_121_4; it is not a model call. Then Evaluate once dotted.split('.'); assign in source target order to parts.
  // Source: vvaharness/util/logs.py:123-124
  if (the source predicate len(parts) < 3 is truthy) {
    // Source: vvaharness/util/logs.py:124-124
    End this invocation with dotted.
  }
  // Source: vvaharness/util/logs.py:125-125
  End this invocation with '.'.join([p[0] for p in parts[:-2]] + parts[-2:]).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/logs.py:128-150
interface _ProductRenderer {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/util/logs.py:129-129
  In source order: Retain source documentation literal source_literal_129_4; it is not a model call.
  // Source: vvaharness/util/logs.py:131-132
  // Source signature: __init__(self, *, colour: bool) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self, colour) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/util/logs.py:132-132
    In source order: Evaluate once colour; assign in source target order to self._colour.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/util/logs.py:134-136
  // Source signature: _paint(self, text: str, level: str) -> str
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _paint(self, text, level) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/util/logs.py:135-135
    In source order: Retain source documentation literal source_literal_135_8; it is not a model call.
    // Source: vvaharness/util/logs.py:136-136
    End this invocation with source_template_136_15 if self._colour else text.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/util/logs.py:138-150
  // Source signature: __call__(self, _logger: Any, _name: str, event: dict[str, Any]) -> str
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __call__(self, _logger, _name, event) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/util/logs.py:139-143
    In source order: Evaluate once str(event.get('level', 'info')); assign in source target order to level. Then Evaluate once str(event.get('timestamp', ''))[11:23]; assign in source target order to clock. Then Evaluate once ' '.join((source_template_141_26 for k in event if k not in _SKIP)); assign in source target order to fields. Then Evaluate once event.get('code'); assign in source target order to code. Then Evaluate once ' '.join((x for x in (fields, source_template_143_44 if code else '') if x)); assign in source target order to tail.
    // Source: vvaharness/util/logs.py:144-146
    In source order: Evaluate once source_template_144_16; assign in source target order to line.
    // Source: vvaharness/util/logs.py:147-148
    if (the source predicate tail is truthy) {
      // Source: vvaharness/util/logs.py:148-148
      In source order: Apply source augmented assignment line += '  ' + self._paint(tail, 'debug') with source evaluation/in-place semantics.
    }
    // Source: vvaharness/util/logs.py:149-149
    In source order: Evaluate once event.get('exception'); assign in source target order to exc.
    // Source: vvaharness/util/logs.py:150-150
    End this invocation with source_template_150_15 if isinstance(exc, str) and exc else line.
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vvaharness/util/logs.py:153-161
// Source signature: _supports_colour(stream: Any) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _supports_colour(stream) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/logs.py:154-154
  In source order: Retain source documentation literal source_literal_154_4; it is not a model call.
  // Source: vvaharness/util/logs.py:155-156
  if (the source predicate os.environ.get('NO_COLOR') or os.environ.get('TERM', '') == 'dumb' is truthy) {
    // Source: vvaharness/util/logs.py:156-156
    End this invocation with False.
  }
  // Source: vvaharness/util/logs.py:157-157
  In source order: Evaluate once getattr(stream, 'isatty', None); assign in source target order to isatty.
  // Source: vvaharness/util/logs.py:158-161
  Perform the following protected operations {
    // Source: vvaharness/util/logs.py:159-159
    End this invocation with bool(callable(isatty) and isatty()).
  }
  // Source: vvaharness/util/logs.py:160-161
  On the first matching source exception (OSError, ValueError), in handler order {
    // Source: vvaharness/util/logs.py:161-161
    End this invocation with False.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/logs.py:164-177
In source order: For _SHARED, assign (structlog.contextvars.merge_contextvars, structlog.stdlib.add_log_level, structlog.stdlib.add_logger_name, structlog.processors.TimeStamper(fmt='iso', utc=True), structlog.processors.StackInfoRenderer(), structlog.processors.format_exc_info, structlog.processors.CallsiteParameterAdder([structlog.processors.CallsiteParameter.FUNC_NAME]), structlog.processors.UnicodeDecoder(), structlog.stdlib.PositionalArgumentsFormatter(), _event_code, _redact_event); source annotation tuple[Any, ...].
// Source: vvaharness/util/logs.py:180-203
// Source signature: configure(level: str | None=None, path: str | Path | None=None) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn configure(level, path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/logs.py:181-185
  In source order: Retain source documentation literal source_literal_181_4; it is not a model call. Then Bind names in module scope: _CLI_MODE. Then Evaluate once (level or os.environ.get('VVAHARNESS_LOG_LEVEL') or '').strip().lower(); assign in source target order to asked. Then Evaluate once asked or _DEFAULT_LEVEL; assign in source target order to chosen. Then Evaluate once getattr(logging, chosen.upper(), None); assign in source target order to numeric.
  // Source: vvaharness/util/logs.py:186-189
  if (the source predicate not isinstance(numeric, int) is truthy) {
    // Source: vvaharness/util/logs.py:187-189
    In source order: Evaluate print(source_template_187_14, file=sys.stderr); retain side effects and discard the expression result. Then Evaluate once (logging.WARNING, ''); assign in source target order to (numeric, asked).
  }
  // Source: vvaharness/util/logs.py:191-191
  In source order: Evaluate once logging.getLogger(_ROOT); assign in source target order to log.
  // Source: vvaharness/util/logs.py:192-194
  for each existing in [h for h in log.handlers if getattr(h, '_vvaharness', False)] {
    // Source: vvaharness/util/logs.py:193-194
    In source order: Evaluate log.removeHandler(existing); retain side effects and discard the expression result. Then Evaluate existing.close(); retain side effects and discard the expression result.
  }
  // Source: vvaharness/util/logs.py:195-198
  for each handler in _handlers(path or os.environ.get('VVAHARNESS_LOG_FILE')) {
    // Source: vvaharness/util/logs.py:196-198
    In source order: Evaluate handler.setFormatter(_formatter(handler)); retain side effects and discard the expression result. Then Evaluate once True; assign in source target order to handler._vvaharness. Then Evaluate log.addHandler(handler); retain side effects and discard the expression result.
  }
  // Source: vvaharness/util/logs.py:199-202
  In source order: Evaluate log.setLevel(numeric); retain side effects and discard the expression result. Then Evaluate once False; assign in source target order to log.propagate. Then Evaluate once True; assign in source target order to _CLI_MODE.
  // Source: vvaharness/util/logs.py:203-203
  End this invocation with bool(asked).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/logs.py:206-216
// Source signature: _formatter(handler: logging.Handler) -> logging.Formatter
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _formatter(handler) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/logs.py:207-208
  In source order: Retain source documentation literal source_literal_207_4; it is not a model call. Then For renderer, declare without assigning a value; source annotation Any.
  // Source: vvaharness/util/logs.py:209-212
  if (the source predicate isinstance(handler, logging.FileHandler) is truthy) {
    // Source: vvaharness/util/logs.py:210-210
    In source order: Evaluate once structlog.processors.JSONRenderer(); assign in source target order to renderer.
  }
  else {
    // Source: vvaharness/util/logs.py:212-212
    In source order: Evaluate once _ProductRenderer(colour=_supports_colour(getattr(handler, 'stream', None))); assign in source target order to renderer.
  }
  // Source: vvaharness/util/logs.py:213-216
  End this invocation with structlog.stdlib.ProcessorFormatter(foreign_pre_chain=list(_SHARED), processors=[structlog.stdlib.ProcessorFormatter.remove_processors_meta, renderer]).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/logs.py:219-235
// Source signature: _handlers(path: str | Path | None) -> list[logging.Handler]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _handlers(path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/logs.py:220-223
  In source order: Retain source documentation literal source_literal_220_4; it is not a model call. Then Evaluate once _StderrHandler(); assign in source target order to stderr.
  // Source: vvaharness/util/logs.py:224-225
  if (the source predicate not path is truthy) {
    // Source: vvaharness/util/logs.py:225-225
    End this invocation with [stderr].
  }
  // Source: vvaharness/util/logs.py:226-233
  Perform the following protected operations {
    // Source: vvaharness/util/logs.py:227-229
    In source order: Evaluate once Path(path); assign in source target order to dest. Then Evaluate dest.parent.mkdir(parents=True, exist_ok=True); retain side effects and discard the expression result. Then For file_handler, assign logging.FileHandler(dest, encoding='utf-8'); source annotation logging.Handler.
  }
  // Source: vvaharness/util/logs.py:230-233
  On the first matching source exception OSError as exc, in handler order {
    // Source: vvaharness/util/logs.py:231-232
    In source order: Evaluate print(source_template_231_14, file=sys.stderr); retain side effects and discard the expression result.
    // Source: vvaharness/util/logs.py:233-233
    End this invocation with [stderr].
  }
  // Source: vvaharness/util/logs.py:234-234
  In source order: Evaluate stderr.setLevel(logging.WARNING); retain side effects and discard the expression result.
  // Source: vvaharness/util/logs.py:235-235
  End this invocation with [stderr, file_handler].
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.report.redact import redact` at source line 26: `source_detail/vvaharness/report/redact.py.sudo.md`.
- `from vvaharness.util.events import Event` at source line 85: `source_detail/vvaharness/util/events.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../prompt_representation/vvaharness/util/logs.py.sudo.md). Exact strings in the evidence asset support this conversion.
