# vvaharness/plugins/semgrep/findings.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/plugins/semgrep/findings.py.evidence.json`. SHA-256: `1541b00f38075a264f00e823cdf9b07a47bda1dc07293c6dd2deceb13676227b`.

```sudo
// Source: vvaharness/plugins/semgrep/findings.py:15-20
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import json; preserve alias and import-time effects. Then Resolve source import import re; preserve alias and import-time effects. Then Resolve source import from pathlib import Path, PurePosixPath; preserve alias and import-time effects.
// Source: vvaharness/plugins/semgrep/findings.py:22-26
In source order: Resolve source import from vvaharness.models import Finding, VulnClass; preserve alias and import-time effects. Then Resolve source import from vvaharness.report.cwe import cwe_name; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import logs; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.counters import COUNTERS; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.events import Event; preserve alias and import-time effects.
// Source: vvaharness/plugins/semgrep/findings.py:28-33
In source order: Evaluate once logs.get_logger(__name__); assign in source target order to log. Then Evaluate once 2000; assign in source target order to MAX_FINDINGS. Then Evaluate once 64 * 1024 * 1024; assign in source target order to MAX_JSON_BYTES. Then Evaluate once 2000; assign in source target order to _MAX_SNIPPET_CHARS. Then Evaluate once 200; assign in source target order to _MAX_TITLE_CHARS.
// Source: vvaharness/plugins/semgrep/findings.py:34-68
In source order: Evaluate once 120; assign in source target order to _MAX_LABEL_CHARS. Then Evaluate once re.compile('CWE-(\\d{1,5})'); assign in source target order to _CWE_RE. Then For _CWE_TO_CLASS, assign {77: VulnClass.INJECTION, 78: VulnClass.INJECTION, 79: VulnClass.INJECTION, 89: VulnClass.INJECTION, 90: VulnClass.INJECTION, 91: VulnClass.INJECTION, 94: VulnClass.INJECTION, 95: VulnClass.INJECTION, 611: VulnClass.INJECTION, 643: VulnClass.INJECTION, 917: VulnClass.INJECTION, 502: VulnClass.DESERIALIZATION, 190: VulnClass.INT_OVERFLOW, 191: VulnClass.INT_OVERFLOW, 362: VulnClass.RACE, 367: VulnClass.RACE, 134: VulnClass.FMT_STRING, 416: VulnClass.UAF, 121: VulnClass.STACK_OVERFLOW, 122: VulnClass.HEAP_OVERFLOW, 787: VulnClass.HEAP_OVERFLOW, 843: VulnClass.TYPE_CONFUSION, 200: VulnClass.INFO_LEAK, 209: VulnClass.INFO_LEAK, 532: VulnClass.INFO_LEAK, 22: VulnClass.LOGIC, 287: VulnClass.LOGIC, 306: VulnClass.LOGIC, 352: VulnClass.LOGIC, 862: VulnClass.LOGIC, 863: VulnClass.LOGIC, 88: VulnClass.INJECTION, 117: VulnClass.INJECTION, 470: VulnClass.INJECTION, 943: VulnClass.INJECTION, 1336: VulnClass.INJECTION, 704: VulnClass.TYPE_CONFUSION, 215: VulnClass.INFO_LEAK, 311: VulnClass.INFO_LEAK, 312: VulnClass.INFO_LEAK, 313: VulnClass.INFO_LEAK, 315: VulnClass.INFO_LEAK, 319: VulnClass.INFO_LEAK, 359: VulnClass.INFO_LEAK, 497: VulnClass.INFO_LEAK, 522: VulnClass.INFO_LEAK, 614: VulnClass.INFO_LEAK, 798: VulnClass.INFO_LEAK}; source annotation dict[int, VulnClass]. Then Evaluate once {'ERROR': 'high', 'WARNING': 'medium', 'INFO': 'low'}; assign in source target order to _SEVERITY.
// Source: vvaharness/plugins/semgrep/findings.py:71-72
interface SemgrepFindingsError {
  Describe the source Python type, preserving its base/metaclass expression order: ValueError.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/plugins/semgrep/findings.py:72-72
  In source order: Retain source documentation literal source_literal_72_4; it is not a model call.
}
// Source: vvaharness/plugins/semgrep/findings.py:75-77
// Source signature: _posix(value: str) -> PurePosixPath
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _posix(value) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/plugins/semgrep/findings.py:76-76
  In source order: Retain source documentation literal source_literal_76_4; it is not a model call.
  // Source: vvaharness/plugins/semgrep/findings.py:77-77
  End this invocation with PurePosixPath(value.replace('\\', '/')).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/plugins/semgrep/findings.py:80-82
// Source signature: _under(base: PurePosixPath, candidate: PurePosixPath) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _under(base, candidate) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/plugins/semgrep/findings.py:81-81
  In source order: Retain source documentation literal source_literal_81_4; it is not a model call.
  // Source: vvaharness/plugins/semgrep/findings.py:82-82
  End this invocation with str(candidate.relative_to(base)) if candidate.is_relative_to(base) else ''.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/plugins/semgrep/findings.py:85-98
// Source signature: relative_path(path: str, root: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn relative_path(path, root) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/plugins/semgrep/findings.py:86-87
  In source order: Retain source documentation literal source_literal_86_4; it is not a model call. Then Evaluate once _posix(path); assign in source target order to candidate.
  // Source: vvaharness/plugins/semgrep/findings.py:88-89
  if (the source predicate not root or not candidate.is_absolute() is truthy) {
    // Source: vvaharness/plugins/semgrep/findings.py:89-89
    End this invocation with str(candidate) if str(candidate) not in ('.', '') else path.
  }
  // Source: vvaharness/plugins/semgrep/findings.py:90-91
  In source order: Evaluate once _posix(str(Path(root).resolve())); assign in source target order to base. Then Evaluate once _under(base, candidate) or _under(base, _posix(str(Path(path).resolve()))); assign in source target order to under.
  // Source: vvaharness/plugins/semgrep/findings.py:92-93
  if (the source predicate under is truthy) {
    // Source: vvaharness/plugins/semgrep/findings.py:93-93
    End this invocation with under.
  }
  // Source: vvaharness/plugins/semgrep/findings.py:94-97
  In source order: Evaluate COUNTERS.bump('semgrep_path_outside_repo'); retain side effects and discard the expression result. Then Evaluate log.warning(Event.SEMGREP_PATH_NOT_RELATIVE, path=str(candidate), repo_root=str(base), detail='this finding keeps an absolute path, so S5 drops it as a file that is not in the repo inventory'); retain side effects and discard the expression result.
  // Source: vvaharness/plugins/semgrep/findings.py:98-98
  End this invocation with str(candidate).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/plugins/semgrep/findings.py:101-109
// Source signature: _cwe_ids(metadata: dict) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _cwe_ids(metadata) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/plugins/semgrep/findings.py:102-105
  In source order: Retain source documentation literal source_literal_102_4; it is not a model call. Then Evaluate once metadata.get('cwe') or []; assign in source target order to raw. Then Evaluate once [raw] if isinstance(raw, str) else [v for v in raw if isinstance(v, str)]; assign in source target order to values. Then For seen, assign {}; source annotation dict[str, None].
  // Source: vvaharness/plugins/semgrep/findings.py:106-108
  for each value in values {
    // Source: vvaharness/plugins/semgrep/findings.py:107-108
    for each match in _CWE_RE.finditer(value) {
      // Source: vvaharness/plugins/semgrep/findings.py:108-108
      In source order: Evaluate seen.setdefault(source_template_108_28, None); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/plugins/semgrep/findings.py:109-109
  End this invocation with list(seen).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/plugins/semgrep/findings.py:112-118
// Source signature: _vuln_class(cwes: list[str]) -> VulnClass
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _vuln_class(cwes) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/plugins/semgrep/findings.py:113-113
  In source order: Retain source documentation literal source_literal_113_4; it is not a model call.
  // Source: vvaharness/plugins/semgrep/findings.py:114-117
  for each cwe in cwes {
    // Source: vvaharness/plugins/semgrep/findings.py:115-115
    In source order: Evaluate once _CWE_TO_CLASS.get(int(cwe.removeprefix('CWE-'))); assign in source target order to mapped.
    // Source: vvaharness/plugins/semgrep/findings.py:116-117
    if (the source predicate mapped is not None is truthy) {
      // Source: vvaharness/plugins/semgrep/findings.py:117-117
      End this invocation with mapped.
    }
  }
  // Source: vvaharness/plugins/semgrep/findings.py:118-118
  End this invocation with VulnClass.OTHER.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/plugins/semgrep/findings.py:121-126
// Source signature: _label(metadata: dict, cwes: list[str]) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _label(metadata, cwes) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/plugins/semgrep/findings.py:122-125
  In source order: Retain source documentation literal source_literal_122_4; it is not a model call. Then Evaluate once metadata.get('vulnerability_class') or []; assign in source target order to raw. Then Evaluate once [raw] if isinstance(raw, str) else [v for v in raw if isinstance(v, str)]; assign in source target order to values. Then Evaluate once next((v.strip() for v in values if v.strip()), ''); assign in source target order to authored.
  // Source: vvaharness/plugins/semgrep/findings.py:126-126
  End this invocation with authored or next((cwe_name(c) for c in cwes if cwe_name(c)), '').
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/plugins/semgrep/findings.py:129-158
// Source signature: _finding(result: dict, root: str) -> Finding | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _finding(result, root) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/plugins/semgrep/findings.py:130-132
  In source order: Retain source documentation literal source_literal_130_4; it is not a model call. Then Evaluate once result.get('path'); assign in source target order to raw_path. Then Evaluate once (result.get('start') or {}).get('line'); assign in source target order to start.
  // Source: vvaharness/plugins/semgrep/findings.py:133-134
  if (the source predicate not isinstance(raw_path, str) or not isinstance(start, int) is truthy) {
    // Source: vvaharness/plugins/semgrep/findings.py:134-134
    End this invocation with None.
  }
  // Source: vvaharness/plugins/semgrep/findings.py:135-139
  In source order: Evaluate once relative_path(raw_path, root); assign in source target order to path. Then Evaluate once result.get('extra') or {}; assign in source target order to extra. Then Evaluate once extra.get('metadata') or {}; assign in source target order to metadata. Then Evaluate once _cwe_ids(metadata); assign in source target order to cwes. Then Evaluate once _vuln_class(cwes); assign in source target order to vuln_class.
  // Source: vvaharness/plugins/semgrep/findings.py:140-149
  In source order: Evaluate once str(result.get('check_id') or 'semgrep'); assign in source target order to rule_id. Then Evaluate once str(extra.get('message') or rule_id); assign in source target order to message. Then Evaluate once {'line_end': (result.get('end') or {}).get('line'), 'cwe': cwes[0] if cwes else None, 'severity': _SEVERITY.get(str(extra.get('severity', '')).upper()), 'code_snippet': str(extra.get('lines') or '')[:_MAX_SNIPPET_CHARS] or None, 'vuln_class_label': _label(metadata, cwes)[:_MAX_LABEL_CHARS] if vuln_class is VulnClass.OTHER else None}; assign in source target order to optional.
  // Source: vvaharness/plugins/semgrep/findings.py:150-158
  End this invocation with Finding(title=message.strip().splitlines()[0][:_MAX_TITLE_CHARS] or rule_id, file=path, line_start=start, vuln_class=vuln_class, description=message, origin=source_template_156_15, **{k: v for k, v in optional.items() if v is not None}).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/plugins/semgrep/findings.py:161-173
// Source signature: findings_from_semgrep(payload: Path | str | dict, *, repo: Path | str | None=None) -> list[Finding]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn findings_from_semgrep(payload, repo) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/plugins/semgrep/findings.py:163-168
  In source order: Retain source documentation literal source_literal_163_4; it is not a model call. Then Evaluate once payload if isinstance(payload, dict) else read_semgrep_json(Path(payload)); assign in source target order to document. Then Evaluate once '' if repo is None else str(repo); assign in source target order to root. Then Evaluate once document.get('results'); assign in source target order to results.
  // Source: vvaharness/plugins/semgrep/findings.py:169-170
  if (the source predicate not isinstance(results, list) is truthy) {
    // Source: vvaharness/plugins/semgrep/findings.py:170-170
    Raise SemgrepFindingsError("semgrep JSON has no 'results' list").
  }
  // Source: vvaharness/plugins/semgrep/findings.py:171-172
  if (the source predicate len(results) > MAX_FINDINGS is truthy) {
    // Source: vvaharness/plugins/semgrep/findings.py:172-172
    Raise SemgrepFindingsError(source_template_172_35).
  }
  // Source: vvaharness/plugins/semgrep/findings.py:173-173
  End this invocation with [f for r in results if isinstance(r, dict) and (f := _finding(r, root)) is not None].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/plugins/semgrep/findings.py:176-186
// Source signature: read_semgrep_json(path: Path) -> dict
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn read_semgrep_json(path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/plugins/semgrep/findings.py:177-177
  In source order: Retain source documentation literal source_literal_177_4; it is not a model call.
  // Source: vvaharness/plugins/semgrep/findings.py:178-183
  Perform the following protected operations {
    // Source: vvaharness/plugins/semgrep/findings.py:179-180
    if (the source predicate path.stat().st_size > MAX_JSON_BYTES is truthy) {
      // Source: vvaharness/plugins/semgrep/findings.py:180-180
      Raise SemgrepFindingsError(source_template_180_39).
    }
    // Source: vvaharness/plugins/semgrep/findings.py:181-181
    In source order: Evaluate once json.loads(path.read_text(encoding='utf-8')); assign in source target order to document.
  }
  // Source: vvaharness/plugins/semgrep/findings.py:182-183
  On the first matching source exception (OSError, json.JSONDecodeError) as exc, in handler order {
    // Source: vvaharness/plugins/semgrep/findings.py:183-183
    Raise SemgrepFindingsError(source_template_183_35) with explicit source cause exc.
  }
  // Source: vvaharness/plugins/semgrep/findings.py:184-185
  if (the source predicate not isinstance(document, dict) is truthy) {
    // Source: vvaharness/plugins/semgrep/findings.py:185-185
    Raise SemgrepFindingsError(source_template_185_35).
  }
  // Source: vvaharness/plugins/semgrep/findings.py:186-186
  End this invocation with document.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/plugins/semgrep/findings.py:189-196
In source order: Evaluate once ['MAX_FINDINGS', 'MAX_JSON_BYTES', 'SemgrepFindingsError', 'findings_from_semgrep', 'read_semgrep_json', 'relative_path']; assign in source target order to __all__.
```

## Local import links

- `from vvaharness.models import Finding, VulnClass` at source line 22: `source_detail/vvaharness/models/__init__.py.sudo.md`.
- `from vvaharness.report.cwe import cwe_name` at source line 23: `source_detail/vvaharness/report/cwe.py.sudo.md`.
- `from vvaharness.util import logs` at source line 24: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import logs` at source line 24: `source_detail/vvaharness/util/logs.py.sudo.md`.
- `from vvaharness.util.counters import COUNTERS` at source line 25: `source_detail/vvaharness/util/counters.py.sudo.md`.
- `from vvaharness.util.events import Event` at source line 26: `source_detail/vvaharness/util/events.py.sudo.md`.
