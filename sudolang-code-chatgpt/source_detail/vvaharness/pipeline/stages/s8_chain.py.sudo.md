# vvaharness/pipeline/stages/s8_chain.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/pipeline/stages/s8_chain.py.evidence.json`. SHA-256: `911e3281266ec19ab3e90f737efe9df1eb7acab728448d5ef2b73446a6b513b1`.

```sudo
// Source: vvaharness/pipeline/stages/s8_chain.py:16-23
In source order: Retain source documentation literal source_literal_16_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from typing import Any; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import logs; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.models import TruncatedResponseError, is_halt_error; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s8_chain.py:24-45
In source order: Resolve source import from vvaharness.backends.llm.models import ModelRefusal; preserve alias and import-time effects. Then Resolve source import from vvaharness.models import ContextPackage, DroppedFinding, FinalReport, Finding, ScanMetrics; preserve alias and import-time effects. Then Resolve source import from vvaharness.pipeline.stages.s8.outcomes import ChainReport, deterministic_report, hydrate_report, parse_chain_reply, templated_summary; preserve alias and import-time effects. Then Resolve source import from vvaharness.pipeline.stages.s8.session import chain_call, repair_call, repair_fits, repairable; preserve alias and import-time effects. Then Resolve source import from vvaharness.pipeline.stages.s8.window import half_window, select_window; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s8_chain.py:46-50
In source order: Resolve source import from vvaharness.report.redact import redact; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import console; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import errlog as _errlog; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.counters import COUNTERS; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.events import Event; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s8_chain.py:51-55
In source order: Resolve source import from vvaharness.util.response_quality import is_truncated_without_retry; preserve alias and import-time effects. Then Evaluate once logs.get_logger(__name__); assign in source target order to log. Then Evaluate once 's8_ranked_findings_entry_invalid'; assign in source target order to _RANKED_INVALID.
// Source: vvaharness/pipeline/stages/s8_chain.py:58-60
// Source signature: _redacted_err(e: BaseException, cap: int=400) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _redacted_err(e, cap) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s8_chain.py:59-59
  In source order: Retain source documentation literal source_literal_59_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s8_chain.py:60-60
  End this invocation with redact(str(e))[:cap].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s8_chain.py:63-69
// Source signature: _enrichment_failure_text(e: BaseException) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _enrichment_failure_text(e) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s8_chain.py:64-66
  In source order: Retain source documentation literal source_literal_64_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s8_chain.py:67-68
  if (the source predicate isinstance(e, ModelRefusal) is truthy) {
    // Source: vvaharness/pipeline/stages/s8_chain.py:68-68
    End this invocation with 'no chain analysis: the chain model refused the request'.
  }
  // Source: vvaharness/pipeline/stages/s8_chain.py:69-69
  End this invocation with source_template_69_11.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s8_chain.py:72-99
// Source signature: _chain_call_with_half_window_retry(sub: list[Finding], labels: list[str], window: list[int], findings: list[Finding], ctx: ContextPackage, cfg) -> tuple[str, list[int], list[str], int]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _chain_call_with_half_window_retry(sub, labels, window, findings, ctx, cfg) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s8_chain.py:76-83
  In source order: Retain source documentation literal source_literal_76_4; it is not a model call. Then Evaluate once COUNTERS.get(_RANKED_INVALID); assign in source target order to invalid0.
  // Source: vvaharness/pipeline/stages/s8_chain.py:84-99
  Perform the following protected operations {
    // Source: vvaharness/pipeline/stages/s8_chain.py:85-85
    End this invocation with (chain_call(sub, ctx, cfg, labels=labels), window, labels, invalid0).
  }
  // Source: vvaharness/pipeline/stages/s8_chain.py:86-99
  On the first matching source exception TruncatedResponseError as e, in handler order {
    // Source: vvaharness/pipeline/stages/s8_chain.py:87-88
    if (the source predicate not is_truncated_without_retry(e) is truthy) {
      // Source: vvaharness/pipeline/stages/s8_chain.py:88-88
      Raise the currently handled exception.
    }
    // Source: vvaharness/pipeline/stages/s8_chain.py:89-89
    In source order: Evaluate once half_window(findings, window); assign in source target order to half.
    // Source: vvaharness/pipeline/stages/s8_chain.py:90-92
    if (the source predicate half == window is truthy) {
      // Source: vvaharness/pipeline/stages/s8_chain.py:92-92
      Raise the currently handled exception.
    }
    // Source: vvaharness/pipeline/stages/s8_chain.py:93-98
    In source order: Evaluate console.write(source_template_93_22); retain side effects and discard the expression result. Then Evaluate once [findings[i] for i in half]; assign in source target order to half_sub. Then Evaluate once [source_template_96_23 for i in half]; assign in source target order to half_labels. Then Evaluate once COUNTERS.get(_RANKED_INVALID); assign in source target order to invalid0. Then Evaluate once chain_call(half_sub, ctx, cfg, labels=half_labels, allow_resend=False); assign in source target order to raw.
    // Source: vvaharness/pipeline/stages/s8_chain.py:99-99
    End this invocation with (raw, half, half_labels, invalid0).
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s8_chain.py:102-112
// Source signature: _persist_raw(text: str, suffix: str) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _persist_raw(text, suffix) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s8_chain.py:103-103
  In source order: Retain source documentation literal source_literal_103_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s8_chain.py:104-112
  Perform the following protected operations {
    // Source: vvaharness/pipeline/stages/s8_chain.py:105-110
    In source order: Evaluate once _errlog.current_path(); assign in source target order to errp. Then Evaluate once errp.name[:-len('_errors.jsonl')] if errp.name.endswith('_errors.jsonl') else errp.stem; assign in source target order to stem. Then Evaluate once errp.parent / source_template_108_33; assign in source target order to raw_path. Then Evaluate raw_path.parent.mkdir(parents=True, exist_ok=True); retain side effects and discard the expression result. Then Evaluate raw_path.write_text(redact(text), encoding='utf-8'); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s8_chain.py:111-112
  On the first matching source exception OSError as e, in handler order {
    // Source: vvaharness/pipeline/stages/s8_chain.py:112-112
    In source order: Evaluate log.warning(Event.S8_RAW_PERSIST_FAILED, detail=redact(str(e))); retain side effects and discard the expression result.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s8_chain.py:115-144
// Source signature: _json_repair(raw: object, err: Exception, ctx: ContextPackage, cfg) -> tuple[ChainReport | None, str | None, dict[str, Any]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _json_repair(raw, err, ctx, cfg) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s8_chain.py:117-119
  In source order: Retain source documentation literal source_literal_117_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s8_chain.py:120-121
  if (the source predicate not repairable(raw) is truthy) {
    // Source: vvaharness/pipeline/stages/s8_chain.py:121-121
    End this invocation with (None, None, {}).
  }
  // Source: vvaharness/pipeline/stages/s8_chain.py:122-122
  In source order: Evaluate once str(raw); assign in source target order to text.
  // Source: vvaharness/pipeline/stages/s8_chain.py:123-127
  if (the source predicate not repair_fits(text, cfg) is truthy) {
    // Source: vvaharness/pipeline/stages/s8_chain.py:124-126
    In source order: Evaluate console.write('  [s8] reply did not parse and is too large to restate under the replay cap; no json-repair re-ask'); retain side effects and discard the expression result. Then Evaluate COUNTERS.bump('s8_parse_repair_skipped_oversize'); retain side effects and discard the expression result.
    // Source: vvaharness/pipeline/stages/s8_chain.py:127-127
    End this invocation with (None, None, {}).
  }
  // Source: vvaharness/pipeline/stages/s8_chain.py:128-130
  In source order: Evaluate console.write('  [s8] reply did not parse; one json-repair re-ask'); retain side effects and discard the expression result. Then Evaluate COUNTERS.bump('s8_parse_repair_attempted'); retain side effects and discard the expression result. Then For repaired, assign None; source annotation str | None.
  // Source: vvaharness/pipeline/stages/s8_chain.py:131-141
  Perform the following protected operations {
    // Source: vvaharness/pipeline/stages/s8_chain.py:132-133
    In source order: Evaluate once repair_call(text, err, ctx, cfg); assign in source target order to repaired. Then Evaluate once parse_chain_reply(repaired); assign in source target order to data.
  }
  // Source: vvaharness/pipeline/stages/s8_chain.py:134-141
  On the first matching source exception Exception as e2, in handler order {
    // Source: vvaharness/pipeline/stages/s8_chain.py:135-136
    if (the source predicate is_halt_error(e2) is truthy) {
      // Source: vvaharness/pipeline/stages/s8_chain.py:136-136
      Raise the currently handled exception.
    }
    // Source: vvaharness/pipeline/stages/s8_chain.py:137-137
    In source order: For extra, assign {'repair_error': redact(str(e2))[:400]}; source annotation dict[str, Any].
    // Source: vvaharness/pipeline/stages/s8_chain.py:138-140
    if (the source predicate isinstance(repaired, str) is truthy) {
      // Source: vvaharness/pipeline/stages/s8_chain.py:140-140
      In source order: Evaluate once redact(repaired)[:500].replace(source_literal_140_66, '\\n'); assign in source target order to extra['repair_head'].
    }
    // Source: vvaharness/pipeline/stages/s8_chain.py:141-141
    End this invocation with (None, None, extra).
  }
  // Source: vvaharness/pipeline/stages/s8_chain.py:142-143
  In source order: Evaluate COUNTERS.bump('s8_parse_repair_recovered'); retain side effects and discard the expression result. Then Evaluate _persist_raw(repaired, '_s8_raw_repaired.txt'); retain side effects and discard the expression result.
  // Source: vvaharness/pipeline/stages/s8_chain.py:144-144
  End this invocation with (data, repaired, {}).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s8_chain.py:147-275
// Source signature: run(findings: list[Finding], ctx: ContextPackage, cfg, *, dropped: list[DroppedFinding] | None=None, raw_findings_count: int=0, metrics: ScanMetrics | None=None) -> FinalReport
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn run(findings, ctx, cfg, dropped, raw_findings_count, metrics) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s8_chain.py:151-151
  In source order: Evaluate once dropped or []; assign in source target order to dropped.
  // Source: vvaharness/pipeline/stages/s8_chain.py:152-170
  if (the source predicate not findings is truthy) {
    // Source: vvaharness/pipeline/stages/s8_chain.py:154-154
    In source order: Evaluate once metrics is not None and (not metrics.total_files_in_scope); assign in source target order to empty.
    // Source: vvaharness/pipeline/stages/s8_chain.py:155-170
    End this invocation with FinalReport(repo_root=ctx.repo_root, findings=[], chains=[], dropped=dropped, raw_findings_count=raw_findings_count, metrics=metrics, summary='0 files analysed — no conclusion can be drawn about this repository; check the S1 file inventory and exclusions.' if empty else 'No findings survived adversarial verification.', degraded=empty, enrichment_unavailable=empty, degraded_reason='scope was empty: 0 files reached analysis' if empty else '').
  }
  // Source: vvaharness/pipeline/stages/s8_chain.py:173-180
  Perform the following protected operations {
    // Source: vvaharness/pipeline/stages/s8_chain.py:174-174
    In source order: Evaluate once select_window(findings, ctx, cfg); assign in source target order to window.
  }
  // Source: vvaharness/pipeline/stages/s8_chain.py:175-180
  On the first matching source exception Exception as e, in handler order {
    // Source: vvaharness/pipeline/stages/s8_chain.py:177-180
    In source order: Evaluate log.warning(Event.S8_WINDOW_SELECTION_FAILED, detail=redact(str(e))); retain side effects and discard the expression result. Then Evaluate _errlog.log('s8', 'chain-window', e, recovered=True); retain side effects and discard the expression result. Then Evaluate once list(range(len(findings))); assign in source target order to window.
  }
  // Source: vvaharness/pipeline/stages/s8_chain.py:181-187
  if (the source predicate not window is truthy) {
    // Source: vvaharness/pipeline/stages/s8_chain.py:183-187
    End this invocation with deterministic_report(ctx, findings, dropped, raw_findings_count, metrics, enrichment_failure='prompt_token_budget admits no findings into the enrichment window').
  }
  // Source: vvaharness/pipeline/stages/s8_chain.py:188-189
  In source order: Evaluate once [findings[i] for i in window]; assign in source target order to sub. Then Evaluate once [source_template_189_14 for i in window]; assign in source target order to labels.
  // Source: vvaharness/pipeline/stages/s8_chain.py:191-202
  Perform the following protected operations {
    // Source: vvaharness/pipeline/stages/s8_chain.py:192-193
    In source order: Evaluate once _chain_call_with_half_window_retry(sub, labels, window, findings, ctx, cfg); assign in source target order to (raw, window, labels, invalid0).
  }
  // Source: vvaharness/pipeline/stages/s8_chain.py:194-202
  On the first matching source exception Exception as e, in handler order {
    // Source: vvaharness/pipeline/stages/s8_chain.py:195-196
    if (the source predicate is_halt_error(e) is truthy) {
      // Source: vvaharness/pipeline/stages/s8_chain.py:196-196
      Raise the currently handled exception.
    }
    // Source: vvaharness/pipeline/stages/s8_chain.py:197-198
    In source order: Evaluate log.warning(Event.S8_CALL_FAILED, detail=redact(str(e))); retain side effects and discard the expression result. Then Evaluate _errlog.log('s8', 'chain', e); retain side effects and discard the expression result.
    // Source: vvaharness/pipeline/stages/s8_chain.py:199-202
    End this invocation with deterministic_report(ctx, findings, dropped, raw_findings_count, metrics, enrichment_failure=_enrichment_failure_text(e)).
  }
  // Source: vvaharness/pipeline/stages/s8_chain.py:203-206
  In source order: Evaluate once len(window) < len(findings); assign in source target order to windowed. Then Evaluate _persist_raw(raw or '', '_s8_raw.txt'); retain side effects and discard the expression result.
  // Source: vvaharness/pipeline/stages/s8_chain.py:209-231
  Perform the following protected operations {
    // Source: vvaharness/pipeline/stages/s8_chain.py:210-210
    In source order: Evaluate once parse_chain_reply(raw); assign in source target order to data.
  }
  // Source: vvaharness/pipeline/stages/s8_chain.py:211-231
  On the first matching source exception (ValueError, TypeError) as e, in handler order {
    // Source: vvaharness/pipeline/stages/s8_chain.py:213-214
    In source order: Evaluate once COUNTERS.get(_RANKED_INVALID); assign in source target order to invalid0. Then Evaluate once _json_repair(raw, e, ctx, cfg); assign in source target order to (repaired, repaired_raw, repair_extra).
    // Source: vvaharness/pipeline/stages/s8_chain.py:215-228
    if (the source predicate repaired is None is truthy) {
      // Source: vvaharness/pipeline/stages/s8_chain.py:217-222
      In source order: Evaluate once redact(raw) if isinstance(raw, str) else ''; assign in source target order to safe_raw. Then Evaluate once safe_raw[:500].replace(source_literal_218_42, '\\n'); assign in source target order to head. Then Evaluate once safe_raw[-200:].replace(source_literal_219_43, '\\n'); assign in source target order to tail. Then Evaluate log.warning(Event.S8_RESPONSE_UNPARSEABLE, detail=redact(str(e))); retain side effects and discard the expression result. Then Evaluate _errlog.log('s8', 'chain', e, raw_head=head, raw_tail=tail, **repair_extra); retain side effects and discard the expression result.
      // Source: vvaharness/pipeline/stages/s8_chain.py:223-224
      In source order: Evaluate console.write(source_template_223_26); retain side effects and discard the expression result. Then Evaluate console.write(source_template_224_26); retain side effects and discard the expression result.
      // Source: vvaharness/pipeline/stages/s8_chain.py:225-228
      End this invocation with deterministic_report(ctx, findings, dropped, raw_findings_count, metrics, enrichment_failure=source_template_227_35).
    }
    // Source: vvaharness/pipeline/stages/s8_chain.py:229-231
    In source order: Evaluate once repaired; assign in source target order to data. Then Evaluate once repaired_raw; assign in source target order to raw.
  }
  // Source: vvaharness/pipeline/stages/s8_chain.py:234-234
  In source order: Evaluate once {id(f): f.severity for f in findings}; assign in source target order to original_severity.
  // Source: vvaharness/pipeline/stages/s8_chain.py:235-247
  Perform the following protected operations {
    // Source: vvaharness/pipeline/stages/s8_chain.py:236-238
    In source order: Evaluate once hydrate_report(data, ctx, findings, dropped, raw_findings_count, metrics, window=set(window) if windowed else None, cfg=cfg); assign in source target order to (report, covered).
  }
  // Source: vvaharness/pipeline/stages/s8_chain.py:239-247
  On the first matching source exception Exception as e, in handler order {
    // Source: vvaharness/pipeline/stages/s8_chain.py:240-241
    for each f in findings {
      // Source: vvaharness/pipeline/stages/s8_chain.py:241-241
      In source order: Evaluate once original_severity[id(f)]; assign in source target order to f.severity.
    }
    // Source: vvaharness/pipeline/stages/s8_chain.py:242-243
    In source order: Evaluate log.warning(Event.S8_HYDRATION_FAILED, detail=redact(str(e))); retain side effects and discard the expression result. Then Evaluate _errlog.log('s8', 'chain-hydrate', e); retain side effects and discard the expression result.
    // Source: vvaharness/pipeline/stages/s8_chain.py:244-247
    End this invocation with deterministic_report(ctx, findings, dropped, raw_findings_count, metrics, enrichment_failure=source_template_246_31).
  }
  // Source: vvaharness/pipeline/stages/s8_chain.py:249-251
  if (the source predicate windowed is truthy) {
    // Source: vvaharness/pipeline/stages/s8_chain.py:251-251
    In source order: Evaluate once source_template_251_25; assign in source target order to report.summary.
  }
  // Source: vvaharness/pipeline/stages/s8_chain.py:254-270
  if (the source predicate len(covered) < len(window) is truthy) {
    // Source: vvaharness/pipeline/stages/s8_chain.py:255-262
    In source order: Evaluate once redact(raw)[:500].replace(source_literal_255_41, '\\n') if isinstance(raw, str) else ''; assign in source target order to head. Then Evaluate once len(window) - len(covered); assign in source target order to missing. Then Evaluate once source_template_257_15; assign in source target order to msg. Then Evaluate once len(data.ranked_findings) == len(covered) and COUNTERS.get(_RANKED_INVALID) == invalid0; assign in source target order to nothing_dropped.
    // Source: vvaharness/pipeline/stages/s8_chain.py:263-270
    if (the source predicate nothing_dropped is truthy) {
      // Source: vvaharness/pipeline/stages/s8_chain.py:264-266
      In source order: Evaluate console.counts('s8', 'sparse ranking (by design); shipping unranked', ranked=len(covered), shown=len(window), unranked=missing); retain side effects and discard the expression result. Then Evaluate COUNTERS.bump('s8_sparse_ranking_recovered'); retain side effects and discard the expression result.
    }
    else {
      // Source: vvaharness/pipeline/stages/s8_chain.py:268-270
      In source order: Evaluate log.warning(Event.S8_NO_RANKED_FINDINGS, ranked=len(covered), shown=len(window), unranked=missing, raw_head=head); retain side effects and discard the expression result. Then Evaluate _errlog.log('s8', 'chain', msg, raw_head=head); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/pipeline/stages/s8_chain.py:272-274
  In source order: Evaluate console.write(source_template_272_18); retain side effects and discard the expression result.
  // Source: vvaharness/pipeline/stages/s8_chain.py:275-275
  End this invocation with report.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.util import logs` at source line 21: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import logs` at source line 21: `source_detail/vvaharness/util/logs.py.sudo.md`.
- `from vvaharness.backends.harness.models import TruncatedResponseError, is_halt_error` at source line 23: `source_detail/vvaharness/backends/harness/models.py.sudo.md`.
- `from vvaharness.backends.llm.models import ModelRefusal` at source line 24: `source_detail/vvaharness/backends/llm/models.py.sudo.md`.
- `from vvaharness.models import ContextPackage, DroppedFinding, FinalReport, Finding, ScanMetrics` at source line 25: `source_detail/vvaharness/models/__init__.py.sudo.md`.
- `from vvaharness.pipeline.stages.s8.outcomes import ChainReport, deterministic_report, hydrate_report, parse_chain_reply, templated_summary` at source line 32: `source_detail/vvaharness/pipeline/stages/s8/outcomes.py.sudo.md`.
- `from vvaharness.pipeline.stages.s8.session import chain_call, repair_call, repair_fits, repairable` at source line 39: `source_detail/vvaharness/pipeline/stages/s8/session.py.sudo.md`.
- `from vvaharness.pipeline.stages.s8.window import half_window, select_window` at source line 45: `source_detail/vvaharness/pipeline/stages/s8/window.py.sudo.md`.
- `from vvaharness.report.redact import redact` at source line 46: `source_detail/vvaharness/report/redact.py.sudo.md`.
- `from vvaharness.util import console` at source line 47: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import console` at source line 47: `source_detail/vvaharness/util/console.py.sudo.md`.
- `from vvaharness.util import errlog as _errlog` at source line 48: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import errlog as _errlog` at source line 48: `source_detail/vvaharness/util/errlog.py.sudo.md`.
- `from vvaharness.util.counters import COUNTERS` at source line 49: `source_detail/vvaharness/util/counters.py.sudo.md`.
- `from vvaharness.util.events import Event` at source line 50: `source_detail/vvaharness/util/events.py.sudo.md`.
- `from vvaharness.util.response_quality import is_truncated_without_retry` at source line 51: `source_detail/vvaharness/util/response_quality.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../prompt_representation/vvaharness/pipeline/stages/s8_chain.py.sudo.md). Exact strings in the evidence asset support this conversion.
