# vvaharness/orchestrator/enrich_findings.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/orchestrator/enrich_findings.py.evidence.json`. SHA-256: `d298dccdb37ed344dda7dbbae9afb64fe05b05a3faa3128714b9cc7163f9efb1`.

```sudo
// Source: vvaharness/orchestrator/enrich_findings.py:16-21
In source order: Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Retain source documentation literal source_literal_18_0; it is not a model call. Then Resolve source import from vvaharness.report import appcontext; preserve alias and import-time effects. Then Resolve source import from vvaharness.report.cvss import rating as _cvss_rating; preserve alias and import-time effects. Then Resolve source import from vvaharness.report.cvss import score_or_sentinel as _cvss_score; preserve alias and import-time effects.
// Source: vvaharness/orchestrator/enrich_findings.py:22-22
In source order: Resolve source import from vvaharness.rules.cwe import norm_cwe; preserve alias and import-time effects.
// Source: vvaharness/orchestrator/enrich_findings.py:25-28
// Source signature: _prefix_path(path: str | None, prefix: str) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _prefix_path(path, prefix) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/enrich_findings.py:26-27
  if (the source predicate not path or path.startswith(source_template_26_35) is truthy) {
    // Source: vvaharness/orchestrator/enrich_findings.py:27-27
    End this invocation with path.
  }
  // Source: vvaharness/orchestrator/enrich_findings.py:28-28
  End this invocation with source_template_28_11.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/enrich_findings.py:31-36
// Source signature: _prefix_ref(ref: str | None, prefix: str) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _prefix_ref(ref, prefix) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/enrich_findings.py:33-34
  if (the source predicate not ref is truthy) {
    // Source: vvaharness/orchestrator/enrich_findings.py:34-34
    End this invocation with ref.
  }
  // Source: vvaharness/orchestrator/enrich_findings.py:35-35
  In source order: Evaluate once ref.partition(':'); assign in source target order to (file_part, sep, line_part).
  // Source: vvaharness/orchestrator/enrich_findings.py:36-36
  End this invocation with source_template_36_11.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/enrich_findings.py:39-67
// Source signature: _enrich_findings(findings: list, app_info, path_prefix: str | None=None) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _enrich_findings(findings, app_info, path_prefix) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/enrich_findings.py:41-41
  In source order: Retain source documentation literal source_literal_41_4; it is not a model call.
  // Source: vvaharness/orchestrator/enrich_findings.py:42-67
  for each f in findings {
    // Source: vvaharness/orchestrator/enrich_findings.py:43-52
    if (the source predicate path_prefix is truthy) {
      // Source: vvaharness/orchestrator/enrich_findings.py:44-48
      In source order: Evaluate once _prefix_path(f.file, path_prefix); assign in source target order to f.file. Then Evaluate once _prefix_ref(getattr(f, 'source_ref', None), path_prefix); assign in source target order to f.source_ref. Then Evaluate once _prefix_ref(getattr(f, 'sink_ref', None), path_prefix); assign in source target order to f.sink_ref.
      // Source: vvaharness/orchestrator/enrich_findings.py:49-52
      for each d in f.duplicates {
        // Source: vvaharness/orchestrator/enrich_findings.py:50-52
        In source order: Evaluate once _prefix_path(d.file, path_prefix) or d.file; assign in source target order to d.file. Then Evaluate once _prefix_ref(d.source_ref, path_prefix); assign in source target order to d.source_ref. Then Evaluate once _prefix_ref(d.sink_ref, path_prefix); assign in source target order to d.sink_ref.
      }
    }
    // Source: vvaharness/orchestrator/enrich_findings.py:54-54
    In source order: Evaluate once norm_cwe(f.cwe); assign in source target order to f.cwe.
    // Source: vvaharness/orchestrator/enrich_findings.py:55-59
    if (the source predicate f.cvss_vector is truthy) {
      // Source: vvaharness/orchestrator/enrich_findings.py:56-56
      In source order: Evaluate once _cvss_score(f.cvss_vector); assign in source target order to _score.
      // Source: vvaharness/orchestrator/enrich_findings.py:57-59
      if (the source predicate _score >= 0 is truthy) {
        // Source: vvaharness/orchestrator/enrich_findings.py:58-59
        In source order: Evaluate once _score; assign in source target order to f.cvss_score. Then Evaluate once _cvss_rating(_score); assign in source target order to f.cvss_rating.
      }
    }
    // Source: vvaharness/orchestrator/enrich_findings.py:60-65
    if (the source predicate f.cvss_vector and app_info is not None is truthy) {
      // Source: vvaharness/orchestrator/enrich_findings.py:61-61
      In source order: Evaluate once appcontext.vsvs_score(f.cvss_vector, app_info); assign in source target order to vr.
      // Source: vvaharness/orchestrator/enrich_findings.py:62-65
      if (the source predicate vr is truthy) {
        // Source: vvaharness/orchestrator/enrich_findings.py:63-65
        In source order: Evaluate once vr.vector; assign in source target order to f.vsvs_vector. Then Evaluate once vr.score; assign in source target order to f.vsvs_score. Then Evaluate once vr.rating; assign in source target order to f.vsvs_rating.
      }
    }
    // Source: vvaharness/orchestrator/enrich_findings.py:66-67
    In source order: Evaluate once appcontext.offensive_priority_for(f.title, f.vuln_class.value, f.description, f.cvss_vector, app_info); assign in source target order to (f.offensive_priority, f.offensive_reason).
  }
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.report import appcontext` at source line 19: `source_detail/vvaharness/report/__init__.py.sudo.md`.
- `from vvaharness.report import appcontext` at source line 19: `source_detail/vvaharness/report/appcontext.py.sudo.md`.
- `from vvaharness.report.cvss import rating as _cvss_rating` at source line 20: `source_detail/vvaharness/report/cvss.py.sudo.md`.
- `from vvaharness.report.cvss import score_or_sentinel as _cvss_score` at source line 21: `source_detail/vvaharness/report/cvss.py.sudo.md`.
- `from vvaharness.rules.cwe import norm_cwe` at source line 22: `source_detail/vvaharness/rules/cwe.py.sudo.md`.
