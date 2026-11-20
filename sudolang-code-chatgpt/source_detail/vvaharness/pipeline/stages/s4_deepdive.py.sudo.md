# vvaharness/pipeline/stages/s4_deepdive.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/pipeline/stages/s4_deepdive.py.evidence.json`. SHA-256: `663ce4ed01e701f3252a36e3bc9175846fb451648602e922a0e16257231aba46`.

```sudo
// Source: vvaharness/pipeline/stages/s4_deepdive.py:15-20
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import re; preserve alias and import-time effects. Then Resolve source import from concurrent.futures import ThreadPoolExecutor, as_completed; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s4_deepdive.py:22-28
In source order: Resolve source import from vvaharness.util import logs; preserve alias and import-time effects. Then Evaluate once logs.get_logger(__name__); assign in source target order to log. Then Resolve source import from vvaharness.backends.harness.models import is_halt_error; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm import cli; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm.cli import GuardrailBlocked; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s4_deepdive.py:29-33
In source order: Resolve source import from vvaharness.backends.llm.models import guardrail_gate_hit; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm.tools import sanitize_packed_text; preserve alias and import-time effects. Then Resolve source import from vvaharness.evidence import _cap_int; preserve alias and import-time effects. Then Resolve source import from vvaharness.models import ContextPackage, Finding, InvestigationUnit; preserve alias and import-time effects. Then Resolve source import from vvaharness.pipeline.stages.s4.batching import plan_batches; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s4_deepdive.py:34-38
In source order: Resolve source import from vvaharness.report.redact import _luhn, redact, redact_counts; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import console; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import errlog as _errlog; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.config import knob; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.counters import COUNTERS; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s4_deepdive.py:39-40
In source order: Resolve source import from vvaharness.util.response_quality import is_deterministic_failure; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.warn_once import warn_once; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s4_deepdive.py:43-362
// Source signature: run(units: list[InvestigationUnit], ctx: ContextPackage, cfg) -> tuple[list[Finding], dict[str, str]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn run(units, ctx, cfg) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s4_deepdive.py:45-49
  In source order: Retain source documentation literal source_literal_45_4; it is not a model call. Then Evaluate log.info('s4/deepdive: starting deep-dive analysis - units=%d', len(units)); retain side effects and discard the expression result. Then Evaluate once getattr(cfg, '_scan_progress', None); assign in source target order to tracker. Then Evaluate once Path(ctx.repo_root); assign in source target order to repo_root. Then Evaluate once sorted(units, key=lambda c: c.risk_rank); assign in source target order to units.
  // Source: vvaharness/pipeline/stages/s4_deepdive.py:50-54
  In source order: Evaluate once getattr(cfg.step4, 'parallel', 12); assign in source target order to parallel. Then Resolve source import from vvaharness.pipeline.stages.s4.session import deepdive_tools, investigate_unit; preserve alias and import-time effects. Then Evaluate deepdive_tools(cfg); retain side effects and discard the expression result. Then Evaluate once investigate_unit; assign in source target order to investigate.
  // Source: vvaharness/pipeline/stages/s4_deepdive.py:56-60
  // Source signature: _label(unit: InvestigationUnit) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _label(unit) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/pipeline/stages/s4_deepdive.py:57-60
    In source order: Evaluate once '+'.join(unit.languages[:3]) or 'generic'; assign in source target order to lens. Then Evaluate once unit.threat; assign in source target order to h. Then Evaluate console.write(source_template_59_22); retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/pipeline/stages/s4_deepdive.py:62-68
  In source order: Evaluate once 0; assign in source target order to guardrail_hits. Then Evaluate once max(3, parallel); assign in source target order to guardrail_gate. Then Evaluate once 0; assign in source target order to successes. Then For outcomes, assign {}; source annotation dict[str, str]. Then For non_empty_units, assign []; source annotation list[InvestigationUnit].
  // Source: vvaharness/pipeline/stages/s4_deepdive.py:69-81
  for each unit in units {
    // Source: vvaharness/pipeline/stages/s4_deepdive.py:70-72
    if (the source predicate unit.files is truthy) {
      // Source: vvaharness/pipeline/stages/s4_deepdive.py:71-71
      In source order: Evaluate non_empty_units.append(unit); retain side effects and discard the expression result.
      // Source: vvaharness/pipeline/stages/s4_deepdive.py:72-72
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/pipeline/stages/s4_deepdive.py:73-79
    In source order: Evaluate console.write(source_template_73_22); retain side effects and discard the expression result. Then Evaluate _errlog.log('s4', unit.id, 'unit carries no files after upstream normalisation; skipped before any model call', scope='unit', reason='empty_chunk_skipped'); retain side effects and discard the expression result. Then Evaluate once 'skipped'; assign in source target order to outcomes[unit.id].
    // Source: vvaharness/pipeline/stages/s4_deepdive.py:80-81
    if (the source predicate tracker is not None is truthy) {
      // Source: vvaharness/pipeline/stages/s4_deepdive.py:81-81
      In source order: Evaluate tracker.scanned(unit, outcome='skipped', n_findings=0); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/pipeline/stages/s4_deepdive.py:82-82
  In source order: Evaluate once non_empty_units; assign in source target order to units.
  // Source: vvaharness/pipeline/stages/s4_deepdive.py:86-91
  // Source signature: _guardrail_fail_fast(e: GuardrailBlocked) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _guardrail_fail_fast(e) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/pipeline/stages/s4_deepdive.py:87-91
    Raise RuntimeError(source_template_88_12) with explicit source cause e.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/pipeline/stages/s4_deepdive.py:93-152
  if (the source predicate parallel <= 1 is truthy) {
    // Source: vvaharness/pipeline/stages/s4_deepdive.py:94-94
    In source order: For all_findings, assign []; source annotation list[Finding].
    // Source: vvaharness/pipeline/stages/s4_deepdive.py:95-144
    for each (i, unit) in enumerate(units) {
      // Source: vvaharness/pipeline/stages/s4_deepdive.py:96-96
      In source order: Evaluate _label(unit); retain side effects and discard the expression result.
      // Source: vvaharness/pipeline/stages/s4_deepdive.py:97-98
      if (the source predicate tracker is not None is truthy) {
        // Source: vvaharness/pipeline/stages/s4_deepdive.py:98-98
        In source order: Evaluate tracker.scanning(unit); retain side effects and discard the expression result.
      }
      // Source: vvaharness/pipeline/stages/s4_deepdive.py:99-99
      In source order: For unit_stats, assign {}; source annotation dict.
      // Source: vvaharness/pipeline/stages/s4_deepdive.py:100-136
      Perform the following protected operations {
        // Source: vvaharness/pipeline/stages/s4_deepdive.py:101-101
        In source order: Evaluate once investigate(unit, ctx, repo_root, cfg, stats=unit_stats); assign in source target order to findings.
      }
      // Source: vvaharness/pipeline/stages/s4_deepdive.py:102-112
      On the first matching source exception GuardrailBlocked as e, in handler order {
        // Source: vvaharness/pipeline/stages/s4_deepdive.py:103-107
        In source order: Evaluate once guardrail_gate_hit(e, guardrail_hits, guardrail_gate); assign in source target order to (guardrail_hits, gate_label). Then Evaluate console.write(source_template_104_30); retain side effects and discard the expression result. Then Evaluate _errlog.log('s4', source_template_105_34, e, scope='unit', files=len(unit.files)); retain side effects and discard the expression result. Then Evaluate once 'guardrail'; assign in source target order to outcomes[unit.id].
        // Source: vvaharness/pipeline/stages/s4_deepdive.py:108-109
        if (the source predicate tracker is not None is truthy) {
          // Source: vvaharness/pipeline/stages/s4_deepdive.py:109-109
          In source order: Evaluate tracker.scanned(unit, outcome='guardrail', n_findings=0); retain side effects and discard the expression result.
        }
        // Source: vvaharness/pipeline/stages/s4_deepdive.py:110-111
        if (the source predicate guardrail_hits >= guardrail_gate and successes == 0 is truthy) {
          // Source: vvaharness/pipeline/stages/s4_deepdive.py:111-111
          In source order: Evaluate _guardrail_fail_fast(e); retain side effects and discard the expression result.
        }
        // Source: vvaharness/pipeline/stages/s4_deepdive.py:112-112
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/pipeline/stages/s4_deepdive.py:113-136
      On the first matching source exception Exception as e, in handler order {
        // Source: vvaharness/pipeline/stages/s4_deepdive.py:114-115
        if (the source predicate cli.aborted() is truthy) {
          // Source: vvaharness/pipeline/stages/s4_deepdive.py:115-115
          Raise the currently handled exception.
        }
        // Source: vvaharness/pipeline/stages/s4_deepdive.py:116-128
        if (the source predicate is_halt_error(e) is truthy) {
          // Source: vvaharness/pipeline/stages/s4_deepdive.py:118-123
          In source order: Evaluate once units[i:]; assign in source target order to remaining. Then Evaluate console.write(source_template_119_34); retain side effects and discard the expression result. Then Evaluate _errlog.log('s4', unit.id, e, scope='unit', files=len(unit.files)); retain side effects and discard the expression result. Then Evaluate COUNTERS.bump('s4_units_halted', len(remaining)); retain side effects and discard the expression result.
          // Source: vvaharness/pipeline/stages/s4_deepdive.py:124-127
          for each skipped in remaining {
            // Source: vvaharness/pipeline/stages/s4_deepdive.py:125-125
            In source order: Evaluate once 'halted'; assign in source target order to outcomes[skipped.id].
            // Source: vvaharness/pipeline/stages/s4_deepdive.py:126-127
            if (the source predicate tracker is not None is truthy) {
              // Source: vvaharness/pipeline/stages/s4_deepdive.py:127-127
              In source order: Evaluate tracker.scanned(skipped, outcome='halted', n_findings=0); retain side effects and discard the expression result.
            }
          }
          // Source: vvaharness/pipeline/stages/s4_deepdive.py:128-128
          Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
        }
        // Source: vvaharness/pipeline/stages/s4_deepdive.py:130-133
        In source order: Evaluate console.write(source_template_130_30); retain side effects and discard the expression result. Then Evaluate _errlog.log('s4', unit.id, e, scope='unit', files=len(unit.files)); retain side effects and discard the expression result. Then Evaluate once 'error'; assign in source target order to outcomes[unit.id].
        // Source: vvaharness/pipeline/stages/s4_deepdive.py:134-135
        if (the source predicate tracker is not None is truthy) {
          // Source: vvaharness/pipeline/stages/s4_deepdive.py:135-135
          In source order: Evaluate tracker.scanned(unit, outcome='error', n_findings=0); retain side effects and discard the expression result.
        }
        // Source: vvaharness/pipeline/stages/s4_deepdive.py:136-136
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/pipeline/stages/s4_deepdive.py:137-139
      In source order: Apply source augmented assignment successes += 1 with source evaluation/in-place semantics. Then Evaluate once 'completed'; assign in source target order to outcomes[unit.id]. Then Evaluate all_findings.extend(findings); retain side effects and discard the expression result.
      // Source: vvaharness/pipeline/stages/s4_deepdive.py:140-141
      if (the source predicate tracker is not None is truthy) {
        // Source: vvaharness/pipeline/stages/s4_deepdive.py:141-141
        In source order: Evaluate tracker.scanned(unit, outcome='completed', n_findings=len(findings)); retain side effects and discard the expression result.
      }
      // Source: vvaharness/pipeline/stages/s4_deepdive.py:142-144
      In source order: Evaluate once unit_stats.get('merged', 0); assign in source target order to merged. Then Evaluate once source_template_143_21 if merged else ''; assign in source target order to suffix. Then Evaluate console.write(source_template_144_26); retain side effects and discard the expression result.
    }
    // Source: vvaharness/pipeline/stages/s4_deepdive.py:145-149
    In source order: Evaluate once sum((1 for v in outcomes.values() if v == 'error')); assign in source target order to error_count. Then Evaluate once sum((1 for v in outcomes.values() if v == 'guardrail')); assign in source target order to guardrail_count. Then Evaluate once sum((1 for v in outcomes.values() if v == 'halted')); assign in source target order to halted_count. Then Evaluate log.info('s4/deepdive: serial processing complete - units=%d findings=%d errors=%d guardrails=%d halted=%d', len(units), len(all_findings), error_count, guardrail_count, halted_count); retain side effects and discard the expression result.
    // Source: vvaharness/pipeline/stages/s4_deepdive.py:150-151
    if (the source predicate tracker is not None is truthy) {
      // Source: vvaharness/pipeline/stages/s4_deepdive.py:151-151
      In source order: Evaluate tracker.print_summary(); retain side effects and discard the expression result.
    }
    // Source: vvaharness/pipeline/stages/s4_deepdive.py:152-152
    End this invocation with (all_findings, outcomes).
  }
  // Source: vvaharness/pipeline/stages/s4_deepdive.py:154-157
  In source order: Evaluate console.write(source_template_154_18); retain side effects and discard the expression result. Then For results, assign {}; source annotation dict[str, list[Finding]]. Then Evaluate once plan_batches(units, _batch_size(cfg)); assign in source target order to batches. Then Evaluate once bool(knob(cfg, 'step4.split_retry', True)); assign in source target order to split_retry.
  // Source: vvaharness/pipeline/stages/s4_deepdive.py:158-159
  if (the source predicate any((len(b) > 1 for b in batches)) is truthy) {
    // Source: vvaharness/pipeline/stages/s4_deepdive.py:159-159
    In source order: Evaluate console.write(source_template_159_22); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s4_deepdive.py:160-162
  In source order: Evaluate once ThreadPoolExecutor(max_workers=parallel); assign in source target order to ex. Then Evaluate once {}; assign in source target order to futs. Then For retry_futs, assign {}; source annotation dict.
  // Source: vvaharness/pipeline/stages/s4_deepdive.py:164-168
  // Source signature: _resubmit(unit: InvestigationUnit) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _resubmit(unit) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/pipeline/stages/s4_deepdive.py:165-168
    In source order: Evaluate once _submit_batch(ex, [unit], investigate, ctx, repo_root, cfg); assign in source target order to fut. Then Evaluate once [unit]; assign in source target order to futs[fut]. Then Evaluate once [unit]; assign in source target order to retry_futs[fut]. Then Evaluate COUNTERS.bump('s4_batch_member_resubmitted'); retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/pipeline/stages/s4_deepdive.py:170-183
  // Source signature: _mark_halted(batches_to_mark: list[list[InvestigationUnit]]) -> int
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _mark_halted(batches_to_mark) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/pipeline/stages/s4_deepdive.py:171-173
    In source order: Retain source documentation literal source_literal_171_8; it is not a model call. Then Evaluate once 0; assign in source target order to n.
    // Source: vvaharness/pipeline/stages/s4_deepdive.py:174-182
    for each b in batches_to_mark {
      // Source: vvaharness/pipeline/stages/s4_deepdive.py:175-182
      for each unit in b {
        // Source: vvaharness/pipeline/stages/s4_deepdive.py:176-177
        if (the source predicate unit.id in outcomes is truthy) {
          // Source: vvaharness/pipeline/stages/s4_deepdive.py:177-177
          Continue the immediately enclosing source loop at its next iteration.
        }
        // Source: vvaharness/pipeline/stages/s4_deepdive.py:178-180
        In source order: Evaluate once 'halted'; assign in source target order to outcomes[unit.id]. Then Evaluate once []; assign in source target order to results[unit.id]. Then Apply source augmented assignment n += 1 with source evaluation/in-place semantics.
        // Source: vvaharness/pipeline/stages/s4_deepdive.py:181-182
        if (the source predicate tracker is not None is truthy) {
          // Source: vvaharness/pipeline/stages/s4_deepdive.py:182-182
          In source order: Evaluate tracker.scanned(unit, outcome='halted', n_findings=0); retain side effects and discard the expression result.
        }
      }
    }
    // Source: vvaharness/pipeline/stages/s4_deepdive.py:183-183
    End this invocation with n.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/pipeline/stages/s4_deepdive.py:185-190
  for each batch in batches {
    // Source: vvaharness/pipeline/stages/s4_deepdive.py:186-189
    for each unit in batch {
      // Source: vvaharness/pipeline/stages/s4_deepdive.py:187-187
      In source order: Evaluate _label(unit); retain side effects and discard the expression result.
      // Source: vvaharness/pipeline/stages/s4_deepdive.py:188-189
      if (the source predicate tracker is not None is truthy) {
        // Source: vvaharness/pipeline/stages/s4_deepdive.py:189-189
        In source order: Evaluate tracker.scanning(unit); retain side effects and discard the expression result.
      }
    }
    // Source: vvaharness/pipeline/stages/s4_deepdive.py:190-190
    In source order: Evaluate once batch; assign in source target order to futs[_submit_batch(ex, batch, investigate, ctx, repo_root, cfg)].
  }
  // Source: vvaharness/pipeline/stages/s4_deepdive.py:191-191
  In source order: Evaluate once False; assign in source target order to halted.
  // Source: vvaharness/pipeline/stages/s4_deepdive.py:192-344
  Perform the following protected operations {
    // Source: vvaharness/pipeline/stages/s4_deepdive.py:193-279
    for each fut in as_completed(futs) {
      // Source: vvaharness/pipeline/stages/s4_deepdive.py:194-194
      In source order: Evaluate once futs[fut]; assign in source target order to batch.
      // Source: vvaharness/pipeline/stages/s4_deepdive.py:195-245
      Perform the following protected operations {
        // Source: vvaharness/pipeline/stages/s4_deepdive.py:196-196
        In source order: Evaluate once fut.result(); assign in source target order to (found, merged_by_unit, verdict_by_unit).
      }
      // Source: vvaharness/pipeline/stages/s4_deepdive.py:197-211
      On the first matching source exception GuardrailBlocked as e, in handler order {
        // Source: vvaharness/pipeline/stages/s4_deepdive.py:198-198
        In source order: Evaluate once guardrail_gate_hit(e, guardrail_hits, guardrail_gate); assign in source target order to (guardrail_hits, gate_label).
        // Source: vvaharness/pipeline/stages/s4_deepdive.py:199-206
        for each unit in batch {
          // Source: vvaharness/pipeline/stages/s4_deepdive.py:200-204
          In source order: Evaluate console.write(source_template_200_34); retain side effects and discard the expression result. Then Evaluate _errlog.log('s4', source_template_201_38, e, scope='unit', files=len(unit.files)); retain side effects and discard the expression result. Then Evaluate once []; assign in source target order to results[unit.id]. Then Evaluate once 'guardrail'; assign in source target order to outcomes[unit.id].
          // Source: vvaharness/pipeline/stages/s4_deepdive.py:205-206
          if (the source predicate tracker is not None is truthy) {
            // Source: vvaharness/pipeline/stages/s4_deepdive.py:206-206
            In source order: Evaluate tracker.scanned(unit, outcome='guardrail', n_findings=0); retain side effects and discard the expression result.
          }
        }
        // Source: vvaharness/pipeline/stages/s4_deepdive.py:207-210
        if (the source predicate guardrail_hits >= guardrail_gate and successes == 0 is truthy) {
          // Source: vvaharness/pipeline/stages/s4_deepdive.py:208-210
          In source order: Evaluate cli.abort(); retain side effects and discard the expression result. Then Evaluate ex.shutdown(wait=False, cancel_futures=True); retain side effects and discard the expression result. Then Evaluate _guardrail_fail_fast(e); retain side effects and discard the expression result.
        }
        // Source: vvaharness/pipeline/stages/s4_deepdive.py:211-211
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/pipeline/stages/s4_deepdive.py:212-245
      On the first matching source exception Exception as e, in handler order {
        // Source: vvaharness/pipeline/stages/s4_deepdive.py:213-227
        if (the source predicate is_halt_error(e) is truthy) {
          // Source: vvaharness/pipeline/stages/s4_deepdive.py:215-220
          In source order: Evaluate once [b for f, b in futs.items() if not f.done()]; assign in source target order to pending_batches. Then Evaluate once sum((len(b) for b in pending_batches)); assign in source target order to n_pending. Then Evaluate _mark_halted([batch, *pending_batches]); retain side effects and discard the expression result. Then Evaluate console.write(source_template_218_34); retain side effects and discard the expression result.
          // Source: vvaharness/pipeline/stages/s4_deepdive.py:221-222
          for each unit in batch {
            // Source: vvaharness/pipeline/stages/s4_deepdive.py:222-222
            In source order: Evaluate _errlog.log('s4', unit.id, e, scope='unit', files=len(unit.files)); retain side effects and discard the expression result.
          }
          // Source: vvaharness/pipeline/stages/s4_deepdive.py:223-226
          In source order: Evaluate COUNTERS.bump('s4_units_halted', len(batch) + n_pending); retain side effects and discard the expression result. Then Evaluate cli.abort(); retain side effects and discard the expression result. Then Evaluate ex.shutdown(wait=False, cancel_futures=True); retain side effects and discard the expression result. Then Evaluate once True; assign in source target order to halted.
          // Source: vvaharness/pipeline/stages/s4_deepdive.py:227-227
          Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
        }
        // Source: vvaharness/pipeline/stages/s4_deepdive.py:228-229
        In source order: Evaluate once split_retry and len(batch) > 1 and (not is_deterministic_failure(e)) and (not cli.aborted()); assign in source target order to retryable.
        // Source: vvaharness/pipeline/stages/s4_deepdive.py:230-244
        for each unit in batch {
          // Source: vvaharness/pipeline/stages/s4_deepdive.py:231-231
          In source order: Evaluate once 'error'; assign in source target order to outcomes[unit.id].
          // Source: vvaharness/pipeline/stages/s4_deepdive.py:232-238
          if (the source predicate retryable is truthy) {
            // Source: vvaharness/pipeline/stages/s4_deepdive.py:233-237
            In source order: Evaluate console.write(source_template_233_38); retain side effects and discard the expression result. Then Evaluate _errlog.log('s4', unit.id, e, scope='unit', files=len(unit.files), recovered=True); retain side effects and discard the expression result. Then Evaluate _resubmit(unit); retain side effects and discard the expression result.
            // Source: vvaharness/pipeline/stages/s4_deepdive.py:238-238
            Continue the immediately enclosing source loop at its next iteration.
          }
          // Source: vvaharness/pipeline/stages/s4_deepdive.py:239-242
          In source order: Evaluate console.write(source_template_239_34); retain side effects and discard the expression result. Then Evaluate _errlog.log('s4', unit.id, e, scope='unit', files=len(unit.files)); retain side effects and discard the expression result. Then Evaluate once []; assign in source target order to results[unit.id].
          // Source: vvaharness/pipeline/stages/s4_deepdive.py:243-244
          if (the source predicate tracker is not None is truthy) {
            // Source: vvaharness/pipeline/stages/s4_deepdive.py:244-244
            In source order: Evaluate tracker.scanned(unit, outcome='error', n_findings=0); retain side effects and discard the expression result.
          }
        }
        // Source: vvaharness/pipeline/stages/s4_deepdive.py:245-245
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/pipeline/stages/s4_deepdive.py:246-246
      In source order: Apply source augmented assignment successes += 1 with source evaluation/in-place semantics.
      // Source: vvaharness/pipeline/stages/s4_deepdive.py:247-279
      for each unit in batch {
        // Source: vvaharness/pipeline/stages/s4_deepdive.py:248-249
        In source order: Evaluate once found.get(unit.id, []); assign in source target order to findings. Then Evaluate once verdict_by_unit.get(unit.id); assign in source target order to verdict.
        // Source: vvaharness/pipeline/stages/s4_deepdive.py:250-272
        if (the source predicate verdict in ('uninvestigated', 'failed') is truthy) {
          // Source: vvaharness/pipeline/stages/s4_deepdive.py:251-255
          In source order: Evaluate once verdict; assign in source target order to outcomes[unit.id]. Then Evaluate once split_retry and len(batch) > 1 and (not cli.aborted()); assign in source target order to retryable. Then Evaluate once 'model omitted this unit from the shared batch reply' if verdict == 'uninvestigated' else "this unit's entry in the shared batch reply did not parse"; assign in source target order to msg.
          // Source: vvaharness/pipeline/stages/s4_deepdive.py:256-263
          if (the source predicate retryable is truthy) {
            // Source: vvaharness/pipeline/stages/s4_deepdive.py:257-262
            In source order: Evaluate console.write(source_template_257_38); retain side effects and discard the expression result. Then Evaluate _errlog.log('s4', unit.id, msg, scope='unit', files=len(unit.files), recovered=True); retain side effects and discard the expression result. Then Evaluate _resubmit(unit); retain side effects and discard the expression result.
            // Source: vvaharness/pipeline/stages/s4_deepdive.py:263-263
            Continue the immediately enclosing source loop at its next iteration.
          }
          // Source: vvaharness/pipeline/stages/s4_deepdive.py:264-269
          In source order: Evaluate _errlog.log('s4', unit.id, msg, scope='unit', files=len(unit.files), reason=source_template_266_39); retain side effects and discard the expression result. Then Evaluate console.write(source_template_267_34); retain side effects and discard the expression result. Then Evaluate once []; assign in source target order to results[unit.id].
          // Source: vvaharness/pipeline/stages/s4_deepdive.py:270-271
          if (the source predicate tracker is not None is truthy) {
            // Source: vvaharness/pipeline/stages/s4_deepdive.py:271-271
            In source order: Evaluate tracker.scanned(unit, outcome=verdict, n_findings=0); retain side effects and discard the expression result.
          }
          // Source: vvaharness/pipeline/stages/s4_deepdive.py:272-272
          Continue the immediately enclosing source loop at its next iteration.
        }
        // Source: vvaharness/pipeline/stages/s4_deepdive.py:273-274
        In source order: Evaluate once findings; assign in source target order to results[unit.id]. Then Evaluate once 'completed'; assign in source target order to outcomes[unit.id].
        // Source: vvaharness/pipeline/stages/s4_deepdive.py:275-276
        if (the source predicate tracker is not None is truthy) {
          // Source: vvaharness/pipeline/stages/s4_deepdive.py:276-276
          In source order: Evaluate tracker.scanned(unit, outcome='completed', n_findings=len(findings)); retain side effects and discard the expression result.
        }
        // Source: vvaharness/pipeline/stages/s4_deepdive.py:277-279
        In source order: Evaluate once merged_by_unit.get(unit.id, 0); assign in source target order to merged. Then Evaluate once source_template_278_25 if merged else ''; assign in source target order to suffix. Then Evaluate console.write(source_template_279_30); retain side effects and discard the expression result.
      }
    }
    // Source: vvaharness/pipeline/stages/s4_deepdive.py:282-336
    for each fut in as_completed(retry_futs) if not halted else () {
      // Source: vvaharness/pipeline/stages/s4_deepdive.py:283-283
      In source order: Evaluate once retry_futs[fut]; assign in source target order to batch.
      // Source: vvaharness/pipeline/stages/s4_deepdive.py:284-325
      Perform the following protected operations {
        // Source: vvaharness/pipeline/stages/s4_deepdive.py:285-285
        In source order: Evaluate once fut.result(); assign in source target order to (found, merged_by_unit, verdict_by_unit).
      }
      // Source: vvaharness/pipeline/stages/s4_deepdive.py:286-300
      On the first matching source exception GuardrailBlocked as e, in handler order {
        // Source: vvaharness/pipeline/stages/s4_deepdive.py:287-287
        In source order: Evaluate once guardrail_gate_hit(e, guardrail_hits, guardrail_gate); assign in source target order to (guardrail_hits, gate_label).
        // Source: vvaharness/pipeline/stages/s4_deepdive.py:288-295
        for each unit in batch {
          // Source: vvaharness/pipeline/stages/s4_deepdive.py:289-293
          In source order: Evaluate console.write(source_template_289_34); retain side effects and discard the expression result. Then Evaluate _errlog.log('s4', source_template_290_38, e, scope='unit', files=len(unit.files)); retain side effects and discard the expression result. Then Evaluate once []; assign in source target order to results[unit.id]. Then Evaluate once 'guardrail'; assign in source target order to outcomes[unit.id].
          // Source: vvaharness/pipeline/stages/s4_deepdive.py:294-295
          if (the source predicate tracker is not None is truthy) {
            // Source: vvaharness/pipeline/stages/s4_deepdive.py:295-295
            In source order: Evaluate tracker.scanned(unit, outcome='guardrail', n_findings=0); retain side effects and discard the expression result.
          }
        }
        // Source: vvaharness/pipeline/stages/s4_deepdive.py:296-299
        if (the source predicate guardrail_hits >= guardrail_gate and successes == 0 is truthy) {
          // Source: vvaharness/pipeline/stages/s4_deepdive.py:297-299
          In source order: Evaluate cli.abort(); retain side effects and discard the expression result. Then Evaluate ex.shutdown(wait=False, cancel_futures=True); retain side effects and discard the expression result. Then Evaluate _guardrail_fail_fast(e); retain side effects and discard the expression result.
        }
        // Source: vvaharness/pipeline/stages/s4_deepdive.py:300-300
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/pipeline/stages/s4_deepdive.py:301-325
      On the first matching source exception Exception as e, in handler order {
        // Source: vvaharness/pipeline/stages/s4_deepdive.py:302-316
        if (the source predicate is_halt_error(e) is truthy) {
          // Source: vvaharness/pipeline/stages/s4_deepdive.py:303-309
          In source order: Evaluate once [b for f, b in futs.items() if not f.done()] + [b for f, b in retry_futs.items() if not f.done()]; assign in source target order to pending_batches. Then Evaluate once sum((len(b) for b in pending_batches)); assign in source target order to n_pending. Then Evaluate _mark_halted([batch, *pending_batches]); retain side effects and discard the expression result. Then Evaluate console.write(source_template_307_34); retain side effects and discard the expression result.
          // Source: vvaharness/pipeline/stages/s4_deepdive.py:310-311
          for each unit in batch {
            // Source: vvaharness/pipeline/stages/s4_deepdive.py:311-311
            In source order: Evaluate _errlog.log('s4', unit.id, e, scope='unit', files=len(unit.files)); retain side effects and discard the expression result.
          }
          // Source: vvaharness/pipeline/stages/s4_deepdive.py:312-315
          In source order: Evaluate COUNTERS.bump('s4_units_halted', len(batch) + n_pending); retain side effects and discard the expression result. Then Evaluate cli.abort(); retain side effects and discard the expression result. Then Evaluate ex.shutdown(wait=False, cancel_futures=True); retain side effects and discard the expression result. Then Evaluate once True; assign in source target order to halted.
          // Source: vvaharness/pipeline/stages/s4_deepdive.py:316-316
          Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
        }
        // Source: vvaharness/pipeline/stages/s4_deepdive.py:317-324
        for each unit in batch {
          // Source: vvaharness/pipeline/stages/s4_deepdive.py:318-322
          In source order: Evaluate console.write(source_template_318_34); retain side effects and discard the expression result. Then Evaluate _errlog.log('s4', unit.id, e, scope='unit', files=len(unit.files)); retain side effects and discard the expression result. Then Evaluate once []; assign in source target order to results[unit.id]. Then Evaluate once 'error'; assign in source target order to outcomes[unit.id].
          // Source: vvaharness/pipeline/stages/s4_deepdive.py:323-324
          if (the source predicate tracker is not None is truthy) {
            // Source: vvaharness/pipeline/stages/s4_deepdive.py:324-324
            In source order: Evaluate tracker.scanned(unit, outcome='error', n_findings=0); retain side effects and discard the expression result.
          }
        }
        // Source: vvaharness/pipeline/stages/s4_deepdive.py:325-325
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/pipeline/stages/s4_deepdive.py:326-326
      In source order: Apply source augmented assignment successes += 1 with source evaluation/in-place semantics.
      // Source: vvaharness/pipeline/stages/s4_deepdive.py:327-336
      for each unit in batch {
        // Source: vvaharness/pipeline/stages/s4_deepdive.py:328-331
        In source order: Evaluate once found.get(unit.id, []); assign in source target order to findings. Then Evaluate once findings; assign in source target order to results[unit.id]. Then Evaluate once 'completed'; assign in source target order to outcomes[unit.id]. Then Evaluate COUNTERS.bump('s4_batch_member_recovered'); retain side effects and discard the expression result.
        // Source: vvaharness/pipeline/stages/s4_deepdive.py:332-333
        if (the source predicate tracker is not None is truthy) {
          // Source: vvaharness/pipeline/stages/s4_deepdive.py:333-333
          In source order: Evaluate tracker.scanned(unit, outcome='completed', n_findings=len(findings)); retain side effects and discard the expression result.
        }
        // Source: vvaharness/pipeline/stages/s4_deepdive.py:334-336
        In source order: Evaluate once merged_by_unit.get(unit.id, 0); assign in source target order to merged. Then Evaluate once source_template_335_25 if merged else ''; assign in source target order to suffix. Then Evaluate console.write(source_template_336_30); retain side effects and discard the expression result.
      }
    }
  }
  // Source: vvaharness/pipeline/stages/s4_deepdive.py:337-342
  On the first matching source exception (KeyboardInterrupt, SystemExit), in handler order {
    // Source: vvaharness/pipeline/stages/s4_deepdive.py:338-341
    In source order: Evaluate once cli.abort(); assign in source target order to n. Then Evaluate console.write(source_template_339_22); retain side effects and discard the expression result. Then Evaluate ex.shutdown(wait=False, cancel_futures=True); retain side effects and discard the expression result.
    // Source: vvaharness/pipeline/stages/s4_deepdive.py:342-342
    Raise the currently handled exception.
  }
  On every exit from this protected/handler/normal-completion region {
    // Source: vvaharness/pipeline/stages/s4_deepdive.py:344-344
    In source order: Evaluate ex.shutdown(wait=True); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s4_deepdive.py:347-347
  In source order: For all_findings, assign []; source annotation list[Finding].
  // Source: vvaharness/pipeline/stages/s4_deepdive.py:348-349
  for each unit in units {
    // Source: vvaharness/pipeline/stages/s4_deepdive.py:349-349
    In source order: Evaluate all_findings.extend(results.get(unit.id, [])); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s4_deepdive.py:350-354
  In source order: Evaluate once sum((1 for v in outcomes.values() if v == 'completed')); assign in source target order to completed_count. Then Evaluate once sum((1 for v in outcomes.values() if v == 'error')); assign in source target order to error_count. Then Evaluate once sum((1 for v in outcomes.values() if v == 'guardrail')); assign in source target order to guardrail_count. Then Evaluate once sum((1 for v in outcomes.values() if v == 'uninvestigated')); assign in source target order to uninvestigated_count. Then Evaluate once sum((1 for v in outcomes.values() if v == 'failed')); assign in source target order to failed_count.
  // Source: vvaharness/pipeline/stages/s4_deepdive.py:355-359
  In source order: Evaluate once sum((1 for v in outcomes.values() if v == 'halted')); assign in source target order to halted_count. Then Evaluate log.info(source_literal_356_13, len(units), completed_count, error_count, guardrail_count, uninvestigated_count, failed_count, halted_count, len(all_findings)); retain side effects and discard the expression result.
  // Source: vvaharness/pipeline/stages/s4_deepdive.py:360-361
  if (the source predicate tracker is not None is truthy) {
    // Source: vvaharness/pipeline/stages/s4_deepdive.py:361-361
    In source order: Evaluate tracker.print_summary(); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s4_deepdive.py:362-362
  End this invocation with (all_findings, outcomes).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s4_deepdive.py:365-367
// Source signature: _batch_size(cfg) -> int
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _batch_size(cfg) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s4_deepdive.py:366-366
  In source order: Retain source documentation literal source_literal_366_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s4_deepdive.py:367-367
  End this invocation with _cap_int(cfg.step4, 'batch_size', 1).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s4_deepdive.py:370-390
// Source signature: _submit_batch(ex: ThreadPoolExecutor, batch: list[InvestigationUnit], investigate, ctx: ContextPackage, repo_root: Path, cfg)
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _submit_batch(ex, batch, investigate, ctx, repo_root, cfg) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s4_deepdive.py:372-375
  In source order: Retain source documentation literal source_literal_372_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s4_deepdive.py:376-382
  if (the source predicate len(batch) == 1 is truthy) {
    // Source: vvaharness/pipeline/stages/s4_deepdive.py:377-377
    In source order: Evaluate once batch[0]; assign in source target order to unit.
    // Source: vvaharness/pipeline/stages/s4_deepdive.py:378-381
    // Source signature: _run_one()
    Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
    fn _run_one() {
      Bind arguments/defaults/annotations exactly as the source signature specifies.
      // Source: vvaharness/pipeline/stages/s4_deepdive.py:379-380
      In source order: For stats, assign {}; source annotation dict. Then Evaluate once investigate(unit, ctx, repo_root, cfg, stats=stats); assign in source target order to findings.
      // Source: vvaharness/pipeline/stages/s4_deepdive.py:381-381
      End this invocation with ({unit.id: findings}, {unit.id: stats.get('merged', 0)}, {}).
      If execution reaches this end, finish with the source implicit None result.
    }
    // Source: vvaharness/pipeline/stages/s4_deepdive.py:382-382
    End this invocation with ex.submit(_run_one).
  }
  // Source: vvaharness/pipeline/stages/s4_deepdive.py:385-385
  In source order: Resolve source import from vvaharness.pipeline.stages.s4.session import investigate_batch; preserve alias and import-time effects.
  // Source: vvaharness/pipeline/stages/s4_deepdive.py:386-389
  // Source signature: _run_batch()
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _run_batch() {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/pipeline/stages/s4_deepdive.py:387-388
    In source order: For stats, assign {}; source annotation dict. Then Evaluate once investigate_batch(batch, ctx, repo_root, cfg, stats=stats); assign in source target order to (out, verdict_by_unit).
    // Source: vvaharness/pipeline/stages/s4_deepdive.py:389-389
    End this invocation with (out, stats.get('merged_by_unit', {}), verdict_by_unit).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/pipeline/stages/s4_deepdive.py:390-390
  End this invocation with ex.submit(_run_batch).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s4_deepdive.py:394-398
In source order: Evaluate once 4000; assign in source target order to _SHARED_CTX_MAX_SYSTEM_CHARS. Then Evaluate once 25; assign in source target order to _SHARED_CTX_MAX_THREATS. Then Evaluate once 15; assign in source target order to _SHARED_CTX_MAX_BOUNDARIES. Then Evaluate once 10; assign in source target order to _SHARED_CTX_MAX_ASSETS. Then Evaluate once 60; assign in source target order to _SHARED_CTX_MAX_EPS.
// Source: vvaharness/pipeline/stages/s4_deepdive.py:401-440
// Source signature: _build_shared_context_block(ctx: ContextPackage) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _build_shared_context_block(ctx) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s4_deepdive.py:402-403
  In source order: Retain source documentation literal source_literal_402_4; it is not a model call. Then For parts, assign []; source annotation list[str].
  // Source: vvaharness/pipeline/stages/s4_deepdive.py:405-406
  if (the source predicate ctx.app_profile is truthy) {
    // Source: vvaharness/pipeline/stages/s4_deepdive.py:406-406
    In source order: Evaluate parts.append(ctx.app_profile.to_prompt_block()); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s4_deepdive.py:408-414
  if (the source predicate ctx.threat_model is truthy) {
    // Source: vvaharness/pipeline/stages/s4_deepdive.py:409-414
    In source order: Evaluate parts.append(ctx.threat_model.to_compact_prompt_block(max_context_chars=_SHARED_CTX_MAX_SYSTEM_CHARS, max_assets=_SHARED_CTX_MAX_ASSETS, max_boundaries=_SHARED_CTX_MAX_BOUNDARIES, max_threats=_SHARED_CTX_MAX_THREATS)); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s4_deepdive.py:417-430
  if (the source predicate ctx.entry_points is truthy) {
    // Source: vvaharness/pipeline/stages/s4_deepdive.py:418-422
    In source order: Evaluate once sorted(ctx.entry_points, key=lambda e: (e.file, e.function))[:_SHARED_CTX_MAX_EPS]; assign in source target order to eps. Then Evaluate once [source_template_421_12]; assign in source target order to ep_lines.
    // Source: vvaharness/pipeline/stages/s4_deepdive.py:423-425
    for each ep in eps {
      // Source: vvaharness/pipeline/stages/s4_deepdive.py:424-425
      In source order: Evaluate once '[unauth]' if ep.reachable_from_unauth else '[auth]'; assign in source target order to auth_tag. Then Evaluate ep_lines.append(source_template_425_28); retain side effects and discard the expression result.
    }
    // Source: vvaharness/pipeline/stages/s4_deepdive.py:426-429
    if (the source predicate len(ctx.entry_points) > _SHARED_CTX_MAX_EPS is truthy) {
      // Source: vvaharness/pipeline/stages/s4_deepdive.py:427-429
      In source order: Evaluate ep_lines.append(source_template_428_16); retain side effects and discard the expression result.
    }
    // Source: vvaharness/pipeline/stages/s4_deepdive.py:430-430
    In source order: Evaluate parts.append(source_literal_430_21.join(ep_lines)); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s4_deepdive.py:432-438
  In source order: Evaluate parts.append(source_literal_433_8); retain side effects and discard the expression result.
  // Source: vvaharness/pipeline/stages/s4_deepdive.py:440-440
  End this invocation with source_literal_440_11.join((p for p in parts if p)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s4_deepdive.py:445-451
In source order: Evaluate once re.compile('\\b(?:\\d[\\s\\-]?){13,19}\\b'); assign in source target order to _PAN_RX. Then Evaluate once re.compile(source_literal_449_4); assign in source target order to _CARD_CTX.
// Source: vvaharness/pipeline/stages/s4_deepdive.py:454-471
// Source signature: _mask_pan(m: re.Match) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _mask_pan(m) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s4_deepdive.py:455-456
  In source order: Evaluate once m.group(0); assign in source target order to s. Then Evaluate once re.sub('\\D', '', s); assign in source target order to digits.
  // Source: vvaharness/pipeline/stages/s4_deepdive.py:457-458
  if (the source predicate len(digits) < 13 is truthy) {
    // Source: vvaharness/pipeline/stages/s4_deepdive.py:458-458
    End this invocation with s.
  }
  // Source: vvaharness/pipeline/stages/s4_deepdive.py:460-460
  In source order: Evaluate once m.string[max(0, m.start() - 48):m.start()]; assign in source target order to window.
  // Source: vvaharness/pipeline/stages/s4_deepdive.py:461-462
  if (the source predicate not (_luhn(digits) or _CARD_CTX.search(window)) is truthy) {
    // Source: vvaharness/pipeline/stages/s4_deepdive.py:462-462
    End this invocation with s.
  }
  // Source: vvaharness/pipeline/stages/s4_deepdive.py:463-464
  In source order: Evaluate once 0; assign in source target order to kept. Then Evaluate once []; assign in source target order to out.
  // Source: vvaharness/pipeline/stages/s4_deepdive.py:465-470
  for each c in s {
    // Source: vvaharness/pipeline/stages/s4_deepdive.py:466-470
    if (the source predicate c.isdigit() is truthy) {
      // Source: vvaharness/pipeline/stages/s4_deepdive.py:467-468
      In source order: Evaluate out.append(c if kept < 4 else 'X'); retain side effects and discard the expression result. Then Apply source augmented assignment kept += 1 with source evaluation/in-place semantics.
    }
    else {
      // Source: vvaharness/pipeline/stages/s4_deepdive.py:470-470
      In source order: Evaluate out.append(c); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/pipeline/stages/s4_deepdive.py:471-471
  End this invocation with ''.join(out).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s4_deepdive.py:475-475
In source order: For _WARNED_REDACTED_SOURCE, assign set(); source annotation set[str].
// Source: vvaharness/pipeline/stages/s4_deepdive.py:478-501
// Source signature: _redact_source(text: str, rel: str, *, stage: str='s4') -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _redact_source(text, rel, stage) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s4_deepdive.py:479-483
  In source order: Retain source documentation literal source_literal_479_4; it is not a model call. Then Evaluate once sanitize_packed_text(text, rel); assign in source target order to text. Then Evaluate once 0; assign in source target order to n_pan.
  // Source: vvaharness/pipeline/stages/s4_deepdive.py:484-489
  // Source signature: _count_mask(m: re.Match) -> str
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _count_mask(m) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/pipeline/stages/s4_deepdive.py:485-486
    In source order: Bind names in enclosing nonlocal scope: n_pan. Then Evaluate once _mask_pan(m); assign in source target order to repl.
    // Source: vvaharness/pipeline/stages/s4_deepdive.py:487-488
    if (the source predicate repl != m.group(0) is truthy) {
      // Source: vvaharness/pipeline/stages/s4_deepdive.py:488-488
      In source order: Apply source augmented assignment n_pan += 1 with source evaluation/in-place semantics.
    }
    // Source: vvaharness/pipeline/stages/s4_deepdive.py:489-489
    End this invocation with repl.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/pipeline/stages/s4_deepdive.py:491-494
  In source order: Evaluate once _PAN_RX.sub(_count_mask, text); assign in source target order to masked. Then Evaluate once redact_counts(masked); assign in source target order to (masked, counts). Then Evaluate once sum(counts.values()); assign in source target order to n_other.
  // Source: vvaharness/pipeline/stages/s4_deepdive.py:495-500
  if (the source predicate n_pan or n_other is truthy) {
    // Source: vvaharness/pipeline/stages/s4_deepdive.py:496-500
    In source order: Evaluate once ' [' + ', '.join((source_template_496_35 for k, v in sorted(counts.items()))) + ']' if counts else ''; assign in source target order to detail. Then Evaluate warn_once(_WARNED_REDACTED_SOURCE, source_template_498_43, source_template_499_18); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s4_deepdive.py:501-501
  End this invocation with masked.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s4_deepdive.py:505-505
In source order: Evaluate once 8000; assign in source target order to MAX_LINE_CHARS.
// Source: vvaharness/pipeline/stages/s4_deepdive.py:508-525
// Source signature: _load_files_full(files: list[str], repo_root: Path, *, stage: str='s4') -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _load_files_full(files, repo_root, stage) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s4_deepdive.py:509-510
  In source order: Retain source documentation literal source_literal_509_4; it is not a model call. Then Evaluate once []; assign in source target order to parts.
  // Source: vvaharness/pipeline/stages/s4_deepdive.py:511-524
  for each rel in files {
    // Source: vvaharness/pipeline/stages/s4_deepdive.py:512-512
    In source order: Evaluate once repo_root / rel; assign in source target order to p.
    // Source: vvaharness/pipeline/stages/s4_deepdive.py:513-515
    if (the source predicate not p.is_file() is truthy) {
      // Source: vvaharness/pipeline/stages/s4_deepdive.py:514-514
      In source order: Evaluate parts.append(source_template_514_25); retain side effects and discard the expression result.
      // Source: vvaharness/pipeline/stages/s4_deepdive.py:515-515
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/pipeline/stages/s4_deepdive.py:516-520
    Perform the following protected operations {
      // Source: vvaharness/pipeline/stages/s4_deepdive.py:517-517
      In source order: Evaluate once p.read_text(encoding='utf-8', errors='replace'); assign in source target order to text.
    }
    // Source: vvaharness/pipeline/stages/s4_deepdive.py:518-520
    On the first matching source exception Exception as e, in handler order {
      // Source: vvaharness/pipeline/stages/s4_deepdive.py:519-519
      In source order: Evaluate parts.append(source_template_519_25); retain side effects and discard the expression result.
      // Source: vvaharness/pipeline/stages/s4_deepdive.py:520-520
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/pipeline/stages/s4_deepdive.py:521-524
    In source order: Evaluate once _redact_source(text, rel, stage=stage); assign in source target order to text. Then Evaluate once source_literal_522_19.join((source_template_522_29 for i, ln in enumerate(text.splitlines()))); assign in source target order to numbered. Then Evaluate parts.append(source_template_524_21); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s4_deepdive.py:525-525
  End this invocation with source_literal_525_11.join(parts).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.util import logs` at source line 22: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import logs` at source line 22: `source_detail/vvaharness/util/logs.py.sudo.md`.
- `from vvaharness.backends.harness.models import is_halt_error` at source line 26: `source_detail/vvaharness/backends/harness/models.py.sudo.md`.
- `from vvaharness.backends.llm import cli` at source line 27: `source_detail/vvaharness/backends/llm/__init__.py.sudo.md`.
- `from vvaharness.backends.llm import cli` at source line 27: `source_detail/vvaharness/backends/llm/cli/__init__.py.sudo.md`.
- `from vvaharness.backends.llm.cli import GuardrailBlocked` at source line 28: `source_detail/vvaharness/backends/llm/cli/__init__.py.sudo.md`.
- `from vvaharness.backends.llm.models import guardrail_gate_hit` at source line 29: `source_detail/vvaharness/backends/llm/models.py.sudo.md`.
- `from vvaharness.backends.llm.tools import sanitize_packed_text` at source line 30: `source_detail/vvaharness/backends/llm/tools.py.sudo.md`.
- `from vvaharness.evidence import _cap_int` at source line 31: `source_detail/vvaharness/evidence/__init__.py.sudo.md`.
- `from vvaharness.models import ContextPackage, Finding, InvestigationUnit` at source line 32: `source_detail/vvaharness/models/__init__.py.sudo.md`.
- `from vvaharness.pipeline.stages.s4.batching import plan_batches` at source line 33: `source_detail/vvaharness/pipeline/stages/s4/batching.py.sudo.md`.
- `from vvaharness.report.redact import _luhn, redact, redact_counts` at source line 34: `source_detail/vvaharness/report/redact.py.sudo.md`.
- `from vvaharness.util import console` at source line 35: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import console` at source line 35: `source_detail/vvaharness/util/console.py.sudo.md`.
- `from vvaharness.util import errlog as _errlog` at source line 36: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import errlog as _errlog` at source line 36: `source_detail/vvaharness/util/errlog.py.sudo.md`.
- `from vvaharness.util.config import knob` at source line 37: `source_detail/vvaharness/util/config.py.sudo.md`.
- `from vvaharness.util.counters import COUNTERS` at source line 38: `source_detail/vvaharness/util/counters.py.sudo.md`.
- `from vvaharness.util.response_quality import is_deterministic_failure` at source line 39: `source_detail/vvaharness/util/response_quality.py.sudo.md`.
- `from vvaharness.util.warn_once import warn_once` at source line 40: `source_detail/vvaharness/util/warn_once.py.sudo.md`.
- `from vvaharness.pipeline.stages.s4.session import deepdive_tools, investigate_unit` at source line 51: `source_detail/vvaharness/pipeline/stages/s4/session.py.sudo.md`.
- `from vvaharness.pipeline.stages.s4.session import investigate_batch` at source line 385: `source_detail/vvaharness/pipeline/stages/s4/session.py.sudo.md`.
