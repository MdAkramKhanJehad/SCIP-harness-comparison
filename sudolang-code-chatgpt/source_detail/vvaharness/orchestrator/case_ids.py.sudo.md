# vvaharness/orchestrator/case_ids.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/orchestrator/case_ids.py.evidence.json`. SHA-256: `abe36e438a0cb218e61952108e6fbe195b016ccbab28e4cdd9c5b01a4807d0be`.

```sudo
// Source: vvaharness/orchestrator/case_ids.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import hashlib; preserve alias and import-time effects. Then Resolve source import import unicodedata; preserve alias and import-time effects. Then Resolve source import from typing import Final; preserve alias and import-time effects.
// Source: vvaharness/orchestrator/case_ids.py:23-34
In source order: Resolve source import from vvaharness.models import FinalReport, Finding; preserve alias and import-time effects. Then Evaluate once ['CASE_ID_PREFIX', 'LINE_BUCKET', 'mint_case_ids']; assign in source target order to __all__. Then For CASE_ID_PREFIX, assign 'vvaf1_'; source annotation Final. Then For LINE_BUCKET, assign 10; source annotation Final. Then For _DIGEST_CHARS, assign 32; source annotation Final.
// Source: vvaharness/orchestrator/case_ids.py:37-45
// Source signature: _rel_posix(repo_root: str, raw: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _rel_posix(repo_root, raw) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/case_ids.py:38-40
  In source order: Retain source documentation literal source_literal_38_4; it is not a model call. Then Evaluate once unicodedata.normalize('NFC', (raw or '').replace('\\', '/')).strip(); assign in source target order to text. Then Evaluate once unicodedata.normalize('NFC', (repo_root or '').replace('\\', '/')).rstrip('/'); assign in source target order to root.
  // Source: vvaharness/orchestrator/case_ids.py:41-42
  if (the source predicate root and text.startswith(source_template_41_32) is truthy) {
    // Source: vvaharness/orchestrator/case_ids.py:42-42
    In source order: Evaluate once text[len(root) + 1:]; assign in source target order to text.
  }
  // Source: vvaharness/orchestrator/case_ids.py:43-44
  while (the source predicate text.startswith('./') is truthy) {
    // Source: vvaharness/orchestrator/case_ids.py:44-44
    In source order: Evaluate once text[2:]; assign in source target order to text.
  }
  // Source: vvaharness/orchestrator/case_ids.py:45-45
  End this invocation with text.lstrip('/').
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/case_ids.py:48-53
// Source signature: _material(repo_root: str, finding: Finding) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _material(repo_root, finding) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/case_ids.py:49-52
  In source order: Retain source documentation literal source_literal_49_4; it is not a model call. Then Evaluate once _rel_posix(repo_root, finding.file); assign in source target order to path. Then Evaluate once finding.line_start // LINE_BUCKET; assign in source target order to bucket. Then Evaluate once finding.cwe or finding.vuln_class.value; assign in source target order to klass.
  // Source: vvaharness/orchestrator/case_ids.py:53-53
  End this invocation with source_template_53_11.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/case_ids.py:56-59
// Source signature: _digest(material: str, salt: int) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _digest(material, salt) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/case_ids.py:57-58
  In source order: Retain source documentation literal source_literal_57_4; it is not a model call. Then Evaluate once material if salt == 0 else source_template_58_37; assign in source target order to raw.
  // Source: vvaharness/orchestrator/case_ids.py:59-59
  End this invocation with CASE_ID_PREFIX + hashlib.sha256(raw.encode('utf-8')).hexdigest()[:_DIGEST_CHARS].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/case_ids.py:62-71
// Source signature: _tiebreak_key(finding: Finding) -> tuple[int, int, str, str, str, str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _tiebreak_key(finding) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/case_ids.py:63-63
  In source order: Retain source documentation literal source_literal_63_4; it is not a model call.
  // Source: vvaharness/orchestrator/case_ids.py:64-71
  End this invocation with (finding.line_start, finding.line_end, finding.title, finding.chunk_id, finding.source_ref or '', finding.sink_ref or '').
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/case_ids.py:74-79
// Source signature: _claim(material: str, taken: set[str]) -> tuple[str, int]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _claim(material, taken) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/case_ids.py:75-76
  In source order: Retain source documentation literal source_literal_75_4; it is not a model call. Then Evaluate once 0; assign in source target order to salt.
  // Source: vvaharness/orchestrator/case_ids.py:77-78
  while (the source predicate _digest(material, salt) in taken is truthy) {
    // Source: vvaharness/orchestrator/case_ids.py:78-78
    In source order: Apply source augmented assignment salt += 1 with source evaluation/in-place semantics.
  }
  // Source: vvaharness/orchestrator/case_ids.py:79-79
  End this invocation with (_digest(material, salt), salt).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/case_ids.py:82-97
// Source signature: _assert_unique(findings: list[Finding]) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _assert_unique(findings) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/case_ids.py:83-84
  In source order: Retain source documentation literal source_literal_83_4; it is not a model call. Then For seen, assign {}; source annotation dict[str, Finding].
  // Source: vvaharness/orchestrator/case_ids.py:85-97
  for each finding in findings {
    // Source: vvaharness/orchestrator/case_ids.py:86-88
    if (the source predicate not finding.case_id is truthy) {
      // Source: vvaharness/orchestrator/case_ids.py:87-87
      In source order: Evaluate once source_template_87_18; assign in source target order to msg.
      // Source: vvaharness/orchestrator/case_ids.py:88-88
      Raise ValueError(msg).
    }
    // Source: vvaharness/orchestrator/case_ids.py:89-89
    In source order: Evaluate once seen.get(finding.case_id); assign in source target order to clash.
    // Source: vvaharness/orchestrator/case_ids.py:90-96
    if (the source predicate clash is not None is truthy) {
      // Source: vvaharness/orchestrator/case_ids.py:91-95
      In source order: Evaluate once source_template_92_16; assign in source target order to msg.
      // Source: vvaharness/orchestrator/case_ids.py:96-96
      Raise ValueError(msg).
    }
    // Source: vvaharness/orchestrator/case_ids.py:97-97
    In source order: Evaluate once finding; assign in source target order to seen[finding.case_id].
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/case_ids.py:100-122
// Source signature: mint_case_ids(report: FinalReport) -> dict[str, int]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn mint_case_ids(report) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/case_ids.py:101-104
  In source order: Retain source documentation literal source_literal_101_4; it is not a model call. Then Evaluate once [ranked.finding for ranked in report.findings]; assign in source target order to findings. Then Evaluate once {f.case_id for f in findings if f.case_id}; assign in source target order to taken. Then For pending, assign {}; source annotation dict[str, list[Finding]].
  // Source: vvaharness/orchestrator/case_ids.py:105-107
  for each finding in findings {
    // Source: vvaharness/orchestrator/case_ids.py:106-107
    if (the source predicate not finding.case_id is truthy) {
      // Source: vvaharness/orchestrator/case_ids.py:107-107
      In source order: Evaluate pending.setdefault(_material(report.repo_root, finding), []).append(finding); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/orchestrator/case_ids.py:108-109
  In source order: Evaluate once 0; assign in source target order to minted. Then Evaluate once 0; assign in source target order to collisions.
  // Source: vvaharness/orchestrator/case_ids.py:110-116
  for each (material, group) in pending.items() {
    // Source: vvaharness/orchestrator/case_ids.py:111-116
    for each finding in sorted(group, key=_tiebreak_key) {
      // Source: vvaharness/orchestrator/case_ids.py:112-116
      In source order: Evaluate once _claim(material, taken); assign in source target order to (case_id, salt). Then Evaluate once case_id; assign in source target order to finding.case_id. Then Evaluate taken.add(case_id); retain side effects and discard the expression result. Then Apply source augmented assignment minted += 1 with source evaluation/in-place semantics. Then Apply source augmented assignment collisions += 1 if salt else 0 with source evaluation/in-place semantics.
    }
  }
  // Source: vvaharness/orchestrator/case_ids.py:117-117
  In source order: Evaluate _assert_unique(findings); retain side effects and discard the expression result.
  // Source: vvaharness/orchestrator/case_ids.py:118-122
  End this invocation with {'minted': minted, 'collisions': collisions, 'preassigned': len(findings) - minted}.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.models import FinalReport, Finding` at source line 23: `source_detail/vvaharness/models/__init__.py.sudo.md`.
