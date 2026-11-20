# vvaharness/orchestrator/scan.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/orchestrator/scan.py.evidence.json`. SHA-256: `614b829505ef45b8b71e3016b26dc19e68b1107870ec22f4a58027c5b30ffead`.

```sudo
// Source: vvaharness/orchestrator/scan.py:14-19
In source order: Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import logs; preserve alias and import-time effects. Then Retain source documentation literal source_literal_17_0; it is not a model call. Then Resolve source import import copy; preserve alias and import-time effects. Then Resolve source import import hashlib; preserve alias and import-time effects.
// Source: vvaharness/orchestrator/scan.py:20-24
In source order: Resolve source import import os; preserve alias and import-time effects. Then Resolve source import import shlex; preserve alias and import-time effects. Then Resolve source import import shutil; preserve alias and import-time effects. Then Resolve source import import subprocess; preserve alias and import-time effects. Then Resolve source import import time; preserve alias and import-time effects.
// Source: vvaharness/orchestrator/scan.py:25-30
In source order: Resolve source import from collections.abc import MutableMapping; preserve alias and import-time effects. Then Resolve source import from dataclasses import dataclass; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from uuid import uuid4; preserve alias and import-time effects. Then Resolve source import import httpx; preserve alias and import-time effects.
// Source: vvaharness/orchestrator/scan.py:31-36
In source order: Resolve source import import yaml; preserve alias and import-time effects. Then Resolve source import from vvaharness import config as config_mod; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.models import is_halt_error; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm.registry import resolve as resolve_model; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm.tls import coerce_verify; preserve alias and import-time effects.
// Source: vvaharness/orchestrator/scan.py:37-47
In source order: Resolve source import from vvaharness.codegraph import build_graph; preserve alias and import-time effects. Then Resolve source import from vvaharness.injectors.cve_feed import load_cves; preserve alias and import-time effects. Then Resolve source import from vvaharness.injectors.design_controls import load_controls; preserve alias and import-time effects. Then Resolve source import from vvaharness.models import ContextPackage, FinalReport, Finding, TaskManifest, ThreatModel; preserve alias and import-time effects. Then Resolve source import from vvaharness.orchestrator import store as _store; preserve alias and import-time effects.
// Source: vvaharness/orchestrator/scan.py:48-65
In source order: Resolve source import from vvaharness.orchestrator.artifacts import SCAN_DIR_NAME, UnsafeArtifactDir, artifact_dir; preserve alias and import-time effects. Then Resolve source import from vvaharness.orchestrator.case_ids import mint_case_ids; preserve alias and import-time effects. Then Resolve source import from vvaharness.orchestrator.checkpoints import EV_COLLECTION_STEP, REPO_IDENTITY_STEP, load_ckpt, load_stage_provenance, run_id_for, s4_stage_complete, save_ckpt, save_stage_provenance; preserve alias and import-time effects. Then Resolve source import from vvaharness.orchestrator.cmdb import _load_app_profile; preserve alias and import-time effects. Then Resolve source import from vvaharness.orchestrator.config_paths import _iter_model_roles, _resolve_against; preserve alias and import-time effects.
// Source: vvaharness/orchestrator/scan.py:66-82
In source order: Resolve source import from vvaharness.orchestrator.enrich_findings import _enrich_findings; preserve alias and import-time effects. Then Resolve source import from vvaharness.orchestrator.findings_json import write_findings_json; preserve alias and import-time effects. Then Resolve source import from vvaharness.pipeline.stages import s0_seed, s1_autoexclude, s1_preprocess, s2, s3_decompose, s4_deepdive, s5, s6_verify, s7_dedup, s8_chain, s9_sarif; preserve alias and import-time effects. Then Resolve source import from vvaharness.report.redact import redact; preserve alias and import-time effects. Then Resolve source import from vvaharness.sdk.loading import load_plugin_set; preserve alias and import-time effects.
// Source: vvaharness/orchestrator/scan.py:83-87
In source order: Resolve source import from vvaharness.skills import with_injected_skills; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import console; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import errlog as _errlog; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.exceptions import S2HollowAfterRetry; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import metrics as _metrics; preserve alias and import-time effects.
// Source: vvaharness/orchestrator/scan.py:88-97
In source order: Resolve source import from vvaharness.util.config import knob; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.counters import COUNTERS; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.pricing import load_pricing_cached; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.scan_progress import ScanProgress, set_active_tracker; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.stage_telemetry import CACHED_PROVENANCE, STAGE_ROLES, STAGES, stage_token_bucket; preserve alias and import-time effects.
// Source: vvaharness/orchestrator/scan.py:98-103
In source order: Resolve source import from vvaharness.util.stage_telemetry import _resolve_model as _resolve_stage_role; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.status import stage; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.tokens import TOKENS; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.events import Event; preserve alias and import-time effects. Then Evaluate once logs.get_logger(__name__); assign in source target order to log.
// Source: vvaharness/orchestrator/scan.py:107-111
// Source: vvaharness/orchestrator/scan.py:106-106
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vvaharness/orchestrator/scan.py:107-111
interface ScanOutcome {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/orchestrator/scan.py:108-111
  In source order: Retain source documentation literal source_literal_108_4; it is not a model call. Then For report_path, declare without assigning a value; source annotation Path | None. Then For finding_count, declare without assigning a value; source annotation int. Then For exit_code, assign 0; source annotation int.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vvaharness/orchestrator/scan.py:114-121
// Source signature: _head_sha(repo: Path) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _head_sha(repo) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/scan.py:115-115
  In source order: Retain source documentation literal source_literal_115_4; it is not a model call.
  // Source: vvaharness/orchestrator/scan.py:116-121
  Perform the following protected operations {
    // Source: vvaharness/orchestrator/scan.py:117-118
    In source order: Evaluate once subprocess.run(['git', '-C', str(repo), 'rev-parse', 'HEAD'], capture_output=True, text=True, timeout=20); assign in source target order to r.
    // Source: vvaharness/orchestrator/scan.py:119-119
    End this invocation with r.stdout.strip() if r.returncode == 0 else None.
  }
  // Source: vvaharness/orchestrator/scan.py:120-121
  On the first matching source exception Exception, in handler order {
    // Source: vvaharness/orchestrator/scan.py:121-121
    End this invocation with None.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/scan.py:124-130
// Source signature: _config_file_sha256(config_path: str | Path) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _config_file_sha256(config_path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/scan.py:125-125
  In source order: Retain source documentation literal source_literal_125_4; it is not a model call.
  // Source: vvaharness/orchestrator/scan.py:127-130
  Perform the following protected operations {
    // Source: vvaharness/orchestrator/scan.py:128-128
    End this invocation with hashlib.sha256(Path(config_path).read_bytes()).hexdigest().
  }
  // Source: vvaharness/orchestrator/scan.py:129-130
  On the first matching source exception OSError, in handler order {
    // Source: vvaharness/orchestrator/scan.py:130-130
    End this invocation with None.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/scan.py:133-149
// Source signature: _ledger_imbalance(s5_out_count: int, verified: list, dropped: list) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _ledger_imbalance(s5_out_count, verified, dropped) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/scan.py:134-139
  In source order: Retain source documentation literal source_literal_134_4; it is not a model call. Then Evaluate once sum((1 for f in verified if f.origin == 's6_discovered')); assign in source target order to s6_discovered_verified. Then Evaluate once sum((1 for f in verified if f.is_repeat_clone)); assign in source target order to clones. Then Evaluate once sum((1 for d in dropped if not d.chunk_id.endswith('+s6'))); assign in source target order to s6_dropped_from_s5. Then Evaluate once len(verified) - s6_discovered_verified - clones + s6_dropped_from_s5; assign in source target order to accounted.
  // Source: vvaharness/orchestrator/scan.py:140-141
  if (the source predicate accounted == s5_out_count is truthy) {
    // Source: vvaharness/orchestrator/scan.py:141-141
    End this invocation with None.
  }
  // Source: vvaharness/orchestrator/scan.py:142-142
  In source order: Evaluate once s5_out_count - accounted; assign in source target order to diff.
  // Source: vvaharness/orchestrator/scan.py:143-146
  if (the source predicate diff > 0 is truthy) {
    // Source: vvaharness/orchestrator/scan.py:144-146
    End this invocation with source_template_144_16.
  }
  // Source: vvaharness/orchestrator/scan.py:147-149
  End this invocation with source_template_147_12.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/scan.py:152-161
// Source signature: _verified_counts(verified: list[Finding]) -> tuple[int, int, int, int]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _verified_counts(verified) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/scan.py:153-157
  In source order: Retain source documentation literal source_literal_153_4; it is not a model call. Then Evaluate once [f for f in verified if f.verdict == 'TRUE_POSITIVE']; assign in source target order to tps.
  // Source: vvaharness/orchestrator/scan.py:158-161
  End this invocation with (len(tps), sum((1 for f in tps if f.origin == 's6_discovered')), sum((1 for f in tps if f.is_repeat_clone)), len(verified) - len(tps)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/scan.py:164-168
// Source signature: _verified_order(verified: list) -> list
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _verified_order(verified) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/scan.py:165-165
  In source order: Retain source documentation literal source_literal_165_4; it is not a model call.
  // Source: vvaharness/orchestrator/scan.py:166-168
  End this invocation with sorted(verified, key=lambda f: (f.file, f.line_start, f.line_end, f.cwe or '', f.vuln_class or '', f.title or '', f.chunk_id or '')).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/scan.py:171-183
// Source signature: _prune_ev_replays(run_id: str, canonical, ctx) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _prune_ev_replays(run_id, canonical, ctx) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/scan.py:172-172
  In source order: Retain source documentation literal source_literal_172_4; it is not a model call.
  // Source: vvaharness/orchestrator/scan.py:174-175
  if (the source predicate not getattr(ctx, 'ev_collection', None) is truthy) {
    // Source: vvaharness/orchestrator/scan.py:175-175
    End this invocation with None.
  }
  // Source: vvaharness/orchestrator/scan.py:176-183
  Perform the following protected operations {
    // Source: vvaharness/orchestrator/scan.py:177-178
    In source order: Resolve source import from vvaharness.exploit_verification.verify.router import replay_key; preserve alias and import-time effects. Then Evaluate once _store.prune_replays(run_id, {replay_key(f) for f in canonical}); assign in source target order to removed.
    // Source: vvaharness/orchestrator/scan.py:179-181
    if (the source predicate removed is truthy) {
      // Source: vvaharness/orchestrator/scan.py:180-181
      In source order: Evaluate console.write(source_template_180_26); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/orchestrator/scan.py:182-183
  On the first matching source exception Exception as exc, in handler order {
    // Source: vvaharness/orchestrator/scan.py:183-183
    In source order: Evaluate log.warning(Event.REPLAY_PRUNE_FAILED, error=type(exc).__name__); retain side effects and discard the expression result.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/scan.py:186-211
// Source signature: _ev_collection_in(repo: Path, args, ckpt_dir: Path, run_id: str, collection_in=None)
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _ev_collection_in(repo, args, ckpt_dir, run_id, collection_in) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/scan.py:187-189
  In source order: Retain source documentation literal source_literal_187_4; it is not a model call. Then Resolve source import from vvaharness.exploit_verification import options as ev_options; preserve alias and import-time effects.
  // Source: vvaharness/orchestrator/scan.py:191-197
  if (the source predicate ev_options.collection_path(os.environ) is truthy) {
    // Source: vvaharness/orchestrator/scan.py:192-196
    if (the source predicate collection_in is None is truthy) {
      // Source: vvaharness/orchestrator/scan.py:194-195
      In source order: Evaluate console.write('  [ev-probe] no parsed collection handed to the scan; skipping exploit verification'); retain side effects and discard the expression result.
      // Source: vvaharness/orchestrator/scan.py:196-196
      End this invocation with (None, False).
    }
    // Source: vvaharness/orchestrator/scan.py:197-197
    End this invocation with (collection_in, False).
  }
  // Source: vvaharness/orchestrator/scan.py:199-200
  if (the source predicate not getattr(args, 'resume', False) is truthy) {
    // Source: vvaharness/orchestrator/scan.py:200-200
    End this invocation with (None, False).
  }
  // Source: vvaharness/orchestrator/scan.py:201-201
  In source order: Evaluate once load_ckpt(ckpt_dir, run_id, EV_COLLECTION_STEP); assign in source target order to col.
  // Source: vvaharness/orchestrator/scan.py:202-207
  if (the source predicate col is None is truthy) {
    // Source: vvaharness/orchestrator/scan.py:204-206
    if (the source predicate getattr(args, 'stop_after', None) == 'ev' is truthy) {
      // Source: vvaharness/orchestrator/scan.py:205-206
      In source order: Evaluate console.write('  [ev] no checkpointed collection for this run — set EV_API_COLLECTION'); retain side effects and discard the expression result.
    }
    // Source: vvaharness/orchestrator/scan.py:207-207
    End this invocation with (None, False).
  }
  // Source: vvaharness/orchestrator/scan.py:208-210
  In source order: Evaluate console.write(source_template_208_18); retain side effects and discard the expression result.
  // Source: vvaharness/orchestrator/scan.py:211-211
  End this invocation with (col, True).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/scan.py:214-262
// Source signature: _ev_prep(repo: Path, args, cfg, *, ckpt_dir: Path, run_id: str, collection_in=None) -> dict | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _ev_prep(repo, args, cfg, ckpt_dir, run_id, collection_in) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/scan.py:216-220
  In source order: Retain source documentation literal source_literal_216_4; it is not a model call. Then Resolve source import from vvaharness.exploit_verification import options as ev_options; preserve alias and import-time effects. Then Resolve source import from vvaharness.exploit_verification import probe as ev_probe; preserve alias and import-time effects. Then Resolve source import from vvaharness.exploit_verification.errors import EVInputError; preserve alias and import-time effects.
  // Source: vvaharness/orchestrator/scan.py:223-224
  if (the source predicate ev_options.profile_disabled(cfg) is truthy) {
    // Source: vvaharness/orchestrator/scan.py:224-224
    End this invocation with None.
  }
  // Source: vvaharness/orchestrator/scan.py:225-225
  In source order: Evaluate once _ev_collection_in(repo, args, ckpt_dir, run_id, collection_in); assign in source target order to (col_in, resumed).
  // Source: vvaharness/orchestrator/scan.py:226-234
  if (the source predicate col_in is None is truthy) {
    // Source: vvaharness/orchestrator/scan.py:228-233
    if (the source predicate ev_options.required(cfg) is truthy) {
      // Source: vvaharness/orchestrator/scan.py:229-233
      Raise EVInputError(source_literal_230_16).
    }
    // Source: vvaharness/orchestrator/scan.py:234-234
    End this invocation with None.
  }
  // Source: vvaharness/orchestrator/scan.py:235-235
  In source order: Evaluate once ev_options.load_options(cfg, os.environ, resumed_collection=resumed); assign in source target order to opts.
  // Source: vvaharness/orchestrator/scan.py:236-237
  if (the source predicate not opts.enabled is truthy) {
    // Source: vvaharness/orchestrator/scan.py:237-237
    End this invocation with None.
  }
  // Source: vvaharness/orchestrator/scan.py:240-240
  In source order: Evaluate once ev_options.model_preflight(cfg); assign in source target order to _model_err.
  // Source: vvaharness/orchestrator/scan.py:241-242
  if (the source predicate _model_err is truthy) {
    // Source: vvaharness/orchestrator/scan.py:242-242
    Raise EVInputError(_model_err).
  }
  // Source: vvaharness/orchestrator/scan.py:244-253
  if (the source predicate resumed is truthy) {
    // Source: vvaharness/orchestrator/scan.py:246-247
    In source order: Resolve source import from vvaharness.exploit_verification import gate as ev_gate; preserve alias and import-time effects. Then Evaluate once ev_gate.run_gate(opts, os.environ, collection=col_in); assign in source target order to result.
    // Source: vvaharness/orchestrator/scan.py:248-250
    if (the source predicate result.checks is truthy) {
      // Source: vvaharness/orchestrator/scan.py:249-250
      In source order: Evaluate console.write('  [exploit-verification] collection gate (from checkpoint):'); retain side effects and discard the expression result. Then Evaluate console.write(ev_gate.format_checks(result.checks)); retain side effects and discard the expression result.
    }
  }
  else {
    // Source: vvaharness/orchestrator/scan.py:253-253
    In source order: Evaluate save_ckpt(ckpt_dir, run_id, EV_COLLECTION_STEP, col_in); retain side effects and discard the expression result.
  }
  // Source: vvaharness/orchestrator/scan.py:255-257
  In source order: Evaluate once ev_probe.run_probe(col_in, opts, allow_state_changing=bool(ev_options.ev_section(cfg).allow_state_changing_methods)); assign in source target order to col.
  // Source: vvaharness/orchestrator/scan.py:259-260
  if (the source predicate col is None is truthy) {
    // Source: vvaharness/orchestrator/scan.py:260-260
    End this invocation with None.
  }
  // Source: vvaharness/orchestrator/scan.py:261-261
  In source order: Evaluate _ev_oob_selftest(opts); retain side effects and discard the expression result.
  // Source: vvaharness/orchestrator/scan.py:262-262
  End this invocation with col.model_dump().
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/scan.py:265-284
// Source signature: _ev_oob_selftest(opts) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _ev_oob_selftest(opts) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/scan.py:266-269
  In source order: Retain source documentation literal source_literal_266_4; it is not a model call. Then Resolve source import from vvaharness.exploit_verification.executor.oob import resolve_oob; preserve alias and import-time effects. Then Evaluate once resolve_oob(opts); assign in source target order to mgr.
  // Source: vvaharness/orchestrator/scan.py:270-275
  if (the source predicate not mgr.enabled is truthy) {
    // Source: vvaharness/orchestrator/scan.py:271-274
    if (the source predicate (opts.oob_mode or 'auto') != 'off' is truthy) {
      // Source: vvaharness/orchestrator/scan.py:272-274
      In source order: Evaluate console.write(source_literal_272_26); retain side effects and discard the expression result.
    }
    // Source: vvaharness/orchestrator/scan.py:275-275
    End this invocation with None.
  }
  // Source: vvaharness/orchestrator/scan.py:276-284
  Perform the following protected operations {
    // Source: vvaharness/orchestrator/scan.py:277-282
    In source order: Evaluate mgr.start(); retain side effects and discard the expression result. Then Evaluate once mgr.self_test(); assign in source target order to ok. Then Evaluate console.mark('ok' if ok else 'fail', source_template_280_21); retain side effects and discard the expression result.
  }
  On every exit from this protected/handler/normal-completion region {
    // Source: vvaharness/orchestrator/scan.py:284-284
    In source order: Evaluate mgr.stop(); retain side effects and discard the expression result.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/scan.py:287-299
// Source signature: _hydrate_ctx_callgraph_from_store(run_id: str, ctx: ContextPackage, *steps: str) -> ContextPackage
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _hydrate_ctx_callgraph_from_store(run_id, ctx, steps) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/scan.py:289-289
  In source order: Retain source documentation literal source_literal_289_4; it is not a model call.
  // Source: vvaharness/orchestrator/scan.py:290-298
  for each step in steps {
    // Source: vvaharness/orchestrator/scan.py:291-291
    In source order: Evaluate once _store.load_callgraph(run_id, step); assign in source target order to graph.
    // Source: vvaharness/orchestrator/scan.py:292-293
    if (the source predicate not graph is truthy) {
      // Source: vvaharness/orchestrator/scan.py:293-293
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/orchestrator/scan.py:294-297
    In source order: Evaluate console.write(source_template_295_12); retain side effects and discard the expression result.
    // Source: vvaharness/orchestrator/scan.py:298-298
    End this invocation with ctx.model_copy(update={'call_graph': graph['call_graph']}).
  }
  // Source: vvaharness/orchestrator/scan.py:299-299
  End this invocation with ctx.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/scan.py:302-360
// Source signature: _upload_to_ingest(md_path: Path, sarif_path: Path, *, repository_name: str, application_id: str | None, cfg, cfg_dir: Path) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _upload_to_ingest(md_path, sarif_path, repository_name, application_id, cfg, cfg_dir) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/scan.py:305-309
  In source order: Retain source documentation literal source_literal_305_4; it is not a model call. Then Evaluate once getattr(cfg, 'output', None); assign in source target order to output_cfg. Then Evaluate once getattr(output_cfg, 'ingest_url', None); assign in source target order to url. Then Evaluate once getattr(output_cfg, 'ingest_token', None); assign in source target order to token.
  // Source: vvaharness/orchestrator/scan.py:310-312
  if (the source predicate not url is truthy) {
    // Source: vvaharness/orchestrator/scan.py:311-311
    In source order: Evaluate console.write('  [ingest] no output.ingest_url configured - skipping'); retain side effects and discard the expression result.
    // Source: vvaharness/orchestrator/scan.py:312-312
    End this invocation with False.
  }
  // Source: vvaharness/orchestrator/scan.py:313-315
  if (the source predicate not token is truthy) {
    // Source: vvaharness/orchestrator/scan.py:314-314
    In source order: Evaluate console.write('  [ingest] no output.ingest_token configured - skipping'); retain side effects and discard the expression result.
    // Source: vvaharness/orchestrator/scan.py:315-315
    End this invocation with False.
  }
  // Source: vvaharness/orchestrator/scan.py:316-318
  if (the source predicate not md_path.exists() or not sarif_path.exists() is truthy) {
    // Source: vvaharness/orchestrator/scan.py:317-317
    In source order: Evaluate console.write(source_template_317_22); retain side effects and discard the expression result.
    // Source: vvaharness/orchestrator/scan.py:318-318
    End this invocation with False.
  }
  // Source: vvaharness/orchestrator/scan.py:320-320
  In source order: Evaluate once getattr(output_cfg, 'ingest_verify', None); assign in source target order to verify.
  // Source: vvaharness/orchestrator/scan.py:321-322
  if (the source predicate verify is None is truthy) {
    // Source: vvaharness/orchestrator/scan.py:322-322
    In source order: Evaluate once getattr(getattr(cfg, 'sdk', None), 'verify_ssl', True); assign in source target order to verify.
  }
  // Source: vvaharness/orchestrator/scan.py:323-323
  In source order: Evaluate once coerce_verify(verify); assign in source target order to verify.
  // Source: vvaharness/orchestrator/scan.py:324-330
  if (the source predicate isinstance(verify, str) is truthy) {
    // Source: vvaharness/orchestrator/scan.py:325-325
    In source order: Evaluate once _resolve_against(cfg_dir, verify); assign in source target order to verify.
    // Source: vvaharness/orchestrator/scan.py:326-330
    if (the source predicate not Path(verify).exists() is truthy) {
      // Source: vvaharness/orchestrator/scan.py:328-329
      In source order: Evaluate log.error(Event.INGEST_CA_MISSING, path=verify, remedy='set output.ingest_verify to a readable bundle, or to false to accept an unverified upload'); retain side effects and discard the expression result.
      // Source: vvaharness/orchestrator/scan.py:330-330
      End this invocation with False.
    }
  }
  // Source: vvaharness/orchestrator/scan.py:332-336
  In source order: Evaluate once {'Authorization': source_template_333_25, 'accept': 'application/json'}; assign in source target order to headers. Then Evaluate once {'repositoryName': repository_name}; assign in source target order to data.
  // Source: vvaharness/orchestrator/scan.py:337-338
  if (the source predicate application_id is truthy) {
    // Source: vvaharness/orchestrator/scan.py:338-338
    In source order: Evaluate once application_id; assign in source target order to data['applicationId'].
  }
  // Source: vvaharness/orchestrator/scan.py:340-340
  In source order: Evaluate console.write(source_template_340_18); retain side effects and discard the expression result.
  // Source: vvaharness/orchestrator/scan.py:341-360
  Perform the following protected operations {
    // Source: vvaharness/orchestrator/scan.py:342-348
    Enter source context managers left-to-right: open(md_path, 'rb') bound to md_f; open(sarif_path, 'rb') bound to sarif_f {
      // Source: vvaharness/orchestrator/scan.py:343-346
      In source order: Evaluate once {'file': (md_path.name, md_f, 'text/markdown'), 'sarifFile': (sarif_path.name, sarif_f, 'application/json')}; assign in source target order to files.
      // Source: vvaharness/orchestrator/scan.py:347-348
      Enter source context managers left-to-right: httpx.Client(timeout=60, verify=verify) bound to client {
        // Source: vvaharness/orchestrator/scan.py:348-348
        In source order: Evaluate once client.post(url, headers=headers, data=data, files=files); assign in source target order to resp.
      }
      Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    // Source: vvaharness/orchestrator/scan.py:349-354
    if (the source predicate resp.status_code >= 400 is truthy) {
      // Source: vvaharness/orchestrator/scan.py:350-353
      In source order: Evaluate once (resp.text or '')[:500]; assign in source target order to body. Then Evaluate console.write(source_template_351_26); retain side effects and discard the expression result.
      // Source: vvaharness/orchestrator/scan.py:354-354
      End this invocation with False.
    }
    // Source: vvaharness/orchestrator/scan.py:355-356
    In source order: Evaluate console.write(source_template_355_22); retain side effects and discard the expression result.
    // Source: vvaharness/orchestrator/scan.py:357-357
    End this invocation with True.
  }
  // Source: vvaharness/orchestrator/scan.py:358-360
  On the first matching source exception Exception as e, in handler order {
    // Source: vvaharness/orchestrator/scan.py:359-359
    In source order: Evaluate console.write(source_template_359_22); retain side effects and discard the expression result.
    // Source: vvaharness/orchestrator/scan.py:360-360
    End this invocation with False.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/scan.py:363-370
// Source signature: _recorded_stage_outcome(step_id: str, fallback: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _recorded_stage_outcome(step_id, fallback) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/scan.py:364-367
  In source order: Retain source documentation literal source_literal_364_4; it is not a model call. Then Evaluate once STAGES.snapshot().get(step_id) or {}; assign in source target order to rec. Then Evaluate once rec.get('outcome'); assign in source target order to recorded.
  // Source: vvaharness/orchestrator/scan.py:368-369
  if (the source predicate recorded in (None, 'running', 'not_run') is truthy) {
    // Source: vvaharness/orchestrator/scan.py:369-369
    End this invocation with fallback.
  }
  // Source: vvaharness/orchestrator/scan.py:370-370
  End this invocation with recorded.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/scan.py:373-376
// Source signature: _artifact_module_name(repo_name: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _artifact_module_name(repo_name) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/scan.py:374-375
  In source order: Retain source documentation literal source_literal_374_4; it is not a model call. Then Evaluate once ''.join((c if c.isalnum() or c in '._-' else '_' for c in repo_name)); assign in source target order to safe.
  // Source: vvaharness/orchestrator/scan.py:376-376
  End this invocation with safe if safe and safe.strip('.') else 'repo'.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/scan.py:380-1072
// Source: vvaharness/orchestrator/scan.py:379-379
Before creating this callable, evaluate and retain decorators top-to-bottom: with_injected_skills.
// Source: vvaharness/orchestrator/scan.py:380-1072
// Source signature: scan_repo(repo: Path, repo_name: str, application_id: str | None, args, cfg, path_prefix: str | None=None, ev_collection_in=None) -> ScanOutcome
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn scan_repo(repo, repo_name, application_id, args, cfg, path_prefix, ev_collection_in) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/scan.py:384-392
  In source order: Retain source documentation literal source_literal_384_4; it is not a model call. Then Evaluate once run_id_for(repo); assign in source target order to run_id. Then Evaluate once _store.state_root(); assign in source target order to _state. Then Evaluate once _state / 'checkpoints' / run_id; assign in source target order to ckpt_dir. Then Evaluate _store.register_run(run_id, repo_root=str(repo.resolve()), repo_name=repo_name, app_id=application_id); retain side effects and discard the expression result.
  // Source: vvaharness/orchestrator/scan.py:395-399
  if (the source predicate not args.resume and args.stop_after != 'ev' is truthy) {
    // Source: vvaharness/orchestrator/scan.py:396-396
    In source order: Evaluate once _store.reset_run(run_id); assign in source target order to _cleared.
    // Source: vvaharness/orchestrator/scan.py:397-399
    if (the source predicate _cleared is truthy) {
      // Source: vvaharness/orchestrator/scan.py:398-399
      In source order: Evaluate console.write(source_template_398_26); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/orchestrator/scan.py:402-402
  In source order: Evaluate once _head_sha(repo); assign in source target order to repo_head.
  // Source: vvaharness/orchestrator/scan.py:403-408
  if (the source predicate args.resume and repo_head is truthy) {
    // Source: vvaharness/orchestrator/scan.py:404-404
    In source order: Evaluate once load_ckpt(ckpt_dir, run_id, REPO_IDENTITY_STEP); assign in source target order to prior_head.
    // Source: vvaharness/orchestrator/scan.py:405-408
    if (the source predicate isinstance(prior_head, str) and prior_head and (prior_head != repo_head) is truthy) {
      // Source: vvaharness/orchestrator/scan.py:406-408
      In source order: Evaluate log.warning(Event.CKPT_TARGET_CHANGED, run_id=run_id[:12], prior_head=prior_head[:12], repo_head=repo_head[:12]); retain side effects and discard the expression result. Then Evaluate _store.reset_run(run_id); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/orchestrator/scan.py:409-410
  if (the source predicate repo_head is truthy) {
    // Source: vvaharness/orchestrator/scan.py:410-410
    In source order: Evaluate save_ckpt(ckpt_dir, run_id, REPO_IDENTITY_STEP, repo_head); retain side effects and discard the expression result.
  }
  // Source: vvaharness/orchestrator/scan.py:413-416
  In source order: Evaluate once artifact_dir(repo, SCAN_DIR_NAME); assign in source target order to out_dir. Then Evaluate once 0; assign in source target order to rem_rc.
  // Source: vvaharness/orchestrator/scan.py:419-427
  if (the source predicate args.resume is truthy) {
    // Source: vvaharness/orchestrator/scan.py:420-427
    Perform the following protected operations {
      // Source: vvaharness/orchestrator/scan.py:421-421
      In source order: Evaluate ckpt_dir.resolve().relative_to(repo.resolve()); retain side effects and discard the expression result.
    }
    // Source: vvaharness/orchestrator/scan.py:422-423
    On the first matching source exception ValueError, in handler order {
      // Source: vvaharness/orchestrator/scan.py:423-423
      In source order: Perform no operation at this source statement.
    }
    Only when the protected body falls through normally, without exception, return, break or continue {
      // Source: vvaharness/orchestrator/scan.py:425-426
      In source order: Evaluate console.mark('fail', 'refusing --resume: checkpoint dir resolves inside the scanned repository', indent=0); retain side effects and discard the expression result.
      // Source: vvaharness/orchestrator/scan.py:427-427
      End this invocation with ScanOutcome(None, 0).
    }
  }
  // Source: vvaharness/orchestrator/scan.py:429-434
  In source order: Evaluate once time.time(); assign in source target order to t0. Then Evaluate once _metrics.now_iso(); assign in source target order to start_ts. Then Evaluate once start_ts.replace(':', '').replace('-', ''); assign in source target order to ts_safe. Then Evaluate once _artifact_module_name(repo_name); assign in source target order to module_safe. Then Evaluate once out_dir / source_template_434_25; assign in source target order to out_path.
  // Source: vvaharness/orchestrator/scan.py:435-441
  In source order: Evaluate once out_dir / source_template_435_27; assign in source target order to sarif_path. Then Evaluate _errlog.configure(out_dir / source_template_437_32); retain side effects and discard the expression result. Then Evaluate once _ev_prep(repo, args, cfg, ckpt_dir=ckpt_dir, run_id=run_id, collection_in=ev_collection_in); assign in source target order to ev_collection.
  // Source: vvaharness/orchestrator/scan.py:442-443
  if (the source predicate args.stop_after == 'ev' is truthy) {
    // Source: vvaharness/orchestrator/scan.py:443-443
    End this invocation with ScanOutcome(None, 0).
  }
  // Source: vvaharness/orchestrator/scan.py:446-503
  if (the source predicate getattr(args, 'auto_step1', False) is truthy) {
    // Source: vvaharness/orchestrator/scan.py:448-449
    In source order: Evaluate _store.ensure_state_dir('checkpoints', run_id); retain side effects and discard the expression result. Then Evaluate once ckpt_dir / 'step1.yaml'; assign in source target order to auto_path.
    // Source: vvaharness/orchestrator/scan.py:450-494
    if (the source predicate not (args.resume and auto_path.is_file()) is truthy) {
      // Source: vvaharness/orchestrator/scan.py:451-459
      Perform the following protected operations {
        // Source: vvaharness/orchestrator/scan.py:452-453
        Enter source context managers left-to-right: TOKENS.phase('s1-autoexclude') {
          // Source: vvaharness/orchestrator/scan.py:453-453
          In source order: Evaluate s1_autoexclude.run(repo, cfg, out_path=auto_path); retain side effects and discard the expression result.
        }
        Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
      }
      // Source: vvaharness/orchestrator/scan.py:454-459
      On the first matching source exception Exception as e, in handler order {
        // Source: vvaharness/orchestrator/scan.py:455-456
        if (the source predicate is_halt_error(e) is truthy) {
          // Source: vvaharness/orchestrator/scan.py:456-456
          Raise the currently handled exception.
        }
        // Source: vvaharness/orchestrator/scan.py:457-459
        In source order: Evaluate log.warning(Event.S1_AUTOEXCLUDE_FAILED, detail=str(e)); retain side effects and discard the expression result. Then Evaluate _errlog.log('s1.autoexclude', repo_name, e); retain side effects and discard the expression result. Then Evaluate once None; assign in source target order to auto_path.
      }
    }
    else {
      // Source: vvaharness/orchestrator/scan.py:461-463
      In source order: Evaluate console.write(source_template_461_26); retain side effects and discard the expression result. Then Evaluate once yaml.safe_load(auto_path.read_text(encoding='utf-8')) or {}; assign in source target order to stored.
      // Source: vvaharness/orchestrator/scan.py:464-494
      if (the source predicate isinstance(stored, dict) is truthy) {
        // Source: vvaharness/orchestrator/scan.py:465-470
        In source order: Evaluate once list(stored.get('exclude_dirs') or []); assign in source target order to dirs0. Then Evaluate once list(stored.get('exclude_exts') or []); assign in source target order to exts0. Then Evaluate once list(stored.get('exclude_globs') or []); assign in source target order to globs0. Then Evaluate once s1_autoexclude.vet_overlay(repo, cfg, dirs=dirs0, exts=exts0, globs=globs0); assign in source target order to (dirs1, exts1, globs1). Then Evaluate once stored.get('config_dedup') or {}; assign in source target order to dedup0.
        // Source: vvaharness/orchestrator/scan.py:471-475
        In source order: Evaluate once s1_autoexclude.vet_config_dedup(dedup0); assign in source target order to dedup1. Then Evaluate once sorted(set(dirs0) - set(dirs1)); assign in source target order to vetoed_dirs. Then Evaluate once sorted(set(exts0) - set(exts1)); assign in source target order to vetoed_exts. Then Evaluate once sorted(set(globs0) - set(globs1)); assign in source target order to vetoed_globs. Then Evaluate once dedup1 != dedup0; assign in source target order to changed_dedup.
        // Source: vvaharness/orchestrator/scan.py:476-494
        if (the source predicate vetoed_dirs or vetoed_exts or vetoed_globs or changed_dedup is truthy) {
          // Source: vvaharness/orchestrator/scan.py:477-484
          In source order: Evaluate log.warning(source_template_477_32 + (source_template_480_29 if changed_dedup else '')); retain side effects and discard the expression result. Then Evaluate once dirs1; assign in source target order to stored['exclude_dirs']. Then Evaluate once exts1; assign in source target order to stored['exclude_exts']. Then Evaluate once globs1; assign in source target order to stored['exclude_globs'].
          // Source: vvaharness/orchestrator/scan.py:485-488
          if (the source predicate dedup1 is truthy) {
            // Source: vvaharness/orchestrator/scan.py:486-486
            In source order: Evaluate once dedup1; assign in source target order to stored['config_dedup'].
          }
          else {
            // Source: vvaharness/orchestrator/scan.py:487-488
            if (the source predicate 'config_dedup' in stored is truthy) {
              // Source: vvaharness/orchestrator/scan.py:488-488
              In source order: Delete source targets in order: stored['config_dedup'].
            }
          }
          // Source: vvaharness/orchestrator/scan.py:489-494
          In source order: Evaluate auto_path.write_text(source_literal_490_24 + yaml.safe_dump(stored, sort_keys=False, default_flow_style=False), encoding='utf-8'); retain side effects and discard the expression result.
        }
      }
    }
    // Source: vvaharness/orchestrator/scan.py:495-503
    if (the source predicate auto_path and auto_path.is_file() is truthy) {
      // Source: vvaharness/orchestrator/scan.py:496-503
      In source order: Evaluate once config_mod.Config(copy.deepcopy(cfg._data)); assign in source target order to cfg. Then Evaluate once config_mod.apply_step1_overlay(cfg, auto_path, expand=False); assign in source target order to (cfg, _). Then Evaluate once cfg._data.get('step1', {}); assign in source target order to s1. Then Evaluate console.write(source_template_500_26); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/orchestrator/scan.py:506-508
  In source order: Evaluate once ScanProgress.from_cfg(cfg, repo_name=repo_name); assign in source target order to tracker. Then Evaluate set_active_tracker(tracker); retain side effects and discard the expression result. Then Evaluate once tracker; assign in source target order to cfg._data['_scan_progress'].
  // Source: vvaharness/orchestrator/scan.py:510-512
  // Source signature: _sp_start(step_id: str, label: str) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _sp_start(step_id, label) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/orchestrator/scan.py:511-512
    if (the source predicate tracker.enabled is truthy) {
      // Source: vvaharness/orchestrator/scan.py:512-512
      In source order: Evaluate tracker.stage_started(step_id, label=label); retain side effects and discard the expression result.
    }
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/orchestrator/scan.py:514-528
  // Source signature: _sp_done(step_id: str, *, outcome: str='completed', detail: str='') -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _sp_done(step_id, outcome, detail) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/orchestrator/scan.py:517-518
    if (the source predicate outcome not in ('completed', 'error') is truthy) {
      // Source: vvaharness/orchestrator/scan.py:518-518
      In source order: Evaluate STAGES.mark(step_id, outcome); retain side effects and discard the expression result.
    }
    // Source: vvaharness/orchestrator/scan.py:519-523
    if (the source predicate outcome == 'cached' is truthy) {
      // Source: vvaharness/orchestrator/scan.py:521-521
      In source order: Evaluate once load_stage_provenance(ckpt_dir, run_id, step_id); assign in source target order to prov.
      // Source: vvaharness/orchestrator/scan.py:522-523
      if (the source predicate prov is not None is truthy) {
        // Source: vvaharness/orchestrator/scan.py:523-523
        In source order: Evaluate CACHED_PROVENANCE.record(step_id, prov); retain side effects and discard the expression result.
      }
    }
    // Source: vvaharness/orchestrator/scan.py:524-528
    if (the source predicate tracker.enabled is truthy) {
      // Source: vvaharness/orchestrator/scan.py:526-528
      In source order: Evaluate tracker.stage_done(step_id, outcome=_recorded_stage_outcome(step_id, outcome), detail=detail); retain side effects and discard the expression result.
    }
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/orchestrator/scan.py:530-533
  In source order: Evaluate console.banner(); retain side effects and discard the expression result. Then Evaluate console.write(source_template_531_18); retain side effects and discard the expression result. Then Evaluate console.write('  models:'); retain side effects and discard the expression result.
  // Source: vvaharness/orchestrator/scan.py:534-537
  for each (role, m) in _iter_model_roles(cfg) {
    // Source: vvaharness/orchestrator/scan.py:535-537
    In source order: Evaluate once resolve_model(m); assign in source target order to (mid, via, extras). Then Evaluate once source_template_536_13 if extras else ''; assign in source target order to ex. Then Evaluate console.write(source_template_537_22); retain side effects and discard the expression result.
  }
  // Source: vvaharness/orchestrator/scan.py:539-544
  In source order: Evaluate once Path(args.config).resolve().parent; assign in source target order to cfg_dir. Then Evaluate once load_cves(_resolve_against(cfg_dir, cfg.inject.cve_file)); assign in source target order to cves. Then Evaluate once load_controls(_resolve_against(cfg_dir, cfg.inject.controls_file)); assign in source target order to controls. Then Evaluate once _load_app_profile(application_id); assign in source target order to (app_profile, app_info). Then Evaluate console.write(source_template_543_18); retain side effects and discard the expression result.
  // Source: vvaharness/orchestrator/scan.py:546-548
  // Source signature: _m(role: str) -> str
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _m(role) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/orchestrator/scan.py:547-547
    In source order: Evaluate once resolve_model(getattr(cfg.models, role)); assign in source target order to (mid, via, _).
    // Source: vvaharness/orchestrator/scan.py:548-548
    End this invocation with source_template_548_15.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/orchestrator/scan.py:551-555
  In source order: Evaluate once {role: resolve_model(m)[0] for role, m in _iter_model_roles(cfg)}; assign in source target order to _scan_role_models. Then Evaluate once load_pricing_cached(getattr(getattr(cfg, 'pricing', None), 'file', None)); assign in source target order to _scan_pricing. Then Evaluate once {role: resolve_model(m)[1] for role, m in _iter_model_roles(cfg)}; assign in source target order to _scan_role_vias. Then Evaluate once _config_file_sha256(args.config); assign in source target order to _scan_config_sha256.
  // Source: vvaharness/orchestrator/scan.py:557-567
  // Source signature: _save_stage_provenance(step_id: str) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _save_stage_provenance(step_id) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/orchestrator/scan.py:558-567
    In source order: Evaluate once STAGE_ROLES.get(step_id); assign in source target order to role. Then Evaluate once stage_token_bucket(step_id, TOKENS.snapshot()); assign in source target order to bucket. Then Evaluate save_stage_provenance(ckpt_dir, run_id, step_id, model=_resolve_stage_role(role, _scan_role_models), via=_resolve_stage_role(role, _scan_role_vias), config_sha256=_scan_config_sha256, tokens=bucket); retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/orchestrator/scan.py:570-570
  In source order: Evaluate once load_ckpt(ckpt_dir, run_id, 's0') if args.resume else None; assign in source target order to seed.
  // Source: vvaharness/orchestrator/scan.py:571-582
  if (the source predicate seed is None is truthy) {
    // Source: vvaharness/orchestrator/scan.py:573-573
    In source order: Evaluate _sp_start('s0', 'rules'); retain side effects and discard the expression result.
    // Source: vvaharness/orchestrator/scan.py:574-576
    Enter source context managers left-to-right: stage('Step 0 — Static seed (rules)', n=0, total=11, stage_id='s0'); TOKENS.phase('s0-seed') {
      // Source: vvaharness/orchestrator/scan.py:576-576
      In source order: Evaluate once s0_seed.run(str(repo), cfg, ckpt_dir=ckpt_dir); assign in source target order to seed.
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    // Source: vvaharness/orchestrator/scan.py:577-580
    In source order: Evaluate save_ckpt(ckpt_dir, run_id, 's0', seed); retain side effects and discard the expression result. Then Evaluate _save_stage_provenance('s0'); retain side effects and discard the expression result. Then Evaluate _sp_done('s0', detail=source_template_579_31); retain side effects and discard the expression result.
  }
  else {
    // Source: vvaharness/orchestrator/scan.py:582-582
    In source order: Evaluate _sp_done('s0', outcome='cached'); retain side effects and discard the expression result.
  }
  // Source: vvaharness/orchestrator/scan.py:583-590
  In source order: Evaluate _store.save_callgraph(run_id, 's0', seed); retain side effects and discard the expression result. Then Evaluate once load_plugin_set(cfg); assign in source target order to _plugins. Then Evaluate _plugins.install_graph_tools(); retain side effects and discard the expression result. Then Evaluate once _store.ensure_state_dir('graphs', run_id, uuid4().hex); assign in source target order to graph_dir. Then Evaluate once build_graph(str(repo), run_id, graph_dir, enrichers=_plugins.contribution.enrichers); assign in source target order to graph_handle.
  // Source: vvaharness/orchestrator/scan.py:592-1072
  Perform the following protected operations {
    // Source: vvaharness/orchestrator/scan.py:593-594
    if (the source predicate args.stop_after == 's0' is truthy) {
      // Source: vvaharness/orchestrator/scan.py:594-594
      End this invocation with ScanOutcome(None, 0).
    }
    // Source: vvaharness/orchestrator/scan.py:596-596
    In source order: For ctx, assign load_ckpt(ckpt_dir, run_id, 's1') if args.resume else None; source annotation ContextPackage | None.
    // Source: vvaharness/orchestrator/scan.py:597-607
    if (the source predicate ctx is None is truthy) {
      // Source: vvaharness/orchestrator/scan.py:598-598
      In source order: Evaluate _sp_start('s1', source_template_598_28); retain side effects and discard the expression result.
      // Source: vvaharness/orchestrator/scan.py:599-602
      Enter source context managers left-to-right: stage(source_template_599_23, n=1, total=11, stage_id='s1'); TOKENS.phase('s1-preprocess') {
        // Source: vvaharness/orchestrator/scan.py:601-602
        In source order: Evaluate once s1_preprocess.run(str(repo), cfg, cves, controls, seed=seed, graph_handle=graph_handle); assign in source target order to ctx.
      }
      Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
      // Source: vvaharness/orchestrator/scan.py:603-605
      In source order: Evaluate save_ckpt(ckpt_dir, run_id, 's1', ctx); retain side effects and discard the expression result. Then Evaluate _save_stage_provenance('s1'); retain side effects and discard the expression result. Then Evaluate _sp_done('s1', detail=source_template_605_34); retain side effects and discard the expression result.
    }
    else {
      // Source: vvaharness/orchestrator/scan.py:607-607
      In source order: Evaluate _sp_done('s1', outcome='cached'); retain side effects and discard the expression result.
    }
    // Source: vvaharness/orchestrator/scan.py:608-612
    In source order: Evaluate _store.save_callgraph(run_id, 's1', ctx); retain side effects and discard the expression result. Then Evaluate once _hydrate_ctx_callgraph_from_store(run_id, ctx, 's1', 's0'); assign in source target order to ctx. Then Evaluate once app_profile; assign in source target order to ctx.app_profile. Then Evaluate once ev_collection; assign in source target order to ctx.ev_collection. Then Evaluate once graph_handle; assign in source target order to ctx.graph_handle.
    // Source: vvaharness/orchestrator/scan.py:613-614
    if (the source predicate args.stop_after == 's1' is truthy) {
      // Source: vvaharness/orchestrator/scan.py:614-614
      End this invocation with ScanOutcome(None, 0).
    }
    // Source: vvaharness/orchestrator/scan.py:617-623
    In source order: For tm, assign load_ckpt(ckpt_dir, run_id, 's2') if args.resume else None; source annotation ThreatModel | None. Then Evaluate once False; assign in source target order to s2_reran.
    // Source: vvaharness/orchestrator/scan.py:624-662
    if (the source predicate tm is None is truthy) {
      // Source: vvaharness/orchestrator/scan.py:625-625
      In source order: Evaluate once True; assign in source target order to s2_reran.
      // Source: vvaharness/orchestrator/scan.py:626-660
      Perform the following protected operations {
        // Source: vvaharness/orchestrator/scan.py:627-627
        In source order: Evaluate _sp_start('s2', source_template_627_32); retain side effects and discard the expression result.
        // Source: vvaharness/orchestrator/scan.py:628-633
        Enter source context managers left-to-right: stage(source_template_628_27, n=2, total=11, stage_id='s2'); TOKENS.phase('s2-threatmodel') {
          // Source: vvaharness/orchestrator/scan.py:631-633
          In source order: Evaluate once s2.run(str(repo), repo_name, cfg, cves, controls, ctx=ctx, app_profile=app_profile); assign in source target order to tm.
        }
        Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
        // Source: vvaharness/orchestrator/scan.py:635-639
        if (the source predicate tm.threats or tm.assets or tm.trust_boundaries is truthy) {
          // Source: vvaharness/orchestrator/scan.py:636-637
          In source order: Evaluate save_ckpt(ckpt_dir, run_id, 's2', tm); retain side effects and discard the expression result. Then Evaluate _save_stage_provenance('s2'); retain side effects and discard the expression result.
        }
        else {
          // Source: vvaharness/orchestrator/scan.py:639-639
          In source order: Evaluate COUNTERS.bump('s2_degraded'); retain side effects and discard the expression result.
        }
        // Source: vvaharness/orchestrator/scan.py:640-641
        In source order: Evaluate _sp_done('s2', detail=source_template_640_39); retain side effects and discard the expression result.
      }
      // Source: vvaharness/orchestrator/scan.py:642-648
      On the first matching source exception S2HollowAfterRetry as e, in handler order {
        // Source: vvaharness/orchestrator/scan.py:643-647
        In source order: Evaluate COUNTERS.bump('s2_degraded'); retain side effects and discard the expression result. Then Evaluate _errlog.log('s2', repo_name, str(e), reason=e.reason); retain side effects and discard the expression result. Then Evaluate _sp_done('s2', outcome='error', detail=source_template_645_55); retain side effects and discard the expression result. Then Evaluate tracker.stop_live(); retain side effects and discard the expression result. Then Evaluate console.mark('fail', source_template_647_37, lead=source_literal_647_50); retain side effects and discard the expression result.
        // Source: vvaharness/orchestrator/scan.py:648-648
        End this invocation with ScanOutcome(None, 0, exit_code=1).
      }
      // Source: vvaharness/orchestrator/scan.py:649-660
      On the first matching source exception Exception as e, in handler order {
        // Source: vvaharness/orchestrator/scan.py:650-651
        if (the source predicate is_halt_error(e) is truthy) {
          // Source: vvaharness/orchestrator/scan.py:651-651
          Raise the currently handled exception.
        }
        // Source: vvaharness/orchestrator/scan.py:652-652
        In source order: Evaluate log.warning(Event.S2_STEP_FAILED, detail=str(e)); retain side effects and discard the expression result.
        // Source: vvaharness/orchestrator/scan.py:654-655
        if (the source predicate not _errlog.already_logged(e) is truthy) {
          // Source: vvaharness/orchestrator/scan.py:655-655
          In source order: Evaluate _errlog.log('s2', repo_name, e); retain side effects and discard the expression result.
        }
        // Source: vvaharness/orchestrator/scan.py:656-660
        In source order: Evaluate _sp_done('s2', outcome='error', detail=redact(source_template_657_39)); retain side effects and discard the expression result. Then Evaluate COUNTERS.bump('s2_degraded'); retain side effects and discard the expression result. Then Evaluate once None; assign in source target order to tm.
      }
    }
    else {
      // Source: vvaharness/orchestrator/scan.py:662-662
      In source order: Evaluate _sp_done('s2', outcome='cached'); retain side effects and discard the expression result.
    }
    // Source: vvaharness/orchestrator/scan.py:664-666
    In source order: Evaluate once tm; assign in source target order to ctx.threat_model. Then Evaluate _store.save_callgraph(run_id, 's2', ctx); retain side effects and discard the expression result. Then Evaluate once _hydrate_ctx_callgraph_from_store(run_id, ctx, 's2', 's1', 's0'); assign in source target order to ctx.
    // Source: vvaharness/orchestrator/scan.py:667-668
    if (the source predicate args.stop_after == 's2' is truthy) {
      // Source: vvaharness/orchestrator/scan.py:668-668
      End this invocation with ScanOutcome(None, 0).
    }
    // Source: vvaharness/orchestrator/scan.py:671-673
    In source order: For manifest, assign load_ckpt(ckpt_dir, run_id, 's3') if args.resume and (not s2_reran) else None; source annotation TaskManifest | None. Then Evaluate once manifest is not None; assign in source target order to s3_resumed.
    // Source: vvaharness/orchestrator/scan.py:674-683
    if (the source predicate manifest is None is truthy) {
      // Source: vvaharness/orchestrator/scan.py:675-675
      In source order: Evaluate _sp_start('s3', source_template_675_28); retain side effects and discard the expression result.
      // Source: vvaharness/orchestrator/scan.py:676-678
      Enter source context managers left-to-right: stage(source_template_676_23, n=3, total=11, stage_id='s3'); TOKENS.phase('s3-decompose') {
        // Source: vvaharness/orchestrator/scan.py:678-678
        In source order: Evaluate once s3_decompose.run(ctx, cfg); assign in source target order to manifest.
      }
      Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
      // Source: vvaharness/orchestrator/scan.py:679-681
      In source order: Evaluate save_ckpt(ckpt_dir, run_id, 's3', manifest); retain side effects and discard the expression result. Then Evaluate _save_stage_provenance('s3'); retain side effects and discard the expression result. Then Evaluate _sp_done('s3', detail=source_template_681_34); retain side effects and discard the expression result.
    }
    else {
      // Source: vvaharness/orchestrator/scan.py:683-683
      In source order: Evaluate _sp_done('s3', outcome='cached'); retain side effects and discard the expression result.
    }
    // Source: vvaharness/orchestrator/scan.py:684-684
    In source order: Evaluate _store.save_callgraph(run_id, 's3', ctx); retain side effects and discard the expression result.
    // Source: vvaharness/orchestrator/scan.py:685-686
    if (the source predicate args.stop_after == 's3' is truthy) {
      // Source: vvaharness/orchestrator/scan.py:686-686
      End this invocation with ScanOutcome(None, 0).
    }
    // Source: vvaharness/orchestrator/scan.py:689-689
    In source order: Evaluate once load_ckpt(ckpt_dir, run_id, 's4') if args.resume and s3_resumed else None; assign in source target order to s4_ckpt.
    // Source: vvaharness/orchestrator/scan.py:691-697
    if (the source predicate s4_ckpt is not None and (not (isinstance(s4_ckpt, dict) and s4_stage_complete(s4_ckpt))) is truthy) {
      // Source: vvaharness/orchestrator/scan.py:692-697
      In source order: Evaluate log.warning(Event.CKPT_STAGE_DEGRADED, step='s4'); retain side effects and discard the expression result. Then Evaluate console.write(source_literal_694_16); retain side effects and discard the expression result. Then Evaluate once None; assign in source target order to s4_ckpt.
    }
    // Source: vvaharness/orchestrator/scan.py:698-700
    In source order: Evaluate once s4_ckpt is not None; assign in source target order to s4_resumed. Then For unit_outcomes, assign {}; source annotation dict[str, str]. Then Evaluate once False; assign in source target order to external_input.
    // Source: vvaharness/orchestrator/scan.py:701-718
    if (the source predicate s4_ckpt is None is truthy) {
      // Source: vvaharness/orchestrator/scan.py:702-702
      In source order: Evaluate _sp_start('s4', source_template_702_28); retain side effects and discard the expression result.
      // Source: vvaharness/orchestrator/scan.py:703-706
      Enter source context managers left-to-right: stage(source_template_703_23, n=4, total=11, stage_id='s4'); TOKENS.phase('s4-deepdive') {
        // Source: vvaharness/orchestrator/scan.py:706-706
        In source order: Evaluate once s4_deepdive.run(manifest.sorted_units(), ctx, cfg); assign in source target order to (findings, unit_outcomes).
      }
      Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
      // Source: vvaharness/orchestrator/scan.py:708-711
      In source order: Evaluate save_ckpt(ckpt_dir, run_id, 's4', {'findings': findings, 'outcomes': unit_outcomes}); retain side effects and discard the expression result. Then Evaluate _save_stage_provenance('s4'); retain side effects and discard the expression result. Then Evaluate _sp_done('s4', detail=source_template_711_34); retain side effects and discard the expression result.
    }
    else {
      // Source: vvaharness/orchestrator/scan.py:713-718
      In source order: Resolve source import from vvaharness.orchestrator.checkpoints import s4_input_kind; preserve alias and import-time effects. Then Evaluate once s4_ckpt.get('findings', []); assign in source target order to findings. Then Evaluate once s4_ckpt.get('outcomes', {}); assign in source target order to unit_outcomes. Then Evaluate once s4_input_kind(s4_ckpt) == 'external'; assign in source target order to external_input. Then Evaluate _sp_done('s4', outcome='cached'); retain side effects and discard the expression result.
    }
    // Source: vvaharness/orchestrator/scan.py:719-719
    In source order: Evaluate _store.save_callgraph(run_id, 's4', ctx); retain side effects and discard the expression result.
    // Source: vvaharness/orchestrator/scan.py:720-721
    if (the source predicate args.stop_after == 's4' is truthy) {
      // Source: vvaharness/orchestrator/scan.py:721-721
      End this invocation with ScanOutcome(None, 0).
    }
    // Source: vvaharness/orchestrator/scan.py:724-731
    In source order: Evaluate once len(findings); assign in source target order to s4_count. Then Evaluate once load_ckpt(ckpt_dir, run_id, 's7') if args.resume and s4_resumed else None; assign in source target order to s7_ckpt. Then Evaluate once ''; assign in source target order to legacy_s7_note.
    // Source: vvaharness/orchestrator/scan.py:732-830
    if (the source predicate s7_ckpt is None is truthy) {
      // Source: vvaharness/orchestrator/scan.py:734-736
      In source order: Evaluate once load_ckpt(ckpt_dir, run_id, 's5') if args.resume and s4_resumed else None; assign in source target order to s5_ckpt. Then Evaluate once s5_ckpt is not None; assign in source target order to s5_resumed.
      // Source: vvaharness/orchestrator/scan.py:737-752
      if (the source predicate s5_ckpt is None is truthy) {
        // Source: vvaharness/orchestrator/scan.py:738-738
        In source order: Evaluate _sp_start('s5', 'enrich'); retain side effects and discard the expression result.
        // Source: vvaharness/orchestrator/scan.py:739-742
        Enter source context managers left-to-right: stage('Step 5 — Enrich (snippet + evidence refs, deterministic)', n=5, total=11, stage_id='s5'); TOKENS.phase('s5-prefilter') {
          // Source: vvaharness/orchestrator/scan.py:742-742
          In source order: Evaluate once s5.run(findings, ctx, cfg); assign in source target order to (findings, pre_dropped).
        }
        Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
        // Source: vvaharness/orchestrator/scan.py:743-748
        In source order: Evaluate save_ckpt(ckpt_dir, run_id, 's5', {'findings': findings, 'pre_dropped': pre_dropped}); retain side effects and discard the expression result. Then Evaluate _save_stage_provenance('s5'); retain side effects and discard the expression result. Then Evaluate _sp_done('s5', detail=source_template_748_38); retain side effects and discard the expression result.
      }
      else {
        // Source: vvaharness/orchestrator/scan.py:750-752
        In source order: Evaluate once s5_ckpt['findings']; assign in source target order to findings. Then Evaluate once s5_ckpt['pre_dropped']; assign in source target order to pre_dropped. Then Evaluate _sp_done('s5', outcome='cached'); retain side effects and discard the expression result.
      }
      // Source: vvaharness/orchestrator/scan.py:753-754
      if (the source predicate args.stop_after == 's5' is truthy) {
        // Source: vvaharness/orchestrator/scan.py:754-754
        End this invocation with ScanOutcome(None, 0).
      }
      // Source: vvaharness/orchestrator/scan.py:757-758
      In source order: Evaluate once load_ckpt(ckpt_dir, run_id, 's6') if args.resume and s5_resumed else None; assign in source target order to s6_ckpt.
      // Source: vvaharness/orchestrator/scan.py:759-786
      if (the source predicate s6_ckpt is None is truthy) {
        // Source: vvaharness/orchestrator/scan.py:761-763
        In source order: Evaluate once _hydrate_ctx_callgraph_from_store(run_id, ctx, 's4', 's3', 's2', 's1', 's0'); assign in source target order to ctx. Then Evaluate _sp_start('s6', source_template_763_32); retain side effects and discard the expression result.
        // Source: vvaharness/orchestrator/scan.py:764-774
        Enter source context managers left-to-right: stage(source_template_764_27, n=6, total=11, stage_id='s6'); TOKENS.phase('s6-verify') {
          // Source: vvaharness/orchestrator/scan.py:766-774
          if (the source predicate getattr(ctx, 'ev_collection', None) is truthy) {
            // Source: vvaharness/orchestrator/scan.py:768-772
            In source order: Resolve source import from vvaharness.exploit_verification.verify import router as ev_router; preserve alias and import-time effects. Then Evaluate once ev_router.run(findings, ctx, cfg, run_id=run_id); assign in source target order to (verified, dropped).
          }
          else {
            // Source: vvaharness/orchestrator/scan.py:774-774
            In source order: Evaluate once s6_verify.run(findings, ctx, cfg, run_id=run_id); assign in source target order to (verified, dropped).
          }
        }
        Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
        // Source: vvaharness/orchestrator/scan.py:775-781
        In source order: Evaluate once _verified_order(verified); assign in source target order to verified. Then Evaluate save_ckpt(ckpt_dir, run_id, 's6', {'verified': verified, 'dropped': dropped}); retain side effects and discard the expression result. Then Evaluate _save_stage_provenance('s6'); retain side effects and discard the expression result. Then Evaluate _sp_done('s6', detail=source_template_781_38); retain side effects and discard the expression result.
      }
      else {
        // Source: vvaharness/orchestrator/scan.py:784-786
        In source order: Evaluate once _verified_order(s6_ckpt['verified']); assign in source target order to verified. Then Evaluate once s6_ckpt['dropped']; assign in source target order to dropped. Then Evaluate _sp_done('s6', outcome='cached'); retain side effects and discard the expression result.
      }
      // Source: vvaharness/orchestrator/scan.py:787-788
      if (the source predicate args.stop_after == 's6' is truthy) {
        // Source: vvaharness/orchestrator/scan.py:788-788
        End this invocation with ScanOutcome(None, 0).
      }
      // Source: vvaharness/orchestrator/scan.py:790-792
      In source order: Evaluate once _hydrate_ctx_callgraph_from_store(run_id, ctx, 's4', 's3', 's2', 's1', 's0'); assign in source target order to ctx. Then Evaluate _sp_start('s7', source_template_792_28); retain side effects and discard the expression result.
      // Source: vvaharness/orchestrator/scan.py:793-795
      Enter source context managers left-to-right: stage(source_template_793_23, n=7, total=11, stage_id='s7'); TOKENS.phase('s7-dedup') {
        // Source: vvaharness/orchestrator/scan.py:795-795
        In source order: Evaluate once s7_dedup.run(verified, cfg, ctx=ctx); assign in source target order to (canonical, dup_dropped).
      }
      Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
      // Source: vvaharness/orchestrator/scan.py:796-802
      In source order: Evaluate _sp_done('s7', detail=source_template_796_34); retain side effects and discard the expression result. Then Evaluate _prune_ev_replays(run_id, canonical, ctx); retain side effects and discard the expression result. Then Evaluate once len(findings); assign in source target order to s5_out_count. Then Evaluate save_ckpt(ckpt_dir, run_id, 's7', (pre_dropped, verified, dropped, canonical, dup_dropped, s5_out_count)); retain side effects and discard the expression result. Then Evaluate _save_stage_provenance('s7'); retain side effects and discard the expression result.
      // Source: vvaharness/orchestrator/scan.py:803-804
      In source order: Evaluate once source_template_803_27; assign in source target order to _resume_cmd.
      // Source: vvaharness/orchestrator/scan.py:805-806
      if (the source predicate application_id is truthy) {
        // Source: vvaharness/orchestrator/scan.py:806-806
        In source order: Apply source augmented assignment _resume_cmd += source_template_806_31 with source evaluation/in-place semantics.
      }
      // Source: vvaharness/orchestrator/scan.py:807-807
      In source order: Evaluate console.write(source_template_807_26); retain side effects and discard the expression result.
    }
    else {
      // Source: vvaharness/orchestrator/scan.py:808-830
      if (the source predicate len(s7_ckpt) == 6 is truthy) {
        // Source: vvaharness/orchestrator/scan.py:809-812
        In source order: Evaluate once s7_ckpt; assign in source target order to (pre_dropped, verified, dropped, canonical, dup_dropped, s5_out_count). Then Evaluate _sp_done('s5', outcome='cached'); retain side effects and discard the expression result. Then Evaluate _sp_done('s6', outcome='cached'); retain side effects and discard the expression result. Then Evaluate _sp_done('s7', outcome='cached'); retain side effects and discard the expression result.
      }
      else {
        // Source: vvaharness/orchestrator/scan.py:813-830
        if (the source predicate len(s7_ckpt) == 5 is truthy) {
          // Source: vvaharness/orchestrator/scan.py:814-820
          In source order: Evaluate once s7_ckpt; assign in source target order to (pre_dropped, verified, dropped, canonical, dup_dropped). Then Evaluate once None; assign in source target order to s5_out_count. Then Evaluate once 's5 post-enrich count unavailable for the finding ledger balance check (legacy checkpoint)'; assign in source target order to legacy_s7_note. Then Evaluate _sp_done('s5', outcome='cached'); retain side effects and discard the expression result. Then Evaluate _sp_done('s6', outcome='cached'); retain side effects and discard the expression result.
          // Source: vvaharness/orchestrator/scan.py:821-821
          In source order: Evaluate _sp_done('s7', outcome='cached'); retain side effects and discard the expression result.
        }
        else {
          // Source: vvaharness/orchestrator/scan.py:823-828
          In source order: Evaluate once s7_ckpt; assign in source target order to (verified, dropped, canonical, dup_dropped). Then Evaluate once []; assign in source target order to pre_dropped. Then Evaluate once None; assign in source target order to s5_out_count. Then Evaluate once 's5 drop audit unavailable (legacy checkpoint)'; assign in source target order to legacy_s7_note. Then Evaluate _sp_done('s5', outcome='cached'); retain side effects and discard the expression result.
          // Source: vvaharness/orchestrator/scan.py:829-830
          In source order: Evaluate _sp_done('s6', outcome='cached'); retain side effects and discard the expression result. Then Evaluate _sp_done('s7', outcome='cached'); retain side effects and discard the expression result.
        }
      }
    }
    // Source: vvaharness/orchestrator/scan.py:832-833
    if (the source predicate args.stop_after in ('s5', 's6') is truthy) {
      // Source: vvaharness/orchestrator/scan.py:833-833
      End this invocation with ScanOutcome(None, 0).
    }
    // Source: vvaharness/orchestrator/scan.py:834-837
    In source order: Evaluate _enrich_findings(canonical, app_info, path_prefix=path_prefix); retain side effects and discard the expression result. Then Evaluate once pre_dropped + dropped + dup_dropped; assign in source target order to all_dropped. Then Evaluate once s5_out_count if s5_out_count is not None else s4_count; assign in source target order to raw_count.
    // Source: vvaharness/orchestrator/scan.py:838-843
    if (the source predicate s5_out_count is not None is truthy) {
      // Source: vvaharness/orchestrator/scan.py:839-839
      In source order: Evaluate once _ledger_imbalance(s5_out_count, verified, dropped); assign in source target order to ledger_msg.
      // Source: vvaharness/orchestrator/scan.py:840-843
      if (the source predicate ledger_msg is truthy) {
        // Source: vvaharness/orchestrator/scan.py:841-843
        In source order: Evaluate log.warning(Event.LEDGER_IMBALANCE, detail=ledger_msg); retain side effects and discard the expression result. Then Evaluate _errlog.log('s6-verify', repo_name, ledger_msg, recovered=True); retain side effects and discard the expression result.
      }
    }
    // Source: vvaharness/orchestrator/scan.py:844-844
    In source order: Evaluate _store.save_callgraph(run_id, 's7', ctx); retain side effects and discard the expression result.
    // Source: vvaharness/orchestrator/scan.py:845-846
    if (the source predicate args.stop_after == 's7' is truthy) {
      // Source: vvaharness/orchestrator/scan.py:846-846
      End this invocation with ScanOutcome(None, 0).
    }
    // Source: vvaharness/orchestrator/scan.py:849-855
    In source order: Evaluate once _hydrate_ctx_callgraph_from_store(run_id, ctx, 's4', 's3', 's2', 's1', 's0'); assign in source target order to ctx. Then Evaluate once s7_ckpt is not None; assign in source target order to s7_resumed. Then For report, assign load_ckpt(ckpt_dir, run_id, 's8') if args.resume and s7_resumed else None; source annotation FinalReport | None.
    // Source: vvaharness/orchestrator/scan.py:856-893
    if (the source predicate report is None is truthy) {
      // Source: vvaharness/orchestrator/scan.py:857-871
      In source order: Evaluate once _metrics.now_iso(); assign in source target order to end_ts. Then Evaluate once sum((1 for d in dropped if d.reason == 'FALSE_POSITIVE')); assign in source target order to fp. Then Evaluate once _verified_counts(verified); assign in source target order to (true_pos, discovered_tp, clone_tp, ev_rescued). Then Evaluate once _metrics.build(ctx, manifest, repo_name=repo_name, start_ts=start_ts, end_ts=end_ts, raw_findings=raw_count, true_pos=true_pos, false_pos=fp, duplicates=len(dup_dropped), discovered_tp=discovered_tp, clone_tp=clone_tp, ev_rescued=ev_rescued, unit_outcomes=unit_outcomes, external_input=external_input, role_models=_scan_role_models, pricing=_scan_pricing); assign in source target order to metrics. Then Evaluate _sp_start('s8', source_template_871_28); retain side effects and discard the expression result.
      // Source: vvaharness/orchestrator/scan.py:872-877
      Enter source context managers left-to-right: stage(source_template_872_23, n=8, total=11, stage_id='s8'); TOKENS.phase('s8-chain') {
        // Source: vvaharness/orchestrator/scan.py:874-877
        In source order: Evaluate once s8_chain.run(canonical, ctx, cfg, dropped=all_dropped, raw_findings_count=raw_count, metrics=metrics); assign in source target order to report.
      }
      Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
      // Source: vvaharness/orchestrator/scan.py:879-884
      In source order: Evaluate _metrics.refresh_tokens(report.metrics, end_ts=_metrics.now_iso(), role_models=_scan_role_models, pricing=_scan_pricing); retain side effects and discard the expression result. Then Evaluate once repo_name; assign in source target order to report.repo_name. Then Evaluate once tm; assign in source target order to report.threat_model. Then Evaluate once app_profile; assign in source target order to report.app_profile. Then Evaluate once manifest.threats_without_unit_for(tm); assign in source target order to report.threats_without_unit.
      // Source: vvaharness/orchestrator/scan.py:885-886
      if (the source predicate getattr(cfg.output, 'emit_unreachable_appendix', False) is truthy) {
        // Source: vvaharness/orchestrator/scan.py:886-886
        In source order: Evaluate once manifest.unreachable_files; assign in source target order to report.unreachable_files.
      }
      // Source: vvaharness/orchestrator/scan.py:888-891
      In source order: Evaluate once _head_sha(repo); assign in source target order to report.git_sha. Then Evaluate save_ckpt(ckpt_dir, run_id, 's8', report); retain side effects and discard the expression result. Then Evaluate _save_stage_provenance('s8'); retain side effects and discard the expression result. Then Evaluate _sp_done('s8', detail=source_template_891_34); retain side effects and discard the expression result.
    }
    else {
      // Source: vvaharness/orchestrator/scan.py:893-893
      In source order: Evaluate _sp_done('s8', outcome='cached'); retain side effects and discard the expression result.
    }
    // Source: vvaharness/orchestrator/scan.py:894-894
    In source order: Evaluate _store.save_callgraph(run_id, 's8', ctx); retain side effects and discard the expression result.
    // Source: vvaharness/orchestrator/scan.py:895-899
    if (the source predicate legacy_s7_note and legacy_s7_note not in report.degraded_reason is truthy) {
      // Source: vvaharness/orchestrator/scan.py:897-899
      In source order: Evaluate once source_template_897_38 if report.degraded_reason else legacy_s7_note; assign in source target order to report.degraded_reason. Then Evaluate once True; assign in source target order to report.degraded.
    }
    // Source: vvaharness/orchestrator/scan.py:902-902
    In source order: For _starved, assign []; source annotation list[str].
    // Source: vvaharness/orchestrator/scan.py:903-914
    for each _stage_id in ('s2', 's4', 's6') {
      // Source: vvaharness/orchestrator/scan.py:904-904
      In source order: Evaluate once STAGES.snapshot().get(_stage_id); assign in source target order to _rec.
      // Source: vvaharness/orchestrator/scan.py:905-906
      if (the source predicate not _rec or _rec.get('outcome') != 'error' is truthy) {
        // Source: vvaharness/orchestrator/scan.py:906-906
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/orchestrator/scan.py:907-910
      In source order: Evaluate _starved.append(_stage_id); retain side effects and discard the expression result. Then Evaluate once _errlog.last_message_for_stage(_stage_id); assign in source target order to _msg. Then Evaluate once source_template_909_23 if _msg else source_template_910_27; assign in source target order to _clause.
      // Source: vvaharness/orchestrator/scan.py:911-914
      if (the source predicate _clause not in report.degraded_reason is truthy) {
        // Source: vvaharness/orchestrator/scan.py:912-914
        In source order: Evaluate once source_template_912_42 if report.degraded_reason else _clause; assign in source target order to report.degraded_reason. Then Evaluate once True; assign in source target order to report.degraded.
      }
    }
    // Source: vvaharness/orchestrator/scan.py:915-922
    if (the source predicate _starved is truthy) {
      // Source: vvaharness/orchestrator/scan.py:916-922
      In source order: Evaluate log.warning(Event.INVESTIGATION_STAGE_FAILED, stages=_starved, findings=len(report.findings)); retain side effects and discard the expression result. Then Evaluate console.mark('fail', source_template_918_33, lead=source_literal_922_30); retain side effects and discard the expression result.
    }
    // Source: vvaharness/orchestrator/scan.py:925-925
    In source order: Evaluate once sum((1 for v in unit_outcomes.values() if v == 'halted')); assign in source target order to _n_halted.
    // Source: vvaharness/orchestrator/scan.py:926-932
    if (the source predicate _n_halted is truthy) {
      // Source: vvaharness/orchestrator/scan.py:927-928
      In source order: Evaluate once source_template_927_23; assign in source target order to _clause.
      // Source: vvaharness/orchestrator/scan.py:929-932
      if (the source predicate _clause not in report.degraded_reason is truthy) {
        // Source: vvaharness/orchestrator/scan.py:930-932
        In source order: Evaluate once source_template_930_42 if report.degraded_reason else _clause; assign in source target order to report.degraded_reason. Then Evaluate once True; assign in source target order to report.degraded.
      }
    }
    // Source: vvaharness/orchestrator/scan.py:935-946
    In source order: Evaluate once 1 if report.degraded else 0; assign in source target order to degraded_rc. Then Evaluate once mint_case_ids(report); assign in source target order to _ids. Then Evaluate console.write(source_template_939_22 + (source_template_941_25 if _ids['collisions'] else '')); retain side effects and discard the expression result. Then Evaluate out_path.parent.mkdir(parents=True, exist_ok=True); retain side effects and discard the expression result. Then Evaluate once write_findings_json(report, repo); assign in source target order to findings_path.
    // Source: vvaharness/orchestrator/scan.py:947-957
    In source order: Evaluate console.write(source_template_947_22); retain side effects and discard the expression result. Then Evaluate once redact(report.to_markdown(posture_channel=bool(knob(cfg, 'output.posture_channel', True)), unreachable_appendix=bool(knob(cfg, 'output.emit_unreachable_appendix', False)))); assign in source target order to md_text. Then Evaluate out_path.write_text(md_text, encoding='utf-8'); retain side effects and discard the expression result. Then Evaluate once sum(getattr(redact, 'last_counts', {}).values()); assign in source target order to n_redacted. Then Evaluate console.write(source_template_955_22 + (source_template_956_25 if n_redacted else '')); retain side effects and discard the expression result.
    // Source: vvaharness/orchestrator/scan.py:958-959
    if (the source predicate args.stop_after == 's8' is truthy) {
      // Source: vvaharness/orchestrator/scan.py:959-959
      End this invocation with ScanOutcome(out_path, len(report.findings), rem_rc or degraded_rc).
    }
    // Source: vvaharness/orchestrator/scan.py:961-961
    In source order: Evaluate once load_ckpt(ckpt_dir, run_id, 's9') if args.resume else None; assign in source target order to s9_done.
    // Source: vvaharness/orchestrator/scan.py:962-973
    if (the source predicate s9_done is None or not sarif_path.exists() is truthy) {
      // Source: vvaharness/orchestrator/scan.py:963-963
      In source order: Evaluate _sp_start('s9', 'sarif'); retain side effects and discard the expression result.
      // Source: vvaharness/orchestrator/scan.py:964-968
      Enter source context managers left-to-right: stage(source_template_964_23, n=9, total=11, stage_id='s9') {
        // Source: vvaharness/orchestrator/scan.py:966-968
        In source order: Evaluate s9_sarif.run(report, sarif_path, application_id=application_id, app_info=app_info, cfg=cfg); retain side effects and discard the expression result.
      }
      Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
      // Source: vvaharness/orchestrator/scan.py:969-971
      In source order: Evaluate console.write(source_template_969_26); retain side effects and discard the expression result. Then Evaluate save_ckpt(ckpt_dir, run_id, 's9', str(sarif_path)); retain side effects and discard the expression result. Then Evaluate _sp_done('s9', detail=source_template_971_34); retain side effects and discard the expression result.
    }
    else {
      // Source: vvaharness/orchestrator/scan.py:973-973
      In source order: Evaluate _sp_done('s9', outcome='cached'); retain side effects and discard the expression result.
    }
    // Source: vvaharness/orchestrator/scan.py:974-977
    In source order: Evaluate _store.save_callgraph(run_id, 's9', ctx); retain side effects and discard the expression result. Then Evaluate once load_ckpt(ckpt_dir, run_id, 'ingest') if args.resume else None; assign in source target order to ingest_done.
    // Source: vvaharness/orchestrator/scan.py:978-990
    if (the source predicate ingest_done is truthy) {
      // Source: vvaharness/orchestrator/scan.py:979-979
      In source order: Evaluate console.write('  [ingest] already uploaded (checkpoint) - skipping'); retain side effects and discard the expression result.
    }
    else {
      // Source: vvaharness/orchestrator/scan.py:981-988
      In source order: Evaluate once _upload_to_ingest(out_path, sarif_path, repository_name=repo_name, application_id=application_id, cfg=cfg, cfg_dir=cfg_dir); assign in source target order to ok.
      // Source: vvaharness/orchestrator/scan.py:989-990
      if (the source predicate ok is truthy) {
        // Source: vvaharness/orchestrator/scan.py:990-990
        In source order: Evaluate save_ckpt(ckpt_dir, run_id, 'ingest', True); retain side effects and discard the expression result.
      }
    }
    // Source: vvaharness/orchestrator/scan.py:992-993
    if (the source predicate args.stop_after == 's9' is truthy) {
      // Source: vvaharness/orchestrator/scan.py:993-993
      End this invocation with ScanOutcome(out_path, len(report.findings), rem_rc or degraded_rc).
    }
    // Source: vvaharness/orchestrator/scan.py:996-998
    In source order: Evaluate once getattr(cfg, 'step_remediate', None); assign in source target order to rem_cfg. Then Evaluate once bool(getattr(args, 'remediate', False) or getattr(rem_cfg, 'enabled', False)); assign in source target order to rem_on.
    // Source: vvaharness/orchestrator/scan.py:1000-1022
    if (the source predicate not (rem_on and report.findings) is truthy) {
      // Source: vvaharness/orchestrator/scan.py:1001-1001
      In source order: Evaluate _sp_done('s10', outcome='disabled'); retain side effects and discard the expression result.
    }
    else {
      // Source: vvaharness/orchestrator/scan.py:1003-1003
      In source order: Evaluate once _remediate_preflight(cfg, args, repo, report); assign in source target order to rem_err.
      // Source: vvaharness/orchestrator/scan.py:1004-1022
      if (the source predicate rem_err is truthy) {
        // Source: vvaharness/orchestrator/scan.py:1005-1007
        In source order: Evaluate console.write(source_template_1005_30); retain side effects and discard the expression result. Then Evaluate _errlog.log('s10.preflight', repo_name, RuntimeError(rem_err)); retain side effects and discard the expression result. Then Evaluate _sp_done('s10', outcome='disabled'); retain side effects and discard the expression result.
      }
      else {
        // Source: vvaharness/orchestrator/scan.py:1009-1010
        In source order: For rem_progress, assign {}; source annotation dict[str, int]. Then Evaluate _sp_start('s10', source_template_1010_33); retain side effects and discard the expression result.
        // Source: vvaharness/orchestrator/scan.py:1011-1018
        Enter source context managers left-to-right: stage(source_template_1011_27, n=10, total=11, stage_id='s10'); TOKENS.phase('s10-remediate') {
          // Source: vvaharness/orchestrator/scan.py:1014-1018
          In source order: Evaluate once _run_remediation(report, repo, cfg, ckpt_dir, run_id, resume=args.resume, top=getattr(args, 'top', None), report_md=out_path, progress=rem_progress); assign in source target order to rem_rc.
        }
        Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
        // Source: vvaharness/orchestrator/scan.py:1019-1020
        In source order: Evaluate _sp_done('s10', detail=_progress_detail(rem_progress, 'attempted', 'fixed', 'not_fixed')); retain side effects and discard the expression result.
        // Source: vvaharness/orchestrator/scan.py:1021-1022
        if (the source predicate rem_rc is truthy) {
          // Source: vvaharness/orchestrator/scan.py:1022-1022
          In source order: Evaluate log.warning(Event.REMEDIATION_INCOMPLETE, exit_code=rem_rc); retain side effects and discard the expression result.
        }
      }
    }
    // Source: vvaharness/orchestrator/scan.py:1024-1025
    if (the source predicate args.stop_after == 's10' is truthy) {
      // Source: vvaharness/orchestrator/scan.py:1025-1025
      End this invocation with ScanOutcome(out_path, len(report.findings), rem_rc or degraded_rc).
    }
    // Source: vvaharness/orchestrator/scan.py:1028-1030
    In source order: Evaluate once 0; assign in source target order to val_rc. Then Evaluate once getattr(cfg, 'step_validate', None); assign in source target order to val_cfg. Then Evaluate once bool(getattr(val_cfg, 'enabled', False)); assign in source target order to val_on.
    // Source: vvaharness/orchestrator/scan.py:1032-1049
    if (the source predicate not (val_on and report.findings) is truthy) {
      // Source: vvaharness/orchestrator/scan.py:1033-1033
      In source order: Evaluate _sp_done('s11', outcome='disabled'); retain side effects and discard the expression result.
    }
    else {
      // Source: vvaharness/orchestrator/scan.py:1035-1035
      In source order: Evaluate once _validate_preflight(cfg); assign in source target order to val_err.
      // Source: vvaharness/orchestrator/scan.py:1036-1049
      if (the source predicate val_err is truthy) {
        // Source: vvaharness/orchestrator/scan.py:1037-1039
        In source order: Evaluate console.write(source_template_1037_30); retain side effects and discard the expression result. Then Evaluate _errlog.log('s11.preflight', repo_name, RuntimeError(val_err)); retain side effects and discard the expression result. Then Evaluate _sp_done('s11', outcome='disabled'); retain side effects and discard the expression result.
      }
      else {
        // Source: vvaharness/orchestrator/scan.py:1041-1042
        In source order: For val_progress, assign {}; source annotation dict[str, int]. Then Evaluate _sp_start('s11', 'validation'); retain side effects and discard the expression result.
        // Source: vvaharness/orchestrator/scan.py:1043-1047
        Enter source context managers left-to-right: stage('Step 11 — Validate (s11)', n=11, total=11, stage_id='s11'); TOKENS.phase('s11-validate') {
          // Source: vvaharness/orchestrator/scan.py:1045-1047
          In source order: Evaluate once _run_validation(repo, cfg, config_path=args.config, resume=args.resume, report_md=out_path, progress=val_progress); assign in source target order to val_rc.
        }
        Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
        // Source: vvaharness/orchestrator/scan.py:1048-1049
        In source order: Evaluate _sp_done('s11', detail=_progress_detail(val_progress, 'validated', 'passed', 'failed')); retain side effects and discard the expression result.
      }
    }
    // Source: vvaharness/orchestrator/scan.py:1050-1052
    if (the source predicate args.stop_after == 's11' is truthy) {
      // Source: vvaharness/orchestrator/scan.py:1052-1052
      End this invocation with ScanOutcome(out_path, len(report.findings), rem_rc or val_rc or degraded_rc).
    }
    // Source: vvaharness/orchestrator/scan.py:1054-1060
    In source order: Evaluate once time.time() - t0; assign in source target order to elapsed. Then Evaluate console.write(source_template_1055_22); retain side effects and discard the expression result. Then Evaluate once report.metrics; assign in source target order to m. Then Evaluate once m.prompt_tokens if m and m.prompt_tokens is not None else 'unavailable'; assign in source target order to tok_p. Then Evaluate once m.completion_tokens if m and m.completion_tokens is not None else 'unavailable'; assign in source target order to tok_c.
    // Source: vvaharness/orchestrator/scan.py:1061-1065
    In source order: Evaluate once m.total_tokens if m and m.total_tokens is not None else 'unavailable'; assign in source target order to tok_t. Then Evaluate console.write(source_template_1062_22); retain side effects and discard the expression result. Then Evaluate console.write(source_template_1063_22); retain side effects and discard the expression result. Then Evaluate print(md_text); retain side effects and discard the expression result.
    // Source: vvaharness/orchestrator/scan.py:1066-1066
    End this invocation with ScanOutcome(out_path, len(report.findings), rem_rc or val_rc or degraded_rc).
  }
  On every exit from this protected/handler/normal-completion region {
    // Source: vvaharness/orchestrator/scan.py:1068-1068
    In source order: Evaluate tracker.stop_live(); retain side effects and discard the expression result.
    // Source: vvaharness/orchestrator/scan.py:1069-1070
    if (the source predicate graph_handle is truthy) {
      // Source: vvaharness/orchestrator/scan.py:1070-1070
      In source order: Evaluate graph_handle.close(); retain side effects and discard the expression result.
    }
    // Source: vvaharness/orchestrator/scan.py:1072-1072
    In source order: Evaluate shutil.rmtree(graph_dir, ignore_errors=True); retain side effects and discard the expression result.
  }
  If execution reaches this end, finish with the source implicit None result.
}
At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
// Source: vvaharness/orchestrator/scan.py:1075-1126
// Source signature: _run_remediation(report: FinalReport, repo: Path, cfg, ckpt_dir, run_id, *, resume: bool=False, top: int | None=None, report_md: Path | None=None, progress: MutableMapping[str, int] | None=None) -> int
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _run_remediation(report, repo, cfg, ckpt_dir, run_id, resume, top, report_md, progress) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/scan.py:1079-1083
  In source order: Retain source documentation literal source_literal_1079_4; it is not a model call. Then Resolve source import from vvaharness.remediation_agent.discovery import Layout; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.options import RemediateOptions; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.report_parser import REMEDIATION_DIR_NAME; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.runner import process_targets; preserve alias and import-time effects.
  // Source: vvaharness/orchestrator/scan.py:1084-1096
  In source order: Resolve source import from vvaharness.remediation_agent.select import drop_non_main_channel, resolve_top, select_top_logged; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.target import RemediationTarget; preserve alias and import-time effects. Then Evaluate once artifact_dir(repo, REMEDIATION_DIR_NAME); assign in source target order to rem_dir. Then Evaluate rem_dir.mkdir(exist_ok=True); retain side effects and discard the expression result. Then Evaluate once resolve_top(top, cfg); assign in source target order to eff_top.
  // Source: vvaharness/orchestrator/scan.py:1098-1106
  In source order: Evaluate once select_top_logged(drop_non_main_channel(report.findings, log_prefix='[s10]'), eff_top, score_of=lambda rf: rf.finding.cvss_score, log_prefix='[s10]'); assign in source target order to selected. Then Evaluate once [rf.finding for rf in selected]; assign in source target order to findings. Then Evaluate once resolve_model(cfg.models.remediate); assign in source target order to (_, _remediate_via, _).
  // Source: vvaharness/orchestrator/scan.py:1107-1114
  if (the source predicate _remediate_via in ('cli', 'sdk', 'deepagents') is truthy) {
    // Source: vvaharness/orchestrator/scan.py:1108-1109
    In source order: Evaluate console.mark('warn', source_template_1108_29); retain side effects and discard the expression result.
  }
  else {
    // Source: vvaharness/orchestrator/scan.py:1111-1114
    In source order: Evaluate console.mark('warn', source_template_1112_21); retain side effects and discard the expression result.
  }
  // Source: vvaharness/orchestrator/scan.py:1115-1124
  In source order: Evaluate console.write(source_template_1115_18); retain side effects and discard the expression result. Then Evaluate once Layout(rem_dir=rem_dir, ckpt_dir=ckpt_dir, run_id=run_id); assign in source target order to layout. Then Evaluate once RemediateOptions(resume=resume, mode='fix'); assign in source target order to opts. Then Evaluate once [RemediationTarget(finding=f, index=i) for i, f in enumerate(findings, start=1)]; assign in source target order to targets. Then Evaluate once {'progress': progress} if progress is not None else {}; assign in source target order to kwargs.
  // Source: vvaharness/orchestrator/scan.py:1125-1126
  End this invocation with process_targets(targets, layout=layout, cfg=cfg, repo_path=repo, opts=opts, report=report_md, **kwargs).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/scan.py:1129-1139
// Source signature: _run_validation(repo: Path, cfg, *, config_path: str, resume: bool=False, report_md: Path | None=None, progress: MutableMapping[str, int] | None=None) -> int
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _run_validation(repo, cfg, config_path, resume, report_md, progress) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/scan.py:1132-1136
  In source order: Retain source documentation literal source_literal_1132_4; it is not a model call. Then Resolve source import from vvaharness.pipeline.stages.s11_validate import run as s11_run; preserve alias and import-time effects. Then Evaluate once {'progress': progress} if progress is not None else {}; assign in source target order to kwargs. Then Evaluate once s11_run(repo, cfg=cfg, config_path=config_path, resume=resume, report_md=report_md, **kwargs); assign in source target order to rc.
  // Source: vvaharness/orchestrator/scan.py:1137-1138
  if (the source predicate rc != 0 is truthy) {
    // Source: vvaharness/orchestrator/scan.py:1138-1138
    In source order: Evaluate log.warning(Event.VALIDATION_NONZERO_EXIT, exit_code=rc); retain side effects and discard the expression result.
  }
  // Source: vvaharness/orchestrator/scan.py:1139-1139
  End this invocation with rc.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/scan.py:1142-1144
// Source signature: _progress_detail(progress: MutableMapping[str, int], *fields: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _progress_detail(progress, fields) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/scan.py:1143-1143
  In source order: Retain source documentation literal source_literal_1143_4; it is not a model call.
  // Source: vvaharness/orchestrator/scan.py:1144-1144
  End this invocation with ' '.join((source_template_1144_20 for field in fields)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/scan.py:1147-1172
// Source signature: _remediate_preflight(cfg, args, repo: Path, report) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _remediate_preflight(cfg, args, repo, report) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/scan.py:1148-1149
  In source order: Retain source documentation literal source_literal_1148_4; it is not a model call. Then Evaluate once getattr(cfg.models, 'remediate', None); assign in source target order to rem.
  // Source: vvaharness/orchestrator/scan.py:1150-1151
  if (the source predicate rem is None is truthy) {
    // Source: vvaharness/orchestrator/scan.py:1151-1151
    End this invocation with 'models.remediate must be set'.
  }
  // Source: vvaharness/orchestrator/scan.py:1153-1153
  In source order: Resolve source import from vvaharness.remediation_agent.report_parser import REMEDIATION_DIR_NAME; preserve alias and import-time effects.
  // Source: vvaharness/orchestrator/scan.py:1154-1157
  Perform the following protected operations {
    // Source: vvaharness/orchestrator/scan.py:1155-1155
    In source order: Evaluate artifact_dir(repo, REMEDIATION_DIR_NAME); retain side effects and discard the expression result.
  }
  // Source: vvaharness/orchestrator/scan.py:1156-1157
  On the first matching source exception UnsafeArtifactDir as exc, in handler order {
    // Source: vvaharness/orchestrator/scan.py:1157-1157
    End this invocation with str(exc).
  }
  // Source: vvaharness/orchestrator/scan.py:1160-1162
  In source order: Resolve source import from vvaharness.util.environment import _backend_credential_ok; preserve alias and import-time effects. Then Evaluate once resolve_model(rem); assign in source target order to (model_id, via, _). Then Evaluate once _backend_credential_ok(via, model_id, getattr(rem, 'provider', None)); assign in source target order to (ready, detail).
  // Source: vvaharness/orchestrator/scan.py:1163-1164
  if (the source predicate not ready is truthy) {
    // Source: vvaharness/orchestrator/scan.py:1164-1164
    End this invocation with source_template_1164_15.
  }
  // Source: vvaharness/orchestrator/scan.py:1167-1167
  In source order: Evaluate once _head_sha(repo); assign in source target order to cur.
  // Source: vvaharness/orchestrator/scan.py:1168-1171
  if (the source predicate report.git_sha and cur and (report.git_sha != cur) and (not getattr(args, 'force', False)) is truthy) {
    // Source: vvaharness/orchestrator/scan.py:1170-1171
    End this invocation with source_template_1170_16.
  }
  // Source: vvaharness/orchestrator/scan.py:1172-1172
  End this invocation with None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/scan.py:1175-1193
// Source signature: _validate_preflight(cfg: object) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _validate_preflight(cfg) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/scan.py:1176-1184
  In source order: Retain source documentation literal source_literal_1176_4; it is not a model call. Then Resolve source import from vvaharness.util.environment import _backend_credential_ok; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.config.validate_role import normalize_validate_backend, validate_model_spec; preserve alias and import-time effects. Then Evaluate once validate_model_spec(cfg); assign in source target order to val.
  // Source: vvaharness/orchestrator/scan.py:1185-1186
  if (the source predicate val is None is truthy) {
    // Source: vvaharness/orchestrator/scan.py:1186-1186
    End this invocation with 'models.validate.orchestrator must be set'.
  }
  // Source: vvaharness/orchestrator/scan.py:1188-1192
  In source order: Evaluate once resolve_model(val); assign in source target order to (model_id, via, _). Then Evaluate once normalize_validate_backend(via, getattr(val, 'provider', None)); assign in source target order to (via, provider). Then Evaluate once _backend_credential_ok(via, model_id, provider); assign in source target order to (ready, detail).
  // Source: vvaharness/orchestrator/scan.py:1193-1193
  End this invocation with None if ready else source_template_1193_30.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.util import logs` at source line 15: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import logs` at source line 15: `source_detail/vvaharness/util/logs.py.sudo.md`.
- `from vvaharness import config as config_mod` at source line 33: `source_detail/vvaharness/__init__.py.sudo.md`.
- `from vvaharness import config as config_mod` at source line 33: `source_detail/vvaharness/config/__init__.py.sudo.md`.
- `from vvaharness.backends.harness.models import is_halt_error` at source line 34: `source_detail/vvaharness/backends/harness/models.py.sudo.md`.
- `from vvaharness.backends.llm.registry import resolve as resolve_model` at source line 35: `source_detail/vvaharness/backends/llm/registry.py.sudo.md`.
- `from vvaharness.backends.llm.tls import coerce_verify` at source line 36: `source_detail/vvaharness/backends/llm/tls.py.sudo.md`.
- `from vvaharness.codegraph import build_graph` at source line 37: `source_detail/vvaharness/codegraph/__init__.py.sudo.md`.
- `from vvaharness.injectors.cve_feed import load_cves` at source line 38: `source_detail/vvaharness/injectors/cve_feed.py.sudo.md`.
- `from vvaharness.injectors.design_controls import load_controls` at source line 39: `source_detail/vvaharness/injectors/design_controls.py.sudo.md`.
- `from vvaharness.models import ContextPackage, FinalReport, Finding, TaskManifest, ThreatModel` at source line 40: `source_detail/vvaharness/models/__init__.py.sudo.md`.
- `from vvaharness.orchestrator import store as _store` at source line 47: `source_detail/vvaharness/orchestrator/__init__.py.sudo.md`.
- `from vvaharness.orchestrator import store as _store` at source line 47: `source_detail/vvaharness/orchestrator/store/__init__.py.sudo.md`.
- `from vvaharness.orchestrator.artifacts import SCAN_DIR_NAME, UnsafeArtifactDir, artifact_dir` at source line 48: `source_detail/vvaharness/orchestrator/artifacts.py.sudo.md`.
- `from vvaharness.orchestrator.case_ids import mint_case_ids` at source line 53: `source_detail/vvaharness/orchestrator/case_ids.py.sudo.md`.
- `from vvaharness.orchestrator.checkpoints import EV_COLLECTION_STEP, REPO_IDENTITY_STEP, load_ckpt, load_stage_provenance, run_id_for, s4_stage_complete, save_ckpt, save_stage_provenance` at source line 54: `source_detail/vvaharness/orchestrator/checkpoints.py.sudo.md`.
- `from vvaharness.orchestrator.cmdb import _load_app_profile` at source line 64: `source_detail/vvaharness/orchestrator/cmdb.py.sudo.md`.
- `from vvaharness.orchestrator.config_paths import _iter_model_roles, _resolve_against` at source line 65: `source_detail/vvaharness/orchestrator/config_paths.py.sudo.md`.
- `from vvaharness.orchestrator.enrich_findings import _enrich_findings` at source line 66: `source_detail/vvaharness/orchestrator/enrich_findings.py.sudo.md`.
- `from vvaharness.orchestrator.findings_json import write_findings_json` at source line 67: `source_detail/vvaharness/orchestrator/findings_json.py.sudo.md`.
- `from vvaharness.pipeline.stages import s0_seed, s1_autoexclude, s1_preprocess, s2, s3_decompose, s4_deepdive, s5, s6_verify, s7_dedup, s8_chain, s9_sarif` at source line 68: `source_detail/vvaharness/pipeline/stages/s0_seed.py.sudo.md`.
- `from vvaharness.pipeline.stages import s0_seed, s1_autoexclude, s1_preprocess, s2, s3_decompose, s4_deepdive, s5, s6_verify, s7_dedup, s8_chain, s9_sarif` at source line 68: `source_detail/vvaharness/pipeline/stages/s1_autoexclude.py.sudo.md`.
- `from vvaharness.pipeline.stages import s0_seed, s1_autoexclude, s1_preprocess, s2, s3_decompose, s4_deepdive, s5, s6_verify, s7_dedup, s8_chain, s9_sarif` at source line 68: `source_detail/vvaharness/pipeline/stages/s1_preprocess.py.sudo.md`.
- `from vvaharness.pipeline.stages import s0_seed, s1_autoexclude, s1_preprocess, s2, s3_decompose, s4_deepdive, s5, s6_verify, s7_dedup, s8_chain, s9_sarif` at source line 68: `source_detail/vvaharness/pipeline/stages/s2/__init__.py.sudo.md`.
- `from vvaharness.pipeline.stages import s0_seed, s1_autoexclude, s1_preprocess, s2, s3_decompose, s4_deepdive, s5, s6_verify, s7_dedup, s8_chain, s9_sarif` at source line 68: `source_detail/vvaharness/pipeline/stages/s3_decompose.py.sudo.md`.
- `from vvaharness.pipeline.stages import s0_seed, s1_autoexclude, s1_preprocess, s2, s3_decompose, s4_deepdive, s5, s6_verify, s7_dedup, s8_chain, s9_sarif` at source line 68: `source_detail/vvaharness/pipeline/stages/s4_deepdive.py.sudo.md`.
- `from vvaharness.pipeline.stages import s0_seed, s1_autoexclude, s1_preprocess, s2, s3_decompose, s4_deepdive, s5, s6_verify, s7_dedup, s8_chain, s9_sarif` at source line 68: `source_detail/vvaharness/pipeline/stages/s5/__init__.py.sudo.md`.
- `from vvaharness.pipeline.stages import s0_seed, s1_autoexclude, s1_preprocess, s2, s3_decompose, s4_deepdive, s5, s6_verify, s7_dedup, s8_chain, s9_sarif` at source line 68: `source_detail/vvaharness/pipeline/stages/s6_verify.py.sudo.md`.
- `from vvaharness.pipeline.stages import s0_seed, s1_autoexclude, s1_preprocess, s2, s3_decompose, s4_deepdive, s5, s6_verify, s7_dedup, s8_chain, s9_sarif` at source line 68: `source_detail/vvaharness/pipeline/stages/s7_dedup.py.sudo.md`.
- `from vvaharness.pipeline.stages import s0_seed, s1_autoexclude, s1_preprocess, s2, s3_decompose, s4_deepdive, s5, s6_verify, s7_dedup, s8_chain, s9_sarif` at source line 68: `source_detail/vvaharness/pipeline/stages/s8_chain.py.sudo.md`.
- `from vvaharness.pipeline.stages import s0_seed, s1_autoexclude, s1_preprocess, s2, s3_decompose, s4_deepdive, s5, s6_verify, s7_dedup, s8_chain, s9_sarif` at source line 68: `source_detail/vvaharness/pipeline/stages/s9_sarif.py.sudo.md`.
- `from vvaharness.report.redact import redact` at source line 81: `source_detail/vvaharness/report/redact.py.sudo.md`.
- `from vvaharness.sdk.loading import load_plugin_set` at source line 82: `source_detail/vvaharness/sdk/loading.py.sudo.md`.
- `from vvaharness.skills import with_injected_skills` at source line 83: `source_detail/vvaharness/skills/__init__.py.sudo.md`.
- `from vvaharness.util import console` at source line 84: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import console` at source line 84: `source_detail/vvaharness/util/console.py.sudo.md`.
- `from vvaharness.util import errlog as _errlog` at source line 85: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import errlog as _errlog` at source line 85: `source_detail/vvaharness/util/errlog.py.sudo.md`.
- `from vvaharness.util.exceptions import S2HollowAfterRetry` at source line 86: `source_detail/vvaharness/util/exceptions.py.sudo.md`.
- `from vvaharness.util import metrics as _metrics` at source line 87: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import metrics as _metrics` at source line 87: `source_detail/vvaharness/util/metrics.py.sudo.md`.
- `from vvaharness.util.config import knob` at source line 88: `source_detail/vvaharness/util/config.py.sudo.md`.
- `from vvaharness.util.counters import COUNTERS` at source line 89: `source_detail/vvaharness/util/counters.py.sudo.md`.
- `from vvaharness.util.pricing import load_pricing_cached` at source line 90: `source_detail/vvaharness/util/pricing.py.sudo.md`.
- `from vvaharness.util.scan_progress import ScanProgress, set_active_tracker` at source line 91: `source_detail/vvaharness/util/scan_progress.py.sudo.md`.
- `from vvaharness.util.stage_telemetry import CACHED_PROVENANCE, STAGE_ROLES, STAGES, stage_token_bucket` at source line 92: `source_detail/vvaharness/util/stage_telemetry.py.sudo.md`.
- `from vvaharness.util.stage_telemetry import _resolve_model as _resolve_stage_role` at source line 98: `source_detail/vvaharness/util/stage_telemetry.py.sudo.md`.
- `from vvaharness.util.status import stage` at source line 99: `source_detail/vvaharness/util/status.py.sudo.md`.
- `from vvaharness.util.tokens import TOKENS` at source line 100: `source_detail/vvaharness/util/tokens.py.sudo.md`.
- `from vvaharness.util.events import Event` at source line 101: `source_detail/vvaharness/util/events.py.sudo.md`.
- `from vvaharness.exploit_verification import options as ev_options` at source line 189: `source_detail/vvaharness/exploit_verification/__init__.py.sudo.md`.
- `from vvaharness.exploit_verification import options as ev_options` at source line 189: `source_detail/vvaharness/exploit_verification/options.py.sudo.md`.
- `from vvaharness.exploit_verification import options as ev_options` at source line 218: `source_detail/vvaharness/exploit_verification/__init__.py.sudo.md`.
- `from vvaharness.exploit_verification import options as ev_options` at source line 218: `source_detail/vvaharness/exploit_verification/options.py.sudo.md`.
- `from vvaharness.exploit_verification import probe as ev_probe` at source line 219: `source_detail/vvaharness/exploit_verification/__init__.py.sudo.md`.
- `from vvaharness.exploit_verification import probe as ev_probe` at source line 219: `source_detail/vvaharness/exploit_verification/probe.py.sudo.md`.
- `from vvaharness.exploit_verification.errors import EVInputError` at source line 220: `source_detail/vvaharness/exploit_verification/errors.py.sudo.md`.
- `from vvaharness.exploit_verification.executor.oob import resolve_oob` at source line 267: `source_detail/vvaharness/exploit_verification/executor/oob.py.sudo.md`.
- `from vvaharness.remediation_agent.discovery import Layout` at source line 1080: `source_detail/vvaharness/remediation_agent/discovery.py.sudo.md`.
- `from vvaharness.remediation_agent.options import RemediateOptions` at source line 1081: `source_detail/vvaharness/remediation_agent/options.py.sudo.md`.
- `from vvaharness.remediation_agent.report_parser import REMEDIATION_DIR_NAME` at source line 1082: `source_detail/vvaharness/remediation_agent/report_parser/__init__.py.sudo.md`.
- `from vvaharness.remediation_agent.runner import process_targets` at source line 1083: `source_detail/vvaharness/remediation_agent/runner.py.sudo.md`.
- `from vvaharness.remediation_agent.select import drop_non_main_channel, resolve_top, select_top_logged` at source line 1084: `source_detail/vvaharness/remediation_agent/select/__init__.py.sudo.md`.
- `from vvaharness.remediation_agent.target import RemediationTarget` at source line 1089: `source_detail/vvaharness/remediation_agent/target.py.sudo.md`.
- `from vvaharness.pipeline.stages.s11_validate import run as s11_run` at source line 1133: `source_detail/vvaharness/pipeline/stages/s11_validate.py.sudo.md`.
- `from vvaharness.remediation_agent.report_parser import REMEDIATION_DIR_NAME` at source line 1153: `source_detail/vvaharness/remediation_agent/report_parser/__init__.py.sudo.md`.
- `from vvaharness.util.environment import _backend_credential_ok` at source line 1160: `source_detail/vvaharness/util/environment.py.sudo.md`.
- `from vvaharness.util.environment import _backend_credential_ok` at source line 1178: `source_detail/vvaharness/util/environment.py.sudo.md`.
- `from vvaharness.validation.config.validate_role import normalize_validate_backend, validate_model_spec` at source line 1179: `source_detail/vvaharness/validation/config/validate_role.py.sudo.md`.
- `from vvaharness.exploit_verification.verify.router import replay_key` at source line 177: `source_detail/vvaharness/exploit_verification/verify/router.py.sudo.md`.
- `from vvaharness.exploit_verification import gate as ev_gate` at source line 246: `source_detail/vvaharness/exploit_verification/__init__.py.sudo.md`.
- `from vvaharness.exploit_verification import gate as ev_gate` at source line 246: `source_detail/vvaharness/exploit_verification/gate.py.sudo.md`.
- `from vvaharness.orchestrator.checkpoints import s4_input_kind` at source line 713: `source_detail/vvaharness/orchestrator/checkpoints.py.sudo.md`.
- `from vvaharness.exploit_verification.verify import router as ev_router` at source line 768: `source_detail/vvaharness/exploit_verification/verify/__init__.py.sudo.md`.
- `from vvaharness.exploit_verification.verify import router as ev_router` at source line 768: `source_detail/vvaharness/exploit_verification/verify/router.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../prompt_representation/vvaharness/orchestrator/scan.py.sudo.md). Exact strings in the evidence asset support this conversion.
