# vvaharness/pipeline/stages/s8/facts.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/pipeline/stages/s8/facts.py.evidence.json`. SHA-256: `a0790d668a814fd32eccf984145a0138d63c8f12b1ddf0e4a597a82177b352f2`.

```sudo
// Source: vvaharness/pipeline/stages/s8/facts.py:16-21
In source order: Retain source documentation literal source_literal_16_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import re; preserve alias and import-time effects. Then Resolve source import from functools import lru_cache; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s8/facts.py:22-29
In source order: Resolve source import from stat import S_ISREG; preserve alias and import-time effects. Then Resolve source import from vvaharness.detect.matcher import split_lines; preserve alias and import-time effects. Then Resolve source import from vvaharness.models import ContextPackage, Finding; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import net as _net; preserve alias and import-time effects. Then Evaluate once 1200; assign in source target order to MAX_SNIPPET_CHARS.
// Source: vvaharness/pipeline/stages/s8/facts.py:32-46
In source order: Evaluate once 4; assign in source target order to MAX_DECORATOR_LINES. Then Evaluate once 200; assign in source target order to MAX_PROLOGUE_CHARS. Then Evaluate once re.compile(source_literal_38_28); assign in source target order to _ANNOTATION_RX. Then Evaluate once re.compile('^[^\\S\\n]*FROM[^\\S\\n]', re.IGNORECASE | re.MULTILINE); assign in source target order to _FROM_RX. Then Evaluate once re.compile('^[^\\S\\n]*USER[^\\S\\n]+(?P<user>\\S+)', re.IGNORECASE | re.MULTILINE); assign in source target order to _USER_RX.
// Source: vvaharness/pipeline/stages/s8/facts.py:49-49
In source order: Evaluate once re.compile('^[A-Za-z0-9_.:\\-]{1,64}$'); assign in source target order to _USER_TOKEN_RX.
// Source: vvaharness/pipeline/stages/s8/facts.py:52-61
// Source signature: _is_dockerfile_name(name: str) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _is_dockerfile_name(name) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s8/facts.py:53-54
  In source order: Retain source documentation literal source_literal_53_4; it is not a model call. Then Evaluate once name.lower(); assign in source target order to low.
  // Source: vvaharness/pipeline/stages/s8/facts.py:55-56
  if (the source predicate low == 'dockerfile' is truthy) {
    // Source: vvaharness/pipeline/stages/s8/facts.py:56-56
    End this invocation with True.
  }
  // Source: vvaharness/pipeline/stages/s8/facts.py:58-58
  In source order: Evaluate once low.partition('.'); assign in source target order to (prefix, dot, suffix).
  // Source: vvaharness/pipeline/stages/s8/facts.py:59-61
  End this invocation with prefix == 'dockerfile' and bool(dot) and (suffix not in {'py', 'pyi', 'js', 'ts', 'rb', 'go', 'java', 'cs', 'php', 'sh', 'yml', 'yaml', 'json', 'md', 'txt', 'html'}).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s8/facts.py:64-81
In source order: Evaluate once '\\[?[0-9a-fA-F:.]+\\]?|(?i:localhost)'; assign in source target order to _ADDR. Then Evaluate once re.compile(source_template_66_4, re.MULTILINE); assign in source target order to _BIND_RX.
// Source: vvaharness/pipeline/stages/s8/facts.py:84-86
// Source signature: _real_host(host: str) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _real_host(host) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s8/facts.py:85-85
  In source order: Retain source documentation literal source_literal_85_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s8/facts.py:86-86
  End this invocation with _net.is_loopback_host(host) or bool(_net.ip_literal(host)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s8/facts.py:89-106
// Source signature: snippet_for(f: Finding, repo_root: str | Path, *, include_decorators: bool=False) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn snippet_for(f, repo_root, include_decorators) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s8/facts.py:91-93
  In source order: Retain source documentation literal source_literal_91_4; it is not a model call. Then Resolve source import from vvaharness.pipeline.stages.s4_deepdive import _redact_source; preserve alias and import-time effects. Then Evaluate once (f.code_snippet or '').strip(); assign in source target order to text.
  // Source: vvaharness/pipeline/stages/s8/facts.py:94-98
  if (the source predicate text is truthy) {
    // Source: vvaharness/pipeline/stages/s8/facts.py:96-96
    In source order: Evaluate once _redact_source(text, f.file, stage='s8'); assign in source target order to text.
  }
  else {
    // Source: vvaharness/pipeline/stages/s8/facts.py:98-98
    In source order: Evaluate once _read_range(repo_root, f.file, f.line_start, f.line_end); assign in source target order to text.
  }
  // Source: vvaharness/pipeline/stages/s8/facts.py:99-103
  if (the source predicate include_decorators is truthy) {
    // Source: vvaharness/pipeline/stages/s8/facts.py:100-100
    In source order: Evaluate once _decorator_lines(repo_root, f.file, f.line_start); assign in source target order to prologue.
    // Source: vvaharness/pipeline/stages/s8/facts.py:102-103
    if (the source predicate prologue and prologue.rsplit(source_literal_102_40, 1)[-1].strip() not in text is truthy) {
      // Source: vvaharness/pipeline/stages/s8/facts.py:103-103
      In source order: Evaluate once source_template_103_19 if text else prologue; assign in source target order to text.
    }
  }
  // Source: vvaharness/pipeline/stages/s8/facts.py:104-105
  if (the source predicate len(text) > MAX_SNIPPET_CHARS is truthy) {
    // Source: vvaharness/pipeline/stages/s8/facts.py:105-105
    In source order: Evaluate once text[:MAX_SNIPPET_CHARS] + source_literal_105_42; assign in source target order to text.
  }
  // Source: vvaharness/pipeline/stages/s8/facts.py:106-106
  End this invocation with text.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s8/facts.py:110-122
// Source signature: _file_lines(repo_root: str | Path, file: str) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _file_lines(repo_root, file) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s8/facts.py:111-111
  In source order: Retain source documentation literal source_literal_111_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s8/facts.py:112-122
  Perform the following protected operations {
    // Source: vvaharness/pipeline/stages/s8/facts.py:113-116
    In source order: Evaluate once Path(repo_root).resolve(); assign in source target order to root. Then Evaluate once (root / file).resolve(); assign in source target order to target. Then Evaluate target.relative_to(root); retain side effects and discard the expression result. Then Evaluate once target.stat(); assign in source target order to st.
    // Source: vvaharness/pipeline/stages/s8/facts.py:117-119
    if (the source predicate not S_ISREG(st.st_mode) is truthy) {
      // Source: vvaharness/pipeline/stages/s8/facts.py:119-119
      End this invocation with [].
    }
    // Source: vvaharness/pipeline/stages/s8/facts.py:120-120
    End this invocation with list(_lines_cached(str(target), st.st_mtime_ns, st.st_size)).
  }
  // Source: vvaharness/pipeline/stages/s8/facts.py:121-122
  On the first matching source exception (OSError, ValueError, RuntimeError), in handler order {
    // Source: vvaharness/pipeline/stages/s8/facts.py:122-122
    End this invocation with [].
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s8/facts.py:127-130
// Source: vvaharness/pipeline/stages/s8/facts.py:126-126
Before creating this callable, evaluate and retain decorators top-to-bottom: lru_cache(maxsize=256).
// Source: vvaharness/pipeline/stages/s8/facts.py:127-130
// Source signature: _lines_cached(path: str, mtime_ns: int, size: int) -> tuple[str, ...]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _lines_cached(path, mtime_ns, size) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s8/facts.py:129-130
  End this invocation with tuple(split_lines(Path(path).read_text(encoding='utf-8', errors='replace'))).
  If execution reaches this end, finish with the source implicit None result.
}
At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
// Source: vvaharness/pipeline/stages/s8/facts.py:133-141
// Source signature: _read_range(repo_root: str | Path, file: str, start: int, end: int) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _read_range(repo_root, file, start, end) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s8/facts.py:134-135
  In source order: Retain source documentation literal source_literal_134_4; it is not a model call. Then Evaluate once _file_lines(repo_root, file); assign in source target order to lines.
  // Source: vvaharness/pipeline/stages/s8/facts.py:136-137
  if (the source predicate not lines is truthy) {
    // Source: vvaharness/pipeline/stages/s8/facts.py:137-137
    End this invocation with ''.
  }
  // Source: vvaharness/pipeline/stages/s8/facts.py:138-140
  In source order: Evaluate once max(start - 1, 0); assign in source target order to lo. Then Evaluate once max(end or start, start); assign in source target order to hi. Then Resolve source import from vvaharness.pipeline.stages.s4_deepdive import _redact_source; preserve alias and import-time effects.
  // Source: vvaharness/pipeline/stages/s8/facts.py:141-141
  End this invocation with _redact_source(source_literal_141_26.join(lines[lo:hi]), file, stage='s8').
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s8/facts.py:144-166
// Source signature: _decorator_lines(repo_root: str | Path, file: str, start: int) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _decorator_lines(repo_root, file, start) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s8/facts.py:145-145
  In source order: Retain source documentation literal source_literal_145_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s8/facts.py:146-147
  if (the source predicate start <= 1 is truthy) {
    // Source: vvaharness/pipeline/stages/s8/facts.py:147-147
    End this invocation with ''.
  }
  // Source: vvaharness/pipeline/stages/s8/facts.py:148-148
  In source order: Evaluate once _file_lines(repo_root, file); assign in source target order to lines.
  // Source: vvaharness/pipeline/stages/s8/facts.py:149-150
  if (the source predicate not lines is truthy) {
    // Source: vvaharness/pipeline/stages/s8/facts.py:150-150
    End this invocation with ''.
  }
  // Source: vvaharness/pipeline/stages/s8/facts.py:151-153
  In source order: For picked, assign []; source annotation list[str]. Then Evaluate once 0; assign in source target order to total. Then Evaluate once min(start - 1, len(lines)) - 1; assign in source target order to i.
  // Source: vvaharness/pipeline/stages/s8/facts.py:154-162
  while (the source predicate i >= 0 and len(picked) < MAX_DECORATOR_LINES is truthy) {
    // Source: vvaharness/pipeline/stages/s8/facts.py:155-156
    if (the source predicate not _ANNOTATION_RX.match(lines[i]) is truthy) {
      // Source: vvaharness/pipeline/stages/s8/facts.py:156-156
      Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
    }
    // Source: vvaharness/pipeline/stages/s8/facts.py:157-157
    In source order: Apply source augmented assignment total += len(lines[i]) + 1 with source evaluation/in-place semantics.
    // Source: vvaharness/pipeline/stages/s8/facts.py:158-160
    if (the source predicate total > MAX_PROLOGUE_CHARS is truthy) {
      // Source: vvaharness/pipeline/stages/s8/facts.py:160-160
      Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
    }
    // Source: vvaharness/pipeline/stages/s8/facts.py:161-162
    In source order: Evaluate picked.append(lines[i]); retain side effects and discard the expression result. Then Apply source augmented assignment i -= 1 with source evaluation/in-place semantics.
  }
  // Source: vvaharness/pipeline/stages/s8/facts.py:163-164
  if (the source predicate not picked is truthy) {
    // Source: vvaharness/pipeline/stages/s8/facts.py:164-164
    End this invocation with ''.
  }
  // Source: vvaharness/pipeline/stages/s8/facts.py:165-165
  In source order: Resolve source import from vvaharness.pipeline.stages.s4_deepdive import _redact_source; preserve alias and import-time effects.
  // Source: vvaharness/pipeline/stages/s8/facts.py:166-166
  End this invocation with _redact_source(source_literal_166_26.join(reversed(picked)), file, stage='s8').
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s8/facts.py:169-176
// Source signature: same_location_groups(findings: list[Finding], labels: list[str]) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn same_location_groups(findings, labels) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s8/facts.py:171-172
  In source order: Retain source documentation literal source_literal_171_4; it is not a model call. Then For groups, assign {}; source annotation dict[tuple[str, int], list[str]].
  // Source: vvaharness/pipeline/stages/s8/facts.py:173-174
  for each (lbl, f) in zip(labels, findings) {
    // Source: vvaharness/pipeline/stages/s8/facts.py:174-174
    In source order: Evaluate groups.setdefault((f.file, f.line_start), []).append(lbl); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s8/facts.py:175-176
  End this invocation with [source_template_175_12 for (file, line), ids in groups.items() if len(ids) > 1].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s8/facts.py:179-196
// Source signature: _user_directive_facts(rel: str, text: str) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _user_directive_facts(rel, text) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s8/facts.py:180-183
  In source order: Retain source documentation literal source_literal_180_4; it is not a model call. Then Evaluate once list(_USER_RX.finditer(text)); assign in source target order to matches. Then Evaluate once [m for m in matches if _USER_TOKEN_RX.match(m.group('user'))]; assign in source target order to users.
  // Source: vvaharness/pipeline/stages/s8/facts.py:184-185
  if (the source predicate matches and (not users) is truthy) {
    // Source: vvaharness/pipeline/stages/s8/facts.py:185-185
    End this invocation with [].
  }
  // Source: vvaharness/pipeline/stages/s8/facts.py:186-187
  if (the source predicate not users is truthy) {
    // Source: vvaharness/pipeline/stages/s8/facts.py:187-187
    End this invocation with [source_template_187_16].
  }
  // Source: vvaharness/pipeline/stages/s8/facts.py:188-190
  In source order: Evaluate once list(_FROM_RX.finditer(text)); assign in source target order to froms. Then Evaluate once froms[-1].start() if froms else -1; assign in source target order to last_from. Then Evaluate once [m for m in users if m.start() > last_from]; assign in source target order to final.
  // Source: vvaharness/pipeline/stages/s8/facts.py:191-193
  if (the source predicate final is truthy) {
    // Source: vvaharness/pipeline/stages/s8/facts.py:192-193
    End this invocation with [source_template_192_16].
  }
  // Source: vvaharness/pipeline/stages/s8/facts.py:194-194
  In source order: Evaluate once ', '.join(dict.fromkeys((m.group('user') for m in users))); assign in source target order to earlier.
  // Source: vvaharness/pipeline/stages/s8/facts.py:195-196
  End this invocation with [source_template_195_12].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s8/facts.py:199-238
// Source signature: exposure_facts(ctx: ContextPackage, findings: list[Finding], *, user_facts: bool=False) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn exposure_facts(ctx, findings, user_facts) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s8/facts.py:201-207
  In source order: Retain source documentation literal source_literal_201_4; it is not a model call. Then Evaluate once Path(ctx.repo_root); assign in source target order to root. Then For facts, assign []; source annotation list[str]. Then Evaluate once ['Dockerfile', 'docker-compose.yml', 'docker-compose.yaml', 'compose.yml', 'Makefile']; assign in source target order to names. Then Apply source augmented assignment names += sorted({f.file for f in findings})[:60] with source evaluation/in-place semantics.
  // Source: vvaharness/pipeline/stages/s8/facts.py:208-237
  for each rel in dict.fromkeys(names) {
    // Source: vvaharness/pipeline/stages/s8/facts.py:209-216
    Perform the following protected operations {
      // Source: vvaharness/pipeline/stages/s8/facts.py:210-211
      In source order: Evaluate once (root / rel).resolve(); assign in source target order to target. Then Evaluate target.relative_to(root.resolve()); retain side effects and discard the expression result.
      // Source: vvaharness/pipeline/stages/s8/facts.py:212-213
      if (the source predicate not target.is_file() is truthy) {
        // Source: vvaharness/pipeline/stages/s8/facts.py:213-213
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/pipeline/stages/s8/facts.py:214-214
      In source order: Evaluate once target.read_text(encoding='utf-8', errors='replace'); assign in source target order to text.
    }
    // Source: vvaharness/pipeline/stages/s8/facts.py:215-216
    On the first matching source exception (OSError, ValueError, RuntimeError), in handler order {
      // Source: vvaharness/pipeline/stages/s8/facts.py:216-216
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/pipeline/stages/s8/facts.py:217-218
    if (the source predicate user_facts and _is_dockerfile_name(Path(rel).name) is truthy) {
      // Source: vvaharness/pipeline/stages/s8/facts.py:218-218
      In source order: Apply source augmented assignment facts += _user_directive_facts(rel, text) with source evaluation/in-place semantics.
    }
    // Source: vvaharness/pipeline/stages/s8/facts.py:219-237
    for each m in _BIND_RX.finditer(text) {
      // Source: vvaharness/pipeline/stages/s8/facts.py:220-220
      In source order: Evaluate once m.group('host') or m.group('tuple') or m.group('const'); assign in source target order to host.
      // Source: vvaharness/pipeline/stages/s8/facts.py:221-237
      if (the source predicate host is truthy) {
        // Source: vvaharness/pipeline/stages/s8/facts.py:222-223
        if (the source predicate not _real_host(host) is truthy) {
          // Source: vvaharness/pipeline/stages/s8/facts.py:223-223
          Continue the immediately enclosing source loop at its next iteration.
        }
        // Source: vvaharness/pipeline/stages/s8/facts.py:224-228
        In source order: Evaluate once _net.is_loopback_host(host); assign in source target order to loop. Then Evaluate facts.append(source_template_226_20 + (' (LOOPBACK — not remotely reachable as written)' if loop else ' (all interfaces — remotely reachable)')); retain side effects and discard the expression result.
      }
      else {
        // Source: vvaharness/pipeline/stages/s8/facts.py:229-237
        if (the source predicate m.group('port') is truthy) {
          // Source: vvaharness/pipeline/stages/s8/facts.py:231-233
          if (the source predicate 'compose' in Path(rel).name.lower() is truthy) {
            // Source: vvaharness/pipeline/stages/s8/facts.py:232-233
            In source order: Evaluate facts.append(source_template_233_24); retain side effects and discard the expression result.
          }
        }
        else {
          // Source: vvaharness/pipeline/stages/s8/facts.py:234-237
          if (the source predicate m.group('to') is truthy) {
            // Source: vvaharness/pipeline/stages/s8/facts.py:235-237
            if (the source predicate _real_host(m.group('from')) and _real_host(m.group('to')) is truthy) {
              // Source: vvaharness/pipeline/stages/s8/facts.py:236-237
              In source order: Evaluate facts.append(source_template_236_33); retain side effects and discard the expression result.
            }
          }
        }
      }
    }
  }
  // Source: vvaharness/pipeline/stages/s8/facts.py:238-238
  End this invocation with list(dict.fromkeys(facts))[:12].
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.detect.matcher import split_lines` at source line 24: `source_detail/vvaharness/detect/matcher.py.sudo.md`.
- `from vvaharness.models import ContextPackage, Finding` at source line 25: `source_detail/vvaharness/models/__init__.py.sudo.md`.
- `from vvaharness.util import net as _net` at source line 26: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import net as _net` at source line 26: `source_detail/vvaharness/util/net.py.sudo.md`.
- `from vvaharness.pipeline.stages.s4_deepdive import _redact_source` at source line 92: `source_detail/vvaharness/pipeline/stages/s4_deepdive.py.sudo.md`.
- `from vvaharness.pipeline.stages.s4_deepdive import _redact_source` at source line 140: `source_detail/vvaharness/pipeline/stages/s4_deepdive.py.sudo.md`.
- `from vvaharness.pipeline.stages.s4_deepdive import _redact_source` at source line 165: `source_detail/vvaharness/pipeline/stages/s4_deepdive.py.sudo.md`.
