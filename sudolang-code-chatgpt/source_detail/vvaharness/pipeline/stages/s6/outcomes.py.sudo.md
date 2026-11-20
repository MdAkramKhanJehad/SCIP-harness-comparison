# vvaharness/pipeline/stages/s6/outcomes.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/pipeline/stages/s6/outcomes.py.evidence.json`. SHA-256: `59939a21f74c487904ed86bcbe40320bd124fd632d6f6e696de6959db63809f2`.

```sudo
// Source: vvaharness/pipeline/stages/s6/outcomes.py:15-20
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import math; preserve alias and import-time effects. Then Resolve source import import re; preserve alias and import-time effects. Then Resolve source import from collections.abc import Callable, Collection; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s6/outcomes.py:21-27
In source order: Resolve source import from typing import Literal; preserve alias and import-time effects. Then Resolve source import from pydantic import BaseModel, Field, field_validator; preserve alias and import-time effects. Then Resolve source import from pydantic.json_schema import SkipJsonSchema; preserve alias and import-time effects. Then Resolve source import from vvaharness.models.scan.findings import Finding; preserve alias and import-time effects. Then Resolve source import from vvaharness.models.scan._coerce import flag as _coerce_bool; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s6/outcomes.py:28-32
In source order: Resolve source import from vvaharness.pipeline.stages.s4.outcomes import InvestigatedFinding, fan_out; preserve alias and import-time effects. Then Resolve source import from vvaharness.report.cvss import rating as cvss_rating; preserve alias and import-time effects. Then Resolve source import from vvaharness.report.cvss import score as cvss_score; preserve alias and import-time effects. Then Resolve source import from vvaharness.rules.cwe import norm_cwe; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.counters import COUNTERS; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s6/outcomes.py:33-36
In source order: Resolve source import from vvaharness.util.json_extract import extract_json; preserve alias and import-time effects. Then Evaluate once re.compile('\\s*([^/]*?)\\s*/\\s*10\\s*'); assign in source target order to _OUT_OF_TEN.
// Source: vvaharness/pipeline/stages/s6/outcomes.py:39-128
interface VerificationOutcome {
  Describe the source Python type, preserving its base/metaclass expression order: BaseModel.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/pipeline/stages/s6/outcomes.py:40-50
  In source order: For finding_id, assign Field(description='Echo the FINDING id you were given, verbatim.'); source annotation str. Then For verdict, assign Field(description=source_literal_42_8); source annotation Literal['TRUE_POSITIVE', 'FALSE_POSITIVE', 'INCONCLUSIVE']. Then For confidence, assign Field(ge=0, le=10, description=source_literal_48_8); source annotation int.
  // Source: vvaharness/pipeline/stages/s6/outcomes.py:54-72
  // Source: vvaharness/pipeline/stages/s6/outcomes.py:52-53
  Before creating this callable, evaluate and retain decorators top-to-bottom: field_validator('confidence', mode='before'), classmethod.
  // Source: vvaharness/pipeline/stages/s6/outcomes.py:54-72
  // Source signature: _clamp_confidence(cls, v: object) -> object
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _clamp_confidence(cls, v) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/pipeline/stages/s6/outcomes.py:55-56
    In source order: Retain source documentation literal source_literal_55_8; it is not a model call. Then Evaluate once _OUT_OF_TEN.fullmatch(v) if isinstance(v, str) else None; assign in source target order to m.
    // Source: vvaharness/pipeline/stages/s6/outcomes.py:57-63
    Perform the following protected operations {
      // Source: vvaharness/pipeline/stages/s6/outcomes.py:58-58
      In source order: Evaluate once float(m.group(1) if m else v); assign in source target order to f.
    }
    // Source: vvaharness/pipeline/stages/s6/outcomes.py:59-60
    On the first matching source exception (TypeError, ValueError), in handler order {
      // Source: vvaharness/pipeline/stages/s6/outcomes.py:60-60
      End this invocation with v.
    }
    // Source: vvaharness/pipeline/stages/s6/outcomes.py:61-63
    On the first matching source exception OverflowError, in handler order {
      // Source: vvaharness/pipeline/stages/s6/outcomes.py:63-63
      In source order: Evaluate once math.inf if isinstance(v, int) and v > 0 else -math.inf; assign in source target order to f.
    }
    // Source: vvaharness/pipeline/stages/s6/outcomes.py:64-68
    if (the source predicate not math.isfinite(f) is truthy) {
      // Source: vvaharness/pipeline/stages/s6/outcomes.py:66-66
      In source order: Evaluate once 10 if f > 0 else 0; assign in source target order to score.
    }
    else {
      // Source: vvaharness/pipeline/stages/s6/outcomes.py:68-68
      In source order: Evaluate once min(10, max(0, int(f))); assign in source target order to score.
    }
    // Source: vvaharness/pipeline/stages/s6/outcomes.py:69-71
    if (the source predicate score != f is truthy) {
      // Source: vvaharness/pipeline/stages/s6/outcomes.py:71-71
      In source order: Evaluate COUNTERS.bump('s6_confidence_clamped'); retain side effects and discard the expression result.
    }
    // Source: vvaharness/pipeline/stages/s6/outcomes.py:72-72
    End this invocation with score.
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vvaharness/pipeline/stages/s6/outcomes.py:73-92
  In source order: For reason, assign Field(description='Why, in one or two sentences. Required for every verdict.'); source annotation str. Then For corrected_cwe, assign Field(default='', description=source_literal_75_8); source annotation str. Then For corrected_line_start, assign Field(default=0, description=source_literal_81_8); source annotation int. Then For confirmed_repeat_lines, assign Field(default=[], description=source_literal_85_8); source annotation list[int]. Then For cvss_vector, assign Field(default='', description=source_literal_91_8); source annotation str.
  // Source: vvaharness/pipeline/stages/s6/outcomes.py:93-107
  In source order: For control_absence, assign Field(default=False, description=source_literal_94_8); source annotation bool. Then For channel, assign Field(default='main', description=source_literal_100_8); source annotation str. Then For reframed, assign Field(default=False, description=source_literal_105_8); source annotation bool.
  // Source: vvaharness/pipeline/stages/s6/outcomes.py:111-113
  // Source: vvaharness/pipeline/stages/s6/outcomes.py:109-110
  Before creating this callable, evaluate and retain decorators top-to-bottom: field_validator('control_absence', 'reframed', mode='before'), classmethod.
  // Source: vvaharness/pipeline/stages/s6/outcomes.py:111-113
  // Source signature: _coerce_flag(cls, v: object) -> bool
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _coerce_flag(cls, v) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/pipeline/stages/s6/outcomes.py:112-112
    In source order: Retain source documentation literal source_literal_112_8; it is not a model call.
    // Source: vvaharness/pipeline/stages/s6/outcomes.py:113-113
    End this invocation with _coerce_bool(v).
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vvaharness/pipeline/stages/s6/outcomes.py:117-120
  // Source: vvaharness/pipeline/stages/s6/outcomes.py:115-116
  Before creating this callable, evaluate and retain decorators top-to-bottom: field_validator('channel', mode='before'), classmethod.
  // Source: vvaharness/pipeline/stages/s6/outcomes.py:117-120
  // Source signature: _coerce_channel(cls, v: object) -> str
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _coerce_channel(cls, v) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/pipeline/stages/s6/outcomes.py:118-118
    In source order: Retain source documentation literal source_literal_118_8; it is not a model call.
    // Source: vvaharness/pipeline/stages/s6/outcomes.py:119-120
    End this invocation with 'posture' if isinstance(v, str) and v.strip().lower() == 'posture' else 'main'.
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vvaharness/pipeline/stages/s6/outcomes.py:121-128
  In source order: For additional_findings, assign Field(default=[], description=source_literal_122_8); source annotation list[InvestigatedFinding]. Then For replayed, assign False; source annotation SkipJsonSchema[bool].
}
// Source: vvaharness/pipeline/stages/s6/outcomes.py:131-135
interface VerificationOutcomes {
  Describe the source Python type, preserving its base/metaclass expression order: BaseModel.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/pipeline/stages/s6/outcomes.py:132-135
  In source order: For outcomes, assign Field(description=source_literal_133_8); source annotation list[VerificationOutcome].
}
// Source: vvaharness/pipeline/stages/s6/outcomes.py:138-142
// Source signature: _validate_direct(raw: str) -> VerificationOutcomes | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _validate_direct(raw) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s6/outcomes.py:139-142
  Perform the following protected operations {
    // Source: vvaharness/pipeline/stages/s6/outcomes.py:140-140
    End this invocation with VerificationOutcomes.model_validate_json(raw).
  }
  // Source: vvaharness/pipeline/stages/s6/outcomes.py:141-142
  On the first matching source exception ValueError, in handler order {
    // Source: vvaharness/pipeline/stages/s6/outcomes.py:142-142
    End this invocation with None.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s6/outcomes.py:145-149
// Source signature: _validate_salvaged(raw: str) -> VerificationOutcomes | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _validate_salvaged(raw) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s6/outcomes.py:146-149
  Perform the following protected operations {
    // Source: vvaharness/pipeline/stages/s6/outcomes.py:147-147
    End this invocation with VerificationOutcomes.model_validate(extract_json(raw)).
  }
  // Source: vvaharness/pipeline/stages/s6/outcomes.py:148-149
  On the first matching source exception ValueError, in handler order {
    // Source: vvaharness/pipeline/stages/s6/outcomes.py:149-149
    End this invocation with None.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s6/outcomes.py:152-156
// Source signature: _validate_lone(raw: str) -> VerificationOutcomes | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _validate_lone(raw) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s6/outcomes.py:153-156
  Perform the following protected operations {
    // Source: vvaharness/pipeline/stages/s6/outcomes.py:154-154
    End this invocation with VerificationOutcomes(outcomes=[VerificationOutcome.model_validate_json(raw)]).
  }
  // Source: vvaharness/pipeline/stages/s6/outcomes.py:155-156
  On the first matching source exception ValueError, in handler order {
    // Source: vvaharness/pipeline/stages/s6/outcomes.py:156-156
    End this invocation with None.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s6/outcomes.py:159-168
// Source signature: parse_outcomes(raw: str) -> VerificationOutcomes | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn parse_outcomes(raw) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s6/outcomes.py:160-160
  In source order: Retain source documentation literal source_literal_160_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s6/outcomes.py:161-164
  for each attempt in (_validate_direct, _validate_salvaged, _validate_lone) {
    // Source: vvaharness/pipeline/stages/s6/outcomes.py:162-162
    In source order: Evaluate once attempt(raw); assign in source target order to parsed.
    // Source: vvaharness/pipeline/stages/s6/outcomes.py:163-164
    if (the source predicate parsed is not None is truthy) {
      // Source: vvaharness/pipeline/stages/s6/outcomes.py:164-164
      End this invocation with parsed.
    }
  }
  // Source: vvaharness/pipeline/stages/s6/outcomes.py:165-167
  In source order: Evaluate once (raw or '').strip(); assign in source target order to stripped. Then Evaluate COUNTERS.bump('s6_outcome_truncated' if stripped and (not stripped.endswith('}')) else 's6_outcome_malformed'); retain side effects and discard the expression result.
  // Source: vvaharness/pipeline/stages/s6/outcomes.py:168-168
  End this invocation with None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s6/outcomes.py:171-186
// Source signature: split_batch_reply(raw: str, finding_ids: list[str]) -> dict[str, VerificationOutcome]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn split_batch_reply(raw, finding_ids) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s6/outcomes.py:172-173
  In source order: Retain source documentation literal source_literal_172_4; it is not a model call. Then Evaluate once parse_outcomes(raw); assign in source target order to parsed.
  // Source: vvaharness/pipeline/stages/s6/outcomes.py:174-175
  if (the source predicate parsed is None is truthy) {
    // Source: vvaharness/pipeline/stages/s6/outcomes.py:175-175
    End this invocation with {}.
  }
  // Source: vvaharness/pipeline/stages/s6/outcomes.py:176-177
  In source order: Evaluate once set(finding_ids); assign in source target order to wanted. Then For by_id, assign {}; source annotation dict[str, VerificationOutcome].
  // Source: vvaharness/pipeline/stages/s6/outcomes.py:178-182
  for each outcome in parsed.outcomes {
    // Source: vvaharness/pipeline/stages/s6/outcomes.py:179-181
    if (the source predicate outcome.finding_id not in wanted is truthy) {
      // Source: vvaharness/pipeline/stages/s6/outcomes.py:180-180
      In source order: Evaluate COUNTERS.bump('s6_batch_finding_id_invented'); retain side effects and discard the expression result.
      // Source: vvaharness/pipeline/stages/s6/outcomes.py:181-181
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/pipeline/stages/s6/outcomes.py:182-182
    In source order: Evaluate once outcome; assign in source target order to by_id[outcome.finding_id].
  }
  // Source: vvaharness/pipeline/stages/s6/outcomes.py:183-183
  In source order: Evaluate once len(wanted) - len(by_id); assign in source target order to absent.
  // Source: vvaharness/pipeline/stages/s6/outcomes.py:184-185
  if (the source predicate absent is truthy) {
    // Source: vvaharness/pipeline/stages/s6/outcomes.py:185-185
    In source order: Evaluate COUNTERS.bump('s6_batch_finding_omitted', absent); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s6/outcomes.py:186-186
  End this invocation with by_id.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s6/outcomes.py:190-190
In source order: Evaluate once re.compile('(?<![\\w./$-])f\\d+\\b(?!\\.\\w)'); assign in source target order to _REASON_PROSE_ID_RX.
// Source: vvaharness/pipeline/stages/s6/outcomes.py:193-198
// Source signature: remap_reason_ids(reason: str, display: dict[str, str]) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn remap_reason_ids(reason, display) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s6/outcomes.py:194-194
  In source order: Retain source documentation literal source_literal_194_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s6/outcomes.py:195-196
  if (the source predicate not reason is truthy) {
    // Source: vvaharness/pipeline/stages/s6/outcomes.py:196-196
    End this invocation with reason.
  }
  // Source: vvaharness/pipeline/stages/s6/outcomes.py:197-198
  End this invocation with _REASON_PROSE_ID_RX.sub(lambda m: display.get(m.group(0), m.group(0)), reason).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s6/outcomes.py:201-228
// Source signature: _corrections(f: Finding, outcome: VerificationOutcome, max_line: int | None=None) -> dict
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _corrections(f, outcome, max_line) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s6/outcomes.py:203-205
  In source order: Retain source documentation literal source_literal_203_4; it is not a model call. Then For fixed, assign {}; source annotation dict. Then Evaluate once norm_cwe(outcome.corrected_cwe); assign in source target order to cwe.
  // Source: vvaharness/pipeline/stages/s6/outcomes.py:206-208
  if (the source predicate cwe and cwe != f.cwe is truthy) {
    // Source: vvaharness/pipeline/stages/s6/outcomes.py:207-208
    In source order: Evaluate once cwe; assign in source target order to fixed['cwe']. Then Evaluate COUNTERS.bump('s6_finding_cwe_corrected'); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s6/outcomes.py:209-209
  In source order: Evaluate once outcome.corrected_line_start; assign in source target order to line.
  // Source: vvaharness/pipeline/stages/s6/outcomes.py:210-221
  if (the source predicate line > 0 and line != f.line_start is truthy) {
    // Source: vvaharness/pipeline/stages/s6/outcomes.py:212-221
    if (the source predicate f.pre_anchor_line > 0 and line == f.pre_anchor_line is truthy) {
      // Source: vvaharness/pipeline/stages/s6/outcomes.py:213-213
      In source order: Evaluate COUNTERS.bump('s6_finding_line_correction_reverted_reanchor'); retain side effects and discard the expression result.
    }
    else {
      // Source: vvaharness/pipeline/stages/s6/outcomes.py:214-221
      if (the source predicate max_line is not None and line > max_line is truthy) {
        // Source: vvaharness/pipeline/stages/s6/outcomes.py:215-215
        In source order: Evaluate COUNTERS.bump('s6_finding_line_correction_ignored'); retain side effects and discard the expression result.
      }
      else {
        // Source: vvaharness/pipeline/stages/s6/outcomes.py:217-221
        In source order: Evaluate once line; assign in source target order to fixed['line_start']. Then Evaluate once max(f.line_end, line); assign in source target order to fixed['line_end']. Then Evaluate once 0; assign in source target order to fixed['pre_anchor_line']. Then Evaluate COUNTERS.bump('s6_finding_line_corrected'); retain side effects and discard the expression result.
      }
    }
  }
  // Source: vvaharness/pipeline/stages/s6/outcomes.py:223-227
  if (the source predicate max_line is not None is truthy) {
    // Source: vvaharness/pipeline/stages/s6/outcomes.py:224-224
    In source order: Evaluate once fixed.get('line_end', f.line_end); assign in source target order to end.
    // Source: vvaharness/pipeline/stages/s6/outcomes.py:225-227
    if (the source predicate end > max_line is truthy) {
      // Source: vvaharness/pipeline/stages/s6/outcomes.py:226-227
      In source order: Evaluate once max_line; assign in source target order to fixed['line_end']. Then Evaluate COUNTERS.bump('s6_finding_line_end_clamped_eof'); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/pipeline/stages/s6/outcomes.py:228-228
  End this invocation with fixed.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s6/outcomes.py:231-240
// Source signature: _trait_stamps(outcome: VerificationOutcome) -> dict
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _trait_stamps(outcome) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s6/outcomes.py:232-233
  In source order: Retain source documentation literal source_literal_232_4; it is not a model call. Then For stamped, assign {}; source annotation dict.
  // Source: vvaharness/pipeline/stages/s6/outcomes.py:234-236
  if (the source predicate outcome.control_absence is truthy) {
    // Source: vvaharness/pipeline/stages/s6/outcomes.py:235-236
    In source order: Evaluate once True; assign in source target order to stamped['control_absence']. Then Evaluate COUNTERS.bump('s6_stamp_control_absence'); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s6/outcomes.py:237-239
  if (the source predicate outcome.channel == 'posture' is truthy) {
    // Source: vvaharness/pipeline/stages/s6/outcomes.py:238-239
    In source order: Evaluate once 'posture'; assign in source target order to stamped['channel']. Then Evaluate COUNTERS.bump('s6_stamp_channel_posture'); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s6/outcomes.py:240-240
  End this invocation with stamped.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s6/outcomes.py:243-259
// Source signature: _verdict_fields(outcome: VerificationOutcome) -> dict
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _verdict_fields(outcome) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s6/outcomes.py:244-247
  In source order: Retain source documentation literal source_literal_244_4; it is not a model call. Then Evaluate once outcome.cvss_vector.strip() or None; assign in source target order to vector. Then Evaluate once cvss_score(vector) if vector else None; assign in source target order to score.
  // Source: vvaharness/pipeline/stages/s6/outcomes.py:248-251
  if (the source predicate outcome.verdict == 'TRUE_POSITIVE' and vector and (score == 0.0) is truthy) {
    // Source: vvaharness/pipeline/stages/s6/outcomes.py:250-251
    In source order: Evaluate COUNTERS.bump('s6_cvss_zero_impact_on_tp'); retain side effects and discard the expression result. Then Evaluate once (None, None); assign in source target order to (vector, score).
  }
  // Source: vvaharness/pipeline/stages/s6/outcomes.py:252-259
  End this invocation with {'verdict': outcome.verdict if outcome.verdict != 'INCONCLUSIVE' else None, 'verdict_confidence': outcome.confidence, 'verdict_reason': outcome.reason, 'cvss_vector': vector, 'cvss_score': score, 'cvss_rating': cvss_rating(score) if score is not None else None}.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s6/outcomes.py:262-276
// Source signature: classify(outcome: VerificationOutcome, min_confidence: int) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn classify(outcome, min_confidence) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s6/outcomes.py:263-263
  In source order: Retain source documentation literal source_literal_263_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s6/outcomes.py:265-268
  if (the source predicate outcome.replayed and outcome.verdict == 'FALSE_POSITIVE' and (outcome.confidence < min_confidence) is truthy) {
    // Source: vvaharness/pipeline/stages/s6/outcomes.py:267-267
    In source order: Evaluate COUNTERS.bump('s6_replayed_fp_held'); retain side effects and discard the expression result.
    // Source: vvaharness/pipeline/stages/s6/outcomes.py:268-268
    End this invocation with 'INCONCLUSIVE'.
  }
  // Source: vvaharness/pipeline/stages/s6/outcomes.py:269-271
  if (the source predicate outcome.verdict == 'INCONCLUSIVE' is truthy) {
    // Source: vvaharness/pipeline/stages/s6/outcomes.py:270-270
    In source order: Evaluate COUNTERS.bump('s6_verdict_inconclusive'); retain side effects and discard the expression result.
    // Source: vvaharness/pipeline/stages/s6/outcomes.py:271-271
    End this invocation with 'INCONCLUSIVE'.
  }
  // Source: vvaharness/pipeline/stages/s6/outcomes.py:272-273
  if (the source predicate outcome.verdict == 'FALSE_POSITIVE' is truthy) {
    // Source: vvaharness/pipeline/stages/s6/outcomes.py:273-273
    End this invocation with 'FALSE_POSITIVE'.
  }
  // Source: vvaharness/pipeline/stages/s6/outcomes.py:274-275
  if (the source predicate outcome.confidence < min_confidence is truthy) {
    // Source: vvaharness/pipeline/stages/s6/outcomes.py:275-275
    End this invocation with 'UNCONFIRMED'.
  }
  // Source: vvaharness/pipeline/stages/s6/outcomes.py:276-276
  End this invocation with 'TRUE_POSITIVE'.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s6/outcomes.py:279-301
// Source signature: _new_repeat_lines(primary: Finding, outcome: VerificationOutcome, reserve: Callable[[int], bool], max_line: int | None=None) -> list[int]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _new_repeat_lines(primary, outcome, reserve, max_line) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s6/outcomes.py:282-283
  In source order: Retain source documentation literal source_literal_282_4; it is not a model call. Then Evaluate once ([], 0, 0); assign in source target order to (fresh, stale, oob).
  // Source: vvaharness/pipeline/stages/s6/outcomes.py:284-294
  for each n in sorted(set(outcome.confirmed_repeat_lines)) {
    // Source: vvaharness/pipeline/stages/s6/outcomes.py:285-286
    if (the source predicate n <= 0 or n == primary.line_start is truthy) {
      // Source: vvaharness/pipeline/stages/s6/outcomes.py:286-286
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/pipeline/stages/s6/outcomes.py:287-289
    if (the source predicate max_line is not None and n > max_line is truthy) {
      // Source: vvaharness/pipeline/stages/s6/outcomes.py:288-288
      In source order: Apply source augmented assignment oob += 1 with source evaluation/in-place semantics.
      // Source: vvaharness/pipeline/stages/s6/outcomes.py:289-289
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/pipeline/stages/s6/outcomes.py:291-293
    if (the source predicate not reserve(n) is truthy) {
      // Source: vvaharness/pipeline/stages/s6/outcomes.py:292-292
      In source order: Apply source augmented assignment stale += 1 with source evaluation/in-place semantics.
      // Source: vvaharness/pipeline/stages/s6/outcomes.py:293-293
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/pipeline/stages/s6/outcomes.py:294-294
    In source order: Evaluate fresh.append(n); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s6/outcomes.py:295-296
  if (the source predicate oob is truthy) {
    // Source: vvaharness/pipeline/stages/s6/outcomes.py:296-296
    In source order: Evaluate COUNTERS.bump('s6_finding_repeat_beyond_eof', oob); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s6/outcomes.py:297-298
  if (the source predicate stale is truthy) {
    // Source: vvaharness/pipeline/stages/s6/outcomes.py:298-298
    In source order: Evaluate COUNTERS.bump('s6_finding_repeat_already_filed', stale); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s6/outcomes.py:299-300
  if (the source predicate fresh is truthy) {
    // Source: vvaharness/pipeline/stages/s6/outcomes.py:300-300
    In source order: Evaluate COUNTERS.bump('s6_finding_repeat_confirmed', len(fresh)); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s6/outcomes.py:301-301
  End this invocation with fresh.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s6/outcomes.py:304-338
// Source signature: apply_outcome(f: Finding, outcome: VerificationOutcome, reserve: Callable[[int], bool] | None=None, *, stamps: bool=True, reframe: bool=False, max_line: int | None=None, clone_repeats: bool=True) -> list[Finding]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn apply_outcome(f, outcome, reserve, stamps, reframe, max_line, clone_repeats) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s6/outcomes.py:309-310
  In source order: Retain source documentation literal source_literal_309_4; it is not a model call. Then Evaluate once {**_verdict_fields(outcome), **_corrections(f, outcome, max_line)}; assign in source target order to update.
  // Source: vvaharness/pipeline/stages/s6/outcomes.py:311-312
  if (the source predicate stamps is truthy) {
    // Source: vvaharness/pipeline/stages/s6/outcomes.py:312-312
    In source order: Evaluate update.update(_trait_stamps(outcome)); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s6/outcomes.py:313-313
  In source order: Evaluate once f.model_copy(update=update); assign in source target order to primary.
  // Source: vvaharness/pipeline/stages/s6/outcomes.py:314-315
  if (the source predicate outcome.verdict != 'TRUE_POSITIVE' is truthy) {
    // Source: vvaharness/pipeline/stages/s6/outcomes.py:315-315
    End this invocation with [primary].
  }
  // Source: vvaharness/pipeline/stages/s6/outcomes.py:316-320
  if (the source predicate reserve is None is truthy) {
    // Source: vvaharness/pipeline/stages/s6/outcomes.py:317-317
    In source order: Evaluate once lambda _line: True; assign in source target order to reserve.
  }
  else {
    // Source: vvaharness/pipeline/stages/s6/outcomes.py:318-320
    if (the source predicate primary.line_start != f.line_start is truthy) {
      // Source: vvaharness/pipeline/stages/s6/outcomes.py:320-320
      In source order: Evaluate reserve(primary.line_start); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/pipeline/stages/s6/outcomes.py:321-324
  if (the source predicate reframe and outcome.reframed is truthy) {
    // Source: vvaharness/pipeline/stages/s6/outcomes.py:323-323
    In source order: Evaluate COUNTERS.bump('s6_verdict_reframed'); retain side effects and discard the expression result.
    // Source: vvaharness/pipeline/stages/s6/outcomes.py:324-324
    End this invocation with [primary].
  }
  // Source: vvaharness/pipeline/stages/s6/outcomes.py:325-330
  if (the source predicate not clone_repeats is truthy) {
    // Source: vvaharness/pipeline/stages/s6/outcomes.py:326-329
    if (the source predicate outcome.confirmed_repeat_lines is truthy) {
      // Source: vvaharness/pipeline/stages/s6/outcomes.py:328-329
      In source order: Evaluate COUNTERS.bump('s6_repeat_clone_reverify_discarded', len(outcome.confirmed_repeat_lines)); retain side effects and discard the expression result.
    }
    // Source: vvaharness/pipeline/stages/s6/outcomes.py:330-330
    End this invocation with [primary].
  }
  // Source: vvaharness/pipeline/stages/s6/outcomes.py:332-332
  In source order: Evaluate once _new_repeat_lines(primary, outcome, reserve, max_line); assign in source target order to extra.
  // Source: vvaharness/pipeline/stages/s6/outcomes.py:334-338
  End this invocation with [primary, *(primary.model_copy(update={'line_start': n, 'line_end': n, 'is_repeat_clone': True, 'code_snippet': '', 'sink_ref': None, 'source_ref': None, 'backfilled_refs': [], 'pre_anchor_line': 0}) for n in extra)].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s6/outcomes.py:341-359
// Source signature: discovered(outcome: VerificationOutcome, parent: Finding, *, repo_root: str, inventory: Collection[str]) -> list[Finding]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn discovered(outcome, parent, repo_root, inventory) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s6/outcomes.py:343-343
  In source order: Retain source documentation literal source_literal_343_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s6/outcomes.py:344-345
  if (the source predicate not outcome.additional_findings is truthy) {
    // Source: vvaharness/pipeline/stages/s6/outcomes.py:345-345
    End this invocation with [].
  }
  // Source: vvaharness/pipeline/stages/s6/outcomes.py:347-354
  In source order: Evaluate once source_template_347_12; assign in source target order to chunk. Then Evaluate once {'verdict': 'TRUE_POSITIVE', 'verdict_confidence': outcome.confidence, 'verdict_reason': source_template_351_26, 'origin': 's6_discovered'}; assign in source target order to verdict. Then For out, assign []; source annotation list[Finding].
  // Source: vvaharness/pipeline/stages/s6/outcomes.py:355-357
  for each extra in outcome.additional_findings {
    // Source: vvaharness/pipeline/stages/s6/outcomes.py:356-357
    In source order: Evaluate out.extend(fan_out(extra, chunk, [parent.cwe] if parent.cwe else [], repo_root=repo_root, inventory=inventory)); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s6/outcomes.py:358-358
  In source order: Evaluate COUNTERS.bump('s6_finding_discovered', len(out)); retain side effects and discard the expression result.
  // Source: vvaharness/pipeline/stages/s6/outcomes.py:359-359
  End this invocation with [f.model_copy(update=verdict) for f in out].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s6/outcomes.py:362-365
// Source signature: unverified(f: Finding, detail: str) -> Finding
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn unverified(f, detail) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s6/outcomes.py:363-363
  In source order: Retain source documentation literal source_literal_363_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s6/outcomes.py:364-365
  End this invocation with f.model_copy(update={'verdict': None, 'verdict_confidence': 0, 'verdict_reason': detail}).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.models.scan.findings import Finding` at source line 26: `source_detail/vvaharness/models/scan/findings.py.sudo.md`.
- `from vvaharness.models.scan._coerce import flag as _coerce_bool` at source line 27: `source_detail/vvaharness/models/scan/_coerce.py.sudo.md`.
- `from vvaharness.pipeline.stages.s4.outcomes import InvestigatedFinding, fan_out` at source line 28: `source_detail/vvaharness/pipeline/stages/s4/outcomes.py.sudo.md`.
- `from vvaharness.report.cvss import rating as cvss_rating` at source line 29: `source_detail/vvaharness/report/cvss.py.sudo.md`.
- `from vvaharness.report.cvss import score as cvss_score` at source line 30: `source_detail/vvaharness/report/cvss.py.sudo.md`.
- `from vvaharness.rules.cwe import norm_cwe` at source line 31: `source_detail/vvaharness/rules/cwe.py.sudo.md`.
- `from vvaharness.util.counters import COUNTERS` at source line 32: `source_detail/vvaharness/util/counters.py.sudo.md`.
- `from vvaharness.util.json_extract import extract_json` at source line 33: `source_detail/vvaharness/util/json_extract.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../../prompt_representation/vvaharness/pipeline/stages/s6/outcomes.py.sudo.md). Exact strings in the evidence asset support this conversion.
