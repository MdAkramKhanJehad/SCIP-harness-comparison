# vvaharness/detect/matcher.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/detect/matcher.py.evidence.json`. SHA-256: `8904d4e9f2896e181b15adfde372402d84512c27df69e542f8948deeb3e8f48b`.

```sudo
// Source: vvaharness/detect/matcher.py:15-20
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import re; preserve alias and import-time effects. Then Resolve source import from dataclasses import dataclass, field; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects.
// Source: vvaharness/detect/matcher.py:22-24
In source order: Resolve source import from vvaharness.detect.spec import MatchSpec; preserve alias and import-time effects. Then Evaluate once 120; assign in source target order to _SNIPPET_MAX.
// Source: vvaharness/detect/matcher.py:28-36
// Source: vvaharness/detect/matcher.py:27-27
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vvaharness/detect/matcher.py:28-36
interface Hit {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/detect/matcher.py:29-34
  In source order: Retain source documentation literal source_literal_29_4; it is not a model call. Then For file, declare without assigning a value; source annotation str. Then For line, declare without assigning a value; source annotation int. Then For spec, declare without assigning a value; source annotation MatchSpec. Then For snippet, declare without assigning a value; source annotation str.
  // Source: vvaharness/detect/matcher.py:36-36
  In source order: For line_end, assign 0; source annotation int.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vvaharness/detect/matcher.py:39-40
// Source signature: _compiled(specs: list[MatchSpec]) -> list[tuple[MatchSpec, re.Pattern[str]]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _compiled(specs) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/detect/matcher.py:40-40
  End this invocation with [(spec, re.compile(spec.pattern)) for spec in specs].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/detect/matcher.py:43-49
// Source signature: split_lines(text: str) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn split_lines(text) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/detect/matcher.py:44-46
  In source order: Retain source documentation literal source_literal_44_4; it is not a model call. Then Evaluate once text.split(source_literal_46_21); assign in source target order to out.
  // Source: vvaharness/detect/matcher.py:47-48
  if (the source predicate out and out[-1] == '' is truthy) {
    // Source: vvaharness/detect/matcher.py:48-48
    In source order: Evaluate out.pop(); retain side effects and discard the expression result.
  }
  // Source: vvaharness/detect/matcher.py:49-49
  End this invocation with [ln.removesuffix('\r') for ln in out].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/detect/matcher.py:52-57
// Source signature: _read_text(repo_root: Path, rel_path: str) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _read_text(repo_root, rel_path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/detect/matcher.py:53-53
  In source order: Evaluate once repo_root / rel_path; assign in source target order to full.
  // Source: vvaharness/detect/matcher.py:54-57
  Perform the following protected operations {
    // Source: vvaharness/detect/matcher.py:55-55
    End this invocation with full.read_text(encoding='utf-8', errors='replace').
  }
  // Source: vvaharness/detect/matcher.py:56-57
  On the first matching source exception OSError, in handler order {
    // Source: vvaharness/detect/matcher.py:57-57
    End this invocation with None.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/detect/matcher.py:60-74
// Source signature: scan_file(repo_root: Path, rel_path: str, compiled: list[tuple[MatchSpec, re.Pattern[str]]]) -> list[Hit]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn scan_file(repo_root, rel_path, compiled) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/detect/matcher.py:65-66
  In source order: Retain source documentation literal source_literal_65_4; it is not a model call. Then Evaluate once _read_text(repo_root, rel_path); assign in source target order to text.
  // Source: vvaharness/detect/matcher.py:67-68
  if (the source predicate text is None is truthy) {
    // Source: vvaharness/detect/matcher.py:68-68
    End this invocation with [].
  }
  // Source: vvaharness/detect/matcher.py:69-69
  In source order: For hits, assign []; source annotation list[Hit].
  // Source: vvaharness/detect/matcher.py:70-73
  for each (line_no, line) in enumerate(split_lines(text), start=1) {
    // Source: vvaharness/detect/matcher.py:71-73
    for each (spec, rx) in compiled {
      // Source: vvaharness/detect/matcher.py:72-73
      if (the source predicate rx.search(line) is truthy) {
        // Source: vvaharness/detect/matcher.py:73-73
        In source order: Evaluate hits.append(Hit(rel_path, line_no, spec, line.strip()[:_SNIPPET_MAX])); retain side effects and discard the expression result.
      }
    }
  }
  // Source: vvaharness/detect/matcher.py:74-74
  End this invocation with hits.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/detect/matcher.py:77-83
// Source signature: scan_files(repo_root: Path, rel_paths: list[str], specs: list[MatchSpec]) -> list[Hit]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn scan_files(repo_root, rel_paths, specs) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/detect/matcher.py:78-80
  In source order: Retain source documentation literal source_literal_78_4; it is not a model call. Then Evaluate once _compiled(specs); assign in source target order to compiled. Then For hits, assign []; source annotation list[Hit].
  // Source: vvaharness/detect/matcher.py:81-82
  for each rel_path in rel_paths {
    // Source: vvaharness/detect/matcher.py:82-82
    In source order: Evaluate hits.extend(scan_file(repo_root, rel_path, compiled)); retain side effects and discard the expression result.
  }
  // Source: vvaharness/detect/matcher.py:83-83
  End this invocation with hits.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/detect/matcher.py:90-99
// Source: vvaharness/detect/matcher.py:89-89
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vvaharness/detect/matcher.py:90-99
interface CompiledDetector {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/detect/matcher.py:91-96
  In source order: Retain source documentation literal source_literal_91_4; it is not a model call. Then For spec, declare without assigning a value; source annotation MatchSpec. Then For pattern, declare without assigning a value; source annotation re.Pattern[str]. Then For present, declare without assigning a value; source annotation re.Pattern[str] | None. Then For absent, declare without assigning a value; source annotation re.Pattern[str] | None.
  // Source: vvaharness/detect/matcher.py:97-99
  In source order: For file_gate, declare without assigning a value; source annotation re.Pattern[str] | None. Then For near, declare without assigning a value; source annotation re.Pattern[str] | None. Then For span_end, declare without assigning a value; source annotation re.Pattern[str] | None.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vvaharness/detect/matcher.py:102-116
// Source signature: compile_detectors(specs: list[MatchSpec]) -> list[CompiledDetector]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn compile_detectors(specs) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/detect/matcher.py:103-103
  In source order: Retain source documentation literal source_literal_103_4; it is not a model call.
  // Source: vvaharness/detect/matcher.py:104-105
  // Source signature: _rx(pat: str) -> re.Pattern[str] | None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _rx(pat) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/detect/matcher.py:105-105
    End this invocation with re.compile(pat) if pat else None.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/detect/matcher.py:107-116
  End this invocation with [CompiledDetector(spec=s, pattern=re.compile(s.pattern), present=_rx(s.present_re), absent=_rx(s.absent_re), file_gate=_rx(s.file_re), near=_rx(s.near_re), span_end=_rx(s.span_end)) for s in specs if s.role == 'detector' and s.enabled].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/detect/matcher.py:120-131
In source order: Evaluate once re.compile('"""(?:\\\\.|[^\\\\])*?"""|\'\'\'(?:\\\\.|[^\\\\])*?\'\'\'|\\"\\"\\"|\'\'\'|\\"(?:\\\\.|[^\\"\\\\])*\\"?|\'(?:\\\\.|[^\'\\\\])*\'?'); assign in source target order to _STRING_LITERAL_RX. Then Evaluate once {'"""': re.compile('(?:\\\\.|[^\\\\])*?"""'), "'''": re.compile("(?:\\\\.|[^\\\\])*?'''")}; assign in source target order to _TRIPLE_CLOSE.
// Source: vvaharness/detect/matcher.py:134-159
// Source signature: _mask_strings(seg: str, in_triple: str='') -> tuple[str, str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _mask_strings(seg, in_triple) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/detect/matcher.py:135-138
  In source order: Retain source documentation literal source_literal_135_4; it is not a model call. Then For out, assign []; source annotation list[str]. Then Evaluate once 0; assign in source target order to pos.
  // Source: vvaharness/detect/matcher.py:139-145
  if (the source predicate in_triple is truthy) {
    // Source: vvaharness/detect/matcher.py:140-140
    In source order: Evaluate once _TRIPLE_CLOSE[in_triple].match(seg); assign in source target order to m.
    // Source: vvaharness/detect/matcher.py:141-142
    if (the source predicate m is None is truthy) {
      // Source: vvaharness/detect/matcher.py:142-142
      End this invocation with (' ' * len(seg), in_triple).
    }
    // Source: vvaharness/detect/matcher.py:143-145
    In source order: Evaluate out.append(' ' * m.end()); retain side effects and discard the expression result. Then Evaluate once m.end(); assign in source target order to pos. Then Evaluate once ''; assign in source target order to in_triple.
  }
  // Source: vvaharness/detect/matcher.py:146-158
  while (the source predicate True is truthy) {
    // Source: vvaharness/detect/matcher.py:147-147
    In source order: Evaluate once _STRING_LITERAL_RX.search(seg, pos); assign in source target order to m.
    // Source: vvaharness/detect/matcher.py:148-150
    if (the source predicate m is None is truthy) {
      // Source: vvaharness/detect/matcher.py:149-149
      In source order: Evaluate out.append(seg[pos:]); retain side effects and discard the expression result.
      // Source: vvaharness/detect/matcher.py:150-150
      Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
    }
    // Source: vvaharness/detect/matcher.py:151-152
    In source order: Evaluate out.append(seg[pos:m.start()]); retain side effects and discard the expression result. Then Evaluate once m.group(0); assign in source target order to tok.
    // Source: vvaharness/detect/matcher.py:153-156
    if (the source predicate tok in ('"""', "'''") is truthy) {
      // Source: vvaharness/detect/matcher.py:154-155
      In source order: Evaluate out.append(' ' * (len(seg) - m.start())); retain side effects and discard the expression result. Then Evaluate once tok; assign in source target order to in_triple.
      // Source: vvaharness/detect/matcher.py:156-156
      Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
    }
    // Source: vvaharness/detect/matcher.py:157-158
    In source order: Evaluate out.append(' ' * len(tok)); retain side effects and discard the expression result. Then Evaluate once m.end(); assign in source target order to pos.
  }
  // Source: vvaharness/detect/matcher.py:159-159
  End this invocation with (''.join(out), in_triple).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/detect/matcher.py:162-181
// Source signature: _call_span(lines: list[str], idx: int, col: int, max_lines: int) -> tuple[str, int] | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _call_span(lines, idx, col, max_lines) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/detect/matcher.py:164-168
  In source order: Retain source documentation literal source_literal_164_4; it is not a model call. Then Evaluate once 0; assign in source target order to depth. Then For parts, assign []; source annotation list[str]. Then Evaluate once ''; assign in source target order to in_triple.
  // Source: vvaharness/detect/matcher.py:169-180
  for each i in range(idx, min(idx + max_lines, len(lines))) {
    // Source: vvaharness/detect/matcher.py:170-171
    In source order: Evaluate once lines[i][col:] if i == idx else lines[i]; assign in source target order to seg. Then Evaluate once _mask_strings(seg, in_triple); assign in source target order to (masked, in_triple).
    // Source: vvaharness/detect/matcher.py:172-179
    for each (j, ch) in enumerate(masked) {
      // Source: vvaharness/detect/matcher.py:173-179
      if (the source predicate ch == '(' is truthy) {
        // Source: vvaharness/detect/matcher.py:174-174
        In source order: Apply source augmented assignment depth += 1 with source evaluation/in-place semantics.
      }
      else {
        // Source: vvaharness/detect/matcher.py:175-179
        if (the source predicate ch == ')' is truthy) {
          // Source: vvaharness/detect/matcher.py:176-176
          In source order: Apply source augmented assignment depth -= 1 with source evaluation/in-place semantics.
          // Source: vvaharness/detect/matcher.py:177-179
          if (the source predicate depth == 0 is truthy) {
            // Source: vvaharness/detect/matcher.py:178-178
            In source order: Evaluate parts.append(seg[:j + 1]); retain side effects and discard the expression result.
            // Source: vvaharness/detect/matcher.py:179-179
            End this invocation with (source_literal_179_27.join(parts), i + 1).
          }
        }
      }
    }
    // Source: vvaharness/detect/matcher.py:180-180
    In source order: Evaluate parts.append(seg); retain side effects and discard the expression result.
  }
  // Source: vvaharness/detect/matcher.py:181-181
  End this invocation with None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/detect/matcher.py:184-193
// Source signature: _block_span(lines: list[str], idx: int, col: int, end_rx: re.Pattern[str], max_lines: int) -> tuple[str, int] | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _block_span(lines, idx, col, end_rx, max_lines) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/detect/matcher.py:186-187
  In source order: Retain source documentation literal source_literal_186_4; it is not a model call. Then For parts, assign []; source annotation list[str].
  // Source: vvaharness/detect/matcher.py:188-192
  for each i in range(idx, min(idx + max_lines, len(lines))) {
    // Source: vvaharness/detect/matcher.py:189-190
    In source order: Evaluate once lines[i][col:] if i == idx else lines[i]; assign in source target order to seg. Then Evaluate parts.append(seg); retain side effects and discard the expression result.
    // Source: vvaharness/detect/matcher.py:191-192
    if (the source predicate end_rx.search(seg) is truthy) {
      // Source: vvaharness/detect/matcher.py:192-192
      End this invocation with (source_literal_192_19.join(parts), i + 1).
    }
  }
  // Source: vvaharness/detect/matcher.py:193-193
  End this invocation with None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/detect/matcher.py:196-204
// Source signature: _span_for(det: CompiledDetector, lines: list[str], idx: int, col: int) -> tuple[str, int] | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _span_for(det, lines, idx, col) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/detect/matcher.py:198-199
  In source order: Retain source documentation literal source_literal_198_4; it is not a model call. Then Evaluate once det.spec; assign in source target order to spec.
  // Source: vvaharness/detect/matcher.py:200-201
  if (the source predicate spec.span == 'call' is truthy) {
    // Source: vvaharness/detect/matcher.py:201-201
    End this invocation with _call_span(lines, idx, col, max(1, spec.span_max_lines)).
  }
  // Source: vvaharness/detect/matcher.py:202-203
  if (the source predicate spec.span == 'block' and det.span_end is not None is truthy) {
    // Source: vvaharness/detect/matcher.py:203-203
    End this invocation with _block_span(lines, idx, col, det.span_end, max(1, spec.span_max_lines)).
  }
  // Source: vvaharness/detect/matcher.py:204-204
  End this invocation with (lines[idx], idx + 1).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/detect/matcher.py:207-216
// Source signature: _guard_text(det: CompiledDetector, lines: list[str], idx: int, body: str, end_line: int) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _guard_text(det, lines, idx, body, end_line) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/detect/matcher.py:209-211
  In source order: Retain source documentation literal source_literal_209_4; it is not a model call. Then Evaluate once det.spec.absent_window; assign in source target order to window.
  // Source: vvaharness/detect/matcher.py:212-213
  if (the source predicate window <= 0 is truthy) {
    // Source: vvaharness/detect/matcher.py:213-213
    End this invocation with body.
  }
  // Source: vvaharness/detect/matcher.py:214-215
  In source order: Evaluate once max(0, idx - window); assign in source target order to lo. Then Evaluate once min(len(lines), end_line + window); assign in source target order to hi.
  // Source: vvaharness/detect/matcher.py:216-216
  End this invocation with source_literal_216_11.join(lines[lo:hi]).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/detect/matcher.py:219-225
// Source signature: _near_ok(det: CompiledDetector, lines: list[str], idx: int) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _near_ok(det, lines, idx) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/detect/matcher.py:220-220
  In source order: Retain source documentation literal source_literal_220_4; it is not a model call.
  // Source: vvaharness/detect/matcher.py:221-222
  if (the source predicate det.near is None is truthy) {
    // Source: vvaharness/detect/matcher.py:222-222
    End this invocation with True.
  }
  // Source: vvaharness/detect/matcher.py:223-224
  In source order: Evaluate once max(0, idx - det.spec.near_window); assign in source target order to lo. Then Evaluate once min(len(lines), idx + det.spec.near_window + 1); assign in source target order to hi.
  // Source: vvaharness/detect/matcher.py:225-225
  End this invocation with bool(det.near.search(source_literal_225_32.join(lines[lo:hi]))).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/detect/matcher.py:229-229
In source order: Evaluate once tuple[str, str, int, int, int]; assign in source target order to _SpanKey.
// Source: vvaharness/detect/matcher.py:232-239
// Source signature: _live_detectors(lines: list[str], detectors: list[CompiledDetector]) -> list[CompiledDetector]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _live_detectors(lines, detectors) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/detect/matcher.py:234-234
  In source order: Retain source documentation literal source_literal_234_4; it is not a model call.
  // Source: vvaharness/detect/matcher.py:235-236
  if (the source predicate not any((d.file_gate is not None for d in detectors)) is truthy) {
    // Source: vvaharness/detect/matcher.py:236-236
    End this invocation with detectors.
  }
  // Source: vvaharness/detect/matcher.py:237-237
  In source order: Evaluate once source_literal_237_11.join(lines); assign in source target order to text.
  // Source: vvaharness/detect/matcher.py:238-239
  End this invocation with [d for d in detectors if d.file_gate is None or d.file_gate.search(text)].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/detect/matcher.py:243-283
// Source: vvaharness/detect/matcher.py:242-242
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass.
// Source: vvaharness/detect/matcher.py:243-283
interface _FileScan {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/detect/matcher.py:244-248
  In source order: Retain source documentation literal source_literal_244_4; it is not a model call. Then For rel_path, declare without assigning a value; source annotation str. Then For lines, declare without assigning a value; source annotation list[str]. Then For spans, assign field(default_factory=dict); source annotation dict[_SpanKey, tuple[str, int] | None].
  // Source: vvaharness/detect/matcher.py:250-256
  // Source signature: _span(self, det: CompiledDetector, idx: int, start: int) -> tuple[str, int] | None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _span(self, det, idx, start) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/detect/matcher.py:252-253
    In source order: Retain source documentation literal source_literal_252_8; it is not a model call. Then Evaluate once (det.spec.span, det.spec.span_end, det.spec.span_max_lines, idx, start); assign in source target order to key.
    // Source: vvaharness/detect/matcher.py:254-255
    if (the source predicate key not in self.spans is truthy) {
      // Source: vvaharness/detect/matcher.py:255-255
      In source order: Evaluate once _span_for(det, self.lines, idx, start); assign in source target order to self.spans[key].
    }
    // Source: vvaharness/detect/matcher.py:256-256
    End this invocation with self.spans[key].
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/detect/matcher.py:258-264
  // Source signature: _rejected(self, det: CompiledDetector, idx: int, body: str, end_line: int) -> bool
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _rejected(self, det, idx, body, end_line) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/detect/matcher.py:260-260
    In source order: Retain source documentation literal source_literal_260_8; it is not a model call.
    // Source: vvaharness/detect/matcher.py:261-264
    End this invocation with det.present is not None and (not det.present.search(body)) or (det.absent is not None and bool(det.absent.search(_guard_text(det, self.lines, idx, body, end_line)))) or (not _near_ok(det, self.lines, idx)).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/detect/matcher.py:266-276
  // Source signature: hit(self, det: CompiledDetector, idx: int, line: str, start: int) -> Hit | None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn hit(self, det, idx, line, start) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/detect/matcher.py:268-269
    In source order: Retain source documentation literal source_literal_268_8; it is not a model call. Then Evaluate once self._span(det, idx, start); assign in source target order to span.
    // Source: vvaharness/detect/matcher.py:270-271
    if (the source predicate span is None is truthy) {
      // Source: vvaharness/detect/matcher.py:271-271
      End this invocation with None.
    }
    // Source: vvaharness/detect/matcher.py:272-272
    In source order: Evaluate once span; assign in source target order to (body, end_line).
    // Source: vvaharness/detect/matcher.py:273-274
    if (the source predicate self._rejected(det, idx, body, end_line) is truthy) {
      // Source: vvaharness/detect/matcher.py:274-274
      End this invocation with None.
    }
    // Source: vvaharness/detect/matcher.py:275-276
    End this invocation with Hit(self.rel_path, idx + 1, det.spec, line.strip()[:_SNIPPET_MAX], end_line).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/detect/matcher.py:278-283
  // Source signature: line_hits(self, live: list[CompiledDetector], idx: int, line: str) -> list[Hit]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn line_hits(self, live, idx, line) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/detect/matcher.py:280-281
    In source order: Retain source documentation literal source_literal_280_8; it is not a model call. Then Evaluate once ((det, det.pattern.search(line)) for det in live); assign in source target order to found.
    // Source: vvaharness/detect/matcher.py:282-283
    End this invocation with [hit for det, m in found if m is not None if (hit := self.hit(det, idx, line, m.start())) is not None].
    If execution reaches this end, finish with the source implicit None result.
  }
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vvaharness/detect/matcher.py:286-300
// Source signature: detector_hits(rel_path: str, lines: list[str], detectors: list[CompiledDetector]) -> list[Hit]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn detector_hits(rel_path, lines, detectors) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/detect/matcher.py:288-289
  In source order: Retain source documentation literal source_literal_288_4; it is not a model call. Then Evaluate once _live_detectors(lines, detectors) if detectors else []; assign in source target order to live.
  // Source: vvaharness/detect/matcher.py:290-291
  if (the source predicate not live is truthy) {
    // Source: vvaharness/detect/matcher.py:291-291
    End this invocation with [].
  }
  // Source: vvaharness/detect/matcher.py:293-295
  In source order: Evaluate once rel_path.endswith('.py'); assign in source target order to skip_comments. Then Evaluate once _FileScan(rel_path, lines); assign in source target order to scan. Then For hits, assign []; source annotation list[Hit].
  // Source: vvaharness/detect/matcher.py:296-299
  for each (idx, line) in enumerate(lines) {
    // Source: vvaharness/detect/matcher.py:297-298
    if (the source predicate skip_comments and line.lstrip().startswith('#') is truthy) {
      // Source: vvaharness/detect/matcher.py:298-298
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/detect/matcher.py:299-299
    In source order: Evaluate hits.extend(scan.line_hits(live, idx, line)); retain side effects and discard the expression result.
  }
  // Source: vvaharness/detect/matcher.py:300-300
  End this invocation with hits.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.detect.spec import MatchSpec` at source line 22: `source_detail/vvaharness/detect/spec.py.sudo.md`.
