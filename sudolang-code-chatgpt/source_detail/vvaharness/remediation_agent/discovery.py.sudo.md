# vvaharness/remediation_agent/discovery.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/remediation_agent/discovery.py.evidence.json`. SHA-256: `49729706ad9625c4093c39aa3c1f8fc69a959f799f1c42c3646a8ed00630e6cd`.

```sudo
// Source: vvaharness/remediation_agent/discovery.py:15-22
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from dataclasses import dataclass; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from vvaharness.models import FinalReport; preserve alias and import-time effects.
// Source: vvaharness/remediation_agent/discovery.py:23-30
In source order: Resolve source import from vvaharness.models.case import FindingCase; preserve alias and import-time effects. Then Resolve source import from vvaharness.models.vocab import CaseState; preserve alias and import-time effects. Then Resolve source import from vvaharness.orchestrator.artifacts import artifact_dir; preserve alias and import-time effects. Then Resolve source import from vvaharness.orchestrator.checkpoints import run_id_for; preserve alias and import-time effects. Then Resolve source import from vvaharness.orchestrator.findings_json import findings_json_path, read_findings_json; preserve alias and import-time effects.
// Source: vvaharness/remediation_agent/discovery.py:31-46
In source order: Resolve source import from vvaharness.remediation_agent.report_parser import REMEDIATION_DIR_NAME, SCAN_DIR_NAME, find_scan_dir, latest_report, parse_findings; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.select import drop_non_main_channel, select_top_logged; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.target import RemediationTarget; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import console; preserve alias and import-time effects. Then Evaluate once ['Findings', 'Layout', 'completed_case_ids', 'cvss_score_of', 'load_findings', 'locate_report', 'prepare_layout']; assign in source target order to __all__.
// Source: vvaharness/remediation_agent/discovery.py:48-48
In source order: Evaluate once 'checkpoints'; assign in source target order to CHECKPOINTS_DIR_NAME.
// Source: vvaharness/remediation_agent/discovery.py:51-56
// Source signature: _mtime(path: Path) -> float | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _mtime(path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/discovery.py:52-52
  In source order: Retain source documentation literal source_literal_52_4; it is not a model call.
  // Source: vvaharness/remediation_agent/discovery.py:53-56
  Perform the following protected operations {
    // Source: vvaharness/remediation_agent/discovery.py:54-54
    End this invocation with path.stat().st_mtime.
  }
  // Source: vvaharness/remediation_agent/discovery.py:55-56
  On the first matching source exception OSError, in handler order {
    // Source: vvaharness/remediation_agent/discovery.py:56-56
    End this invocation with None.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/discovery.py:59-72
// Source signature: locate_report(repo_path: Path) -> tuple[Path | None, int]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn locate_report(repo_path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/discovery.py:60-61
  In source order: Retain source documentation literal source_literal_60_4; it is not a model call. Then Evaluate once find_scan_dir(repo_path); assign in source target order to scan_dir.
  // Source: vvaharness/remediation_agent/discovery.py:62-65
  if (the source predicate scan_dir is None is truthy) {
    // Source: vvaharness/remediation_agent/discovery.py:63-64
    In source order: Evaluate console.mark('fail', source_template_63_29, indent=2); retain side effects and discard the expression result.
    // Source: vvaharness/remediation_agent/discovery.py:65-65
    End this invocation with (None, 1).
  }
  // Source: vvaharness/remediation_agent/discovery.py:67-67
  In source order: Evaluate once latest_report(scan_dir); assign in source target order to report.
  // Source: vvaharness/remediation_agent/discovery.py:68-71
  if (the source predicate report is None is truthy) {
    // Source: vvaharness/remediation_agent/discovery.py:69-70
    In source order: Evaluate console.mark('fail', source_template_69_29, indent=2); retain side effects and discard the expression result.
    // Source: vvaharness/remediation_agent/discovery.py:71-71
    End this invocation with (None, 1).
  }
  // Source: vvaharness/remediation_agent/discovery.py:72-72
  End this invocation with (report, 0).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/discovery.py:75-77
// Source signature: cvss_score_of(target: RemediationTarget) -> float | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn cvss_score_of(target) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/discovery.py:76-76
  In source order: Retain source documentation literal source_literal_76_4; it is not a model call.
  // Source: vvaharness/remediation_agent/discovery.py:77-77
  End this invocation with target.finding.cvss_score.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/discovery.py:81-85
// Source: vvaharness/remediation_agent/discovery.py:80-80
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vvaharness/remediation_agent/discovery.py:81-85
interface Findings {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/remediation_agent/discovery.py:82-85
  In source order: Retain source documentation literal source_literal_82_4; it is not a model call. Then For selected, declare without assigning a value; source annotation list[RemediationTarget]. Then For discovered, declare without assigning a value; source annotation list[RemediationTarget].
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vvaharness/remediation_agent/discovery.py:88-104
// Source signature: completed_case_ids(repo_path: Path, *, since: float | None=None) -> set[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn completed_case_ids(repo_path, since) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/discovery.py:90-91
  In source order: Retain source documentation literal source_literal_90_4; it is not a model call. Then For done, assign set(); source annotation set[str].
  // Source: vvaharness/remediation_agent/discovery.py:92-102
  for each case_path in sorted((repo_path / REMEDIATION_DIR_NAME).glob('*/finding_case.json')) {
    // Source: vvaharness/remediation_agent/discovery.py:94-100
    Perform the following protected operations {
      // Source: vvaharness/remediation_agent/discovery.py:95-96
      if (the source predicate since is not None and case_path.stat().st_mtime < since is truthy) {
        // Source: vvaharness/remediation_agent/discovery.py:96-96
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/remediation_agent/discovery.py:97-98
      In source order: Evaluate once FindingCase.model_validate_json(case_path.read_text(encoding='utf-8')); assign in source target order to case.
    }
    // Source: vvaharness/remediation_agent/discovery.py:99-100
    On the first matching source exception (OSError, ValueError), in handler order {
      // Source: vvaharness/remediation_agent/discovery.py:100-100
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/remediation_agent/discovery.py:101-102
    if (the source predicate case.state in (CaseState.REMEDIATED, CaseState.VALIDATED) is truthy) {
      // Source: vvaharness/remediation_agent/discovery.py:102-102
      In source order: Evaluate done.add(case.case_id); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/remediation_agent/discovery.py:103-103
  In source order: Evaluate done.discard(''); retain side effects and discard the expression result.
  // Source: vvaharness/remediation_agent/discovery.py:104-104
  End this invocation with done.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/discovery.py:107-118
// Source signature: _targets_from_typed(report: FinalReport, done: set[str]) -> list[RemediationTarget]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _targets_from_typed(report, done) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/discovery.py:109-111
  In source order: Retain source documentation literal source_literal_109_4; it is not a model call. Then Evaluate once []; assign in source target order to targets.
  // Source: vvaharness/remediation_agent/discovery.py:112-117
  for each (i, rf) in enumerate(report.findings, 1) {
    // Source: vvaharness/remediation_agent/discovery.py:113-117
    In source order: Evaluate once rf.finding; assign in source target order to f. Then Evaluate once rf.severity; assign in source target order to f.severity. Then Evaluate once RemediationTarget(finding=f, index=i); assign in source target order to t. Then Evaluate once t.case_id in done; assign in source target order to t.done. Then Evaluate targets.append(t); retain side effects and discard the expression result.
  }
  // Source: vvaharness/remediation_agent/discovery.py:118-118
  End this invocation with drop_non_main_channel(targets, log_prefix='[Remediation Agent]').
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/discovery.py:121-140
// Source signature: load_findings(repo_path: Path, report: Path, top: int | None) -> Findings
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn load_findings(repo_path, report, top) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/discovery.py:122-128
  In source order: Retain source documentation literal source_literal_122_4; it is not a model call. Then Evaluate once read_findings_json(repo_path); assign in source target order to typed. Then Evaluate once completed_case_ids(repo_path, since=_mtime(findings_json_path(repo_path) if typed is not None else report)); assign in source target order to done.
  // Source: vvaharness/remediation_agent/discovery.py:129-137
  if (the source predicate typed is not None is truthy) {
    // Source: vvaharness/remediation_agent/discovery.py:130-131
    In source order: Evaluate console.write('  [Remediation Agent] source: findings.json (typed scan result)'); retain side effects and discard the expression result. Then Evaluate once _targets_from_typed(typed, done); assign in source target order to discovered.
  }
  else {
    // Source: vvaharness/remediation_agent/discovery.py:133-135
    In source order: Evaluate console.write('  [Remediation Agent] source: legacy Markdown parse (this checkout has no findings.json — older scan)'); retain side effects and discard the expression result. Then Evaluate once parse_findings(report.read_text(encoding='utf-8')); assign in source target order to discovered.
    // Source: vvaharness/remediation_agent/discovery.py:136-137
    for each t in discovered {
      // Source: vvaharness/remediation_agent/discovery.py:137-137
      In source order: Evaluate once t.done or t.case_id in done; assign in source target order to t.done.
    }
  }
  // Source: vvaharness/remediation_agent/discovery.py:138-139
  In source order: Evaluate once select_top_logged(discovered, top, score_of=cvss_score_of, log_prefix='[Remediation Agent]'); assign in source target order to selected.
  // Source: vvaharness/remediation_agent/discovery.py:140-140
  End this invocation with Findings(selected=selected, discovered=discovered).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/discovery.py:144-148
// Source: vvaharness/remediation_agent/discovery.py:143-143
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vvaharness/remediation_agent/discovery.py:144-148
interface Layout {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/remediation_agent/discovery.py:145-148
  In source order: Retain source documentation literal source_literal_145_4; it is not a model call. Then For rem_dir, declare without assigning a value; source annotation Path. Then For ckpt_dir, declare without assigning a value; source annotation Path. Then For run_id, declare without assigning a value; source annotation str.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vvaharness/remediation_agent/discovery.py:151-163
// Source signature: prepare_layout(repo_path: Path) -> Layout
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn prepare_layout(repo_path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/discovery.py:152-158
  In source order: Retain source documentation literal source_literal_152_4; it is not a model call. Then Evaluate once artifact_dir(repo_path, REMEDIATION_DIR_NAME); assign in source target order to rem_dir. Then Evaluate rem_dir.mkdir(exist_ok=True); retain side effects and discard the expression result.
  // Source: vvaharness/remediation_agent/discovery.py:159-163
  End this invocation with Layout(rem_dir=rem_dir, ckpt_dir=repo_path / CHECKPOINTS_DIR_NAME, run_id=run_id_for(repo_path)).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.models import FinalReport` at source line 22: `source_detail/vvaharness/models/__init__.py.sudo.md`.
