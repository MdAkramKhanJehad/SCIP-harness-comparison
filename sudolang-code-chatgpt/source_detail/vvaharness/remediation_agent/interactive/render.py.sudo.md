# vvaharness/remediation_agent/interactive/render.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/remediation_agent/interactive/render.py.evidence.json`. SHA-256: `21ae707e574fe7d8d3a376e86a71546c0bac829160fde71b713ab7b469e7c691`.

```sudo
// Source: vvaharness/remediation_agent/interactive/render.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import re; preserve alias and import-time effects. Then Evaluate once ('\x1b[32m', '\x1b[36m', '\x1b[2m', '\x1b[7m', '\x1b[0m'); assign in source target order to (_GREEN, _CYAN, _DIM, _INV, _RST).
// Source: vvaharness/remediation_agent/interactive/render.py:24-37
// Source signature: render_rows(findings, *, cursor: int | None=None) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn render_rows(findings, cursor) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/interactive/render.py:25-26
  In source order: Retain source documentation literal source_literal_25_4; it is not a model call. Then Evaluate once []; assign in source target order to rows.
  // Source: vvaharness/remediation_agent/interactive/render.py:27-36
  for each (i, f) in enumerate(findings) {
    // Source: vvaharness/remediation_agent/interactive/render.py:28-29
    In source order: Evaluate once source_template_28_15 if f.done else '  '; assign in source target order to mark. Then Evaluate once source_template_29_15; assign in source target order to line.
    // Source: vvaharness/remediation_agent/interactive/render.py:30-31
    if (the source predicate f.file is truthy) {
      // Source: vvaharness/remediation_agent/interactive/render.py:31-31
      In source order: Apply source augmented assignment line += source_template_31_20 with source evaluation/in-place semantics.
    }
    // Source: vvaharness/remediation_agent/interactive/render.py:32-35
    if (the source predicate cursor is not None and i == cursor is truthy) {
      // Source: vvaharness/remediation_agent/interactive/render.py:33-33
      In source order: Evaluate once source_template_33_19; assign in source target order to line.
    }
    else {
      // Source: vvaharness/remediation_agent/interactive/render.py:35-35
      In source order: Evaluate once source_template_35_19; assign in source target order to line.
    }
    // Source: vvaharness/remediation_agent/interactive/render.py:36-36
    In source order: Evaluate rows.append(line); retain side effects and discard the expression result.
  }
  // Source: vvaharness/remediation_agent/interactive/render.py:37-37
  End this invocation with rows.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/interactive/render.py:40-48
// Source signature: _clear_and_draw(findings, cursor: int, out) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _clear_and_draw(findings, cursor, out) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/interactive/render.py:41-45
  In source order: Evaluate once sum((1 for f in findings if f.done)); assign in source target order to n_done. Then Evaluate out.write('\x1b[2J\x1b[H'); retain side effects and discard the expression result. Then Evaluate out.write(source_template_43_14); retain side effects and discard the expression result. Then Evaluate out.write(source_template_45_14); retain side effects and discard the expression result.
  // Source: vvaharness/remediation_agent/interactive/render.py:46-47
  for each row in render_rows(findings, cursor=cursor) {
    // Source: vvaharness/remediation_agent/interactive/render.py:47-47
    In source order: Evaluate out.write(row + source_literal_47_24); retain side effects and discard the expression result.
  }
  // Source: vvaharness/remediation_agent/interactive/render.py:48-48
  In source order: Evaluate out.flush(); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/interactive/render.py:51-82
// Source signature: parse_selection(text: str, findings) -> list[int] | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn parse_selection(text, findings) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/interactive/render.py:52-53
  In source order: Retain source documentation literal source_literal_52_4; it is not a model call. Then Evaluate once (text or '').strip().lower(); assign in source target order to t.
  // Source: vvaharness/remediation_agent/interactive/render.py:54-55
  if (the source predicate t in ('q', 'quit', 'exit', '') is truthy) {
    // Source: vvaharness/remediation_agent/interactive/render.py:55-55
    End this invocation with None.
  }
  // Source: vvaharness/remediation_agent/interactive/render.py:56-57
  if (the source predicate t == 'all' is truthy) {
    // Source: vvaharness/remediation_agent/interactive/render.py:57-57
    End this invocation with list(range(len(findings))).
  }
  // Source: vvaharness/remediation_agent/interactive/render.py:58-59
  if (the source predicate t == 'pending' is truthy) {
    // Source: vvaharness/remediation_agent/interactive/render.py:59-59
    End this invocation with [i for i, f in enumerate(findings) if not f.done].
  }
  // Source: vvaharness/remediation_agent/interactive/render.py:61-62
  In source order: Evaluate once {f.index: i for i, f in enumerate(findings)}; assign in source target order to by_index. Then For chosen, assign []; source annotation list[int].
  // Source: vvaharness/remediation_agent/interactive/render.py:63-81
  for each tok in re.split('[,\\s]+', t) {
    // Source: vvaharness/remediation_agent/interactive/render.py:64-65
    if (the source predicate not tok is truthy) {
      // Source: vvaharness/remediation_agent/interactive/render.py:65-65
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/remediation_agent/interactive/render.py:66-81
    if (the source predicate '-' in tok is truthy) {
      // Source: vvaharness/remediation_agent/interactive/render.py:67-67
      In source order: Evaluate once tok.partition('-'); assign in source target order to (a, _, b).
      // Source: vvaharness/remediation_agent/interactive/render.py:68-71
      Perform the following protected operations {
        // Source: vvaharness/remediation_agent/interactive/render.py:69-69
        In source order: Evaluate once (int(a), int(b)); assign in source target order to (lo, hi).
      }
      // Source: vvaharness/remediation_agent/interactive/render.py:70-71
      On the first matching source exception ValueError, in handler order {
        // Source: vvaharness/remediation_agent/interactive/render.py:71-71
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/remediation_agent/interactive/render.py:72-74
      for each idx in range(lo, hi + 1) {
        // Source: vvaharness/remediation_agent/interactive/render.py:73-74
        if (the source predicate idx in by_index and by_index[idx] not in chosen is truthy) {
          // Source: vvaharness/remediation_agent/interactive/render.py:74-74
          In source order: Evaluate chosen.append(by_index[idx]); retain side effects and discard the expression result.
        }
      }
    }
    else {
      // Source: vvaharness/remediation_agent/interactive/render.py:76-79
      Perform the following protected operations {
        // Source: vvaharness/remediation_agent/interactive/render.py:77-77
        In source order: Evaluate once int(tok); assign in source target order to idx.
      }
      // Source: vvaharness/remediation_agent/interactive/render.py:78-79
      On the first matching source exception ValueError, in handler order {
        // Source: vvaharness/remediation_agent/interactive/render.py:79-79
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/remediation_agent/interactive/render.py:80-81
      if (the source predicate idx in by_index and by_index[idx] not in chosen is truthy) {
        // Source: vvaharness/remediation_agent/interactive/render.py:81-81
        In source order: Evaluate chosen.append(by_index[idx]); retain side effects and discard the expression result.
      }
    }
  }
  // Source: vvaharness/remediation_agent/interactive/render.py:82-82
  End this invocation with chosen.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

No statically resolved in-checkout import; external calls remain explicit dependency boundaries.
