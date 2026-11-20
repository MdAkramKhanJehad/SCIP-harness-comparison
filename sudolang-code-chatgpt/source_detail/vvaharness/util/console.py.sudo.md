# vvaharness/util/console.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/util/console.py.evidence.json`. SHA-256: `413d58633538f7525ccd9d97986f08f19c4b803b7939c999b8e18c6e1a1dfed0`.

```sudo
// Source: vvaharness/util/console.py:15-20
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import os; preserve alias and import-time effects. Then Resolve source import import re; preserve alias and import-time effects. Then Resolve source import import sys; preserve alias and import-time effects.
// Source: vvaharness/util/console.py:21-27
In source order: Resolve source import from typing import Any; preserve alias and import-time effects. Then Resolve source import from rich.console import Console; preserve alias and import-time effects. Then Resolve source import from rich.table import Table; preserve alias and import-time effects. Then Resolve source import from rich.theme import Theme; preserve alias and import-time effects. Then Resolve source import from vvaharness.report.redact import redact; preserve alias and import-time effects.
// Source: vvaharness/util/console.py:29-49
In source order: Evaluate once ['ICON', 'STATUS_STYLE', 'THEME', 'banner', 'console', 'counts', 'mark', 'status_row', 'status_table', 'write']; assign in source target order to __all__. Then For ICON, assign {'ok': '✓', 'warn': '⚠', 'fail': '✗', 'skip': '–'}; source annotation dict[str, str]. Then For STATUS_STYLE, assign {'ok': 'ok', 'warn': 'warn', 'fail': 'fail', 'skip': 'muted'}; source annotation dict[str, str]. Then Evaluate once Theme({'ok': 'bold green', 'warn': 'bold yellow', 'fail': 'bold red', 'muted': 'dim', 'model': 'cyan', 'route': 'magenta', 'heading': 'bold', 'wordmark': 'bold #1434CB', 'wordmark.shadow': '#1434CB', 'wordmark.tag': '#F7B600'}); assign in source target order to THEME. Then Evaluate once 'VVAHARNESS_NO_BANNER'; assign in source target order to NO_BANNER_ENV.
// Source: vvaharness/util/console.py:51-66
In source order: For _WORDMARK, assign ('██╗   ██╗██╗   ██╗ █████╗ ██╗  ██╗', '██║   ██║██║   ██║██╔══██╗██║  ██║', '██║   ██║██║   ██║███████║███████║', '╚██╗ ██╔╝╚██╗ ██╔╝██╔══██║██╔══██║', ' ╚████╔╝  ╚████╔╝ ██║  ██║██║  ██║', '  ╚═══╝    ╚═══╝  ╚═╝  ╚═╝╚═╝  ╚═╝'); source annotation tuple[str, ...]. Then Evaluate once 200; assign in source target order to _PIPED_WIDTH. Then Evaluate once re.compile('[\x00-\x08\x0b-\x1f\x7f-\x9f]'); assign in source target order to _CONTROL_RX.
// Source: vvaharness/util/console.py:69-71
// Source signature: _safe(text: Any) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _safe(text) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/console.py:70-70
  In source order: Retain source documentation literal source_literal_70_4; it is not a model call.
  // Source: vvaharness/util/console.py:71-71
  End this invocation with _CONTROL_RX.sub(' ', redact(str(text))).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/console.py:74-86
// Source signature: console(*, err: bool=True) -> Console
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn console(err) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/console.py:75-77
  In source order: Retain source documentation literal source_literal_75_4; it is not a model call. Then Evaluate once sys.stderr if err else sys.stdout; assign in source target order to stream. Then Evaluate once getattr(stream, 'isatty', None); assign in source target order to isatty.
  // Source: vvaharness/util/console.py:78-86
  End this invocation with Console(file=stream, theme=THEME, no_color=bool(os.environ.get('NO_COLOR')), soft_wrap=False, highlight=False, emoji=False, width=None if callable(isatty) and isatty() else _PIPED_WIDTH).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/console.py:89-97
// Source signature: _encodable(stream: object, lines: tuple[str, ...]) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _encodable(stream, lines) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/console.py:90-91
  In source order: Retain source documentation literal source_literal_90_4; it is not a model call. Then Evaluate once getattr(stream, 'encoding', None) or 'utf-8'; assign in source target order to encoding.
  // Source: vvaharness/util/console.py:92-96
  Perform the following protected operations {
    // Source: vvaharness/util/console.py:93-94
    for each line in lines {
      // Source: vvaharness/util/console.py:94-94
      In source order: Evaluate line.encode(encoding); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/util/console.py:95-96
  On the first matching source exception (LookupError, UnicodeEncodeError), in handler order {
    // Source: vvaharness/util/console.py:96-96
    End this invocation with False.
  }
  // Source: vvaharness/util/console.py:97-97
  End this invocation with True.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/console.py:100-125
// Source signature: banner(*, err: bool=True, force: bool=False) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn banner(err, force) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/console.py:101-107
  In source order: Retain source documentation literal source_literal_101_4; it is not a model call. Then Resolve source import from rich.text import Text; preserve alias and import-time effects. Then Resolve source import from vvaharness import __version__; preserve alias and import-time effects. Then Evaluate once sys.stderr if err else sys.stdout; assign in source target order to stream. Then Evaluate once getattr(stream, 'isatty', None); assign in source target order to isatty.
  // Source: vvaharness/util/console.py:108-110
  if (the source predicate not force and (os.environ.get(NO_BANNER_ENV) or not (callable(isatty) and isatty())) is truthy) {
    // Source: vvaharness/util/console.py:110-110
    End this invocation with False.
  }
  // Source: vvaharness/util/console.py:111-111
  In source order: Evaluate once console(err=err); assign in source target order to out.
  // Source: vvaharness/util/console.py:112-118
  if (the source predicate not _encodable(stream, _WORDMARK) is truthy) {
    // Source: vvaharness/util/console.py:113-113
    In source order: Evaluate out.print(Text('VVAH', style='wordmark'), soft_wrap=True); retain side effects and discard the expression result.
  }
  else {
    // Source: vvaharness/util/console.py:115-115
    In source order: Evaluate out.print(''); retain side effects and discard the expression result.
    // Source: vvaharness/util/console.py:116-118
    for each (row, line) in enumerate(_WORDMARK) {
      // Source: vvaharness/util/console.py:117-118
      In source order: Evaluate out.print(Text(source_template_117_27, style='wordmark' if row < 3 else 'wordmark.shadow'), soft_wrap=True); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/util/console.py:119-123
  In source order: Evaluate once Text('  '); assign in source target order to tag. Then Evaluate tag.append(source_template_120_15, style='wordmark.tag'); retain side effects and discard the expression result. Then Evaluate tag.append('  ·  ', style='muted'); retain side effects and discard the expression result. Then Evaluate tag.append('agentic SAST', style='muted'); retain side effects and discard the expression result. Then Evaluate out.print(tag, soft_wrap=True); retain side effects and discard the expression result.
  // Source: vvaharness/util/console.py:124-124
  In source order: Evaluate out.print(''); retain side effects and discard the expression result.
  // Source: vvaharness/util/console.py:125-125
  End this invocation with True.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/console.py:128-132
// Source signature: write(text: str, *, err: bool=True) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn write(text, err) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/console.py:129-132
  In source order: Retain source documentation literal source_literal_129_4; it is not a model call. Then Resolve source import from rich.text import Text; preserve alias and import-time effects. Then Evaluate console(err=err).print(Text(_safe(text)), soft_wrap=True); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/console.py:135-149
// Source signature: counts(stage: str, label: str, /, **fields: Any) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn counts(stage, label, fields) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/console.py:136-141
  In source order: Retain source documentation literal source_literal_136_4; it is not a model call. Then Resolve source import from rich.text import Text; preserve alias and import-time effects. Then Evaluate once {key: _safe(value) for key, value in fields.items()}; assign in source target order to redacted. Then Evaluate once Text('  '); assign in source target order to line. Then Evaluate line.append(source_template_141_16, style='muted'); retain side effects and discard the expression result.
  // Source: vvaharness/util/console.py:142-142
  In source order: Evaluate line.append(source_template_142_16); retain side effects and discard the expression result.
  // Source: vvaharness/util/console.py:143-147
  for each (i, (key, value)) in enumerate(redacted.items()) {
    // Source: vvaharness/util/console.py:144-145
    if (the source predicate i is truthy) {
      // Source: vvaharness/util/console.py:145-145
      In source order: Evaluate line.append(' · ', style='muted'); retain side effects and discard the expression result.
    }
    // Source: vvaharness/util/console.py:146-147
    In source order: Evaluate line.append(source_template_146_20, style='muted'); retain side effects and discard the expression result. Then Evaluate line.append(source_template_147_20, style='model'); retain side effects and discard the expression result.
  }
  // Source: vvaharness/util/console.py:148-148
  In source order: Evaluate console().print(line, soft_wrap=True); retain side effects and discard the expression result.
  // Source: vvaharness/util/console.py:149-149
  End this invocation with ' '.join((source_template_149_20 for k, v in redacted.items())).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/console.py:152-167
// Source signature: status_table(*, title: str, columns: tuple[str, ...]) -> Table
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn status_table(title, columns) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/console.py:153-164
  In source order: Retain source documentation literal source_literal_153_4; it is not a model call. Then Resolve source import from rich.text import Text; preserve alias and import-time effects. Then Evaluate once Table(title=Text(title), title_justify='left', title_style='heading', box=None, pad_edge=False, show_edge=False, header_style='muted'); assign in source target order to table.
  // Source: vvaharness/util/console.py:165-166
  for each name in columns {
    // Source: vvaharness/util/console.py:166-166
    In source order: Evaluate table.add_column(name, overflow='fold'); retain side effects and discard the expression result.
  }
  // Source: vvaharness/util/console.py:167-167
  End this invocation with table.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/console.py:170-175
// Source signature: status_row(table: Table, outcome: str, *cells: Any) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn status_row(table, outcome, cells) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/console.py:171-175
  In source order: Retain source documentation literal source_literal_171_4; it is not a model call. Then Resolve source import from rich.text import Text; preserve alias and import-time effects. Then Evaluate once Text(ICON.get(outcome, '?'), style=STATUS_STYLE.get(outcome, 'muted')); assign in source target order to glyph. Then Evaluate table.add_row(glyph, *[Text(_safe(c)) for c in cells]); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/console.py:178-185
// Source signature: mark(outcome: str, text: str, *, indent: int=2, lead: str='', err: bool=True) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn mark(outcome, text, indent, lead, err) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/console.py:179-184
  In source order: Retain source documentation literal source_literal_179_4; it is not a model call. Then Resolve source import from rich.text import Text; preserve alias and import-time effects. Then Evaluate once Text(source_template_182_16); assign in source target order to line. Then Evaluate line.append(ICON.get(outcome, '?'), style=STATUS_STYLE.get(outcome, 'muted')); retain side effects and discard the expression result. Then Evaluate line.append(source_template_184_16); retain side effects and discard the expression result.
  // Source: vvaharness/util/console.py:185-185
  In source order: Evaluate console(err=err).print(line, soft_wrap=True); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.report.redact import redact` at source line 27: `source_detail/vvaharness/report/redact.py.sudo.md`.
- `from vvaharness import __version__` at source line 104: `source_detail/vvaharness/__init__.py.sudo.md`.
