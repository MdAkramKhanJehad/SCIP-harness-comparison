# vvaharness/remediation_agent/policy/patch_content.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/remediation_agent/policy/patch_content.py.evidence.json`. SHA-256: `aa8171079be50d66d1d351848a09684c12cf1760d1943a52b84c4a11367d36a1`.

```sudo
// Source: vvaharness/remediation_agent/policy/patch_content.py:15-28
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import re; preserve alias and import-time effects. Then Resolve source import from collections.abc import Iterable; preserve alias and import-time effects. Then Resolve source import from pathlib import PurePosixPath; preserve alias and import-time effects.
// Source: vvaharness/remediation_agent/policy/patch_content.py:31-158
In source order: For _RULES, assign (('auth_bypass', 'introduces an authentication/authorization short-circuit', (re.compile(source_literal_38_16), re.compile(source_literal_44_16), re.compile(source_literal_50_16), re.compile(source_literal_57_16), re.compile('(?i)\\bCERT_NONE\\b|\\bInsecureSkipVerify\\s*:\\s*true\\b'))), ('code_execution', 'introduces dynamic code execution', (re.compile('(?<![\\w.])(?:eval|exec|compile)\\s*\\('), re.compile(source_literal_72_16), re.compile('(?<![\\w.])new\\s+Function\\s*\\('), re.compile('(?i)\\bpickle\\.loads?\\s*\\(|\\byaml\\.load\\s*\\((?![^)]*Safe)'), re.compile('(?i)\\b__import__\\s*\\(|\\bimportlib\\.import_module\\s*\\('), re.compile('(?i)\\bsetTimeout\\s*\\(\\s*[\'\\"]'))), ('network_egress', 'introduces outbound network access', (re.compile(source_literal_89_16), re.compile('(?i)(?<![\\w.])(?:curl|wget|nc|ncat|netcat)\\s+(?:-\\S+\\s+)*(?:https?://|\\d{1,3}\\.)'))), ('credential_exfiltration', 'reads credentials or secret material into a new code path', (re.compile(source_literal_111_16), re.compile('(?i)\\bos\\.environ(?:\\.get)?\\s*[\\[(]\\s*[\'\\"][^\'\\"\\n]*(?:SECRET|TOKEN|PASSWORD|API_?KEY|PRIVATE_?KEY|CREDENTIAL)'), re.compile('(?i)\\b(?:base64\\.b64decode|atob)\\s*\\(\\s*[\'\\"][A-Za-z0-9+/=]{24,}'))), ('reverse_shell', 'introduces a reverse shell or interactive listener', (re.compile('(?i)\\b(?:/bin/(?:ba)?sh|cmd\\.exe|powershell)\\b[^\\n]{0,60}(?:-i|-c|/c|-nop|-enc)\\b'), re.compile('(?i)\\bpty\\.spawn\\s*\\(|\\bsocket\\.dup2\\b|\\bdup2\\s*\\(\\s*s\\b'), re.compile('(?i)\\bnc\\s+-\\w*l\\w*\\b|\\bbash\\s+-i\\s*>&')))); source annotation tuple[tuple[str, str, tuple[re.Pattern[str], ...]], ...]. Then Evaluate once re.compile('^\\s*(?:\\#|//|/\\*|\\*|<!--|--|;|%|\\"\\"\\"|\'\'\'|rem\\s)', re.IGNORECASE | re.VERBOSE); assign in source target order to _COMMENT_ONLY. Then Evaluate once re.compile(source_literal_150_4, re.VERBOSE | re.DOTALL); assign in source target order to _PROSE_STRING_ONLY.
// Source: vvaharness/remediation_agent/policy/patch_content.py:161-170
// Source signature: _is_prose_string(text: str) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _is_prose_string(text) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/policy/patch_content.py:162-169
  In source order: Retain source documentation literal source_literal_162_4; it is not a model call. Then Evaluate once _PROSE_STRING_ONLY.match(text.strip()); assign in source target order to match.
  // Source: vvaharness/remediation_agent/policy/patch_content.py:170-170
  End this invocation with bool(match) and ' ' in (match.group('body') or '').
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/policy/patch_content.py:172-175
In source order: Evaluate once ('+++', '---'); assign in source target order to _DIFF_HEADER_PREFIXES. Then Evaluate once re.compile('^@@ '); assign in source target order to _HUNK. Then Evaluate once re.compile('^diff --git a/(?P<a>.+?) b/(?P<b>.+?)\\s*$'); assign in source target order to _DIFF_GIT. Then Evaluate once re.compile('^\\+\\+\\+ (?:b/)?(?P<path>.+?)\\s*$'); assign in source target order to _PLUS_FILE.
// Source: vvaharness/remediation_agent/policy/patch_content.py:178-207
// Source signature: added_lines_by_file(diff_text: str | None) -> dict[str, list[tuple[int, str]]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn added_lines_by_file(diff_text) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/policy/patch_content.py:179-184
  In source order: Retain source documentation literal source_literal_179_4; it is not a model call.
  // Source: vvaharness/remediation_agent/policy/patch_content.py:185-186
  if (the source predicate not diff_text is truthy) {
    // Source: vvaharness/remediation_agent/policy/patch_content.py:186-186
    End this invocation with {}.
  }
  // Source: vvaharness/remediation_agent/policy/patch_content.py:187-189
  In source order: For out, assign {}; source annotation dict[str, list[tuple[int, str]]]. Then For current, assign None; source annotation str | None. Then Evaluate once 0; assign in source target order to counter.
  // Source: vvaharness/remediation_agent/policy/patch_content.py:190-206
  for each raw in diff_text.splitlines() {
    // Source: vvaharness/remediation_agent/policy/patch_content.py:191-191
    In source order: Evaluate once _DIFF_GIT.match(raw); assign in source target order to m.
    // Source: vvaharness/remediation_agent/policy/patch_content.py:192-195
    if (the source predicate m is truthy) {
      // Source: vvaharness/remediation_agent/policy/patch_content.py:193-194
      In source order: Evaluate once (m.group('b') or m.group('a')).strip() or None; assign in source target order to current. Then Evaluate once 0; assign in source target order to counter.
      // Source: vvaharness/remediation_agent/policy/patch_content.py:195-195
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/remediation_agent/policy/patch_content.py:196-196
    In source order: Evaluate once _PLUS_FILE.match(raw); assign in source target order to m.
    // Source: vvaharness/remediation_agent/policy/patch_content.py:197-201
    if (the source predicate m is truthy) {
      // Source: vvaharness/remediation_agent/policy/patch_content.py:198-200
      In source order: Evaluate once m.group('path').strip(); assign in source target order to path. Then Evaluate once None if path == '/dev/null' else path; assign in source target order to current. Then Evaluate once 0; assign in source target order to counter.
      // Source: vvaharness/remediation_agent/policy/patch_content.py:201-201
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/remediation_agent/policy/patch_content.py:202-203
    if (the source predicate raw.startswith(_DIFF_HEADER_PREFIXES) or _HUNK.match(raw) is truthy) {
      // Source: vvaharness/remediation_agent/policy/patch_content.py:203-203
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/remediation_agent/policy/patch_content.py:204-206
    if (the source predicate current and raw.startswith('+') is truthy) {
      // Source: vvaharness/remediation_agent/policy/patch_content.py:205-206
      In source order: Apply source augmented assignment counter += 1 with source evaluation/in-place semantics. Then Evaluate out.setdefault(current, []).append((counter, raw[1:])); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/remediation_agent/policy/patch_content.py:207-207
  End this invocation with out.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/policy/patch_content.py:211-218
In source order: Evaluate once frozenset({'.sh', '.bash', '.zsh', '.ksh', '.ps1', '.psm1'}); assign in source target order to _SHELL_EXTS. Then Evaluate once ('vvaharness/', 'security-scan/', 'security-remediation/'); assign in source target order to _HARNESS_OWNED_PREFIXES.
// Source: vvaharness/remediation_agent/policy/patch_content.py:221-235
// Source signature: _is_executable_source(path: str) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _is_executable_source(path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/policy/patch_content.py:222-234
  In source order: Retain source documentation literal source_literal_222_4; it is not a model call. Then Resolve source import from vvaharness.remediation_agent.frameworks import language_for; preserve alias and import-time effects. Then Evaluate once PurePosixPath(path or '').suffix.lower(); assign in source target order to suffix.
  // Source: vvaharness/remediation_agent/policy/patch_content.py:235-235
  End this invocation with suffix in _SHELL_EXTS or language_for(path) != 'default'.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/policy/patch_content.py:238-271
// Source signature: scan_added_lines(diff_text: str | None, *, only_files: Iterable[str] | None=None) -> dict[str, list[str]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn scan_added_lines(diff_text, only_files) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/policy/patch_content.py:241-247
  In source order: Retain source documentation literal source_literal_241_4; it is not a model call.
  // Source: vvaharness/remediation_agent/policy/patch_content.py:248-251
  Perform the following protected operations {
    // Source: vvaharness/remediation_agent/policy/patch_content.py:249-249
    In source order: Evaluate once added_lines_by_file(diff_text); assign in source target order to added.
  }
  // Source: vvaharness/remediation_agent/policy/patch_content.py:250-251
  On the first matching source exception Exception, in handler order {
    // Source: vvaharness/remediation_agent/policy/patch_content.py:251-251
    End this invocation with {}.
  }
  // Source: vvaharness/remediation_agent/policy/patch_content.py:252-253
  In source order: Evaluate once {_fold(f) for f in only_files} if only_files is not None else None; assign in source target order to allowed. Then For issues, assign {}; source annotation dict[str, list[str]].
  // Source: vvaharness/remediation_agent/policy/patch_content.py:254-270
  for each (path, lines) in added.items() {
    // Source: vvaharness/remediation_agent/policy/patch_content.py:255-256
    if (the source predicate allowed is not None and _fold(path) not in allowed is truthy) {
      // Source: vvaharness/remediation_agent/policy/patch_content.py:256-256
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/remediation_agent/policy/patch_content.py:257-257
    In source order: Evaluate once _fold(path); assign in source target order to folded.
    // Source: vvaharness/remediation_agent/policy/patch_content.py:258-259
    if (the source predicate folded.startswith(_HARNESS_OWNED_PREFIXES) is truthy) {
      // Source: vvaharness/remediation_agent/policy/patch_content.py:259-259
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/remediation_agent/policy/patch_content.py:260-261
    if (the source predicate not _is_executable_source(path) is truthy) {
      // Source: vvaharness/remediation_agent/policy/patch_content.py:261-261
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/remediation_agent/policy/patch_content.py:262-270
    for each (lineno, text) in lines {
      // Source: vvaharness/remediation_agent/policy/patch_content.py:263-265
      if (the source predicate not text.strip() or _COMMENT_ONLY.match(text) or _is_prose_string(text) is truthy) {
        // Source: vvaharness/remediation_agent/policy/patch_content.py:265-265
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/remediation_agent/policy/patch_content.py:266-270
      for each (label, reason, patterns) in _RULES {
        // Source: vvaharness/remediation_agent/policy/patch_content.py:267-270
        if (the source predicate any((p.search(text) for p in patterns)) is truthy) {
          // Source: vvaharness/remediation_agent/policy/patch_content.py:268-269
          In source order: Evaluate issues.setdefault(path, []).append(source_template_269_24); retain side effects and discard the expression result.
          // Source: vvaharness/remediation_agent/policy/patch_content.py:270-270
          Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
        }
      }
    }
  }
  // Source: vvaharness/remediation_agent/policy/patch_content.py:271-271
  End this invocation with issues.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/policy/patch_content.py:274-290
// Source signature: undeclared_edited_files(diff_text: str | None, declared: Iterable[str]) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn undeclared_edited_files(diff_text, declared) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/policy/patch_content.py:277-284
  In source order: Retain source documentation literal source_literal_277_4; it is not a model call.
  // Source: vvaharness/remediation_agent/policy/patch_content.py:285-288
  Perform the following protected operations {
    // Source: vvaharness/remediation_agent/policy/patch_content.py:286-286
    In source order: Evaluate once added_lines_by_file(diff_text); assign in source target order to touched.
  }
  // Source: vvaharness/remediation_agent/policy/patch_content.py:287-288
  On the first matching source exception Exception, in handler order {
    // Source: vvaharness/remediation_agent/policy/patch_content.py:288-288
    End this invocation with [].
  }
  // Source: vvaharness/remediation_agent/policy/patch_content.py:289-289
  In source order: Evaluate once {_fold(d) for d in declared if d}; assign in source target order to want.
  // Source: vvaharness/remediation_agent/policy/patch_content.py:290-290
  End this invocation with sorted((p for p in touched if _fold(p) not in want)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/policy/patch_content.py:293-294
// Source signature: _fold(path: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _fold(path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/policy/patch_content.py:294-294
  End this invocation with (path or '').replace('\\', '/').lstrip('./').casefold().
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/policy/patch_content.py:297-300
// Source signature: _snippet(text: str, limit: int=120) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _snippet(text, limit) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/policy/patch_content.py:298-299
  In source order: Retain source documentation literal source_literal_298_4; it is not a model call. Then Evaluate once ' '.join(text.split()); assign in source target order to flat.
  // Source: vvaharness/remediation_agent/policy/patch_content.py:300-300
  End this invocation with flat if len(flat) <= limit else flat[:limit - 1] + '…'.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/policy/patch_content.py:303-303
In source order: Evaluate once ['added_lines_by_file', 'scan_added_lines', 'undeclared_edited_files']; assign in source target order to __all__.
```

## Local import links

- `from vvaharness.remediation_agent.frameworks import language_for` at source line 232: `source_detail/vvaharness/remediation_agent/frameworks.py.sudo.md`.
