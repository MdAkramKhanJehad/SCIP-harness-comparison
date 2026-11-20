# vvaharness/pipeline/stages/s6_verify.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/pipeline/stages/s6_verify.py.evidence.json`. SHA-256: `1710037a7d8f2e63047c15d3da7daea5c9e63d1ea836e8b2fbbfacfb1a1d4691`.

```sudo
// Source: vvaharness/pipeline/stages/s6_verify.py:15-20
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import logs; preserve alias and import-time effects. Then Resolve source import import contextlib; preserve alias and import-time effects. Then Resolve source import import json; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s6_verify.py:21-25
In source order: Resolve source import import os; preserve alias and import-time effects. Then Resolve source import import queue; preserve alias and import-time effects. Then Resolve source import import re; preserve alias and import-time effects. Then Resolve source import import tempfile; preserve alias and import-time effects. Then Resolve source import import threading; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s6_verify.py:26-30
In source order: Resolve source import import time; preserve alias and import-time effects. Then Resolve source import from collections import Counter; preserve alias and import-time effects. Then Resolve source import from collections.abc import Callable, Collection; preserve alias and import-time effects. Then Resolve source import from concurrent.futures import FIRST_COMPLETED, Executor, Future, wait; preserve alias and import-time effects. Then Resolve source import from datetime import UTC, datetime; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s6_verify.py:31-36
In source order: Resolve source import from functools import partial; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.models import TruncatedResponseError; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm import cli; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm.cli import GuardrailBlocked; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s6_verify.py:37-47
In source order: Resolve source import from vvaharness.backends.llm.models import ModelRefusal, call_timeout_error, guardrail_gate_hit, refusal_resend_allowed, validate_detection_tools; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm.registry import resolve; preserve alias and import-time effects. Then Resolve source import from vvaharness.evidence import _cap_int; preserve alias and import-time effects. Then Resolve source import from vvaharness.models import ContextPackage, DroppedFinding, Finding; preserve alias and import-time effects. Then Resolve source import from vvaharness.orchestrator.store import ensure_state_dir; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s6_verify.py:48-66
In source order: Resolve source import from vvaharness.pipeline.stages.replay import settle_future; preserve alias and import-time effects. Then Resolve source import from vvaharness.pipeline.stages.s5.enrich import FileCache; preserve alias and import-time effects. Then Resolve source import from vvaharness.pipeline.stages.s6.batching import Item, filed_lines, label, plan_batches, sweep_ceiling_secs, sweep_effort; preserve alias and import-time effects. Then Resolve source import from vvaharness.pipeline.stages.s6.outcomes import VerificationOutcome, apply_outcome, classify, discovered, remap_reason_ids, unverified; preserve alias and import-time effects. Then Resolve source import from vvaharness.pipeline.stages.s6.session import verify_batch; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s6_verify.py:67-71
In source order: Resolve source import from vvaharness.report.redact import redact; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import console; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import errlog as _errlog; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.config import knob; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.counters import COUNTERS; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s6_verify.py:72-83
In source order: Resolve source import from vvaharness.util.response_quality import is_deterministic_failure, is_structured_output_failure, is_timeout_failure; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.warn_once import warn_once; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.events import Event; preserve alias and import-time effects. Then Evaluate once logs.get_logger(__name__); assign in source target order to log. Then Evaluate once 60.0; assign in source target order to _HEARTBEAT_SECS.
// Source: vvaharness/pipeline/stages/s6_verify.py:85-89
In source order: Evaluate once 12; assign in source target order to _UNIFORM_CONFIDENCE_MIN. Then Evaluate once '[replayed] '; assign in source target order to _REPLAYED_LABEL. Then For _WARNED_REPLAYED_DISCOVERIES, assign set(); source annotation set[str].
// Source: vvaharness/pipeline/stages/s6_verify.py:92-141
interface _DaemonPool {
  Describe the source Python type, preserving its base/metaclass expression order: Executor.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/pipeline/stages/s6_verify.py:93-93
  In source order: Retain source documentation literal source_literal_93_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s6_verify.py:97-105
  // Source signature: __init__(self, max_workers: int, thread_name_prefix: str='s6-verify') -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self, max_workers, thread_name_prefix) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/pipeline/stages/s6_verify.py:98-99
    if (the source predicate max_workers <= 0 is truthy) {
      // Source: vvaharness/pipeline/stages/s6_verify.py:99-99
      Raise ValueError('max_workers must be greater than 0').
    }
    // Source: vvaharness/pipeline/stages/s6_verify.py:100-104
    In source order: Evaluate once max_workers; assign in source target order to self._max_workers. Then Evaluate once thread_name_prefix; assign in source target order to self._prefix. Then For self._queue, assign queue.SimpleQueue(); source annotation queue.SimpleQueue. Then For self._threads, assign []; source annotation list[threading.Thread]. Then Evaluate once threading.Lock(); assign in source target order to self._lock.
    // Source: vvaharness/pipeline/stages/s6_verify.py:105-105
    In source order: Evaluate once False; assign in source target order to self._shutdown.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/pipeline/stages/s6_verify.py:107-119
  // Source signature: submit(self, fn, /, *args, **kwargs) -> Future
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn submit(self, fn, args, kwargs) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/pipeline/stages/s6_verify.py:108-119
    Enter source context managers left-to-right: self._lock {
      // Source: vvaharness/pipeline/stages/s6_verify.py:109-110
      if (the source predicate self._shutdown is truthy) {
        // Source: vvaharness/pipeline/stages/s6_verify.py:110-110
        Raise RuntimeError('cannot schedule new futures after shutdown').
      }
      // Source: vvaharness/pipeline/stages/s6_verify.py:111-112
      In source order: For fut, assign Future(); source annotation Future. Then Evaluate self._queue.put((fut, partial(fn, *args, **kwargs))); retain side effects and discard the expression result.
      // Source: vvaharness/pipeline/stages/s6_verify.py:114-118
      if (the source predicate len(self._threads) < self._max_workers is truthy) {
        // Source: vvaharness/pipeline/stages/s6_verify.py:115-118
        In source order: Evaluate once threading.Thread(target=self._work, daemon=True, name=source_template_116_42); assign in source target order to t. Then Evaluate t.start(); retain side effects and discard the expression result. Then Evaluate self._threads.append(t); retain side effects and discard the expression result.
      }
      // Source: vvaharness/pipeline/stages/s6_verify.py:119-119
      End this invocation with fut.
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/pipeline/stages/s6_verify.py:121-125
  // Source signature: _work(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _work(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/pipeline/stages/s6_verify.py:122-125
    while (the source predicate (item := self._queue.get()) is not None is truthy) {
      // Source: vvaharness/pipeline/stages/s6_verify.py:123-125
      In source order: Evaluate settle_future(*item); retain side effects and discard the expression result. Then Delete source targets in order: item.
    }
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/pipeline/stages/s6_verify.py:127-141
  // Source signature: shutdown(self, wait: bool=True, *, cancel_futures: bool=False) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn shutdown(self, wait, cancel_futures) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/pipeline/stages/s6_verify.py:128-138
    Enter source context managers left-to-right: self._lock {
      // Source: vvaharness/pipeline/stages/s6_verify.py:129-129
      In source order: Evaluate once True; assign in source target order to self._shutdown.
      // Source: vvaharness/pipeline/stages/s6_verify.py:130-136
      while (the source predicate cancel_futures is truthy) {
        // Source: vvaharness/pipeline/stages/s6_verify.py:131-134
        Perform the following protected operations {
          // Source: vvaharness/pipeline/stages/s6_verify.py:132-132
          In source order: Evaluate once self._queue.get_nowait(); assign in source target order to item.
        }
        // Source: vvaharness/pipeline/stages/s6_verify.py:133-134
        On the first matching source exception queue.Empty, in handler order {
          // Source: vvaharness/pipeline/stages/s6_verify.py:134-134
          Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
        }
        // Source: vvaharness/pipeline/stages/s6_verify.py:135-136
        if (the source predicate item is not None is truthy) {
          // Source: vvaharness/pipeline/stages/s6_verify.py:136-136
          In source order: Evaluate item[0].cancel(); retain side effects and discard the expression result.
        }
      }
      // Source: vvaharness/pipeline/stages/s6_verify.py:137-138
      for each _ in self._threads {
        // Source: vvaharness/pipeline/stages/s6_verify.py:138-138
        In source order: Evaluate self._queue.put(None); retain side effects and discard the expression result.
      }
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    // Source: vvaharness/pipeline/stages/s6_verify.py:139-141
    if (the source predicate wait is truthy) {
      // Source: vvaharness/pipeline/stages/s6_verify.py:140-141
      for each t in self._threads {
        // Source: vvaharness/pipeline/stages/s6_verify.py:141-141
        In source order: Evaluate t.join(); retain side effects and discard the expression result.
      }
    }
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vvaharness/pipeline/stages/s6_verify.py:144-147
// Source signature: _file_cache(repo_root: str, cfg) -> FileCache
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _file_cache(repo_root, cfg) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s6_verify.py:145-145
  In source order: Retain source documentation literal source_literal_145_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s6_verify.py:147-147
  End this invocation with FileCache(repo_root, max_kb=int(knob(cfg, 'step1.max_file_kb', 1024))).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s6_verify.py:150-233
// Source signature: run(findings: list[Finding], ctx: ContextPackage, cfg, *, run_id: str='') -> tuple[list[Finding], list[DroppedFinding]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn run(findings, ctx, cfg, run_id) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s6_verify.py:152-154
  In source order: Retain source documentation literal source_literal_152_4; it is not a model call. Then Evaluate log.info('s6/verify: starting verification - findings=%d', len(findings)); retain side effects and discard the expression result. Then Evaluate once _S6Progress(len(findings), cfg, run_id); assign in source target order to progress.
  // Source: vvaharness/pipeline/stages/s6_verify.py:155-158
  if (the source predicate not findings is truthy) {
    // Source: vvaharness/pipeline/stages/s6_verify.py:156-157
    In source order: Evaluate progress.finish(); retain side effects and discard the expression result. Then Evaluate log.info('s6/verify: no findings to verify'); retain side effects and discard the expression result.
    // Source: vvaharness/pipeline/stages/s6_verify.py:158-158
    End this invocation with ([], []).
  }
  // Source: vvaharness/pipeline/stages/s6_verify.py:160-164
  In source order: Evaluate once getattr(cfg.step6_verify, 'parallel', 5); assign in source target order to parallel. Then Evaluate once getattr(cfg.step6_verify, 'min_confidence', 7); assign in source target order to min_conf. Then Evaluate once bool(knob(cfg, 'step6_verify.split_retry', True)); assign in source target order to split_retry. Then Evaluate once resolve(cfg.models.verify).via; assign in source target order to via. Then Evaluate once getattr(cfg.step6_verify, 'tool_timeout_s', None); assign in source target order to tool_timeout_s.
  // Source: vvaharness/pipeline/stages/s6_verify.py:166-175
  In source order: Evaluate once validate_detection_tools(getattr(cfg.step6_verify, 'allowed_tools', None), config_key='step6_verify.allowed_tools', via=via); assign in source target order to tools. Then Evaluate console.write(source_template_169_18); retain side effects and discard the expression result. Then For verified, assign []; source annotation list[Finding]. Then For dropped, assign []; source annotation list[DroppedFinding]. Then Evaluate once label(findings); assign in source target order to items.
  // Source: vvaharness/pipeline/stages/s6_verify.py:176-176
  In source order: Evaluate once plan_batches(items, _cap_int(cfg.step6_verify, 'batch_size', 12)); assign in source target order to batches.
  // Source: vvaharness/pipeline/stages/s6_verify.py:177-179
  if (the source predicate len(batches) < len(items) is truthy) {
    // Source: vvaharness/pipeline/stages/s6_verify.py:178-179
    In source order: Evaluate console.write(source_template_178_22); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s6_verify.py:180-193
  In source order: Evaluate once _file_cache(ctx.repo_root, cfg); assign in source target order to cache. Then Evaluate once _Sink(verified, dropped, progress, min_conf, filed_lines(items), {f.canonical_key() for f in findings}, repo_root=ctx.repo_root, stamps=bool(knob(cfg, 'step6_verify.trait_stamps', True)), reframe=bool(knob(cfg, 'step6_verify.reframe_enabled', False)), inventory=set(ctx.all_files) if getattr(ctx, 'all_files', None) else None, line_count=cache.line_count, read_lines=cache.lines); assign in source target order to sink. Then Evaluate once cli._effective_effort(None); assign in source target order to cli_effort. Then Evaluate once sweep_ceiling_secs(cfg.step6_verify, via=via, cli_effort=cli_effort); assign in source target order to ceiling. Then Evaluate once sweep_effort(cfg.step6_verify, via=via, cli_effort=cli_effort); assign in source target order to tier.
  // Source: vvaharness/pipeline/stages/s6_verify.py:195-201
  if (the source predicate tool_timeout_s is None is truthy) {
    // Source: vvaharness/pipeline/stages/s6_verify.py:196-196
    In source order: Evaluate once contextlib.nullcontext(); assign in source target order to timeout_override.
  }
  else {
    // Source: vvaharness/pipeline/stages/s6_verify.py:198-201
    In source order: Resolve source import from vvaharness.backends.harness.deepagents.options.filesystem import patched_read_timeouts; preserve alias and import-time effects. Then Evaluate once patched_read_timeouts(tool_timeout_s); assign in source target order to timeout_override.
  }
  // Source: vvaharness/pipeline/stages/s6_verify.py:204-217
  Enter source context managers left-to-right: timeout_override {
    // Source: vvaharness/pipeline/stages/s6_verify.py:206-206
    In source order: Evaluate once _DaemonPool(max_workers=parallel); assign in source target order to ex.
    // Source: vvaharness/pipeline/stages/s6_verify.py:207-217
    Perform the following protected operations {
      // Source: vvaharness/pipeline/stages/s6_verify.py:209-214
      In source order: Evaluate once _run_wave(batches, ctx, cfg, tools, sink, ex, split_retry=split_retry, ceiling=ceiling, parallel=parallel, sweep_tier=tier); assign in source target order to captive. Then Evaluate _reverify_discoveries(ctx, cfg, tools, sink, ex, captive, split_retry=split_retry, ceiling=ceiling, parallel=parallel, sweep_tier=tier); retain side effects and discard the expression result.
    }
    On every exit from this protected/handler/normal-completion region {
      // Source: vvaharness/pipeline/stages/s6_verify.py:217-217
      In source order: Evaluate ex.shutdown(wait=False, cancel_futures=True); retain side effects and discard the expression result.
    }
  }
  Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
  // Source: vvaharness/pipeline/stages/s6_verify.py:219-223
  In source order: Evaluate once len(verified); assign in source target order to tp. Then Evaluate once sum((1 for d in dropped if d.reason == 'FALSE_POSITIVE')); assign in source target order to fp. Then Evaluate once sum((1 for d in dropped if d.reason == 'UNCONFIRMED')); assign in source target order to unc. Then Evaluate once sum((1 for d in dropped if d.reason == 'GUARDRAIL_BLOCKED')); assign in source target order to gb. Then Evaluate once sum((1 for d in dropped if d.reason == 'INCONCLUSIVE')); assign in source target order to inc.
  // Source: vvaharness/pipeline/stages/s6_verify.py:225-232
  In source order: Evaluate once sum((1 for d in dropped if d.reason == 'VERIFY_ERROR')); assign in source target order to errs. Then Evaluate console.write(source_template_226_18); retain side effects and discard the expression result. Then Evaluate log.info('s6/verify: verification complete - tp=%d fp=%d unconfirmed=%d guardrail=%d inconclusive=%d errors=%d', tp, fp, unc, gb, inc, errs); retain side effects and discard the expression result. Then Evaluate _flag_uniform_confidence(sink.confidences, min_conf); retain side effects and discard the expression result.
  // Source: vvaharness/pipeline/stages/s6_verify.py:233-233
  End this invocation with (verified, dropped).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s6_verify.py:236-247
// Source signature: _flag_uniform_confidence(confidences: Counter[int], min_confidence: int) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _flag_uniform_confidence(confidences, min_confidence) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s6_verify.py:237-238
  In source order: Retain source documentation literal source_literal_237_4; it is not a model call. Then Evaluate once confidences.total(); assign in source target order to n.
  // Source: vvaharness/pipeline/stages/s6_verify.py:239-240
  if (the source predicate n < _UNIFORM_CONFIDENCE_MIN or len(confidences) != 1 is truthy) {
    // Source: vvaharness/pipeline/stages/s6_verify.py:240-240
    End this invocation with None.
  }
  // Source: vvaharness/pipeline/stages/s6_verify.py:241-247
  In source order: Evaluate once confidences; assign in source target order to (value,). Then Evaluate COUNTERS.bump('s6_confidence_uniform', n); retain side effects and discard the expression result. Then Evaluate once COUNTERS.get('s6_confidence_clamped'); assign in source target order to clamped. Then Evaluate once 'admitted every TRUE_POSITIVE' if value >= min_confidence else 'dropped every TRUE_POSITIVE as UNCONFIRMED'; assign in source target order to gate. Then Evaluate log.warning(Event.S6_UNIFORM_CONFIDENCE, verdicts=n, confidence=value, clamped=clamped, min_confidence=min_confidence, gate=gate); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s6_verify.py:250-280
// Source signature: _reverify_discoveries(ctx: ContextPackage, cfg, tools, sink: _Sink, ex: _DaemonPool, captive: set, *, split_retry: bool, ceiling: int, parallel: int, sweep_tier: str | None) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _reverify_discoveries(ctx, cfg, tools, sink, ex, captive, split_retry, ceiling, parallel, sweep_tier) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s6_verify.py:255-256
  In source order: Retain source documentation literal source_literal_255_4; it is not a model call. Then Evaluate once [f for f in sink.verified if f.origin == 's6_discovered']; assign in source target order to to_reverify.
  // Source: vvaharness/pipeline/stages/s6_verify.py:257-258
  if (the source predicate not to_reverify is truthy) {
    // Source: vvaharness/pipeline/stages/s6_verify.py:258-258
    End this invocation with None.
  }
  // Source: vvaharness/pipeline/stages/s6_verify.py:260-265
  In source order: Evaluate once [f for f in sink.verified if f.origin != 's6_discovered']; assign in source target order to sink.verified[:]. Then Evaluate console.write(source_template_261_18); retain side effects and discard the expression result. Then Evaluate once label(to_reverify); assign in source target order to items. Then Evaluate once plan_batches(items, _cap_int(cfg.step6_verify, 'batch_size', 12)); assign in source target order to batches. Then Evaluate once False; assign in source target order to sink.mint_discoveries.
  // Source: vvaharness/pipeline/stages/s6_verify.py:267-267
  In source order: Evaluate sink.progress.widen_total(len(to_reverify)); retain side effects and discard the expression result.
  // Source: vvaharness/pipeline/stages/s6_verify.py:269-270
  for each f in to_reverify {
    // Source: vvaharness/pipeline/stages/s6_verify.py:270-270
    In source order: Evaluate sink.filed.setdefault(f.file, set()).add(f.line_start); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s6_verify.py:272-272
  In source order: Evaluate once False; assign in source target order to sink.clone_repeats.
  // Source: vvaharness/pipeline/stages/s6_verify.py:273-280
  Perform the following protected operations {
    // Source: vvaharness/pipeline/stages/s6_verify.py:275-277
    In source order: Evaluate _run_wave(batches, ctx, cfg, tools, sink, ex, captive=captive, split_retry=split_retry, ceiling=ceiling, parallel=parallel, sweep_tier=sweep_tier, abort_on_guardrail=False); retain side effects and discard the expression result.
  }
  On every exit from this protected/handler/normal-completion region {
    // Source: vvaharness/pipeline/stages/s6_verify.py:279-280
    In source order: Evaluate once True; assign in source target order to sink.mint_discoveries. Then Evaluate once True; assign in source target order to sink.clone_repeats.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s6_verify.py:283-543
// Source signature: _run_wave(batches: list[list[Item]], ctx: ContextPackage, cfg, tools, sink: _Sink, ex: _DaemonPool, *, split_retry: bool, ceiling: int, parallel: int, sweep_tier: str | None, captive: set=frozenset(), abort_on_guardrail: bool=True) -> set
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _run_wave(batches, ctx, cfg, tools, sink, ex, split_retry, ceiling, parallel, sweep_tier, captive, abort_on_guardrail) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s6_verify.py:288-294
  In source order: Retain source documentation literal source_literal_288_4; it is not a model call. Then Evaluate once 0; assign in source target order to guardrail_hits. Then Evaluate once max(3, parallel); assign in source target order to guardrail_gate. Then For started, assign {}; source annotation dict[int, float]. Then For abandoned, assign {}; source annotation dict[int, threading.Event].
  // Source: vvaharness/pipeline/stages/s6_verify.py:296-296
  In source order: Evaluate once refusal_resend_allowed(cfg, cfg.models.verify); assign in source target order to refusal_resend.
  // Source: vvaharness/pipeline/stages/s6_verify.py:298-308
  // Source signature: _submit(idx: int, batch: list[Item], *, refusal_child: bool=False)
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _submit(idx, batch, refusal_child) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/pipeline/stages/s6_verify.py:299-301
    In source order: Evaluate once abandoned.setdefault(idx, threading.Event()); assign in source target order to flag. Then Evaluate once refusal_resend and len(batch) == 1 and (not refusal_child); assign in source target order to resend.
    // Source: vvaharness/pipeline/stages/s6_verify.py:303-307
    // Source signature: timed() -> dict
    Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
    fn timed() {
      Bind arguments/defaults/annotations exactly as the source signature specifies.
      // Source: vvaharness/pipeline/stages/s6_verify.py:305-305
      In source order: Evaluate once time.monotonic(); assign in source target order to started[idx].
      // Source: vvaharness/pipeline/stages/s6_verify.py:306-307
      End this invocation with verify_batch(batch, ctx, cfg, tools, abandoned=flag.is_set, resend_refusal=resend).
      If execution reaches this end, finish with the source implicit None result.
    }
    // Source: vvaharness/pipeline/stages/s6_verify.py:308-308
    End this invocation with ex.submit(timed).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/pipeline/stages/s6_verify.py:310-315
  In source order: Evaluate once {_submit(idx, batch): (idx, batch) for idx, batch in enumerate(batches)}; assign in source target order to futs. Then Evaluate once set(futs); assign in source target order to pending. Then Evaluate once len(batches); assign in source target order to next_idx. Then Evaluate once len(batches); assign in source target order to total_submitted.
  // Source: vvaharness/pipeline/stages/s6_verify.py:317-341
  // Source signature: _split_and_resubmit(batch: list[Item], e: Exception, *, counter: str, reason_prefix: str, label: str, refusal_child: bool=False) -> list[int]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _split_and_resubmit(batch, e, counter, reason_prefix, label, refusal_child) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/pipeline/stages/s6_verify.py:320-325
    In source order: Retain source documentation literal source_literal_320_8; it is not a model call. Then Bind names in enclosing nonlocal scope: next_idx, total_submitted. Then Evaluate console.write(source_template_322_22); retain side effects and discard the expression result. Then Evaluate COUNTERS.bump(counter); retain side effects and discard the expression result. Then For new_indices, assign []; source annotation list[int].
    // Source: vvaharness/pipeline/stages/s6_verify.py:326-340
    for each (fid, f) in batch {
      // Source: vvaharness/pipeline/stages/s6_verify.py:328-336
      In source order: Evaluate _errlog.log('s6-verify', source_template_328_37, e, file=getattr(f, 'file', None), line=getattr(f, 'line_start', None), vuln_class=str(getattr(f, 'vuln_class', '')), recovered=True); retain side effects and discard the expression result. Then Evaluate once next_idx; assign in source target order to cidx. Then Apply source augmented assignment next_idx += 1 with source evaluation/in-place semantics. Then Apply source augmented assignment total_submitted += 1 with source evaluation/in-place semantics. Then Evaluate once [(fid, f)]; assign in source target order to child.
      // Source: vvaharness/pipeline/stages/s6_verify.py:337-340
      In source order: Evaluate once _submit(cidx, child, refusal_child=refusal_child); assign in source target order to fut2. Then Evaluate once (cidx, child); assign in source target order to futs[fut2]. Then Evaluate pending.add(fut2); retain side effects and discard the expression result. Then Evaluate new_indices.append(cidx); retain side effects and discard the expression result.
    }
    // Source: vvaharness/pipeline/stages/s6_verify.py:341-341
    End this invocation with new_indices.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/pipeline/stages/s6_verify.py:344-352
  In source order: For resolved, assign set(); source annotation set[int]. Then For structured_split_children, assign set(); source annotation set[int]. Then For structured_singleton_retried, assign set(); source annotation set[int]. Then For timeout_split_retried, assign set(); source annotation set[int]. Then For member_children, assign set(); source annotation set[int].
  // Source: vvaharness/pipeline/stages/s6_verify.py:354-354
  In source order: For member_resubmitted, assign set(); source annotation set[int].
  // Source: vvaharness/pipeline/stages/s6_verify.py:355-357
  // Source signature: _timeout_splittable(idx: int, batch: list[Item]) -> bool
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _timeout_splittable(idx, batch) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/pipeline/stages/s6_verify.py:356-357
    End this invocation with split_retry and len(batch) > 1 and (idx not in timeout_split_retried) and (not cli.aborted()).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/pipeline/stages/s6_verify.py:359-362
  // Source signature: _timeout_split(batch: list[Item], e: Exception) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _timeout_split(batch, e) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/pipeline/stages/s6_verify.py:360-362
    In source order: Evaluate timeout_split_retried.update(_split_and_resubmit(batch, e, counter='s6_batch_timeout_split', reason_prefix='timeout-split', label='TIMEOUT')); retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/pipeline/stages/s6_verify.py:364-367
  In source order: For captive, assign set(captive); source annotation set. Then For captive_full_since, assign None; source annotation float | None. Then Evaluate once time.monotonic(); assign in source target order to quiet_since. Then Evaluate once min(_HEARTBEAT_SECS, ceiling) if ceiling > 0 else _HEARTBEAT_SECS; assign in source target order to _wake.
  // Source: vvaharness/pipeline/stages/s6_verify.py:368-541
  Perform the following protected operations {
    // Source: vvaharness/pipeline/stages/s6_verify.py:369-535
    while (the source predicate pending is truthy) {
      // Source: vvaharness/pipeline/stages/s6_verify.py:371-371
      In source order: Evaluate once wait(pending, timeout=_wake, return_when=FIRST_COMPLETED); assign in source target order to (done, _).
      // Source: vvaharness/pipeline/stages/s6_verify.py:372-480
      for each fut in done {
        // Source: vvaharness/pipeline/stages/s6_verify.py:373-374
        In source order: Evaluate pending.discard(fut); retain side effects and discard the expression result. Then Evaluate once futs[fut]; assign in source target order to (idx, batch).
        // Source: vvaharness/pipeline/stages/s6_verify.py:375-377
        if (the source predicate idx in resolved is truthy) {
          // Source: vvaharness/pipeline/stages/s6_verify.py:377-377
          Continue the immediately enclosing source loop at its next iteration.
        }
        // Source: vvaharness/pipeline/stages/s6_verify.py:378-379
        In source order: Evaluate resolved.add(idx); retain side effects and discard the expression result. Then Evaluate once time.monotonic(); assign in source target order to quiet_since.
        // Source: vvaharness/pipeline/stages/s6_verify.py:380-458
        Perform the following protected operations {
          // Source: vvaharness/pipeline/stages/s6_verify.py:381-381
          In source order: Evaluate once fut.result(); assign in source target order to outcomes.
        }
        // Source: vvaharness/pipeline/stages/s6_verify.py:382-417
        On the first matching source exception GuardrailBlocked as e, in handler order {
          // Source: vvaharness/pipeline/stages/s6_verify.py:385-388
          In source order: Evaluate once guardrail_gate_hit(e, guardrail_hits, guardrail_gate); assign in source target order to (guardrail_hits, gate_label). Then Evaluate console.write(source_template_387_34); retain side effects and discard the expression result.
          // Source: vvaharness/pipeline/stages/s6_verify.py:391-397
          if (the source predicate abort_on_guardrail and guardrail_hits >= guardrail_gate and (not sink.verified) is truthy) {
            // Source: vvaharness/pipeline/stages/s6_verify.py:393-393
            In source order: Evaluate cli.abort(); retain side effects and discard the expression result.
            // Source: vvaharness/pipeline/stages/s6_verify.py:395-397
            Raise RuntimeError(source_template_396_28) with explicit source cause e.
          }
          // Source: vvaharness/pipeline/stages/s6_verify.py:401-410
          if (the source predicate isinstance(e, ModelRefusal) is truthy) {
            // Source: vvaharness/pipeline/stages/s6_verify.py:402-408
            if (the source predicate refusal_resend and split_retry and (len(batch) > 1) and (not cli.aborted()) is truthy) {
              // Source: vvaharness/pipeline/stages/s6_verify.py:404-407
              In source order: Evaluate _split_and_resubmit(batch, e, counter='s6_batch_refusal_split', reason_prefix='refusal-split', label='REFUSED', refusal_child=True); retain side effects and discard the expression result.
              // Source: vvaharness/pipeline/stages/s6_verify.py:408-408
              Continue the immediately enclosing source loop at its next iteration.
            }
            // Source: vvaharness/pipeline/stages/s6_verify.py:409-409
            In source order: Evaluate sink.fail(batch, 'GUARDRAIL_BLOCKED', e); retain side effects and discard the expression result.
            // Source: vvaharness/pipeline/stages/s6_verify.py:410-410
            Continue the immediately enclosing source loop at its next iteration.
          }
          // Source: vvaharness/pipeline/stages/s6_verify.py:411-415
          if (the source predicate split_retry and len(batch) > 1 and (not cli.aborted()) is truthy) {
            // Source: vvaharness/pipeline/stages/s6_verify.py:412-414
            In source order: Evaluate _split_and_resubmit(batch, e, counter='s6_batch_guardrail_split', reason_prefix='guardrail-split', label='GUARDRAIL-BLOCKED'); retain side effects and discard the expression result.
            // Source: vvaharness/pipeline/stages/s6_verify.py:415-415
            Continue the immediately enclosing source loop at its next iteration.
          }
          // Source: vvaharness/pipeline/stages/s6_verify.py:416-416
          In source order: Evaluate sink.fail(batch, 'GUARDRAIL_BLOCKED', e); retain side effects and discard the expression result.
          // Source: vvaharness/pipeline/stages/s6_verify.py:417-417
          Continue the immediately enclosing source loop at its next iteration.
        }
        // Source: vvaharness/pipeline/stages/s6_verify.py:418-428
        On the first matching source exception TruncatedResponseError as e, in handler order {
          // Source: vvaharness/pipeline/stages/s6_verify.py:420-424
          if (the source predicate split_retry and len(batch) > 1 and (not cli.aborted()) is truthy) {
            // Source: vvaharness/pipeline/stages/s6_verify.py:421-423
            In source order: Evaluate _split_and_resubmit(batch, e, counter='s6_batch_truncated_split', reason_prefix='truncated-split', label='TRUNCATED'); retain side effects and discard the expression result.
            // Source: vvaharness/pipeline/stages/s6_verify.py:424-424
            Continue the immediately enclosing source loop at its next iteration.
          }
          // Source: vvaharness/pipeline/stages/s6_verify.py:425-427
          In source order: Evaluate console.write(source_template_425_34); retain side effects and discard the expression result. Then Evaluate sink.fail(batch, 'VERIFY_ERROR', e); retain side effects and discard the expression result.
          // Source: vvaharness/pipeline/stages/s6_verify.py:428-428
          Continue the immediately enclosing source loop at its next iteration.
        }
        // Source: vvaharness/pipeline/stages/s6_verify.py:429-458
        On the first matching source exception Exception as e, in handler order {
          // Source: vvaharness/pipeline/stages/s6_verify.py:431-442
          if (the source predicate split_retry and is_structured_output_failure(e) and (idx not in structured_singleton_retried) and (not cli.aborted()) is truthy) {
            // Source: vvaharness/pipeline/stages/s6_verify.py:435-441
            In source order: Evaluate COUNTERS.bump('s6_structured_retry_attempted', len(batch)); retain side effects and discard the expression result. Then Evaluate once _split_and_resubmit(batch, e, counter='s6_batch_structured_split', reason_prefix='structured-split', label='STRUCTURED-OUTPUT REJECTED'); assign in source target order to new_indices. Then Evaluate structured_split_children.update(new_indices); retain side effects and discard the expression result. Then Evaluate structured_singleton_retried.update(new_indices); retain side effects and discard the expression result.
            // Source: vvaharness/pipeline/stages/s6_verify.py:442-442
            Continue the immediately enclosing source loop at its next iteration.
          }
          // Source: vvaharness/pipeline/stages/s6_verify.py:443-446
          if (the source predicate is_timeout_failure(e) and _timeout_splittable(idx, batch) is truthy) {
            // Source: vvaharness/pipeline/stages/s6_verify.py:445-445
            In source order: Evaluate _timeout_split(batch, e); retain side effects and discard the expression result.
            // Source: vvaharness/pipeline/stages/s6_verify.py:446-446
            Continue the immediately enclosing source loop at its next iteration.
          }
          // Source: vvaharness/pipeline/stages/s6_verify.py:449-454
          if (the source predicate split_retry and len(batch) > 1 and (not is_deterministic_failure(e)) and (not cli.aborted()) is truthy) {
            // Source: vvaharness/pipeline/stages/s6_verify.py:451-453
            In source order: Evaluate _split_and_resubmit(batch, e, counter='s6_batch_generic_split', reason_prefix='generic-split', label='ERROR'); retain side effects and discard the expression result.
            // Source: vvaharness/pipeline/stages/s6_verify.py:454-454
            Continue the immediately enclosing source loop at its next iteration.
          }
          // Source: vvaharness/pipeline/stages/s6_verify.py:455-457
          In source order: Evaluate console.write(source_template_455_34); retain side effects and discard the expression result. Then Evaluate sink.fail(batch, 'VERIFY_ERROR', e); retain side effects and discard the expression result.
          // Source: vvaharness/pipeline/stages/s6_verify.py:458-458
          Continue the immediately enclosing source loop at its next iteration.
        }
        // Source: vvaharness/pipeline/stages/s6_verify.py:463-464
        In source order: Evaluate once [(fid, f) for fid, f in batch if fid not in outcomes]; assign in source target order to missing. Then For skip, assign set(); source annotation set[str].
        // Source: vvaharness/pipeline/stages/s6_verify.py:465-475
        if (the source predicate split_retry and missing and (len(batch) > 1) and (idx not in member_resubmitted) and (not cli.aborted()) is truthy) {
          // Source: vvaharness/pipeline/stages/s6_verify.py:467-475
          In source order: Evaluate COUNTERS.bump('s6_outcome_members_resubmitted', len(missing)); retain side effects and discard the expression result. Then Evaluate once _split_and_resubmit(missing, RuntimeError(source_template_470_37), counter='s6_batch_members_split', reason_prefix='members-split', label='MEMBERS OMITTED'); assign in source target order to new_indices. Then Evaluate member_resubmitted.update(new_indices); retain side effects and discard the expression result. Then Evaluate member_children.update(new_indices); retain side effects and discard the expression result. Then Evaluate once {fid for fid, _ in missing}; assign in source target order to skip.
        }
        // Source: vvaharness/pipeline/stages/s6_verify.py:476-476
        In source order: Evaluate sink.accept(batch, outcomes, skip=skip); retain side effects and discard the expression result.
        // Source: vvaharness/pipeline/stages/s6_verify.py:477-478
        if (the source predicate idx in structured_split_children is truthy) {
          // Source: vvaharness/pipeline/stages/s6_verify.py:478-478
          In source order: Evaluate COUNTERS.bump('s6_structured_retry_recovered'); retain side effects and discard the expression result.
        }
        // Source: vvaharness/pipeline/stages/s6_verify.py:479-480
        if (the source predicate idx in member_children and batch[0][0] in outcomes is truthy) {
          // Source: vvaharness/pipeline/stages/s6_verify.py:480-480
          In source order: Evaluate COUNTERS.bump('s6_outcome_members_recovered'); retain side effects and discard the expression result.
        }
      }
      // Source: vvaharness/pipeline/stages/s6_verify.py:481-481
      In source order: Evaluate once time.monotonic(); assign in source target order to now.
      // Source: vvaharness/pipeline/stages/s6_verify.py:482-527
      if (the source predicate ceiling > 0 is truthy) {
        // Source: vvaharness/pipeline/stages/s6_verify.py:483-507
        for each fut in list(pending) {
          // Source: vvaharness/pipeline/stages/s6_verify.py:484-485
          In source order: Evaluate once futs[fut]; assign in source target order to (idx, batch). Then Evaluate once started.get(idx); assign in source target order to begun.
          // Source: vvaharness/pipeline/stages/s6_verify.py:486-487
          if (the source predicate begun is None or now - begun <= ceiling is truthy) {
            // Source: vvaharness/pipeline/stages/s6_verify.py:487-487
            Continue the immediately enclosing source loop at its next iteration.
          }
          // Source: vvaharness/pipeline/stages/s6_verify.py:488-492
          In source order: Evaluate resolved.add(idx); retain side effects and discard the expression result. Then Evaluate pending.discard(fut); retain side effects and discard the expression result. Then Evaluate captive.add(fut); retain side effects and discard the expression result. Then Evaluate abandoned[idx].set(); retain side effects and discard the expression result. Then Evaluate COUNTERS.bump('s6_batch_ceiling_expired'); retain side effects and discard the expression result.
          // Source: vvaharness/pipeline/stages/s6_verify.py:493-502
          In source order: Evaluate once call_timeout_error(stage='s6', route='stage-ceiling', budget_s=ceiling, effort=sweep_tier, cause_text=source_template_496_35); assign in source target order to err. Then Evaluate once _timeout_splittable(idx, batch); assign in source target order to split. Then Evaluate console.write(source_template_498_34); retain side effects and discard the expression result.
          // Source: vvaharness/pipeline/stages/s6_verify.py:503-507
          if (the source predicate split is truthy) {
            // Source: vvaharness/pipeline/stages/s6_verify.py:505-505
            In source order: Evaluate _timeout_split(batch, err); retain side effects and discard the expression result.
          }
          else {
            // Source: vvaharness/pipeline/stages/s6_verify.py:507-507
            In source order: Evaluate sink.fail(batch, 'VERIFY_ERROR', err); retain side effects and discard the expression result.
          }
        }
        // Source: vvaharness/pipeline/stages/s6_verify.py:509-509
        In source order: Evaluate once {f for f in captive if not f.done()}; assign in source target order to captive.
        // Source: vvaharness/pipeline/stages/s6_verify.py:510-527
        if (the source predicate len(captive) >= parallel and pending is truthy) {
          // Source: vvaharness/pipeline/stages/s6_verify.py:512-525
          if (the source predicate captive_full_since is None is truthy) {
            // Source: vvaharness/pipeline/stages/s6_verify.py:513-513
            In source order: Evaluate once now; assign in source target order to captive_full_since.
          }
          else {
            // Source: vvaharness/pipeline/stages/s6_verify.py:514-525
            if (the source predicate now - captive_full_since >= ceiling is truthy) {
              // Source: vvaharness/pipeline/stages/s6_verify.py:515-525
              for each fut in list(pending) {
                // Source: vvaharness/pipeline/stages/s6_verify.py:516-516
                In source order: Evaluate once futs[fut]; assign in source target order to (idx, batch).
                // Source: vvaharness/pipeline/stages/s6_verify.py:518-525
                if (the source predicate fut.cancel() is truthy) {
                  // Source: vvaharness/pipeline/stages/s6_verify.py:519-525
                  In source order: Evaluate resolved.add(idx); retain side effects and discard the expression result. Then Evaluate pending.discard(fut); retain side effects and discard the expression result. Then Evaluate COUNTERS.bump('s6_batch_never_started'); retain side effects and discard the expression result. Then Evaluate sink.fail(batch, 'VERIFY_ERROR', TimeoutError(source_template_523_36)); retain side effects and discard the expression result.
                }
              }
            }
          }
        }
        else {
          // Source: vvaharness/pipeline/stages/s6_verify.py:527-527
          In source order: Evaluate once None; assign in source target order to captive_full_since.
        }
      }
      // Source: vvaharness/pipeline/stages/s6_verify.py:528-535
      if (the source predicate pending and now - quiet_since >= _HEARTBEAT_SECS is truthy) {
        // Source: vvaharness/pipeline/stages/s6_verify.py:530-535
        In source order: Evaluate once max((now - started[futs[f][0]] for f in pending if futs[f][0] in started), default=0.0); assign in source target order to longest. Then Evaluate console.write(source_template_532_30); retain side effects and discard the expression result. Then Evaluate once now; assign in source target order to quiet_since.
      }
    }
  }
  // Source: vvaharness/pipeline/stages/s6_verify.py:536-541
  On the first matching source exception (KeyboardInterrupt, SystemExit), in handler order {
    // Source: vvaharness/pipeline/stages/s6_verify.py:537-540
    In source order: Evaluate once cli.abort(); assign in source target order to n. Then Evaluate console.write(source_template_538_22); retain side effects and discard the expression result.
    // Source: vvaharness/pipeline/stages/s6_verify.py:541-541
    Raise the currently handled exception.
  }
  // Source: vvaharness/pipeline/stages/s6_verify.py:543-543
  End this invocation with {f for f in captive if not f.done()}.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s6_verify.py:546-606
interface _S6Progress {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/pipeline/stages/s6_verify.py:547-547
  In source order: Retain source documentation literal source_literal_547_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s6_verify.py:549-559
  // Source signature: __init__(self, total: int, cfg, run_id: str)
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self, total, cfg, run_id) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/pipeline/stages/s6_verify.py:550-554
    In source order: Evaluate once total; assign in source target order to self.total. Then Evaluate once bool(getattr(cfg.step6_verify, 'progress_file', False)); assign in source target order to self.enabled. Then For self.path, assign None; source annotation Path | None. Then Evaluate once threading.Lock(); assign in source target order to self._lock. Then For self._counts, assign {}; source annotation dict[str, int].
    // Source: vvaharness/pipeline/stages/s6_verify.py:555-555
    In source order: Evaluate once 0; assign in source target order to self._completed.
    // Source: vvaharness/pipeline/stages/s6_verify.py:556-559
    if (the source predicate self.enabled is truthy) {
      // Source: vvaharness/pipeline/stages/s6_verify.py:557-559
      In source order: Evaluate once re.sub('[^A-Za-z0-9_.-]', '_', run_id or 'current'); assign in source target order to safe_run_id. Then Evaluate once ensure_state_dir('s6_progress', safe_run_id) / 's6_progress.json'; assign in source target order to self.path. Then Evaluate self._write('running'); retain side effects and discard the expression result.
    }
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/pipeline/stages/s6_verify.py:561-567
  // Source signature: record(self, outcome: str) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn record(self, outcome) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/pipeline/stages/s6_verify.py:562-563
    if (the source predicate not self.enabled is truthy) {
      // Source: vvaharness/pipeline/stages/s6_verify.py:563-563
      End this invocation with None.
    }
    // Source: vvaharness/pipeline/stages/s6_verify.py:564-567
    Enter source context managers left-to-right: self._lock {
      // Source: vvaharness/pipeline/stages/s6_verify.py:565-567
      In source order: Apply source augmented assignment self._completed += 1 with source evaluation/in-place semantics. Then Evaluate once self._counts.get(outcome, 0) + 1; assign in source target order to self._counts[outcome]. Then Evaluate self._write('completed' if self._completed == self.total else 'running'); retain side effects and discard the expression result.
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/pipeline/stages/s6_verify.py:569-575
  // Source signature: widen_total(self, n: int) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn widen_total(self, n) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/pipeline/stages/s6_verify.py:570-570
    In source order: Retain source documentation literal source_literal_570_8; it is not a model call.
    // Source: vvaharness/pipeline/stages/s6_verify.py:571-572
    if (the source predicate not self.enabled is truthy) {
      // Source: vvaharness/pipeline/stages/s6_verify.py:572-572
      End this invocation with None.
    }
    // Source: vvaharness/pipeline/stages/s6_verify.py:573-575
    Enter source context managers left-to-right: self._lock {
      // Source: vvaharness/pipeline/stages/s6_verify.py:574-575
      In source order: Apply source augmented assignment self.total += n with source evaluation/in-place semantics. Then Evaluate self._write('completed' if self._completed == self.total else 'running'); retain side effects and discard the expression result.
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/pipeline/stages/s6_verify.py:577-581
  // Source signature: finish(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn finish(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/pipeline/stages/s6_verify.py:578-579
    if (the source predicate not self.enabled is truthy) {
      // Source: vvaharness/pipeline/stages/s6_verify.py:579-579
      End this invocation with None.
    }
    // Source: vvaharness/pipeline/stages/s6_verify.py:580-581
    Enter source context managers left-to-right: self._lock {
      // Source: vvaharness/pipeline/stages/s6_verify.py:581-581
      In source order: Evaluate self._write('completed'); retain side effects and discard the expression result.
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/pipeline/stages/s6_verify.py:583-606
  // Source signature: _write(self, status: str) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _write(self, status) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/pipeline/stages/s6_verify.py:584-584
    Enforce source assert self.path is not None; retain Python optimization-dependent assert behavior.
    // Source: vvaharness/pipeline/stages/s6_verify.py:585-594
    In source order: Evaluate once {'status': status, 'total': self.total, 'completed': self._completed, 'remaining': self.total - self._completed, 'outcomes': dict(sorted(self._counts.items())), 'updated_at': datetime.now(UTC).isoformat()}; assign in source target order to payload. Then Evaluate once tempfile.mkstemp(prefix='.s6_progress.', suffix='.tmp', dir=self.path.parent); assign in source target order to (fd, tmp_name).
    // Source: vvaharness/pipeline/stages/s6_verify.py:595-606
    Perform the following protected operations {
      // Source: vvaharness/pipeline/stages/s6_verify.py:596-600
      Enter source context managers left-to-right: os.fdopen(fd, 'w', encoding='utf-8') bound to tmp {
        // Source: vvaharness/pipeline/stages/s6_verify.py:597-600
        In source order: Evaluate json.dump(payload, tmp, separators=(',', ':')); retain side effects and discard the expression result. Then Evaluate tmp.write(source_literal_598_26); retain side effects and discard the expression result. Then Evaluate tmp.flush(); retain side effects and discard the expression result. Then Evaluate os.fsync(tmp.fileno()); retain side effects and discard the expression result.
      }
      Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
      // Source: vvaharness/pipeline/stages/s6_verify.py:601-601
      In source order: Evaluate os.replace(tmp_name, self.path); retain side effects and discard the expression result.
    }
    On every exit from this protected/handler/normal-completion region {
      // Source: vvaharness/pipeline/stages/s6_verify.py:603-606
      Perform the following protected operations {
        // Source: vvaharness/pipeline/stages/s6_verify.py:604-604
        In source order: Evaluate os.unlink(tmp_name); retain side effects and discard the expression result.
      }
      // Source: vvaharness/pipeline/stages/s6_verify.py:605-606
      On the first matching source exception FileNotFoundError, in handler order {
        // Source: vvaharness/pipeline/stages/s6_verify.py:606-606
        In source order: Perform no operation at this source statement.
      }
    }
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vvaharness/pipeline/stages/s6_verify.py:609-611
// Source signature: _ids(batch: list[Item]) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _ids(batch) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s6_verify.py:610-610
  In source order: Retain source documentation literal source_literal_610_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s6_verify.py:611-611
  End this invocation with ','.join((fid for fid, _ in batch)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s6_verify.py:619-636
In source order: Evaluate once re.compile(source_literal_620_4, re.IGNORECASE); assign in source target order to _PREMISE_IMPORT_RX. Then Evaluate once re.compile('[`\'\\"]?([A-Za-z_]\\w*(?:\\.[A-Za-z_]\\w*)*)[`\'\\"]?\\s+is\\s+(?:undefined|not\\s+defined)\\b', re.IGNORECASE); assign in source target order to _PREMISE_DEFINED_RX. Then Evaluate once frozenset({'is', 'module', 'the', 'this', 'that', 'it', 'which', 'name', 'variable', 'function', 'class', 'method'}); assign in source target order to _PREMISE_PROSE_STOPWORDS.
// Source: vvaharness/pipeline/stages/s6_verify.py:639-649
// Source signature: _premise_module(reason: str) -> tuple[str, bool] | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _premise_module(reason) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s6_verify.py:640-643
  In source order: Retain source documentation literal source_literal_640_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s6_verify.py:644-648
  for each (rx, allow_from) in ((_PREMISE_IMPORT_RX, True), (_PREMISE_DEFINED_RX, False)) {
    // Source: vvaharness/pipeline/stages/s6_verify.py:645-648
    for each m in rx.finditer(reason or '') {
      // Source: vvaharness/pipeline/stages/s6_verify.py:646-646
      In source order: Evaluate once next((g for g in m.groups() if g), None); assign in source target order to token.
      // Source: vvaharness/pipeline/stages/s6_verify.py:647-648
      if (the source predicate token and token.lower() not in _PREMISE_PROSE_STOPWORDS is truthy) {
        // Source: vvaharness/pipeline/stages/s6_verify.py:648-648
        End this invocation with (token, allow_from).
      }
    }
  }
  // Source: vvaharness/pipeline/stages/s6_verify.py:649-649
  End this invocation with None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s6_verify.py:652-660
