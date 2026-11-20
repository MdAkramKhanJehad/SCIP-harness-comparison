# vvaharness/pipeline/stages/s9/typed_sarif.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/pipeline/stages/s9/typed_sarif.py.evidence.json`. SHA-256: `1986facb0ca4a41f799440741952f381ea740fe5900e095eb7c446ee6bfd80ba`.

```sudo
// Source: vvaharness/pipeline/stages/s9/typed_sarif.py:16-22
In source order: Retain source documentation literal source_literal_16_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import json; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from vvaharness import __version__ as _PKG_VERSION; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s9/typed_sarif.py:23-27
In source order: Resolve source import from vvaharness.models import FinalReport; preserve alias and import-time effects. Then Resolve source import from vvaharness.models.scan._render import _md_cell; preserve alias and import-time effects. Then Resolve source import from vvaharness.models.scan.findings import Finding, RankedFinding; preserve alias and import-time effects. Then Resolve source import from vvaharness.models.scan.report import finding_description_lines; preserve alias and import-time effects. Then Resolve source import from vvaharness.models.vocab import OFFENSIVE_LABELS, SEV_RANK; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s9/typed_sarif.py:28-32
In source order: Resolve source import from vvaharness.pipeline.stages.s9.health import scan_health as _scan_health; preserve alias and import-time effects. Then Resolve source import from vvaharness.report.appcontext import AppInfo; preserve alias and import-time effects. Then Resolve source import from vvaharness.report.cvss import rating as _cvss_rating; preserve alias and import-time effects. Then Resolve source import from vvaharness.report.cvss import score_or_sentinel as _cvss_score; preserve alias and import-time effects. Then Resolve source import from vvaharness.report.cwe import cwe_for, cwe_label, cwe_name; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s9/typed_sarif.py:33-37
In source order: Resolve source import from vvaharness.report.redact import redact_counts, redact_tree; preserve alias and import-time effects. Then Resolve source import from vvaharness.rules.cwe import norm_cwe; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import console; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.config import knob; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.counters import COUNTERS; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s9/typed_sarif.py:40-43
In source order: Evaluate once 'vvaFindingId/v1'; assign in source target order to FINGERPRINT_KEY. Then Evaluate once 'aliasFindingIds'; assign in source target order to ALIAS_KEY.
// Source: vvaharness/pipeline/stages/s9/typed_sarif.py:46-54
// Source signature: result_identifies(result, case_id: str) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn result_identifies(result, case_id) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:47-47
  In source order: Retain source documentation literal source_literal_47_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:48-49
  if (the source predicate not case_id is truthy) {
    // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:49-49
    End this invocation with False.
  }
  // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:50-50
  In source order: Evaluate once result.get('partialFingerprints') or {}; assign in source target order to prints.
  // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:51-52
  if (the source predicate str(prints.get(FINGERPRINT_KEY, '')) == case_id is truthy) {
    // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:52-52
    End this invocation with True.
  }
  // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:53-53
  In source order: Evaluate once (result.get('properties') or {}).get(ALIAS_KEY) or []; assign in source target order to aliases.
  // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:54-54
  End this invocation with case_id in aliases.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s9/typed_sarif.py:57-59
// Source signature: result_fingerprint(result) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn result_fingerprint(result) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:58-58
  In source order: Retain source documentation literal source_literal_58_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:59-59
  End this invocation with str((result.get('partialFingerprints') or {}).get(FINGERPRINT_KEY, '')).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s9/typed_sarif.py:62-77
// Source signature: record_result_block(result, case_id: str, block, *, key: str, alias_key: str) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn record_result_block(result, case_id, block, key, alias_key) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:64-67
  In source order: Retain source documentation literal source_literal_64_4; it is not a model call. Then Evaluate once result.setdefault('properties', {}); assign in source target order to props. Then Evaluate once result_fingerprint(result); assign in source target order to own.
  // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:69-71
  if (the source predicate not (own and case_id and (own != case_id)) is truthy) {
    // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:70-70
    In source order: Evaluate once block; assign in source target order to props[key].
    // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:71-71
    End this invocation with True.
  }
  // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:72-72
  In source order: Evaluate once props.get(alias_key); assign in source target order to aliases.
  // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:73-75
  if (the source predicate not isinstance(aliases, dict) is truthy) {
    // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:74-75
    In source order: Evaluate once {}; assign in source target order to aliases. Then Evaluate once aliases; assign in source target order to props[alias_key].
  }
  // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:76-76
  In source order: Evaluate once block; assign in source target order to aliases[case_id].
  // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:77-77
  End this invocation with False.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s9/typed_sarif.py:81-89
In source order: Evaluate once 'ec480a2c-8267-5d90-affc-401687cd64b0'; assign in source target order to CWE_TAXONOMY_GUID. Then Evaluate once 'Additional call site — collapsed during dedup; same root cause as the primary location and needs the same fix.'; assign in source target order to _DEDUP_RELATED_MSG. Then Evaluate once {'source': 'Source — where untrusted input enters.', 'sink': 'Sink — where the tainted value is used unsafely.'}; assign in source target order to _REF_RELATED_MSG.
// Source: vvaharness/pipeline/stages/s9/typed_sarif.py:92-94
// Source signature: _sarif_level(sev: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _sarif_level(sev) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:93-94
  End this invocation with {'CRITICAL': 'error', 'HIGH': 'error', 'MEDIUM': 'warning'}.get(sev, 'note').
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s9/typed_sarif.py:97-101
// Source signature: _security_severity(sev: str, cvss_score: float) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _security_severity(sev, cvss_score) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:98-99
  if (the source predicate cvss_score >= 0 is truthy) {
    // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:99-99
    End this invocation with source_template_99_15.
  }
  // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:100-101
  End this invocation with {'CRITICAL': '9.0', 'HIGH': '7.0', 'MEDIUM': '4.0', 'LOW': '0.1'}.get(sev, '0.0').
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s9/typed_sarif.py:104-110
// Source signature: _class_label(f: Finding) -> tuple[str | None, str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _class_label(f) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:105-109
  In source order: Retain source documentation literal source_literal_105_4; it is not a model call. Then Evaluate once norm_cwe(f.cwe) or cwe_for(None, f.vuln_class); assign in source target order to eff. Then Evaluate once cwe_name(eff) if eff else ''; assign in source target order to nm. Then Evaluate once ((source_template_109_14 if nm else eff) if eff else '') or f.vuln_class.value; assign in source target order to label.
  // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:110-110
  End this invocation with (eff, label).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s9/typed_sarif.py:113-117
// Source signature: _result_message(f: Finding, score: float) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _result_message(f, score) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:114-115
  In source order: Retain source documentation literal source_literal_114_4; it is not a model call. Then Evaluate once source_template_115_16 if score >= 0 else ''; assign in source target order to score_txt.
  // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:116-117
  End this invocation with _md_cell(f.title) + (source_template_116_32 if f.cvss_vector else '').
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s9/typed_sarif.py:120-125
// Source signature: _dup_result_key(f: Finding, eff: str | None, msg: str) -> tuple[str, int, str, str, str, str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _dup_result_key(f, eff, msg) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:122-122
  In source order: Retain source documentation literal source_literal_122_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:124-125
  End this invocation with (f.file or 'unknown', f.line_start, eff or f.vuln_class.value, msg, f.channel or 'main', f.origin or '').
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s9/typed_sarif.py:128-131
// Source signature: _survivor_rank(rf: RankedFinding) -> tuple[int]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _survivor_rank(rf) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:129-129
  In source order: Retain source documentation literal source_literal_129_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:131-131
  End this invocation with (SEV_RANK.get(rf.severity, 9),).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s9/typed_sarif.py:134-139
// Source signature: _section_description(i: int, rf: RankedFinding) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _section_description(i, rf) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:135-138
  In source order: Retain source documentation literal source_literal_135_4; it is not a model call. Then Evaluate once redact_counts(source_literal_138_8.join(finding_description_lines(i, rf)).strip()); assign in source target order to (desc, _).
  // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:139-139
  End this invocation with desc[:4000] + '…' if len(desc) > 4000 else desc.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s9/typed_sarif.py:142-157
// Source signature: _ref_related_location(role: str, ref: str) -> dict
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _ref_related_location(role, ref) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:143-145
  In source order: Retain source documentation literal source_literal_143_4; it is not a model call. Then Evaluate once ref.rpartition(':'); assign in source target order to (uri, _, line). Then For region, assign {}; source annotation dict.
  // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:146-149
  if (the source predicate uri and line.isdigit() is truthy) {
    // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:147-147
    In source order: Evaluate once {'startLine': int(line)}; assign in source target order to region.
  }
  else {
    // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:149-149
    In source order: Evaluate once ref; assign in source target order to uri.
  }
  // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:150-150
  In source order: For physical, assign {'artifactLocation': {'uri': uri}}; source annotation dict.
  // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:151-152
  if (the source predicate region is truthy) {
    // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:152-152
    In source order: Evaluate once region; assign in source target order to physical['region'].
  }
  // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:153-157
  End this invocation with {'physicalLocation': physical, 'message': {'text': _REF_RELATED_MSG[role]}, 'properties': {'role': role}}.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s9/typed_sarif.py:160-167
// Source signature: _taint_code_flow(source_ref: str, sink_ref: str) -> dict | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _taint_code_flow(source_ref, sink_ref) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:161-163
  In source order: Retain source documentation literal source_literal_161_4; it is not a model call. Then Evaluate once [_ref_related_location(role, ref) for role, ref in (('source', source_ref), ('sink', sink_ref)) if ref]; assign in source target order to steps.
  // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:164-165
  if (the source predicate not steps is truthy) {
    // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:165-165
    End this invocation with None.
  }
  // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:166-167
  End this invocation with {'threadFlows': [{'locations': [{'location': s, 'importance': 'essential'} for s in steps]}]}.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s9/typed_sarif.py:170-442
// Source signature: build_sarif(report: FinalReport, application_id: str | None, app_info: AppInfo | None, *, cfg=None) -> dict
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn build_sarif(report, application_id, app_info, cfg) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:172-177
  In source order: Retain source documentation literal source_literal_172_4; it is not a model call. Then Evaluate once knob(cfg, 'step9.duplicate_result_guard', True); assign in source target order to dup_guard. Then Evaluate once knob(cfg, 'output.posture_channel', True); assign in source target order to posture_channel. Then Evaluate once []; assign in source target order to results. Then For rule_ids, assign []; source annotation list[str].
  // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:178-183
  In source order: For rep_name, assign {}; source annotation dict[str, str]. Then For eff_cwes, assign []; source annotation list[str]. Then For rule_cwe, assign {}; source annotation dict[str, str]. Then For rule_sev, assign {}; source annotation dict[str, str]. Then Evaluate once [_class_label(rf0.finding) for rf0 in report.findings]; assign in source target order to labels.
  // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:184-190
  In source order: Evaluate once [_cvss_score(rf0.finding.cvss_vector) for rf0 in report.findings]; assign in source target order to scores. Then Evaluate once [_result_message(rf0.finding, scores[k]) for k, rf0 in enumerate(report.findings)]; assign in source target order to msgs. Then For dup_keys, assign []; source annotation list[tuple]. Then For winner_of, assign {}; source annotation dict[tuple, int]. Then For alias_ids, assign {}; source annotation dict[int, list[str]].
  // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:192-192
  In source order: For seen_dup_sites, assign set(); source annotation set[tuple[str, int, str]].
  // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:193-207
  if (the source predicate dup_guard is truthy) {
    // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:194-196
    In source order: Evaluate once [_dup_result_key(rf0.finding, labels[k][0], msgs[k]) for k, rf0 in enumerate(report.findings)]; assign in source target order to dup_keys. Then Evaluate once [_survivor_rank(rf0) for rf0 in report.findings]; assign in source target order to ranks.
    // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:197-200
    for each i0 in range(len(report.findings)) {
      // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:198-198
      In source order: Evaluate once winner_of.get(dup_keys[i0]); assign in source target order to held.
      // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:199-200
      if (the source predicate held is None or ranks[i0] < ranks[held] is truthy) {
        // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:200-200
        In source order: Evaluate once i0; assign in source target order to winner_of[dup_keys[i0]].
      }
    }
    // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:201-207
    for each (i0, rf0) in enumerate(report.findings) {
      // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:202-202
      In source order: Evaluate once winner_of[dup_keys[i0]]; assign in source target order to won_by.
      // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:203-204
      if (the source predicate won_by != i0 and rf0.finding.case_id is truthy) {
        // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:204-204
        In source order: Evaluate alias_ids.setdefault(won_by, []).append(rf0.finding.case_id); retain side effects and discard the expression result.
      }
      // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:205-207
      In source order: Evaluate once rf0.finding; assign in source target order to f0. Then Evaluate seen_dup_sites.add((f0.file or 'unknown', f0.line_start, labels[i0][0] or f0.vuln_class.value)); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:208-328
  for each (i, rf) in enumerate(report.findings, 1) {
    // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:209-210
    In source order: Evaluate once rf.finding; assign in source target order to f. Then Evaluate once rf.severity.value.upper(); assign in source target order to sev.
    // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:211-214
    if (the source predicate dup_guard and winner_of[dup_keys[i - 1]] != i - 1 is truthy) {
      // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:213-213
      In source order: Evaluate COUNTERS.bump('s9_sarif_dup_result_suppressed'); retain side effects and discard the expression result.
      // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:214-214
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:215-218
    In source order: Evaluate once labels[i - 1]; assign in source target order to (eff_cwe, category). Then Evaluate once scores[i - 1]; assign in source target order to cvss_score. Then Evaluate once msgs[i - 1]; assign in source target order to msg. Then Evaluate once category or sev.lower(); assign in source target order to rule_id.
    // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:219-220
    if (the source predicate rule_id and rule_id not in rule_ids is truthy) {
      // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:220-220
      In source order: Evaluate rule_ids.append(rule_id); retain side effects and discard the expression result.
    }
    // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:221-224
    if (the source predicate rule_id and rule_id not in rep_name and eff_cwe is truthy) {
      // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:222-222
      In source order: Evaluate once cwe_name(eff_cwe); assign in source target order to nm.
      // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:223-224
      if (the source predicate nm is truthy) {
        // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:224-224
        In source order: Evaluate once nm; assign in source target order to rep_name[rule_id].
      }
    }
    // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:225-226
    if (the source predicate eff_cwe is truthy) {
      // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:226-226
      In source order: Evaluate eff_cwes.append(eff_cwe); retain side effects and discard the expression result.
    }
    // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:227-238
    In source order: For props, assign {'severity': sev.lower(), 'security-severity': _security_severity(sev, cvss_score), 'cvssRating': _cvss_rating(cvss_score if cvss_score >= 0 else float(_security_severity(sev, cvss_score))), 'category': category, 'cvssVector': f.cvss_vector}; source annotation dict. Then Evaluate rule_cwe.setdefault(rule_id, eff_cwe); retain side effects and discard the expression result. Then Evaluate once max(rule_sev.get(rule_id, '0.0'), props['security-severity'], key=float); assign in source target order to rule_sev[rule_id].
    // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:239-244
    if (the source predicate eff_cwe is truthy) {
      // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:240-242
      In source order: Evaluate once cwe_label(eff_cwe); assign in source target order to props['cwe']. Then Evaluate once eff_cwe; assign in source target order to props['cweId']. Then Evaluate once cwe_name(eff_cwe); assign in source target order to nm.
      // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:243-244
      if (the source predicate nm is truthy) {
        // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:244-244
        In source order: Evaluate once nm; assign in source target order to props['cweName'].
      }
    }
    // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:245-246
    if (the source predicate cvss_score >= 0 is truthy) {
      // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:246-246
      In source order: Evaluate once round(cvss_score, 1); assign in source target order to props['cvssScore'].
    }
    // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:247-250
    if (the source predicate f.vsvs_score is not None is truthy) {
      // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:248-250
      In source order: Evaluate once f.vsvs_vector; assign in source target order to props['vulContextSeverityVector']. Then Evaluate once round(f.vsvs_score, 1); assign in source target order to props['vulContextSeverityScore']. Then Evaluate once f.vsvs_rating; assign in source target order to props['vulContextSeverityRating'].
    }
    // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:251-256
    if (the source predicate f.offensive_priority is truthy) {
      // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:252-256
      In source order: Evaluate once OFFENSIVE_LABELS.get(f.offensive_priority, ''); assign in source target order to _label. Then Evaluate once f.offensive_priority; assign in source target order to props['offensivePriority']. Then Evaluate once _label; assign in source target order to props['offensivePriorityLabel']. Then Evaluate once source_template_256_47.strip(); assign in source target order to props['offensivePriorityReason'].
    }
    // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:258-272
    In source order: Evaluate once _section_description(i, rf); assign in source target order to props['description']. Then For result, assign {'ruleId': rule_id, 'level': _sarif_level(sev), 'message': {'text': msg}, 'locations': [{'physicalLocation': {'artifactLocation': {'uri': f.file or 'unknown'}, 'region': {'startLine': f.line_start}}}], 'properties': props}; source annotation dict.
    // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:273-277
    if (the source predicate eff_cwe is truthy) {
      // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:274-277
      In source order: Evaluate once [{'toolComponent': {'name': 'CWE', 'guid': CWE_TAXONOMY_GUID}, 'id': eff_cwe}]; assign in source target order to result['taxa'].
    }
    // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:278-278
    In source order: Evaluate once []; assign in source target order to related.
    // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:279-305
    for each d in f.duplicates {
      // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:280-286
      if (the source predicate dup_guard is truthy) {
        // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:282-282
        In source order: Evaluate once (d.file, d.line_start, eff_cwe or f.vuln_class.value); assign in source target order to gkey.
        // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:283-285
        if (the source predicate gkey in seen_dup_sites is truthy) {
          // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:284-284
          In source order: Evaluate COUNTERS.bump('s9_sarif_dup_site_deduped'); retain side effects and discard the expression result.
          // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:285-285
          Continue the immediately enclosing source loop at its next iteration.
        }
        // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:286-286
        In source order: Evaluate seen_dup_sites.add(gkey); retain side effects and discard the expression result.
      }
      // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:287-287
      In source order: For region, assign {'startLine': d.line_start}; source annotation dict.
      // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:288-289
      if (the source predicate d.line_end and d.line_end != d.line_start is truthy) {
        // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:289-289
        In source order: Evaluate once d.line_end; assign in source target order to region['endLine'].
      }
      // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:290-302
      In source order: For entry, assign {'physicalLocation': {'artifactLocation': {'uri': d.file}, 'region': region}, 'message': {'text': _DEDUP_RELATED_MSG}}; source annotation dict. Then Evaluate once {k: v for k, v in (('title', d.title), ('vulnClass', d.vuln_class.value), ('sourceRef', d.source_ref), ('sinkRef', d.sink_ref)) if v}; assign in source target order to meta.
      // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:303-304
      if (the source predicate meta is truthy) {
        // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:304-304
        In source order: Evaluate once meta; assign in source target order to entry['properties'].
      }
      // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:305-305
      In source order: Evaluate related.append(entry); retain side effects and discard the expression result.
    }
    // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:306-308
    if (the source predicate related is truthy) {
      // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:308-308
      In source order: Evaluate once len(related); assign in source target order to props['dedupRelatedLocationCount'].
    }
    // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:309-310
    if (the source predicate (flow := _taint_code_flow(f.source_ref, f.sink_ref)) is not None is truthy) {
      // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:310-310
      In source order: Evaluate once [flow]; assign in source target order to result['codeFlows'].
    }
    // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:311-312
    if (the source predicate related is truthy) {
      // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:312-312
      In source order: Evaluate once related; assign in source target order to result['relatedLocations'].
    }
    // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:313-314
    if (the source predicate f.backfilled_refs is truthy) {
      // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:314-314
      In source order: Evaluate once list(f.backfilled_refs); assign in source target order to props['backfilledRefs'].
    }
    // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:316-317
    if (the source predicate posture_channel is truthy) {
      // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:317-317
      In source order: Evaluate once f.channel or 'main'; assign in source target order to props['channel'].
    }
    // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:318-320
    if (the source predicate f.origin is truthy) {
      // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:320-320
      In source order: Evaluate once f.origin; assign in source target order to props['origin'].
    }
    // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:321-322
    if (the source predicate (aliases := alias_ids.get(i - 1)) is truthy) {
      // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:322-322
      In source order: Evaluate once aliases; assign in source target order to props[ALIAS_KEY].
    }
    // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:323-325
    if (the source predicate cvss_score >= 0 is truthy) {
      // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:325-325
      In source order: Evaluate once round(cvss_score * 10.0, 1); assign in source target order to result['rank'].
    }
    // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:326-327
    if (the source predicate f.case_id is truthy) {
      // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:327-327
      In source order: Evaluate once {FINGERPRINT_KEY: f.case_id}; assign in source target order to result['partialFingerprints'].
    }
    // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:328-328
    In source order: Evaluate results.append(result); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:330-330
  In source order: Evaluate once []; assign in source target order to rules.
  // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:331-339
  for each rid in rule_ids {
    // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:332-332
    In source order: For rule, assign {'id': rid, 'name': rid}; source annotation dict.
    // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:333-334
    if (the source predicate rid in rep_name is truthy) {
      // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:334-334
      In source order: Evaluate once {'text': rep_name[rid]}; assign in source target order to rule['shortDescription'].
    }
    // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:335-335
    In source order: Evaluate once ['security']; assign in source target order to tags.
    // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:336-337
    if (the source predicate rule_cwe.get(rid) is truthy) {
      // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:337-337
      In source order: Evaluate tags.append(source_template_337_24); retain side effects and discard the expression result.
    }
    // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:338-339
    In source order: Evaluate once {'tags': tags, 'security-severity': rule_sev[rid]}; assign in source target order to rule['properties']. Then Evaluate rules.append(rule); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:341-341
  In source order: Evaluate once []; assign in source target order to taxa.
  // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:342-352
  for each cid in sorted(set(eff_cwes), key=lambda c: int(c.split('-')[-1])) {
    // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:343-348
    In source order: Evaluate once cwe_name(cid); assign in source target order to nm. Then Evaluate once cid.split('-')[-1]; assign in source target order to n. Then For taxon, assign {'id': cid, 'helpUri': source_template_347_23}; source annotation dict.
    // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:349-351
    if (the source predicate nm is truthy) {
      // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:350-351
      In source order: Evaluate once nm; assign in source target order to taxon['name']. Then Evaluate once {'text': nm}; assign in source target order to taxon['shortDescription'].
    }
    // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:352-352
    In source order: Evaluate taxa.append(taxon); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:353-365
  In source order: Evaluate once {'guid': CWE_TAXONOMY_GUID, 'name': 'CWE', 'organization': 'MITRE', 'shortDescription': {'text': 'The MITRE Common Weakness Enumeration'}, 'informationUri': 'https://cwe.mitre.org/', 'taxa': taxa}; assign in source target order to taxonomy. Then Evaluate once report.app_profile; assign in source target order to prof. Then For run_props, assign {'applicationId': (prof.application_id if prof else '') or application_id or ''}; source annotation dict.
  // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:366-371
  if (the source predicate prof is truthy) {
    // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:367-368
    In source order: Evaluate once prof.source; assign in source target order to run_props['cmdbSource']. Then Evaluate once prof.name; assign in source target order to run_props['applicationName'].
  }
  else {
    // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:369-371
    if (the source predicate app_info is truthy) {
      // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:370-371
      In source order: Evaluate once app_info.source; assign in source target order to run_props['cmdbSource']. Then Evaluate once app_info.name; assign in source target order to run_props['applicationName'].
    }
  }
  // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:373-386
  In source order: For run, assign {'tool': {'driver': {'name': 'Agentic SAST', 'version': _PKG_VERSION, 'rules': rules, 'supportedTaxonomies': [{'guid': CWE_TAXONOMY_GUID}]}}, 'taxonomies': [taxonomy], 'properties': run_props, 'results': results}; source annotation dict. Then Evaluate once _scan_health(report); assign in source target order to health. Then Evaluate once []; assign in source target order to notifications.
  // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:387-392
  for each (stg, n) in sorted((health.get('errors_by_stage') or {}).items()) {
    // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:389-392
    In source order: Evaluate notifications.append({'level': 'warning', 'message': {'text': source_template_391_32}}); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:393-393
  In source order: Evaluate once int(health.get('chunks_failed', 0) or 0); assign in source target order to cf.
  // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:394-399
  if (the source predicate cf is truthy) {
    // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:395-399
    In source order: Evaluate notifications.append({'level': 'warning', 'message': {'text': source_template_397_32}}); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:400-406
  if (the source predicate health.get('degraded') is truthy) {
    // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:402-406
    In source order: Evaluate notifications.append({'level': 'warning', 'message': {'text': health.get('degraded_reason') or 'report degraded (no reason recorded)'}}); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:407-407
  In source order: Evaluate once int(health.get('threats_truncated', 0) or 0); assign in source target order to truncated.
  // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:408-414
  if (the source predicate truncated is truthy) {
    // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:409-414
    In source order: Evaluate notifications.append({'level': 'warning', 'message': {'text': source_template_411_32}}); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:415-417
  In source order: For invocation, assign {'executionSuccessful': bool(health.get('executionSuccessful', True))}; source annotation dict.
  // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:418-419
  if (the source predicate notifications is truthy) {
    // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:419-419
    In source order: Evaluate once notifications; assign in source target order to invocation['toolExecutionNotifications'].
  }
  // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:420-426
  In source order: Evaluate once [invocation]; assign in source target order to run['invocations']. Then Evaluate once bool(health.get('enrichment_unavailable')); assign in source target order to run_props['enrichmentUnavailable']. Then Evaluate once bool(health.get('deepdive_skipped')); assign in source target order to run_props['deepdiveSkipped']. Then Evaluate once bool(health.get('hollow')); assign in source target order to run_props['hollow']. Then Evaluate once bool(health.get('coverage_degraded')); assign in source target order to run_props['coverageDegraded'].
  // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:427-435
  In source order: Evaluate once list(health.get('coverage_degraded_reasons') or []); assign in source target order to run_props['coverageDegradedReasons']. Then Evaluate once health['threats_total']; assign in source target order to run_props['threatsTotal']. Then Evaluate once health['threats_without_unit']; assign in source target order to run_props['threatsWithoutUnit']. Then Evaluate once int(health.get('threats_before_cap', 0) or 0); assign in source target order to run_props['threatsBeforeCap']. Then Evaluate once int(health.get('threats_truncated', 0) or 0); assign in source target order to run_props['threatsTruncated'].
  // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:436-436
  In source order: Evaluate once int(health.get('threats_promoted', 0) or 0); assign in source target order to run_props['threatsPromoted'].
  // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:438-442
  End this invocation with {'$schema': 'https://json.schemastore.org/sarif-2.1.0.json', 'version': '2.1.0', 'runs': [run]}.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s9/typed_sarif.py:445-456
// Source signature: write_sarif(report: FinalReport, sarif_path: Path, application_id: str | None, app_info: AppInfo | None, *, cfg=None) -> Path
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn write_sarif(report, sarif_path, application_id, app_info, cfg) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:448-449
  In source order: Retain source documentation literal source_literal_448_4; it is not a model call. Then Evaluate once build_sarif(report, application_id, app_info, cfg=cfg); assign in source target order to doc.
  // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:450-452
  Enter source context managers left-to-right: open(sarif_path, 'w', encoding='utf-8') bound to fh {
    // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:451-452
    In source order: Evaluate fh.write(json.dumps(redact_tree(doc), indent=2)); retain side effects and discard the expression result. Then Evaluate fh.write(source_literal_452_17); retain side effects and discard the expression result.
  }
  Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
  // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:454-455
  In source order: Evaluate once len(doc['runs'][0]['results']); assign in source target order to n_results. Then Evaluate console.write(source_template_455_18); retain side effects and discard the expression result.
  // Source: vvaharness/pipeline/stages/s9/typed_sarif.py:456-456
  End this invocation with sarif_path.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness import __version__ as _PKG_VERSION` at source line 22: `source_detail/vvaharness/__init__.py.sudo.md`.
