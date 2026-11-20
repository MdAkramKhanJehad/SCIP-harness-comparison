# vvaharness/models/scan/_sections_chain.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/models/scan/_sections_chain.py.evidence.json`. SHA-256: `342b850664349662970b9d75b36ff3ebaa4497cd63f5d1085a4a951875ed5a36`.

```sudo
// Source: vvaharness/models/scan/_sections_chain.py:14-24
In source order: Retain source documentation literal source_literal_14_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import logging; preserve alias and import-time effects. Then Resolve source import from typing import TYPE_CHECKING; preserve alias and import-time effects. Then Resolve source import from vvaharness.models.scan._render import _demote_md_headings, _escape_angles, _md_cell; preserve alias and import-time effects.
// Source: vvaharness/models/scan/_sections_chain.py:25-26
In source order: Resolve source import from vvaharness.models.scan.findings import Chain; preserve alias and import-time effects. Then Resolve source import from vvaharness.models.scan.threat import ThreatModel; preserve alias and import-time effects.
// Source: vvaharness/models/scan/_sections_chain.py:28-29
if (the source predicate TYPE_CHECKING is truthy) {
  // Source: vvaharness/models/scan/_sections_chain.py:29-29
  In source order: Resolve source import from vvaharness.models.scan.report import FinalReport; preserve alias and import-time effects.
}
// Source: vvaharness/models/scan/_sections_chain.py:31-33
In source order: Evaluate once logging.getLogger(__name__); assign in source target order to log. Then Evaluate once 20; assign in source target order to _UNPROMOTED_SHOWN.
// Source: vvaharness/models/scan/_sections_chain.py:36-94
// Source signature: _chain_lines(report, n: int, c: Chain) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _chain_lines(report, n, c) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/models/scan/_sections_chain.py:37-58
  In source order: Retain source documentation literal source_literal_37_4; it is not a model call. Then Evaluate once ' → '.join((source_template_39_8 for idx in c.steps)); assign in source target order to steps_str. Then Evaluate once source_template_43_8 if c.blocked_by_controls else ''; assign in source target order to blocked. Then Evaluate once source_template_49_8 if c.preconditions else ''; assign in source target order to requires. Then Evaluate once source_template_55_8 if c.entry_reachability else ''; assign in source target order to reached.
  // Source: vvaharness/models/scan/_sections_chain.py:59-63
  In source order: Evaluate once [source_template_61_8, source_template_62_8]; assign in source target order to out.
  // Source: vvaharness/models/scan/_sections_chain.py:64-72
  if (the source predicate c.link_evidence is truthy) {
    // Source: vvaharness/models/scan/_sections_chain.py:66-66
    In source order: Evaluate out.extend(['', '**Step links:**']); retain side effects and discard the expression result.
    // Source: vvaharness/models/scan/_sections_chain.py:67-72
    for each ln in c.link_evidence {
      // Source: vvaharness/models/scan/_sections_chain.py:68-72
      In source order: Evaluate once ' — ' + _escape_angles(_md_cell(ln.mechanism)) if ln.mechanism else ''; assign in source target order to mech. Then Evaluate once source_template_70_19 if ln.file and ln.line else ''; assign in source target order to loc. Then Evaluate out.append(source_template_72_23); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/models/scan/_sections_chain.py:74-80
  In source order: Evaluate once {'lift_withheld': 'severity not raised to the strongest constituent finding', 'self_raise_capped': 'severity capped at the strongest constituent finding'}; assign in source target order to _decision_note. Then For meta, assign []; source annotation list[str].
  // Source: vvaharness/models/scan/_sections_chain.py:81-82
  if (the source predicate c.link_coverage is truthy) {
    // Source: vvaharness/models/scan/_sections_chain.py:82-82
    In source order: Evaluate meta.append(source_template_82_20); retain side effects and discard the expression result.
  }
  // Source: vvaharness/models/scan/_sections_chain.py:83-84
  if (the source predicate (note := _decision_note.get(c.severity_decision)) is truthy) {
    // Source: vvaharness/models/scan/_sections_chain.py:84-84
    In source order: Evaluate meta.append(note); retain side effects and discard the expression result.
  }
  // Source: vvaharness/models/scan/_sections_chain.py:85-86
  In source order: Evaluate meta.extend((_md_cell(a) for a in c.quality_notes)); retain side effects and discard the expression result. Then Evaluate meta.extend((_md_cell(a) for a in c.disclosures)); retain side effects and discard the expression result.
  // Source: vvaharness/models/scan/_sections_chain.py:87-88
  if (the source predicate meta is truthy) {
    // Source: vvaharness/models/scan/_sections_chain.py:88-88
    In source order: Evaluate out.extend(['', source_template_88_24]); retain side effects and discard the expression result.
  }
  // Source: vvaharness/models/scan/_sections_chain.py:89-93
  In source order: Evaluate out.extend(['', _demote_md_headings(c.narrative, escape_angles=True), '']); retain side effects and discard the expression result.
  // Source: vvaharness/models/scan/_sections_chain.py:94-94
  End this invocation with out.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/models/scan/_sections_chain.py:96-101
// Source signature: _unpromoted_pairs_text(report: FinalReport) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _unpromoted_pairs_text(report) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/models/scan/_sections_chain.py:97-100
  In source order: Retain source documentation literal source_literal_97_4; it is not a model call. Then Evaluate once report.unpromoted_links; assign in source target order to pairs. Then Evaluate once ', '.join((source_template_99_22 for o, t in pairs[:_UNPROMOTED_SHOWN])); assign in source target order to shown. Then Evaluate once len(pairs) - _UNPROMOTED_SHOWN; assign in source target order to more.
  // Source: vvaharness/models/scan/_sections_chain.py:101-101
  End this invocation with source_template_101_11 if more > 0 else shown.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/models/scan/_sections_chain.py:103-110
// Source signature: _unpromoted_link_leadin(report: FinalReport) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _unpromoted_link_leadin(report) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/models/scan/_sections_chain.py:104-105
  In source order: Retain source documentation literal source_literal_104_4; it is not a model call. Then Evaluate once len(report.unpromoted_links); assign in source target order to n.
  // Source: vvaharness/models/scan/_sections_chain.py:106-107
  if (the source predicate not n is truthy) {
    // Source: vvaharness/models/scan/_sections_chain.py:107-107
    End this invocation with [].
  }
  // Source: vvaharness/models/scan/_sections_chain.py:108-110
  End this invocation with [source_template_108_13, ''].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/models/scan/_sections_chain.py:112-124
// Source signature: _chain_removal_leadins(report: FinalReport) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _chain_removal_leadins(report) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/models/scan/_sections_chain.py:113-113
  In source order: Retain source documentation literal source_literal_113_4; it is not a model call.
  // Source: vvaharness/models/scan/_sections_chain.py:114-124
  End this invocation with [line for note, n in ((source_template_115_9, report.chains_dropped), (source_template_118_9, report.chains_deduped), (source_template_121_10, report.chains_invalid)) if n for line in (note, '')].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/models/scan/_sections_chain.py:126-135
// Source signature: _terminal_diversity_leadin(report: FinalReport) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _terminal_diversity_leadin(report) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/models/scan/_sections_chain.py:127-131
  In source order: Retain source documentation literal source_literal_127_4; it is not a model call. Then Evaluate once len(report.chains); assign in source target order to n. Then Evaluate once len({(f.file, f.line_start) for f in (report.findings[c.steps[-1]].finding for c in report.chains if c.steps)}); assign in source target order to m.
  // Source: vvaharness/models/scan/_sections_chain.py:132-133
  if (the source predicate n <= m is truthy) {
    // Source: vvaharness/models/scan/_sections_chain.py:133-133
    End this invocation with [].
  }
  // Source: vvaharness/models/scan/_sections_chain.py:134-135
  End this invocation with [source_template_134_13, ''].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/models/scan/_sections_chain.py:137-145
// Source signature: _summary_reconciliation_note(report: FinalReport) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _summary_reconciliation_note(report) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/models/scan/_sections_chain.py:138-139
  In source order: Retain source documentation literal source_literal_138_4; it is not a model call. Then Evaluate once report.chains_dropped + report.chains_invalid; assign in source target order to n.
  // Source: vvaharness/models/scan/_sections_chain.py:140-141
  if (the source predicate not n is truthy) {
    // Source: vvaharness/models/scan/_sections_chain.py:141-141
    End this invocation with [].
  }
  // Source: vvaharness/models/scan/_sections_chain.py:142-145
  End this invocation with [source_template_142_13, ''].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/models/scan/_sections_chain.py:147-164
// Source signature: _empty_chain_section_copy(report: FinalReport) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _empty_chain_section_copy(report) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/models/scan/_sections_chain.py:148-160
  In source order: Retain source documentation literal source_literal_148_4; it is not a model call. Then Evaluate once [note for note, n in ((source_template_150_9, report.chains_dropped), (source_template_153_9, report.chains_deduped), (source_template_155_10, report.chains_invalid), (source_template_157_10, len(report.unpromoted_links))) if n]; assign in source target order to clauses.
  // Source: vvaharness/models/scan/_sections_chain.py:161-162
  if (the source predicate clauses is truthy) {
    // Source: vvaharness/models/scan/_sections_chain.py:162-162
    End this invocation with [source_template_162_16, ''].
  }
  // Source: vvaharness/models/scan/_sections_chain.py:163-164
  End this invocation with ['No exploit chains were identified — no chain entry combining findings reached this report.', ''].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/models/scan/_sections_chain.py:166-173
// Source signature: _chain_pass_caveat(report: FinalReport) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _chain_pass_caveat(report) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/models/scan/_sections_chain.py:167-167
  In source order: Retain source documentation literal source_literal_167_4; it is not a model call.
  // Source: vvaharness/models/scan/_sections_chain.py:169-170
  if (the source predicate not report.findings is truthy) {
    // Source: vvaharness/models/scan/_sections_chain.py:170-170
    End this invocation with [].
  }
  // Source: vvaharness/models/scan/_sections_chain.py:171-173
  End this invocation with [source_literal_171_13, ''].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/models/scan/_sections_chain.py:175-197
// Source signature: _render_unreachable_appendix(report) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _render_unreachable_appendix(report) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/models/scan/_sections_chain.py:176-189
  In source order: Retain source documentation literal source_literal_176_4; it is not a model call. Then Evaluate once 200; assign in source target order to cap. Then Evaluate once report.unreachable_files; assign in source target order to files. Then Evaluate once ['', source_template_181_8, '', source_template_184_9, '']; assign in source target order to out.
  // Source: vvaharness/models/scan/_sections_chain.py:190-192
  for each f in files[:cap] {
    // Source: vvaharness/models/scan/_sections_chain.py:192-192
    In source order: Evaluate out.append(source_template_192_19); retain side effects and discard the expression result.
  }
  // Source: vvaharness/models/scan/_sections_chain.py:193-195
  if (the source predicate len(files) > cap is truthy) {
    // Source: vvaharness/models/scan/_sections_chain.py:194-195
    In source order: Evaluate out.append(source_template_194_19); retain side effects and discard the expression result.
  }
  // Source: vvaharness/models/scan/_sections_chain.py:196-196
  In source order: Evaluate out.append(''); retain side effects and discard the expression result.
  // Source: vvaharness/models/scan/_sections_chain.py:197-197
  End this invocation with out.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/models/scan/_sections_chain.py:199-217
// Source signature: _app_profile_lines(report) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _app_profile_lines(report) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/models/scan/_sections_chain.py:200-201
  In source order: Retain source documentation literal source_literal_200_4; it is not a model call. Then Evaluate once report.app_profile; assign in source target order to ap.
  // Source: vvaharness/models/scan/_sections_chain.py:202-203
  if (the source predicate not ap is truthy) {
    // Source: vvaharness/models/scan/_sections_chain.py:203-203
    End this invocation with [].
  }
  // Source: vvaharness/models/scan/_sections_chain.py:204-207
  In source order: Evaluate once ', '.join((s for s, ok in (('PCI-scoped', ap.pci_scoped), ('processes PAN', ap.processes_pan), ('PII', ap.pii)) if ok)) or 'standard'; assign in source target order to sens.
  // Source: vvaharness/models/scan/_sections_chain.py:208-217
  End this invocation with ['### Application profile (CMDB)', source_template_211_9, source_template_213_8, source_template_214_8, source_template_215_8, ''].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/models/scan/_sections_chain.py:219-240
// Source signature: _ranked_threat_rows(tm: ThreatModel, without_unit: list[str] | None) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _ranked_threat_rows(tm, without_unit) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/models/scan/_sections_chain.py:220-222
  In source order: Retain source documentation literal source_literal_220_4; it is not a model call. Then Evaluate once '| ID | Threat | Actor | Surface | Asset | Impact | Likelihood | Controls |'; assign in source target order to header. Then Evaluate once '|---|---|---|---|---|---|---|---|'; assign in source target order to rule.
  // Source: vvaharness/models/scan/_sections_chain.py:223-225
  if (the source predicate without_unit is not None is truthy) {
    // Source: vvaharness/models/scan/_sections_chain.py:224-225
    In source order: Apply source augmented assignment header += ' Investigation unit |' with source evaluation/in-place semantics. Then Apply source augmented assignment rule += '---|' with source evaluation/in-place semantics.
  }
  // Source: vvaharness/models/scan/_sections_chain.py:226-227
  In source order: Evaluate once set(without_unit or ()); assign in source target order to missing. Then Evaluate once ['### Ranked threats', '', header, rule]; assign in source target order to out.
  // Source: vvaharness/models/scan/_sections_chain.py:228-238
  for each (tid, t) in zip(tm.threat_ids(), tm.threats, strict=True) {
    // Source: vvaharness/models/scan/_sections_chain.py:229-233
    In source order: Evaluate once source_template_229_15; assign in source target order to row.
    // Source: vvaharness/models/scan/_sections_chain.py:234-237
    if (the source predicate without_unit is not None is truthy) {
      // Source: vvaharness/models/scan/_sections_chain.py:237-237
      In source order: Apply source augmented assignment row += ' **none — never reviewed** |' if tid in missing else ' minted |' with source evaluation/in-place semantics.
    }
    // Source: vvaharness/models/scan/_sections_chain.py:238-238
    In source order: Evaluate out.append(row); retain side effects and discard the expression result.
  }
  // Source: vvaharness/models/scan/_sections_chain.py:239-239
  In source order: Evaluate out.append(''); retain side effects and discard the expression result.
  // Source: vvaharness/models/scan/_sections_chain.py:240-240
  End this invocation with out.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/models/scan/_sections_chain.py:243-278
// Source signature: _render_threat_model(report) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _render_threat_model(report) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/models/scan/_sections_chain.py:244-246
  In source order: Evaluate once report.threat_model; assign in source target order to tm. Then Evaluate once ['## Threat Model', '']; assign in source target order to out. Then Evaluate out.extend(_app_profile_lines(report)); retain side effects and discard the expression result.
  // Source: vvaharness/models/scan/_sections_chain.py:247-250
  if (the source predicate tm.system_context is truthy) {
    // Source: vvaharness/models/scan/_sections_chain.py:248-250
    In source order: Evaluate out.extend(['### System context', '', _demote_md_headings(tm.system_context, escape_angles=True), '']); retain side effects and discard the expression result.
  }
  // Source: vvaharness/models/scan/_sections_chain.py:251-258
  if (the source predicate tm.assets is truthy) {
    // Source: vvaharness/models/scan/_sections_chain.py:252-254
    In source order: Evaluate out.extend(['### Assets', '', '| Asset | Sensitivity | Description |', '|---|---|---|']); retain side effects and discard the expression result.
    // Source: vvaharness/models/scan/_sections_chain.py:255-257
    for each a in tm.assets {
      // Source: vvaharness/models/scan/_sections_chain.py:256-257
      In source order: Evaluate out.append(source_template_256_23); retain side effects and discard the expression result.
    }
    // Source: vvaharness/models/scan/_sections_chain.py:258-258
    In source order: Evaluate out.append(''); retain side effects and discard the expression result.
  }
  // Source: vvaharness/models/scan/_sections_chain.py:259-265
  if (the source predicate tm.trust_boundaries is truthy) {
    // Source: vvaharness/models/scan/_sections_chain.py:260-260
    In source order: Evaluate out.extend(['### Trust boundaries', '']); retain side effects and discard the expression result.
    // Source: vvaharness/models/scan/_sections_chain.py:261-264
    for each b in tm.trust_boundaries {
      // Source: vvaharness/models/scan/_sections_chain.py:262-264
      In source order: Evaluate once ', '.join((_md_cell(x) for x in b.reachable_assets)) or '-'; assign in source target order to ra. Then Evaluate out.append(source_template_263_23); retain side effects and discard the expression result.
    }
    // Source: vvaharness/models/scan/_sections_chain.py:265-265
    In source order: Evaluate out.append(''); retain side effects and discard the expression result.
  }
  // Source: vvaharness/models/scan/_sections_chain.py:266-267
  if (the source predicate tm.threats is truthy) {
    // Source: vvaharness/models/scan/_sections_chain.py:267-267
    In source order: Evaluate out.extend(_ranked_threat_rows(tm, report.threats_without_unit)); retain side effects and discard the expression result.
  }
  // Source: vvaharness/models/scan/_sections_chain.py:268-277
  if (the source predicate tm.open_questions is truthy) {
    // Source: vvaharness/models/scan/_sections_chain.py:270-277
    In source order: Evaluate out.extend(['### Open questions', '', source_literal_271_20, '']); retain side effects and discard the expression result. Then Evaluate out.extend((source_template_276_19 for q in tm.open_questions)); retain side effects and discard the expression result. Then Evaluate out.append(''); retain side effects and discard the expression result.
  }
  // Source: vvaharness/models/scan/_sections_chain.py:278-278
  End this invocation with out.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.models.scan._render import _demote_md_headings, _escape_angles, _md_cell` at source line 20: `source_detail/vvaharness/models/scan/_render.py.sudo.md`.
- `from vvaharness.models.scan.findings import Chain` at source line 25: `source_detail/vvaharness/models/scan/findings.py.sudo.md`.
- `from vvaharness.models.scan.threat import ThreatModel` at source line 26: `source_detail/vvaharness/models/scan/threat.py.sudo.md`.
- `from vvaharness.models.scan.report import FinalReport` at source line 29: `source_detail/vvaharness/models/scan/report.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../prompt_representation/vvaharness/models/scan/_sections_chain.py.sudo.md). Exact strings in the evidence asset support this conversion.