// Source signature: _resolve_module_file(module: str, inventory: Collection[str] | None) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _resolve_module_file(module, inventory) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s6_verify.py:653-653
  In source order: Retain source documentation literal source_literal_653_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s6_verify.py:654-655
  if (the source predicate inventory is None is truthy) {
    // Source: vvaharness/pipeline/stages/s6_verify.py:655-655
    End this invocation with None.
  }
  // Source: vvaharness/pipeline/stages/s6_verify.py:656-657
  In source order: Evaluate once module.replace('.', '/'); assign in source target order to rel. Then Evaluate once (source_template_657_18, source_template_657_31); assign in source target order to candidates.
  // Source: vvaharness/pipeline/stages/s6_verify.py:658-660
  End this invocation with next((entry for entry in inventory if entry in candidates or entry.endswith(tuple((source_template_659_64 for c in candidates)))), None).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s6_verify.py:663-682
// Source signature: _premise_contradicted(reason: str, finding_file: str, inventory: Collection[str] | None, read_lines: Callable[[str], list[str] | None]) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _premise_contradicted(reason, finding_file, inventory, read_lines) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s6_verify.py:666-667
  In source order: Retain source documentation literal source_literal_666_4; it is not a model call. Then Evaluate once _premise_module(reason); assign in source target order to found.
  // Source: vvaharness/pipeline/stages/s6_verify.py:668-669
  if (the source predicate found is None is truthy) {
    // Source: vvaharness/pipeline/stages/s6_verify.py:669-669
    End this invocation with None.
  }
  // Source: vvaharness/pipeline/stages/s6_verify.py:670-674
  In source order: Evaluate once found; assign in source target order to (module, allow_from). Then Evaluate once _resolve_module_file(module, inventory) or finding_file; assign in source target order to target. Then Evaluate once read_lines(target); assign in source target order to lines.
  // Source: vvaharness/pipeline/stages/s6_verify.py:675-676
  if (the source predicate not lines is truthy) {
    // Source: vvaharness/pipeline/stages/s6_verify.py:676-676
    End this invocation with None.
  }
  // Source: vvaharness/pipeline/stages/s6_verify.py:679-681
  In source order: Evaluate once source_template_679_15 if allow_from else source_template_680_19; assign in source target order to pattern. Then Evaluate once re.compile(pattern); assign in source target order to stmt_rx.
  // Source: vvaharness/pipeline/stages/s6_verify.py:682-682
  End this invocation with module if any((stmt_rx.match(ln) for ln in lines)) else None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s6_verify.py:685-871