- `from vvaharness.models import FinalReport` at source line 23: `source_detail/vvaharness/models/__init__.py.sudo.md`.
- `from vvaharness.models.scan._render import _md_cell` at source line 24: `source_detail/vvaharness/models/scan/_render.py.sudo.md`.
- `from vvaharness.models.scan.findings import Finding, RankedFinding` at source line 25: `source_detail/vvaharness/models/scan/findings.py.sudo.md`.
- `from vvaharness.models.scan.report import finding_description_lines` at source line 26: `source_detail/vvaharness/models/scan/report.py.sudo.md`.
- `from vvaharness.models.vocab import OFFENSIVE_LABELS, SEV_RANK` at source line 27: `source_detail/vvaharness/models/vocab.py.sudo.md`.
- `from vvaharness.pipeline.stages.s9.health import scan_health as _scan_health` at source line 28: `source_detail/vvaharness/pipeline/stages/s9/health.py.sudo.md`.
- `from vvaharness.report.appcontext import AppInfo` at source line 29: `source_detail/vvaharness/report/appcontext.py.sudo.md`.
- `from vvaharness.report.cvss import rating as _cvss_rating` at source line 30: `source_detail/vvaharness/report/cvss.py.sudo.md`.
- `from vvaharness.report.cvss import score_or_sentinel as _cvss_score` at source line 31: `source_detail/vvaharness/report/cvss.py.sudo.md`.
- `from vvaharness.report.cwe import cwe_for, cwe_label, cwe_name` at source line 32: `source_detail/vvaharness/report/cwe.py.sudo.md`.
- `from vvaharness.report.redact import redact_counts, redact_tree` at source line 33: `source_detail/vvaharness/report/redact.py.sudo.md`.
- `from vvaharness.rules.cwe import norm_cwe` at source line 34: `source_detail/vvaharness/rules/cwe.py.sudo.md`.
- `from vvaharness.util import console` at source line 35: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import console` at source line 35: `source_detail/vvaharness/util/console.py.sudo.md`.
- `from vvaharness.util.config import knob` at source line 36: `source_detail/vvaharness/util/config.py.sudo.md`.
- `from vvaharness.util.counters import COUNTERS` at source line 37: `source_detail/vvaharness/util/counters.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../../prompt_representation/vvaharness/pipeline/stages/s9/typed_sarif.py.sudo.md). Exact strings in the evidence asset support this conversion.
