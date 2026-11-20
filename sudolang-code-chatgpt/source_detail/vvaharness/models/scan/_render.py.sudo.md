# vvaharness/models/scan/_render.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/models/scan/_render.py.evidence.json`. SHA-256: `c0d63b3aa97069bde3a98f84ffca9b3817c3579a45f9c085eb6f982ed38b39df`.

```sudo
// Source: vvaharness/models/scan/_render.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import logging; preserve alias and import-time effects. Then Resolve source import import re; preserve alias and import-time effects. Then Evaluate once logging.getLogger(__name__); assign in source target order to log.
// Source: vvaharness/models/scan/_render.py:23-32
In source order: Evaluate once re.compile('^(\\s{0,3})#{1,6}[ \\t]+(.*)$'); assign in source target order to _ATX_HEADING_RX. Then Evaluate once re.compile('^\\s{0,3}(```|~~~)'); assign in source target order to _FENCE_RX. Then Evaluate once re.compile('^\\s{0,3}=+\\s*$'); assign in source target order to _SETEXT_H1_RX. Then Evaluate once re.compile(source_literal_29_4); assign in source target order to _MD_LINEBREAK_RX. Then Evaluate once re.compile(source_template_32_29); assign in source target order to _NEWLINE_RUN_RX.
// Source: vvaharness/models/scan/_render.py:34-43
In source order: Evaluate once re.compile('[\x00-\x08\x0e-\x1f\x7f\xad\u061c\u200b-\u200f\u202a-\u202e\u2060-\u2064\u2066-\u2069\ufeff]'); assign in source target order to _MD_INVISIBLE_RX. Then Evaluate once str.maketrans({'<': '&lt;', '>': '&gt;'}); assign in source target order to _ANGLE_ENTITY. Then Evaluate once re.compile('(`+[^`]*`+)'); assign in source target order to _INLINE_CODE_SPAN_RX.
// Source: vvaharness/models/scan/_render.py:46-87
// Source signature: _demote_md_headings(text, *, escape_angles: bool=False)
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _demote_md_headings(text, escape_angles) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/models/scan/_render.py:47-47
  In source order: Retain source documentation literal source_literal_47_4; it is not a model call.
  // Source: vvaharness/models/scan/_render.py:49-50
  if (the source predicate not text is truthy) {
    // Source: vvaharness/models/scan/_render.py:50-50
    End this invocation with text.
  }
  // Source: vvaharness/models/scan/_render.py:51-55
  In source order: Evaluate once str(text).splitlines(); assign in source target order to lines. Then Evaluate once [False] * len(lines); assign in source target order to fenced. Then For open_idx, assign None; source annotation int | None. Then Evaluate once ''; assign in source target order to marker.
  // Source: vvaharness/models/scan/_render.py:56-65
  for each (i, ln) in enumerate(lines) {
    // Source: vvaharness/models/scan/_render.py:57-57
    In source order: Evaluate once _FENCE_RX.match(ln); assign in source target order to m.
    // Source: vvaharness/models/scan/_render.py:58-59
    if (the source predicate not m is truthy) {
      // Source: vvaharness/models/scan/_render.py:59-59
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/models/scan/_render.py:60-65
    if (the source predicate open_idx is None is truthy) {
      // Source: vvaharness/models/scan/_render.py:61-61
      In source order: Evaluate once (i, m.group(1)); assign in source target order to (open_idx, marker).
    }
    else {
      // Source: vvaharness/models/scan/_render.py:62-65
      if (the source predicate m.group(1) == marker is truthy) {
        // Source: vvaharness/models/scan/_render.py:63-64
        for each j in range(open_idx, i + 1) {
          // Source: vvaharness/models/scan/_render.py:64-64
          In source order: Evaluate once True; assign in source target order to fenced[j].
        }
        // Source: vvaharness/models/scan/_render.py:65-65
        In source order: Evaluate once None; assign in source target order to open_idx.
      }
    }
  }
  // Source: vvaharness/models/scan/_render.py:66-67
  In source order: Evaluate once lines[open_idx] if open_idx is not None else ''; assign in source target order to dangling. Then Evaluate once []; assign in source target order to out.
  // Source: vvaharness/models/scan/_render.py:68-82
  for each (i, ln) in enumerate(lines) {
    // Source: vvaharness/models/scan/_render.py:69-71
    if (the source predicate fenced[i] is truthy) {
      // Source: vvaharness/models/scan/_render.py:70-70
      In source order: Evaluate out.append(ln); retain side effects and discard the expression result.
      // Source: vvaharness/models/scan/_render.py:71-71
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/models/scan/_render.py:72-76
    if (the source predicate escape_angles is truthy) {
      // Source: vvaharness/models/scan/_render.py:74-76
      In source order: Evaluate once _INLINE_CODE_SPAN_RX.split(ln); assign in source target order to parts. Then Evaluate once ''.join((p.translate(_ANGLE_ENTITY) if i % 2 == 0 else p for i, p in enumerate(parts))); assign in source target order to ln.
    }
    // Source: vvaharness/models/scan/_render.py:77-78
    In source order: Evaluate once _ATX_HEADING_RX.sub(lambda m: source_template_78_22, ln); assign in source target order to ln.
    // Source: vvaharness/models/scan/_render.py:80-81
    if (the source predicate _SETEXT_H1_RX.match(ln) and out and out[-1].strip() is truthy) {
      // Source: vvaharness/models/scan/_render.py:81-81
      In source order: Evaluate out.append(''); retain side effects and discard the expression result.
    }
    // Source: vvaharness/models/scan/_render.py:82-82
    In source order: Evaluate out.append(ln); retain side effects and discard the expression result.
  }
  // Source: vvaharness/models/scan/_render.py:83-86
  if (the source predicate dangling is truthy) {
    // Source: vvaharness/models/scan/_render.py:85-86
    In source order: Evaluate once re.match('\\s{0,3}(`{3,}|~{3,})', dangling); assign in source target order to m. Then Evaluate out.append(m.group(1) if m else '```'); retain side effects and discard the expression result.
  }
  // Source: vvaharness/models/scan/_render.py:87-87
  End this invocation with source_literal_87_11.join(out).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/models/scan/_render.py:90-90
In source order: Evaluate once re.compile('`+'); assign in source target order to _TICK_RUN_RX.
// Source: vvaharness/models/scan/_render.py:93-96
// Source signature: _escape_angles(text) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _escape_angles(text) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/models/scan/_render.py:94-94
  In source order: Retain source documentation literal source_literal_94_4; it is not a model call.
  // Source: vvaharness/models/scan/_render.py:96-96
  End this invocation with str(text or '').translate(_ANGLE_ENTITY).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/models/scan/_render.py:99-102
// Source signature: _snippet_fence(code) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _snippet_fence(code) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/models/scan/_render.py:100-101
  In source order: Retain source documentation literal source_literal_100_4; it is not a model call. Then Evaluate once _TICK_RUN_RX.findall(str(code or '')); assign in source target order to runs.
  // Source: vvaharness/models/scan/_render.py:102-102
  End this invocation with '`' * max(3, max((len(r) for r in runs), default=0) + 1).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/models/scan/_render.py:105-113
// Source signature: _code_span(text) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _code_span(text) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/models/scan/_render.py:106-109
  In source order: Retain source documentation literal source_literal_106_4; it is not a model call. Then Evaluate once _MD_INVISIBLE_RX.sub('', _MD_LINEBREAK_RX.sub(' ', str(text or ''))).strip(); assign in source target order to s. Then Evaluate once _TICK_RUN_RX.findall(s); assign in source target order to runs.
  // Source: vvaharness/models/scan/_render.py:110-111
  if (the source predicate not runs is truthy) {
    // Source: vvaharness/models/scan/_render.py:111-111
    End this invocation with source_template_111_15.
  }
  // Source: vvaharness/models/scan/_render.py:112-112
  In source order: Evaluate once '`' * (max((len(r) for r in runs)) + 1); assign in source target order to d.
  // Source: vvaharness/models/scan/_render.py:113-113
  End this invocation with source_template_113_11.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/models/scan/_render.py:117-117
In source order: Evaluate once re.compile('CVSS:3\\.[01]/[A-Za-z:./]+'); assign in source target order to _CVSS_VECTOR_RX.
// Source: vvaharness/models/scan/_render.py:120-124
// Source signature: _vector_span(vec) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _vector_span(vec) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/models/scan/_render.py:121-123
  In source order: Retain source documentation literal source_literal_121_4; it is not a model call. Then Evaluate once str(vec or ''); assign in source target order to v.
  // Source: vvaharness/models/scan/_render.py:124-124
  End this invocation with source_template_124_11 if _CVSS_VECTOR_RX.fullmatch(v) else _code_span(v).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/models/scan/_render.py:127-130
// Source signature: _one_line(text) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _one_line(text) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/models/scan/_render.py:128-128
  In source order: Retain source documentation literal source_literal_128_4; it is not a model call.
  // Source: vvaharness/models/scan/_render.py:130-130
  End this invocation with _NEWLINE_RUN_RX.sub(' ', str(text or '')).strip().
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/models/scan/_render.py:133-135
// Source signature: _confidence_label(confidence: int | None) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _confidence_label(confidence) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/models/scan/_render.py:134-134
  In source order: Retain source documentation literal source_literal_134_4; it is not a model call.
  // Source: vvaharness/models/scan/_render.py:135-135
  End this invocation with source_template_135_11 if confidence is not None else 'not scored'.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/models/scan/_render.py:138-148
// Source signature: _md_cell(text) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _md_cell(text) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/models/scan/_render.py:139-139
  In source order: Retain source documentation literal source_literal_139_4; it is not a model call.
  // Source: vvaharness/models/scan/_render.py:141-142
  if (the source predicate text is None is truthy) {
    // Source: vvaharness/models/scan/_render.py:142-142
    End this invocation with ''.
  }
  // Source: vvaharness/models/scan/_render.py:143-146
  In source order: Evaluate once _MD_LINEBREAK_RX.sub(' ', str(text)); assign in source target order to s. Then Evaluate once _MD_INVISIBLE_RX.sub('', s); assign in source target order to s. Then Evaluate once s.replace('&', '&amp;').translate(_ANGLE_ENTITY); assign in source target order to s.
  // Source: vvaharness/models/scan/_render.py:148-148
  End this invocation with s.replace('\\', '\\\\').replace('|', '\\|').strip().
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/models/scan/_render.py:151-159
// Source signature: _render_repro_block(detail: dict) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _render_repro_block(detail) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/models/scan/_render.py:152-152
  In source order: Retain source documentation literal source_literal_152_4; it is not a model call.
  // Source: vvaharness/models/scan/_render.py:154-159
  Perform the following protected operations {
    // Source: vvaharness/models/scan/_render.py:155-156
    In source order: Resolve source import from vvaharness.exploit_verification.verify.model import ReproDetail; preserve alias and import-time effects. Then Resolve source import from vvaharness.exploit_verification.verify.repro import render_block; preserve alias and import-time effects.
    // Source: vvaharness/models/scan/_render.py:157-157
    End this invocation with render_block(ReproDetail.model_validate(detail)).
  }
  // Source: vvaharness/models/scan/_render.py:158-159
  On the first matching source exception Exception, in handler order {
    // Source: vvaharness/models/scan/_render.py:159-159
    End this invocation with [].
  }
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.exploit_verification.verify.model import ReproDetail` at source line 155: `source_detail/vvaharness/exploit_verification/verify/model.py.sudo.md`.
- `from vvaharness.exploit_verification.verify.repro import render_block` at source line 156: `source_detail/vvaharness/exploit_verification/verify/repro.py.sudo.md`.
