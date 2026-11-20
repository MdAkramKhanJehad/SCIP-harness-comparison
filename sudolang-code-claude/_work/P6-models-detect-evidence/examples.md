# Example, slice models (top level)

## finalize: outcome and run mode choose the remediation kind

Source `vvaharness/models/remediation.py:105-112`:
```python
def finalize(evidence: RemediationEvidence, *, mode: str, diff: str = "",
             files_touched: tuple[str, ...] = ()) -> Remediation:
    """Turn engine evidence into harness's contract, adding *diff*, *files_touched*, ``kind``."""
    fix_kind, report_kind, disposition = _KIND[evidence.outcome]
    kind = report_kind if mode in _REPORT_ONLY else fix_kind
    # edits_applied with no files touched and no diff is treated as already_resolved instead.
    if kind is RemediationKind.EDITS_APPLIED and not files_touched and not diff:
        kind = RemediationKind.ALREADY_RESOLVED
```

SudoLang `vvah/vvaharness/models/remediation.sudo`:
```
// src: vvaharness/models/remediation.py:105-125
fn finalize(evidence, mode, diff="", files_touched=[]):executor=code {
  [fix_kind, report_kind, disposition] = _KIND[evidence.outcome]
  kind = if (mode in _REPORT_ONLY) report_kind else fix_kind
  if (kind == "edits_applied" && files_touched is empty && diff is empty) kind = "already_resolved"
  return Remediation({ kind, summary: evidence.summary, disposition, diff, files_touched,
    changes, gates, root_cause, remaining_risks, recommendations, produced_by from evidence })
}
```

## Semgrep enricher refusal gate
Source `vvaharness/plugins/semgrep/enricher.py:342-352`:
```python
checks = (
    (context.cancellation.is_cancelled, "cancelled before the Semgrep scan started"),
    (not context.project.source_path, "the project carries no source path to scan"),
    (not self.configs and not self.rulesets, "no local rule files and no rulesets were configured"),
    (budget < MIN_BUDGET_SECONDS, f"{budget:.0f}s is under the {MIN_BUDGET_SECONDS:.0f}s floor a Semgrep scan needs"),
)
return next((reason for failed, reason in checks if failed), "")
```
SudoLang (`vvah/vvaharness/plugins/semgrep/enricher.sudo`):
```
require !context.cancellation.is_cancelled => return "cancelled before the Semgrep scan started"
require context.project.source_path => return "the project carries no source path to scan"
require configs || rulesets => return "no local rule files and no rulesets were configured"
require budget >= MIN_BUDGET_SECONDS => return "${budget}s is under the 15s floor a Semgrep scan needs"
```
