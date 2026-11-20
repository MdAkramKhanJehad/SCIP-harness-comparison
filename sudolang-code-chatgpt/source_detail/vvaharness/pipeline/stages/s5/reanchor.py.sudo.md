# vvaharness/pipeline/stages/s5/reanchor.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/pipeline/stages/s5/reanchor.py.evidence.json`. SHA-256: `ee24448ecb9aea196a9f26e8195be9efb31800475969751f70673a643c8f8b1f`.

```sudo
// Source: vvaharness/pipeline/stages/s5/reanchor.py:15-20
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import ast; preserve alias and import-time effects. Then Resolve source import import re; preserve alias and import-time effects. Then Resolve source import from dataclasses import dataclass, field; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s5/reanchor.py:22-26
In source order: Resolve source import from vvaharness.detect.patterns import default_corpus; preserve alias and import-time effects. Then Resolve source import from vvaharness.models import Finding; preserve alias and import-time effects. Then Resolve source import from vvaharness.pipeline.stages.s5.enrich import FileCache, snippet; preserve alias and import-time effects. Then Resolve source import from vvaharness.rules.cwe import weakness_key; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.counters import COUNTERS; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s5/reanchor.py:29-38
// Source signature: sink_patterns_by_cwe() -> dict[str, list[re.Pattern[str]]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn sink_patterns_by_cwe() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s5/reanchor.py:30-31
  In source order: Retain source documentation literal source_literal_30_4; it is not a model call. Then For by_cwe, assign {}; source annotation dict[str, list[re.Pattern[str]]].
  // Source: vvaharness/pipeline/stages/s5/reanchor.py:32-37
  for each spec in default_corpus() {
    // Source: vvaharness/pipeline/stages/s5/reanchor.py:33-34
    if (the source predicate spec.role != 'sink' is truthy) {
      // Source: vvaharness/pipeline/stages/s5/reanchor.py:34-34
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/pipeline/stages/s5/reanchor.py:35-35
    In source order: Evaluate once weakness_key(spec.cwe); assign in source target order to cwe.
    // Source: vvaharness/pipeline/stages/s5/reanchor.py:36-37
    if (the source predicate cwe is truthy) {
      // Source: vvaharness/pipeline/stages/s5/reanchor.py:37-37
      In source order: Evaluate by_cwe.setdefault(cwe, []).append(re.compile(spec.pattern)); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/pipeline/stages/s5/reanchor.py:38-38
  End this invocation with by_cwe.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s5/reanchor.py:41-45
// Source signature: _header_start(node: ast.AST) -> int
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _header_start(node) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s5/reanchor.py:42-44
  In source order: Retain source documentation literal source_literal_42_4; it is not a model call. Then Evaluate once getattr(node, 'decorator_list', []); assign in source target order to decorators. Then Evaluate once [d.lineno for d in decorators] + [node.lineno]; assign in source target order to linenos.
  // Source: vvaharness/pipeline/stages/s5/reanchor.py:45-45
  End this invocation with min(linenos).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s5/reanchor.py:48-50
// Source signature: _first_body_line(scope: ast.AST) -> int
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _first_body_line(scope) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s5/reanchor.py:49-49
  In source order: Retain source documentation literal source_literal_49_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s5/reanchor.py:50-50
  End this invocation with _header_start(scope.body[0]).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s5/reanchor.py:53-55
In source order: Evaluate once (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef); assign in source target order to _SCOPE_NODES. Then Evaluate once (*_SCOPE_NODES, ast.Lambda); assign in source target order to _NESTED_SCOPE_NODES.
// Source: vvaharness/pipeline/stages/s5/reanchor.py:58-66
// Source signature: _innermost_scope(scopes: list[tuple[int, int, ast.AST]], line: int) -> tuple[ast.AST | None, int]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _innermost_scope(scopes, line) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s5/reanchor.py:60-62
  In source order: Retain source documentation literal source_literal_60_4; it is not a model call. Then For best, assign None; source annotation ast.AST | None. Then Evaluate once 0; assign in source target order to best_header.
  // Source: vvaharness/pipeline/stages/s5/reanchor.py:63-65
  for each (header, end, node) in scopes {
    // Source: vvaharness/pipeline/stages/s5/reanchor.py:64-65
    if (the source predicate header <= line <= end and (best is None or header >= best_header) is truthy) {
      // Source: vvaharness/pipeline/stages/s5/reanchor.py:65-65
      In source order: Evaluate once (node, header); assign in source target order to (best, best_header).
    }
  }
  // Source: vvaharness/pipeline/stages/s5/reanchor.py:66-66
  End this invocation with (best, best_header).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s5/reanchor.py:69-81
// Source signature: _own_nodes(scope: ast.AST)
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _own_nodes(scope) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s5/reanchor.py:70-71
  In source order: Retain source documentation literal source_literal_70_4; it is not a model call. Then For stack, assign list(scope.body); source annotation list[ast.AST].
  // Source: vvaharness/pipeline/stages/s5/reanchor.py:72-75
  if (the source predicate isinstance(scope, ast.ClassDef) is truthy) {
    // Source: vvaharness/pipeline/stages/s5/reanchor.py:73-75
    for each node in scope.body {
      // Source: vvaharness/pipeline/stages/s5/reanchor.py:74-75
      if (the source predicate isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) is truthy) {
        // Source: vvaharness/pipeline/stages/s5/reanchor.py:75-75
        In source order: Evaluate stack.extend(node.body); retain side effects and discard the expression result.
      }
    }
  }
  // Source: vvaharness/pipeline/stages/s5/reanchor.py:76-81
  while (the source predicate stack is truthy) {
    // Source: vvaharness/pipeline/stages/s5/reanchor.py:77-78
    In source order: Evaluate once stack.pop(); assign in source target order to node. Then Yield node; suspend this generator until resumed.
    // Source: vvaharness/pipeline/stages/s5/reanchor.py:79-80
    if (the source predicate isinstance(node, _NESTED_SCOPE_NODES) is truthy) {
      // Source: vvaharness/pipeline/stages/s5/reanchor.py:80-80
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/pipeline/stages/s5/reanchor.py:81-81
    In source order: Evaluate stack.extend(ast.iter_child_nodes(node)); retain side effects and discard the expression result.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s5/reanchor.py:84-90
// Source signature: _callee_text(node: ast.Call) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _callee_text(node) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s5/reanchor.py:85-85
  In source order: Retain source documentation literal source_literal_85_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s5/reanchor.py:86-90
  Perform the following protected operations {
    // Source: vvaharness/pipeline/stages/s5/reanchor.py:87-87
    End this invocation with source_template_87_15.
  }
  // Source: vvaharness/pipeline/stages/s5/reanchor.py:89-90
  On the first matching source exception (AttributeError, ValueError, RecursionError), in handler order {
    // Source: vvaharness/pipeline/stages/s5/reanchor.py:90-90
    End this invocation with ''.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s5/reanchor.py:93-96
// Source signature: _scope_calls(scope: ast.AST) -> list[tuple[int, str]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _scope_calls(scope) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s5/reanchor.py:94-94
  In source order: Retain source documentation literal source_literal_94_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s5/reanchor.py:95-96
  End this invocation with [(node.lineno, _callee_text(node)) for node in _own_nodes(scope) if isinstance(node, ast.Call)].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s5/reanchor.py:99-103
// Source signature: _sink_lines(calls: list[tuple[int, str]], patterns: list[re.Pattern[str]]) -> list[int]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _sink_lines(calls, patterns) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s5/reanchor.py:101-101
  In source order: Retain source documentation literal source_literal_101_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s5/reanchor.py:102-103
  End this invocation with sorted({ln for ln, callee in calls if callee and any((rx.search(callee) for rx in patterns))}).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s5/reanchor.py:107-107
In source order: Evaluate once 16; assign in source target order to _MAX_PARSED_FILES.
// Source: vvaharness/pipeline/stages/s5/reanchor.py:111-117
// Source: vvaharness/pipeline/stages/s5/reanchor.py:110-110
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass.
// Source: vvaharness/pipeline/stages/s5/reanchor.py:111-117
interface _ParsedFile {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/pipeline/stages/s5/reanchor.py:112-117
  In source order: Retain source documentation literal source_literal_112_4; it is not a model call. Then For scopes, declare without assigning a value; source annotation list[tuple[int, int, ast.AST]]. Then For calls, assign field(default_factory=dict); source annotation dict[int, list[tuple[int, str]]].
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vvaharness/pipeline/stages/s5/reanchor.py:120-227
interface Reanchorer {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/pipeline/stages/s5/reanchor.py:121-121
  In source order: Retain source documentation literal source_literal_121_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s5/reanchor.py:123-129
  // Source signature: __init__(self, cache: FileCache, by_cwe: dict[str, list[re.Pattern[str]]], max_move: int)
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self, cache, by_cwe, max_move) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/pipeline/stages/s5/reanchor.py:125-129
    In source order: Evaluate once cache; assign in source target order to self._cache. Then Evaluate once by_cwe; assign in source target order to self._by_cwe. Then Evaluate once max_move; assign in source target order to self._max_move. Then For self._parsed, assign {}; source annotation dict[str, _ParsedFile | None].
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/pipeline/stages/s5/reanchor.py:131-152
  // Source signature: _file(self, rel: str) -> _ParsedFile | None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _file(self, rel) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/pipeline/stages/s5/reanchor.py:132-132
    In source order: Retain source documentation literal source_literal_132_8; it is not a model call.
    // Source: vvaharness/pipeline/stages/s5/reanchor.py:133-135
    if (the source predicate rel in self._parsed is truthy) {
      // Source: vvaharness/pipeline/stages/s5/reanchor.py:134-134
      In source order: Evaluate once self._parsed.pop(rel); assign in source target order to self._parsed[rel], parsed.
      // Source: vvaharness/pipeline/stages/s5/reanchor.py:135-135
      End this invocation with parsed.
    }
    // Source: vvaharness/pipeline/stages/s5/reanchor.py:136-137
    In source order: Evaluate once self._cache.lines(rel); assign in source target order to lines. Then Evaluate once None; assign in source target order to parsed.
    // Source: vvaharness/pipeline/stages/s5/reanchor.py:138-148
    if (the source predicate lines is not None is truthy) {
      // Source: vvaharness/pipeline/stages/s5/reanchor.py:139-148
      Perform the following protected operations {
        // Source: vvaharness/pipeline/stages/s5/reanchor.py:140-145
        In source order: Evaluate once ast.parse(source_literal_140_33.join(lines)); assign in source target order to tree. Then Evaluate once _ParsedFile(scopes=[(_header_start(node), getattr(node, 'end_lineno', None) or node.lineno, node) for node in ast.walk(tree) if isinstance(node, _SCOPE_NODES)]); assign in source target order to parsed.
      }
      // Source: vvaharness/pipeline/stages/s5/reanchor.py:147-148
      On the first matching source exception (SyntaxError, ValueError, MemoryError, RecursionError), in handler order {
        // Source: vvaharness/pipeline/stages/s5/reanchor.py:148-148
        In source order: Evaluate once None; assign in source target order to parsed.
      }
    }
    // Source: vvaharness/pipeline/stages/s5/reanchor.py:149-149
    In source order: Evaluate once parsed; assign in source target order to self._parsed[rel].
    // Source: vvaharness/pipeline/stages/s5/reanchor.py:150-151
    if (the source predicate len(self._parsed) > _MAX_PARSED_FILES is truthy) {
      // Source: vvaharness/pipeline/stages/s5/reanchor.py:151-151
      In source order: Delete source targets in order: self._parsed[next(iter(self._parsed))].
    }
    // Source: vvaharness/pipeline/stages/s5/reanchor.py:152-152
    End this invocation with parsed.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/pipeline/stages/s5/reanchor.py:154-159
  // Source signature: _calls(self, parsed: _ParsedFile, scope: ast.AST) -> list[tuple[int, str]]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _calls(self, parsed, scope) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/pipeline/stages/s5/reanchor.py:155-156
    In source order: Retain source documentation literal source_literal_155_8; it is not a model call. Then Evaluate once id(scope); assign in source target order to key.
    // Source: vvaharness/pipeline/stages/s5/reanchor.py:157-158
    if (the source predicate key not in parsed.calls is truthy) {
      // Source: vvaharness/pipeline/stages/s5/reanchor.py:158-158
      In source order: Evaluate once _scope_calls(scope); assign in source target order to parsed.calls[key].
    }
    // Source: vvaharness/pipeline/stages/s5/reanchor.py:159-159
    End this invocation with parsed.calls[key].
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/pipeline/stages/s5/reanchor.py:161-170
  // Source signature: _own_sink_line(self, f: Finding) -> int | None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _own_sink_line(self, f) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/pipeline/stages/s5/reanchor.py:162-163
    In source order: Retain source documentation literal source_literal_162_8; it is not a model call. Then Evaluate once (f.sink_ref or '').strip().rpartition(':'); assign in source target order to (path, _, ln).
    // Source: vvaharness/pipeline/stages/s5/reanchor.py:164-165
    if (the source predicate path != f.file or not ln.isdigit() is truthy) {
      // Source: vvaharness/pipeline/stages/s5/reanchor.py:165-165
      End this invocation with None.
    }
    // Source: vvaharness/pipeline/stages/s5/reanchor.py:166-167
    In source order: Evaluate once int(ln); assign in source target order to line. Then Evaluate once self._cache.lines(f.file); assign in source target order to lines.
    // Source: vvaharness/pipeline/stages/s5/reanchor.py:168-169
    if (the source predicate lines is None or not 1 <= line <= len(lines) is truthy) {
      // Source: vvaharness/pipeline/stages/s5/reanchor.py:169-169
      End this invocation with None.
    }
    // Source: vvaharness/pipeline/stages/s5/reanchor.py:170-170
    End this invocation with line.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/pipeline/stages/s5/reanchor.py:172-227
  // Source signature: apply(self, f: Finding) -> Finding
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn apply(self, f) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/pipeline/stages/s5/reanchor.py:173-176
    In source order: Retain source documentation literal source_literal_173_8; it is not a model call. Then Evaluate once self._own_sink_line(f); assign in source target order to own_sink. Then Evaluate once None; assign in source target order to patterns.
    // Source: vvaharness/pipeline/stages/s5/reanchor.py:177-181
    if (the source predicate own_sink is None is truthy) {
      // Source: vvaharness/pipeline/stages/s5/reanchor.py:178-178
      In source order: Evaluate once self._by_cwe.get(weakness_key(f.cwe) or ''); assign in source target order to patterns.
      // Source: vvaharness/pipeline/stages/s5/reanchor.py:179-181
      if (the source predicate not patterns is truthy) {
        // Source: vvaharness/pipeline/stages/s5/reanchor.py:180-180
        In source order: Evaluate COUNTERS.bump('s5_reanchor_no_pattern'); retain side effects and discard the expression result.
        // Source: vvaharness/pipeline/stages/s5/reanchor.py:181-181
        End this invocation with f.
      }
    }
    // Source: vvaharness/pipeline/stages/s5/reanchor.py:182-182
    In source order: Evaluate once self._file(f.file) if f.file.endswith('.py') else None; assign in source target order to parsed.
    // Source: vvaharness/pipeline/stages/s5/reanchor.py:183-185
    if (the source predicate parsed is None is truthy) {
      // Source: vvaharness/pipeline/stages/s5/reanchor.py:184-184
      In source order: Evaluate COUNTERS.bump('s5_reanchor_unparsed'); retain side effects and discard the expression result.
      // Source: vvaharness/pipeline/stages/s5/reanchor.py:185-185
      End this invocation with f.
    }
    // Source: vvaharness/pipeline/stages/s5/reanchor.py:186-187
    In source order: Evaluate once max(1, int(f.line_start)); assign in source target order to line. Then Evaluate once _innermost_scope(parsed.scopes, line); assign in source target order to (scope, header).
    // Source: vvaharness/pipeline/stages/s5/reanchor.py:188-190
    if (the source predicate scope is None is truthy) {
      // Source: vvaharness/pipeline/stages/s5/reanchor.py:189-189
      In source order: Evaluate COUNTERS.bump('s5_reanchor_no_scope'); retain side effects and discard the expression result.
      // Source: vvaharness/pipeline/stages/s5/reanchor.py:190-190
      End this invocation with f.
    }
    // Source: vvaharness/pipeline/stages/s5/reanchor.py:192-194
    if (the source predicate not header <= line < max(_first_body_line(scope), header + 1) is truthy) {
      // Source: vvaharness/pipeline/stages/s5/reanchor.py:193-193
      In source order: Evaluate COUNTERS.bump('s5_reanchor_body_anchored'); retain side effects and discard the expression result.
      // Source: vvaharness/pipeline/stages/s5/reanchor.py:194-194
      End this invocation with f.
    }
    // Source: vvaharness/pipeline/stages/s5/reanchor.py:196-202
    if (the source predicate own_sink is not None and own_sink == line and (line < _first_body_line(scope)) is truthy) {
      // Source: vvaharness/pipeline/stages/s5/reanchor.py:197-199
      In source order: Evaluate COUNTERS.bump('s5_reanchor_own_sink_is_header'); retain side effects and discard the expression result. Then Evaluate once None; assign in source target order to own_sink. Then Evaluate once self._by_cwe.get(weakness_key(f.cwe) or ''); assign in source target order to patterns.
      // Source: vvaharness/pipeline/stages/s5/reanchor.py:200-202
      if (the source predicate not patterns is truthy) {
        // Source: vvaharness/pipeline/stages/s5/reanchor.py:201-201
        In source order: Evaluate COUNTERS.bump('s5_reanchor_no_pattern'); retain side effects and discard the expression result.
        // Source: vvaharness/pipeline/stages/s5/reanchor.py:202-202
        End this invocation with f.
      }
    }
    // Source: vvaharness/pipeline/stages/s5/reanchor.py:203-207
    if (the source predicate own_sink is not None is truthy) {
      // Source: vvaharness/pipeline/stages/s5/reanchor.py:204-205
      In source order: Evaluate COUNTERS.bump('s5_reanchor_own_sink_ref'); retain side effects and discard the expression result. Then Evaluate once [own_sink]; assign in source target order to candidates.
    }
    else {
      // Source: vvaharness/pipeline/stages/s5/reanchor.py:207-207
      In source order: Evaluate once _sink_lines(self._calls(parsed, scope), patterns); assign in source target order to candidates.
    }
    // Source: vvaharness/pipeline/stages/s5/reanchor.py:208-210
    if (the source predicate not candidates is truthy) {
      // Source: vvaharness/pipeline/stages/s5/reanchor.py:209-209
      In source order: Evaluate COUNTERS.bump('s5_reanchor_no_sink'); retain side effects and discard the expression result.
      // Source: vvaharness/pipeline/stages/s5/reanchor.py:210-210
      End this invocation with f.
    }
    // Source: vvaharness/pipeline/stages/s5/reanchor.py:211-211
    In source order: Evaluate once min(candidates, key=lambda ln: (abs(ln - line), ln)); assign in source target order to sink.
    // Source: vvaharness/pipeline/stages/s5/reanchor.py:212-214
    if (the source predicate sink == line is truthy) {
      // Source: vvaharness/pipeline/stages/s5/reanchor.py:213-213
      In source order: Evaluate COUNTERS.bump('s5_reanchor_already_at_sink'); retain side effects and discard the expression result.
      // Source: vvaharness/pipeline/stages/s5/reanchor.py:214-214
      End this invocation with f.
    }
    // Source: vvaharness/pipeline/stages/s5/reanchor.py:215-217
    if (the source predicate abs(sink - line) > self._max_move is truthy) {
      // Source: vvaharness/pipeline/stages/s5/reanchor.py:216-216
      In source order: Evaluate COUNTERS.bump('s5_reanchor_capped'); retain side effects and discard the expression result.
      // Source: vvaharness/pipeline/stages/s5/reanchor.py:217-217
      End this invocation with f.
    }
    // Source: vvaharness/pipeline/stages/s5/reanchor.py:218-218
    In source order: For update, assign {'line_start': sink, 'line_end': max(int(f.line_end), sink)}; source annotation dict.
    // Source: vvaharness/pipeline/stages/s5/reanchor.py:219-222
    if (the source predicate not (f.sink_ref or '').strip() is truthy) {
      // Source: vvaharness/pipeline/stages/s5/reanchor.py:221-222
      In source order: Evaluate once source_template_221_33; assign in source target order to update['sink_ref']. Then Evaluate once sorted(set(f.backfilled_refs) | {'sink_ref'}); assign in source target order to update['backfilled_refs'].
    }
    // Source: vvaharness/pipeline/stages/s5/reanchor.py:223-226
    In source order: Evaluate once f.model_copy(update=update); assign in source target order to moved. Then Evaluate once snippet(moved, self._cache.lines(f.file) or []); assign in source target order to moved.code_snippet. Then Evaluate COUNTERS.bump('s5_sink_reanchored'); retain side effects and discard the expression result.
    // Source: vvaharness/pipeline/stages/s5/reanchor.py:227-227
    End this invocation with moved.
    If execution reaches this end, finish with the source implicit None result.
  }
}
```

## Local import links

- `from vvaharness.detect.patterns import default_corpus` at source line 22: `source_detail/vvaharness/detect/patterns.py.sudo.md`.
- `from vvaharness.models import Finding` at source line 23: `source_detail/vvaharness/models/__init__.py.sudo.md`.
- `from vvaharness.pipeline.stages.s5.enrich import FileCache, snippet` at source line 24: `source_detail/vvaharness/pipeline/stages/s5/enrich.py.sudo.md`.
- `from vvaharness.rules.cwe import weakness_key` at source line 25: `source_detail/vvaharness/rules/cwe.py.sudo.md`.
- `from vvaharness.util.counters import COUNTERS` at source line 26: `source_detail/vvaharness/util/counters.py.sudo.md`.
