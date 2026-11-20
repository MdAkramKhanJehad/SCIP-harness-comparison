# vvaharness/models/scan/_finding_section.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/models/scan/_finding_section.py.evidence.json`. SHA-256: `0d8a1d6d5a9262577350d7aa0d047c331cfd8a318192e3bb80ba7654d11a1764`.

```sudo
// Source: vvaharness/models/scan/_finding_section.py:14-29
In source order: Retain source documentation literal source_literal_14_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import logging; preserve alias and import-time effects. Then Resolve source import from vvaharness.models.scan._render import _code_span, _confidence_label, _demote_md_headings, _md_cell, _one_line, _render_repro_block, _snippet_fence, _vector_span; preserve alias and import-time effects. Then Resolve source import from vvaharness.models.scan.findings import RankedFinding; preserve alias and import-time effects.
// Source: vvaharness/models/scan/_finding_section.py:30-49
In source order: Resolve source import from vvaharness.models.vocab import OFFENSIVE_LABELS; preserve alias and import-time effects. Then Evaluate once logging.getLogger(__name__); assign in source target order to log. Then Evaluate once logging.getLogger(__name__); assign in source target order to log. Then Evaluate once {'CONFIRMED': 'CONFIRMED (beta)', 'NOT_CONFIRMED': 'NOT CONFIRMED (beta)', 'INCONCLUSIVE': 'REQUIRES REVIEW (beta)', 'NOT_TESTED': 'SAST-ONLY (beta; not live-testable)'}; assign in source target order to _EV_VERDICT_LABEL. Then Evaluate once {'rule': '[rule] ', 'triage': '[triage] ', 'judge': '[judge] '}; assign in source target order to _EV_REASON_TAG.
// Source: vvaharness/models/scan/_finding_section.py:51-57
In source order: Evaluate once source_literal_51_21; assign in source target order to _EV_NOT_A_FP_NOTE. Then Evaluate once source_literal_55_26; assign in source target order to _EV_POSITIVE_ONLY_NOTE.
// Source: vvaharness/models/scan/_finding_section.py:60-62
// Source signature: finding_section_lines(i: int, rf: RankedFinding) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn finding_section_lines(i, rf) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/models/scan/_finding_section.py:61-61
  In source order: Retain source documentation literal source_literal_61_4; it is not a model call.
  // Source: vvaharness/models/scan/_finding_section.py:62-62
  End this invocation with [line for line, _ in _finding_section(i, rf)].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/models/scan/_finding_section.py:65-67
// Source signature: finding_description_lines(i: int, rf: RankedFinding) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn finding_description_lines(i, rf) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/models/scan/_finding_section.py:66-66
  In source order: Retain source documentation literal source_literal_66_4; it is not a model call.
  // Source: vvaharness/models/scan/_finding_section.py:67-67
  End this invocation with [line for line, keep in _finding_section(i, rf) if keep].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/models/scan/_finding_section.py:70-235
// Source signature: _finding_section(i: int, rf: RankedFinding) -> list[tuple[str, bool]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _finding_section(i, rf) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/models/scan/_finding_section.py:71-72
  In source order: Retain source documentation literal source_literal_71_4; it is not a model call. Then Evaluate once rf.finding; assign in source target order to f.
  // Source: vvaharness/models/scan/_finding_section.py:73-82
  if (the source predicate f.cvss_score is not None is truthy) {
    // Source: vvaharness/models/scan/_finding_section.py:75-78
    In source order: Evaluate once '(scored against the claim, verdict FALSE_POSITIVE)' if f.verdict == 'FALSE_POSITIVE' else source_template_77_23; assign in source target order to _score. Then Evaluate once source_template_78_15; assign in source target order to cvss.
  }
  else {
    // Source: vvaharness/models/scan/_finding_section.py:79-82
    if (the source predicate f.cvss_vector is truthy) {
      // Source: vvaharness/models/scan/_finding_section.py:80-80
      In source order: Evaluate once _vector_span(f.cvss_vector); assign in source target order to cvss.
    }
    else {
      // Source: vvaharness/models/scan/_finding_section.py:82-82
      In source order: Evaluate once '_not computed_'; assign in source target order to cvss.
    }
  }
  // Source: vvaharness/models/scan/_finding_section.py:83-90
  In source order: Resolve source import from vvaharness.report.cwe import cwe_for, cwe_name; preserve alias and import-time effects. Then Evaluate once cwe_for(f.cwe, f.vuln_class); assign in source target order to _cwe. Then Evaluate once cwe_name(_cwe) if _cwe else ''; assign in source target order to _nm. Then Evaluate once (source_template_86_18 if _nm else _cwe) if _cwe else ''; assign in source target order to _cwe_label. Then Evaluate once [(source_template_88_9, False), (source_template_89_9, False)]; assign in source target order to out.
  // Source: vvaharness/models/scan/_finding_section.py:91-95
  if (the source predicate _cwe is truthy) {
    // Source: vvaharness/models/scan/_finding_section.py:92-95
    In source order: Evaluate once _cwe.split('-')[-1]; assign in source target order to _n. Then Evaluate out.append((source_template_94_13, False)); retain side effects and discard the expression result.
  }
  // Source: vvaharness/models/scan/_finding_section.py:97-105
  In source order: Evaluate once _md_cell(f.file).replace(chr(96), chr(715)); assign in source target order to _file_span. Then Evaluate once source_template_99_14 if f.line_end else source_template_100_19; assign in source target order to _lines. Then Evaluate out.extend([(source_template_102_9, False), (source_template_104_9, cvss == '_not computed_')]); retain side effects and discard the expression result.
  // Source: vvaharness/models/scan/_finding_section.py:106-108
  if (the source predicate f.vsvs_score is not None is truthy) {
    // Source: vvaharness/models/scan/_finding_section.py:107-108
    In source order: Evaluate out.append((source_template_107_20, False)); retain side effects and discard the expression result.
  }
  // Source: vvaharness/models/scan/_finding_section.py:109-112
  if (the source predicate f.offensive_priority is truthy) {
    // Source: vvaharness/models/scan/_finding_section.py:110-112
    In source order: Evaluate out.append((source_template_110_20, False)); retain side effects and discard the expression result.
  }
  // Source: vvaharness/models/scan/_finding_section.py:113-121
  if (the source predicate f.duplicates is truthy) {
    // Source: vvaharness/models/scan/_finding_section.py:115-121
    In source order: Evaluate once ', '.join((source_template_116_12 + (source_template_117_15 if d.line_end and d.line_end != d.line_start else '`') for d in f.duplicates)); assign in source target order to refs. Then Evaluate out.append((source_template_121_20, False)); retain side effects and discard the expression result.
  }
  // Source: vvaharness/models/scan/_finding_section.py:122-122
  In source order: Evaluate out.append(('', True)); retain side effects and discard the expression result.
  // Source: vvaharness/models/scan/_finding_section.py:123-129
  if (the source predicate f.duplicates is truthy) {
    // Source: vvaharness/models/scan/_finding_section.py:124-129
    In source order: Evaluate out.extend([(source_template_125_14, True), ('', True)]); retain side effects and discard the expression result.
  }
  // Source: vvaharness/models/scan/_finding_section.py:131-133
  In source order: Evaluate out.extend([('#### Description', True), (_demote_md_headings(f.description, escape_angles=True), True), ('', True)]); retain side effects and discard the expression result.
  // Source: vvaharness/models/scan/_finding_section.py:134-137
  if (the source predicate f.impact is truthy) {
    // Source: vvaharness/models/scan/_finding_section.py:135-137
    In source order: Evaluate out.extend([('#### Impact', True), (_demote_md_headings(f.impact, escape_angles=True), True), ('', True)]); retain side effects and discard the expression result.
  }
  // Source: vvaharness/models/scan/_finding_section.py:138-142
  if (the source predicate f.exploit_scenario is truthy) {
    // Source: vvaharness/models/scan/_finding_section.py:139-142
    In source order: Evaluate out.extend([('#### Exploit scenario', True), (_demote_md_headings(f.exploit_scenario, escape_angles=True), True), ('', True)]); retain side effects and discard the expression result.
  }
  // Source: vvaharness/models/scan/_finding_section.py:143-146
  if (the source predicate f.preconditions is truthy) {
    // Source: vvaharness/models/scan/_finding_section.py:144-146
    In source order: Evaluate out.append(('#### Preconditions', True)); retain side effects and discard the expression result. Then Evaluate out.extend(((source_template_145_20, True) for p in f.preconditions)); retain side effects and discard the expression result. Then Evaluate out.append(('', True)); retain side effects and discard the expression result.
  }
  // Source: vvaharness/models/scan/_finding_section.py:148-154
  In source order: Evaluate once _snippet_fence(f.code_snippet); assign in source target order to _snip_fence. Then Evaluate out.extend([(_snip_fence, True), (f.code_snippet, True), (_snip_fence, True), ('', True)]); retain side effects and discard the expression result.
  // Source: vvaharness/models/scan/_finding_section.py:155-159
  if (the source predicate f.recommendation is truthy) {
    // Source: vvaharness/models/scan/_finding_section.py:156-159
    In source order: Evaluate out.extend([('#### How to fix', True), (_demote_md_headings(f.recommendation, escape_angles=True), True), ('', True)]); retain side effects and discard the expression result.
  }
  // Source: vvaharness/models/scan/_finding_section.py:161-162
  In source order: Evaluate out.extend([(source_template_161_18, True), ('', True)]); retain side effects and discard the expression result.
  // Source: vvaharness/models/scan/_finding_section.py:163-170
  if (the source predicate f.verdict is truthy) {
    // Source: vvaharness/models/scan/_finding_section.py:164-170
    In source order: Evaluate out.extend([('#### Adversarial verification', True), (source_template_166_14, True), ('', True)]); retain side effects and discard the expression result.
  }
  // Source: vvaharness/models/scan/_finding_section.py:172-234
  if (the source predicate f.ev_status in _EV_VERDICT_LABEL is truthy) {
    // Source: vvaharness/models/scan/_finding_section.py:173-180
    In source order: Evaluate once _EV_VERDICT_LABEL[f.ev_status]; assign in source target order to verdict. Then Evaluate once _one_line(f.ev_evidence) if f.ev_evidence else ''; assign in source target order to reason. Then Evaluate out.append(('#### Exploit Verification', True)); retain side effects and discard the expression result. Then Evaluate once source_template_179_21 if f.ev_confidence_score is not None else None; assign in source target order to conf_line.
    // Source: vvaharness/models/scan/_finding_section.py:181-203
    if (the source predicate f.ev_status == 'CONFIRMED' is truthy) {
      // Source: vvaharness/models/scan/_finding_section.py:183-187
      In source order: Evaluate out.extend([(source_template_184_17 + (source_template_185_20 if reason else ''), False), ('', True)]); retain side effects and discard the expression result.
      // Source: vvaharness/models/scan/_finding_section.py:188-189
      if (the source predicate conf_line is truthy) {
        // Source: vvaharness/models/scan/_finding_section.py:189-189
        In source order: Evaluate out.extend([(conf_line, False), ('', True)]); retain side effects and discard the expression result.
      }
    }
    else {
      // Source: vvaharness/models/scan/_finding_section.py:192-193
      In source order: Evaluate out.extend([(source_template_192_25, False), ('', True)]); retain side effects and discard the expression result.
      // Source: vvaharness/models/scan/_finding_section.py:194-195
      if (the source predicate conf_line is truthy) {
        // Source: vvaharness/models/scan/_finding_section.py:195-195
        In source order: Evaluate out.extend([(conf_line, False), ('', True)]); retain side effects and discard the expression result.
      }
      // Source: vvaharness/models/scan/_finding_section.py:196-202
      if (the source predicate reason is truthy) {
        // Source: vvaharness/models/scan/_finding_section.py:197-202
        In source order: Evaluate out.extend([(source_template_198_21, False), ('', True)]); retain side effects and discard the expression result.
      }
      // Source: vvaharness/models/scan/_finding_section.py:203-203
      In source order: Evaluate out.extend([(_EV_NOT_A_FP_NOTE, False), ('', True)]); retain side effects and discard the expression result.
    }
    // Source: vvaharness/models/scan/_finding_section.py:205-234
    if (the source predicate f.ev_status == 'CONFIRMED' is truthy) {
      // Source: vvaharness/models/scan/_finding_section.py:206-211
      if (the source predicate f.ev_method or f.ev_confidence is truthy) {
        // Source: vvaharness/models/scan/_finding_section.py:207-211
        In source order: Evaluate out.extend([(source_template_208_22, False), ('', True)]); retain side effects and discard the expression result.
      }
      // Source: vvaharness/models/scan/_finding_section.py:212-221
      if (the source predicate f.ev_cvss_score is not None is truthy) {
        // Source: vvaharness/models/scan/_finding_section.py:214-221
        In source order: Evaluate out.extend([(source_template_215_21 + (source_template_216_24 if f.ev_cvss_rating else '') + (source_template_217_24 if f.ev_cvss_vector else ''), False), ('', True)]); retain side effects and discard the expression result.
      }
      // Source: vvaharness/models/scan/_finding_section.py:222-225
      if (the source predicate f.ev_repro is truthy) {
        // Source: vvaharness/models/scan/_finding_section.py:224-225
        In source order: Evaluate out.extend([(source_template_224_29, False), ('', True)]); retain side effects and discard the expression result.
      }
      // Source: vvaharness/models/scan/_finding_section.py:226-234
      if (the source predicate f.ev_repro_detail is truthy) {
        // Source: vvaharness/models/scan/_finding_section.py:228-228
        In source order: Evaluate once False; assign in source target order to in_details.
        // Source: vvaharness/models/scan/_finding_section.py:229-234
        for each ln in _render_repro_block(f.ev_repro_detail) {
          // Source: vvaharness/models/scan/_finding_section.py:230-231
          if (the source predicate ln.startswith('<details>') is truthy) {
            // Source: vvaharness/models/scan/_finding_section.py:231-231
            In source order: Evaluate once True; assign in source target order to in_details.
          }
          // Source: vvaharness/models/scan/_finding_section.py:232-232
          In source order: Evaluate out.append((ln, ln == '' and (not in_details))); retain side effects and discard the expression result.
          // Source: vvaharness/models/scan/_finding_section.py:233-234
          if (the source predicate ln == '</details>' is truthy) {
            // Source: vvaharness/models/scan/_finding_section.py:234-234
            In source order: Evaluate once False; assign in source target order to in_details.
          }
        }
      }
    }
  }
  // Source: vvaharness/models/scan/_finding_section.py:235-235
  End this invocation with out.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.models.scan._render import _code_span, _confidence_label, _demote_md_headings, _md_cell, _one_line, _render_repro_block, _snippet_fence, _vector_span` at source line 19: `source_detail/vvaharness/models/scan/_render.py.sudo.md`.
- `from vvaharness.models.scan.findings import RankedFinding` at source line 29: `source_detail/vvaharness/models/scan/findings.py.sudo.md`.
- `from vvaharness.models.vocab import OFFENSIVE_LABELS` at source line 30: `source_detail/vvaharness/models/vocab.py.sudo.md`.
- `from vvaharness.report.cwe import cwe_for, cwe_name` at source line 83: `source_detail/vvaharness/report/cwe.py.sudo.md`.
