# vvaharness/models/scan/report.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/models/scan/report.py.evidence.json`. SHA-256: `d1b1ca4cc8d2d669bab13d2d7a2c08b408e7627ab63725f5b32d95da13d6fe68`.

```sudo
// Source: vvaharness/models/scan/report.py:14-20
In source order: Retain source documentation literal source_literal_14_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import logging; preserve alias and import-time effects. Then Resolve source import import re; preserve alias and import-time effects. Then Resolve source import from pydantic import BaseModel; preserve alias and import-time effects.
// Source: vvaharness/models/scan/report.py:22-48
In source order: Resolve source import from vvaharness.models.scan._finding_section import finding_description_lines, finding_section_lines; preserve alias and import-time effects. Then Resolve source import from vvaharness.models.scan._render import _demote_md_headings, _md_cell; preserve alias and import-time effects. Then Resolve source import from vvaharness.models.scan._sections_chain import _app_profile_lines, _chain_lines, _chain_pass_caveat, _chain_removal_leadins, _empty_chain_section_copy, _render_threat_model, _render_unreachable_appendix, _summary_reconciliation_note, _terminal_diversity_leadin, _unpromoted_link_leadin; preserve alias and import-time effects. Then Resolve source import from vvaharness.models.scan._sections_metrics import _render_metrics, _render_scan_health, _render_scope_appendix, _render_verification; preserve alias and import-time effects. Then Resolve source import from vvaharness.models.scan.findings import NOT_RANKED_NOTE, Chain, DroppedFinding, RankedFinding; preserve alias and import-time effects.
// Source: vvaharness/models/scan/report.py:49-55
In source order: Resolve source import from vvaharness.models.scan.inputs import AppProfile; preserve alias and import-time effects. Then Resolve source import from vvaharness.models.scan.metrics import ScanMetrics; preserve alias and import-time effects. Then Resolve source import from vvaharness.models.scan.threat import ThreatModel; preserve alias and import-time effects. Then Evaluate once ['FinalReport', 'finding_description_lines', 'finding_section_lines']; assign in source target order to __all__. Then Evaluate once logging.getLogger(__name__); assign in source target order to log.
// Source: vvaharness/models/scan/report.py:58-282
interface FinalReport {
  Describe the source Python type, preserving its base/metaclass expression order: BaseModel.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/models/scan/report.py:60-64
  In source order: For schema_version, assign '1.0'; source annotation str. Then For repo_root, declare without assigning a value; source annotation str. Then For repo_name, assign None; source annotation str | None. Then For git_sha, assign None; source annotation str | None. Then For findings, declare without assigning a value; source annotation list[RankedFinding].
  // Source: vvaharness/models/scan/report.py:65-74
  In source order: For chains, declare without assigning a value; source annotation list[Chain]. Then For chains_dropped, assign 0; source annotation int. Then For chains_deduped, assign 0; source annotation int. Then For chains_invalid, assign 0; source annotation int. Then For unpromoted_links, assign []; source annotation list[tuple[int, int]].
  // Source: vvaharness/models/scan/report.py:75-79
  In source order: For dropped, assign []; source annotation list[DroppedFinding]. Then For raw_findings_count, assign 0; source annotation int. Then For metrics, assign None; source annotation ScanMetrics | None. Then For threat_model, assign None; source annotation ThreatModel | None. Then For app_profile, assign None; source annotation AppProfile | None.
  // Source: vvaharness/models/scan/report.py:81-86
  In source order: For unreachable_files, assign None; source annotation list[str] | None. Then For threats_without_unit, assign None; source annotation list[str] | None. Then For summary, declare without assigning a value; source annotation str. Then For degraded, assign False; source annotation bool. Then For degraded_reason, assign ''; source annotation str.
  // Source: vvaharness/models/scan/report.py:88-88
  In source order: For enrichment_unavailable, assign False; source annotation bool.
  // Source: vvaharness/models/scan/report.py:92-102
  // Source signature: is_hollow(self) -> bool
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn is_hollow(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/models/scan/report.py:93-94
    In source order: Retain source documentation literal source_literal_93_8; it is not a model call. Then Evaluate once self.metrics; assign in source target order to m.
    // Source: vvaharness/models/scan/report.py:95-96
    if (the source predicate m is None or self.findings is truthy) {
      // Source: vvaharness/models/scan/report.py:96-96
      End this invocation with False.
    }
    // Source: vvaharness/models/scan/report.py:98-99
    In source order: Evaluate once max(self.raw_findings_count or 0, getattr(m, 'raw_findings_count', 0) or 0); assign in source target order to raw.
    // Source: vvaharness/models/scan/report.py:100-102
    End this invocation with bool(not raw and (getattr(m, 'total_files_in_scope', 0) or 0) > 0 and getattr(m, 's2_degraded', False)).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/models/scan/report.py:104-107
  // Source signature: _undetermined_drop_count(self) -> int
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _undetermined_drop_count(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/models/scan/report.py:105-105
    In source order: Retain source documentation literal source_literal_105_8; it is not a model call.
    // Source: vvaharness/models/scan/report.py:106-107
    End this invocation with sum((1 for d in self.dropped if d.reason in ('VERIFY_ERROR', 'GUARDRAIL_BLOCKED', 'INCONCLUSIVE'))).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/models/scan/report.py:109-132
  // Source signature: unranked_split(self) -> tuple[int, int, int]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn unranked_split(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/models/scan/report.py:110-130
    In source order: Retain source documentation literal source_literal_110_8; it is not a model call. Then Evaluate once {s for c in self.chains for s in c.steps[:-1]}; assign in source target order to feeders. Then Evaluate once [i for i, rf in enumerate(self.findings) if rf.exploitability_notes == NOT_RANKED_NOTE]; assign in source target order to unranked. Then Evaluate once sum((1 for i in unranked if i in feeders)); assign in source target order to feeder_missed. Then Evaluate once len(unranked) - feeder_missed; assign in source target order to by_design.
    // Source: vvaharness/models/scan/report.py:131-131
    In source order: Evaluate once len(self.findings) - len(unranked); assign in source target order to ranked.
    // Source: vvaharness/models/scan/report.py:132-132
    End this invocation with (ranked, by_design, feeder_missed).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/models/scan/report.py:134-142
  // Source signature: _verified_tp_fp(self) -> tuple[int, int]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _verified_tp_fp(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/models/scan/report.py:135-137
    In source order: Retain source documentation literal source_literal_135_8; it is not a model call. Then Evaluate once self.metrics; assign in source target order to m.
    // Source: vvaharness/models/scan/report.py:138-139
    if (the source predicate m is not None is truthy) {
      // Source: vvaharness/models/scan/report.py:139-139
      End this invocation with (m.true_positive_count, m.false_positive_count).
    }
    // Source: vvaharness/models/scan/report.py:141-142
    End this invocation with (len(self.findings), sum((1 for d in self.dropped if d.reason == 'FALSE_POSITIVE'))).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/models/scan/report.py:144-157
  // Source signature: coverage_degraded(self) -> tuple[str, ...]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn coverage_degraded(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/models/scan/report.py:145-147
    In source order: Retain source documentation literal source_literal_145_8; it is not a model call. Then Evaluate once self.metrics; assign in source target order to m.
    // Source: vvaharness/models/scan/report.py:148-149
    if (the source predicate m is None is truthy) {
      // Source: vvaharness/models/scan/report.py:149-149
      End this invocation with ().
    }
    // Source: vvaharness/models/scan/report.py:150-150
    In source order: For reasons, assign []; source annotation list[str].
    // Source: vvaharness/models/scan/report.py:151-152
    if (the source predicate self._undetermined_drop_count() > 0 is truthy) {
      // Source: vvaharness/models/scan/report.py:152-152
      In source order: Evaluate reasons.append('s6_undetermined'); retain side effects and discard the expression result.
    }
    // Source: vvaharness/models/scan/report.py:153-154
    if (the source predicate m.total_files_in_scope > 0 and m.analyzed_files_unique == 0 is truthy) {
      // Source: vvaharness/models/scan/report.py:154-154
      In source order: Evaluate reasons.append('zero_analysis'); retain side effects and discard the expression result.
    }
    // Source: vvaharness/models/scan/report.py:155-156
    if (the source predicate m.llm_turn_cap_exhausted > 0 is truthy) {
      // Source: vvaharness/models/scan/report.py:156-156
      In source order: Evaluate reasons.append('llm_turn_cap_exhausted'); retain side effects and discard the expression result.
    }
    // Source: vvaharness/models/scan/report.py:157-157
    End this invocation with tuple(reasons).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/models/scan/report.py:159-282
  // Source signature: to_markdown(self, *, posture_channel: bool=True, unreachable_appendix: bool=True) -> str
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn to_markdown(self, posture_channel, unreachable_appendix) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/models/scan/report.py:162-170
    In source order: Evaluate once re.sub('[<>`|\\[\\]]', '', str(self.repo_name or self.repo_root or '')); assign in source target order to safe_title. Then Evaluate once [source_template_164_12, '', '## Summary', _demote_md_headings(self.summary, escape_angles=True), '', *_summary_reconciliation_note(self)]; assign in source target order to out.
    // Source: vvaharness/models/scan/report.py:171-179
    if (the source predicate self.app_profile is None is truthy) {
      // Source: vvaharness/models/scan/report.py:173-179
      In source order: Evaluate out.extend([source_literal_174_17, '']); retain side effects and discard the expression result.
    }
    // Source: vvaharness/models/scan/report.py:180-182
    if (the source predicate self.metrics is truthy) {
      // Source: vvaharness/models/scan/report.py:181-182
      In source order: Evaluate out.extend(_render_metrics(self, unreachable_appendix=unreachable_appendix)); retain side effects and discard the expression result.
    }
    // Source: vvaharness/models/scan/report.py:183-183
    In source order: Evaluate out.extend(_render_scan_health(self)); retain side effects and discard the expression result.
    // Source: vvaharness/models/scan/report.py:184-187
    if (the source predicate self.threat_model is truthy) {
      // Source: vvaharness/models/scan/report.py:185-185
      In source order: Evaluate out.extend(_render_threat_model(self)); retain side effects and discard the expression result.
    }
    else {
      // Source: vvaharness/models/scan/report.py:186-187
      if (the source predicate self.app_profile is truthy) {
        // Source: vvaharness/models/scan/report.py:187-187
        In source order: Evaluate out.extend(['## Threat Model', ''] + _app_profile_lines(self)); retain side effects and discard the expression result.
      }
    }
    // Source: vvaharness/models/scan/report.py:188-191
    In source order: Evaluate out.extend(_render_verification(self, posture_channel=posture_channel)); retain side effects and discard the expression result. Then For _main, assign []; source annotation list[tuple[int, RankedFinding]]. Then For _posture, assign []; source annotation list[tuple[int, RankedFinding]].
    // Source: vvaharness/models/scan/report.py:192-196
    for each (i, rf) in enumerate(self.findings, 1) {
      // Source: vvaharness/models/scan/report.py:193-196
      if (the source predicate posture_channel and rf.finding.channel == 'posture' is truthy) {
        // Source: vvaharness/models/scan/report.py:194-194
        In source order: Evaluate _posture.append((i, rf)); retain side effects and discard the expression result.
      }
      else {
        // Source: vvaharness/models/scan/report.py:196-196
        In source order: Evaluate _main.append((i, rf)); retain side effects and discard the expression result.
      }
    }
    // Source: vvaharness/models/scan/report.py:197-201
    In source order: Evaluate out.extend(['', source_template_199_12, '']); retain side effects and discard the expression result.
    // Source: vvaharness/models/scan/report.py:203-209
    if (the source predicate _posture is truthy) {
      // Source: vvaharness/models/scan/report.py:204-209
      In source order: Evaluate out.extend([source_template_205_17, '']); retain side effects and discard the expression result.
    }
    // Source: vvaharness/models/scan/report.py:210-211
    for each (i, rf) in _main {
      // Source: vvaharness/models/scan/report.py:211-211
      In source order: Evaluate out.extend(finding_section_lines(i, rf)); retain side effects and discard the expression result.
    }
    // Source: vvaharness/models/scan/report.py:212-225
    if (the source predicate _posture is truthy) {
      // Source: vvaharness/models/scan/report.py:213-223
      In source order: Evaluate out.extend(['', source_template_215_16, '', source_literal_217_17, '']); retain side effects and discard the expression result.
      // Source: vvaharness/models/scan/report.py:224-225
      for each (i, rf) in _posture {
        // Source: vvaharness/models/scan/report.py:225-225
        In source order: Evaluate out.extend(finding_section_lines(i, rf)); retain side effects and discard the expression result.
      }
    }
    // Source: vvaharness/models/scan/report.py:226-254
    if (the source predicate self.chains is truthy) {
      // Source: vvaharness/models/scan/report.py:227-232
      In source order: Evaluate out.extend(['## Exploit Chains', '']); retain side effects and discard the expression result. Then Evaluate out.extend(_chain_removal_leadins(self) + _terminal_diversity_leadin(self)); retain side effects and discard the expression result. Then Evaluate out.extend(_unpromoted_link_leadin(self)); retain side effects and discard the expression result. Then Evaluate out.extend(_chain_pass_caveat(self)); retain side effects and discard the expression result. Then Evaluate once list(enumerate(self.chains, 1)); assign in source target order to _numbered.
      // Source: vvaharness/models/scan/report.py:233-236
      In source order: Evaluate once [(n, c) for n, c in _numbered if len(c.quality_notes) >= 2]; assign in source target order to _lower. Then Evaluate once [(n, c) for n, c in _numbered if len(c.quality_notes) < 2]; assign in source target order to _confirmed.
      // Source: vvaharness/models/scan/report.py:237-238
      for each (n, c) in _confirmed {
        // Source: vvaharness/models/scan/report.py:238-238
        In source order: Evaluate out.extend(_chain_lines(self, n, c)); retain side effects and discard the expression result.
      }
      // Source: vvaharness/models/scan/report.py:239-250
      if (the source predicate _lower is truthy) {
        // Source: vvaharness/models/scan/report.py:240-248
        In source order: Evaluate out.extend(['### Lower-confidence chains', '', source_literal_243_21, '']); retain side effects and discard the expression result.
        // Source: vvaharness/models/scan/report.py:249-250
        for each (n, c) in _lower {
          // Source: vvaharness/models/scan/report.py:250-250
          In source order: Evaluate out.extend(_chain_lines(self, n, c)); retain side effects and discard the expression result.
        }
      }
    }
    else {
      // Source: vvaharness/models/scan/report.py:251-254
      if (the source predicate not self.enrichment_unavailable is truthy) {
        // Source: vvaharness/models/scan/report.py:252-254
        In source order: Evaluate out.extend(['## Exploit Chains', '']); retain side effects and discard the expression result. Then Evaluate out.extend(_empty_chain_section_copy(self)); retain side effects and discard the expression result. Then Evaluate out.extend(_chain_pass_caveat(self)); retain side effects and discard the expression result.
      }
    }
    // Source: vvaharness/models/scan/report.py:255-255
    In source order: Evaluate out.extend(['', '## Dropped Findings', '']); retain side effects and discard the expression result.
    // Source: vvaharness/models/scan/report.py:256-276
    if (the source predicate self.dropped is truthy) {
      // Source: vvaharness/models/scan/report.py:257-264
      In source order: Evaluate once {'FALSE_POSITIVE': 'FP', 'UNCONFIRMED': 'UNCONFIRMED', 'VERIFY_ERROR': 'VERIFY-ERR', 'EXCLUDED': 'EXCLUDED', 'GUARDRAIL_BLOCKED': 'GUARDRAIL', 'INCONCLUSIVE': 'INCONCLUSIVE'}; assign in source target order to _tag.
      // Source: vvaharness/models/scan/report.py:265-274
      for each d in self.dropped {
        // Source: vvaharness/models/scan/report.py:266-271
        if (the source predicate d.reason == 'DUPLICATE' is truthy) {
          // Source: vvaharness/models/scan/report.py:267-269
          In source order: Evaluate once source_template_267_27 if d.canonical_idx is not None else 'DUP (pre-verify)'; assign in source target order to tag.
        }
        else {
          // Source: vvaharness/models/scan/report.py:271-271
          In source order: Evaluate once _tag.get(d.reason, d.reason); assign in source target order to tag.
        }
        // Source: vvaharness/models/scan/report.py:272-274
        In source order: Evaluate out.append(source_template_272_27); retain side effects and discard the expression result.
      }
    }
    else {
      // Source: vvaharness/models/scan/report.py:276-276
      In source order: Evaluate out.append('_None._'); retain side effects and discard the expression result.
    }
    // Source: vvaharness/models/scan/report.py:277-277
    In source order: Evaluate out.append(''); retain side effects and discard the expression result.
    // Source: vvaharness/models/scan/report.py:278-279
    if (the source predicate self.metrics is truthy) {
      // Source: vvaharness/models/scan/report.py:279-279
      In source order: Evaluate out.extend(_render_scope_appendix(self)); retain side effects and discard the expression result.
    }
    // Source: vvaharness/models/scan/report.py:280-281
    if (the source predicate self.unreachable_files and unreachable_appendix is truthy) {
      // Source: vvaharness/models/scan/report.py:281-281
      In source order: Evaluate out.extend(_render_unreachable_appendix(self)); retain side effects and discard the expression result.
    }
    // Source: vvaharness/models/scan/report.py:282-282
    End this invocation with source_literal_282_15.join(out).
    If execution reaches this end, finish with the source implicit None result.
  }
}
```

## Local import links

- `from vvaharness.models.scan._finding_section import finding_description_lines, finding_section_lines` at source line 22: `source_detail/vvaharness/models/scan/_finding_section.py.sudo.md`.
- `from vvaharness.models.scan._render import _demote_md_headings, _md_cell` at source line 26: `source_detail/vvaharness/models/scan/_render.py.sudo.md`.
- `from vvaharness.models.scan._sections_chain import _app_profile_lines, _chain_lines, _chain_pass_caveat, _chain_removal_leadins, _empty_chain_section_copy, _render_threat_model, _render_unreachable_appendix, _summary_reconciliation_note, _terminal_diversity_leadin, _unpromoted_link_leadin` at source line 30: `source_detail/vvaharness/models/scan/_sections_chain.py.sudo.md`.
- `from vvaharness.models.scan._sections_metrics import _render_metrics, _render_scan_health, _render_scope_appendix, _render_verification` at source line 42: `source_detail/vvaharness/models/scan/_sections_metrics.py.sudo.md`.
- `from vvaharness.models.scan.findings import NOT_RANKED_NOTE, Chain, DroppedFinding, RankedFinding` at source line 48: `source_detail/vvaharness/models/scan/findings.py.sudo.md`.
- `from vvaharness.models.scan.inputs import AppProfile` at source line 49: `source_detail/vvaharness/models/scan/inputs.py.sudo.md`.
- `from vvaharness.models.scan.metrics import ScanMetrics` at source line 50: `source_detail/vvaharness/models/scan/metrics.py.sudo.md`.
- `from vvaharness.models.scan.threat import ThreatModel` at source line 51: `source_detail/vvaharness/models/scan/threat.py.sudo.md`.
