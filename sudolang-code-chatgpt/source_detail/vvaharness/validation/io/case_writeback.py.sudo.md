# vvaharness/validation/io/case_writeback.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/validation/io/case_writeback.py.evidence.json`. SHA-256: `135f6f68337409bad39b3a7885d33f8de5b26d825586044da74305db3250b349`.

```sudo
// Source: vvaharness/validation/io/case_writeback.py:15-22
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from vvaharness.models import FindingCase, Provenance, ScoringPolicy, Verdict; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import logs; preserve alias and import-time effects.
// Source: vvaharness/validation/io/case_writeback.py:23-33
In source order: Resolve source import from vvaharness.validation.constants.artifacts import VALIDATION_REPORT_FILENAME; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.io._host_score import conformant, load_synthesized_gates, verdict_for; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.models.output import OutputFinding, ValidationReport; preserve alias and import-time effects. Then Evaluate once logs.get_logger(__name__); assign in source target order to log. Then Evaluate once ['write_back_verdict']; assign in source target order to __all__.
// Source: vvaharness/validation/io/case_writeback.py:36-47
// Source signature: _load_output_finding(workspace: Path, case_id: str) -> OutputFinding | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _load_output_finding(workspace, case_id) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/io/case_writeback.py:37-38
  In source order: Retain source documentation literal source_literal_37_4; it is not a model call. Then For report_path, assign workspace / VALIDATION_REPORT_FILENAME; source annotation Path.
  // Source: vvaharness/validation/io/case_writeback.py:39-43
  Perform the following protected operations {
    // Source: vvaharness/validation/io/case_writeback.py:40-40
    In source order: For report, assign ValidationReport.from_file(report_path); source annotation ValidationReport.
  }
  // Source: vvaharness/validation/io/case_writeback.py:41-43
  On the first matching source exception (OSError, ValueError), in handler order {
    // Source: vvaharness/validation/io/case_writeback.py:42-42
    In source order: Evaluate log.warning('no readable validation report at %s; recording INCONCLUSIVE', report_path); retain side effects and discard the expression result.
    // Source: vvaharness/validation/io/case_writeback.py:43-43
    End this invocation with None.
  }
  // Source: vvaharness/validation/io/case_writeback.py:44-46
  for each finding in report.findings {
    // Source: vvaharness/validation/io/case_writeback.py:45-46
    if (the source predicate finding.tracking_id == case_id is truthy) {
      // Source: vvaharness/validation/io/case_writeback.py:46-46
      End this invocation with finding.
    }
  }
  // Source: vvaharness/validation/io/case_writeback.py:47-47
  End this invocation with report.findings[0] if report.findings else None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/io/case_writeback.py:50-62
// Source signature: build_verdict(case: FindingCase, workspace: Path, *, provenance: Provenance, policy: ScoringPolicy | None=None, session_failed: bool=False) -> Verdict
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn build_verdict(case, workspace, provenance, policy, session_failed) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/io/case_writeback.py:58-61
  In source order: Retain source documentation literal source_literal_58_4; it is not a model call. Then Evaluate once _load_output_finding(workspace, case.case_id); assign in source target order to output_finding. Then Evaluate once None if session_failed else load_synthesized_gates(workspace).get(case.case_id); assign in source target order to gates. Then Evaluate once verdict_for(output_finding, gates, provenance=provenance, policy=policy); assign in source target order to scored.
  // Source: vvaharness/validation/io/case_writeback.py:62-62
  End this invocation with conformant(scored, policy).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/io/case_writeback.py:65-73
// Source signature: write_back_verdict(case: FindingCase, verdict: Verdict, path: Path) -> FindingCase | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn write_back_verdict(case, verdict, path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/io/case_writeback.py:66-66
  In source order: Retain source documentation literal source_literal_66_4; it is not a model call.
  // Source: vvaharness/validation/io/case_writeback.py:67-72
  Perform the following protected operations {
    // Source: vvaharness/validation/io/case_writeback.py:68-69
    In source order: Evaluate once case.with_verdict(verdict); assign in source target order to judged. Then Evaluate judged.write(path); retain side effects and discard the expression result.
  }
  // Source: vvaharness/validation/io/case_writeback.py:70-72
  On the first matching source exception (OSError, ValueError), in handler order {
    // Source: vvaharness/validation/io/case_writeback.py:71-71
    In source order: Evaluate log.warning('could not write verdict back to %s', path); retain side effects and discard the expression result.
    // Source: vvaharness/validation/io/case_writeback.py:72-72
    End this invocation with None.
  }
  // Source: vvaharness/validation/io/case_writeback.py:73-73
  End this invocation with judged.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.models import FindingCase, Provenance, ScoringPolicy, Verdict` at source line 21: `source_detail/vvaharness/models/__init__.py.sudo.md`.
- `from vvaharness.util import logs` at source line 22: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import logs` at source line 22: `source_detail/vvaharness/util/logs.py.sudo.md`.
- `from vvaharness.validation.constants.artifacts import VALIDATION_REPORT_FILENAME` at source line 23: `source_detail/vvaharness/validation/constants/artifacts.py.sudo.md`.
- `from vvaharness.validation.io._host_score import conformant, load_synthesized_gates, verdict_for` at source line 24: `source_detail/vvaharness/validation/io/_host_score.py.sudo.md`.
- `from vvaharness.validation.models.output import OutputFinding, ValidationReport` at source line 29: `source_detail/vvaharness/validation/models/output.py.sudo.md`.