- `from vvaharness.models.case import FindingCase` at source line 23: `source_detail/vvaharness/models/case.py.sudo.md`.
- `from vvaharness.models.vocab import CaseState` at source line 24: `source_detail/vvaharness/models/vocab.py.sudo.md`.
- `from vvaharness.orchestrator.artifacts import artifact_dir` at source line 25: `source_detail/vvaharness/orchestrator/artifacts.py.sudo.md`.
- `from vvaharness.orchestrator.checkpoints import run_id_for` at source line 26: `source_detail/vvaharness/orchestrator/checkpoints.py.sudo.md`.
- `from vvaharness.orchestrator.findings_json import findings_json_path, read_findings_json` at source line 27: `source_detail/vvaharness/orchestrator/findings_json.py.sudo.md`.
- `from vvaharness.remediation_agent.report_parser import REMEDIATION_DIR_NAME, SCAN_DIR_NAME, find_scan_dir, latest_report, parse_findings` at source line 31: `source_detail/vvaharness/remediation_agent/report_parser/__init__.py.sudo.md`.
- `from vvaharness.remediation_agent.select import drop_non_main_channel, select_top_logged` at source line 38: `source_detail/vvaharness/remediation_agent/select/__init__.py.sudo.md`.
- `from vvaharness.remediation_agent.target import RemediationTarget` at source line 42: `source_detail/vvaharness/remediation_agent/target.py.sudo.md`.
- `from vvaharness.util import console` at source line 43: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import console` at source line 43: `source_detail/vvaharness/util/console.py.sudo.md`.
