# vvaharness/backends/llm/tools.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/backends/llm/tools.py.evidence.json`. SHA-256: `9f5742057f4ba7a832d6a5c6646075749cfd4e3e282e55a456d118ec187cc15b`.

```sudo
// Source: vvaharness/backends/llm/tools.py:15-22
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import fnmatch; preserve alias and import-time effects. Then Resolve source import import os; preserve alias and import-time effects. Then Resolve source import import re; preserve alias and import-time effects.
// Source: vvaharness/backends/llm/tools.py:23-29
In source order: Resolve source import import threading; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from vvaharness.report.redact import redact_counts; preserve alias and import-time effects. Then Evaluate once 200000; assign in source target order to _MAX_BYTES. Then Evaluate once 200; assign in source target order to _MAX_MATCHES.
// Source: vvaharness/backends/llm/tools.py:30-40
In source order: Evaluate once 500; assign in source target order to _MAX_GLOB. Then Evaluate once 50000; assign in source target order to _MAX_GREP_LINE. Then Evaluate once frozenset({'.git', '.hg', '.svn', 'checkpoints', 'security-scan'}); assign in source target order to _ALWAYS_EXCLUDED_DIRS. Then For _ALWAYS_ALLOWED_PREFIXES, assign ('.vvaharness/',); source annotation tuple[str, ...]. Then For _SCOPE, assign {}; source annotation dict[str, frozenset[str]].
// Source: vvaharness/backends/llm/tools.py:41-41
In source order: Evaluate once threading.Lock(); assign in source target order to _SCOPE_LOCK.
// Source: vvaharness/backends/llm/tools.py:44-46
// Source signature: _always_allowed(rel: str) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _always_allowed(rel) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/tools.py:45-45
  In source order: Retain source documentation literal source_literal_45_4; it is not a model call.
  // Source: vvaharness/backends/llm/tools.py:46-46
  End this invocation with rel.startswith(_ALWAYS_ALLOWED_PREFIXES).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/tools.py:49-54
// Source signature: set_scope(root: str | Path, files) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn set_scope(root, files) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/tools.py:50-52
  In source order: Retain source documentation literal source_literal_50_4; it is not a model call. Then Evaluate once str(Path(root).resolve()); assign in source target order to key. Then Evaluate once frozenset((str(f).replace('\\', '/') for f in files)); assign in source target order to inv.
  // Source: vvaharness/backends/llm/tools.py:53-54
  Enter source context managers left-to-right: _SCOPE_LOCK {
    // Source: vvaharness/backends/llm/tools.py:54-54
    In source order: Evaluate once inv; assign in source target order to _SCOPE[key].
  }
  Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/tools.py:57-62
// Source signature: _scope_for(root: Path) -> frozenset[str] | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _scope_for(root) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/tools.py:58-61
  Perform the following protected operations {
    // Source: vvaharness/backends/llm/tools.py:59-59
    In source order: Evaluate once str(root.resolve()); assign in source target order to key.
  }
  // Source: vvaharness/backends/llm/tools.py:60-61
  On the first matching source exception OSError, in handler order {
    // Source: vvaharness/backends/llm/tools.py:61-61
    In source order: Evaluate once str(root); assign in source target order to key.
  }
  // Source: vvaharness/backends/llm/tools.py:62-62
  End this invocation with _SCOPE.get(key).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/tools.py:65-72
// Source signature: _excluded_rel(rel: str, scope: frozenset[str] | None) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _excluded_rel(rel, scope) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/tools.py:66-66
  In source order: Retain source documentation literal source_literal_66_4; it is not a model call.
  // Source: vvaharness/backends/llm/tools.py:67-68
  if (the source predicate _always_allowed(rel) is truthy) {
    // Source: vvaharness/backends/llm/tools.py:68-68
    End this invocation with False.
  }
  // Source: vvaharness/backends/llm/tools.py:69-69
  In source order: Evaluate once rel.split('/'); assign in source target order to parts.
  // Source: vvaharness/backends/llm/tools.py:70-71
  if (the source predicate any((part.lower() in _ALWAYS_EXCLUDED_DIRS for part in parts[:-1])) is truthy) {
    // Source: vvaharness/backends/llm/tools.py:71-71
    End this invocation with True.
  }
  // Source: vvaharness/backends/llm/tools.py:72-72
  End this invocation with scope is not None and rel not in scope.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/tools.py:75-85
// Source signature: _excluded_target(rel: str, scope: frozenset[str] | None) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _excluded_target(rel, scope) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/tools.py:76-76
  In source order: Retain source documentation literal source_literal_76_4; it is not a model call.
  // Source: vvaharness/backends/llm/tools.py:77-78
  if (the source predicate _always_allowed(rel) is truthy) {
    // Source: vvaharness/backends/llm/tools.py:78-78
    End this invocation with False.
  }
  // Source: vvaharness/backends/llm/tools.py:79-79
  In source order: Evaluate once rel.split('/'); assign in source target order to parts.
  // Source: vvaharness/backends/llm/tools.py:80-81
  if (the source predicate any((part.lower() in _ALWAYS_EXCLUDED_DIRS for part in parts)) is truthy) {
    // Source: vvaharness/backends/llm/tools.py:81-81
    End this invocation with True.
  }
  // Source: vvaharness/backends/llm/tools.py:82-83
  if (the source predicate scope is None or rel in scope is truthy) {
    // Source: vvaharness/backends/llm/tools.py:83-83
    End this invocation with False.
  }
  // Source: vvaharness/backends/llm/tools.py:84-84
  In source order: Evaluate once rel + '/'; assign in source target order to prefix.
  // Source: vvaharness/backends/llm/tools.py:85-85
  End this invocation with not any((f.startswith(prefix) for f in scope)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/tools.py:88-100
In source order: Evaluate once "ERROR: path '{path}' is excluded from the scan scope (not in the scanned file inventory)"; assign in source target order to _SCOPE_ERROR. Then Evaluate once "ERROR: tool '{name}' is not available in this session"; assign in source target order to UNGRANTED_TOOL_ERROR. Then Evaluate once 8192; assign in source target order to _BINARY_SNIFF_CHARS. Then Evaluate once re.compile('data:([\\w.+-]+/[\\w.+-]+);base64,([A-Za-z0-9+/=]*)'); assign in source target order to _DATA_URI_RX. Then Evaluate once re.compile('data:image/([\\w.+-]*)'); assign in source target order to _DATA_URI_IMAGE_RX.
// Source: vvaharness/backends/llm/tools.py:103-108
// Source signature: _is_binary_text(text: str) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _is_binary_text(text) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/tools.py:104-105
  In source order: Retain source documentation literal source_literal_104_4; it is not a model call. Then Evaluate once text[:_BINARY_SNIFF_CHARS]; assign in source target order to head.
  // Source: vvaharness/backends/llm/tools.py:106-107
  if (the source predicate '\x00' in head is truthy) {
    // Source: vvaharness/backends/llm/tools.py:107-107
    End this invocation with True.
  }
  // Source: vvaharness/backends/llm/tools.py:108-108
  End this invocation with bool(head) and head.count('�') / len(head) > 0.1.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/tools.py:111-120
// Source signature: _elide_data_uris(text: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _elide_data_uris(text) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/tools.py:113-116
  In source order: Evaluate once _DATA_URI_RX.sub(lambda m: source_template_114_19 if m.group(2) else source_template_115_38, text); assign in source target order to text.
  // Source: vvaharness/backends/llm/tools.py:117-120
  End this invocation with _DATA_URI_IMAGE_RX.sub(lambda m: source_template_118_19 if m.group(1) else '[data-uri image elided]', text).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/tools.py:123-127
// Source signature: sanitize_packed_text(text: str, rel: str='') -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn sanitize_packed_text(text, rel) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/tools.py:124-124
  In source order: Retain source documentation literal source_literal_124_4; it is not a model call.
  // Source: vvaharness/backends/llm/tools.py:125-126
  if (the source predicate _is_binary_text(text) is truthy) {
    // Source: vvaharness/backends/llm/tools.py:126-126
    End this invocation with source_template_126_15.
  }
  // Source: vvaharness/backends/llm/tools.py:127-127
  End this invocation with _elide_data_uris(text).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/tools.py:131-131
In source order: Evaluate once 48000; assign in source target order to TOOL_RESULT_CAP.
// Source: vvaharness/backends/llm/tools.py:134-141
// Source signature: cap_tool_result(result: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn cap_tool_result(result) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/tools.py:135-135
  In source order: Retain source documentation literal source_literal_135_4; it is not a model call.
  // Source: vvaharness/backends/llm/tools.py:136-137
  if (the source predicate not result or len(result) <= TOOL_RESULT_CAP is truthy) {
    // Source: vvaharness/backends/llm/tools.py:137-137
    End this invocation with result.
  }
  // Source: vvaharness/backends/llm/tools.py:138-138
  In source order: Evaluate once len(result) - TOOL_RESULT_CAP; assign in source target order to extra.
  // Source: vvaharness/backends/llm/tools.py:139-141
  End this invocation with result[:TOOL_RESULT_CAP] + source_template_140_14.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/tools.py:144-153
// Source signature: _jail(root: Path, p: str) -> Path | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _jail(root, p) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/tools.py:145-148
  Perform the following protected operations {
    // Source: vvaharness/backends/llm/tools.py:146-146
    In source order: Evaluate once (root / p).resolve() if not os.path.isabs(p) else Path(p).resolve(); assign in source target order to cand.
  }
  // Source: vvaharness/backends/llm/tools.py:147-148
  On the first matching source exception (OSError, ValueError), in handler order {
    // Source: vvaharness/backends/llm/tools.py:148-148
    End this invocation with None.
  }
  // Source: vvaharness/backends/llm/tools.py:149-152
  Perform the following protected operations {
    // Source: vvaharness/backends/llm/tools.py:150-150
    In source order: Evaluate cand.relative_to(root); retain side effects and discard the expression result.
  }
  // Source: vvaharness/backends/llm/tools.py:151-152
  On the first matching source exception ValueError, in handler order {
    // Source: vvaharness/backends/llm/tools.py:152-152
    End this invocation with None.
  }
  // Source: vvaharness/backends/llm/tools.py:153-153
  End this invocation with cand.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/tools.py:156-181
// Source signature: _read(root: Path, path: str, offset: int=0, limit: int=2000) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _read(root, path, offset, limit) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/tools.py:157-157
  In source order: Evaluate once _jail(root, path); assign in source target order to fp.
  // Source: vvaharness/backends/llm/tools.py:158-159
  if (the source predicate fp is None is truthy) {
    // Source: vvaharness/backends/llm/tools.py:159-159
    End this invocation with source_template_159_15.
  }
  // Source: vvaharness/backends/llm/tools.py:161-161
  In source order: Evaluate once str(fp.relative_to(root)).replace('\\', '/'); assign in source target order to rel.
  // Source: vvaharness/backends/llm/tools.py:162-163
  if (the source predicate _excluded_rel(rel, _scope_for(root)) is truthy) {
    // Source: vvaharness/backends/llm/tools.py:163-163
    End this invocation with _SCOPE_ERROR.format(path=path).
  }
  // Source: vvaharness/backends/llm/tools.py:164-165
  if (the source predicate not fp.is_file() is truthy) {
    // Source: vvaharness/backends/llm/tools.py:165-165
    End this invocation with source_template_165_15.
  }
  // Source: vvaharness/backends/llm/tools.py:166-170
  Perform the following protected operations {
    // Source: vvaharness/backends/llm/tools.py:167-168
    Enter source context managers left-to-right: open(fp, encoding='utf-8', errors='replace') bound to f {
      // Source: vvaharness/backends/llm/tools.py:168-168
      In source order: Evaluate once sanitize_packed_text(f.read(_MAX_BYTES * 4), rel).splitlines(); assign in source target order to lines.
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
  }
  // Source: vvaharness/backends/llm/tools.py:169-170
  On the first matching source exception OSError as e, in handler order {
    // Source: vvaharness/backends/llm/tools.py:170-170
    End this invocation with source_template_170_15.
  }
  // Source: vvaharness/backends/llm/tools.py:171-173
  In source order: Evaluate once max(0, int(offset)); assign in source target order to start. Then Evaluate once start + max(1, int(limit)); assign in source target order to end. Then Evaluate once []; assign in source target order to out.
  // Source: vvaharness/backends/llm/tools.py:174-175
  for each (i, line) in enumerate(lines[start:end], start + 1) {
    // Source: vvaharness/backends/llm/tools.py:175-175
    In source order: Evaluate out.append(source_template_175_19); retain side effects and discard the expression result.
  }
  // Source: vvaharness/backends/llm/tools.py:176-176
  In source order: Evaluate once source_literal_176_11.join(out); assign in source target order to body.
  // Source: vvaharness/backends/llm/tools.py:177-178
  if (the source predicate len(body) > _MAX_BYTES is truthy) {
    // Source: vvaharness/backends/llm/tools.py:178-178
    In source order: Evaluate once body[:_MAX_BYTES] + source_literal_178_35; assign in source target order to body.
  }
  // Source: vvaharness/backends/llm/tools.py:179-180
  if (the source predicate not body is truthy) {
    // Source: vvaharness/backends/llm/tools.py:180-180
    In source order: Evaluate once '(file is empty or offset past EOF)'; assign in source target order to body.
  }
  // Source: vvaharness/backends/llm/tools.py:181-181
  End this invocation with body.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/tools.py:184-204
// Source signature: _glob(root: Path, pattern: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _glob(root, pattern) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/tools.py:185-186
  In source order: Evaluate once pattern.lstrip('/').lstrip('\\'); assign in source target order to pat. Then Evaluate once _scope_for(root); assign in source target order to scope.
  // Source: vvaharness/backends/llm/tools.py:188-199
  Perform the following protected operations {
    // Source: vvaharness/backends/llm/tools.py:189-197
    In source order: Evaluate once sorted((rel for p in root.glob(pat) if p.is_file() and (fp := _jail(root, (rel := str(p.relative_to(root)).replace('\\', '/')))) is not None and (not _excluded_rel(str(fp.relative_to(root)).replace('\\', '/'), scope)))); assign in source target order to hits.
  }
  // Source: vvaharness/backends/llm/tools.py:198-199
  On the first matching source exception (OSError, ValueError) as e, in handler order {
    // Source: vvaharness/backends/llm/tools.py:199-199
    End this invocation with source_template_199_15.
  }
  // Source: vvaharness/backends/llm/tools.py:200-201
  if (the source predicate not hits is truthy) {
    // Source: vvaharness/backends/llm/tools.py:201-201
    End this invocation with 'No files found'.
  }
  // Source: vvaharness/backends/llm/tools.py:202-203
  if (the source predicate len(hits) > _MAX_GLOB is truthy) {
    // Source: vvaharness/backends/llm/tools.py:203-203
    End this invocation with source_literal_203_15.join(hits[:_MAX_GLOB]) + source_template_203_45.
  }
  // Source: vvaharness/backends/llm/tools.py:204-204
  End this invocation with source_literal_204_11.join(hits).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/tools.py:207-212
// Source signature: _grep_wanted(rel: str, glob: str | None) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _grep_wanted(rel, glob) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/tools.py:208-208
  In source order: Retain source documentation literal source_literal_208_4; it is not a model call.
  // Source: vvaharness/backends/llm/tools.py:209-210
  if (the source predicate not glob is truthy) {
    // Source: vvaharness/backends/llm/tools.py:210-210
    End this invocation with True.
  }
  // Source: vvaharness/backends/llm/tools.py:211-211
  In source order: Evaluate once glob.lstrip('/').lstrip('\\'); assign in source target order to pat.
  // Source: vvaharness/backends/llm/tools.py:212-212
  End this invocation with fnmatch.fnmatch(rel, pat) or fnmatch.fnmatch(rel.rsplit('/', 1)[-1], pat).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/tools.py:215-217
// Source signature: _grep_skip_harness(rel: str, explicit_harness: bool) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _grep_skip_harness(rel, explicit_harness) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/tools.py:216-216
  In source order: Retain source documentation literal source_literal_216_4; it is not a model call.
  // Source: vvaharness/backends/llm/tools.py:217-217
  End this invocation with not explicit_harness and (rel == '.vvaharness' or _always_allowed(rel)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/tools.py:220-229
// Source signature: _grep_in_surface(root: Path, p: Path, scope: frozenset[str] | None, glob: str | None, explicit_harness: bool) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _grep_in_surface(root, p, scope, glob, explicit_harness) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/tools.py:223-223
  In source order: Evaluate once _jail(root, str(p)) if p.is_file() else None; assign in source target order to fp.
  // Source: vvaharness/backends/llm/tools.py:224-225
  if (the source predicate fp is None is truthy) {
    // Source: vvaharness/backends/llm/tools.py:225-225
    End this invocation with False.
  }
  // Source: vvaharness/backends/llm/tools.py:226-226
  In source order: Evaluate once str(fp.relative_to(root)).replace('\\', '/'); assign in source target order to rel.
  // Source: vvaharness/backends/llm/tools.py:227-228
  if (the source predicate _grep_skip_harness(rel, explicit_harness) is truthy) {
    // Source: vvaharness/backends/llm/tools.py:228-228
    End this invocation with False.
  }
  // Source: vvaharness/backends/llm/tools.py:229-229
  End this invocation with _grep_wanted(rel, glob) and (not _excluded_rel(rel, scope)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/tools.py:232-250
// Source signature: _grep_files(root: Path, path: str | None, glob: str | None, scope: frozenset[str] | None) -> list[Path] | str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _grep_files(root, path, glob, scope) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/tools.py:234-234
  In source order: Retain source documentation literal source_literal_234_4; it is not a model call.
  // Source: vvaharness/backends/llm/tools.py:235-238
  if (the source predicate not path is truthy) {
    // Source: vvaharness/backends/llm/tools.py:237-238
    End this invocation with sorted((p for p in root.rglob('*') if _grep_in_surface(root, p, scope, glob, False))).
  }
  // Source: vvaharness/backends/llm/tools.py:239-239
  In source order: Evaluate once _jail(root, path); assign in source target order to target.
  // Source: vvaharness/backends/llm/tools.py:240-241
  if (the source predicate target is None is truthy) {
    // Source: vvaharness/backends/llm/tools.py:241-241
    End this invocation with source_template_241_15.
  }
  // Source: vvaharness/backends/llm/tools.py:243-243
  In source order: Evaluate once str(target.relative_to(root)).replace('\\', '/'); assign in source target order to rel.
  // Source: vvaharness/backends/llm/tools.py:244-245
  if (the source predicate rel != '.' and _excluded_target(rel, scope) is truthy) {
    // Source: vvaharness/backends/llm/tools.py:245-245
    End this invocation with _SCOPE_ERROR.format(path=path).
  }
  // Source: vvaharness/backends/llm/tools.py:246-247
  if (the source predicate not target.is_dir() is truthy) {
    // Source: vvaharness/backends/llm/tools.py:247-247
    End this invocation with [target] if target.is_file() else [].
  }
  // Source: vvaharness/backends/llm/tools.py:248-248
  In source order: Evaluate once rel == '.vvaharness' or _always_allowed(rel); assign in source target order to explicit_harness.
  // Source: vvaharness/backends/llm/tools.py:249-250
  End this invocation with sorted((p for p in target.rglob('*') if _grep_in_surface(root, p, scope, glob, explicit_harness))).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/tools.py:253-255
// Source signature: _clip_grep_line(s: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _clip_grep_line(s) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/tools.py:255-255
  End this invocation with s if len(s) <= _MAX_GREP_LINE else s[:_MAX_GREP_LINE] + ' …[line clipped]'.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/tools.py:258-268
// Source signature: _emit_grep_match(out: list[str], rel: str, i: int, lines: list[str], ctx: int) -> int
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _emit_grep_match(out, rel, i, lines, ctx) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/tools.py:259-259
  In source order: Retain source documentation literal source_literal_259_4; it is not a model call.
  // Source: vvaharness/backends/llm/tools.py:260-262
  if (the source predicate not ctx is truthy) {
    // Source: vvaharness/backends/llm/tools.py:261-261
    In source order: Evaluate out.append(source_template_261_19); retain side effects and discard the expression result.
    // Source: vvaharness/backends/llm/tools.py:262-262
    End this invocation with 1.
  }
  // Source: vvaharness/backends/llm/tools.py:263-263
  In source order: Evaluate once (max(0, i - ctx), min(len(lines), i + ctx + 1)); assign in source target order to (lo, hi).
  // Source: vvaharness/backends/llm/tools.py:264-266
  for each j in range(lo, hi) {
    // Source: vvaharness/backends/llm/tools.py:265-266
    In source order: Evaluate once ':' if j == i else '-'; assign in source target order to mark. Then Evaluate out.append(source_template_266_19); retain side effects and discard the expression result.
  }
  // Source: vvaharness/backends/llm/tools.py:267-267
  In source order: Evaluate out.append('--'); retain side effects and discard the expression result.
  // Source: vvaharness/backends/llm/tools.py:268-268
  End this invocation with hi - lo + 1.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/tools.py:271-310
// Source signature: _grep(root: Path, pattern: str, path: str | None=None, glob: str | None=None, ignore_case: bool=False, context: int=0) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _grep(root, pattern, path, glob, ignore_case, context) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/tools.py:274-274
  In source order: Evaluate once re.IGNORECASE if ignore_case else 0; assign in source target order to flags.
  // Source: vvaharness/backends/llm/tools.py:275-278
  Perform the following protected operations {
    // Source: vvaharness/backends/llm/tools.py:276-276
    In source order: Evaluate once re.compile(pattern, flags); assign in source target order to rx.
  }
  // Source: vvaharness/backends/llm/tools.py:277-278
  On the first matching source exception re.error as e, in handler order {
    // Source: vvaharness/backends/llm/tools.py:278-278
    End this invocation with source_template_278_15.
  }
  // Source: vvaharness/backends/llm/tools.py:280-280
  In source order: Evaluate once _grep_files(root, path, glob, _scope_for(root)); assign in source target order to files.
  // Source: vvaharness/backends/llm/tools.py:281-282
  if (the source predicate isinstance(files, str) is truthy) {
    // Source: vvaharness/backends/llm/tools.py:282-282
    End this invocation with files.
  }
  // Source: vvaharness/backends/llm/tools.py:284-286
  In source order: For out, assign []; source annotation list[str]. Then Evaluate once 0; assign in source target order to emitted. Then Evaluate once max(0, min(200, int(context))); assign in source target order to ctx.
  // Source: vvaharness/backends/llm/tools.py:287-309
  for each fp in files {
    // Source: vvaharness/backends/llm/tools.py:288-291
    Perform the following protected operations {
      // Source: vvaharness/backends/llm/tools.py:289-289
      In source order: Evaluate once fp.read_text(encoding='utf-8', errors='replace'); assign in source target order to text.
    }
    // Source: vvaharness/backends/llm/tools.py:290-291
    On the first matching source exception OSError, in handler order {
      // Source: vvaharness/backends/llm/tools.py:291-291
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/backends/llm/tools.py:292-293
    if (the source predicate len(text) > _MAX_BYTES * 8 is truthy) {
      // Source: vvaharness/backends/llm/tools.py:293-293
      In source order: Evaluate once text[:_MAX_BYTES * 8]; assign in source target order to text.
    }
    // Source: vvaharness/backends/llm/tools.py:295-296
    if (the source predicate _is_binary_text(text) is truthy) {
      // Source: vvaharness/backends/llm/tools.py:296-296
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/backends/llm/tools.py:297-299
    In source order: Evaluate once _elide_data_uris(text); assign in source target order to text. Then Evaluate once text.splitlines(); assign in source target order to lines. Then Evaluate once str(fp.relative_to(root)).replace('\\', '/'); assign in source target order to rel.
    // Source: vvaharness/backends/llm/tools.py:301-309
    for each (i, line) in enumerate(lines) {
      // Source: vvaharness/backends/llm/tools.py:303-304
      if (the source predicate not rx.search(line[:_MAX_GREP_LINE]) is truthy) {
        // Source: vvaharness/backends/llm/tools.py:304-304
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/backends/llm/tools.py:305-305
      In source order: Apply source augmented assignment emitted += _emit_grep_match(out, rel, i, lines, ctx) with source evaluation/in-place semantics.
      // Source: vvaharness/backends/llm/tools.py:306-309
      if (the source predicate emitted >= _MAX_MATCHES is truthy) {
        // Source: vvaharness/backends/llm/tools.py:307-308
        In source order: Evaluate out.append(source_template_307_27); retain side effects and discard the expression result.
        // Source: vvaharness/backends/llm/tools.py:309-309
        End this invocation with source_literal_309_23.join(out).
      }
    }
  }
  // Source: vvaharness/backends/llm/tools.py:310-310
  End this invocation with source_literal_310_11.join(out) if out else 'No matches found'.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/tools.py:315-371
In source order: Evaluate once {'Read': {'description': 'Read a file from the repository. Returns numbered lines.', 'parameters': {'type': 'object', 'properties': {'path': {'type': 'string', 'description': 'Path relative to the repo root'}, 'offset': {'type': 'integer', 'description': '0-based line to start from (default 0)'}, 'limit': {'type': 'integer', 'description': 'Max lines to return (default 2000)'}}, 'required': ['path']}}, 'Glob': {'description': 'List files in the repository matching a glob pattern (e.g. **/*.java).', 'parameters': {'type': 'object', 'properties': {'pattern': {'type': 'string'}}, 'required': ['pattern']}}, 'Grep': {'description': 'Search file contents for a regex. Returns file:line:text for each match.', 'parameters': {'type': 'object', 'properties': {'pattern': {'type': 'string', 'description': 'Python regex'}, 'path': {'type': 'string', 'description': 'Restrict to this file or directory'}, 'glob': {'type': 'string', 'description': 'Restrict to files matching this glob'}, 'ignore_case': {'type': 'boolean'}, 'context': {'type': 'integer', 'description': 'Lines of context around each match'}}, 'required': ['pattern']}}}; assign in source target order to _SCHEMAS. Then Evaluate once {'Read': lambda root, a: _read(root, a.get('path', ''), a.get('offset', 0), a.get('limit', 2000)), 'Glob': lambda root, a: _glob(root, a.get('pattern', '')), 'Grep': lambda root, a: _grep(root, a.get('pattern', ''), a.get('path'), a.get('glob'), bool(a.get('ignore_case', False)), a.get('context', 0))}; assign in source target order to _EXEC.
// Source: vvaharness/backends/llm/tools.py:374-382
// Source signature: schemas_for(allowed: list[str]) -> list[dict]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn schemas_for(allowed) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/tools.py:375-376
  In source order: Retain source documentation literal source_literal_375_4; it is not a model call. Then Evaluate once []; assign in source target order to out.
  // Source: vvaharness/backends/llm/tools.py:377-381
  for each name in allowed {
    // Source: vvaharness/backends/llm/tools.py:378-378
    In source order: Evaluate once _SCHEMAS.get(name); assign in source target order to spec.
    // Source: vvaharness/backends/llm/tools.py:379-381
    if (the source predicate spec is truthy) {
      // Source: vvaharness/backends/llm/tools.py:380-381
      In source order: Evaluate out.append({'type': 'function', 'function': {'name': name, **spec}}); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/backends/llm/tools.py:382-382
  End this invocation with out.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/tools.py:385-394
// Source signature: anthropic_schemas_for(allowed: list[str]) -> list[dict]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn anthropic_schemas_for(allowed) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/tools.py:386-387
  In source order: Retain source documentation literal source_literal_386_4; it is not a model call. Then Evaluate once []; assign in source target order to out.
  // Source: vvaharness/backends/llm/tools.py:388-393
  for each name in allowed {
    // Source: vvaharness/backends/llm/tools.py:389-389
    In source order: Evaluate once _SCHEMAS.get(name); assign in source target order to spec.
    // Source: vvaharness/backends/llm/tools.py:390-393
    if (the source predicate spec is truthy) {
      // Source: vvaharness/backends/llm/tools.py:391-393
      In source order: Evaluate out.append({'name': name, 'description': spec['description'], 'input_schema': spec['parameters']}); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/backends/llm/tools.py:394-394
  End this invocation with out.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/tools.py:397-400
// Source signature: supported(allowed: list[str]) -> tuple[list[str], list[str]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn supported(allowed) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/tools.py:398-399
  In source order: Evaluate once [t for t in allowed if t in _SCHEMAS]; assign in source target order to ok. Then Evaluate once [t for t in allowed if t not in _SCHEMAS]; assign in source target order to missing.
  // Source: vvaharness/backends/llm/tools.py:400-400
  End this invocation with (ok, missing).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/tools.py:403-416
// Source signature: summarize_args(args: dict | None) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn summarize_args(args) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/tools.py:404-405
  In source order: Retain source documentation literal source_literal_404_4; it is not a model call. Then For parts, assign []; source annotation list[str].
  // Source: vvaharness/backends/llm/tools.py:406-410
  for each key in ('path', 'pattern', 'glob') {
    // Source: vvaharness/backends/llm/tools.py:407-407
    In source order: Evaluate once (args or {}).get(key); assign in source target order to value.
    // Source: vvaharness/backends/llm/tools.py:408-410
    if (the source predicate value is truthy) {
      // Source: vvaharness/backends/llm/tools.py:409-410
      In source order: Evaluate once str(value); assign in source target order to text. Then Evaluate parts.append(source_template_410_25); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/backends/llm/tools.py:411-411
  In source order: Evaluate once (args or {}).get('context'); assign in source target order to context.
  // Source: vvaharness/backends/llm/tools.py:412-413
  if (the source predicate context is truthy) {
    // Source: vvaharness/backends/llm/tools.py:413-413
    In source order: Evaluate parts.append(source_template_413_21); retain side effects and discard the expression result.
  }
  // Source: vvaharness/backends/llm/tools.py:414-415
  if (the source predicate (args or {}).get('ignore_case') is truthy) {
    // Source: vvaharness/backends/llm/tools.py:415-415
    In source order: Evaluate parts.append('ignore_case=True'); retain side effects and discard the expression result.
  }
  // Source: vvaharness/backends/llm/tools.py:416-416
  End this invocation with ', '.join(parts) or '...'.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/tools.py:419-431
// Source signature: execute(name: str, args: dict, *, cwd: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn execute(name, args, cwd) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/tools.py:420-421
  In source order: Evaluate once Path(cwd).resolve(); assign in source target order to root. Then Evaluate once _EXEC.get(name); assign in source target order to fn.
  // Source: vvaharness/backends/llm/tools.py:422-423
  if (the source predicate fn is None is truthy) {
    // Source: vvaharness/backends/llm/tools.py:423-423
    End this invocation with source_template_423_15.
  }
  // Source: vvaharness/backends/llm/tools.py:424-427
  Perform the following protected operations {
    // Source: vvaharness/backends/llm/tools.py:425-425
    In source order: Evaluate once fn(root, args or {}); assign in source target order to result.
  }
  // Source: vvaharness/backends/llm/tools.py:426-427
  On the first matching source exception Exception as e, in handler order {
    // Source: vvaharness/backends/llm/tools.py:427-427
    End this invocation with source_template_427_15.
  }
  // Source: vvaharness/backends/llm/tools.py:429-430
  if (the source predicate name in ('Read', 'Grep') and (not result.startswith('ERROR:')) is truthy) {
    // Source: vvaharness/backends/llm/tools.py:430-430
    In source order: Evaluate once redact_counts(result); assign in source target order to (result, _).
  }
  // Source: vvaharness/backends/llm/tools.py:431-431
  End this invocation with result.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.report.redact import redact_counts` at source line 26: `source_detail/vvaharness/report/redact.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../prompt_representation/vvaharness/backends/llm/tools.py.sudo.md). Exact strings in the evidence asset support this conversion.