interface _Sink {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/pipeline/stages/s6_verify.py:686-686
  In source order: Retain source documentation literal source_literal_686_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s6_verify.py:688-717
  // Source signature: __init__(self, verified: list[Finding], dropped: list[DroppedFinding], progress: _S6Progress, min_confidence: int, filed: dict[str, set[int]], seen: set[tuple], *, repo_root: str, stamps: bool=True, reframe: bool=False, inventory: set[str] | None=None, line_count: Callable[[str], int | None]=lambda _f: None, read_lines: Callable[[str], list[str] | None]=lambda _f: None, mint_discoveries: bool=True)
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self, verified, dropped, progress, min_confidence, filed, seen, repo_root, stamps, reframe, inventory, line_count, read_lines, mint_discoveries) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/pipeline/stages/s6_verify.py:696-701
    In source order: Evaluate once verified; assign in source target order to self.verified. Then Evaluate once dropped; assign in source target order to self.dropped. Then Evaluate once progress; assign in source target order to self.progress. Then Evaluate once min_confidence; assign in source target order to self.min_confidence. Then Evaluate once mint_discoveries; assign in source target order to self.mint_discoveries.
    // Source: vvaharness/pipeline/stages/s6_verify.py:703-708
    In source order: Evaluate once True; assign in source target order to self.clone_repeats. Then Evaluate once stamps; assign in source target order to self.stamps. Then Evaluate once reframe; assign in source target order to self.reframe. Then Evaluate once inventory; assign in source target order to self.inventory. Then Evaluate once repo_root; assign in source target order to self.repo_root.
    // Source: vvaharness/pipeline/stages/s6_verify.py:709-716
    In source order: Evaluate once line_count; assign in source target order to self.line_count. Then Evaluate once read_lines; assign in source target order to self.read_lines. Then Evaluate once filed; assign in source target order to self.filed. Then Evaluate once seen; assign in source target order to self.seen. Then For self.confidences, assign Counter(); source annotation Counter[int].
    // Source: vvaharness/pipeline/stages/s6_verify.py:717-717
    In source order: Evaluate once threading.Lock(); assign in source target order to self._lock.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/pipeline/stages/s6_verify.py:719-728
  // Source signature: _reserver(self, file: str)
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _reserver(self, file) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/pipeline/stages/s6_verify.py:720-720
    In source order: Retain source documentation literal source_literal_720_8; it is not a model call.
    // Source: vvaharness/pipeline/stages/s6_verify.py:721-727
    // Source signature: reserve(line: int) -> bool
    Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
    fn reserve(line) {
      Bind arguments/defaults/annotations exactly as the source signature specifies.
      // Source: vvaharness/pipeline/stages/s6_verify.py:722-727
      Enter source context managers left-to-right: self._lock {
        // Source: vvaharness/pipeline/stages/s6_verify.py:723-723
        In source order: Evaluate once self.filed.setdefault(file, set()); assign in source target order to lines.
        // Source: vvaharness/pipeline/stages/s6_verify.py:724-725
        if (the source predicate line in lines is truthy) {
          // Source: vvaharness/pipeline/stages/s6_verify.py:725-725
          End this invocation with False.
        }
        // Source: vvaharness/pipeline/stages/s6_verify.py:726-726
        In source order: Evaluate lines.add(line); retain side effects and discard the expression result.
        // Source: vvaharness/pipeline/stages/s6_verify.py:727-727
        End this invocation with True.
      }
      Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
      If execution reaches this end, finish with the source implicit None result.
    }
    // Source: vvaharness/pipeline/stages/s6_verify.py:728-728
    End this invocation with reserve.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/pipeline/stages/s6_verify.py:730-740
  // Source signature: fail(self, batch: list[Item], reason: str, exc: Exception) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn fail(self, batch, reason, exc) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/pipeline/stages/s6_verify.py:731-733
    In source order: Retain source documentation literal source_literal_731_8; it is not a model call. Then Evaluate once redact(str(exc))[:200]; assign in source target order to detail.
    // Source: vvaharness/pipeline/stages/s6_verify.py:734-740
    for each (fid, f) in batch {
      // Source: vvaharness/pipeline/stages/s6_verify.py:735-740
      In source order: Evaluate _errlog.log('s6-verify', source_template_735_37, exc, file=getattr(f, 'file', None), line=getattr(f, 'line_start', None), vuln_class=str(getattr(f, 'vuln_class', ''))); retain side effects and discard the expression result. Then Evaluate self.dropped.append(_drop(f, reason, detail)); retain side effects and discard the expression result. Then Evaluate self.progress.record(reason); retain side effects and discard the expression result.
    }
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/pipeline/stages/s6_verify.py:742-756
  // Source signature: accept(self, batch: list[Item], outcomes: dict[str, VerificationOutcome], *, skip: Collection[str]=()) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn accept(self, batch, outcomes, skip) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/pipeline/stages/s6_verify.py:744-747
    In source order: Retain source documentation literal source_literal_744_8; it is not a model call. Then Evaluate once {fid: source_template_747_24 for fid, member in batch}; assign in source target order to display.
    // Source: vvaharness/pipeline/stages/s6_verify.py:748-756
    for each (fid, f) in batch {
      // Source: vvaharness/pipeline/stages/s6_verify.py:749-750
      if (the source predicate fid in skip is truthy) {
        // Source: vvaharness/pipeline/stages/s6_verify.py:750-750
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/pipeline/stages/s6_verify.py:751-751
      In source order: Evaluate once outcomes.get(fid); assign in source target order to outcome.
      // Source: vvaharness/pipeline/stages/s6_verify.py:752-754
      if (the source predicate outcome is None is truthy) {
        // Source: vvaharness/pipeline/stages/s6_verify.py:753-753
        In source order: Evaluate self._undetermined(fid, f); retain side effects and discard the expression result.
        // Source: vvaharness/pipeline/stages/s6_verify.py:754-754
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/pipeline/stages/s6_verify.py:755-756
      In source order: Evaluate self._judged(f, outcome, display); retain side effects and discard the expression result. Then Evaluate self._discoveries(f, outcome); retain side effects and discard the expression result.
    }
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/pipeline/stages/s6_verify.py:758-766
  // Source signature: _undetermined(self, fid: str, f: Finding) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _undetermined(self, fid, f) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/pipeline/stages/s6_verify.py:759-765
    In source order: Retain source documentation literal source_literal_759_8; it is not a model call. Then Evaluate COUNTERS.bump('s6_finding_no_outcome'); retain side effects and discard the expression result. Then Evaluate once 'verifier returned no verdict for this finding'; assign in source target order to detail. Then Evaluate _errlog.log('s6-verify', source_template_763_33, detail, file=f.file, line=f.line_start); retain side effects and discard the expression result. Then Evaluate self.dropped.append(_drop(unverified(f, detail), 'VERIFY_ERROR', detail)); retain side effects and discard the expression result.
    // Source: vvaharness/pipeline/stages/s6_verify.py:766-766
    In source order: Evaluate self.progress.record('VERIFY_ERROR'); retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/pipeline/stages/s6_verify.py:768-821
  // Source signature: _judged(self, f: Finding, outcome: VerificationOutcome, display: dict[str, str] | None=None) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _judged(self, f, outcome, display) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/pipeline/stages/s6_verify.py:770-772
    In source order: Retain source documentation literal source_literal_770_8; it is not a model call. Then Evaluate once display or {}; assign in source target order to display. Then Evaluate once classify(outcome, self.min_confidence); assign in source target order to bucket.
    // Source: vvaharness/pipeline/stages/s6_verify.py:773-782
    if (the source predicate bucket == 'FALSE_POSITIVE' is truthy) {
      // Source: vvaharness/pipeline/stages/s6_verify.py:774-775
      In source order: Evaluate once _premise_contradicted(outcome.reason, f.file, self.inventory, self.read_lines); assign in source target order to module.
      // Source: vvaharness/pipeline/stages/s6_verify.py:776-782
      if (the source predicate module is truthy) {
        // Source: vvaharness/pipeline/stages/s6_verify.py:777-782
        In source order: Evaluate COUNTERS.bump('s6_fp_premise_contradicted'); retain side effects and discard the expression result. Then Evaluate _errlog.log('s6-verify', source_template_779_41, 'false-positive premise contradicted by the code', reason='s6_fp_premise_contradicted', module=module); retain side effects and discard the expression result. Then Evaluate once 'INCONCLUSIVE'; assign in source target order to bucket.
      }
    }
    // Source: vvaharness/pipeline/stages/s6_verify.py:783-794
    In source order: Apply source augmented assignment self.confidences[outcome.confidence] += 1 with source evaluation/in-place semantics. Then Evaluate once apply_outcome(f, outcome, self._reserver(f.file) if bucket == 'TRUE_POSITIVE' else None, stamps=self.stamps, reframe=self.reframe, max_line=self.line_count(f.file), clone_repeats=self.clone_repeats); assign in source target order to results. Then Evaluate once _REPLAYED_LABEL if outcome.replayed else ''; assign in source target order to label.
    // Source: vvaharness/pipeline/stages/s6_verify.py:795-798
    for each r in results {
      // Source: vvaharness/pipeline/stages/s6_verify.py:796-796
      In source order: Evaluate once remap_reason_ids(r.verdict_reason, display); assign in source target order to r.verdict_reason.
      // Source: vvaharness/pipeline/stages/s6_verify.py:797-798
      if (the source predicate label and bucket == 'TRUE_POSITIVE' is truthy) {
        // Source: vvaharness/pipeline/stages/s6_verify.py:798-798
        In source order: Evaluate once label + r.verdict_reason; assign in source target order to r.verdict_reason.
      }
    }
    // Source: vvaharness/pipeline/stages/s6_verify.py:799-802
    In source order: Evaluate once '-' if results[0].cvss_score is None else results[0].cvss_score; assign in source target order to cvss_display. Then Evaluate console.write(source_template_801_22); retain side effects and discard the expression result.
    // Source: vvaharness/pipeline/stages/s6_verify.py:803-817
    if (the source predicate bucket == 'TRUE_POSITIVE' is truthy) {
      // Source: vvaharness/pipeline/stages/s6_verify.py:804-805
      In source order: Evaluate self.verified.extend(results); retain side effects and discard the expression result. Then Evaluate once results[0]; assign in source target order to primary.
      // Source: vvaharness/pipeline/stages/s6_verify.py:807-809
      for each r in results[1:] {
        // Source: vvaharness/pipeline/stages/s6_verify.py:808-809
        In source order: Evaluate console.write(source_template_808_30); retain side effects and discard the expression result.
      }
      // Source: vvaharness/pipeline/stages/s6_verify.py:810-813
      for each r in results {
        // Source: vvaharness/pipeline/stages/s6_verify.py:811-813
        if (the source predicate not r.cvss_vector is truthy) {
          // Source: vvaharness/pipeline/stages/s6_verify.py:813-813
          In source order: Evaluate COUNTERS.bump('s6_confirmed_without_vector'); retain side effects and discard the expression result.
        }
      }
      // Source: vvaharness/pipeline/stages/s6_verify.py:814-815
      if (the source predicate label is truthy) {
        // Source: vvaharness/pipeline/stages/s6_verify.py:815-815
        In source order: Evaluate COUNTERS.bump('s6_replayed_tp_shipped'); retain side effects and discard the expression result.
      }
      // Source: vvaharness/pipeline/stages/s6_verify.py:816-816
      In source order: Evaluate self.progress.record(bucket); retain side effects and discard the expression result.
      // Source: vvaharness/pipeline/stages/s6_verify.py:817-817
      End this invocation with None.
    }
    // Source: vvaharness/pipeline/stages/s6_verify.py:818-821
    In source order: Evaluate once source_template_818_18 if bucket == 'UNCONFIRMED' else outcome.reason; assign in source target order to detail. Then Evaluate self.dropped.append(_drop(results[0], bucket, label + detail)); retain side effects and discard the expression result. Then Evaluate self.progress.record(bucket); retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/pipeline/stages/s6_verify.py:823-830
  // Source signature: _in_repo(self, f: Finding) -> bool
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _in_repo(self, f) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/pipeline/stages/s6_verify.py:824-824
    In source order: Retain source documentation literal source_literal_824_8; it is not a model call.
    // Source: vvaharness/pipeline/stages/s6_verify.py:825-826
    if (the source predicate self.inventory is None is truthy) {
      // Source: vvaharness/pipeline/stages/s6_verify.py:826-826
      End this invocation with True.
    }
    // Source: vvaharness/pipeline/stages/s6_verify.py:827-828
    if (the source predicate f.file not in self.inventory is truthy) {
      // Source: vvaharness/pipeline/stages/s6_verify.py:828-828
      End this invocation with False.
    }
    // Source: vvaharness/pipeline/stages/s6_verify.py:829-829
    In source order: Evaluate once self.line_count(f.file); assign in source target order to eof.
    // Source: vvaharness/pipeline/stages/s6_verify.py:830-830
    End this invocation with eof is not None and 1 <= int(f.line_start or 0) <= eof.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/pipeline/stages/s6_verify.py:832-871
  // Source signature: _discoveries(self, f: Finding, outcome: VerificationOutcome) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _discoveries(self, f, outcome) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/pipeline/stages/s6_verify.py:833-833
    In source order: Retain source documentation literal source_literal_833_8; it is not a model call.
    // Source: vvaharness/pipeline/stages/s6_verify.py:834-839
    if (the source predicate not self.mint_discoveries is truthy) {
      // Source: vvaharness/pipeline/stages/s6_verify.py:836-838
      if (the source predicate outcome.additional_findings is truthy) {
        // Source: vvaharness/pipeline/stages/s6_verify.py:837-838
        In source order: Evaluate COUNTERS.bump('s6_finding_discovered_reverify_discarded', len(outcome.additional_findings)); retain side effects and discard the expression result.
      }
      // Source: vvaharness/pipeline/stages/s6_verify.py:839-839
      End this invocation with None.
    }
    // Source: vvaharness/pipeline/stages/s6_verify.py:840-848
    if (the source predicate outcome.replayed and outcome.additional_findings is truthy) {
      // Source: vvaharness/pipeline/stages/s6_verify.py:842-847
      In source order: Evaluate once len(outcome.additional_findings); assign in source target order to n. Then Evaluate COUNTERS.bump('s6_replayed_discoveries_dropped', n); retain side effects and discard the expression result. Then Evaluate warn_once(_WARNED_REPLAYED_DISCOVERIES, 's6-replayed-discoveries', source_template_845_22); retain side effects and discard the expression result.
      // Source: vvaharness/pipeline/stages/s6_verify.py:848-848
      End this invocation with None.
    }
    // Source: vvaharness/pipeline/stages/s6_verify.py:849-852
    if (the source predicate outcome.confidence < self.min_confidence is truthy) {
      // Source: vvaharness/pipeline/stages/s6_verify.py:850-851
      In source order: Evaluate COUNTERS.bump('s6_finding_discovered_unconfirmed', len(outcome.additional_findings)); retain side effects and discard the expression result.
      // Source: vvaharness/pipeline/stages/s6_verify.py:852-852
      End this invocation with None.
    }
    // Source: vvaharness/pipeline/stages/s6_verify.py:855-871
    for each extra in discovered(outcome, f, repo_root=self.repo_root, inventory=self.inventory or ()) {
      // Source: vvaharness/pipeline/stages/s6_verify.py:857-860
      if (the source predicate not self._in_repo(extra) is truthy) {
        // Source: vvaharness/pipeline/stages/s6_verify.py:859-859
        In source order: Evaluate COUNTERS.bump('s6_finding_discovered_out_of_repo'); retain side effects and discard the expression result.
        // Source: vvaharness/pipeline/stages/s6_verify.py:860-860
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/pipeline/stages/s6_verify.py:861-861
      In source order: Evaluate once extra.canonical_key(); assign in source target order to key.
      // Source: vvaharness/pipeline/stages/s6_verify.py:862-866
      Enter source context managers left-to-right: self._lock {
        // Source: vvaharness/pipeline/stages/s6_verify.py:863-865
        if (the source predicate key in self.seen is truthy) {
          // Source: vvaharness/pipeline/stages/s6_verify.py:864-864
          In source order: Evaluate COUNTERS.bump('s6_finding_discovered_duplicate'); retain side effects and discard the expression result.
          // Source: vvaharness/pipeline/stages/s6_verify.py:865-865
          Continue the immediately enclosing source loop at its next iteration.
        }
        // Source: vvaharness/pipeline/stages/s6_verify.py:866-866
        In source order: Evaluate self.seen.add(key); retain side effects and discard the expression result.
      }
      Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
      // Source: vvaharness/pipeline/stages/s6_verify.py:867-868
      In source order: Evaluate self.verified.append(extra); retain side effects and discard the expression result. Then Evaluate COUNTERS.bump('s6_finding_discovered_kept'); retain side effects and discard the expression result.
      // Source: vvaharness/pipeline/stages/s6_verify.py:869-871
      if (the source predicate not extra.cvss_vector is truthy) {
        // Source: vvaharness/pipeline/stages/s6_verify.py:871-871
        In source order: Evaluate COUNTERS.bump('s6_confirmed_without_vector'); retain side effects and discard the expression result.
      }
    }
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vvaharness/pipeline/stages/s6_verify.py:874-883
// Source signature: _drop(f: Finding, reason: str, detail: str) -> DroppedFinding
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _drop(f, reason, detail) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s6_verify.py:875-883
  End this invocation with DroppedFinding(file=f.file, line=f.line_start, vuln_class=f.vuln_class, title=f.title, chunk_id=f.chunk_id, reason=reason, detail=detail).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.util import logs` at source line 17: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import logs` at source line 17: `source_detail/vvaharness/util/logs.py.sudo.md`.
- `from vvaharness.backends.harness.models import TruncatedResponseError` at source line 34: `source_detail/vvaharness/backends/harness/models.py.sudo.md`.
- `from vvaharness.backends.llm import cli` at source line 35: `source_detail/vvaharness/backends/llm/__init__.py.sudo.md`.
- `from vvaharness.backends.llm import cli` at source line 35: `source_detail/vvaharness/backends/llm/cli/__init__.py.sudo.md`.
- `from vvaharness.backends.llm.cli import GuardrailBlocked` at source line 36: `source_detail/vvaharness/backends/llm/cli/__init__.py.sudo.md`.
- `from vvaharness.backends.llm.models import ModelRefusal, call_timeout_error, guardrail_gate_hit, refusal_resend_allowed, validate_detection_tools` at source line 37: `source_detail/vvaharness/backends/llm/models.py.sudo.md`.
- `from vvaharness.backends.llm.registry import resolve` at source line 44: `source_detail/vvaharness/backends/llm/registry.py.sudo.md`.
- `from vvaharness.evidence import _cap_int` at source line 45: `source_detail/vvaharness/evidence/__init__.py.sudo.md`.
- `from vvaharness.models import ContextPackage, DroppedFinding, Finding` at source line 46: `source_detail/vvaharness/models/__init__.py.sudo.md`.
- `from vvaharness.orchestrator.store import ensure_state_dir` at source line 47: `source_detail/vvaharness/orchestrator/store/__init__.py.sudo.md`.
- `from vvaharness.pipeline.stages.replay import settle_future` at source line 48: `source_detail/vvaharness/pipeline/stages/replay.py.sudo.md`.
- `from vvaharness.pipeline.stages.s5.enrich import FileCache` at source line 49: `source_detail/vvaharness/pipeline/stages/s5/enrich.py.sudo.md`.
- `from vvaharness.pipeline.stages.s6.batching import Item, filed_lines, label, plan_batches, sweep_ceiling_secs, sweep_effort` at source line 50: `source_detail/vvaharness/pipeline/stages/s6/batching.py.sudo.md`.
- `from vvaharness.pipeline.stages.s6.outcomes import VerificationOutcome, apply_outcome, classify, discovered, remap_reason_ids, unverified` at source line 58: `source_detail/vvaharness/pipeline/stages/s6/outcomes.py.sudo.md`.
- `from vvaharness.pipeline.stages.s6.session import verify_batch` at source line 66: `source_detail/vvaharness/pipeline/stages/s6/session.py.sudo.md`.
- `from vvaharness.report.redact import redact` at source line 67: `source_detail/vvaharness/report/redact.py.sudo.md`.
- `from vvaharness.util import console` at source line 68: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import console` at source line 68: `source_detail/vvaharness/util/console.py.sudo.md`.
- `from vvaharness.util import errlog as _errlog` at source line 69: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import errlog as _errlog` at source line 69: `source_detail/vvaharness/util/errlog.py.sudo.md`.
- `from vvaharness.util.config import knob` at source line 70: `source_detail/vvaharness/util/config.py.sudo.md`.
- `from vvaharness.util.counters import COUNTERS` at source line 71: `source_detail/vvaharness/util/counters.py.sudo.md`.
- `from vvaharness.util.response_quality import is_deterministic_failure, is_structured_output_failure, is_timeout_failure` at source line 72: `source_detail/vvaharness/util/response_quality.py.sudo.md`.
- `from vvaharness.util.warn_once import warn_once` at source line 77: `source_detail/vvaharness/util/warn_once.py.sudo.md`.
- `from vvaharness.util.events import Event` at source line 78: `source_detail/vvaharness/util/events.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.options.filesystem import patched_read_timeouts` at source line 198: `source_detail/vvaharness/backends/harness/deepagents/options/filesystem.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../prompt_representation/vvaharness/pipeline/stages/s6_verify.py.sudo.md). Exact strings in the evidence asset support this conversion.
